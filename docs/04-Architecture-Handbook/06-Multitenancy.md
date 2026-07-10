# 06 — Multi-tenancy

## 1. Modello: schema-per-tenant

Ogni studio (clinica) ha un **proprio schema PostgreSQL** nominato
`t_<8hex>` (es. `t_9d754153`), derivato dai primi 8 caratteri esadecimali del
`clinicId`. Lo schema globale `dentalcare` ospita enum, funzioni e il registro
dei tenant. Un unico database (`dentalcare_prod`), N schemi.

## 2. Contesto tenant

- **`TenantContext`**: thread-local con schema e clinicId correnti.
  `validatedSchema()` restituisce lo schema **validato via regex**
  `^t_[0-9a-f]{8}$` — usato in ogni query. Il tenant non è **mai** preso
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

## 6. Tenant demo

Lo schema `t_9d754153` è il tenant demo, materializzato con dati di esempio da
`database/install.sql`. La sessione demo (`demo@demo.dentalcare.it`) combina
impersonazione + nessuna password temporanea.

## 7. `install.sql` come specchio del DB

`database/install.sql` è l'installer unico e deve **rispecchiare** lo schema
reale: contiene sia il template in `create_tenant()` (per i nuovi tenant) sia lo
schema materializzato del tenant demo. Ogni modifica di schema va riflessa in
entrambe le copie. Verifica: caricamento in un DB fresco + `create_tenant()` di
prova → schema identico a quello prodotto dalle patch runtime.
