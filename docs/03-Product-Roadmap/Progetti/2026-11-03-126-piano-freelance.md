# #126 — Piano «Freelance»: il professionista senza studio proprio che lavora in più studi

**Stato:** Confermata — 03/11/2026 (decisioni in §15) · aperti: prezzo (D1; periodicità mensile decisa), risposta del DPO (D7, prima del rilascio; condiziona S8) · **Fase:** 1 (nessuna AI) · **Registro:** registro interno delle proposte, #126
**Nome del piano:** **Freelance** («Un professionista, più studi»), deciso il 03/11/2026 (§15, D1).

---

## 1. Richiesta del committente (03/11/2026)

- Una variante della sottoscrizione per i **professionisti senza studio proprio**: non hanno uno studio proprio e lavorano in **più studi dentistici**, in giorni e orari diversi.
- Il loro tenant ha **una sola clinica (virtuale, la loro)**. Le **poltrone coincidono con gli studi** in cui lavorano, e ogni poltrona ha il **proprio calendario**.
- Va ricondotto a un **caso particolare** della gestione generale di tenant, cliniche e poltrone, in modo efficiente.
- La professionista ha un ruolo di **amministratore che accede a tutte le funzioni**, oggi divise fra i ruoli: amministratore + dentista/medico/igienista + segreteria.

## 2. Glossario (in aggiunta a README §Terminologia)

| Termine | Significato |
|---|---|
| **Professionista Freelance** | Professionista (dentista o igienista) senza studio proprio, titolare del suo tenant |
| **Studio ospitante** | Studio dentistico di terzi in cui il professionista lavora. **Non** è un tenant suo e non è una sua sede |
| **Sede esterna** | Poltrona del professionista che rappresenta uno studio ospitante: ha un luogo (nome, indirizzo) e un orario proprio |
| **Clinica del professionista** | L'unica `clinics` del suo tenant. Non ha un indirizzo dove ricevere pazienti: porta i dati del professionista |

## 3. Cosa esiste oggi (verificato sul codice)

| Pezzo | Stato oggi | Dove |
|---|---|---|
| Tenant | `dentalcare.tenants`: `plan` (testo libero, predefinito `professional` alla registrazione), `kind` = customer/demo/sandbox, `owner_provider_id` | `install.sql`, `TenantProvisioningService.createTenant` |
| Registrazione | `create_tenant(...)` crea in una transazione schema, tenant, **una** clinica e il titolare con ruolo `tenant_admin` | `TenantProvisioningService:111-165` |
| Utenti | Sono righe di `providers` (per sede), con **un solo** `role` dell'enum `provider_role`: dentist, hygienist, orthodontist, surgeon, assistant, admin, other, tenant_admin, secretary | `install.sql:161`, `:890` |
| Ruolo nel token | Claim `role` = **una stringa** → una authority `ROLE_<RUOLO>`. Esiste già un precedente di authority aggiuntive: `platformRoles` (#69) | `JwtAuthenticationFilter:77-140` |
| Titolare | `tenant_admin` **non** è un ruolo medico (`RoleConstants.MEDICAL_ROLES`) ed è **escluso** dall'elenco dei professionisti (`ProviderService.findAll:99`). Quindi **non si può prenotare**: oggi un dentista titolare di uno studio piccolo deve avere un secondo account per comparire in agenda | `RoleConstants`, `ProviderService` |
| Atti clinici | `SecurityConfig.CLINICAL_WRITE_ROLES` comprende anche `TENANT_ADMIN`. Il titolare puro (non medico) quindi può: registrare esecuzioni e chiudere la seduta (`/session/**`), togliere prestazioni dal piano (#62), modificare la mappa prestazione → stato del dente (#65) e **leggere** lo storico degli episodi (#67) | `SecurityConfig:43,102-119` |
| Frontend | Un solo segnale `role` ('secretary' \| 'doctor' \| 'hygienist' \| 'admin'), in cui `tenant_admin` diventa 'admin'. 35 confronti sul ruolo in 16 file | `user-context.service.ts` |
| Poltrone | Anagrafica `clinic_chairs` (#115): `label` (max 40 caratteri), `active`, `sort_order`. Gli appuntamenti la indicano per **nome** (`appointments.chair_label`), e la rinomina li aggiorna. **Nessun luogo, nessun orario** | `ClinicChairService` |
| Orari | Orario della sede su `clinics` (#31). **Orario settimanale per professionista** `provider_work_hours` (giorno, inizio, fine; ripiego sull'orario della sede) e **assenze** `provider_absences` (#99), usati dalla disponibilità | `ProviderPresenceService`, `AppointmentService:557,913,960` |
| Fatturazione | Modalità **Studio vs Medico** (#44); il professionista ha già P.IVA, IBAN, SDI e prefisso parcella (`invoice_prefix` = `PARC`) | `ClinicSettingsService`, `InvoiceService`, `providers` |
| E-mail appuntamento | Nome e indirizzo presi dalla **clinica** | `AppointmentNotificationService.load()` |
| Giulia (#100) | Una clinica = un PIN, un nome pubblico, una città (`tenant_clinics`) | `VoiceClinicIdentificationService` |

## 4. Il modello: il professionista come caso particolare

### 4.1 Le due strade possibili

| | **A — Una clinica, poltrona = studio ospitante** (proposta del committente) | **B — Una clinica per ogni studio ospitante** |
|---|---|---|
| Pazienti | **Un solo elenco**: il paziente segue il professionista da uno studio all'altro | **Divisi per sede**: per regola i dati per sede sono isolati (README §Terminologia). Lo stesso paziente visto in due studi diventa due pazienti |
| Agenda | Una sola agenda, una colonna per sede esterna | Un'agenda per sede, si passa da una all'altra |
| Fit con la terminologia | La sede esterna **non** è una «sede del tenant» con dati propri: è un **luogo di erogazione** | Forza «clinica = sede fisica del tenant» su luoghi che non gli appartengono |
| Costo per sede | Una riga in `clinic_chairs` | Clinica intera: PIN, impostazioni, listino, poltrone, bucket, export |
| Se un domani apre uno studio | Cambia il piano; le sedi esterne restano poltrone disattivabili | Fusione di cliniche e di pazienti duplicati |

**Proposta: A.** Per farla bene servono **due generalizzazioni**, utili anche agli studi normali:

1. **La poltrona può avere un luogo.** Se il luogo è vuoto vale l'indirizzo della clinica, come oggi. Se è compilato, è il luogo dove si svolge l'appuntamento: e-mail, WhatsApp, Giulia, promemoria.
2. **L'orario del professionista può essere legato a una poltrona.** «Il martedì dalle 9 alle 13 sono alla poltrona X» invece di «il martedì dalle 9 alle 13 sono in studio». Una fascia senza poltrona vale per qualsiasi poltrona, come oggi.

Il professionista non è un «tipo» di tenant con un suo codice: è un tenant con **una clinica, sedi esterne con luogo e orari legati alle poltrone**, e un titolare che è anche professionista. Il codice ragiona sui dati. L'unico interruttore è il **piano** (§10), che governa limiti e parole della UI.

### 4.2 Ogni esigenza del professionista → meccanismo generale

| Esigenza del professionista | Meccanismo generale | Serve anche a uno studio normale? |
|---|---|---|
| Ogni studio ha il suo indirizzo | Luogo facoltativo sulla poltrona | Sì: studio su due piani o con un ambulatorio distaccato nello stesso tenant |
| Ogni studio ha giorni e orari suoi | Fasce dell'orario legate alla poltrona | Sì: igienista che usa solo la poltrona 3, chirurgo solo la sala chirurgica |
| Non si può essere in due studi insieme | Le fasce dello stesso professionista non si sovrappongono, **anche su poltrone diverse** (oggi il controllo vale nello stesso giorno, a prescindere dalla poltrona) | Sì: stessa regola |
| Tempo per spostarsi fra due studi nello stesso giorno | **Margine fra luoghi diversi** (minuti, in Impostazioni → Agenda; 0 = nessuno) | Neutro: con un solo luogo non scatta mai |
| L'agenda mostra solo gli studi di quel giorno | L'agenda nasconde le poltrone senza fasce in quel giorno (con un interruttore «mostra tutte») | Sì: meno colonne vuote |
| Titolare che è anche professionista | Ruolo clinico + capacità di amministratore (§5) | **Sì: è il caso del dentista titolare di uno studio piccolo**, oggi non prenotabile |
| Conti con ogni studio ospitante | Rendiconto delle prestazioni per poltrona e periodo (§9) | Sì: produzione per poltrona |

## 5. Ruoli: «amministratore + professionista»

### 5.1 Principio

Il ruolo clinico è una **qualifica professionale**, non un permesso del software: dice chi è la persona. Per questo il professionista **non** diventa «tutti i ruoli insieme». Un'igienista Freelance **non** deve ottenere i poteri del dentista: per #123 prescrive solo il medico, e per #74 solo i medici usano il Copilot clinico.

Il professionista è quindi **il suo ruolo clinico** (dentista o igienista) **più la capacità di amministrare il tenant**. La segreteria non è una qualifica: le sue funzioni (agenda di tutti, pazienti, fatture, contatti) sono già aperte all'amministratore (`InvoiceService.ADMIN_ROLES`, `DashboardService.ADMIN_ROLES`, `filterProviderId` nullo per 'admin'). Si verifica e si chiude ogni eccezione residua (§7.1).

### 5.2 Modello

- `providers.role` resta **una sola** qualifica (dentist, hygienist, …). Nessun ruolo multiplo nel database: una sola colonna, e le decine di punti del backend che leggono la qualifica non cambiano.
- Nuova colonna `providers.is_tenant_admin boolean NOT NULL DEFAULT false`: **capacità** di amministrare.
- Nel token: `role` = qualifica, claim nuovo `tenantAdmin: true` → authority aggiuntiva `ROLE_TENANT_ADMIN`, con lo stesso meccanismo di `platformRoles`. Le regole `hasRole("TENANT_ADMIN")` di `SecurityConfig` funzionano senza modifiche.
- `TenantContext.isTenantAdmin()` sostituisce i confronti `"tenant_admin".equals(role)`, oggi in 8 servizi: `ProviderPriceOverrideService`, `ProviderPresenceService`, `ProviderPreferencesService`, `ScreenLockService`, `ServiceCatalogService`, `AuthService`, `ProviderService`, `TenantAdminService`.
- Il ruolo `tenant_admin` esistente resta per il titolare **non** professionista (amministratore puro): `role = tenant_admin` vale come `is_tenant_admin = true` senza qualifica clinica.
- `ProviderService.findAll` esclude chi **non ha una qualifica clinica**, non più chi è `tenant_admin`. Così il titolare-professionista compare in agenda.
- Frontend: `role` resta la qualifica ('doctor' o 'hygienist'), segnale nuovo `isTenantAdmin`. Il menu è l'**unione** delle due viste. `tenant-admin.guard.ts` legge `isTenantAdmin`.

### 5.3 Effetti (decisi il 03/11/2026)

- **Atti clinici del titolare non clinico — D3: nessuno.** La verifica del 03/11/2026 ha trovato più delle quattro aree di `CLINICAL_WRITE_ROLES`:
  - **Stato oggi.** Il titolare che non è un clinico apre le pagine cliniche dell'interfaccia, e lato server il controllo per qualifica non copre ancora tutte le scritture cliniche. La correzione è pianificata nel gate di go-live (#18 Blocco 1, segregazione lato server con test per ruolo) e in S1; il dettaglio tecnico sta nel registro interno delle proposte. Oggi tutti gli ambienti contengono solo dati fittizi.
  - **Perché è così.** Il titolare è stato ammesso agli atti clinici perché di norma è un clinico, e la registrazione non permette di dirlo.
  - **Origine del vincolo `'admin'` nell'interfaccia (committente, 04/11/2026).** Serviva in sviluppo, per passare da un profilo all'altro e vedere che cosa abilita ciascuno. Oggi lo stesso scopo lo coprono il cambio di persona e l'ambiente di prova, su dati fittizi, insieme ai percorsi per ruolo dell'Academy. **L'amministratore dello studio vede quindi solo le funzioni amministrative.**
  - **Impersonazione: resta com'è, solo dove i dati sono fittizi.** Verificato nel codice il 04/11/2026:
    - *studio di prova* (`kind='demo'`): chi si registra ha il ruolo reale `dentist`, cioè il medico principale del seed, e sceglie la persona dal menu. Togliere `TENANT_ADMIN` da `CLINICAL_WRITE_ROLES` non lo tocca. La persona «Amministratore» (#87) avrà solo le funzioni amministrative, come nello studio vero: in S1 il suo ruolo lato server va allineato (oggi `ADMIN`).
    - *account demo condiviso* (`demo@`, ruolo `admin`): le persone dei professionisti cambiano l'interfaccia, le API restano col ruolo `admin` (tranne il Copilot). Per questo `ADMIN` resta in `CLINICAL_WRITE_ROLES` finché c'è la demo (#25).
    - *ambiente di prova del cliente* (`kind='sandbox'`): chi entra diventa il medico principale del seed, anche il titolare non clinico; la segreteria diventa la segretaria del seed. Dati fittizi: va bene così.
    - *studio vero*: nessuna impersonazione. `DemoPersonaService` la ammette solo nello schema demo e negli studi di prova non scaduti; S1 aggiunge un test che lo fissa.
    - Le persone dei professionisti e della segreteria valgono oggi solo per l'interfaccia e il Copilot. Se la prova deve mostrare anche i blocchi del server (#18 punto 1.3), la persona va estesa a tutte le API, solo negli schemi di prova: facoltativo.
    - Academy: le lezioni del percorso amministratore vanno riviste in S1.
  - **Regola decisa.** Ogni scrittura clinica, non solo le quattro aree, segue **solo** la qualifica. Per la cartella il titolare non clinico vale come la segreteria, e legge quello che lei legge. Gestisce agenda, anagrafica, preventivi, fatture e impostazioni.
  - **Due interventi.**
    - *Segreteria:* è già nel gate, #18 Blocco 1 punto 3 («segregazione segreteria lato server»). Stima rivista a ~5-7h, con i test per ruolo. Non dipende da #126.
    - *Titolare non clinico:* va dentro S1, perché richiede la qualifica dichiarata. `TENANT_ADMIN` esce da `CLINICAL_WRITE_ROLES`, e la stessa lista vale per gli endpoint chiusi dal punto precedente. Nel frontend le pagine cliniche si aprono su `isClinical`, non più su `'admin'`. `ADMIN` resta solo per la demo, da rivedere con #25.
- **Passaggio per i titolari attuali.** La registrazione oggi crea **ogni** titolare come `tenant_admin`, anche quando è un dentista. La restrizione si attiva solo **dopo** che il titolare ha risposto, al primo accesso, alla domanda esplicita «Sei anche un professionista? Dentista / Igienista / No». Con «Dentista» o «Igienista» il sistema gli dà la qualifica e tiene `is_tenant_admin`. Non c'è migrazione automatica (niente automatismi silenziosi): senza la domanda, un titolare-dentista perderebbe la seduta il giorno del rilascio.
- **Blocco dello schermo (#118) — D4: valgono i minuti della qualifica clinica**, compresa la sospensione durante la seduta. Viene da sé: con S1 il claim `role` del titolare-professionista è la qualifica, e `ScreenLockService.roleGroup` lo mette nel gruppo dei medici. Il titolare puro (`tenant_admin`) resta nel gruppo amministratore.

## 6. Modello dati

```sql
-- 1) Luogo facoltativo della poltrona (NULL = indirizzo della clinica, come oggi)
ALTER TABLE <schema>.clinic_chairs
    ADD COLUMN IF NOT EXISTS location_name   text,     -- es. «Studio Dentistico Bianchi»: il nome dell'ospitante, oltre il label corto
    ADD COLUMN IF NOT EXISTS address_line1   text,
    ADD COLUMN IF NOT EXISTS postal_code     text,
    ADD COLUMN IF NOT EXISTS city            text,
    ADD COLUMN IF NOT EXISTS province        text,
    ADD COLUMN IF NOT EXISTS phone           text,     -- telefono dello studio ospitante, per il paziente
    ADD COLUMN IF NOT EXISTS location_notes  text;     -- «citofono 3, secondo piano»

-- 2) Fascia dell'orario legata a una poltrona, con validità (gli accordi con gli studi cambiano)
ALTER TABLE <schema>.provider_work_hours
    ADD COLUMN IF NOT EXISTS chair_id   uuid NULL REFERENCES <schema>.clinic_chairs(id),
    ADD COLUMN IF NOT EXISTS valid_from date NULL,
    ADD COLUMN IF NOT EXISTS valid_to   date NULL;

-- 3) Titolare che è anche professionista
ALTER TABLE <schema>.providers
    ADD COLUMN IF NOT EXISTS is_tenant_admin boolean NOT NULL DEFAULT false;
UPDATE <schema>.providers SET is_tenant_admin = true
 WHERE role = 'tenant_admin' AND is_tenant_admin = false;   -- idempotente, conserva l'esistente

-- 4) Margine fra luoghi diversi (parametrico, mai costante)
ALTER TABLE <schema>.clinics
    ADD COLUMN IF NOT EXISTS travel_buffer_minutes integer NOT NULL DEFAULT 0;
```

Note:
- Applicazione in `EstimateSchemaInitializer` (DDL idempotente, prima colonne e poi viste), aggiornare `create_tenant()`, rigenerare `install.sql`.
- Gli appuntamenti indicano la poltrona per **nome**: il luogo di un appuntamento si legge con `(clinic_id, chair_label)` → `clinic_chairs`. Gli appuntamenti futuri seguono una modifica del luogo, ed è giusto. Per il passato vale la regola «se lo studio ospitante cambia, nuova poltrona e la vecchia si disattiva»: quella con appuntamenti non si elimina già oggi (#115). I documenti emessi (fatture) hanno già i propri dati copiati.
- Nessuna tabella nuova per il calendario: **riusa `provider_work_hours`** (#99) con la poltrona. Le chiusure di uno studio ospitante si registrano come assenza del professionista (`provider_absences`). La chiusura per poltrona resta fuori dalla Fase 1.

## 7. Backend

### 7.1 Ruoli (§5)
- `JwtService`: claim `tenantAdmin`. `JwtAuthenticationFilter`: authority aggiuntiva. `TenantContext.isTenantAdmin()`.
- Sostituire i confronti nei servizi elencati in §5.2. `ProviderService.findAll` filtra sulla qualifica.
- Rivedere `CLINICAL_WRITE_ROLES` secondo D3.
- Ricognizione: ogni endpoint aperto a `SECRETARY` e chiuso a `TENANT_ADMIN` va aperto anche all'amministratore. Si parte da `grep hasAnyRole` e dai servizi con `ADMIN_ROLES`.
- Test: igienista + amministratore **non** prescrive (#123) e **non** ha il Copilot clinico; dentista + amministratore sì; titolare puro non registra atti clinici (se D3 = sì).

### 7.2 Poltrone e orari
- `ClinicChairService` e DTO: campi del luogo. Il controllo di unicità del nome resta.
- `ProviderPresenceService`: fasce con `chair_id`, `valid_from`/`valid_to`. Le fasce dello stesso professionista non si sovrappongono **nemmeno su poltrone diverse**.
- `AppointmentService` (disponibilità, creazione, spostamento):
  - una fascia legata a una poltrona rende prenotabile **solo** quella poltrona per quel professionista;
  - fra due appuntamenti dello stesso professionista in **luoghi diversi** dello stesso giorno serve `travel_buffer_minutes`;
  - fuori fascia → rifiuto con causa leggibile (#51), come oggi.
- Disattivare una sede esterna che ha appuntamenti futuri: **elenco degli appuntamenti da spostare o annullare**, nessuno spostato da solo (principio di #56).

### 7.3 Comunicazioni al paziente
- `AppointmentNotificationService.load()`, testi WhatsApp, e-mail di promemoria e richiami: luogo = `coalesce(luogo della poltrona, indirizzo della clinica)`.
- Mittente e intestazione: il **nome del professionista** (la clinica del professionista lo porta), più «presso <studio ospitante>».

## 8. Frontend

- **Impostazioni → Poltrone**: nel piano Freelance la scheda si chiama «I tuoi studi». Ogni voce ha nome dello studio, indirizzo, telefono e note; le fasce orarie si impostano dalla scheda dello studio (giorni, ore, valida dal/al).
- **Orario del professionista** (#99): fascia con poltrona facoltativa. Negli studi normali resta vuota e nulla cambia.
- **Agenda**: nasconde le poltrone senza fasce nel giorno (interruttore «mostra tutte»), etichetta di colonna con il nome dello studio, colore per luogo.
- **Nuovo appuntamento**: lo studio si propone dalla fascia del giorno; la disponibilità (#31) mostra già solo gli slot validi.
- **Menu e permessi**: `isTenantAdmin` + qualifica → unione delle viste. Si rivedono i 35 confronti sul ruolo in 16 file, tutti in `user-context.service.ts` o vicino.
- **Moduli**: nel piano Freelance il magazzino è nascosto (i materiali sono dello studio ospitante) e la creazione di altre sedi non c'è. Deciso (D6, 03/11/2026).
- **Vocabolario**: le parole «poltrona» e «sede» cambiano solo nelle etichette, guidate dal piano. Nessuna copia dei componenti.

## 9. Fatturazione e rendiconto per studio ospitante

Esistono due modi di lavorare. **Deciso (D5, 03/11/2026): si coprono entrambi.**

1. **Il professionista fattura al paziente** (libero professionista che affitta la poltrona). Coperto oggi dalla modalità «Medico» di #44: P.IVA, IBAN, SDI e prefisso parcella del professionista ci sono già. Va impostata come predefinita nel piano Freelance.
2. **Lo studio ospitante fattura al paziente e paga il professionista.** Il professionista non fattura ai pazienti: gli serve il **rendiconto per studio**, cioè le prestazioni eseguite (#56) per poltrona e periodo, con totali a listino, esportabile in PDF/CSV. È la base della sua fattura allo studio. La fattura B2B allo studio ospitante dal programma è un passo successivo.

**Il modo si sceglie per studio ospitante** («chi fattura al paziente: io / lo studio»), perché lo stesso professionista può lavorare in un modo in uno studio e nell'altro modo altrove. Gli appuntamenti di uno studio che fattura da sé non generano fatture del professionista al paziente, e finiscono nel rendiconto di quello studio.

Il rendiconto per poltrona e periodo serve anche agli studi normali (produzione per poltrona). **Listini diversi per studio ospitante**: fuori dalla Fase 1 (oggi listino per tenant e override per professionista, #44); da valutare con D5.

## 10. Piano, registrazione, limiti

- **Piano**: valore nuovo di `tenants.plan` = `freelance`, come `essential` e `professional` (nome pubblico «Freelance», D1). Governa i limiti e le parole della UI; nessuna logica clinica dipende dal piano.
- **Limiti** (in configurazione, non costanti):
  - una sola clinica;
  - utenti: il professionista, più eventualmente una segreteria (D2);
  - numero di sedi esterne: illimitato o con un tetto (D2).
  - Oggi i piani non hanno limiti applicati: nasce qui un piccolo `PlanLimitsService`, riusabile per Essential/Professional.
- **Registrazione** (`/registrati`): scelta «Ho uno studio» / «Lavoro in più studi». Nel secondo caso il nome della clinica è quello del professionista, si chiede la qualifica (dentista o igienista) e il titolare nasce con `role = qualifica` e `is_tenant_admin = true`. Gli studi ospitanti si aggiungono al primo accesso, con una procedura guidata.
- **Pagamento** (#75 Mollie): abbonamento **mensile**; il prezzo è ancora aperto nella D1. La landing non promette nulla finché il piano non è nel business plan (regola delle pagine pubbliche).

## 11. Giulia (#100)

- Il PIN identifica il **professionista** (la sua clinica). Il riconoscimento dal numero chiamante funziona già.
- `identify_clinic` restituisce il nome del professionista e gli studi in cui lavora. Disponibilità e prenotazione dicono **dove**: «martedì alle 10 presso lo Studio Bianchi, via …».
- Prompt Retell: per un professionista Freelance il nome non è uno studio. Il testo si adatta («la dottoressa X riceve presso…»). Va provato con i 5 scenari del collaudo di #100 più uno nuovo «stesso giorno, due studi».

## 12. Privacy (GDPR) — chi è titolare dei pazienti degli studi ospitanti

**Indicazione del committente (D7, 03/11/2026).** Il caso prevalente è il paziente **dello studio ospitante**, di cui lo studio è titolare. Esistono però pazienti che **seguono il professionista** da uno studio all'altro, e le due situazioni coesistono, anche nello stesso studio.

**Proposta per il DPO:** [proposta-dpo-126-titolarita-freelance.md](../../06-Compliance/proposta-dpo-126-titolarita-freelance.md). Contiene tre ipotesi di ruolo per i pazienti dello studio (responsabile art. 28, contitolarità art. 26, titolari autonomi) e dieci domande (Q1-Q10). Nel registro DPIA è la voce **D-90**.

**Principio:** il programma non presume il ruolo, e registra il **titolare per ogni paziente**. Così regge qualunque risposta del DPO. È la parte del progetto **specifica del piano Freelance**, perché il rapporto giuridico con uno studio di terzi non esiste negli studi normali.

```sql
-- Studio ospitante come soggetto (chi è e con quale accordo); il luogo resta sulla poltrona (§6.1)
CREATE TABLE IF NOT EXISTS <schema>.host_studios (
    id                     uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id              uuid NOT NULL REFERENCES <schema>.clinics(id),
    legal_name             text NOT NULL,
    vat_number             text,
    registered_address     text,
    privacy_contact        text,              -- referente privacy o DPO dello studio
    agreement_type         text NOT NULL DEFAULT 'none'
                           CHECK (agreement_type IN ('processor', 'joint', 'none')),
    agreement_signed_on    date,
    agreement_expires_on   date,
    agreement_document_id  uuid,              -- copia firmata, nell'archivio documenti
    billing_by             text NOT NULL DEFAULT 'professional'
                           CHECK (billing_by IN ('professional', 'host')),   -- D5: chi fattura al paziente
    collaboration_ended_on date,
    created_at             timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE <schema>.clinic_chairs
    ADD COLUMN IF NOT EXISTS host_studio_id uuid NULL REFERENCES <schema>.host_studios(id);

-- Titolare per paziente: 'tenant' è il caso di ogni studio normale (valore di oggi)
ALTER TABLE <schema>.patients
    ADD COLUMN IF NOT EXISTS controller_kind text NOT NULL DEFAULT 'tenant'
        CHECK (controller_kind IN ('tenant', 'host', 'to_assign')),
    ADD COLUMN IF NOT EXISTS controller_host_studio_id uuid NULL REFERENCES <schema>.host_studios(id);

-- Storico append-only dei cambi di titolare (passaggi A<->B, fine collaborazione)
CREATE TABLE IF NOT EXISTS <schema>.patient_controller_changes (
    id                     uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    patient_id             uuid NOT NULL REFERENCES <schema>.patients(id),
    from_kind              text,
    from_host_studio_id    uuid,
    to_kind                text NOT NULL,
    to_host_studio_id      uuid,
    reason                 text NOT NULL,     -- creazione, passaggio su richiesta del paziente, fine collaborazione
    document_id            uuid,              -- richiesta del paziente, se c'è
    changed_by_provider_id uuid NOT NULL,     -- dal token, mai dal client
    changed_at             timestamptz NOT NULL DEFAULT now()
);
```

Regole (dettaglio nella proposta per il DPO, §4.2):
- **Nessun valore predefinito nel piano Freelance.** Nel modulo del paziente il titolare è obbligatorio e non è preselezionato. Il server rifiuta la creazione senza scelta esplicita. I pazienti creati da Giulia nascono `to_assign`, e la seduta non si apre finché non sono attribuiti.
- Avviso permanente per i pazienti attribuiti a uno studio con `agreement_type = 'none'`. Il blocco della scrittura clinica dipende dalla risposta a Q4.
- Richiami e comunicazioni non legate a un appuntamento: spenti per i pazienti `host`, salvo risposta diversa a Q5. I promemoria degli appuntamenti partono e indicano il luogo.
- Il rendiconto di uno studio (S6) contiene solo i suoi pazienti `host`.
- **Fine collaborazione**: procedura guidata, mai automatica, con la regola delle cancellazioni di dati clinici (prima il conteggio, poi il soft delete):
  - conteggio ed elenco dei pazienti e degli appuntamenti futuri;
  - export delle cartelle, riusando l'export di #18 Blocco 3;
  - scelta per ciascun paziente: restituito oppure passato al professionista;
  - soft delete, poi cancellazione alla scadenza indicata dal DPO (Q6).
- Il passaggio da A a B, o da B ad A, avviene solo con il documento del paziente (Q7). Ogni cambio scrive una riga in `patient_controller_changes`.
- Se lo studio ospitante è a sua volta un tenant DentalCare, nessun dato attraversa i tenant: la condivisione resta **fuori dalla Fase 1**.

## 13. Fuori dalla Fase 1

- Collegamento con lo studio ospitante come tenant DentalCare (agenda condivisa, cartella condivisa).
- Listini diversi per studio ospitante.
- Fattura B2B allo studio ospitante.
- Chiusure per singola poltrona (si usano le assenze del professionista).
- Qualsiasi suggerimento AI sugli orari (Fase 2).

## 14. Slice e stima (ore agente)

| Slice | Contenuto | Stima |
|---|---|---|
| **S1 — Ruolo clinico + amministratore** | §5 e §7.1: colonna, token, `TenantContext`, servizi, `ProviderService`, frontend (`isTenantAdmin`, menu, guard, 35 confronti), test. **Utile da sola** al dentista titolare di uno studio piccolo | ~8-12h |
| **S2 — Luogo sulla poltrona** | §6.1, CRUD, Impostazioni, luogo in e-mail, WhatsApp, promemoria e richiami | ~5-7h |
| **S3 — Orario per poltrona** | §6.2/6.4, presenza, disponibilità, sovrapposizioni fra poltrone, margine di spostamento, agenda che nasconde le poltrone vuote, disattivazione con elenco degli appuntamenti futuri | ~8-10h |
| **S4 — Piano e registrazione** | Piano, `PlanLimitsService`, `create_tenant` con qualifica, scelta in `/registrati`, procedura guidata degli studi, moduli nascosti, vocabolario | ~8-10h |
| **S5 — Giulia** | `identify` e risposte con il luogo, prompt, collaudo | ~3-4h + collaudo |
| **S6 — Rendiconto per studio** | Prestazioni eseguite per poltrona e periodo, PDF/CSV; «chi fattura» per studio ospitante (D5) | ~5-8h |
| **S8 — Titolare per paziente** | §12: `host_studios`, titolare per paziente e storico, avviso o blocco, filtro di richiami e rendiconto, procedura di fine collaborazione, passaggio A↔B, test. **Parte dopo la risposta del DPO** (Q1, Q4, Q6, Q7) | ~12-16h |
| **S7 — Chiusura** | `install.sql`, demo seed (un tenant Freelance di prova), Academy («Percorso del professionista che lavora in più studi»), test trasversali | ~4-6h |

**Totale ≈ 53-73h agente (~7-9 giornate).** Ordine: **S1 → S2 → S3** (base generale, utile a tutti), poi S4, S5 ed S6 in parallelo, poi S8 (dopo la risposta del DPO), infine S7. Il piano non si rilascia senza S8.

Dipendenze:
- #123: la regola «prescrive solo il medico» va provata anche col doppio ruolo;
- #75: prezzo del piano;
- #118: minuti di blocco per ruolo;
- **#18 Blocco 1 punto 3**: segregazione della segreteria lato server, con la stessa lista di endpoint clinici di D3;
- **#18 Blocco 3**: export della cartella, riusato alla fine della collaborazione (S8);
- **risposta del DPO**: condiziona S8.

Nessuna voce del gate di go-live dipende da questo progetto.

## 15. Decisioni del committente (03/11/2026)

| # | Decisione | Esito |
|---|---|---|
| D1 | Nome pubblico, prezzo e periodicità del piano | **Nome: «Freelance»**, sottotitolo «Un professionista, più studi», codice `freelance`. **Periodicità: mensile** (03/11/2026). **Aperto:** prezzo, da business plan, nella fascia di Essential |
| D2 | Utenti e sedi esterne ammessi nel piano | **Confermata:** 1 professionista + 1 segreteria facoltativa; studi ospitanti senza tetto. Il limite che protegge dall'abuso è il professionista unico |
| D3 | Atti clinici del titolare non professionista | **Confermata: nessuno**, per tutte le scritture cliniche e non solo per le quattro di `CLINICAL_WRITE_ROLES`. Per la cartella vale come la segreteria. Si attiva dopo la domanda al primo accesso. Verifica in §5.3. **04/11/2026:** l'amministratore vede solo le funzioni amministrative (il vincolo `'admin'` serviva allo sviluppo); l'impersonazione dei ruoli resta com'è, solo su dati fittizi (prova, demo, ambiente di prova) |
| D4 | Minuti di blocco dello schermo per il titolare-professionista | **Confermata:** quelli della sua qualifica clinica |
| D5 | Fatturazione | **Confermata: entrambi i modi**, scelti per studio ospitante («chi fattura»), in S6 |
| D6 | Moduli nascosti nel piano Freelance | **Confermata:** magazzino e creazione di altre sedi |
| D7 | Titolare del trattamento dei pazienti | **Indicazione:** prevalente il paziente dello studio ospitante, ma esistono pazienti che seguono il professionista. Modello «titolare per paziente» (§12) e [proposta per il DPO](../../06-Compliance/proposta-dpo-126-titolarita-freelance.md); S8 dopo la risposta. Registro DPIA D-90 |

## 16. Rischi

- **Doppio ruolo nel frontend**: i 35 confronti sul ruolo sono il punto più fragile. Mitigazione: un solo `computed` per capacità (`canAdminister`, `isClinical`, `canPrescribe`) e nessun confronto diretto nei template.
- **Nome della poltrona come chiave**: `appointments.chair_label` è testo. Con le sedi esterne il nome conta di più. La rinomina aggiorna già gli appuntamenti (#115); l'FK `chair_id` sugli appuntamenti è un miglioramento separato, non necessario qui.
- **Equivoco di prodotto**: un professionista Freelance che apre uno studio deve poter cambiare piano senza migrazioni. Il modello A lo permette, e va provato in S7.
