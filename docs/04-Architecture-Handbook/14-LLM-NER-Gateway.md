# 14 — LLM NER Gateway & Demo Simulator

Documentazione architetturale e operativa dei componenti di sicurezza e anonimizzazione privacy-preserving per le chiamate verso modelli linguistici (LLM):
- **`llm-ner-gateway`** (Repository: [`fpapale/llm-ner-gateway`](https://github.com/fpapale/llm-ner-gateway)): Reverse proxy enterprise Java Spring Boot 3.5 / Java 25 con motore Dual-Engine NER in Python.
- **`llm-gateway-demo`** (Repository: [`fpapale/llm-gateway-demo`](https://github.com/fpapale/llm-gateway-demo)): Suite web di collaudo, simulatore client e ispettore Side-by-Side a 3 pannelli.

> [!IMPORTANT]
> **AUTONOMIA TOTALE E ARCHITETTURA CONTAINER DOCKER**
> Il sistema è completamente autonomo e opera nativamente tramite **container Docker** sulla rete `dentalcarepro_dentalcarepro`:
> - Il repository **`llm-ner-gateway`** incapsula ed espone **entrambi i motori NER**: il modello fine-tuned `llm-ner-dentalcare-0.3B` e il modello standard `spaCy` (`it_core_news_lg`).
> - Il deployment Docker Compose avvia sia l'istanza primaria (:8080 su 0.3B) sia l'istanza di confronto (:8085 con `NER_MODEL=spacy`), generate dalla **medesima immagine** di `llm-ner-gateway`.
> - Non esiste alcuna dipendenza verso cartelle o repository legacy per l'esecuzione di spaCy.
> - L'installazione e la manutenzione sul server (`192.168.0.72`) avvengono esclusivamente tramite gli script bash idempotenti `scripts/install-llm_gateway.sh` e `scripts/update-llm-gateway.sh`.

---

## 1. Visione Architetturale e Ruolo nel Sistema

Nelle applicazioni sanitarie multi-tenant come **DentalCare Pro**, l'interazione con modelli di fondazione esterni (es. OpenAI GPT-4.1) introduce un severo rischio regolatorio: l'esportazione non controllata di **dati personali (Art. 4 GDPR)** e **dati particolari sulla salute (Art. 9 GDPR)** verso server di terze parti.

`llm-ner-gateway` costituisce il **confine di fiducia invalicabile (Trust Boundary)** tra l'ecosistema applicativo (backend Spring Boot, tool del Copilot, gestione errori) e i provider LLM pubblici:

```mermaid
flowchart LR
    subgraph Core["Dominio di Fiducia Interno (DentalCare Pro)"]
        Backend["DentalCare Backend<br/>(Spring Boot / Java 25)"]
        UI["Copilot UI / Chat"]
        Tools["DentalCareAiTools<br/>(151 Tool Clinici & DTO)"]
    end

    subgraph Gateway["Confine di Sicurezza (llm-ner-gateway)"]
        Auth["Auth & Policy Guard<br/>(JWT ES256 / P-256)"]
        Vault["InMemoryTokenVault<br/>(RAM-Only / Per-Tenant)"]
        NER["Dual-Engine NER<br/>(DentalCare 0.3B / spaCy)"]
        Sanitizer["DTO & Text Sanitizer<br/>(DROP / TEXT / ALLOW / UUID)"]
        Detokenizer["Response Detokenizer<br/>(Ripristino Dati Originali)"]
        FailClosed["Fail-Closed Engine<br/>(502 UNKNOWN_TOKEN)"]
    end

    subgraph External["Dominio Esterno Non Affidabile"]
        OpenAI["OpenAI API / LLM Cloud<br/>(Vede SOLO Pseudonimi)"]
    end

    UI --> Backend
    Backend --> Tools
    Backend -->|"POST /v1/chat/completions<br/>(Payload in chiaro + JWT ES256)"| Auth
    Auth --> Sanitizer
    Sanitizer <--> NER
    Sanitizer <--> Vault
    Sanitizer -->|"Richiesta Anonimizzata<br/>(PERSONA_1, TEL_1, UUID surrogati)"| OpenAI
    OpenAI -->|"Risposta con Pseudonimi"| FailClosed
    FailClosed --> Detokenizer
    Detokenizer <--> Vault
    Detokenizer -->|"Risposta con Dati Ripristinati"| Backend
```

### Principi di Progetto Chiave

1. **Nessun Dato Sensibile all'LLM**: Nomi di pazienti e medici, numeri di telefono, indirizzi, codici fiscali, IBAN e numeri di documenti non lasciano mai l'infrastruttura in chiaro.
2. **Zero-Knowledge sul Provider**: Il fornitore LLM riceve token pseudonimi (`PERSONA_1`, `TEL_1`), segnaposto irreversibili (`[CATASTO]`, `[TARGA]`) e UUID surrogati effimeri.
3. **Nessuna API Key nel Core**: La chiave API di OpenAI risiede unicamente nel gateway. Il backend applicativo possiede solo la propria chiave privata crittografica EC per firmare i token di sessione.
4. **Isolamento Totale in RAM**: Il vault delle corrispondenze (`InMemoryTokenVault`) è memorizzato unicamente nella memoria volatile del gateway, indicizzato per `tenantRef` e `conversationRef`. Nessun dato pseudonimizzato viene persistito su database o disco.
5. **Fail-Closed su Allucinazioni**: Se l'LLM allucina un token non registrato nel vault della conversazione, la richiesta viene abortita all'istante con codice `502 UNKNOWN_TOKEN`, impedendo l'iniezione o il leak di dati cross-tenant.

---

## 2. Modello di Sicurezza e Controllo Accessi

### 2.1 Autenticazione Client tramite JWT `ES256` (Curva Ellittica P-256)

L'accesso a `llm-ner-gateway` è rigidamente controllato da crittografia asimmetrica a curva ellittica:
- **Algoritmo**: `ES256` (ECDSA con curva NIST P-256 e SHA-256).
- **Chiavi**: Il client possiede la chiave privata (`keys/client-private.pem`), mentre il gateway possiede unicamente la chiave pubblica (`config/client-public.pem`).
- **Claim Obbligatori**:
  - `iss` / `sub`: Identificativo dell'applicazione chiamante (es. `dentalcare`).
  - `application`: Dominio applicativo autorizzato (es. `dentalcare`, `legal`).
  - `purpose`: Finalità specifica del trattamento (es. `copilot-admin`, `clinical-copilot`, `smart-error`, `case-analysis`).
  - `tenantRef`: Identificativo univoco del tenant (es. `tenant-studio-rossi`).
  - `actorRef`: Identificativo dell'utente operatore.
  - `conversationRef`: Identificativo univoco della sessione di chat per il partitioning della memoria del vault.

### 2.2 Policy di Sanitizzazione per Finalità (`ApplicationPolicy`)

Il gateway applica policy differenziate in base alla tupla `(application, purpose)`:

| Policy | Finalità Applicativa | Campi Clinici | Note / Anamnesi | Campi Fiscali & Finanziari | Dati Identificativi PII |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **`dentalcare / copilot-admin`** | Gestione operativa studio, agenda e richiami | `DROP` | `DROP` | `DROP` | Pseudonimizzati (`PERSONA_n`) |
| **`dentalcare / clinical-copilot`** | Cartella clinica e piano di cura per medici | `ALLOW` (denti, allergie, terapie) | `TEXT` (bonifica PII) | `DROP` (IBAN, CF) | Pseudonimizzati (`PERSONA_n`) |
| **`dentalcare / smart-error`** | Umanizzazione errori applicativi (#54) | `DROP` | Redazione irreversibile | `DROP` | Redazione irreversibile (`[NOME]`, `[ID]`) |
| **`legal / case-analysis`** | Consulenza legale e perizie odontoiatriche | `ALLOW` | `TEXT` | `ALLOW` | Pseudonimizzati + Checksum P.IVA |

---

## 3. I Modelli di Named Entity Recognition (NER) e Motore Dual-Engine

L'anonimizzazione dei prompt verso i modelli linguistici (LLM) richiede un bilanciamento rigoroso tra **accuratezza clinico-semantica**, **velocità di inferenza** e **continuità di servizio (zero-downtime)**. Nel contesto di DentalCare Pro, la perdita di un identificativo personale (under-redaction) costituisce una violazione del GDPR (Art. 4 e Art. 9), mentre la cancellazione indebita di termini clinici o comandi dell'interfaccia (over-redaction) corrompe l'usabilità del Copilot.

A questo scopo, `llm-ner-gateway` adotta un'architettura **Dual-Engine** ibrida che combina modelli Deep Learning Transformer, pipeline statistiche convoluzionali, euristiche a due passate e validatori algoritmici deterministici.

---

### 3.1 Filosofia di Progetto e Architettura Dual-Engine

Il microservizio Python (`ner/app.py`), esposto internamente sulla porta `8000` (o `8098` in sviluppo), astrae l'esecuzione dei modelli e supporta la commutazione a caldo tramite configurazione parametrizzata in `config/config.yaml` o variabile d'ambiente `NER_MODEL`:

```yaml
ner:
  model: "auto"              # Opzioni: "auto" | "transformers" | "spacy"
  variant_max_length: 2000   # Soglia massima caratteri per analisi a doppia passata
  extra_app_words: []        # Termini protetti custom aggiuntivi
```

```mermaid
flowchart TD
    Req["Richiesta NER POST /analyze<br/>(Testo del prompt / DTO)"] --> CheckConf{"Configurazione ner.model"}
    CheckConf -->|"model: transformers"| LoadTrans["Carica Modello Fine-Tuned<br/>config/llm-ner-dentalcare-0.3B"]
    CheckConf -->|"model: spacy"| LoadSpacy["Carica spaCy<br/>it_core_news_lg"]
    CheckConf -->|"model: auto"| CheckDir{"Esiste cartella pesi<br/>llm-ner-dentalcare-0.3B?"}
    CheckDir -->|Sì| LoadTrans
    CheckDir -->|No (Fallback automatico)| LoadSpacy
    LoadTrans --> PreProc["Pre-Processing & Normalizzazione Simboli/Emoji"]
    LoadSpacy --> PreProc
    PreProc --> Infer["Inferenza Estrazione Entità (CPU Optimized)"]
    Infer --> PostProc["Post-Processing Dual-Pass + Euristiche APP_WORDS"]
    PostProc --> Resp["Entità Estratte (Offsets in Code-Points + Label)"]
```

#### Principio di Continuità e Graceful Degradation
Nei sistemi sanitari mission-critical, un errore nel download dei pesi del modello neurale o la mancanza temporanea di risorse GPU/RAM non deve mai causare il blocco dell'applicazione. Se la cartella del modello `llm-ner-dentalcare-0.3B` non è presente al boot del container, la modalità `auto` attiva immediatamente il fallback trasparente su `spaCy`, garantendo la protezione di base senza interrompere i servizi di studio.

---

### 3.2 Il Modello Fine-Tuned Specializzato: `llm-ner-dentalcare-0.3B` (ModernBERT)

Il motore neurale primario è un modello Transformer compatto da **300 milioni di parametri (0.3B)**, derivato dalla famiglia di modelli **ModernBERT / mmBERT** a 22 categorie PII italiane e specializzato tramite fine-tuning supervisionato sul dominio odontoiatrico:

1. **Finestra di Contesto Estesa a 8.192 Token**:
   - I modelli BERT tradizionali sono limitati a 512 token, costringendo a un frazionamento aggressivo del testo che distrugge le correlazioni tra frasi contigue.
   - `llm-ner-dentalcare-0.3B` supporta nativamente una finestra di **8.192 token**. Per testi lunghi fino a 1.000.000 di caratteri (es. perizie medico-legali, cartelle cliniche storiche), il microservizio adotta una strategia a finestre scorrevoli (`sliding windows`) con blocchi da **4.000 token** e sovrapposizione di sicurezza di **256 token** (`CHUNK_OVERLAP_TOKENS`), prevenendo tagli accidentali a metà di un'entità.
2. **Schema di Etichettatura BIO a 45 Tag**:
   - Il modello adotta lo schema standard BIO (*Beginning*, *Inside*, *Outside*): per ciascuna delle 22 categorie PII italiane viene emesso il tag `B-<LABEL>`, `I-<LABEL>` oppure `O`.
   - **Le 22 Categorie PII Italiane Riconosciute**:
     - `FULLNAME`: Nomi e cognomi di persone (pazienti, medici, familiari).
     - `ADDRESS` (composto da `STREET`, `BUILDINGNUM`, `CITY`, `ZIPCODE`, `PROVINCE`): Dati topografici completi.
     - `CATASTO`: Identificativi catastali (foglio, particella, subalterno).
     - `DOCID` / `ID_DOC`: Carte d'identità, patenti di guida, passaporti.
     - `TARGA`: Targhe automobilistiche italiane.
     - `PIVA`: Partite IVA aziendali e professionali.
     - `CF`: Codici fiscali di persone fisiche.
     - `IBAN`: Coordinate bancarie internazionali.
     - `EMAIL`, `TELEPHONENUM`: Canali di contatto digitali e telefonici.
     - `DATE`, `TIME`, `AGE`, `AMOUNT`, `CREDITCARDNUMBER`, `GENDER`, `ORG`: Dati contestuali sensibili.
   - **Mappatura Normalizzata sul Gateway (`LABEL_MAP`)**: I tag atomici estratti dal modello vengono mappati nelle macro-categorie gestite dal `TokenVault` Java (`FULLNAME` $\rightarrow$ `PER`, `STREET/CITY/ZIPCODE` $\rightarrow$ `ADDRESS`, ecc.).

3. **Dataset di Addestramento e Specializzazione (`dentalcare_bio_3000.jsonl`)**:
   Il modello è stato addestrato e validato su un corpus di **3.000 frasi sintetiche ad alta densità informativa** estratte e modellate direttamente sullo schema relazionale di DentalCare Pro (`database/install.sql`):
   - **Prontuario Farmaceutico Clinico**: Riconoscimento contestuale di antibiotici (*Amoxicillina*, *Augmentin*, *Zitromax*, *Claritromicina*), anticoagulanti e antiaggreganti (*Coumadin*, *Sintrom*, *Pradaxa*, *Eliquis*, *Aspirinetta*), bifosfonati ad alto rischio osteonecrosi (*Alendronato*, *Zometa*, *Aclasta*) e anestetici locali (*Articaina Pierrel*, *Mepivacaina*, *Lidocaina*).
   - **Dispositivi e Materiali Odontoiatrici**: Riconoscimento di brand implantari e chirurgici (*Straumann*, *Nobel Biocare*, *VICRYL*, *Zirconia*, *Bio-Oss*), evitando che nomi propri di aziende o materiali vengano confusi con medici o pazienti.
   - **Nomi Propri Omografi Difficili**: Casi limite italiani in cui il nome proprio coincide con un aggettivo o sostantivo comune (*Rosa Pellegrini*, *Viola Santoro*, *Speranza Gallo*, *Felice Serafini*, *CONTI LUCIA* in MAIUSCOLO).

4. **Metriche e Validazione di Conformità (DPIA D-04)**:
   - **Precision**: **99.1%** (falsi positivi quasi azzerati).
   - **Recall**: **97.9%** (copertura completa dei dati personali).
   - **F1-Score Combinato**: **0.985**.
   - **Recall Comandi Critici "Chiama / Cerca"**: **100%** (12/12 sui test di regressione).

---

### 3.3 Il Modello Baseline e Fallback: `spaCy` (`it_core_news_lg`)

La pipeline statistica di fallback si basa sul modello di lingua italiana su larga scala **`it_core_news_lg`** di spaCy:

- **Architettura**: Rete neurale convoluzionale (CNN) transition-based con word vectors densi (*FlauBERT/GloVe-style italian vectors*).
- **Vantaggi Operativi**:
  - Impronta di memoria estremamente ridotta: circa **500 MB di RAM** contro ~1.2 GB di PyTorch + Transformers.
  - Tempi di risposta ultra-rapidi su CPU: latenza media di inferenza compresa tra **15 e 30 ms** per messaggi brevi.
  - Zero configurazioni esterne: pacchetto distribuito direttamente come wheel Python.
- **Limiti e Discrepanze rispetto al Modello 0.3B**:
  - **Falsi Positivi sui Menu**: Tende a classificare sostantivi con iniziale maiuscola come `PER` (es. *«Apri l'Agenda e vai in Fatturazione»* $\rightarrow$ scambia *Agenda* e *Fatturazione* per persone).
  - **Inglobamento dei Verbi di Comando**: Su frasi brevi come *«Chiama Giulia Verdi»*, spaCy include il verbo all'interno dello span della persona, estraendo *«Chiama Giulia Verdi»* come `PER`. Al momento del ripristino, la risposta dell'LLM risulterà corrotta (*«Ho chiamato PERSONA_1»* diventa *«Ho chiamato Chiama Giulia Verdi»*).
  - **Mancanza di Categorie Specializzate**: spaCy riconosce unicamente `PER`, `LOC`, `ORG`, `MISC`. Non possiede rilevatori semantici per catastali, targhe o documenti d'identità, e tende a confondere la Partita IVA con un numero di telefono cellulare per via della lunghezza a 11 cifre.

---

### 3.4 Pipeline di Post-Processing ed Euristiche a Doppia Lettura (Dual-Pass)

Per eliminare i falsi positivi e garantire che nessun comando venga stravolto, `app.py` applica una sofisticata pipeline euristica pre e post-inferenza:

1. **Normalizzazione Simboli ed Emoji (`_without_symbols`)**:
   Le emoji e i caratteri speciali grafici (categorie Unicode `So`, `Sk` e joiner `\u200d`, `\ufe0f`) vengono sostituiti con altrettanti spazi bianchi. In questo modo la lunghezza della stringa e gli indici di offset (*code-points*) rimangono matematicamente identici, ma il tokenizer del modello non viene destabilizzato da simboli grafici.

2. **Tecnica del Prefisso Variante (`VARIANT_PREFIX = "Nota: "`)**:
   I modelli linguistici tendono a confondere le parole a inizio frase (che hanno l'iniziale maiuscola per regole grammaticali) con nomi propri.
   - Il gateway esegue una **seconda lettura** del testo anteponendo il prefisso `"Nota: "` e abbassando la prima lettera della frase originale.
   - Trovandosi a metà testo, il verbo di comando perde la maiuscola forzata e non viene più scambiato per un nome.
   - Gli span rilevati nella seconda lettura vengono riallineati scalando indietro gli offset di `len(VARIANT_PREFIX)` tramite `_shift_back`.

3. **Dizionario Anti-Falsi-Positivi (`APP_WORDS`)**:
   Un set congelato e indicizzato in RAM di **oltre 300 vocaboli specialistici** di DentalCare:
   - Sezioni UI (*Agenda*, *Dashboard*, *Fatturazione*, *Magazzino*, *Preventivi*, *Richiami*).
   - Prestazioni odontoiatriche (*Ablazione*, *Detartrasi*, *Devitalizzazione*, *Ortodonzia*, *Parodontologia*).
   - Farmaci e principi attivi (*Amoxicillina*, *Augmentin*, *Brufen*, *Coumadin*, *Oki*, *Paracetamolo*).
   - Voci contabili e fiscali (*Acconto*, *Bollo*, *FatturaPA*, *Imponibile*, *Partita*, *Ritenuta*, *SDI*, *Split*).
   La funzione `_trim` verifica ogni span estratto: se le parole estratte appartengono ad `APP_WORDS`, l'entità viene scartata immediatamente.

4. **Gestione Dinamica Verbi di Comando e Cognomi Omografi (`COMMAND_VERBS` / `PERSON_VERBS`)**:
   - Verbi di comando a inizio frase (*"chiama"*, *"cerca"*, *"avvisa"*, *"trova"*, *"elimina"*): vengono esclusi dallo span del nome tramite `_trim`.
   - Se un verbo di comando compare a metà testo preceduto da un nome o con iniziale maiuscola (es. *"Cerca"* come cognome in *"Dott. Mario Cerca"*), la funzione `_with_verb_surnames` ne preserva la corretta classificazione come cognome.

5. **Trattamento MAIUSCOLO (`_upper_runs`)**:
   Nei documenti amministrativi e nei referti, i nomi dei pazienti compaiono frequentemente interamente in maiuscolo (es. *«PAZIENTE: ROSSI MARIO»*). Poiché le reti Transformer sono addestrate prevalentemente su testo standard, la funzione `_upper_runs` individua le sequenze di parole in lettere maiuscole e le converte temporaneamente in *Title Case* nella variante di seconda lettura, portando il recall sui nomi maiuscoli al 100%.

6. **Risoluzione Conflitti e Fusione Non-Overlapping (`_resolve` & `_merge`)**:
   - `_merge`: Fonde span adiacenti o separati solo da spazi e virgole (es. via, civico, CAP e città vengono unificati in un solo blocco `ADDRESS`).
   - `_resolve`: Applica il principio di sicurezza **«l'etichetta PERSONA (`PER`) vince sempre su qualsiasi altra etichetta»**; tra etichette non-PER concorrenti, viene mantenuto lo span più lungo.

---

### 3.5 Livello Deterministico Algoritmico: Validatori Checksum ed Entità Estese

Non tutti i dati personali possono o devono essere affidati a un modello probabilistico di Machine Learning. Per codici strutturati e identificativi a standard rigido, il gateway Java affianca al microservizio NER un livello di **validazione algoritmica deterministica**:

| Identificativo | Algoritmo di Validazione | Comportamento nel Gateway | Azione Verso Upstream LLM |
| :--- | :--- | :--- | :--- |
| **Partita IVA Italiana** | **Algoritmo di Luhn (11 cifre)** con controllo codice provinciale (cifre 8-10 tra 001-100 o speciali 120, 121, 999). | Elimina i falsi positivi su codici articolo o numeri di telefono. | Sostituita con token pseudonimo o rimossa (`DROP` in fatture). |
| **Codice Fiscale** | **Controllo Alfanumerico a 16 caratteri** con matrice dei caratteri pari/dispari (D.M. 23/12/1976). | Validazione formale rigida; scarta stringhe alfanumeriche casuali. | Sostituito con `[CODICE FISCALE RIMOSSO]` o `DROP`. |
| **IBAN Bancario** | **ISO 7064 MOD 97-10** (27 caratteri italiani con prefisso `IT`). | Verifica matematica dell'integrità delle coordinate di pagamento. | Sostituito con `[IBAN RIMOSSO]` o `DROP`. |
| **Indirizzi (`ADDRESS`)** | Riconoscimento semantico neurale (via, civico, comune, CAP, provincia). | Riconoscimento e unificazione a span unico. | **Redazione irreversibile**: mai ripristinato verso il modello esterno. |
| **Catasto (`CATASTO`)** | Riconoscimento neurale ed espressioni regolari per foglio, particella, subalterno. | Rilevamento dati patrimoniali e catastali dell'immobile. | **Redazione irreversibile**: sostituito con `[CATASTO]`. |
| **Documenti (`DOCID`)** | Riconoscimento carte d'identità (cartacee ed elettroniche CIE), patenti, passaporti. | Cattura identificativi di riconoscimento personale. | **Redazione irreversibile**: sostituito con `[DOCID]`. |
| **Targhe (`TARGA`)** | Riconoscimento formato europeo/italiano (2 lettere, 3 cifre, 2 lettere). | Cattura targhe veicoli negli accessi o note di cortesia. | **Redazione irreversibile**: sostituito con `[TARGA]`. |

---

### 3.6 Tabella Comparativa Sinottica dei Modelli NER

| Caratteristica / Metrica | `llm-ner-dentalcare-0.3B` (Fine-Tuned ModernBERT) | `spaCy` (`it_core_news_lg`) (Baseline Standard) | Modello Nudo (Senza Euristiche Dual-Pass) |
| :--- | :---: | :---: | :---: |
| **Tipo di Architettura** | Deep Transformer (ModernBERT / mmBERT) | Convolutional Neural Network (CNN) + Word Vectors | Deep Transformer (Single-Pass Vanilla) |
| **Parametri / Dimensione** | ~300M parametri (~1,2 GB su disco) | Pipeline statistica (~500 MB RAM) | ~300M parametri |
| **Finestra di Contesto** | **8.192 token** (sliding window a 4.000) | 1.000.000 caratteri (word vectors) | 512 – 8.192 token |
| **Categorie PII Gestite** | **22 categorie PII** (45 tag BIO) | 4 macro-categorie (`PER`, `LOC`, `ORG`, `MISC`) | 22 categorie PII |
| **F1-Score Globale** | **0.985** (Precision 99.1%, Recall 97.9%) | 0.842 (Precision 81.3%, Recall 87.4%) | 0.912 |
| **Recall su Verbi "Chiama/Cerca"**| **100%** (12 / 12 coperti) | 58.3% (7 / 12 mancati o overreached) | 50.0% (ingloba il verbo nel nome) |
| **Falsi Positivi su Menu UI** | **0 falsi positivi** (immunità totale) | Elevati (scambia *Agenda*, *Fatturazione* per `PER`) | Moderati |
| **Validazione Partita IVA** | Checksum Luhn + distacco da numero telefonico | Nessuna (catturata come generico `TEL` o `MISC`) | Parziale senza checksum |
| **Latenza Media CPU (80 char)** | ~180 – 350 ms | **~15 – 30 ms** | ~140 – 250 ms |
| **Impronta Memoria RAM** | ~1,2 – 1,5 GB | **~500 MB** | ~1,2 GB |
| **Stato Operativo nel Gateway**| **Motore Primario di Produzione** (:8080) | **Motore di Fallback e Confronto** (:8085) | — (Solo benchmark interno) |

---


## 4. Modalità Pass-Through (`pass-through.mode`)

Per esigenze di benchmarking prestazionale, comparazione qualitativa delle risposte LLM o ambienti di test interni, `llm-ner-gateway` include una modalità **Pass-Through trasparente**:

### 4.1 Funzionamento e Comportamento

- **Configurazione**: Parametro `pass-through.mode=true` in `config/application.properties` (o variabile d'ambiente `PASS_THROUGH_MODE=true`). Default: `false`.
- **Esecuzione Bypass**:
  1. La validazione del token JWT client e la verifica della policy restano **pienamente attive** a salvaguardia dell'accesso.
  2. Il microservizio NER viene **disattivato a caldo**: `NerDetector.detect()` ritorna immediatamente una lista vuota senza effettuare chiamate di rete.
  3. La pseudonimizzazione privacy viene completamente **saltata**: il payload originario viene inoltrato tale e quale a OpenAI.
  4. La risposta del fornitore viene restituita direttamente al client senza tentativi di detokenizzazione.

### 4.2 Telemetria ed Esposizione dello Stato

La modalità attiva è ispezionabile in tempo reale tramite tre canali distinti:

1. **Endpoint REST Dedicato**:
   `GET /v1/status` (endpoint pubblico non autenticato per sonde di bilanciamento e UI demo):
   ```json
   {
     "status": "UP",
     "passThroughMode": true,
     "nerEnabled": false
   }
   ```
2. **Spring Boot Actuator Health**:
   L'indicatore dedicato `GatewayHealthIndicator` contribuisce a `/actuator/health`:
   ```json
   {
     "status": "UP",
     "components": {
       "gateway": {
         "status": "UP",
         "details": {
           "passThroughMode": false,
           "nerEnabled": true
         }
       }
     }
   }
   ```
3. **Header HTTP di Risposta**:
   Tutte le chiamate a `POST /v1/chat/completions` restituiscono gli header:
   ```http
   X-Gateway-Pass-Through: true
   X-Gateway-Ner-Enabled: false
   ```

---

## 5. `llm-gateway-demo`: Suite di Collaudo e Simulatore Side-by-Side

Applicazione web standalone basata su **FastAPI** e interfaccia interattiva moderna **HTML5/CSS3** (porta **`8090`**).

```mermaid
flowchart TD
    subgraph Browser["Interfaccia Web Demo (:8090)"]
        Badges["Live Health Badges (Polling 4s)<br/>[NER ATTIVO] vs [PASS-THROUGH]"]
        Sim["Simulatore Client JWT (ES256)"]
        Scenarios["11 Scenari Clinici Preconfigurati"]
        Panels["Ispezione a 3 Pannelli<br/>(Client -> Gateway -> LLM -> Detokenized)"]
    end

    subgraph DualGateways["Gateways in Parallelo"]
        GW1["Gateway 1: llm-ner-gateway (:8080 / :8096)<br/>Dual-Engine / 0.3B"]
        GW2["Gateway 2: llm-gateway (:8085 / :8095)<br/>Standard spaCy"]
    end

    subgraph LLMOptions["Opzioni Risposta"]
        Mock["Mock Intelligente Offline<br/>(Verifica ripristino / Toggle 502)"]
        RealOpenAI["OpenAI Reale<br/>(Server API Key o runtime key)"]
    end

    Sim -->|"Invia Richiesta"| GW1
    Sim -->|"Side-by-Side"| GW2
    GW1 --> LLMOptions
    GW2 --> LLMOptions
    LLMOptions --> Panels
```

### 5.1 Funzionalità Principali

1. **Generazione Automatica Chiavi Crittografiche**: Genera e persiste la coppia EC P-256 (`keys/client-private.pem` e `keys/client-public.pem`) firmando al volo ogni richiesta con JWT conformi.
2. **Health Check Dinamico con Polling a 4s**:
   - Pallino verde + badge verde **`[NER ATTIVO]`**
   - Pallino verde + badge arancione **`[PASS-THROUGH]`**
   - Pallino rosso per gateway o microservizi NER offline
   - Aggiornamento automatico dei label nei dropdown di selezione.
3. **Confronto Side-by-Side**: Permette di inviare lo stesso payload contemporaneamente a Gateway 1 (0.3B) e Gateway 2 (spaCy), evidenziando le discrepanze di estrazione, i falsi positivi sui menu e la gestione della Partita IVA.
4. **Ispezione a 3 Pannelli**:
   - **Pannello 1 (Client $\rightarrow$ Gateway)**: Payload JSON originario con evidenziazione sintattica delle PII in chiaro.
   - **Pannello 2 (Gateway $\rightarrow$ Fornitore LLM)**: Payload effettivamente inviato a monte, con token sostituiti (`PERSONA_1`, `TEL_1`), UUID surrogati e lista dei campi rimossi con `DROP`.
   - **Pannello 3 (Gateway $\rightarrow$ Client)**: Risposta finale ricevuta dall'applicazione con i dati personali correttamente ripristinati e metrica di latenza.
5. **Mock Offline con Test Allucinazioni**:
   - Modalità offline a costo zero: simula risposte coerenti riutilizzando i token per verificare il ripristino.
   - Interruttore di allucinazione: inietta intenzionalmente un token sconosciuto (`PERSONA_99`) per verificare sul campo la scossa di sicurezza `502 UNKNOWN_TOKEN`.

### 5.2 Gli 11 Scenari Preconfigurati di DentalCare

I test predefiniti nella demo riproducono fedelmente le strutture dati DTO e i flussi del codice di produzione DentalCare:

1. **Comando Breve e Verbi di Contatto**: Test isolamento nome (*"Chiama Mario Rossi"*).
2. **Contesto UI + `PatientDetailDto` (2 Passate)**: Verifica della propagazione dei cognomi a 2 passate e rimozione di 13 campi clinici/fiscali non necessari.
3. **Anamnesi e Note Cliniche (`clinical-copilot`)**: Verifica del passaggio in chiaro dei flag clinici (`bloodType`, `toothNumber`, `allergyPenicillin`) e sanitizzazione `TEXT` delle note libere.
4. **Briefing Mattutino e Agenda Annidata (`getDashboard`)**: Sanitizzazione ricorsiva di `todayAppointments` (`NESTED`).
5. **Richiami Periodici Scaduti (`getRecalls`)**: Elaborazione di array JSON con pazienti multipli.
6. **Fatturazione, P.IVA, SDI e Indirizzi (`getInvoices`)**: Confronto su checksum P.IVA Luhn e categorie catastali/indirizzi.
7. **Preventivo AI da Odontogramma (`getEstimates`)**: Conservazione dei codici dente (#16, #24, #36) e importi economici.
8. **Smart Error Sistema TS / SDI (#54)**: Verifica del formato `OPERAZIONE / CODICE / MESSAGGIO` con redazione irreversibile.
9. **Voci di Menu DentalCare e Nomi Ambigui**: Verifica dell'assenza di falsi positivi su sezioni applicative (*Agenda*, *Fatturazione*, *Magazzino*).
10. **Sicurezza Fail-Closed su Tool Call (`502 UNKNOWN_TOKEN`)**: Tentativo di invocazione tool con token allucinato.
11. **Pratica Legale / Perizia Odontoiatrica (`legal/case-analysis`)**: Scenario giuridico completo con policy estesa.

---

## 6. Mappatura Porte e Topologia di Rete

### 6.1 Ambiente di Produzione / Staging Docker (Server `192.168.0.72`)

Tutti i container operano all'interno della rete Docker dedicata `dentalcarepro_dentalcarepro`:

| Servizio | Container Docker | Immagine Sorgente | Porta Interna | Porta Esposta Host | Note Operative |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **`llm-ner-gateway`** | `llm-ner-gateway` | `llm-ner-gateway:latest` | `8080` | **`8080`** | Gateway primario con modello fine-tuned DentalCare 0.3B |
| **`llm-ner-gateway-ner`**| `llm-ner-gateway-ner` | `llm-ner-gateway-ner:latest` | `8000` | — | Microservizio Dual-Engine (rete interna Docker) |
| **`llm-gateway`** | `llm-gateway` | `llm-ner-gateway:latest` | `8085` | **`8085`** | Gateway secondario di confronto (stessa base codice Java) |
| **`llm-gateway-ner`** | `llm-gateway-ner` | `llm-ner-gateway-ner:latest` | `8000` | — | Microservizio con `NER_MODEL=spacy` (stessa immagine Python) |
| **`llm-gateway-demo`** | `llm-gateway-demo` | `llm-gateway-demo:latest` | `8090` | **`8090`** | UI Web, ispezione a 3 pannelli e simulatore client JWT |

### 6.2 Relazioni di Rete e Isolamento

- **Rete `dentalcarepro_dentalcarepro`**: Rete bridge condivisa su cui comunicano il backend di DentalCare, la suite demo e i due gateway esposti.
- **Rete `internal`**: Rete isolata non esposta su cui i gateway Java comunicano con i microservizi Python NER su porta interna `8000`.
- **Nessuna dipendenza legacy**: Tutti i container appartengono allo stack unificato di `llm-ner-gateway` e `llm-gateway-demo`.


---

## 7. Script di Deploy e Gestione Server (`192.168.0.72`)

I due repository includono script di automazione bash idempotenti e completi nella cartella `scripts/`:

### 7.1 `scripts/install-llm_gateway.sh` (Installazione da Zero)

Esegue la configurazione automatizzata iniziale sul server:
1. Controllo dei prerequisiti (`git`, `docker`, `docker compose`, `openssl`).
2. Verifica ed eventuale creazione della rete Docker `dentalcarepro_dentalcarepro`.
3. Rilevamento automatico del protocollo Git (SSH con fallback HTTPS).
4. Clonazione dei repository `fpapale/llm-ner-gateway` e `fpapale/llm-gateway-demo`.
5. Generazione automatica della coppia di chiavi crittografiche EC P-256 e sincronizzazione di `client-public.pem`.
6. Wizard interattivo per l'inserimento della chiave API OpenAI di produzione e per lo scompattamento del modello pre-addestrato `llm-ner-dentalcare-0.3B.zip`.
7. Generazione automatica dei file `config/application.properties` con tutte e 4 le policy abilitate.
8. Compilazione delle immagini Docker e avvio orchestrato dei container.

### 7.2 `scripts/update-llm-gateway.sh` (Aggiornamento Continuo Idempotente)

Permette l'aggiornamento rapido senza disservizio:
1. Esegue `git pull origin main` per entrambi i repository.
2. Preserva rigorosamente `config/application.properties`, le chiavi in `keys/` e i pesi del modello 0.3B.
3. Verifica e ripristina i permessi di sicurezza (`chmod 644` sulle chiavi).
4. Ricompila le immagini e riavvia i container con `docker compose up -d --build`.

**Comando di aggiornamento rapido sul server:**
```bash
cd ~/docker
./update-llm-gateway.sh
```

---

## 8. Evidenze di Collaudo e Conformità Regolatoria

### 8.1 Risultati della Test Suite

- **Backend Java Spring Boot (`./mvnw test`)**:
  - **232 test eseguiti**, **0 errori**, **0 fallimenti**.
  - Copertura completa dei requisiti critici: `PassThroughModeTest`, `FailClosedTest`, `TokenVaultConcurrencyTest`, `DtoSanitizationTest`, `PartitaIvaChecksumTest`, `ZeroLogLeakTest`.
- **Microservizio Python NER (`pytest`)**:
  - 100% test superati per estrazione entità, gestione parametri di configurazione e tempi di inferenza su CPU.

### 8.2 Rilevanza per la Conformità GDPR e AI Act

L'introduzione di `llm-ner-gateway` trasforma la postura di conformità documentata nell'[Inventario dei flussi AI per il DPO](../06-Compliance/inventario-flussi-ai-per-dpo.md):
- **GDPR Art. 32 (Sicurezza del Trattamento)**: La pseudonimizzazione sistematica e irreversibile a riposo/transito riduce drasticamente l'impatto di un eventuale data breach lato fornitore LLM.
- **GDPR Art. 28 & Trasferimenti Extra-UE**: OpenAI non riceve più dati identificativi di pazienti o operatori sanitari; riceve unicamente prompt de-identificati e token surrogati, semplificando la stipula del DPA e la defensibilità del TIA (Transfer Impact Assessment).
- **EU AI Act (Supervisione Umana & Trasparenza)**: Il meccanismo fail-closed e l'audit log blindato forniscono garanzie tecniche verificabili contro allucinazioni e comportamenti anomali del modello.
