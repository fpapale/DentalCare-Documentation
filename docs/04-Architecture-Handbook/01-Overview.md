# 01 — Overview Architetturale

> Documentazione tecnica dello **stato reale** della piattaforma DentalCare Pro.
> Aggiornata al: 2026-07 (branch `master`).

## 1. Cos'è

Web application full-stack per la gestione di studi dentistici, multi-tenant,
con copilot AI clinico e servizio di analisi radiologica. Architettura a tre
livelli con separazione netta UI / API / persistenza.

## 2. Stack tecnologico (reale)

| Livello | Tecnologia |
|---------|-----------|
| Frontend | Angular 21 (standalone components, signals), Tailwind CSS |
| Backend API | Spring Boot 3.5, Java 25 |
| Persistenza | PostgreSQL 15, accesso via `JdbcTemplate`/`NamedParameterJdbcTemplate` (JPA/Hibernate solo per 6 entity) |
| AI Copilot | Spring AI + OpenAI GPT-4.1 (function calling) |
| AI Radiologia | Servizio Python FastAPI + ONNX Runtime (modelli YOLO) |
| Object storage | MinIO (S3-compatible) per documenti paziente |
| Automazione | n8n (prenotazioni via WhatsApp/voce, webhook) |
| Deploy | Docker Compose (macchina 192.168.0.72), DB `dentalcare_prod` su 192.168.0.173 |

## 3. Componenti e flusso

```
Angular (browser)
  │  HTTPS/JSON  (JWT Bearer)
  ▼
nginx (frontend container) ── proxy /api ──►  Spring Boot API (:8080)
                                                │
                     ┌──────────────────────────┼───────────────────────────┐
                     ▼                           ▼                           ▼
              PostgreSQL                     MinIO (S3)              Servizio AI Python
           (schema-per-tenant)          (documenti/immagini)        (FastAPI + ONNX/YOLO)
                     ▲                                                       │
                     └──────────────── callback HMAC (analisi radiologica) ─┘

  n8n ──(service-token)──► API   |   Copilot AI ──(Spring AI/GPT-4.1 + tools)──► API
```

## 4. Moduli funzionali

**Clinici**: pazienti, anamnesi, cartella clinica, odontogramma, diagnosi,
prescrizioni, piani di cura (treatment plan), appuntamenti/agenda.

**Amministrativi**: preventivi, fatturazione, prestazioni (service catalog),
magazzino (prodotti/movimenti/fornitori), richiami (recall), impostazioni studio.

**Piattaforma**: multi-tenant admin, provisioning studi, gestione utenti/ruoli,
copilot AI, chat, analisi documenti/immagini AI, dashboard e KPI.

## 5. Principi architetturali applicati

- **Layered**: Controller → Service → Repository/JDBC → DB. Nessuna logica di
  business nei controller; nessuna entity persistente esposta nelle API (solo DTO).
- **Multi-tenant a schema separato**: ogni studio ha uno schema PostgreSQL
  `t_<8hex>`; il tenant è derivato dal contesto autenticato, mai dal client.
- **Sicurezza trasversale**: autorizzazione lato server per ruolo; cifratura
  campo-per-campo dei dati personali sensibili (GDPR art. 32).
- **AI-native ma isolata**: copilot e inferenza radiologica sono servizi
  distinti, integrati via tool/callback, non accoppiati al core.

## 6. Stato di maturità (sintesi)

| Area | Stato |
|------|-------|
| Core clinico + amministrativo | Implementato, in uso |
| Multi-tenant + provisioning | Implementato |
| Copilot AI + chat | Implementato |
| Analisi immagini radiologiche (ONNX/YOLO) | Implementato (immagini standard) |
| Cifratura GDPR (birth_date, fiscal_code) | Implementato (#7, Slice 1 + 2a) |
| DICOM nativo | **Non implementato** (roadmap) — vedi [05-DICOM](05-DICOM.md) |
| Secret store esterno (Vault) | Predisposto (seam), non ancora attivo |

Dettaglio nelle sezioni successive (02–10).
