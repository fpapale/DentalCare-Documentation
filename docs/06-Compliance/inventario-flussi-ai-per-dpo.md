# Inventario dei flussi AI — risposte tecniche per il DPO

**Versione:** 1.0 — 18/09/2026
**Scopo:** dare al DPO, in un unico posto, le risposte *tecniche* verificabili sul codice, così
che ROPA (art. 30), DPIA (art. 35) e negoziazione dei DPA (art. 28) non debbano ricostruirle.

> **Cosa questo documento è e cosa non è.**
> È un **inventario tecnico**, redatto leggendo il codice sorgente: ogni affermazione è
> verificabile al file e alla riga indicati. **Non è** una valutazione legale, non individua
> basi giuridiche, non sostituisce DPIA né ROPA. Le colonne *base giuridica*, *necessità e
> proporzionalità*, *periodo di conservazione contrattuale* restano **da compilare al DPO**.
>
> Le sezioni marcate **[DA COMPILARE — DPO]** sono deliberatamente vuote: riempirle qui senza
> un parere sarebbe peggio che lasciarle in bianco.

---

## 1. Quadro in una pagina

Fornitori esterni che ricevono dati, allo stato attuale del codice:

| # | Fornitore | Ruolo | Cosa riceve | Categoria art. 9? | Stato DPA |
|---|---|---|---|:-:|---|
| 1 | **OpenAI** | Modello linguistico (API) | Copilot AI: contenuto conversazione **+ risultato dei tool** (dati clinici) | **Sì** | ❌ non stipulato |
| 2 | **OpenAI** | Modello linguistico (API) | Errori intelligenti: testo del messaggio d'errore | No (vedi §4) | ❌ non stipulato |
| 3 | **Retell AI** | Agente vocale telefonico | Audio e trascrizione della telefonata del paziente | **Sì** (potenziale) | ❌ non stipulato |

**Non escono dall'infrastruttura:**

| Componente | Perché | Evidenza |
|---|---|---|
| **AI radiologica** (rilevamento carie su ortopanoramica) | Servizio **self-hosted**: container proprio, modelli ONNX montati da volume locale, raggiunto per nome di rete interna | `docker-compose.yml:62-73` · `application.properties:98` (`app.ai.base-url=http://dentalcare-ai-service:8000`) |
| Immagini e documenti paziente | MinIO self-hosted, bucket per tenant | `MinioStorageService` |
| Database clinico | PostgreSQL su rete interna, uno schema per tenant | — |

> **Nota di rilievo per la DPIA.** Il componente a rischio più alto sotto l'AI Act — la
> radiologia — è quello che **non** trasferisce nulla a terzi. Il trasferimento riguarda il
> Copilot testuale e l'agente vocale.

---

## 1-bis. Tabella per il ROPA (art. 30)

Struttura dato / finalità / destinatario / base giuridica. Le prime tre colonne sono compilate
dal codice; **la quarta è del DPO** — indicare una base giuridica senza parere legale sarebbe
un'affermazione non verificata, e questo documento non ne contiene.

| # | Dato trattato | Categoria | Finalità | Destinatario | Trasferimento extra-UE | Conservazione (lato app) | Base giuridica |
|---|---|---|---|---|:-:|---|---|
| A1 | Contenuto della conversazione con il Copilot (messaggi utente + risposte) | Dati comuni | Assistenza operativa all'utente di studio | **OpenAI** | Da verificare | 90 gg (configurabile) | **[DPO]** |
| A2 | Anagrafica paziente restituita dai tool | Dati comuni | Rispondere a richieste operative sull'assistito | **OpenAI** | Da verificare | Nel contesto conversazione → 90 gg | **[DPO]** |
| A3 | **Allergie e terapie in corso** (anticoagulanti, bifosfonati) | **Art. 9 — salute** | Alert clinici in conversazione | **OpenAI** | Da verificare | Nel contesto conversazione → 90 gg | **[DPO]** — serve una condizione art. 9(2) |
| A4 | **Odontogramma, diagnosi, prescrizioni, diario clinico, piani di cura** | **Art. 9 — salute** | Consultazione e preparazione di scritture cliniche | **OpenAI** | Da verificare | Nel contesto conversazione → 90 gg | **[DPO]** — serve una condizione art. 9(2) |
| A5 | Registro delle azioni del Copilot | Dati comuni | Tracciabilità e attribuzione | *Interno* | No | Nessuna cancellazione automatica ⚠️ | **[DPO]** |
| B1 | Testo del messaggio d'errore (numeri documento, importi, nomi prestazione) | Dati comuni — vedi §4 | Rendere comprensibile l'errore all'operatore | **OpenAI** | Da verificare | **Nessuna** (cache volatile) | **[DPO]** |
| C1 | Audio della telefonata del paziente | **Art. 9 — potenziale** | Prenotazione e gestione appuntamenti | **Retell AI** | Da verificare | **[DPO]** — lato fornitore | **[DPO]** |
| C2 | Trascrizione della telefonata | **Art. 9 — potenziale** | Come sopra | **Retell AI** | Da verificare | **[DPO]** — lato fornitore | **[DPO]** |
| D1 | Immagine radiografica (ortopanoramica) | **Art. 9 — salute** | Rilevamento assistito di carie | *Interno — self-hosted* | **No** | MinIO, per tenant | **[DPO]** |
| D2 | Esito del rilevamento (condizioni dentali) | **Art. 9 — salute** | Proposta al medico, mai diagnosi automatica | *Interno — self-hosted* | **No** | DB per tenant | **[DPO]** |

**Interessati:** pazienti dello studio (A2-A4, C1-C2, D1-D2); personale di studio (A1, A5, B1).

**Titolare / responsabile:** il rapporto fra studio odontoiatrico e DentalCare Pro è impostato
in `directives/DentalCare_Pro_EU_AI_Act_Compliance_2026.md:976` (*"DentalCare come responsabile
del trattamento per l'erogazione SaaS, se opera su istruzioni"*). **[DA COMPILARE — DPO]** la
qualificazione definitiva e la catena verso i sub-responsabili OpenAI e Retell.

> **Le righe A3 e A4 sono il cuore della questione.** Sono dati relativi alla salute inviati a
> un fornitore terzo, oggi senza DPA. Tutto il resto della tabella è meno oneroso.

---

## 2. Le domande che il DPO porrà, con la risposta dal codice

### 2.1 Quali dati personali escono verso il fornitore del modello?

**Flusso A — Copilot AI** (`ChatService.java`)

Al modello viene inviato: prompt di sistema, cronologia della conversazione, messaggio
dell'utente, **e i risultati dei tool** che il modello invoca. Quest'ultimo punto è il
sostanziale: i tool leggono il database clinico e il loro output rientra nel contesto della
conversazione.

`DentalCareAiTools` espone **151 tool** (`grep -c "@Tool"`). Fra i dati restituiti:

| Dato | Tool | Art. 9 |
|---|---|:-:|
| Anagrafica paziente completa | *"Get detailed information about a specific patient. Medical staff see full clinical data"* | — |
| **Allergie, terapie in corso** (anticoagulanti, bifosfonati) | *"Get anamnesis alerts for a patient"* | **Sì** |
| Odontogramma, incluse condizioni rilevate dall'AI radiologica | *"Get the odontogram (tooth conditions)"* | **Sì** |
| Diagnosi | *"Prepare adding a diagnosis (diagnosi)"* | **Sì** |
| Prescrizioni | *"Prepare adding a prescription (prescrizione)"* | **Sì** |
| Diario clinico | *"Prepare adding a clinical diary entry"* | **Sì** |
| Piani di cura | *"Prepare creation of a new treatment plan"* | **Sì** |

**Conclusione tecnica:** il Copilot trasferisce **dati relativi alla salute** al fornitore del
modello. È il flusso dominante, ed è **già attivo**.

**Flusso B — Errori intelligenti** (`ErrorExplanationService.java`)

Inviato: `operation`, `code`, `message`. Nient'altro — nessun tool collegato
(`ErrorExplanationService.java:86`, commento esplicito). Vedi §4 per il contenuto effettivo.

**Flusso C — Agente vocale Retell** (`Segretaria/*.json`, `compliance/aiact/retell/`)

L'agente riceve la voce del chiamante e la trascrive. Il contenuto dipende da cosa dice il
paziente: può includere motivo della visita, sintomi, dati identificativi.
**[DA COMPILARE — DPO]** perimetro effettivo e informativa in apertura di chiamata (già
affrontata per l'art. 50 AI Act in `compliance/aiact/retell/`).

---

### 2.2 Il fornitore usa i dati per addestrare i propri modelli?

**Non determinabile dal codice.** È una clausola contrattuale, da verificare nel DPA.
Già annotata come da verificare in `directives/piano-lungo-termine.md:147`
(*"DPA + SCC + TIA per Retell, OpenAI, cloud → verificare no-training e data location"*).

**[DA COMPILARE — DPO]**

---

### 2.3 Dove sono trattati i dati? Serve un trasferimento extra-UE?

**Non determinabile dal codice**: dipende dall'endpoint e dalla region del fornitore.
Il codice non fissa una region — usa il client Spring AI con la configurazione di default.

Se il trattamento avviene fuori UE servono SCC + TIA. **[DA COMPILARE — DPO]**

---

### 2.4 Quanto a lungo restano i dati *dentro* l'applicazione?

| Dato | Dove | Conservazione | Evidenza |
|---|---|---|---|
| Conversazioni Copilot | `chat_sessions`, `chat_messages` (per tenant) | **Configurabile**, default **90 giorni**; cancellazione su `DELETE FROM chat_sessions` per età | `ChatHistoryService.java:55,68,88` · `AppSettings.chatHistoryDays` |
| Azioni del Copilot | `ai_audit_log` (per tenant) | Nessuna cancellazione automatica | `AiAuditService.java:38` |
| Testi inviati agli errori intelligenti | **Non persistiti**. Cache solo in memoria, max 200 voci, persa al riavvio | `ErrorExplanationService.java:43,99-100` |

La conservazione **presso il fornitore** è un'altra questione: **[DA COMPILARE — DPO]**, è
clausola di DPA.

---

### 2.5 Che misure di sicurezza sono già implementate?

Verificabili sul codice:

| Misura | Dettaglio | Evidenza |
|---|---|---|
| **Cifratura a riposo** per-tenant | `birth_date` e `fiscal_code` cifrati. Chiave derivata per tenant: `HKDF-SHA256(masterKey, salt=schema)`, cifratura `AES/GCM/NoPadding` con IV a 12 byte e tag a 16 | `TenantEncryptionService.java:19-27` |
| **Blind index** sul codice fiscale | Ricerca senza decifrare | `patients.fiscal_code_idx` |
| **Isolamento multitenant** | Uno schema PostgreSQL per tenant; nome validato contro `^t_[0-9a-f]{8}$` prima di ogni query | `TenantContext.validatedSchema()` |
| **Audit delle azioni AI** | Ogni azione del Copilot registrata per tenant | `AiAuditService` |
| **Gate di conferma del Copilot** | Nessuna scrittura diretta: il modello prepara un'anteprima, la scrittura richiede conferma esplicita lato server | tool `Prepare …` + `confirmAction` |
| **Limite di input** sugli errori intelligenti | Max 2000 caratteri; oltre, il testo non viene inviato | `ErrorExplanationService.java:40,71` |

---

### 2.6 Il trattamento si può disattivare? Con quale granularità?

| Flusso | Interruttore | Granularità |
|---|---|---|
| Errori intelligenti | `app.ai.smart-errors.enabled` (server) | **Per studio** — a `false` nessun testo viene inviato |
| Errori intelligenti | `AppSettings.smartErrors` (client) | Per utente/postazione, default attivo — **preferenza, non misura** (vedi nota) |
| Copilot AI | — | ⚠️ **Nessun interruttore dedicato** |
| AI radiologica | `ai.radiology.enabled` (previsto dal gate no-clinical) | Per studio — `directives/piano-lungo-termine.md:93` |

> **Nota sul flag client.** `AppSettings.smartErrors` vive nel `localStorage` del browser:
> vale per quella postazione, si azzera svuotando la cache del browser e non è verificabile a
> posteriori. Va letto come **preferenza dell'utente**, non come misura tecnica: l'unico
> controllo opponibile sugli errori intelligenti è quello server-side.

> ⚠️ **Lacuna nota — tracciata come [#55].** Il flusso con l'esposizione maggiore (Copilot,
> dati art. 9) è l'unico **privo di un interruttore dedicato**. Se la DPIA dovesse richiedere
> di sospenderlo, oggi l'unica leva è rimuovere la chiave API — che spegne anche gli errori
> intelligenti, perché condividono la stessa chiave.
>
> **Verificato:** un interruttore sul Copilot **non fermerebbe Giulia**. I workflow n8n non
> passano da `/api/chat`: chiamano direttamente `api/appointments`, `api/patients`,
> `api/providers`. Le prenotazioni telefoniche restano operative.
>
> **Decisione del committente (18/09/2026):** problema tracciato, **nessuna modifica alle
> funzionalità** finché non c'è un incontro col DPO. Disegno proposto e stime in
> [`directives/proposte-modifiche.md` §55](../../directives/proposte-modifiche.md) — in sintesi:
> colonna per-tenant `clinics.copilot_mode` sul modello di `billing_mode`, rifiuto applicato
> **lato server** (non nascondendo la UI), modifica riservata a `TENANT_ADMIN` e tracciata in
> `ai_audit_log`; eventuale terza posizione «solo funzioni non cliniche» se il DPO chiede la
> minimizzazione.

---

### 2.7 I dati inviati sono minimizzati?

**Errori intelligenti:** sì, per costruzione — vedi §4.

**Copilot:** no. I tool restituiscono il record clinico come lo leggono dal database; non
esiste pseudonimizzazione né redazione prima dell'invio al modello. È la leva tecnica
principale se la DPIA chiede di ridurre l'esposizione. **[DA COMPILARE — DPO]** se e quanto
sia richiesto.

---

## 3. Cosa chiedere nel DPA (art. 28) — checklist tecnica

Voci su cui il DPO chiederà una risposta e che il contratto deve coprire. L'ordine non implica
priorità legale.

- [ ] **Categorie di dati dichiarate**: includere esplicitamente i **dati relativi alla salute
      (art. 9)** per il flusso Copilot. Cambia le garanzie esigibili.
- [ ] **No-training**: esclusione dell'uso dei dati per l'addestramento dei modelli del fornitore.
- [ ] **Ubicazione del trattamento** e, se extra-UE, SCC + TIA.
- [ ] **Conservazione lato fornitore** dei prompt e tempi di cancellazione.
- [ ] **Sub-responsabili** autorizzati e obbligo di informativa sulle variazioni.
- [ ] **Misure di sicurezza** (art. 32) e **notifica di data breach** con tempistiche.
- [ ] **Assistenza al titolare** per l'esercizio dei diritti dell'interessato (artt. 15-22).
- [ ] **Cancellazione o restituzione** dei dati al termine del contratto.
- [ ] **Diritto di audit** o accettazione di certificazioni equivalenti.

Da stipulare con: **OpenAI** (flussi A e B) e **Retell AI** (flusso C).

---

## 4. Errori intelligenti (#54) — scheda di dettaglio

Trattata a parte perché introdotta il 18/09/2026 e perché è il flusso su cui più facilmente si
sovrastima il rischio.

**Cosa viene inviato:** il testo del messaggio d'errore prodotto dal backend, più l'operazione
e il codice.

**Cosa il messaggio contiene**, verificato sulle eccezioni presenti nel codice:

| Presente | Esempio |
|:-:|---|
| ✅ | Numeri di documento — `PARC-2026-00011` |
| ✅ | Importi — `3.030,00 EUR` |
| ✅ | Nomi di prestazioni — `Impianto osteointegrato 45`, `Corona in zirconia 44` |
| ✅ | Identificativi tecnici (UUID) |
| ❌ | **Nomi di paziente** — nessuna eccezione nel codice li interpola (verificato) |
| ❌ | Codici fiscali, date di nascita, recapiti |
| ❌ | Dati clinici (diagnosi, anamnesi, prescrizioni) |

**Osservazione onesta:** il nome del paziente non compare *oggi*, ma è una proprietà dei
messaggi attualmente scritti, **non un controllo imposto dal codice**. Un messaggio d'errore
futuro potrebbe includerlo senza che nulla lo impedisca. Se la DPIA lo richiede, va introdotta
una redazione esplicita prima dell'invio.

**Persistenza:** nessuna lato applicazione. Cache in memoria (max 200 voci), persa al riavvio.

**Disattivazione:** doppio interruttore, §2.6. A funzione spenta **nessun testo lascia
l'applicazione** — dichiarato anche nella UI (Impostazioni → Sistema).

**Default attivo:** scelta di prodotto del committente, 18/09/2026. Documentata qui perché sia
una decisione tracciata e non un'impostazione implicita.

---

## 5. Riferimenti

| Documento | Cosa contiene |
|---|---|
| `directives/piano-lungo-termine.md` §2, §5 | Tempi DPIA/DPA, gate di go-live (*"DPA firmati con tutti i fornitori AI"*) |
| `directives/piano-lungo-termine.md:71` | Stato governance: *"no DPIA, no ROPA, no DPA, no policy, no registro AI"* |
| `directives/DentalCare_Pro_EU_AI_Act_Compliance_2026.md` | Perimetro AI Act, ruoli titolare/responsabile |
| `directives/proposte-modifiche.md` #54 | Proposta errori intelligenti e nodo privacy |
| `compliance/aiact/retell/` | Evidenze art. 50 per l'agente vocale |

---

## 6. Stato e prossimo passo

Nessun DPA è ad oggi stipulato, per nessuno dei tre flussi. Il percorso critico della Fase 1
passa per l'ingaggio del DPO (`piano-lungo-termine.md` §2): questo documento serve a fargli
risparmiare la ricostruzione tecnica, non a sostituirne il lavoro.

**Da aggiornare** ogni volta che: si aggiunge un fornitore AI, un tool del Copilot inizia a
restituire una nuova categoria di dati, o cambia un interruttore di disattivazione.

### Punti aperti tracciati, non ancora affrontati

| # | Punto | Stato | Sblocca |
|---|---|---|---|
| [#55] | Il Copilot è l'unico flusso senza interruttore dedicato (§2.6) | **Tracciato, non implementato** — decisione del committente 18/09/2026 | Incontro col DPO / avvio DPIA |
| — | DPA con OpenAI e Retell (§1, §3) | Non stipulati | Ingaggio del DPO |
| — | Base giuridica art. 9(2) per le righe A3-A4 del ROPA | **[DPO]** | Ingaggio del DPO |
| — | Retention del registro azioni Copilot (riga A5): nessuna cancellazione automatica | Aperto | Policy di conservazione |

Le funzionalità restano **come sono** finché il DPO non si esprime: nessuna delle voci qui
sopra è stata modificata nel codice per anticiparne il parere.
