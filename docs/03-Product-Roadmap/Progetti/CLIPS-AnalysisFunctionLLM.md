# CLIPS — AnalysisFunctionLLM, il componente Clinical Knowledge

**Versione:** 1.0 · **Data:** 18 novembre 2026  
**Progetto:** [CLIPS — Clinical Intelligence Predictive System](2026-11-12-fase-4-clinical-intelligence.md)  
**Fase di CLIPS:** Fase 2 — Conoscenza clinica (gate M3-M4)  
**Stato:** in uso per la chat dell'Academy · per CLIPS 📋 pianificato, **non implementato**

> **Nota sui numeri.** «Fase 2 di CLIPS» indica il gruppo di gate M3-M4 del progetto CLIPS. Non è la «Fase 2 del prodotto» (AI Copilot clinico e ortopanoramiche).

## 1. Cos'è

AnalysisFunctionLLM è il servizio che nell'interfaccia si chiama **DentalCare Support**. Gira in un contenitore Docker (`analysisfunctionllm-analysis-function-llm-1`) su un host dedicato della rete interna, separato dall'applicazione DentalCare.

Il servizio risponde a domande in italiano consultando **guide documentali** già trasformate in grafi di conoscenza. Non cerca sul web e non usa i dati dei pazienti. Ogni risposta riporta le citazioni delle fonti usate.

Il componente deriva da NotebookLLM. In più offre la raccolta dei requisiti dalla chat (proposte degli utenti, riviste da un amministratore) e un visualizzatore dei grafi riservato agli amministratori.

## 2. Come funziona

1. **Fonti.** Ogni guida è una cartella con il suo grafo e i documenti originali. Le guide sono montate in sola lettura. Oggi sono cinque, tra cui la guida del prodotto e due guide cliniche (parodontologia ed endodonzia).
2. **Modello canonico (CKM).** Un provider legge il grafo di una fonte e lo traduce in un formato comune, il *Canonical Knowledge Model*. Il testo, il codice originale e la posizione nella guida restano associati. Ogni revisione è verificata con SHA-256 e le revisioni precedenti si conservano. Un provider legge un solo tipo di fonte; oggi esiste quello per i grafi JSON. Il motore di consultazione non conosce il formato originale.
3. **Ricerca.** La domanda viene scomposta in parole chiave. Il servizio cerca nel grafo e allarga il contesto ai nodi vicini, in ampiezza (`bfs`, predefinito) o in profondità (`dfs`, modalità approfondita). Ogni fonte riceve un budget di contesto.
4. **Risposta.** Un modello linguistico scrive la risposta **solo** sul contesto recuperato. Se il grafo non contiene evidenze pertinenti, il servizio lo dice e non inventa.
5. **Memoria.** Le conversazioni restano in un database SQLite nel volume del servizio. La cache è volatile (Redis nel contenitore).

Una relazione riportata da un grafo non è una validazione clinica: il servizio conserva la semantica dichiarata dalla fonte e non la rafforza.

### API principali

Autenticazione con token JWT, ottenuto con un login. Le fonti visibili dipendono dal profilo dell'utente.

| Endpoint | Uso |
|---|---|
| `GET /health` | Verifica di stato |
| `POST /api/auth/login` · `POST /api/auth/logout` · `GET /api/auth/me` | Sessione |
| `GET /api/sources` | Fonti consultabili dall'utente |
| `POST /api/chat/ask` | Domanda: testo, fonti, sessione opzionale, modalità di ricerca. Risposta con testo, motore usato, fonti, citazioni (al massimo 12) e sessione |
| `GET /api/chat/sessions` · `GET/DELETE /api/chat/sessions/{id}` | Cronologia dell'utente |
| `/api/admin/*` | Utenti e assegnazione delle fonti, solo amministratori |

Il servizio rifiuta una fonte non assegnata all'utente (403) e una sessione altrui o inesistente (404).

## 3. Oggi: la chat dell'Academy

DentalCare usa il servizio per **«Chiedi all'Academy»**. Il percorso è:

~~~mermaid
flowchart LR
  UTE[Utente nell'Academy] --> FE[Angular: chat Academy]
  FE --> BE[Spring Boot: AcademyChatService]
  BE --> CL[NotebookLlmClient]
  CL -- utente di servizio, JWT in cache --> AF[AnalysisFunctionLLM]
  AF --> G[(Guida_DentalCare_Pro)]
  G --> AF
  AF -- risposta e citazioni --> CL
  CL --> BE
  BE --> FE
  MCP[Servizio documentazione: tool ask_academy] -. spento di default .-> AF
~~~

- Il backend chiama il servizio tramite `NotebookLlmClient`, con un **utente di servizio** e la sola fonte **`Guida_DentalCare_Pro`**. Il token resta nel backend: il browser non lo vede mai.
- La lezione che l'utente sta leggendo si aggiunge alla domanda come contesto. Non cambia la fonte.
- Il token si tiene in cache per un tempo configurabile; se il servizio lo rifiuta, il client rifà il login una sola volta.
- L'integrazione è **spenta di default** (`app.notebookllm.enabled=false`). Si accende negli ambienti di collaudo e di prova. Se il servizio non risponde, l'utente vede un messaggio di servizio non disponibile e l'Academy resta consultabile.
- Anche il servizio della documentazione può chiamarlo, con il tool MCP `ask_academy`. Anche questo è spento di default.
- Indirizzo, utente e password del servizio sono parametri di configurazione dell'ambiente. Non stanno nel repository.

Oggi il servizio lavora **solo sulla guida del prodotto**. Nessun dato di pazienti, clinica o tenant arriva al servizio.

## 4. Domani: Clinical Knowledge nella Fase 2 di CLIPS

Il progetto CLIPS prevede due domini separati per il RAG: il **corpus scientifico** (senza dati identificativi) e il **corpus documentale clinico autorizzato** (dati del paziente). AnalysisFunctionLLM è il candidato per il **primo dominio**: la consultazione dei **Clinical Pathway**, cioè dei percorsi clinici e delle raccomandazioni delle linee guida, con citazione della fonte.

### Collegamenti con CLIPS

| Elemento di CLIPS | Ruolo del Clinical Knowledge |
|---|---|
| **Corpus scientifico governato** | Ogni guida clinica è una fonte con provenienza, versione, data di validità e stato di revisione. Il servizio consulta solo le revisioni attive del catalogo CKM. Una nuova versione di una guida è una nuova revisione, non una sovrascrittura |
| **Clinical RAG Service** | Il RAG chiede al servizio le evidenze per un tema (patologia, procedura, follow-up) e riceve testo, citazione e localizzatore nel documento originale. La ricerca sul paziente resta nel RAG, con pgvector e permessi per tenant, clinica, ruolo e paziente |
| **Care Pathway del CEM** | Il Care Pathway di un problema (per esempio l'endodonzia del 36 su tre sedute) è la chiave della richiesta: tipo di percorso e fase, **mai** l'identità del paziente. Il servizio restituisce le raccomandazioni attese per quel percorso e i controlli previsti |
| **Orchestratore clinico** | Compone fatti di cartella, segnali deterministici, evidenze del servizio ed eventuali risultati ML. Il servizio fornisce solo il blocco «evidenze citate» |

~~~mermaid
flowchart TB
  subgraph OGGI[Oggi]
    A1[Academy DentalCare] --> N1[NotebookLlmClient]
    N1 --> S1[AnalysisFunctionLLM]
    S1 --> F1[(Guida del prodotto)]
  end
  subgraph DOMANI[Domani: CLIPS Fase 2]
    CEM[Care Pathway del CEM] --> ORC[Orchestratore clinico]
    ORC --> RAG[Clinical RAG Service]
    RAG -- solo tema e tipo di percorso --> S2[AnalysisFunctionLLM: Clinical Knowledge]
    S2 --> SCI[(Corpus scientifico governato: linee guida)]
    S2 -- evidenze con citazioni --> RAG
    RAG <--> VEC[(pgvector: documenti del paziente autorizzato)]
    RAG --> ORC
    ORC --> UMANO[Anteprima e decisione del medico]
  end
~~~

### Lavoro previsto

1. Definire, con odontoiatri, quali guide e quali Clinical Pathway entrano nel corpus governato (parte del gate M3).
2. Fissare un contratto stabile della richiesta («tema + tipo di percorso + fonti autorizzate») e della risposta («evidenze + citazioni + revisione della fonte»), distinto dalla chat libera.
3. Collegare il servizio al Clinical RAG Service dietro un'interfaccia astratta, come previsto per il livello vettoriale, così da poterlo sostituire.
4. Aggiungere test di non-regressione: le risposte restano ancorate alle citazioni e il servizio dichiara quando non trova evidenze.
5. Registrare nel registro DPIA il flusso nuovo, prima di ogni attivazione (vedi [addendum DPIA di CLIPS](../../06-Compliance/Fase-4-Clinical-Intelligence-DPIA-Addendum.md)).

## 5. Vincoli

- **Solo dati autorizzati.** Il servizio consulta fonti documentali approvate. Ogni fonte ha un proprietario, un diritto di uso e una revisione.
- **Nessun dato di pazienti verso il servizio** finché non sono soddisfatti i gate di CLIPS: DPIA aggiornata, valutazione MDR e AI Act, conferma del DPO. Fino ad allora il servizio lavora solo sulla guida del prodotto.
- **Il servizio non decide.** Restituisce evidenze citate. Non calcola rischi, non diagnostica, non propone terapie. Le probabilità vengono solo da modelli predittivi validati. Il medico conferma ogni proposta.
- **Fonte non validata non è evidenza clinica.** Prima dell'uso clinico ogni guida richiede revisione clinica e dichiarazione di stato.
- **Isolamento.** Il servizio non conosce i tenant. L'isolamento per tenant, clinica e ruolo resta nel backend DentalCare, che decide cosa inviare.
- **Interruttore.** L'integrazione si spegne con un parametro di configurazione, senza toccare il resto del prodotto.
- Il servizio non va esposto fuori dalla rete interna senza autenticazione e controlli adeguati.

## 6. Stato

| Elemento | Stato |
|---|---|
| Chat dell'Academy su guida del prodotto | ✅ in uso in collaudo e prova; spenta di default |
| Tool `ask_academy` del servizio documentazione | ✅ disponibile; spento di default |
| Modello canonico e provider Graph JSON | ✅ disponibili |
| Guide cliniche nel catalogo del servizio | 🔶 presenti per prova, non validate clinicamente |
| Contratto «evidenze per Clinical Pathway» | 📋 da definire |
| Collegamento al Clinical RAG Service e al Care Pathway | 📋 pianificato, non implementato |
| Uso clinico | ⛔ non autorizzato |

## 7. Riferimenti

[Progetto CLIPS](2026-11-12-fase-4-clinical-intelligence.md) · [Specifica 17 — CEM, FHIR e Predictive AI](../../04-Architecture-Handbook/17-Clinical-Event-Model-and-Predictive-AI.md) · [04 — AI](../../04-Architecture-Handbook/04-AI.md) · [AI Roadmap](../AI-Roadmap.md) · [Addendum DPIA](../../06-Compliance/Fase-4-Clinical-Intelligence-DPIA-Addendum.md) · [Inventario flussi AI per il DPO](../../06-Compliance/inventario-flussi-ai-per-dpo.md).
