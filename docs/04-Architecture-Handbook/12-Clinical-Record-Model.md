# 12 — Modello della cartella clinica

> Questo capitolo descrive il **modello clinico di riferimento** di DentalCare Pro: cosa
> è implementato oggi e cosa la [Release 1.x](../03-Product-Roadmap/Release-1.x.md)
> aggiunge per portare la cartella al livello di **valore probatorio** richiesto a una
> cartella clinica digitale.

## 1. Principio: la cartella non è un file

La cartella clinica non è un documento né una tabella: è un **insieme coerente di eventi e
documenti**, collegati tra loro e ricostruibili nel tempo. Il requisito che la distingue
da un archivio di dati è la capacità di rispondere, in qualsiasi momento:

- chi ha scritto questa informazione, quando, e in quale contesto di cura;
- che aspetto aveva la cartella a una data passata;
- cosa è stato corretto, da chi, e perché;
- chi ha letto o esportato cosa.

Le prime tre domande riguardano il **modello dati**; la quarta l'**audit trail**.

## 2. Entità del modello

| Entità | Ruolo | Stato |
|---|---|---|
| **Tenant / Clinic** | confine organizzativo e di sicurezza | ✅ implementato |
| **Patient** | anagrafica clinica, identificatore interno UUID | ✅ implementato |
| **Provider** | professionista e ruolo | ✅ implementato |
| **Appointment** | pianificazione | ✅ implementato |
| **Encounter (Seduta clinica)** | **episodio di cura effettivo** | ✅ **implementato (#56-#62)** |
| **Anamnesi** | scheda clinica generale, voci strutturate da catalogo | ✅ implementato · tri-stato in Release 1.x |
| **Reperto dentale** (odontogramma) | condizione per dente/superficie, con origine e, se registrata in seduta, autore e seduta (#65) | ✅ implementato · confronto fra date via episodi (#67) · storia per reperto in Release 1.x |
| **Episodio clinico** + fotografie | visita o contatto fuori visita, con la situazione del paziente prima e dopo | ✅ **implementato (#67, Fase 1)** |
| **Diagnosi** | problema, stato, data, risoluzione | ✅ implementato |
| **Piano di cura** + voci | trattamento previsto | ✅ implementato |
| **Voce di cartella** (visita/prestazione) | atto eseguito, note cliniche, materiali | ✅ implementato · **finalizzazione in Release 1.x** |
| **Prescrizione** | terapia prescritta | ✅ implementato |
| **Documento** | immagini, referti, consensi acquisiti | ✅ implementato · integrità in Release 1.x |
| **Analisi AI** + revisione | proposta algoritmica e sua verifica | ✅ implementato (vedi [04-AI](04-AI.md)) |
| **Consenso** | consenso informato versionato | 🔨 Release 1.x |
| **Audit event** | accessi e operazioni | 🔨 Release 1.x |
| **Preventivo / Fattura** | piano economico | ✅ implementato |

### 2.1 Encounter & Ciclo della Seduta Clinica (implementato #56–#62)

Con l'implementazione del **Ciclo della seduta** (#56) e dei controlli probatori associati (#60, #61, #62), la separazione tra pianificazione (appuntamento) e atto clinico (piano di cura / prestazione) è stata saldata mediante un modello relazionale esplicito:

```text
Appointment (pianificazione temporale / poltrona)
     │ 1..N
     ▼
appointment_treatment_items (collegamento e tracciamento esecuzione)
     ├── treatment_plan_item_id
     ├── outcome: completed | partially_completed | not_performed | cancelled
     ├── performed_at (timestamp reale dell'atto)
     ├── performed_by_provider_id (medico reale che firma l'atto, dal JWT)
     └── performed_in_appointment_id (seduta clinica d'origine)
     ▲
     │ 1..N
TreatmentPlanItem (piano di cura del paziente)
     ├── status: planned | in_progress | completed | cancelled
     ├── performed_by_provider_id / performed_at / performed_in_appointment_id
     └── treatment_plan_item_events (storico eventi, riprogrammazioni, stralci)
```

#### Regole e vincoli di integrità clinica:
1. **Tracciabilità probatoria dell'autore (#62):** L'atto clinico deve portare il nome di chi l'ha realmente svolto. Se un medico visita in una seduta originariamente assegnata a un collega, il sistema consente l'operazione ma registra nel DB `performed_by_provider_id = current_user`.
2. **Confine di ruolo server-side (`CLINICAL_WRITE_ROLES`):** Gli endpoint `/api/appointments/{id}/session/**` sono protetti in `SecurityConfig` e riservati ai ruoli sanitari (`dentist`, `hygienist`, `orthodontist`, `surgeon`) e agli amministratori (`tenant_admin`, più `admin` dell'utenza demo). La segreteria non può firmare l'esecuzione di atti clinici.
3. **Inviolabilità temporale della seduta:** Il server rifiuta registrazioni su sedute già chiuse, annullate o no-show (`SESSION_ALREADY_CLOSED`, `SESSION_CANCELLED`, `SESSION_NO_SHOW`).
4. **Tracciamento eventi in sospeso (`treatment_plan_item_events` #61):** Alla chiusura della seduta, ogni prestazione non eseguita non resta in un limbo: viene riprogrammata o stralciata con vincolo di motivazione clinica obbligatoria (`ck_tpie_reason`).
5. **Il dente non cambia stato da solo (#65):** una prestazione eseguita può aggiornare l'odontogramma solo con un gesto del medico. Il listino dichiara lo stato che la prestazione lascia (`service_tooth_outcomes`, per sede e prestazione); in seduta è una proposta da applicare, cambiare o ignorare, e «lascia com'è» è il default. Gli stati di superficie (otturazione) chiedono le superfici, quelli del dente intero no. Dalla seduta si scrive, non si cancella: niente carie, niente «sano». La riga porta `source='session'`, `recorded_by_provider_id` e `recorded_appointment_id`; il tab Odontogramma resta l'autorità e può correggerla (diventa `manual` e perde l'attribuzione) o cancellarla.

### 2.1.1 Dal reperto al piano di cura (#66)

«Genera piano di cura» serve a non dimenticare nulla, non a decidere al posto del medico:

- propone solo ciò che l'odontogramma indica **da fare**: `cavity` sulle superfici, `to_extract`, `missing`, `impacted` sul dente intero. Corona, impianto, ponte e devitalizzato sono cure presenti e non si ripropongono;
- una voce per condizione: le carie di un dente diventano un'unica otturazione con le sue superfici, e la prestazione dipende dal numero di superfici (`condition_service_defaults.surface_count`);
- ciò che si scarta resta **visibile con il motivo**: carie su un dente assente o da estrarre («Non proposte»), stessa prestazione già aperta sullo stesso dente (esclusa, recuperabile con «Aggiungi comunque»);
- il server applica le **stesse regole** (`PlanItemApplicabilityService`) alla creazione da odontogramma, all'aggiunta e al singolo `addItem`: FDI valido, prestazione attiva, posizione, stato del dente (`service_catalog.requires_natural_tooth`), superfici valide. Tutti i problemi in un'unica risposta `422 SERVICE_NOT_APPLICABLE`;
- l'aggiunta a un piano esistente è una sola transazione (`POST /api/treatment-plans/{id}/items/from-odontogram`), e si genera solo da un odontogramma salvato.

### 2.2 Reperto dentale: da snapshot a storia

L'odontogramma è oggi la **fotografia dello stato corrente**: la condizione di un
dente/superficie viene aggiornata in luogo, con la sua origine (`manual` | `ai` |
`session`) e il riferimento all'analisi o alla seduta che l'ha prodotta (#65). La
provenienza è modellata bene; la **storia per singolo reperto** no. Il confronto fra date
oggi lo danno gli **episodi clinici** (§2.3), che congelano l'odontogramma all'ingresso e
all'uscita di ogni visita.

Il modello di riferimento tratta ogni reperto come un **fatto clinico datato**:

```text
DentalFinding
  tenant · patient · encounter
  tooth_code · surface_code · finding_code
  status · certainty            ← sospetto / confermato / trattato
  onset_date · recorded_at · recorded_by
  source_type · source_id       ← esame clinico | radiografia | importazione | AI
  supersedes_id · void_reason   ← storia, non sovrascrittura
```

Il rendering grafico si genera dai dati. Un'immagine dell'odontogramma può essere prodotta
come snapshot leggibile, ma non è mai la fonte.

Questo abilita il **confronto tra date** — cioè la ricostruzione dell'evoluzione clinica
di un dente, che è il motivo per cui esiste un odontogramma.

### 2.3 Episodi clinici e fotografie (implementato #67, Fase 1)

Un **episodio** è una visita in presenza, legata a un appuntamento, oppure un **contatto
fuori visita** (telefonata, documento o RX esterno, altro). A ogni episodio il sistema
associa la situazione clinica del paziente **all'ingresso** e **all'uscita**.

```text
clinical_episodes            (per sede, nello schema del tenant)
  episode_type   visit | contact          contact_kind  phone | external_document | other
  appointment_id (solo visit)             reason
  status         open | closed            close_reason  completed | cancelled | no_show | closed | visit_started
  opened_at / opened_by · closed_at / closed_by · entry_late
     │ 1..N
     ▼
episode_snapshots            (append-only: trigger che rifiuta UPDATE e DELETE)
  kind           entry | exit
  format_version · content (jsonb) · content_hash (SHA-256) · taken_at / taken_by
```

**Cosa entra nella fotografia:** anamnesi in corso con allerte e gruppo sanguigno, diagnosi
non risolte, terapie attive, tutto l'odontogramma, piani di cura aperti con tutte le voci. È
composta lato server nella stessa transazione dell'evento che la scatta. La forma canonica
(liste ordinate con chiavi stabili, chiavi JSON in ordine alfabetico, date `YYYY-MM-DD`)
rende l'hash riproducibile: rileggere il `jsonb` e riserializzarlo dà lo stesso hash.

**Ciclo di vita:**
- la visita si apre quando l'appuntamento passa a **«in corso»**, e si chiude alla chiusura
  della seduta o quando l'appuntamento diventa completato, annullato o non presentato;
- un solo episodio aperto per paziente (indice unico parziale); una seconda visita «in
  corso» risponde `409 EPISODE_VISIT_ALREADY_OPEN`, mentre un contatto aperto si chiude da solo
  (`visit_started`);
- se la seduta registra esiti su una visita mai passata da «in corso», l'ingresso si scatta in
  quel momento, **prima** di scrivere gli esiti, marcato `entry_late`;
- una visita riaperta aggiunge un'altra uscita: le fotografie non si cancellano mai, vale
  l'ultima;
- diario e documenti scritti con un episodio aperto ricevono `episode_id` lato server; le note
  d'ingresso e d'uscita sono voci di diario con `note_kind`.

**Richiesta di apertura.** Prima di un salvataggio clinico (odontogramma, anamnesi, diagnosi,
prescrizioni, diario, documenti) senza episodio aperto, il frontend propone di mettere «in
corso» la visita di oggi, di aprire un contatto, o di salvare **fuori episodio**. Il sistema
propone, non crea da solo. La modifica fuori episodio comparirà come «cambiato fuori episodio»
nell'episodio successivo.

**Consultazione.** Differenze per area (anamnesi, diagnosi, terapie, odontogramma, piani) e un
riepilogo testuale, una riga per cambiamento (es. `Odontogramma: 36 O, M: carie → otturazione`).
Sono calcolati da una funzione **pura e deterministica** (`EpisodeDiffService`), senza AI: il
riepilogo scritto dall'AI è Fase 2. Le API (`/api/patients/{id}/episodes/**`) sono riservate ai
ruoli clinici anche in lettura.

**Resta da fare:** il collegamento diretto (`encounter_id`) di diagnosi, prescrizioni, anamnesi
e odontogramma all'episodio. La consultazione non ne ha bisogno, perché lavora sulle differenze
fra fotografie.

### 2.4 Anamnesi: tre stati, non due

Una voce di anamnesi assente è ambigua: non si distingue *"negato dal paziente"* da *"non
indagato"*. Il modello di riferimento richiede per ogni voce: **stato** (presente /
assente / non noto), **fonte** (paziente, caregiver, documento, professionista), data di
rilevazione, autore, eventuale data di risoluzione.

La struttura a catalogo (categorie e voci, con selezioni per paziente) è già in essere: il
lavoro è sullo stato, non sull'impianto.

## 3. Ciclo di vita dell'informazione clinica

```text
Accettazione → identificazione → anamnesi e consensi
      → ENCOUNTER
            ├── osservazioni e odontogramma
            ├── immagini e analisi
            ├── diagnosi
            ├── piano e consenso
            └── procedure e prescrizioni
      → revisione del professionista
      → FINALIZZAZIONE (hash, blocco modifiche)
      → follow-up, addendum
```

### 3.1 Stati di una nota clinica

| Stato | Significato | Azioni consentite |
|---|---|---|
| Bozza | in compilazione | modifica, eliminazione controllata |
| Da revisionare | completa, non finalizzata | revisione, ritorno in bozza |
| **Finalizzata** | approvata dal professionista | **sola lettura**, addendum |
| Rettificata | sostituita logicamente da una rettifica | consultazione con collegamento |
| Annullata | non valida ma conservata | consultazione con motivazione |

Alla finalizzazione la nota riceve identificatore, autore, timestamp e **impronta
(SHA-256)**; il contenuto non è più modificabile direttamente.

### 3.2 Correzione: addendum, non UPDATE

L'unica via di correzione di una nota finalizzata è l'**addendum**, che contiene:
riferimento all'elemento originale, motivo, testo, autore, data e ora, ed eventuale
impatto sul piano o sul paziente.

Il sistema deve mostrare **quale versione è clinicamente valida** senza eliminare la
storia. È il requisito da cui discende il valore probatorio dell'intera cartella.

### 3.3 Cancellazione

Il dato clinico non si cancella fisicamente nell'operatività ordinaria: si annulla
logicamente, conservando l'originale. La rimozione definitiva è una procedura eccezionale,
guidata dalla politica di retention e documentata.

Nota di coerenza già in essere: i documenti fiscali sono **inalienabili** — non vengono
rimossi insieme al paziente, per obbligo di conservazione.

## 4. Audit trail

L'audit è un'entità **separata** dal log applicativo, **append-only**, con accesso
riservato.

**Eventi da registrare:** autenticazione (successo e fallimento) · apertura di una cartella
· visualizzazione di categorie sensibili · creazione, modifica, finalizzazione · addendum e
annullamenti · download, stampa, export · condivisione · azioni degli agenti AI · variazione
di ruoli · accessi di emergenza.

**Campi:** evento, tenant, utente e ruolo, **paziente**, risorsa, azione, esito, data/ora,
sessione, motivazione, correlation ID, versione applicativa.

L'audit non è un requisito burocratico: è la precondizione di tre cose che il prodotto
promette — il **report degli accessi** al paziente che lo richiede, i **KPI** di qualità
(nessuno dei quali è misurabile senza), e la capacità di rispondere a un controllo.

Oggi esiste l'audit delle **azioni AI** (`ai_audit_log`, vedi [04-AI](04-AI.md));
l'audit clinico generale è la prima milestone tecnica della Release 1.x.

Il **modello probatorio** completo — cosa rende un audit *opponibile* e non solo
"un log", il taglio tra il minimo obbligatorio al go-live (Tier 1) e ciò che è
differito (Tier 2), e le decisioni di design ancora aperte (concorrenza della
hash chain, dove vive il log, come si instrumentano le letture, modulo interno
vs servizio riusabile) — è in [13-Audit-Trail](13-Audit-Trail.md).

## 5. Interoperabilità: strategia duale

Il modello interno è **deliberatamente non modellato su uno standard di scambio**. Gli
standard evolvono; il dominio interno deve restare stabile. L'integrazione avviene con
**adapter**, non copiando un profilo dentro il database.

Mappatura di riferimento (post Release 1.x):

| DentalCare | FHIR |
|---|---|
| Patient | Patient |
| Provider | Practitioner + PractitionerRole |
| Clinic | Organization + Location |
| **Encounter** | Encounter |
| Anamnesi / riscontro | Observation |
| Allergia | AllergyIntolerance |
| Diagnosi | Condition |
| Prestazione eseguita | Procedure |
| Piano di cura | CarePlan |
| Prescrizione | MedicationRequest |
| Analisi radiologica | ImagingStudy + DiagnosticReport |
| Documento | DocumentReference |
| **Consenso** | Consent |
| Origine del dato | Provenance |
| **Audit event** | AuditEvent |

Le tre righe in grassetto sono oggi assenti: non a caso sono le stesse che mancano al
valore probatorio. L'interoperabilità non è un livello che si aggiunge sopra — è una
conseguenza dell'aver modellato bene il dominio.

L'odontogramma richiede un profilo applicativo dedicato: codici dente/superficie con
mappature esplicite, senza inventare estensioni non governate.

## 6. Identità del paziente

- Identificatore interno **UUID**, non significativo.
- Il **codice fiscale non è una chiave primaria**: può mancare, essere errato o cambiare.
  È validato quando presente, opzionale per i pazienti stranieri, ed è cifrato a riposo
  con indice cieco per la ricerca esatta (vedi [11-Data-Encryption](11-Data-Encryption.md)).
- **Stato del record** (attivo / deceduto / duplicato / archiviato) e **merge dei
  duplicati** con approvazione e audit: Release 1.x.

Il duplicato non è un fastidio anagrafico: è il rischio di attribuire dati clinici alla
persona sbagliata. Per questo la procedura di merge è tracciata come un atto, non come una
correzione.

## 7. Documenti e immagini

Ogni oggetto ha metadati clinici, non solo un nome file: tipo di documento, paziente,
episodio, data dell'esame (distinta dalla data di caricamento), autore del caricamento,
MIME verificato.

Su object storage il percorso è costruito su **identificatori opachi**: nessun nome,
cognome o codice fiscale nel path.

Release 1.x aggiunge: **impronta SHA-256**, verifica del MIME reale, scansione malware,
controllo di coerenza tra immagine e paziente selezionato.

## 8. Riepilogo dello stato

| Livello | Stato |
|---|---|
| Modello dati clinico | ✅ ampio e strutturato |
| Provenienza dell'output AI | ✅ modellata (origine + analisi di riferimento) |
| Cifratura dei dati identificativi | ✅ in produzione |
| Separazione dei ruoli | ✅ implementata · verifica end-to-end in Release 1.x |
| **Encounter** (ciclo della seduta) | ✅ implementato (#56-#62) · FK `encounter_id` su diagnosi, prescrizioni, anamnesi e odontogramma in Release 1.x |
| **Episodi clinici con fotografie prima/dopo** | ✅ implementato (#67, Fase 1) · riepilogo AI in Fase 2 |
| Odontogramma aggiornato dalla seduta, con autore | ✅ implementato (#65), solo su conferma del medico |
| **Finalizzazione e addendum** | 🔨 Release 1.x |
| **Consensi versionati** | 🔨 Release 1.x |
| **Audit trail clinico** | 🔨 Release 1.x |
| Storicità dell'odontogramma | 🟡 confronto fra date via episodi (#67) · storia per singolo reperto in Release 1.x |
| Merge duplicati | 🔨 Release 1.x |
| Conservazione a norma · firma qualificata · FHIR · FSE | ⏸️ post Release 1.x |

La lettura onesta: **il nucleo dati è solido, il livello della prova è in costruzione.**
È il profilo tipico di un prodotto costruito rapidamente: la parte comprimibile è avanti,
quella che dipende da processo e governance segue. La Release 1.x esiste per chiudere
questa distanza prima che il primo paziente reale entri nel sistema.

---

## Riferimenti

- [Release 1.x](../03-Product-Roadmap/Release-1.x.md) — scope e criteri di go-live
- [07-Security](07-Security.md) · [11-Data-Encryption](11-Data-Encryption.md) · [13-Audit-Trail](13-Audit-Trail.md) · [04-AI](04-AI.md)
- Regolamento (UE) 2016/679 (GDPR) · HL7 FHIR · DICOM · FSE 2.0
