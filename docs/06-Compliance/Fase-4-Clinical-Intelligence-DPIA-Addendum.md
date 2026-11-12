# Addendum DPIA — Progetto Fase 4 Clinical Intelligence

**Data:** 12/11/2026 · **Stato:** 📋 decisioni progettuali, **non in esercizio**  
**Destinazione:** da incorporare, previa revisione DPO, nel registro ufficiale [dichiarazioni-dpia.md](dichiarazioni-dpia.md).  
**Progetto:** [Fase 4](../03-Product-Roadmap/Progetti/2026-11-12-fase-4-clinical-intelligence.md).

> Le voci D-105..D-109 sono **proposte per la DPIA**, non valutazioni giuridiche già concluse e non autorizzano trattamento ulteriore di dati reali. Non implicano che gli strumenti indicati siano stati sviluppati o rilasciati.

## D-105 — Nuova finalità di analisi predittiva clinica

**Decisione:** progettare predizioni individuali di complicanze, evoluzioni cliniche e necessità di richiamo a partire da dati anamnestici, diagnosi, interventi, misure longitudinali ed esiti.

**Rischio e verifica:** trattamento di dati sanitari ex art. 9 GDPR; possibile nuova finalità e possibile qualificazione MDSW secondo MDR. Necessaria analisi di base giuridica, intended purpose, profili di trattamento, accesso ai dati e appropriatezza del dataset.

**Misure:** attivazione bloccata di default; validazione scientifica e clinica; stime assenti fino alla validazione; proposta distinta dalla decisione del dentista; audit e tracciabilità.

**Stato:** da dichiarare, non implementato.

## D-106 — Secondary use, training e dati di più account

**Decisione:** usare dati storici aggregati per migliorare modelli solo entro basi giuridiche, accordi e perimetri autorizzati. **Nessun pooling cross-tenant di default**.

**Rischio e verifica:** titolarità distinte, rischio di reidentificazione, trasferimenti di dati, finalità ulteriori e qualità del consenso; richiede valutazione DPO e, ove necessario, DPIA dedicata, ROPA/DPA ed eventuale analisi di compatibilità delle finalità.

**Misure:** segregazione del tenant; dataset governati; minimizzazione; pseudonimizzazione senza presunzione di anonimato; controllo accessi e output aggregati; approval gate per federated learning o centralizzazione.

**Stato:** da dichiarare, non implementato.

## D-107 — Embedding, RAG e accessi semantici

**Decisione:** adottare pgvector in PostgreSQL per recupero semantico, con repository scientifico separato e indici clinici per account e paziente.

**Rischio e verifica:** gli embedding e i chunk clinici possono essere dati personali; possibilità di recuperare documenti di altri pazienti o cliniche per errore di filtro; prompt injection.

**Misure:** controllo ACL prima del retrieval, schema-per-tenant, filtro per clinica/paziente e ruolo, cifratura/retention/rotazione degli embedding, audit, test cross-tenant e test di prompt injection; nessun accesso arbitrario diretto dal LLM al database.

**Stato:** da dichiarare, non implementato.

## D-108 — Interoperabilità FHIR e repository HAPI opzionale

**Decisione:** progettare un adapter FHIR R4 con PoC HAPI FHIR JPA isolato su database separato, inizialmente con dati sintetici.

**Rischio e verifica:** duplicazione e propagazione di dati sanitari, accessi al server FHIR e difficoltà di revoca/aggiornamento; lo starter HAPI non fornisce sicurezza enterprise automaticamente.

**Misure:** PoC non pubblico senza dati reali; sincronizzazione unidirezionale iniziale, criteri di retention, autorizzazioni e audit prima di valutare l'operatività; sistema gestionale rimane fonte di verità.

**Stato:** da dichiarare, non implementato.

## D-109 — Monitoraggio automatico, richiami e possibili conseguenze sui pazienti

**Decisione:** produrre segnalazioni cliniche e bozze di richiami/piani, integrate con le agende, ma soggette a verifica e conferma del medico.

**Rischio e verifica:** allarmi falsi, omissioni, discriminazioni di accesso e interferenza con cure; uso della previsione di mancata presentazione per ridurre priorità assistenziale; trattamento di dati e possibili effetti significativi.

**Misure:** separare priorità clinica da operativa, human approval nel backend, override motivato, metriche cliniche/fairness, audit, kill switch, revisione periodica e procedure di escalation.

**Stato:** da dichiarare, non implementato.

## Registro e governance

Questo documento **non sostituisce** [dichiarazioni-dpia.md](dichiarazioni-dpia.md). La script di integrazione del pacchetto aggiunge al registro ufficiale una sezione riassuntiva D-105..D-109, senza modificare le voci precedenti. Prima di un eventuale rilascio: revisione DPO, Regolamento (UE) 2016/679, MDR 2017/745, AI Act 2024/1689, normative nazionali e contratti vigenti.
