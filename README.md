# Documentazione Ufficiale DentalCare Pro

Benvenuti nella documentazione ufficiale di **DentalCare Pro**, la piattaforma gestionale e clinica *AI-Native* progettata per trasformare gli studi odontoiatrici attraverso l'integrazione di Intelligenza Artificiale, sicurezza informatica avanzata e un'architettura cloud scalabile.

---

## 🧭 Come è organizzato e come si aggiorna questo wiki

DentalCare Pro ha **due wiki ufficiali** (decisione del committente, 28/10/2026):

| Wiki | Dove | Cosa contiene |
|---|---|---|
| **Documentazione** | questo repo (`fpapale/DentalCare-Documentation`, locale `D:\DentalCare-Pro-Documentation`) | tutto ciò che si legge: fattibilità, business plan, roadmap e analisi funzionale, architettura, manuale utente, compliance |
| **Codice** | `graphify-out/` del repo applicativo (`fpapale/dentalcare`, privato) | grafo della conoscenza del codice e delle directive di lavoro (`GRAPH_REPORT.md`, `graph.json`), per domande su «come funziona» e «chi chiama cosa» |

Questo repo ha anche un proprio `graphify-out/`: il grafo dei documenti di questo wiki, da rigenerare dopo ogni aggiornamento importante.

### Da dove viene ogni sezione

| Sezione | Fonte | Come si aggiorna |
|---|---|---|
| `05-Manuale-Utente` | **lezioni dell'Academy** nel programma (`backend/src/main/resources/academy/v1` del repo applicativo) | **generata**: `python tools/genera_manuale.py <repo dentalcare>`. Non modificare i `.md` a mano: si corregge la lezione e si rigenera |
| `03-Product-Roadmap` (Release, roadmap, analisi funzionale) | scritta qui | a ogni gruppo di proposte fatte (`directives/proposte-modifiche.md` nel repo applicativo), citando i numeri `#NN` |
| `04-Architecture-Handbook` | scritta qui, verificata sul codice | quando cambiano componenti, API, sicurezza o modello dati |
| `06-Compliance` (registro DPIA, inventario flussi AI, AI Act, fascicolo Retell) | **fonte ufficiale qui** (dal 28/10/2026; prima nel repo applicativo) | ogni decisione con effetto sulla privacy aggiunge una voce D-xx al registro, nella stessa sessione |
| `01`, `02` (fattibilità, business plan, listino) | scritta qui | solo su decisione del committente |

### Regole

- **Pubblico:** questo repo è pubblico. Niente indirizzi interni, credenziali, dati reali; il manuale usa solo dati fittizi.
- **Termini** (concordati il 28/10/2026): **account** (tenant) → **clinica** (= sede) → **poltrona**. Nell'interfaccia e nel manuale mai «Centro» né «Studio» da solo.
- **Stato dichiarato:** ✅ fatto (dev/collaudo/produzione), 📋 confermato, 🔨 in lavorazione, ⏸️ rimandato. Le funzioni non fatte non si descrivono come presenti.

---

## 📚 Indice della Documentazione

### 1. Studio di Fattibilità & Visione (`docs/01-Studio-di-Fattibilita/`)
- [Executive Summary](docs/01-Studio-di-Fattibilita/01-Executive-Summary.md) — Sintesi strategica del progetto.
- [Visione e Missione](docs/01-Studio-di-Fattibilita/02-Vision.md) — La trasformazione digitale dell'odontoiatria.
- [Analisi dei Rischi e Compliance](docs/01-Studio-di-Fattibilita/06-Rischi.md) — Rischi tecnici, clinici e normativi (GDPR, EU AI Act, MDR).
- [Strategia Open Data & Reputation](docs/01-Studio-di-Fattibilita/07-Open-Data-and-Reputation-Strategy.md) — Analisi degli stakeholder (Università, Società Scientifiche, AI Community) e impatto reputazionale dell'iniziativa Open Science.

### 2. Business Plan (`docs/02-Business-Plan/`)
- Modello finanziario, piano di sostenibilità e strategia di go-to-market.

### 3. Product Roadmap & Specifiche (`docs/03-Product-Roadmap/`)
- [Product Roadmap](docs/03-Product-Roadmap/Product-Roadmap.md) — Pianificazione e milestone delle release.
- [AI Roadmap](docs/03-Product-Roadmap/AI-Roadmap.md) — Evoluzione dei modelli LLM e Computer Vision.
- [Release 1.x](docs/03-Product-Roadmap/Release-1.x.md) — Gestionale odontoiatrico con AI amministrativa.
- [Release 2.x](docs/03-Product-Roadmap/Release-2.x.md) — AI radiologica certificata e percorso MDR.
- [Specifica DentalCare Credits & Reputation Network](docs/03-Product-Roadmap/DentalCare-Credits-and-Reputation-Spec.md) — Sistema di gamification, anonimizzazione DICOM, incentivi SaaS e validazione peer-to-peer (Release 3.x/4.x).
- 🆕 [**Specifica Assistente Vocale Chairside Agent**](docs/03-Product-Roadmap/Chairside-Voice-Agent-Spec.md) — Architettura della pipeline vocale offline, acquisizione audio PCM, integrazione Vosk STT, Voices TTS, interprete DSL dei comandi clinici e conformità GDPR/AI Act.

### 4. Manuale Architetturale (`docs/04-Architecture-Handbook/`)
- [Overview Architetturale](docs/04-Architecture-Handbook/01-Overview.md) — Microservizi e struttura cloud.
- [Backend Specification](docs/04-Architecture-Handbook/02-Backend.md) — Spring Boot, gestione dati, standardizzazione errori e profili ambiente (`dev`, `coll`, `prod`).
- [Frontend Specification](docs/04-Architecture-Handbook/03-Frontend.md) — Interfaccia reattiva Angular 17.
- [Architettura AI](docs/04-Architecture-Handbook/04-AI.md) — Sottosistemi Copilot, Errori intelligenti (#54), AI Radiologica (Human-in-the-loop) e governance DPO (#55).
- [Imaging DICOM / PACS](docs/04-Architecture-Handbook/05-DICOM.md) — Standard e gestione radiografica.
- [Multi-tenancy](docs/04-Architecture-Handbook/06-Multitenancy.md) — Modello dati schema-per-tenant, billing mode e guardie pre-cancellazione (#47).
- [Sicurezza e Postura Regolatoria](docs/04-Architecture-Handbook/07-Security.md) — Cifratura, ruoli clinici server-side (`CLINICAL_WRITE_ROLES` #62), AI Act e MDR.
- [DevOps e Container](docs/04-Architecture-Handbook/08-DevOps.md) — Docker multi-stage, stack COLLAUDO (#41) e partizionamento MinIO (#40).
- [Deployment e Topologia](docs/04-Architecture-Handbook/09-Deployment.md) — Procedure di rilascio prod/collaudo e migrazione dati cifrati.
- [Cifratura Dati Sanitari](docs/04-Architecture-Handbook/11-Data-Encryption.md) — Cifratura campo-per-campo con chiavi per-tenant (Art. 32 GDPR).
- [Modello Cartella Clinica](docs/04-Architecture-Handbook/12-Clinical-Record-Model.md) — Ciclo della seduta (`Encounter` #56-#62), odontogramma e diari clinici.
- [Audit Trail Probatorio](docs/04-Architecture-Handbook/13-Audit-Trail.md) — Immutabilità e valore legale ex art. 2236 c.c.
- [LLM NER Gateway & Demo](docs/04-Architecture-Handbook/14-LLM-NER-Gateway.md) — Trust boundary privacy-preserving, Dual-Engine NER (0.3B / spaCy), modalità pass-through e test bench demo.
- [Manuale per ChatGPT e Claude](docs/04-Architecture-Handbook/15-Docs-Service.md) — `dentalcare-docs-service`: le lezioni dell'Academy interrogabili da Claude e ChatGPT con un connettore MCP; come si pubblica, piani necessari, come si collega.

### 5. Manuale Utente (`docs/05-Manuale-Utente/`) — generato dall'Academy
- 📖 [**Manuale integrale**](docs/05-Manuale-Utente/MANUALE_UTENTE.md) — tutti i moduli e le lezioni dell'Academy, con le schermate.
- [Guida per il medico e l'igienista](docs/05-Manuale-Utente/01-Guida-Dottoressa.md) · [Guida per la segreteria](docs/05-Manuale-Utente/02-Guida-Segretaria.md) · [Guida per il titolare e l'amministratore](docs/05-Manuale-Utente/03-Guida-Amministratore.md) — percorsi per ruolo con le lezioni che richiamano.
- [Sintesi con le schermate](docs/05-Manuale-Utente/Manuale-Completo.md) · [Versione Word](docs/05-Manuale-Utente/Manuale_Utente_DentalCare_Pro.docx) · [Indice, matrice per ruolo e glossario](docs/05-Manuale-Utente/README.md).

### 6. Compliance, Privacy & EU AI Act (`docs/06-Compliance/`) — fonte ufficiale
- 📄 [**Registro delle dichiarazioni DPIA**](docs/06-Compliance/dichiarazioni-dpia.md) — scelte di progetto e rischi residui (D-xx) da portare nella DPIA.
- 📄 [**Inventario dei flussi AI per il DPO**](docs/06-Compliance/inventario-flussi-ai-per-dpo.md) — censimento tecnico per ROPA (art. 30), DPIA (art. 35) e DPA, con i dati art. 9.
- 📄 [**Conformità EU AI Act**](docs/06-Compliance/AI-Act-Compliance.md) — classificazione dei sistemi, scadenze, disclosure art. 50.
- 📁 [**Fascicolo di Giulia (Retell)**](docs/06-Compliance/retell/) — REL 1.0 del 28/07/2026, **superata dalla #100** (Giulia centralizzata); il nuovo fascicolo si redige al go-live.

### 7. Presentazioni & Materiali Clinici (`docs/`)
- [Presentazione Clinico-Tecnico-Legale per il Medico](docs/Presentazione-Medico-DentalCare-Pro.md) — Panoramica integrata delle funzionalità attuali e future per odontoiatri e direttori sanitari.

---

## 🎯 Pilastri del Progetto

- **Eccellenza Clinica**: Riduzione del carico burocratico alla poltrona, cartella clinica digitale e supporto decisionale di seconda opinione.
- **Solidità Tecnica**: Architettura Cloud-Native multi-tenant, microservizi reattivi, cifratura AES-256 e tracciabilità audit log.
- **Compliance Normativa**: Conforme a **GDPR Art. 32**, **EU AI Act** (supervisione umana *human-in-the-loop*) e predisposto per la qualificazione **MDR (UE 2017/745)**.