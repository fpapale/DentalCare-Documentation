# 17 — Clinical Event Model, FHIR e Predictive AI (Fase 4)

**Data:** 12 novembre 2026 · **Versione:** 1.0 · **Stato:** 📋 specifica target, NON implementata  
**Documento di progetto:** [Fase 4 — DentalCare Clinical Intelligence](../03-Product-Roadmap/Progetti/2026-11-12-fase-4-clinical-intelligence.md)

> Questo documento propone un'estensione futura della piattaforma e non descrive nuove funzioni già disponibili. Resta applicabile il [12 — Modello cartella clinica](12-Clinical-Record-Model.md) per la fotografia dello stato reale. Il database attuale è schema-per-tenant, non una singola tabella clinica multi-tenant condivisa.

## 1. Architettura di riferimento

~~~mermaid
flowchart LR
  F[Frontend Angular] --> B[Spring Boot: RBAC e API]
  B --> PG[(PostgreSQL: t_* per account)]
  B --> M[(MinIO: immagini/referti)]
  PG --> O[Transactional outbox]
  O --> W[Clinical Event Projection Worker]
  W --> CEM[Eventi / siti / percorsi / osservazioni]
  CEM --> R[Retrieval API]
  R <--> V[(pgvector e full text)]
  CEM --> X[Feature Extraction]
  X --> P[ML Scoring isolato]
  R --> OR[Clinical Orchestrator]
  P --> OR
  OR --> G[LLM Gateway autorizzato]
  G --> B
  B --> H[Revisione e conferma medico]
  H --> B
  CEM --> FM[FHIR Adapter R4]
  FM -. PoC .-> FS[HAPI FHIR JPA con DB separato]
~~~

**Fonte di verità:** tabelle cliniche esistenti in PostgreSQL, schemi t_* per **account**; le cliniche/sedi del medesimo account risiedono nello schema e richiedono filtri aggiuntivi. Le tabelle proposte sono **proiezioni/estensioni**, non un nuovo master di cartella. Per i dati preesistenti rispettare le regole di finalizzazione/addendum, l'immutabilità degli snapshot e i permessi per ruolo.

## 2. Ontologia operativa e cardinalità

### 2.1 Paziente, denti e siti

- **patient:** entità autorevole già esistente; ID opaco; codice fiscale mai chiave primaria.
- **clinical_site:** nodo anatomico con UUID, patient_id, parent_site_id facoltativo, site_kind, code_system/code, valid_from/to. Nodi: dente naturale, superficie coronale, sito parodontale, radice, canale, regione periapicale, gengiva, tessuto, osso, arcata ecc.
- **FDI ISO 3950:** designazione dentaria; non usare FDI come PK. Conservare *dentition*, esistenza/stato temporale. Denti decidui e permanenti successori non condividono l'identificativo; impianto in sede 36 non è il dente naturale 36.
- **clinical_device:** impianto/restauro/protesi identificabile con ciclo di vita, posizione, dati documentati e relazioni a siti; non confondere anatomia e dispositivo.
- **event_site:** N:N tra evento e localizzazioni, con ruolo della sede (primaria, associata, riferimento).

Le superfici coronali e i **sei siti parodontali di sondaggio** sono concetti differenti; misurazioni e unità sono tipizzate. Eventi senza sito (anamnesi generale) o su più siti (ponte, trauma, reperto diffuso) sono validi.

### 2.2 Encounter esistente ≠ Care Pathway nuovo

La cartella già contiene **clinical_episodes** (#67): una **visita** o un **contatto** con fotografie **entry/exit** append-only; non modificarne la semantica. Le registrazioni di seduta e gli item dei piani sono già collegate secondo le regole del core.

Introdurre **care_pathways** per un problema clinico longitudinalmente seguito (es. percorso endodontico sul dente 36 durante più visite). Consentire collegamento N:N tra pathways, clinical_episodes, procedure e osservazioni. Un pathway può essere rivalutato o riaperto, mantenendo storia e motivazione.

### 2.3 Eventi, relazioni e versioni

| Concetto | Campo minimo | Significato |
|---|---|---|
| Identità | event_id, patient_id, clinic_id | Univocità e scope di accesso |
| Classificazione | event_type, clinical_code, code_system, code_version | Semantica verificabile |
| Tempo | effective_at, recorded_at, ingested_at | Quando avvenuto / registrato / derivato |
| Provenienza | source_type, source_id, source_version | Record originale e sua revisione |
| Validità | verification_state, clinical_status, certainty | Fatti/proposte/incertezza distinti |
| Correzione | supersedes_event_id, reason | Rettifica logica senza distruzione |
| Relazioni | event_links (N:N, typed), event_sites (N:N) | Prima/dopo/deriva da/controllo di |
| Audit | author_ref, correlation_id, model_version se AI | Autore e lineage |

La lettura a data T deve poter distinguere **cosa era clinicamente accaduto** da **cosa risultava noto** al professionista in quel momento. Una nota aggiunta oggi su un evento del passato può aggiornare la ricostruzione retrospettiva, ma non deve entrare nel set di feature che simula una previsione fatta in passato.

## 3. Schema PostgreSQL concettuale

**ATTENZIONE:** DDL di riferimento per un nuovo design, **non** script di migrazione eseguibile così com'è. Non sono rappresentate qui tutte le foreign key verso tabelle reali, i vincoli compositi di autorizzazione, i trigger audit e le logiche di patch per tenant. Tali dettagli vanno derivati dall'audit di database/install.sql e dell'inizializzatore delle patch.

~~~sql
-- DA CREARE IN OGNI SCHEMA DEL TENANT (es. t_XXXXXXXX),
-- NON in uno schema clinico globale condiviso.

CREATE TABLE care_pathways (
  id UUID PRIMARY KEY,
  patient_id UUID NOT NULL,
  clinic_id UUID,
  pathway_type TEXT NOT NULL,
  status TEXT NOT NULL,
  started_on DATE,
  closed_on DATE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE clinical_sites (
  id UUID PRIMARY KEY,
  patient_id UUID NOT NULL,
  parent_site_id UUID REFERENCES clinical_sites(id),
  site_kind TEXT NOT NULL,
  code_system TEXT NOT NULL,
  site_code TEXT NOT NULL,
  dentition TEXT,
  valid_from TIMESTAMPTZ,
  valid_to TIMESTAMPTZ
);

CREATE TABLE clinical_events_v2 (
  id UUID PRIMARY KEY,
  patient_id UUID NOT NULL,
  clinic_id UUID,
  pathway_id UUID REFERENCES care_pathways(id),
  event_type TEXT NOT NULL,
  clinical_code TEXT,
  code_system TEXT,
  code_version TEXT,
  effective_at TIMESTAMPTZ,
  recorded_at TIMESTAMPTZ NOT NULL,
  ingested_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  source_type TEXT NOT NULL,
  source_id TEXT NOT NULL,
  source_version TEXT NOT NULL,
  verification_state TEXT NOT NULL,
  supersedes_event_id UUID,
  event_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  UNIQUE (source_type, source_id, source_version)
);

CREATE TABLE clinical_event_sites (
  event_id UUID NOT NULL REFERENCES clinical_events_v2(id),
  site_id UUID NOT NULL REFERENCES clinical_sites(id),
  site_role TEXT NOT NULL DEFAULT 'primary',
  PRIMARY KEY (event_id, site_id, site_role)
);

CREATE TABLE clinical_event_links (
  event_id UUID NOT NULL REFERENCES clinical_events_v2(id),
  related_event_id UUID NOT NULL REFERENCES clinical_events_v2(id),
  relation_type TEXT NOT NULL,
  PRIMARY KEY (event_id, related_event_id, relation_type)
);

CREATE INDEX ix_clinical_events_patient_time
  ON clinical_events_v2 (patient_id, effective_at, recorded_at);
CREATE INDEX ix_clinical_events_pathway_time
  ON clinical_events_v2 (pathway_id, effective_at);
CREATE INDEX ix_clinical_events_source
  ON clinical_events_v2 (source_type, source_id);
~~~

**Regole da completare in implementazione:** FK composite che impediscano legami tra pazienti/cliniche differenti; rispetto di soft delete e politiche retention; schema mapping per tenant; identità canoniche e terminologie validate; idempotenza anche dopo reprocessing; unicità semantica per sito/tempo; immutabilità dei record validati e addendum anziché UPDATE; test di collisione per i dispositivi impiantati.

Per gli **outcome** non basterà un flag bool: memorizzare definizione dell'evento, data, osservabilità, tempo a rischio, contesto, severità e provenienza. I follow-up censurati devono essere rappresentati esplicitamente. Per le osservazioni quantitative usare tipo, unità UCUM ove pertinente, metodo, lato/sito, autore e data.

## 4. Data pipeline e coerenza

**Pattern raccomandato:** nella stessa transazione applicativa che registra una modifica clinica, scrivere un messaggio nel **transactional outbox** del tenant. Il worker consuma in modo at-least-once, proietta con chiavi idempotenti e marca il checkpoint; i duplicati non devono moltiplicare gli eventi.

~~~mermaid
sequenceDiagram
    participant Dentist as Professionista
    participant API as Spring Boot
    participant DB as Cartella PostgreSQL
    participant Out as Outbox
    participant Worker as Event Projector
    participant CEM as DC-CEM
    participant RAG as Indicizzazione / FHIR
    Dentist->>API: Registra atto clinico
    API->>DB: Salvataggio con controlli
    API->>Out: Evento nella stessa transazione
    DB-->>Dentist: Conferma della scrittura originale
    Worker->>Out: Legge evento / checkpoint
    Worker->>DB: Legge record autorevole e sua versione
    Worker->>CEM: Upsert/versione idempotente
    Worker->>RAG: Aggiorna proiezioni derivate
~~~

**Recupero errori:** coda scarti, retry con backoff, dead letter e reconciliation giornaliera; processo di backfill con finestre temporali per tenant e check sui conteggi/hash delle sorgenti; nessun blocco dell'atto clinico se retrieval o FHIR è indisponibile. La latenza del Copilot non deve dipendere da un refresh completo degli embedding.

### 4.1 Derivazione da ortopanoramica

1. File originale in MinIO con metadati corretti e integrità verificabile.
2. Servizio di analisi immagini della Fase 2 genera **candidate observations** con regione, modello/versione, score ed eventuale segmento anatomico.
3. Il medico conferma, modifica o rifiuta; **solo la conferma** permette la registrazione come osservazione clinica.
4. Risultato e note conservano i riferimenti all'immagine, all'analisi, all'autore della revisione e all'esame eseguito.

Non assumere che ogni JPG/PNG sia DICOM. **ImagingStudy** è appropriato per imaging strutturato corrispondente a uno studio DICOM; per documenti o immagini non-DICOM prevedere **DocumentReference** e metadata appropriati. Non inviare pixel a FHIR come sostituto dell'archivio immagini.

## 5. API applicative e sicurezza

**Proposte di API, non endpoint esistenti:** 

| Endpoint | Metodo | Output / controllo |
|---|---|---|
| /api/patients/{patientId}/clinical-timeline | GET | Eventi datati, fonte e accesso autorizzato |
| /api/patients/{patientId}/clinical-timeline/at | GET | Snapshot a T e differenze |
| /api/patients/{patientId}/teeth/{toothId}/timeline | GET | Storia del singolo dente e dei siti |
| /api/patients/{patientId}/care-pathways | GET | Percorsi clinici collegati a più encounter |
| /api/patients/{patientId}/clinical-intelligence/evidence | POST | Ricerca RAG e citazioni, senza scrittura |
| /api/patients/{patientId}/clinical-intelligence/predictions | GET | **Solo** output di modelli validati e autorizzati |
| /api/patients/{patientId}/clinical-intelligence/recall-preview | POST | Proposta di richiamo, mai scrittura automatica |
| /api/patients/{patientId}/clinical-intelligence/confirm | POST | Decisione del professionista e delega al servizio autorizzato |

**Sicurezza:** applicare JWT/RBAC esistente, attribuzione della **clinica/sede** e criteri per-paziente a ogni lettura e a ogni job; il personale di segreteria non può ricevere parametri clinici o punteggi. I job batch non aggirano le regole legate a ruoli, audit, ownership e access policy. Ogni chiamata al modello esterno usa il gateway approvato; i log tecnici non conservano testo clinico in chiaro.

## 6. pgvector, RAG e dimensionamento

Il modello deve recuperare in modo distinto:

- **Dati strutturati**: query SQL e API deterministiche (es. tutte le procedure sul 36 entro T).
- **Documenti del paziente**: retrieval semantico/full-text con ACL e filtro clinica/paziente applicati **prima** della risposta.
- **Linee guida scientifiche**: repository separato con fonte, data, versione, licenza, specialità, stato di validità.

### 6.1 Esempio tabella di embedding per tenant

~~~sql
-- Esempio locale allo schema tenant: dimensione VECTOR da allineare
-- esattamente al modello embedding scelto (768 è solo dimostrativo).
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE clinical_document_chunks (
  chunk_id UUID PRIMARY KEY,
  patient_id UUID NOT NULL,
  clinic_id UUID NOT NULL,
  document_id UUID NOT NULL,
  source_version TEXT NOT NULL,
  content_hash TEXT NOT NULL,
  chunk_text TEXT NOT NULL,
  embedding VECTOR(768) NOT NULL,
  embedding_model TEXT NOT NULL,
  indexed_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX ix_chunks_filter
  ON clinical_document_chunks (clinic_id, patient_id);
CREATE INDEX ix_chunks_hnsw
  ON clinical_document_chunks USING hnsw (embedding vector_cosine_ops);
~~~

L'esempio **non** è una migrazione pronta all'uso: definire l'ACL completa, l'identità reale dei documenti, la chiave di cifratura applicabile e la strategia di retention prima dell'esecuzione. Evitare un singolo indice ANN condiviso da tutti i tenant, che può peggiorare isolation/recall. Verificare il comportamento dei filtri e la possibilità di scansioni iterative HNSW. Configurare un service account a privilegi minimi.

**Benchmark richiesto:** N di chunk e dimensione, percentili p50/p95, QPS concurrent, recall@K contro ricerca esatta, CPU/RAM/IO, qualità filtri, dimensioni indici e impatto sul DB transazionale. **Qdrant** è opzione condizionata ai risultati: non viene introdotto nell'MVP per il solo volume del database sanitario.

## 7. FHIR R4: mappature

| DC-CEM / core | Risorsa FHIR R4 | Considerazioni |
|---|---|---|
| Paziente | Patient | ID logico e riferimenti senza chiavi significative |
| Professionista/sede/account | Practitioner / PractitionerRole / Organization / Location | Separare identità, ruolo e luogo |
| Visita o contatto | Encounter | Mappare gli episodi visita/contatto esistenti, senza alterarli |
| Diagnosi | Condition | Codice, stato, onset, sede anatomica |
| Procedura | Procedure | Prestazione eseguita, autore, data e sede |
| Misurazione di sondaggio | Observation | Valore+unità+metodo+bodySite; differenziare i sei punti |
| Anatomia paziente-specifica | BodyStructure, codifiche e profili | Usare dove appropriato, non duplicare dente naturale/impianto |
| Trattamento pianificato | CarePlan / ServiceRequest | Piano vs richiesta di prestazione |
| Appuntamento | Appointment | Agenda distinta da procedura svolta |
| Ortopanoramica DICOM | ImagingStudy | Metadati e riferimenti alle istanze originali |
| Referto | DiagnosticReport | Risultati e interpretazione dell'esame |
| Documento esterno / file | DocumentReference | Metadati e riferimenti al file |
| Provenienza della registrazione | Provenance | Origine, autore, atti di mapping |
| Care Pathway | Composizione di più risorse | Non esiste un mapping universale tabella-risorsa 1:1 |

**HAPI FHIR JPA PoC:** container isolato con PostgreSQL separato, dati **sintetici**, API non pubbliche; sincronizzazione inizialmente monodirezionale da DentalCare. Definire namespace, profili, versioni e validazione. Non introdurre scritture bi-direzionali senza un'autorità chiara e risoluzione dei conflitti. Lo starter HAPI non comprende sicurezza e audit enterprise pronti per uso reale.

## 8. ML: specifica delle stime

### 8.1 Endpoint e unità di osservazione

Ogni esperimento formalizza **target**, unità, data indice, covariate disponibili alla data indice, inclusioni/esclusioni, orizzonte e definizione della complicanza. I trattamenti di confronto non sono automaticamente randomizzati: non interpretare correlazione come efficacia causale.

**Esempio endodontico:** unità = percorso su dente naturale; endpoint = ritrattamento non programmato entro 24 mesi; il denominatore include solo procedure con follow-up osservabile o applica tecniche di survival per la censura. Distinguere terapie in più sedute, controlli e re-interventi programmati.

### 8.2 Dataset e qualità

- Feature registry con sorgenti e definizioni; test di disponibilità a T.
- Estrazione su finestre cronologiche e separazione a livello paziente; evitare leakage fra visite dello stesso paziente.
- Validazione per clinica/sede e, se possibile, per centro esterno; documentare eterogeneità cliniche.
- Esito ignoto ≠ negativo, follow-up irregolare e registrazioni tardive gestiti formalmente.
- Baseline clinica e regressione logistica prima di boosting; per tempo-evento survival appropriata.
- Report AUROC/AUPRC, calibrazione, Brier, falsi positivi, intervalli e utilità della decisione; per survival c-index e metriche time-dependent.
- Versionamento degli split/dataset, model card, approval workflow, score fuori dominio bloccato.

### 8.3 Contratto di inferenza (schematico)

~~~json
{
  "patientRef": "opaque-patient-id",
  "target": "unplanned_endodontic_retreatment",
  "indexDate": "YYYY-MM-DD",
  "horizonMonths": 24,
  "modelId": "model-version-approved",
  "result": {
    "status": "insufficient_data_or_validated_score",
    "probability": null,
    "calibrationInfo": null,
    "warnings": ["example_only"]
  },
  "lineage": {
    "featureSnapshotId": "opaque-id",
    "predictionId": "opaque-id"
  }
}
~~~

**L'output sopra è solo un esempio di contratto e non un punteggio medico.** In assenza di validazione la probabilità rimane null. Il provider LLM non può scrivere valori di probabilità nello storage delle predizioni.

## 9. Sicurezza, conformità e governance

La presenza di informazioni cliniche predittive individualizzate può dare alla funzione una **destinazione medica** MDR, indipendentemente dal fatto che il dentista approvi il suggerimento. Prima di ogni claim/uso clinico: classificazione del software (MDR, regola 11 ove applicabile), processo qualità, valutazione clinica, documentazione di rischio, applicazione AI Act, DPIA/ROPA/DPA e governance del training. Qualsiasi pilota con pazienti reali richiede previa valutazione giuridica e clinica.

**Controlli obbligatori:** segregazione fra account e cliniche; accesso per ruolo; audit non modificabile; protezione MinIO; interruzione dei fornitori AI non autorizzati; registri versione modello e decisione; no PHI nei log; data retention, export e diritto di accesso; kill switch e rollback. Non convertire il consenso alla prestazione in autorizzazione generica al training.

## 10. Deployment previsto e osservabilità

Target da validare: stack Docker su infrastruttura Proxmox esistente, orchestrato con Docker Compose/Portainer, namespace/logica di progetto indipendente. Servizi proposti, **non ancora installati**:

- clinical-event-projector (worker + outbox consumer);
- clinical-intelligence-api (orchestratore RAG / risk / feedback);
- clinical-ml-service (training **separato** dall'inferenza per risorse e permessi);
- clinical-fhir-adapter (facoltativo per API di interoperabilità);
- hapi-fhir-jpa + postgresql-fhir (solo sandbox PoC);
- MLflow/model registry se scelto, con controllo autorizzazioni;
- monitoring e audit integrati nel sistema operativo esistente.

Separare ambiente demo/collaudo/produzione, segreti in secret management, subnet private, backup e test restore. Non pubblicare porte dei servizi ML/FHIR; ingresso tramite backend autorizzato. La collocazione host/VM/container e il dimensionamento CPU/GPU vanno decisi dopo misure e senza divulgare indirizzi interni nel wiki pubblico.

**SLO da definire:** p95 retrieval e prediction, tasso di errori worker, ritardo proiezioni, accuratezza del backfill, completezza outcome, drift, calibrazione periodica, anomalie ACL e incidenti. Per job predittivi batch preferire esecuzione controllata e auditata.

## 11. Criteri di accettazione tecnici

1. Riprodurre timeline a date passate su dati sintetici, comprese correzioni note solo successivamente.
2. Eseguire replay degli stessi outbox event N volte senza record duplicati.
3. Negare accesso cross-tenant, cross-clinica e segreteria a tutti gli endpoint clinici e ai job.
4. Preservare e verificare provenienza da record cartella e immagine MinIO.
5. Distinguere dente 75 e 35, impianto in posizione 36, sei siti parodontali, più superfici, siti senza dente.
6. Test di retrieval con filtro paziente + ruolo e prompt injection su contenuti recuperati.
7. FHIR validator su bundle sintetici e resilienza del gestionale a HAPI non disponibile.
8. Nessuna scrittura terapeutica da servizio ML/LLM senza approvazione professionale registrata.
9. Un modello non validato / dati insufficienti restituisce «nessuna stima».
10. Restore, rollback, cancellazione logica, audit trail e change management dimostrati.

## 12. Riferimenti

[Progetto Fase 4](../03-Product-Roadmap/Progetti/2026-11-12-fase-4-clinical-intelligence.md) · [12 — Clinical Record](12-Clinical-Record-Model.md) · [06 — Multi-tenancy](06-Multitenancy.md) · [13 — Audit](13-Audit-Trail.md) · [14 — LLM Gateway](14-LLM-NER-Gateway.md).

[HL7 FHIR R4](https://hl7.org/fhir/R4/) · [pgvector](https://github.com/pgvector/pgvector) · [HAPI FHIR JPA Starter](https://github.com/hapifhir/hapi-fhir-jpaserver-starter) · [Linee guida MDCG](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en).
