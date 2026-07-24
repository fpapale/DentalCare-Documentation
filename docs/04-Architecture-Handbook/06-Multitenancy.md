# 06 — Multi-tenancy

## 1. Modello: schema-per-tenant

**Un tenant = uno schema PostgreSQL** `t_<8hex>` (es. `t_9d754153`). Lo schema
globale `dentalcare` ospita enum, funzioni e il registro dei tenant. Un unico
database (`dentalcare_prod`), N schemi.

Lo schema è derivato dai primi 8 caratteri esadecimali del `clinicId` della
clinica **iniziale** creata al provisioning, ma rappresenta il **tenant**, non
la singola clinica: un tenant può avere **più cliniche/sedi**, tutte nello stesso
schema (mappate via `dentalcare.tenant_clinics`).

### 1.1 Terminologia (convenzione ufficiale)

| Livello | Cos'è | Dove |
|---|---|---|
| **Tenant** | Account/abbonamento = lo studio come entità. Titolare del trattamento. 1 schema dedicato | `dentalcare.tenants` + `t_XXXX` |
| **Clinica / sede** | Sede fisica del tenant (`clinic` = `clinica` = `sede`, sinonimi). **1..N per tenant** | `clinics` + `dentalcare.tenant_clinics` |
| **Provider** | Medici e personale | `providers` |

- Chi crea l'account è il **`TENANT_ADMIN`**: possiede il tenant e amministra
  **tutte** le sue cliniche (`createClinic`/`updateClinic`/`deleteClinic`). **Non
  esiste** un ruolo "amministratore di singola clinica": l'amministrazione è al
  livello del tenant.
- **`ADMIN` ≠ `TENANT_ADMIN`**: `ADMIN` è legacy/di servizio (tenant demo +
  service-token n8n), non il ruolo di un cliente reale.
- Evitare la parola **"studio"** da sola: ambigua (a volte = tenant, a volte =
  sede). Usare "tenant" o "sede del tenant".

## 2. Contesto tenant

- **`TenantContext`**: thread-local con schema, clinicId e **ruolo** correnti
  (`getCurrentRole()`). `validatedSchema()` restituisce lo schema **validato via
  regex** `^t_[0-9a-f]{8}$` — usato in ogni query. Il tenant non è **mai** preso
  dall'input client: deriva dal JWT.
- **`JwtAuthenticationFilter`**: a ogni richiesta valida il token e popola
  `SecurityContext` + `TenantContext` (schema, clinicId, ruolo dai claim).
- **`TenantSchemaRegistry`**: mappa `clinicId → schema` caricata all'avvio;
  usata dal flusso di login/impersonazione.

## 3. Isolamento dei dati

- Ogni query di servizio è qualificata sullo schema del tenant corrente
  (`... FROM <schema>.patients ...`) con `clinic_id` come ulteriore filtro.
- Nessuna query attraversa gli schemi. Le viste per-tenant (dashboard, cartella
  clinica, riepilogo preventivi) vivono dentro lo schema del tenant.

### 3.1 Scope del dato: per-tenant condiviso vs per-clinica

Dentro lo schema di un tenant convivono due tipi di tabella:

- **per-clinica** — hanno `clinic_id`: isolate per singola sede (pazienti,
  appuntamenti, fatture, selezioni di anamnesi del paziente…).
- **per-tenant condiviso** — **senza** `clinic_id`: uguali per tutte le sedi del
  tenant. Caso principale: il **catalogo anamnesi**
  (`anamnesis_categories`/`anamnesis_items`), reso per-tenant in #43. Due sedi
  dello stesso tenant condividono per forza lo stesso catalogo; differenziarlo per
  sede richiederebbe di aggiungere `clinic_id` (oggi assente).

### 3.2 Postura di isolamento: applicativa, non a livello DB

L'isolamento cross-tenant è **applicativo**: schema derivato dal JWT firmato (mai
dal client) + prefissatura delle query con lo schema validato via regex. **Non**
c'è Row Level Security sugli schemi per-tenant (la RLS in `V1__init_schema.sql`
appartiene al vecchio modello a tabella condivisa, superato da `create_tenant`).
Un solo ruolo Postgres applicativo.

Conseguenza (GDPR art. 32): il confine tra **titolari diversi = tenant diversi** è
forte (schema dedicato + chiavi di cifratura per-tenant,
[07-Security §3](07-Security.md)); la separazione **tra sedi dello stesso tenant**
è controllo d'accesso interno allo stesso titolare, non un confine tra titolari.
La robustezza dell'isolamento poggia sulla correttezza del codice: la **difesa in
profondità a livello DB** (RLS o ruoli Postgres per-tenant) è un hardening ancora
aperto — vedi [07-Security §6](07-Security.md).

## 4. Provisioning di un nuovo tenant

Funzione PL/pgSQL **`dentalcare.create_tenant(...)`** (in `database/install.sql`):
crea schema + tabelle + viste + tenant + clinica + utente admin in **un'unica
transazione** (rollback totale su errore → niente schemi/record orfani).

`TenantProvisioningService.provision()`:
1. deriva `schemaName` dal `clinicId`, valida la regex;
2. chiama `create_tenant()` (crea tutto atomicamente);
3. registra la mappa nel `TenantSchemaRegistry`;
4. **allinea lo schema** alle patch correnti con `patchSchema()` (vedi sotto);
5. crea il bucket MinIO del tenant (dopo il commit);
6. invia email con password temporanea all'admin.

## 5. Evoluzione dello schema a runtime

`EstimateSchemaInitializer` è un `ApplicationRunner` che, all'avvio, applica in
modo **idempotente** le patch incrementali a **tutti** gli schemi tenant
(`ADD COLUMN IF NOT EXISTS`, ricostruzione viste, indici). Il metodo
`patchSchema(schema)` è riusato anche al provisioning, così un tenant creato tra
due deploy non resta indietro rispetto al codice.

**Regola di ordering importante**: le colonne referenziate da una vista
ricostruita vanno aggiunte **prima** del rebuild della vista; altrimenti
`DROP VIEW` + `CREATE VIEW` fallisce (colonna mancante) e la vista resta
cancellata fino al riavvio successivo. Questa regola è stata la causa di un bug
risolto durante l'introduzione della cifratura di `fiscal_code`.

## 6. Configurazione per-tenant

Alcuni comportamenti sono configurabili per singolo studio, sempre dallo schema
del tenant (mai da input client):

- **Orari studio** — colonne `work_start_time`, `work_end_time`, `slot_minutes`,
  `working_days` su `clinics`. Guidano la proposta del primo slot libero in
  `AppointmentService.findAvailability()`. Nullable di proposito: campo assente =
  default applicativo (`ScheduleConfig.defaults()`, 08:00–19:00, slot 15′,
  lun–ven). Editabili in *Impostazioni → Agenda*.
- **Ruoli per categoria prestazione** — `service_categories.allowed_roles`
  (vedi [07-Security §2](07-Security.md)).

Entrambe le colonne sono aggiunte in modo idempotente da `patchSchema()` (vedi
§5), quindi un tenant preesistente le riceve al primo avvio dopo il deploy.

## 7. Ciclo di vita del tenant: export e cancellazione

Contrappone al provisioning (§4) le operazioni di uscita. **Decisioni #47
(24/07/2026) — da implementare.**

### 7.1 Export dei dati
`TenantExportService` produce ZIP di CSV filtrati per `clinic_id`. Due percorsi
esistenti (una clinica; intero tenant); #47 aggiunge la **selezione di un
sottoinsieme** di cliniche (`clinic_id IN (...)`). Ogni export **include uno
snapshot puntuale e datato del catalogo anamnesi condiviso** (§3.1): senza, le
selezioni del paziente (`item_id`) diventano illeggibili dopo la cancellazione.

L'export **decifra** i campi sensibili ([07-Security §3](07-Security.md)) →
l'artefatto va protetto (archivio cifrato / download firmato a scadenza) e
l'estrazione **auditata**. È **copia di sicurezza / portabilità**, **non**
conservazione a norma (§7.3).

### 7.2 Cancellazione con guardia (grace period)
`deleteClinic()` rifiuta una sede con pazienti o l'ultima sede. `deleteTenant()`
oggi fa `DROP SCHEMA CASCADE` + purge MinIO = **irreversibile immediato**, con
export solo "consigliato lato client".

#47 impone una **guardia verificabile dal server** — mai una checkbox "hai
salvato?" (autodichiarazione non verificabile):

1. **export imposto + token monouso** legato all'export prodotto/scaricato → senza
   export, cancellazione rifiutata (409);
2. **conferma digitata** (nome tenant / `ELIMINA`);
3. **copia dell'export in retention** server-side per N giorni;
4. **soft-delete**: `tenants.active=false` + `scheduled_drop_at=now()+N gg`,
   accesso revocato subito; `DROP SCHEMA` reale solo allo scadere, via job →
   **annullabile nella finestra** (standard cloud account deletion).

Trade-off GDPR art. 17: se la cancellazione nasce da erasure dell'interessato, la
finestra va documentata come tempo tecnico (revoca accesso immediata + drop
differito); per l'offboarding volontario del tenant nessun vincolo.

### 7.3 Backup ≠ export ≠ conservazione a norma
Tre cose distinte: **backup** (MinIO + `pg_dump`, disaster recovery); **export**
(§7.1, portabilità/sicurezza); **conservazione a norma** (sistema conforme AgID —
PDF/A, PAdES + marca temporale, responsabile + manuale, conservatore accreditato).
L'app costruisce i **feeder** della conservazione, non il caveau: finalizzazione +
hash poi PDF/A + PAdES per la documentazione clinica; **fatture** delegate a un
**conservatore accreditato esterno**. La conservazione a norma è roadmap e
dominata da terzi — vedi [13-Audit-Trail](13-Audit-Trail.md).

## 8. Tenant demo

Lo schema `t_9d754153` è il tenant demo, materializzato con dati di esempio da
`database/install.sql`. La combo di **impersonazione** (assumere l'identità di un
altro operatore) è un privilegio del solo **account** demo
`demo@demo.dentalcare.it`, non di ogni utente del tenant: il frontend la abilita
confrontando l'email dell'utente con quella esposta da `/api/public/demo-config`,
che a demo spenta (produzione) non restituisce né email né password.

## 9. `install.sql` come specchio del DB

`database/install.sql` è l'installer unico e deve **rispecchiare** lo schema
reale: contiene sia il template in `create_tenant()` (per i nuovi tenant) sia lo
schema materializzato del tenant demo. Ogni modifica di schema va riflessa in
entrambe le copie. Verifica: caricamento in un DB fresco + `create_tenant()` di
prova → schema identico a quello prodotto dalle patch runtime.
