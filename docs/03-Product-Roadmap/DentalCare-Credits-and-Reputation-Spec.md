# Specifiche Tecniche e di Prodotto: DentalCare Credits & Clinical Reputation Network

**Codice Feature:** FEAT-ROADMAP-3X-COMMONS  
**Modulo:** DentalCare AI Lab & Community Gamification  
**Target Release:** Release 3.x / 4.x  
**Stato:** Specifica per il Team di Progettazione & Architettura  
**Data:** 21 Luglio 2026  

---

## 1. Executive Summary & Vision

Il sistema **DentalCare Credits & Clinical Reputation Network** è un modulo di *Crowdsourced Clinical AI Training & Gamification* progettato per creare un circolo virtuoso di dati (*Data Flywheel*).

L'obiettivo è incentivare gli odontoiatri e i radiologi a partecipare alla de-identificazione, annotazione e validazione coordinata di immagini radiologiche (endorali, OPT, CBCT) e casi clinici. In cambio del loro contributo, i medici accumulano **DentalCare Credits** (utilizzabili per sconti sul canone SaaS del software) e **Punti Reputazione Scientifica** nel network collaborativo della community.

```
+-------------------+      Annotazione /      +-----------------------+
|  Odontoiatra /    | ──────────────────────> | Client-Side DICOM     |
|  Studio Medico    |                         | Anonymizer            |
+-------------------+                         +-----------------------+
          ▲                                               │
          │ Accumulo Crediti                              ▼
          │ & Sconti SaaS                     +-----------------------+
          └────────────────────────────────── | DentalCare AI Lab &   |
                                              | Multi-Peer Consensus  |
                                              +-----------------------+
```

---

## 2. Requisiti di Prodotto e Gamification

### 2.1 Sistema di Incentivazione ("DentalCare Credits")
I crediti non hanno un valore di conversione diretto in valuta monetaria (per evitare restrizioni sulla compravendita di dati sanitari), ma operano come token interni di utilità:

*   **Sconto Canone SaaS**: 100 Credits = 10€ di sconto sulla fattura mensile del software DentalCare Pro (con tetto massimo di sconto impostato al 50% del valore del canone mensile dello studio).
*   **Servizi AI Premium Gratuiti**: Utilizzo dei crediti per sbloccare funzionalità avanzate di rendering 3D CBCT o analisi AI su volumetrie complesse.
*   **Crediti Formativi ECM / FAD**: Conversione dell'attività di validazione e revisione clinica in ore di formazione riconosciute per l'assolvimento dell'obbligo ECM (in partnership con provider FAD).

### 2.2 Reputazione Clinica e Ranking ("Peer Reputation Score")
Ogni medico iscritto all'AI Lab possiede un livello di reputazione clinica (*Reputation Tier*), calcolato in base all'accuratezza delle sue annotazioni rispetto al consenso del network (*Gold Standard Agreement*):

| Tier Reputazione | Requisiti Consensus | Privilegi & Feature Sbloccate |
| :--- | :--- | :--- |
| **Contributor** | < 50 annotazioni validate | Accesso ai task base (rilevamento carie semplici). |
| **Expert Annotator** | 50-200 annotazioni, Accordo > 85% | Accesso a task complessi (riassorbimenti, parodonto), badge sul profilo. |
| **KOL / Senior Validator** | > 200 annotazioni, Accordo > 95% | Diritto di voto finale nei casi controversi (*Super-Validator*), invito a co-autore nei Whitepaper scientifici. |

---

## 3. Architettura Funzionale del Modulo

Il sistema si compone di quattro microservizi principali:

### 3.1 Client-Side DICOM Anonymizer Engine
*   **Posizione**: Eseguito localmente nel browser/client prima di inviare qualsiasi asset al cloud.
*   **Funzionalità**:
    *   Strip completo delle intestazioni e dei metadati DICOM personali (Nome, Cognome, Codice Fiscale, ID Paziente, Nome Studio, Operatore).
    *   Defacing automatico o sfocatura delle strutture ossee estrinseche ed esterne per impedire la ricostruzione facciale 3D (ex Art. 89 GDPR).
    *   Assegnazione di un UUID di hash anonimo e non reversibile (`AnonymousCaseID`).

### 3.2 Peer Consensus Validation Engine (Multi-Reviewer)
L'AI Lab non eroga crediti all'atto della semplice annotazione, ma **solo dopo la conferma da parte del network** per evitare spam o dati inaccurati:

*   **Regola del 3-Peer Consensus**: Una radiografia viene inviata a 3 medici distinti in cieco (*blind review*).
*   **Calcolo dell'Accordo (Fleiss' Kappa)**: 
    *   Se l'accordo tra i 3 medici supera la soglia $K \ge 0.80$, la bounding box / segmentazione viene promossa a **"Gold Standard Label"**.
    *   Tutti e 3 i medici ricevono l'intero ammontare di **DentalCare Credits**.
    *   Se uno dei medici differisce radicalmente dagli altri due, il caso viene scalato a un *Senior Validator (KOL)*.

### 3.3 Anonymized Clinical Cases Feed & Peer-Consultation
*   **Feed Collaborativo**: Sezione "Community" in cui i medici possono condividere anonimamente casi radiologici complessi per richiedere un parere (*Second Opinion*) alla community.
*   **Challenge Diagnostica Mensile**: "Caso del Mese" in cui la community viene sfidata a diagnosticare una patologia rara. I primi classificati ricevono un pacchetto di crediti bonus.

---

## 4. Bozza del Modello Dati (Database Schema Spec)

```sql
-- Tabella Reputazione e Saldo Crediti Utente
CREATE TABLE ai_commons.user_reputation (
    user_id UUID PRIMARY KEY,
    reputation_score INT DEFAULT 100,
    reputation_tier VARCHAR(30) DEFAULT 'CONTRIBUTOR', -- CONTRIBUTOR, EXPERT, KOL
    credits_balance INT DEFAULT 0,
    total_annotations_submitted INT DEFAULT 0,
    total_annotations_accepted INT DEFAULT 0,
    fleiss_kappa_avg DECIMAL(3,2) DEFAULT 0.00,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tabella Task di Annotazione
CREATE TABLE ai_commons.annotation_tasks (
    task_id UUID PRIMARY KEY,
    anonymous_case_id UUID NOT NULL,
    image_url VARCHAR(512) NOT NULL,
    task_type VARCHAR(50) NOT NULL, -- CARIES_DETECTION, PERIODONTAL_BONE_LOSS, PERIAPICAL_LESION
    status VARCHAR(30) DEFAULT 'PENDING', -- PENDING, CONSENSUS_REACHED, DISPUTED
    required_reviews INT DEFAULT 3,
    consensus_result_json JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tabella Sottomissioni Annotazioni dei Medici
CREATE TABLE ai_commons.annotation_submissions (
    submission_id UUID PRIMARY KEY,
    task_id UUID REFERENCES ai_commons.annotation_tasks(task_id),
    user_id UUID NOT NULL,
    annotation_data_json JSONB NOT NULL, -- Bounding boxes, polygon segmentation
    time_spent_seconds INT NOT NULL,
    status VARCHAR(30) DEFAULT 'SUBMITTED', -- SUBMITTED, ACCEPTED, REJECTED
    credits_awarded INT DEFAULT 0,
    submitted_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tabella Registro Transazioni Crediti (Billing Audit)
CREATE TABLE ai_commons.credit_transactions (
    transaction_id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    tenant_id UUID NOT NULL,
    amount INT NOT NULL, -- Positivo per guadagno, negativo per riscatto sconto
    transaction_type VARCHAR(50) NOT NULL, -- ANNOTATION_REWARD, SAAS_DISCOUNT_APPLIED, ECM_REDEEM
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

---

## 5. Matrice di Compliance & Rischi Normativi

| Ambito Normativo | Requisito / Rischio | Soluzione Tecnico-Legale Implementata |
| :--- | :--- | :--- |
| **GDPR Art. 9 & 89** | Trattamento dati sanitari per ricerca. | Anonimizzazione irreversibile client-side prima dell'invio; isolamento totale dal database di produzione. |
| **Consenso del Paziente** | Mancanza di consenso per uso dati AI. | Modulo opt-in facoltativo integrato nell'anamnesi/consenso informato firmato dal paziente. |
| **Regolamento MDR UE 2017/745** | Rischio di alterazione incontrollata del modello medicale. | I dati raccolti alimentano un dataset *offline*. Nessun riaddestramento automatico *in-live*. Il modello rilasciato in produzione segue il normale iter di marcatura CE. |
| **AI Act (Art. 10 & 14)** | Qualità dei dati di addestramento e riduzione dei bias. | Validazione a triplo cieco (*3-Peer Consensus*) per evitare che errori di singoli medici inquinino il ground truth. |
| **Normativa Fiscale / Merci** | Rischio di classificazione come reddito da lavoro dipendente/autonomo. | I crediti non sono convertibili in denaro contante (*non-cashable*), ma esclusivamente in voucher/sconti d'uso sulla piattaforma SaaS. |

---

## 6. Roadmap di Sviluppo & Dipendenze

```
[ Release 1.x / 2.x ] ──► [ Release 3.x ] ──────────────────► [ Release 4.x ]
- Core Cartella Clinica   - Modulo Client Anonymizer          - Full Peer Consensus Engine
- Viewer DICOM Base       - Dashboard "DentalCare AI Lab"    - Integrazione Billing (Sconti SaaS)
                          - Task di Annotazione Manuale       - Sistema Crediti ECM & Challenge
```

### Milestone 1 (Release 3.0): Alpha AI Lab
- Rilascio del motore di anonimizzazione DICOM locale.
- Dashboard riservata al medico per la sottomissione volontaria di casi clinici.

### Milestone 2 (Release 3.5): Engine dei Crediti e Consensus
- Implementazione del sistema di calcolo consensus a 3 revisori.
- Integrazione con il sistema di Billing per l'applicazione automatica dello sconto in fattura.

### Milestone 3 (Release 4.0): Community & Formazione FAD
- Rilascio del Feed Collaborativo Social e delle Challenge di diagnosi mensili.
- Partnership per il rilascio dei crediti ECM.
