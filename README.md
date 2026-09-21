# Documentazione Ufficiale DentalCare Pro

Benvenuti nella documentazione ufficiale di **DentalCare Pro**, la piattaforma gestionale e clinica *AI-Native* progettata per trasformare gli studi odontoiatrici attraverso l'integrazione di Intelligenza Artificiale, sicurezza informatica avanzata e un'architettura cloud scalabile.

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

### 5. Manuale Utente (`docs/05-Manuale-Utente/`)
- 📖 [**Manuale Utente Integrale**](docs/05-Manuale-Utente/MANUALE_UTENTE.md) — Manuale completo di riferimento (1120 righe) con tutti i moduli, schermate, ciclo seduta, fatturazione conforme e glossario stati.
- [Guida Dottoressa / Medico](docs/05-Manuale-Utente/01-Guida-Dottoressa.md) — Flusso clinico, agenda, scheda di seduta (#56-#62) e Copilot.
- [Guida Segretaria](docs/05-Manuale-Utente/02-Guida-Segretaria.md) — Gestione appuntamenti, fatturazione a saldo/acconto/nota credito (#50-#52) e richiami.
- [Guida Amministratore](docs/05-Manuale-Utente/03-Guida-Amministratore.md) — Configurazione studio, impostazioni AI e gestione errori intelligenti (#54).
- [Manuale Presentazione con Schermate](docs/05-Manuale-Utente/Manuale-Completo.md) — Percorsi guidati con screenshot reali per i tre ruoli.

### 6. Compliance, Privacy & EU AI Act (`docs/06-Compliance/`)
- 📄 [**Conformità EU AI Act**](docs/06-Compliance/AI-Act-Compliance.md) — Classificazione sistemi, scadenze, disclosure Art. 50 e Inspection Readiness Binder.
- 📄 [**Inventario Flussi AI per il DPO**](docs/06-Compliance/inventario-flussi-ai-per-dpo.md) — Censimento tecnico per ROPA (Art. 30), DPIA (Art. 35) e accordi DPA con mappatura dati Art. 9 GDPR.
- 📁 [**Cartella 13 Inspection Binder (Retell)**](docs/06-Compliance/retell/) — Evidenze verificabili: snapshot immutabile del system prompt, screenshot configurazione, trascrizione messaggi di disclosure.

### 7. Presentazioni & Materiali Clinici (`docs/`)
- [Presentazione Clinico-Tecnico-Legale per il Medico](docs/Presentazione-Medico-DentalCare-Pro.md) — Panoramica integrata delle funzionalità attuali e future per odontoiatri e direttori sanitari.

---

## 🎯 Pilastri del Progetto

- **Eccellenza Clinica**: Riduzione del carico burocratico alla poltrona, cartella clinica digitale e supporto decisionale di seconda opinione.
- **Solidità Tecnica**: Architettura Cloud-Native multi-tenant, microservizi reattivi, cifratura AES-256 e tracciabilità audit log.
- **Compliance Normativa**: Conforme a **GDPR Art. 32**, **EU AI Act** (supervisione umana *human-in-the-loop*) e predisposto per la qualificazione **MDR (UE 2017/745)**.