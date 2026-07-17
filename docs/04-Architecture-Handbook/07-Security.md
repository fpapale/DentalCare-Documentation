# 07 — Sicurezza

## 1. Autenticazione (JWT)

- Login **a due step**: `POST /api/public/login` (preflight) → se l'utente ha
  una sola clinica ritorna `direct` con token; se ne ha più di una ritorna
  `choose` con le opzioni, e si conferma con `POST /api/public/login/confirm`.
- Il **JWT** (JJWT, HS512) porta nei claim: `sub` (providerId), `clinicId`,
  `schemaName`, `role`, `tenantName`. È la fonte del tenant (vedi
  [06-Multitenancy](06-Multitenancy.md)).
- `JwtService` firma/valida; `JwtAuthenticationFilter` popola il contesto.
- Password con hashing sicuro; cambio obbligatorio al primo accesso
  (`password_temporary`).

## 2. Autorizzazione (ruoli)

Ruoli (enum `dentalcare.provider_role`): `tenant_admin`, `admin`, `dentist`,
`hygienist`, `orthodontist`, `surgeon`, `assistant`, `secretary`, `other`.

`SecurityConfig` (matchers principali):

| Path | Regola |
|------|--------|
| `/api/public/**` | permitAll |
| `/api/internal/**` | permitAll (rete interna) |
| `/api/tenant-admin/**` | `hasRole('TENANT_ADMIN')` |
| `/api/admin/**` | `hasAnyRole('ADMIN','TENANT_ADMIN')` |
| ogni altra | authenticated |

I controlli di autorizzazione sono **sempre** lato server, mai delegati al
frontend. `401` = non autenticato, `403` = non autorizzato.

## 3. Cifratura campo-per-campo (GDPR art. 32) — #7

Dati personali sensibili cifrati **a riposo**, con **chiavi derivate
per-tenant**, così che un breach del solo database non esponga il chiaro.

> Questa sezione descrive la **meccanica**. Le **motivazioni** delle scelte
> (modello di minaccia, perché il nome resta in chiaro, alternative scartate,
> roadmap TDE) sono in [11 — Cifratura dati & GDPR](11-Data-Encryption.md).

### Primitive (`security/crypto`)
- **`TenantEncryptionService`**:
  - `enc_key = HKDF-SHA256(masterKey, salt=schema, info="dental-enc-v1", 32)` →
    `AES-256-GCM` (IV random 12B, tag 128 bit), output `Base64(iv‖ct‖tag)`.
  - `blindIndex(value, schema)`: `HMAC-SHA256` su chiave HKDF **separata**
    (`info="dental-blind-idx-v1"`), normalizzazione `trim().toUpperCase`, output
    esadecimale → **ricerca esatta** su dato cifrato.
  - HKDF (RFC 5869) implementato su `javax.crypto.Mac`, **senza BouncyCastle**.
- **`MasterKeyProvider`**: astrazione della master key (seam per HashiCorp
  **Vault** futuro). Oggi `ConfigMasterKeyProvider` legge la chiave dalla config
  e fa **fail-fast** (avvio bloccato) se assente / non-hex / lunghezza errata.

### Campi cifrati
| Campo | Colonne | Ricerca |
|-------|---------|---------|
| `patients.birth_date` | `birth_date_enc` (età calcolata in Java, TZ `Europe/Rome`) | — |
| `patients.fiscal_code` | `fiscal_code_enc` + `fiscal_code_idx` | esatta (blind index) |
| `invoices.patient_fiscal_code` (snapshot) | `patient_fiscal_code_enc` | — |

`first_name`/`last_name` restano in chiaro (ricerca anagrafica full-text) —
limite noto e accettato. Le colonne plaintext sono **mantenute** (azzerate dai
write al cutover, `DROP` rimandato dopo verifica prod).

### Rollout stadiato
`dual-write` → `migrate` (endpoint idempotente `POST /api/admin/encryption/migrate`,
tenant-scoped, ritorna `{"birthDate":N,"fiscalCode":M}`) → `cutover` (lettura da
`_enc`, ricerca via `_idx`, viste su `_enc`). Le viste `v_patient_*` espongono le
colonne `_enc`/`_idx`, mai il plaintext.

### Master key — gestione
Dev: `backend/config/application.properties` (gitignored). Prod:
`config/application-prod.properties` montata sul server (placeholder non-hex nei
file versionati → fail-fast finché non impostata). **Chiave prod diversa da
dev.** Perdita della chiave = dati cifrati **irrecuperabili**. Generazione:
`openssl rand -hex 32`.

## 4. Altre misure

- **CORS** controllato; **HTTPS** in produzione.
- Segreti fuori dal repo (config esterne gitignored) e fuori dall'immagine
  Docker (montati a runtime).
- Callback del servizio AI firmati **HMAC** (`HmacVerifier`).
- Nessun dato sensibile nei log; stack trace non esposti in prod.
- Validazione input server-side (Bean Validation, `@ValidFiscalCode`).

## 5. Postura regolatoria (AI Act, MDR, GDPR)

La piattaforma è oggi in **stato dimostrativo**: nessuno studio la usa su pazienti reali.
Questo determina il regime applicabile.

- **AI Act** — si applica quando un sistema è immesso sul mercato o messo in servizio.
  Finché DentalCare è una demo con dati fittizi gli obblighi non sono ancora scattati;
  scattano **tutti insieme al primo paziente reale**. Per questo la conformità è
  organizzata come **gate di go-live** e non come scadenza di calendario: vedi i criteri
  in [Release 1.x §29](../03-Product-Roadmap/Release-1.x.md#29-criteri-go-live--gate-1).
- **Perimetro non high-risk** — Copilot e assistente vocale sono AI **amministrative**:
  obblighi di trasparenza (art. 50), AI literacy (art. 4), governance, registro AI,
  policy d'uso. Il confine da non superare: un'AI che suggerisce diagnosi, terapia o
  priorità clinica cambia classificazione.
- **MDR** — il modulo di analisi radiologica è probabile Medical Device Software e resta
  **disattivato in produzione clinica** fino alla marcatura CE
  ([Release 2.x](../03-Product-Roadmap/Release-2.x.md)). La separazione tecnica del modulo
  è ciò che rende dimostrabile quale parte del prodotto è soggetta a MDR.
- **GDPR** — cifratura a riposo già attiva (§3); DPIA, informative, DPA con i fornitori
  AI, diritti dell'interessato: Release 1.x.
- **L. 132/2025** — il paziente ha diritto di essere informato dell'uso dell'AI in sanità;
  la decisione resta al professionista.

Il dettaglio dei controlli di supervisione umana implementati (conferma obbligatoria delle
scritture del Copilot, tracciabilità della versione dei modelli, distinzione tra output AI
e osservazione umana) è in [04-AI](04-AI.md).

## 6. Roadmap sicurezza

**Release 1.x** (prerequisiti di go-live):
- **audit trail clinico** append-only — accessi, letture, scritture, export
  (vedi [12-Clinical-Record-Model §4](12-Clinical-Record-Model.md#4-audit-trail));
- **MFA** per professionisti e amministratori;
- verifica end-to-end della segregazione dei ruoli, con test automatici;
- **integrità dei documenti**: impronta SHA-256, verifica MIME, scansione malware;
- test cross-tenant automatici;
- **pen test** e restore test documentati.

**Successive:**
- `VaultMasterKeyProvider` (rotazione/gestione centralizzata chiavi);
- Slice 2b cifratura: `phone` / `email` / `address` (normalizzazione blind index dedicata);
- `DROP` delle colonne plaintext dopo verifica prod prolungata;
- valutazione TDE / cifratura del volume per il dato a riposo su disco e backup
  (vedi [11-Data-Encryption §6](11-Data-Encryption.md));
- SSO OIDC/SAML per clienti enterprise.
