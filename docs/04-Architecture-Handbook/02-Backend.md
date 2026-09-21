# 02 — Backend (Spring Boot)

## 1. Panoramica

API REST Spring Boot 3.5 su Java 25. Architettura **layered** classica con DTO
separati dalle entity. Persistenza prevalentemente via SQL esplicito
(`NamedParameterJdbcTemplate`), non ORM: scelta deliberata per controllo su
query multi-tenant e viste. JPA/Hibernate è presente ma limitato a 6 entity.

## 2. Struttura dei package

```
com.dentalcare
├── config/       configurazioni Spring, EstimateSchemaInitializer (patch schema)
├── controller/   REST controllers (~29) + controller/ai
├── dto/          record di request/response (Java records)
├── entity/       6 entity JPA: Appointment, Clinic, Patient, Provider, TenantUser, User
├── exception/    eccezioni applicative + GlobalExceptionHandler
├── mapper/       conversione entity/row ↔ DTO (dove serve)
├── security/     JWT, TenantContext, SecurityConfig, crypto/
├── service/      logica applicativa (~40 service) + service/ai
├── util/         helper (es. TempPasswordGenerator)
└── validation/   Bean Validation custom (@ValidFiscalCode)
```

## 3. Flusso di una richiesta

```
HTTP → JwtAuthenticationFilter (valida token, popola SecurityContext + TenantContext)
     → Controller (@Valid DTO, delega)
     → Service (@Transactional, logica, TenantContext.validatedSchema())
     → NamedParameterJdbcTemplate (SQL su schema tenant) → PostgreSQL
     ← DTO ← mapping row → JSON
```

## 4. Controller

Sottili: ricevono/restituiscono DTO, validano con `@Valid`, delegano al service,
usano status HTTP coerenti (201 + `Location` in creazione, 204 in delete). Nessuna
logica di business. Esempi: `PatientController`, `AppointmentController`,
`AppointmentSessionController` (scheda di seduta ed esecuzione prestazioni),
`EstimateController`, `InvoiceController` (fatture, acconti, note di credito),
`TreatmentPlanController`, `OdontogramController`, `ProductController` (magazzino),
`RecallController` (richiami), `ErrorExplanationController` (spiegazione AI errori),
`CopilotController`, `ChatController`, `TenantAdminController`,
`ClinicSettingsController` (dati fatturazione + orari studio per-tenant).

`AppointmentController` espone anche `GET /availability`: dato un servizio e una
data, `AppointmentService.findAvailability()` restituisce i primi slot liberi
rispettando gli orari studio del tenant e le sovrapposizioni con appuntamenti
non cancellati (`starts_at < candidateEnd AND ends_at > candidateStart`).

## 5. Service

Contengono la logica e le transazioni. Pattern ricorrenti:
- `private String s()` → `TenantContext.validatedSchema()` (schema tenant validato regex).
- SQL con parametri bindati (`MapSqlParameterSource`), mai concatenazione di input.
- Mapping riga→DTO in metodi `mapXxxRow`.
- Lettura anagrafica pazienti via viste (`v_patient_dashboard`,
  `v_patient_clinical_card`, `v_patient_estimates_summary`).
- `SessionService`: orchestra la transizione della seduta clinica (`loadSession`,
  `recordOutcomes`, `closeSession`, `openItems`, `removeSuspendedItem`) garantendo
  la consistenza relazionale e l'audit dell'autore reale dell'atto clinico.
- `ErrorExplanationService`: interroga il modello OpenAI (`error.humanize`) con
  cache locale in-memory e sanitizzazione preventiva di identificatori o dati sensibili.

## 6. Persistenza

- **SQL-first**: `NamedParameterJdbcTemplate` su schema tenant. Le viste
  incapsulano join e aggregazioni ricorrenti.
- **JPA/Hibernate**: solo per 6 entity core; `ddl-auto=none`, `open-in-view=false`.
- **Migrazioni**: schema creato/aggiornato da `database/install.sql` (installer)
  + funzione `dentalcare.create_tenant()` per nuovi tenant + patch idempotente
  a runtime (vedi [06-Multitenancy](06-Multitenancy.md)).

## 7. DTO e validazione

- Request/response sono `record` Java. Nessuna entity JPA esposta.
- Bean Validation su DTO (`@NotBlank`, `@Email`, `@Size`, `@ValidFiscalCode`
  custom per il codice fiscale italiano — validatore in `validation/`).

## 8. Gestione errori (#51, #54, #58)

`GlobalExceptionHandler` (`@RestControllerAdvice`) centralizza e standardizza tutte
le risposte di errore nel contratto `{ code, message, fieldErrors? }`:
- `ResourceNotFoundException` e rotte inesistenti (`NoResourceFoundException`) → 404 (evita 500 spuri).
- `MethodArgumentNotValidException` → 400 con mappa degli errori di validazione per campo.
- Errori di integrità e conflitti di business → 409 con codici semantici espliciti:
  - Fatturazione: `INVOICE_ALREADY_CANCELLED`, `TREATMENT_PLAN_HAS_ISSUED_INVOICES`, `ESTIMATE_HAS_ISSUED_INVOICES`, `CANNOT_CANCEL_ISSUED_INVOICE`.
  - Seduta clinica: `SESSION_ALREADY_CLOSED`, `SESSION_CANCELLED`, `SESSION_NO_SHOW`, `SESSION_CHANGED`, `SESSION_ITEM_ALREADY_PERFORMED`.
- `EncryptionException` → 500 senza mai esporre plaintext o dettagli crittografici.
- Handler generico (`handleGeneric`): sanitizzato, non restituisce più `ex.getMessage()` grezzo al client in ambienti non-dev.
- **Errori intelligenti via AI (`POST /api/errors/explain`)**: endpoint dedicato che riscrive i messaggi d'errore tecnici in spiegazioni chiare e rimedi azionabili per l'operatore di studio.

## 9. Integrazioni server-side

- **n8n**: endpoint `POST /api/public/service-token` autenticato con header
  `X-N8N-Key`; rilascia un JWT di servizio per i workflow (prenotazioni).
- **Servizio AI Python**: chiamate outbound + callback firmati HMAC
  (`HmacVerifier`) per l'esito delle analisi immagini.
- **SSE**: streaming eventi (suggerimenti copilot, analisi documenti,
  eventi agenda) via `SseEmitterRegistry`.

## 10. Configurazione

Profili Spring:
- `default` (sviluppo locale);
- `coll` (collaudo, porta 8082, DB `dentalcare_coll`, bucket MinIO prefix `coll/`);
- `prod` (produzione, DB `dentalcare_prod`, bucket MinIO prefix `prod/`).

I segreti reali stanno in file esterni gitignored (`backend/config/` in dev,
`config/application-prod.properties` montata in prod), che sovrascrivono i default
del classpath. Vedi [08-DevOps](08-DevOps.md) e [09-Deployment](09-Deployment.md).
