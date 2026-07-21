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
| **Encounter** | **episodio di cura effettivo** | 🔨 Release 1.x |
| **Anamnesi** | scheda clinica generale, voci strutturate da catalogo | ✅ implementato · tri-stato in Release 1.x |
| **Reperto dentale** (odontogramma) | condizione per dente/superficie, con origine | ✅ implementato · storicità in Release 1.x |
| **Diagnosi** | problema, stato, data, risoluzione | ✅ implementato |
| **Piano di cura** + voci | trattamento previsto | ✅ implementato |
| **Voce di cartella** (visita/prestazione) | atto eseguito, note cliniche, materiali | ✅ implementato · **finalizzazione in Release 1.x** |
| **Prescrizione** | terapia prescritta | ✅ implementato |
| **Documento** | immagini, referti, consensi acquisiti | ✅ implementato · integrità in Release 1.x |
| **Analisi AI** + revisione | proposta algoritmica e sua verifica | ✅ implementato (vedi [04-AI](04-AI.md)) |
| **Consenso** | consenso informato versionato | 🔨 Release 1.x |
| **Audit event** | accessi e operazioni | 🔨 Release 1.x |
| **Preventivo / Fattura** | piano economico | ✅ implementato |

### 2.1 Encounter — il perno mancante

Oggi l'appuntamento (pianificazione) e la voce di cartella (registrazione) esistono, ma
non c'è l'entità che lega **tutto ciò che è accaduto in una visita**: osservazioni,
odontogramma, immagini, diagnosi, piano, procedure.

L'`Encounter` (con stato *pianificato / in corso / concluso*) diventa il riferimento
comune delle entità cliniche. È il prerequisito di due cose: la ricostruzione della
cartella a una data storica, e la mappatura verso standard di scambio (§5).

### 2.2 Reperto dentale: da snapshot a storia

L'odontogramma è oggi la **fotografia dello stato corrente**: la condizione di un
dente/superficie viene aggiornata in luogo, con la sua origine (`manual` | `ai`) e il
riferimento all'analisi che l'ha prodotta. La provenienza è modellata bene; la **storia**
no.

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

### 2.3 Anamnesi: tre stati, non due

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
| **Encounter** | 🔨 Release 1.x |
| **Finalizzazione e addendum** | 🔨 Release 1.x |
| **Consensi versionati** | 🔨 Release 1.x |
| **Audit trail clinico** | 🔨 Release 1.x |
| Storicità dell'odontogramma | 🔨 Release 1.x |
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
