# Fase 4 — DentalCare Clinical Intelligence (DC-CI)

**Versione:** 1.0 · **Data:** 12 novembre 2026  
**Stato:** 📋 Progettato — **non implementato, non validato clinicamente e non autorizzato all'uso clinico**  
**Ambito:** DentalCare Pro SaaS multi-tenant; supporto decisionale odontoiatrico, evoluzione clinica e richiami  
**Specifica tecnica:** [17 — Clinical Event Model, FHIR e Predictive AI](../../04-Architecture-Handbook/17-Clinical-Event-Model-and-Predictive-AI.md).

> **Nomenclatura:** «Fase 4» è il nome di questo progetto evolutivo richiesto dal committente. Non coincide automaticamente con la **Release 4.x** del catalogo, che ad oggi descrive una visione più ampia non pianificata. La **Fase 2** resta dedicata all'AI Copilot clinico e all'analisi delle ortopanoramiche (con i gate regolatori previsti). La Fase 4 riutilizza gli output della Fase 2 e non ne anticipa la messa in uso clinico. La collocazione funzionale della Fase 3 non è ridefinita in questo documento.

## 1. Executive summary

DentalCare Clinical Intelligence trasforma informazioni registrate in cartella in una **storia clinica longitudinale, verificabile e interrogabile**, sulla quale costruire ricerca di evidenze scientifiche e, dopo validazione, modelli prognostici. La soluzione combina:

1. **Clinical Event Model (DC-CEM)**: eventi ordinati nel tempo per paziente, dente, superficie/sito, impianto/dispositivo, trattamento ed esito.
2. **RAG clinico e scientifico**: recupero controllato di fonti mediche e documenti del solo paziente autorizzato.
3. **ML predittivo**: modelli specifici per endpoint clinico, con orizzonte, calibrazione, limiti e monitoraggio.
4. **LLM Clinical Assistant**: sintesi spiegabile di fatti, fonti e risultati predittivi, senza generazione autonoma di probabilità.
5. **Care Planning & Recall Intelligence**: proposte motivate di monitoraggio, piano di cura e richiami, sempre soggette al professionista.

**Principio:** l'AI propone, il professionista decide. Il sistema **non** diagnostica autonomamente, non scrive in cartella senza conferma, non sostituisce la valutazione clinica e non tratta un risultato ML come una certezza.

## 2. Obiettivi e casi d'uso

| Caso | Risultato atteso | Unità primaria |
|---|---|---|
| Ricostruzione della storia | Timeline clinica completa con fonti e rettifiche | Paziente |
| Temporal Odontogram | Stato di un dente/superficie alla data T | Dente, sito |
| Monitoraggio dei percorsi | Diagnosi → procedure → controlli → esiti | Care Pathway |
| RAG clinico | Risposte motivate con fonti e data della documentazione | Paziente, documento |
| Segnali deterministici | Parametri peggiorati, follow-up mancanti, interventi non conclusi | Evento, percorso |
| Previsione complicanze | Stime calibrate di specifici eventi futuri, **solo dopo validazione** | Paziente, dente, impianto, percorso |
| Supporto al piano di cura | Segnalazione delle criticità e delle alternative da valutare | Piano, percorso |
| Richiami personalizzati | Proposta di intervallo e motivazione clinica, non prenotazione autonoma | Paziente |
| Analisi esiti | KPI e coorti aggregate nei confini giuridici autorizzati | Popolazione |

### Non-obiettivi

- Diagnosi, prescrizioni o terapie autonome.
- Punteggi di rischio inventati dal modello linguistico.
- Uso dei dati di tutti gli account per training senza una separata analisi legale, DPIA e autorizzazione.
- Conversione dell'odontogramma in un unico embedding privo di semantica temporale.
- Sostituzione del database gestionale con FHIR, pgvector o Qdrant.
- Riclassificazione automatica di un suggerimento AI in «diagnosi confermata».

## 3. Dipendenze reali e confini delle fasi

Il [modello della cartella clinica](../../04-Architecture-Handbook/12-Clinical-Record-Model.md) documenta funzionalità già esistenti: sedute, stato odontogramma, **clinical_episodes** (#67, **visita o contatto**), snapshot append-only di ingresso/uscita, prestazioni e collegamenti ai piani. La Fase 4 **estende** questi oggetti senza duplicarli.

| Livello | Stato / strategia |
|---|---|
| Core gestionale e cartella | Fonte autorevole; invariati i workflow probatori preesistenti |
| Fase 2 — Copilot e ortopanoramiche | Produce contestualizzazione della cartella e reperti radiografici proposti, da validare |
| Fase 4 — DC-CEM | Proiezioni strutturate e registri longitudinali derivati da dati originali |
| Fase 4 — RAG | pgvector e corpus governato, accesso tramite API autorizzate |
| Fase 4 — ML | Solo dopo audit di completezza, etichette ed esiti verificabili |
| Fase 4 — piani/richiami | Sui servizi già esistenti, con anteprima e conferma medica |
| Interoperabilità FHIR | Adapter separato; server HAPI FHIR come PoC non obbligatorio in produzione |

Le fasi del prodotto e le **Release 1.x/2.x/3.x/4.x** della roadmap storica hanno finalità differenti: il presente documento non elimina il precedente confine MDR/CE della Release 2.x.

## 4. Architettura logica

~~~mermaid
flowchart TB
  UI[Angular: Timeline / Clinical Intelligence] --> API[Spring Boot: Auth / RBAC / Audit / Conferme]
  API --> CORE[(PostgreSQL: schema-per-tenant, cartella)]
  CORE --> OUTBOX[Outbox e proiezioni idempotenti]
  OUTBOX --> CEM[Clinical Event Model]
  CORE --> DOC[(MinIO: originali / immagini)]
  CEM --> RAG[Clinical RAG Service]
  DOC --> RAG
  SCI[Corpus scientifico governato] --> RAG
  RAG <--> VEC[(PostgreSQL + pgvector)]
  CEM --> FEATURES[Feature snapshots / dataset versionati]
  FEATURES --> ML[ML Prediction Service]
  ML --> ORC[Clinical Intelligence Orchestrator]
  RAG --> ORC
  API --> ORC
  ORC --> LLM[LLM via gateway approvato]
  LLM --> API
  API --> HUMAN[Anteprima e decisione del clinico]
  HUMAN --> APP[Servizi applicativi piani / agenda / richiami]
  CEM --> FHIRMAP[FHIR R4 Adapter]
  FHIRMAP -. PoC .-> HAPI[HAPI FHIR JPA isolato]
~~~

### Responsabilità dei componenti

| Componente | Tecnologia prevista | Responsabilità |
|---|---|---|
| Core e Clinical Event API | Spring Boot + SQL-first | Verifica identità, autorizzazione, lettura/scrittura dei dati autorevoli |
| Proiezioni temporali | PostgreSQL, transactional outbox, worker | Ricostruzione degli eventi senza alterare la fonte, replay e idempotenza |
| Corpus/RAG | pgvector + full-text PostgreSQL | Retrieval di testi con filtri server-side e citazioni |
| Originali | MinIO | Documenti, ortopanoramiche e file clinici |
| ML | Python, scikit-learn / boosting / survival | Training, stime e controllo scientifico del modello |
| Clinical Orchestrator | Python FastAPI o Spring Boot (scelta al design review) | Compone risultati ML, contesto paziente ed evidenze RAG |
| LLM | Gateway già documentato | Spiegazione e interazione, non ground truth |
| FHIR Adapter | Spring/HAPI FHIR | Interoperabilità verso risorse FHIR R4, senza vincolo sul database interno |
| Monitoraggio | Metriche, audit, job governati | Drift, errori, richiami da revisionare, rollback |

**Isolamento:** il prodotto usa **uno schema PostgreSQL per account/tenant** (ad es. t_XXXXXXXX), con più cliniche/sedi possibili nello stesso schema. Non introdurre un'unica tabella clinica globale con filtro tenant_id come sostituto del confine esistente. I worker ricevono un contesto firmato/autorizzato; non ricavano il tenant da testo o richieste LLM.

## 5. Clinical Event Model — quattro livelli più percorso

Lettura logica: **paziente → struttura anatomica → superficie/sito → eventi e trattamenti**. Il **Care Pathway** collega trasversalmente i singoli eventi clinici di uno stesso problema, anche su visite differenti. Non è una gerarchia fisica rigida: eventi multi-sito, arcate, mandibola, tessuti molli e anamnesi sistemica richiedono relazioni molti-a-molti.

| Oggetto | Identità | Esempi |
|---|---|---|
| Paziente | UUID interno del paziente nell'account | Anamnesi, trattamenti, fattori di rischio |
| Dente naturale | UUID persistente + codice FDI e tipo dentizione | 36 permanente, 75 deciduo |
| Superficie coronale | Codice sito e relazione al dente | Mesiale, distale, occlusale, vestibolare, linguale/palatale |
| Sito parodontale | Identità del sito e data di misura | 6 punti, profondità, BOP, recessione |
| Altre sedi | Struttura anatomica specifica | Radice, canale, regione periapicale, mucosa, osso, arcata |
| Impianto/protesi/restauro | UUID e ciclo di vita distinti dal dente naturale | Impianto posizione 36, corona, ponte |
| Evento | UUID, tipo, data clinica, fonte, autore, stato | Diagnosi, procedura, osservazione, controllo, complicanza |
| Care Pathway | UUID del problema/percorso longitudinale | Endodonzia del 36 su tre sedute |

**Distinzione essenziale:** clinical_episodes **esiste già** e rappresenta «visita/contatto con fotografie di stato»; non va riutilizzata semanticamente come problema clinico pluriennale. Se necessario creare **care_pathways** per attraversare più clinical_episodes, associando episodi, diagnosi, procedure e follow-up.

### Modello temporale e provenienza

Registrare **effective_at** (evento avvenuto), **recorded_at** (registrazione da parte di un operatore) e **ingested_at** (derivazione/indicizzazione). Mantenere fonte/versione, autore, stato di verifica, supersedes_id e motivo della rettifica. Il dato finale resta distinguibile da «proposta AI», «importazione da verificare» e «osservazione confermata».

**Dato mancante non significa esito negativo.** Per prognosi registrare follow-up perso, sconosciuto, censurato, verificato favorevole e complicanza verificata. Le feature a tempo T non possono utilizzare informazioni registrate o divenute disponibili dopo T.

### Temporal Odontogram

Rappresentazione grafica *derivata* dallo storico: la situazione al momento T, le superfici cambiate, gli eventi di trattamento, gli snapshot ingresso/uscita delle visite e le rettifiche. Nessun aggiornamento automatizzato dello stato odontografico da parte dell'AI: restano le regole di conferma già documentate.

## 6. RAG, conoscenza scientifica e pgvector

Si mantengono due domini logici separati:

1. **Corpus scientifico:** linee guida, protocolli e letteratura con licenza, fonte, versione, data, validità e specialità; **senza dati identificativi del paziente**.
2. **Corpus documentale clinico autorizzato:** note/referti/documenti con scope di account, clinica, paziente, ruolo e stato della cartella.

Per dati quantitativi/eventi utilizzare SQL e Clinical Event API deterministiche; per i testi utilizzare ricerca full-text + similarity vettoriale. I risultati per il Copilot devono indicare **provenienza, data, incertezza e citazione**. Gli embedding non sostituiscono diagnosi o outcome strutturati.

**Scelta ADR-04-02:** partire da **PostgreSQL + pgvector**. Ogni schema tenant conserva le risorse documentali proprie e applica filtri e permessi prima del retrieval. Il corpus scientifico, privo di PHI, può avere repository e schema separati. Usare HNSW e/o ricerca esatta in base ai benchmark; l'applicazione deve avere un'interfaccia vettoriale astratta per poter passare in futuro a Qdrant senza cambiare Copilot.

**Quando valutare Qdrant:** indici davvero grandi, alte concorrenze e filtri complessi con p95/recall fuori obiettivo *dopo* tuning pgvector. Prima valutare isolare carico vettoriale dal DB transazionale tramite istanza PostgreSQL dedicata e replica/proiezioni conformi alla policy di accesso. Nessuna soglia rigida in numero di pazienti.

## 7. Machine Learning predittivo

L'LLM non calcola direttamente il rischio; un **modello predittivo versionato** produce probabilità calibrate e limiti. La prima versione può funzionare con regole cliniche esplicite e RAG **senza alcuna percentuale ML**.

| Pilota | Outcome da definire clinicamente | Orizzonte illustrativo |
|---|---|---|
| Parodontologia | Progressione misurata/diagnosticata secondo definizione condivisa | 6–12 mesi |
| Endodonzia | Ritrattamento non programmato | 12–24 mesi |
| Implantologia | Specifica complicanza implantare verificata | 12–36 mesi |
| Restaurativa | Rifacimento/sostituzione documentato e motivato | 12–24 mesi |
| Adesione ai richiami | Mancata presentazione al controllo (endpoint operativo, non clinico) | 3–12 mesi |

**Protocollo minimo:** coorte, data indice, caratteristiche osservabili allora, definizione verificabile del target, finestra di osservazione, censura, baseline, split temporale/per paziente, valutazione fra cliniche, calibration curve, AUPRC/AUROC, Brier, falsi allarmi e utilità clinica. Per *time to event*: Cox/Random Survival Forest, censura e metriche appropriate. Preferire baseline interpretabile (regole/logistica) prima di boosting; reti temporali solo se volumi e qualità lo giustificano.

Conservare dataset, feature, split, versioni, ambiente e model card. Niente training autonomo su nuovi pazienti di produzione, niente apprendimento continuo senza change control. Shadow mode e validazione prospettica/esterna precedono qualunque proposta d'uso clinico.

### Dati degli altri pazienti

Le cartelle individuali di altri pazienti **non** vengono recuperate dall'LLM per analogia. I dati della popolazione servono per modelli e statistiche **solo nel perimetro autorizzato**. L'uso cross-tenant o federato va progettato separatamente: basi giuridiche per dati sanitari, rapporti di titolarità, DPIA, minimizzazione, protezione da re-identificazione, qualità e governance. Pseudonimizzazione **non** equivale ad anonimizzazione.

## 8. Supporto ai piani e richiami

Il motore combina: **fatti di cartella**, **regole cliniche**, **evidenze scientifiche** e, se disponibili/validati, **risultati ML**. La proposta contiene fonti, data, orizzonte, incertezza e dati mancanti. Il dentista può accettare, modificare o respingere, documentando la decisione. Solo i servizi applicativi confermati possono aggiornare piano di cura, richiami e agenda.

Lo scheduler può segnalare follow-up mancanti e predisporre **bozze**; non imposta autonomamente priorità cliniche né esegue nuove prestazioni. Distinguere l'ottimizzazione degli slot dall'accessibilità sanitaria: una previsione di no-show non deve penalizzare il paziente.

## 9. Decisioni architetturali (ADR)

| ADR | Decisione | Motivazione |
|---|---|---|
| ADR-04-01 | PostgreSQL come system of record, schema-per-tenant | Riuso coerente dell'architettura e dei confini di accesso |
| ADR-04-02 | pgvector come prima implementazione RAG; Qdrant eventuale | Minore complessità, SQL; migrazione solo su benchmark |
| ADR-04-03 | FHIR R4 tramite adapter | Interoperabilità senza cambiare schema interno |
| ADR-04-04 | HAPI FHIR JPA PoC opzionale in sandbox separata | Verifica dei mapping, non dipendenza operativa del gestionale |
| ADR-04-05 | Care Pathway separato da clinical_episodes | Non duplicare né alterare la semantica di visita/contatto già implementata |
| ADR-04-06 | LLM distinto da ML, niente percentuali sintetiche | Prognosi verificabile, controllabile e calibrabile |
| ADR-04-07 | Outbox e proiezioni idempotenti | Nessuna doppia scrittura disallineata dei dati clinici |
| ADR-04-08 | Approvazione clinica obbligatoria nel backend | La supervisione non può essere soltanto un prompt |
| ADR-04-09 | MinIO conserva originali, retrieval conserva riferimenti | Integrità e provenienza documentale |
| ADR-04-10 | Contenitori Docker separati e monitorati | Rollback, isolamento, deployment su infrastruttura Proxmox |

## 10. FHIR e HAPI

La mappatura FHIR R4 è **un contratto di scambio**: Patient, Encounter, Condition, Procedure, Observation, CarePlan, ServiceRequest, Appointment, ImagingStudy (quando sono presenti studi DICOM), DiagnosticReport, DocumentReference, BodyStructure e Provenance. Un *Care Pathway* può corrispondere a **più** risorse FHIR, non a una tabella 1:1. Terminologie e profili odontoiatrici richiedono governance e test.

**HAPI FHIR JPA**: sperimentazione isolata con database PostgreSQL dedicato, sincronizzazione unidirezionale iniziale, soltanto dati sintetici. Lo starter non è dotato automaticamente di autenticazione, audit e isolamento pronti per dati clinici: non esporre pubblicamente né alimentare con dati reali senza hardening e verifiche. Il core DentalCare deve continuare a funzionare se HAPI non è raggiungibile.

## 11. Privacy, sicurezza e conformità

Un software che prevede complicanze e informa decisioni diagnostico-terapeutiche può rientrare nel **Medical Device Software** ai sensi del MDR (Reg. UE 2017/745), con possibile applicazione della regola 11; occorre determinare destinazione d'uso, classificazione, evidenze cliniche e percorso CE prima della messa in uso. Considerare anche AI Act, GDPR e relativi obblighi. **Human-in-the-loop non esenta automaticamente da MDR.**

- Controlli **tenant → clinica → ruolo → paziente**, server-side, per API, job, RAG e ML.
- Nessuna trasmissione a fornitori AI non approvati; rispettare il gateway e la minimizzazione documentati.
- Audit di consultazioni, inferenze, modello/versione, fonti, azioni proposte, conferma e accessi negati; niente PHI nei log tecnici.
- Cifratura e backup per tenant; retention, export e cancellazioni secondo policy e valutazione DPO.
- Piani qualità: gestione dei rischi, validation protocol, model card, kill switch, rollback, monitoraggio del drift, formazione e incident management.
- Il training su dati sanitari per finalità ulteriori richiede verifica specifica di base giuridica, ROPA/DPIA e accordi; non abilitato da questo documento.

Vedi [proposta voci DPIA D-105..D-109](../../06-Compliance/Fase-4-Clinical-Intelligence-DPIA-Addendum.md). Da integrare nel registro ufficiale dopo revisione DPO.

## 12. Roadmap per milestone/gate (nessuna data promessa)

| Gate | Attività principali | Deliverable | Criterio di uscita |
|---|---|---|---|
| M0 — Audit | Inventario tabelle, volumi, flussi, legittimità dei dati | Data dictionary e gap analysis | Nessuna sovrapposizione con clinical_episodes; ruoli documentati |
| M1 — CEM | Anatomia, siti, percorsi, eventi, esiti, vincoli | ERD, migrazioni per tenant, test | Isolamento e provenienza verificati |
| M2 — Timeline | Proiezioni, outbox, backfill, Temporal Odontogram | API temporali, UI lettura, riconciliazione | Ricostruzioni coerenti con sorgenti e snapshot |
| M3 — RAG | Corpus, pgvector, ACL, citazioni, prompt-injection tests | Retrieval clinico e scientifico | Accessi autorizzati, nessun dato cross-tenant |
| M4 — FHIR PoC | Mapping, profili, HAPI isolato, validator | Bundle sintetici, mapping spec | No dati reali esposti, scelta go/no-go |
| M5 — ML Data | Target, coorte, feature, etichette, missingness, consenso/diritti | Dataset/versioni, report qualità | Follow-up ed esiti sufficienti, altrimenti stop |
| M6 — Model validation | Baseline, boosting/survival, split e calibrazione | Model card, validation report, shadow mode | Soglie predefinite superate e verifiche cliniche |
| M7 — Clinical UI | Piani/richiami, override, spiegazioni, audit | Interfaccia e flussi di approvazione | Gate MDR/AI Act/GDPR e test end-to-end soddisfatti |
| M8 — Operations | Drift, revalidation, incidenti, rollback | SOP, dashboard, procedure retraining | Monitoraggio continuo governato |

**Sequenza:** M0→M1→M2, quindi M3 e M4 in parallelo; M5 richiede output M1/M2 e qualità sufficiente; M6→M7→M8 solo dopo gate scientifici e normativi. Alcune attività M0–M4 possono essere prototipate con dati fittizi senza pretendere utilizzo sanitario.

## 13. Acceptance criteria e KPI

### Acceptance criteria

- Test su: dentizione decidua/permanente, siti parodontali, dente estratto, impianto, più superfici, evento multi-dente, rettifica retroattiva.
- Ogni proiezione porta source_id, versione, timestamp; reprocessing idempotente.
- Timeline a T non legge rettifiche o osservazioni divenute note dopo T.
- Test negativi cross-tenant, cross-clinica e role-based anche per job/RAG.
- Nessuna diagnosi da output radiologico AI non validato.
- Nessun piano/richiamo scritto automaticamente: anteprima e approvazione registrate.
- Nessuna stima prognostica senza validazione, calibrazione e intended use definiti.
- Test di restore, ricostruzione embedding, disattivazione AI, tracciabilità modello-fonte.

### KPI da misurare (non ancora disponibili)

Completezza timeline; quota procedure legate a dente/sito; eventi con esito osservabile; qualità del backfill; precisione delle citazioni; p95 retrieval, recall e filtri; falsi allarmi; sensibilità/precisione e calibrazione; tasso di override; richiami efficaci; drift; incidenti e violazioni cross-tenant (obiettivo zero).

## 14. Questioni aperte

- Scelta dei primi endpoint clinici in base ai dati realmente disponibili e a protocolli validati da odontoiatri.
- Terminologie, sistema FDI/ISO 3950 e profili FHIR odontoiatrici governati.
- Granularità esiti e disponibilità del follow-up esterno.
- Rapporti di titolarità nelle attività freelance e tra cliniche/sedi del medesimo account.
- Localizzazione dei servizi ML e benchmarking su volumi reali.
- Decisione sull'eventuale operatività del server FHIR dopo il PoC.
- Valutazione per funzione di qualificazione MDR, classificazione e claim ammissibili.

## 15. Riferimenti

**Interne:** [Product Roadmap](../Product-Roadmap.md) · [AI Roadmap](../AI-Roadmap.md) · [Clinical Record Model](../../04-Architecture-Handbook/12-Clinical-Record-Model.md) · [Multi-tenancy](../../04-Architecture-Handbook/06-Multitenancy.md) · [Audit Trail](../../04-Architecture-Handbook/13-Audit-Trail.md) · [DPIA](../../06-Compliance/dichiarazioni-dpia.md).

**Esterni:** [HL7 FHIR R4](https://hl7.org/fhir/R4/) · [pgvector](https://github.com/pgvector/pgvector) · [HAPI FHIR JPA Starter](https://github.com/hapifhir/hapi-fhir-jpaserver-starter) · [Commissione europea, linee guida MDCG](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en) · Reg. (UE) 2017/745 (MDR) · Reg. (UE) 2024/1689 (AI Act) · Reg. (UE) 2016/679 (GDPR).
