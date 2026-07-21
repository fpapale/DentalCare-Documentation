# Documentazione Ufficiale DentalCare Pro

Benvenuti nella documentazione ufficiale di **DentalCare Pro**, la piattaforma gestionale e clinica *AI-Native* progettata per trasformare gli studi odontoiatrici attraverso l'integrazione di Intelligenza Artificiale, sicurezza informatica avanzata e un'architettura cloud scalabile.

---

## 📚 Indice della Documentazione

### 1. Studio di Fattibilità & Visione (`docs/01-Studio-di-Fattibilita/`)
- [Executive Summary](docs/01-Studio-di-Fattibilita/01-Executive-Summary.md) — Sintesi strategica del progetto.
- [Visione e Missione](docs/01-Studio-di-Fattibilita/02-Vision.md) — La trasformazione digitale dell'odontoiatria.
- [Analisi dei Rischi e Compliance](docs/01-Studio-di-Fattibilita/06-Rischi.md) — Rischi tecnici, clinici e normativi (GDPR, EU AI Act, MDR).

### 2. Business Plan (`docs/02-Business-Plan/`)
- Modello finanziario, piano di sostenibilità e strategia di go-to-market.

### 3. Product Roadmap & Specifiche (`docs/03-Product-Roadmap/`)
- [Product Roadmap](docs/03-Product-Roadmap/Product-Roadmap.md) — Pianificazione e milestone delle release.
- [AI Roadmap](docs/03-Product-Roadmap/AI-Roadmap.md) — Evoluzione dei modelli LLM e Computer Vision.
- [Release 1.x](docs/03-Product-Roadmap/Release-1.x.md) — Gestionale odontoiatrico con AI amministrativa.
- [Release 2.x](docs/03-Product-Roadmap/Release-2.x.md) — AI radiologica certificata e percorso MDR.
- 🆕 [**Specifica DentalCare Credits & Reputation Network**](docs/03-Product-Roadmap/DentalCare-Credits-and-Reputation-Spec.md) — Sistema di gamification, anonimizzazione DICOM, incentivi SaaS e validazione peer-to-peer (Release 3.x/4.x).

### 4. Manuale Architetturale (`docs/04-Architecture-Handbook/`)
- [Overview Architetturale](docs/04-Architecture-Handbook/01-Overview.md) — Microservizi e struttura cloud.
- [Backend Specification](docs/04-Architecture-Handbook/02-Backend.md) — Spring Boot e gestione dati.
- [Frontend Specification](docs/04-Architecture-Handbook/03-Frontend.md) — Interfaccia reattiva.
- [Architettura AI](docs/04-Architecture-Handbook/04-AI.md) — Sottosistemi Copilot e AI Radiologica (Human-in-the-loop).
- [Imaging DICOM / PACS](docs/04-Architecture-Handbook/05-DICOM.md) — Standard e gestione radiografica.
- [Multi-tenancy](docs/04-Architecture-Handbook/06-Multitenancy.md) — Modello dati schema-per-tenant.
- [Sicurezza e Postura Regolatoria](docs/04-Architecture-Handbook/07-Security.md) — Cifratura, GDPR, AI Act e MDR.
- [Cifratura Dati Sanitari](docs/04-Architecture-Handbook/11-Data-Encryption.md) — Cifratura campo-per-campo (Art. 32 GDPR).
- [Modello Cartella Clinica](docs/04-Architecture-Handbook/12-Clinical-Record-Model.md) — Odontogramma e diari clinici.
- [Audit Trail Probatorio](docs/04-Architecture-Handbook/13-Audit-Trail.md) — Immutabilità e valore legale ex art. 2236 c.c.

### 5. Manuale Utente (`docs/05-Manuale-Utente/`)
- [Guida Dottoressa / Medico](docs/05-Manuale-Utente/01-Guida-Dottoressa.md) — Flusso clinico, agenda e Copilot.
- [Guida Segretaria](docs/05-Manuale-Utente/02-Guida-Segretaria.md) — Gestione appuntamenti e fatturazione.
- [Guida Amministratore](docs/05-Manuale-Utente/03-Guida-Amministratore.md) — Configurazione studio e impostazioni AI.

### 6. Presentazioni & Materiali Clinici (`docs/`)
- 🆕 [**Presentazione Clinico-Tecnico-Legale per il Medico**](docs/Presentazione-Medico-DentalCare-Pro.md) — Panoramica integrata delle funzionalità attuali e future per odontoiatri e direttori sanitari.

---

## 🎯 Pilastri del Progetto

- **Eccellenza Clinica**: Riduzione del carico burocratico alla poltrona, cartella clinica digitale e supporto decisionale di seconda opinione.
- **Solidità Tecnica**: Architettura Cloud-Native multi-tenant, microservizi reattivi, cifratura AES-256 e tracciabilità audit log.
- **Compliance Normativa**: Conforme a **GDPR Art. 32**, **EU AI Act** (supervisione umana *human-in-the-loop*) e predisposto per la qualificazione **MDR (UE 2017/745)**.