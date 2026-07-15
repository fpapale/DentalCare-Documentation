# 11 — Cifratura dati & scelte GDPR

> Questo capitolo motiva le **decisioni di progetto** sulla protezione dei dati
> personali a riposo. La meccanica implementativa (primitive, colonne, rollout)
> è in [07-Security §3](07-Security.md). Qui si spiega il **perché**: modello di
> minaccia, trade-off, e cosa è deliberatamente lasciato in chiaro.

## 1. Premessa giuridica: la GDPR non impone di cifrare tutto

Errore comune: "dato personale in chiaro nel DB = violazione GDPR". Non è così.

L'**art. 32** chiede misure tecniche e organizzative **adeguate al rischio** e
cita la cifratura come esempio *"ove opportuno"* (`where appropriate`), non come
obbligo assoluto su ogni colonna. La conformità è un **insieme proporzionato** di
misure, non la cifratura indiscriminata.

Un gestionale sanitario con nominativi in chiaro, protetto da autenticazione,
autorizzazione per ruolo, isolamento multi-tenant, accesso DB ristretto a rete
privata, TLS in transito e backup protetti, è **pratica standard e conforme**.
Nome e cognome, isolati, sono dato personale **comune** (non categoria
particolare dell'art. 9): il dato sanitario è la *relazione* fra la persona e le
prestazioni cliniche, non il nome in sé.

La cifratura campo-per-campo qui adottata è quindi una misura di
**difesa-in-profondità mirata**, non un requisito di legge "tutto-o-niente".

## 2. Modello di minaccia

Le scelte discendono da *cosa* si vuole mitigare. Scenari, dal più al meno
probabile:

| # | Minaccia | Mitigato da |
|---|----------|-------------|
| M1 | **Esfiltrazione di un dump/backup del DB** (credenziali rubate, backup mal custodito) | Cifratura app-level dei campi forti (§3) |
| M2 | **Insider / DBA** che legge le tabelle | Cifratura app-level (chiave fuori dal DB) |
| M3 | **Furto del disco / snapshot** della macchina | *Non ancora coperto* → TDE/disk-encryption (§6) |
| M4 | Accesso applicativo non autorizzato | Auth + ruoli lato server (07-Security) |
| M5 | Intercettazione in transito | TLS |

La cifratura di campo protegge **M1 e M2**: chi ottiene il dump vede blob
`Base64`, non i valori. La chiave non è nel database — è derivata da una master
key montata a runtime e mai persistita accanto ai dati.

## 3. Cosa è cifrato, e perché *quei* campi

Cifrati (`patients`): **`birth_date`** e **`fiscal_code`**; più lo snapshot
`invoices.patient_fiscal_code`.

Criterio: si cifrano gli **identificatori forti e i dati a maggior rischio di
re-identificazione**, non ogni attributo.

- **`fiscal_code`** — identificatore **univoco nazionale**. Da solo lega un
  record a una persona fisica reale in modo deterministico. È il singolo campo
  più pericoloso in un breach: consente incrocio con altre banche dati.
- **`birth_date`** — forte fattore di **re-identificazione** (data di nascita +
  altri quasi-identificatori restringe drasticamente l'insieme). Dato a rischio
  in analisi di de-anonimizzazione.

Cifrando questi due, un dump esfiltrato contiene nomi ma **non** i due
identificatori che li ancorano univocamente a una persona: l'impatto del breach
si riduce da "elenco pazienti completo e collegabile" a "elenco di nomi senza
CF/nascita".

## 4. Perché nome e cognome restano in chiaro

Decisione **deliberata**, non una lacuna.

- **Ragione tecnica.** Il nome richiede **ricerca parziale** (`ILIKE '%mar%'`,
  typeahead, liste ordinate alfabeticamente). Il meccanismo di ricerca su dato
  cifrato adottato — *blind index* — supporta solo il **match esatto**. Cifrare
  il nome romperebbe la ricerca anagrafica, funzione core del gestionale.
- **Ragione di rischio.** Nome+cognome sono dato comune; il loro valore per un
  attaccante crolla senza gli identificatori forti (§3), che invece sono cifrati.
- **Misure compensative** già presenti: auth, ruoli, isolamento tenant, rete
  privata DB, TLS, backup protetti.

Trade-off esplicito e tracciato: **operatività della ricerca** vs
**cifratura del nome**. Si è scelta l'operatività, coprendo il rischio maggiore
(re-identificazione via CF/nascita) per altra via.

## 5. Motivazione delle scelte crittografiche

| Scelta | Alternativa scartata | Perché |
|--------|----------------------|--------|
| **Chiave per-tenant** (`HKDF(masterKey, salt=schema)`) | Chiave unica globale | Un tenant compromesso non espone gli altri; coerente con isolamento schema-per-tenant. Deriva deterministica → nessuna tabella-chiavi da gestire. |
| **AES-256-GCM** | AES-CBC + HMAC separato | AEAD in una primitiva: riservatezza **e** integrità/autenticità (tag) insieme, meno superficie d'errore. |
| **Blind index** (`HMAC-SHA256`, chiave separata) per il CF | Cifratura deterministica del campo | HMAC dedicato non rivela il ciphertext reale e non permette di decifrare dall'indice; consente ugualmente la ricerca esatta del CF. Chiave d'indice **distinta** da quella di cifratura. |
| **HKDF su `javax.crypto`** | BouncyCastle | Zero dipendenze crittografiche esterne: superficie e manutenzione minori. |
| **`MasterKeyProvider` (astrazione)** | Chiave hardcoded / solo da file | *Seam* pronto per HashiCorp Vault. Oggi `ConfigMasterKeyProvider` da config; domani rotazione centralizzata senza toccare il codice di cifratura. |
| **Fail-fast** se la master key manca/è invalida | Degradare silenziosamente | Meglio un avvio bloccato e visibile che scrivere/leggere dati con chiave errata o assente. |
| **Colonne plaintext mantenute** dopo il cutover | `DROP` immediato | Rollback sicuro: il codice precedente rilegge il chiaro. `DROP` solo dopo verifica prod prolungata. Le write azzerano il chiaro nel frattempo. |
| **Master key diversa dev/prod, fuori dal repo** | Chiave condivisa/versionata | Compromissione di dev non tocca prod; nessun segreto in git o nell'immagine Docker. |

**Nota operativa critica:** perdita della master key di produzione =
`*_enc` **irrecuperabili**. Nessun recovery. La chiave va custodita in un secret
store e mai committata.

## 6. Rischio residuo e roadmap

**Cosa resta scoperto oggi:**

- **Nominativi, contatti e altri attributi** sono in chiaro nel dump/disco (M1
  parzialmente, M2, M3).
- Le **colonne plaintext** di `birth_date`/`fiscal_code` esistono ancora (per
  rollback) finché non verranno droppate.

**Opzioni per estendere la copertura** (in ordine di rapporto valore/costo):

| Opzione | Copre | Costo | Impatto ricerca |
|---------|-------|-------|-----------------|
| **A. TDE / cifratura del volume PostgreSQL** | M3 (disco/backup rubato) su **tutti** i campi | Basso (infra, no codice) | **Nessuno** (typeahead intatto) |
| **B. Cifratura app-level del nome + ricerca esatta** | M1/M2 sul nome | Medio | Perde la ricerca **parziale** |
| **C. Cifratura + blind index n-gram sul nome** | M1/M2 sul nome, ricerca parziale | Alto | Ricerca parziale su dato cifrato (complessa) |

**Raccomandazione.** L'**opzione A** copre lo scenario più realistico (furto di
backup/disco) su *tutti* i campi in un colpo solo, senza rompere la ricerca né
aggiungere complessità applicativa. La cifratura app-level già in essere
(nascita/CF) resta per il rischio **insider/DBA** (M2), che il TDE **non**
copre. A e app-level sono complementari, non alternative.

**Roadmap cifratura:**

- **Slice 2b**: `phone` / `email` / `address` (blind index con normalizzazione
  dedicata: telefono solo cifre, email lowercase).
- **TDE / disk-encryption** in produzione (valutazione — copre nomi e tutto il
  resto per M3).
- **`VaultMasterKeyProvider`**: gestione e rotazione centralizzata delle chiavi.
- **`DROP`** delle colonne plaintext dopo verifica prod prolungata.

## 7. Sintesi delle decisioni

1. GDPR non impone cifratura totale → misure **proporzionate al rischio**.
2. Cifrati gli **identificatori forti** (CF, nascita): massimo impatto sul breach.
3. Nome in chiaro = trade-off **deliberato** per la ricerca, rischio residuo
   coperto da misure compensative.
4. Scelte crypto orientate a **isolamento per-tenant**, **AEAD**, **zero
   dipendenze esterne** e **seam Vault**.
5. Rischio residuo su disco/backup indirizzabile con **TDE** (roadmap), su
   contatti con **Slice 2b**.
