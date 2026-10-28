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
├── service/      logica applicativa (~40 service) + service/ai, service/demo e
│                 service/academy (ambiente di prova, #69)
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
`ClinicSettingsController` (dati della clinica corrente, orari, documenti, modalità di fatturazione, codice e
limite di Giulia, WhatsApp; da #117 niente elenco né creazione di cliniche, che stanno solo in
`TenantAdminController`), `ClinicChairController` (poltrone della clinica corrente, #115),
`ProviderPresenceController` (orari e assenze dei professionisti, #99), `ProviderPreferencesController` e
`ProviderPriceOverrideController` (impostazioni e tariffe personali, #96, #98), `AppointmentNoticeController`
(avvisi al paziente, #111), `VoiceIdentifyController` (riconoscimento della clinica per Giulia, #100),
`EpisodeController` (storico episodi, #67), `DemoController` (stato e ripristino del
workspace demo, #69), `SandboxController` (ambiente di prova dello studio, #70), `AcademyController` e `AcademyAdminController` (lezioni, progressi e
redazione dell'Academy, #69).

`AppointmentController` espone anche `GET /availability`: data la durata (e facoltativi professionista, paziente,
giorno di partenza), `AppointmentService.findAvailability()` restituisce gli slot liberi a passi di slot (#90), dentro
le presenze del professionista (#99), con la prima poltrona attiva libera dell'anagrafica (#115) e senza
sovrapposizioni con appuntamenti non cancellati (`starts_at < candidateEnd AND ends_at > candidateStart`). Le stesse
regole valgono in creazione e spostamento, anche per Copilot e Giulia. `GET /{id}/whatsapp-link` prepara il link
`wa.me` del promemoria o dell'annullamento; `POST /{id}/notify` manda l'e-mail (usato da Giulia).

## 5. Service

Contengono la logica e le transazioni. Pattern ricorrenti:
- `private String s()` → `TenantContext.validatedSchema()` (schema tenant validato regex).
- SQL con parametri bindati (`MapSqlParameterSource`), mai concatenazione di input.
- Mapping riga→DTO in metodi `mapXxxRow`.
- Lettura anagrafica pazienti via viste (`v_patient_dashboard`,
  `v_patient_clinical_card`, `v_patient_estimates_summary`).
- `SessionService`: orchestra la transizione della seduta clinica (`loadSession`,
  `recordOutcomes`, `closeSession`, `openItems`, `removeSuspendedItem`) garantendo
  la consistenza relazionale e l'audit dell'autore reale dell'atto clinico. Da #65 propone
  nella scheda lo stato che la prestazione lascia sul dente e, se il medico lo conferma, lo
  scrive in odontogramma con autore e seduta; da #67 apre l'episodio **prima** di scrivere
  gli esiti quando la visita non è mai passata da «in corso».
- `PlanItemApplicabilityService` (#66): un solo controllo, usato da tutte le vie che mettono
  una prestazione in un piano di cura (FDI, prestazione attiva, posizione, stato del dente,
  superfici). Tutti i problemi in un unico `422 SERVICE_NOT_APPLICABLE`.
- `EpisodeService`, `EpisodeSnapshotService`, `EpisodeDiffService` (#67): ciclo di vita degli
  episodi agganciato ai cambi di stato dell'appuntamento, fotografie canoniche con hash,
  differenze e riepilogo con una funzione pura.
- `DemoWorkspaceService` e `DemoSeedService` (#69): registrazione del workspace demo,
  caricamento dei dati di esempio (date spostate, campi cifrati ricalcolati con la chiave del
  tenant), ripristino e pulizia notturna (`DemoWorkspacePurgeScheduler`).
- `SandboxService` (#70): ambiente di prova dello studio, creato alla prima apertura, con
  scambio di token (identità d'origine, scadenza non oltre il token reale).
- `AcademyService`, `AcademyEditorService`, `AcademyContentInitializer` (#69): catalogo e
  avanzamento (sull'identità reale anche nell'ambiente di prova), redazione, caricamento del
  catalogo iniziale senza sovrascrivere.
- `InvoiceService`: gestisce l'intero ciclo documentale e calcola i numeri fattura mediante `nextProgressive(clinicId, year, prefix)` (#63) leggendo il valore massimo assegnato: in caso di eliminazione di una bozza, i numeri rimangono buchi storici senza causare collisioni sul vincolo `ux_invoices_number`.
- `ErrorExplanationService`: interroga il modello OpenAI (`error.humanize`) con
  cache locale in-memory e sanitizzazione preventiva di identificatori o dati sensibili.
- `ClinicChairService` (#115): anagrafica `clinic_chairs` della clinica corrente; `activeLabels()` è la sola fonte
  delle poltrone prenotabili (agenda, disponibilità, Copilot, Giulia); la rinomina aggiorna `appointments.chair_label`;
  una clinica senza poltrone parte da «Poltrona 1».
- `ProviderPresenceService` (#99): fasce orarie e assenze; `AppointmentService` rifiuta fuori presenza
  (`PROVIDER_NOT_PRESENT`) proponendo i primi orari liberi.
- `AppointmentNoShowScheduler` (#108): ogni notte (`app.appointments.no-show.cron`, 01:30) `markNoShows()` porta a
  `no_show` gli appuntamenti dei giorni precedenti senza esiti né visita avviata, con `status_auto_at` («automatico»);
  ogni scelta manuale lo azzera. `SessionService` porta a «In corso» quando si registrano esiti.
- `AppointmentNoticeService` (#111): `AppointmentService.create / reschedule / updateStatus('cancelled') / cancel`
  registrano un avviso in `appointment_notices` con l'origine (`gestionale`, `copilot` via `asCopilot()`, `giulia` dal
  token dell'agente vocale); conta solo l'ultimo avviso aperto per appuntamento. `AppointmentNotificationService`
  compone e-mail (`EmailService`) e testi WhatsApp; `WhatsAppLinks` costruisce i link `wa.me`; `WhatsAppSettingsService`
  legge attivo/modalità/numero della clinica e blocca i link con WhatsApp spento.
- `RecallMessagingService` (#111): invio del richiamo per e-mail e link WhatsApp, con registrazione del contatto.
- `PatientMailRouting` (#103): destinatario delle e-mail ai pazienti (con dati fittizi va a chi prova il programma).
- `InvoicePdfService` e `InvoiceDeliveryService` (#101): PDF del documento generato sul server e invio al paziente.
- `voice/*` (#100, #109): `VoiceClinicIdentificationService` (codice, numero chiamante, nome e città),
  `ClinicTicketService` (biglietto firmato), `VoiceAgentTokenService` (token `voice_agent` limitato da
  `VoiceAgentScope`), `VoiceAttemptLimiter`, `PatientPhoneIndexService` (indice HMAC dei numeri),
  `VoiceTrialQuotaService` (limite di Giulia negli studi di prova).

## 6. Persistenza e migrazioni a caldo

- **SQL-first**: `NamedParameterJdbcTemplate` su schema tenant. Le viste
  incapsulano join e aggregazioni ricorrenti.
- **JPA/Hibernate**: solo per 6 entity core; `ddl-auto=none`, `open-in-view=false`.
- **Migrazioni**: schema creato/aggiornato da `database/install.sql` (installer)
  + funzione `dentalcare.create_tenant()` per nuovi tenant + patch idempotente
  a runtime gestita da `EstimateSchemaInitializer` (vedi [06-Multitenancy](06-Multitenancy.md)).
  Le tabelle globali dello schema `dentalcare` aggiunte da #69 (registro tenant, Academy,
  ruoli di piattaforma) le crea `PlatformSchemaInitializer`, che gira per primo.
- **DDL transazionale e zero-downtime (#64)**: per prevenire risposte HTTP 500 durante il riavvio del backend, `EstimateSchemaInitializer` esegue l'aggiornamento delle viste (`v_agenda_daily`, `v_patient_dashboard`, etc.) in modalità DDL transazionale atomica (`replaceView()` in singola transazione PostgreSQL), garantendo che i client in volo non vedano mai oggetti mancanti.

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
  - Episodi (#67): `EPISODE_ALREADY_OPEN`, `EPISODE_VISIT_ALREADY_OPEN` (con data e ora dell'altra visita), `EPISODE_VISIT_CLOSES_WITH_SESSION`, `EPISODE_ALREADY_CLOSED`, `EPISODE_AUTHOR_UNKNOWN`.
- Richiesta ben formata ma non ammessa → 422: `SERVICE_NOT_APPLICABLE` (#66, prestazione non applicabile al dente, con dente e motivo), come `SchedulingConstraintException`.
  - Agenda: `OFF_GRID` (#90), `PROVIDER_NOT_PRESENT` (#99), `PROVIDER_NOT_CLINICAL` (#95), `CHAIR_UNKNOWN` (#115),
    `VOICE_TRIAL_LIMIT` (#109), `NOTICE_STATUS_MISMATCH` (#100/#111), oltre a `CHAIR_CONFLICT`, `PROVIDER_CONFLICT`,
    `PROVIDER_LOCKED` (409).
  - Fatturazione: `DEPOSIT_EXCEEDS_ESTIMATE`, `DEPOSIT_DRAFT_PENDING` (#102), `INVOICE_NOT_SENDABLE` (#101).
- Permessi personali → 403: `PRESENCE_NOT_OWNER` (#99), `PREFERENCES_NOT_OWNER` (#98), `PRICES_NOT_OWNER`;
  `TRIAL_NO_ACCOUNTS` negli studi di prova (#87); `INVALID_SERVICE_KEY` per n8n.
- Operazione non consentita → 403 con codice: `DEMO_EXPIRED` (prova terminata, anche su token già emessi), `DEMO_ONLY`, `DEMO_OWNER_ONLY`, `DEMO_RESET_LIMIT` (#69); `SANDBOX_FROM_STUDIO_ONLY`, `SANDBOX_CUSTOMERS_ONLY`, `SANDBOX_USER_INACTIVE` (#70).
- Troppe richieste → 429: `RATE_LIMITED` (limiti per IP, con `Retry-After`), `DEMO_REGISTRATIONS_PAUSED` (tetto giornaliero delle registrazioni di prova).
- `EncryptionException` → 500 senza mai esporre plaintext o dettagli crittografici.
- Handler generico (`handleGeneric`): sanitizzato, non restituisce più `ex.getMessage()` grezzo al client in ambienti non-dev.
- **Errori intelligenti via AI (`POST /api/errors/explain`)**: endpoint dedicato che riscrive i messaggi d'errore tecnici in spiegazioni chiare e rimedi azionabili per l'operatore di studio.

## 9. Integrazioni server-side

- **n8n / Giulia** (#100): `POST /api/public/voice/identify` (header `X-N8N-Key`) riconosce la clinica e rilascia un
  biglietto firmato; `POST /api/public/service-token` con l'id dell'agente centrale e il biglietto rilascia un JWT
  `voice_agent` (ruolo segreteria) valido solo per quella clinica e limitato agli endpoint di `VoiceAgentScope`.
- **Posta**: `EmailService` (SMTP di DentalCare, oppure FakeSMTP su file in sviluppo) per fatture, richiami, avvisi
  e conferme di Giulia; le risposte vanno all'e-mail della clinica.
- **WhatsApp** (#111, modalità manuale): solo link `wa.me` aperti dal browser della clinica; nessuna chiamata a Meta.
- **Servizio AI Python**: chiamate outbound + callback firmati HMAC
  (`HmacVerifier`) per l'esito delle analisi immagini.
- **SSE**: streaming eventi (suggerimenti copilot, analisi documenti,
  eventi agenda) via `SseEmitterRegistry`.

## 10. Configurazione

Profili Spring:
- `default` (sviluppo locale);
- `coll` (collaudo, porta 8082, DB `dentalcare_coll`, bucket MinIO prefix `coll/`);
- `prod` (produzione, DB `dentalcare_prod`, bucket MinIO prefix `prod/`).

Porte d'ingresso (#69, #70), indipendenti: `app.registration.customer-enabled` (nuovo studio,
acceso), `app.demo-workspace.public-registration` (prova gratuita, spenta),
`app.demo-workspace.public-url` (istanza di prova dove mandare chi la chiede),
`app.sandbox.enabled` (ambiente di prova degli studi, spento), `app.academy.enabled`,
`app.academy.editor-emails`, `app.demo-workspace.*` (durata, pulizia, tetti giornalieri,
destinatario delle richieste di attivazione), `app.rate-limit.*`.

I segreti reali stanno in file esterni gitignored (`backend/config/` in dev,
`config/application-prod.properties` montata in prod), che sovrascrivono i default
del classpath. Vedi [08-DevOps](08-DevOps.md) e [09-Deployment](09-Deployment.md).
