# Architecture Handbook — DentalCare Pro

Documentazione tecnica dello **stato reale** della piattaforma (branch `master`,
aggiornata 2026-07). Descrive ciò che è implementato, segnalando esplicitamente
ciò che è pianificato/non ancora presente.

## Indice

| # | Sezione | Contenuto |
|---|---------|-----------|
| 01 | [Overview](01-Overview.md) | Stack, componenti, flusso, moduli, maturità |
| 02 | [Backend](02-Backend.md) | Spring Boot layered, package, JDBC-first, error handling |
| 03 | [Frontend](03-Frontend.md) | Angular 21 standalone, feature, layout 3 colonne |
| 04 | [AI](04-AI.md) | Copilot (Spring AI/GPT-4.1 + tool), analisi radiologica ONNX, n8n |
| 05 | [DICOM](05-DICOM.md) | Stato: non implementato (roadmap) |
| 06 | [Multi-tenancy](06-Multitenancy.md) | Schema-per-tenant, TenantContext, provisioning, patchSchema |
| 07 | [Security](07-Security.md) | JWT, ruoli, cifratura GDPR campo-per-campo (#7) |
| 08 | [DevOps](08-DevOps.md) | Build, Docker, config/segreti, ambienti |
| 09 | [Deployment](09-Deployment.md) | Compose, install.sh/setup.sh, deploy cifratura |
| 10 | [Testing](10-Testing.md) | Unit-first + validazione DB reale |
| 11 | [Cifratura dati & GDPR](11-Data-Encryption.md) | Scelte di progetto, modello di minaccia, trade-off, roadmap |
| 12 | [Modello cartella clinica](12-Clinical-Record-Model.md) | Entità, encounter, finalizzazione e addendum, audit, mappatura FHIR |
| 13 | [Audit trail clinico](13-Audit-Trail.md) | Modello probatorio, taglio Tier 1 (gate) / Tier 2, decisioni di design |

## Sintesi tecnica

DentalCare Pro è una web app full-stack **multi-tenant a schema separato** per
studi dentistici:

- **Frontend** Angular 21 (standalone, signals, Tailwind) → **API** Spring Boot
  3.5 / Java 25 → **PostgreSQL** (SQL-first, viste per-tenant).
- **AI**: copilot clinico (GPT-4.1 con function calling) + servizio Python
  FastAPI/ONNX per l'analisi radiologica (YOLO), integrati via tool e callback
  HMAC. Automazione conversazionale via **n8n**.
- **Storage**: MinIO (S3) per documenti/immagini.
- **Sicurezza**: JWT + autorizzazione per ruolo lato server; **cifratura
  campo-per-campo** dei dati personali (birth_date, fiscal_code) con chiavi
  derivate per-tenant (HKDF + AES-256-GCM) e **blind index** per la ricerca.
- **Deploy**: Docker Compose su singola macchina; DB su host dedicato; script
  `setup.sh`/`install.sh`.

### Scelte architetturali distintive

1. **Persistenza SQL-first** (JdbcTemplate) invece di ORM pervasivo: controllo
   diretto su query multi-tenant e viste.
2. **Schema-per-tenant** con patch idempotente a runtime (startup + provisioning)
   invece di sole migrazioni versionate.
3. **Cifratura per-tenant con seam Vault**: astrazione `MasterKeyProvider`
   pronta per un secret store esterno.
4. **AI disaccoppiata**: copilot e visione sono servizi separati, non parte del
   core transazionale.

### Non ancora implementato (roadmap)

**Release 1.x** — prerequisiti del go-live clinico (vedi
[Release 1.x](../03-Product-Roadmap/Release-1.x.md)):

- **audit trail clinico** (modello probatorio, Tier 1/Tier 2 e decisioni di
  design in [13-Audit-Trail](13-Audit-Trail.md)), **finalizzazione delle note +
  addendum**, **consensi versionati**, **encounter**: il livello del *valore
  probatorio* della cartella (vedi [12-Clinical-Record-Model](12-Clinical-Record-Model.md));
- MFA, merge dei duplicati, integrità dei documenti (SHA-256, malware scan),
  export paziente art. 15.

**Successive:**

- DICOM nativo / PACS — imaging oggi su formati standard.
- Conservazione a norma, firma qualificata/PAdES, FHIR API, connettore FSE 2.0,
  portale paziente, terminology service.
- `VaultMasterKeyProvider` (secret store esterno).
- Cifratura Slice 2b (phone/email/address) e drop delle colonne plaintext.
- TDE / disk-encryption a valutazione per il dato a riposo su disco/backup
  (vedi [11-Data-Encryption §6](11-Data-Encryption.md)).

### Stato del prodotto

La piattaforma è in **stato dimostrativo**: nessuno studio la usa su pazienti reali.
Il modulo di **analisi radiologica** è disattivato in produzione clinica in attesa del
percorso MDR ([Release 2.x](../03-Product-Roadmap/Release-2.x.md)). Il piano completo è in
[Product Roadmap](../03-Product-Roadmap/Product-Roadmap.md).
