# 10 — Testing

## 1. Backend

- **Framework**: `spring-boot-starter-test` (JUnit 5 + Mockito + AssertJ).
- **Stile**: prevalentemente **unit test mockati** (nessun Testcontainers): i
  service sono testati con `NamedParameterJdbcTemplate`/dipendenze mockate,
  asserendo SQL, parametri e comportamento. ~14 classi di test.
- **Copertura mirata** sulle aree a rischio:
  - crypto: `TenantEncryptionServiceTest` (round-trip encrypt/decrypt,
    blind index deterministico e case-insensitive, chiavi schema-bound, HKDF),
    `ConfigMasterKeyProviderTest` (fail-fast);
  - migrazione cifratura: `EncryptionMigrationServiceTest` (idempotenza, path
    positivi/negativi);
  - provisioning: `TenantProvisioningServiceTest` (patchSchema al provisioning,
    best-effort);
  - dominio: `PatientServiceTest`, `ProductCategoryServiceTest`,
    `FiscalCodeValidatorTest`, ecc.
- **Gate**: `./mvnw test` deve essere verde prima di merge; la build è il gate
  principale.

## 2. Validazione su DB reale

Le aree con SQL/viste/schema (multi-tenant, cifratura) sono validate **anche
manualmente su DB dev** dopo l'implementazione, perché i test unit sono mockati e
non esercitano lo schema reale. Procedura tipica:
1. riavvio backend → `patchSchema` applica colonne/viste;
2. `POST /api/admin/encryption/migrate` → verifica conteggi e idempotenza;
3. lettura via API (dettaglio/lista/ricerca) → confronto con il valore atteso;
4. verifica su schema fresco (`install.sql` + `create_tenant()`).

Questo approccio ha intercettato bug non coglibili dai test mockati (es. ordering
colonne/viste in `patchSchema`).

## 3. Frontend

Test Angular (componenti/service/guard/pipe) da configurare/estendere secondo la
configurazione reale del progetto. Priorità su validazione form e guard.

## 4. Direzione

- Introduzione di **Testcontainers** per integration test su schema reale
  (chiuderebbe il gap oggi coperto dalla validazione manuale).
- Test di contratto tra service Angular e DTO backend.
