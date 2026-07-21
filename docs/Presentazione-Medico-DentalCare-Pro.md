# DentalCare Pro: Presentazione Clinico-Tecnico-Legale per l'Odontoiatria Moderna

**Destinatario:** Direttore Sanitario / Odontoiatra Titolare / Medico Curante  
**Versione Documento:** 1.0  
**Data:** 21 Luglio 2026  
**Oggetto:** Panoramica Integrata delle Funzionalità Attuali (Release 1.x) e della Roadmap Futura (Release 2.x+), con analisi delle componenti Cliniche, Architetturali e di Compliance Normativa (GDPR, EU AI Act, MDR).

---

## Executive Summary

**DentalCare Pro** è la piattaforma gestionale e clinica di nuova generazione progettata per trasformare lo studio odontoiatrico attraverso l'integrazione di Intelligenza Artificiale, sicurezza informatica avanzata e un'architettura cloud scalabile.

A differenza dei software gestionali tradizionali, DentalCare Pro combina tre pilastri inscindibili:
1. **Eccellenza Clinica**: Ottimizzazione del tempo alla poltrona, riduzione degli errori di trascrizione e diagnosi coadiuvata.
2. **Solidità Tecnica**: Infrastruttura Cloud-Native multi-tenant, microservizi ad alte prestazioni, cifratura avanzata e tracciabilità totale dei dati.
3. **Tutela Legale e Compliance**: Piena aderenza al **GDPR (Art. 32)**, conformità all'**EU AI Act** (Human-in-the-loop) e percorso di qualificazione per il **Regolamento Europeo Dispositivi Medici (MDR UE 2017/745)**.

---

## 1. Stato Attuale: Le Funzionalità Operative (Release 1.x)

La Release 1.x mette a disposizione del medico e del personale di studio una suite completa per la gestione clinica e amministrativa, potenziata da assistenti AI non diagnostici.

### 1.1 Anamnesi Digitale Guidata e Odontogramma Dinamico
*   **Clinico**: Registrazione rapida dell'anamnesi sistemica ed odontoiatrica con alert automatici per allergie, patologie pregresse e terapie farmacologiche in corso. Odontogramma grafico interattivo per la mappatura di elementi dentali, restauri, protesi e impianti.
*   **Tecnico**: Interfaccia reattiva in HTML5/React con salvataggio in tempo reale su microservizi RESTful. Struttura dati JSON schema-validated.
*   **Legale**: Consenso informato e anamnesi firmati digitalmente. Valutazione preliminare del rischio del paziente con conservazione delle versioni storiche dell'anamnesi a tutela della responsabilità medica.

### 1.2 Cartella Clinica Elettronica & Audit Trail Probatorio
*   **Clinico**: Diario clinico dettagliato con tracciamento delle visite, delle prestazioni effettuate, dei parametri parodontali e del piano di trattamento.
*   **Tecnico**: Modello dati clinico con registro degli eventi **Append-Only (Audit Trail)**. Ogni modifica, inserimento o cancellazione logica viene firmata e timestampata in modo immutabile.
*   **Legale**: Il sistema garantisce inoppugnabilità e valore probatorio in sede medico-legale (ex art. 2236 c.c. e Legge Gelli-Bianco 24/2017), impedendo la manomissione retroattiva del diario clinico.

### 1.3 Copilot AI Amministrativo e Verbalizzazione (DentalCare Voice & Assistant)
*   **Clinico**: Trascrizione ed estrazione automatica dei dati durante il colloquio con il paziente. Trascrizione di note cliniche senza staccare le mani dalla zona sterile.
*   **Tecnico**: Integrazione con modelli di elaborazione del linguaggio naturale (LLM) su infrastruttura privata e protetta. Isolamento dei dati del tenant e nessuna ri-condivisione dei dati clinici per l'allenamento dei modelli pubblici.
*   **Legale**: Conformità all'**EU AI Act** per i sistemi AI a basso rischio (assistenza amministrativa). Trasparenza dell'output con validazione obbligatoria da parte dell'odontoiatra (*Human-in-the-loop*).

### 1.4 Sicurezza dei Dati Sanitari e Cifratura Avanzata
*   **Clinico**: Massima tranquillità sulla riservatezza dei dati dei propri pazienti.
*   **Tecnico**: Cifratura dei dati a riposo (AES-256) e in transito (TLS 1.3). **Cifratura campo-per-campo** per i dati identificativi sensibili del paziente (Codice Fiscale, Nome, Cognome, Dati Sanitari) in ottemperanza all'Art. 32 del GDPR. Separazione logica del database tra tenant su architettura PostgreSQL multi-tenant.
*   **Legale**: Riduzione al minimo del rischio di Data Breach e sollevamento del titolare dello studio da responsabilità per colpa grave legata a cattiva gestione informatica dei dati (GDPR Accountability).

---

## 2. Roadmap Futura: L'Evoluzione Clinica e AI (Release 2.x e Oltre)

La Release 2.x introduce moduli di Intelligenza Artificiale diagnostica radiologica, integrazione con imaging tridimensionale ed evoluzione dell'assistenza clinica alla poltrona.

```
+-----------------------------------------------------------------------------------+
|                        EVOLUZIONE DENTALCARE PRO                                   |
+-----------------------------------------------------------------------------------+
| RELEASE 1.x (Attuale)          | RELEASE 2.x (In Arrivo)                          |
| - Cartella Clinica & Audit     | - Viewer DICOM / PACS Integrato                   |
| - Odontogramma & Anamnesi      | - AI Radiologica (Carie, Lesioni, Riassorbimenti) |
| - Copilot AI Amministrativo    | - Certificazione MDR (Classe IIa / IIb)           |
| - Cifratura Campo-per-Campo    | - Tracciabilità Strumentale & Sterilizzazione     |
+-----------------------------------------------------------------------------------+
```

### 2.1 Visualizzatore DICOM Integrato & PACS Cloud (Release 2.x)
*   **Clinico**: Archiviazione, visualizzazione e confronto direttamente in piattaforma delle radiografie endorali, ortopantomografie (OPT) e TC Cone Beam (CBCT), senza dipendere da software terzi installati sui singoli PC.
*   **Tecnico**: Integrazione dello standard DICOM web (WADO-RS, QIDO-RS, STOW-RS), rendering grafico ad alte prestazioni su GPU tramite WebGL.
*   **Legale**: Tracciabilità della filiera di acquisizione dell'immagine radiologica e rispetto delle norme sulla conservazione sostitutiva delle immagini diagnostiche.

### 2.2 AI Radiologica Certificata (Medical Device Regulation - MDR)
*   **Clinico**: Modulo di *Computer Vision* per l'identificazione precoce e automatica di lesioni cariose interprossimali, difetti ossei parodontali, riassorbimenti radicolari e lesioni periapicali, con evidenziazione grafica delle regioni di interesse (ROI).
*   **Tecnico**: Algoritmi di Deep Learning addestrati su dataset clinici annotati, con calcolo del livello di confidenza predittiva e supporto all'analisi differenziale.
*   **Legale**: **Qualificazione come Software as a Medical Device (SaMD)** in accordo al **Regolamento UE 2017/745 (MDR)** in Classe IIa/IIb. Il sistema opererà rigorosamente come strumento di *Second Opinion*, mantenendo l'odontoiatra come unico responsabile finale della diagnosi e dell'impostazione del piano di cura.

### 2.3 Agente Vocale Hands-Free da Poltrona (DentalCare Hands-Free)
*   **Clinico**: Possibilità per l'operatore in guanti sterili di dettare misurazioni di sondaggio parodontale, odontogramma e note cliniche a voce tramite microfono direzionale, senza toccare tastiera o mouse.
*   **Tecnico**: Elaborazione vocale in tempo reale (Speech-to-Text adattato alla terminologia odontoiatrica) con riduzione del rumore ambientale della turbina/aspiratore.
*   **Legale**: Miglioramento dei protocolli di igiene e prevenzione delle infezioni incrociate nello studio (rispetto delle Linee Guida di Odontoiatria Preventiva e Sicurezza sul Lavoro).

---

## 3. Matrice Integrata Clinico-Tecnico-Legale

La seguente tabella sintetizza il valore tripartito delle principali funzionalità di DentalCare Pro:

| Feature / Modulo | Prospettiva Clinica | Prospettiva Tecnica | Prospettiva Legale & Compliance |
| :--- | :--- | :--- | :--- |
| **Cartella Clinica & Audit Trail** | Tracciabilità completa della storia del paziente e delle prestazioni. | Registro eventi Append-Only immutabile con marca temporale. | Efficacia probatoria ex art. 2236 c.c. e Legge Gelli-Bianco. |
| **Cifratura Dati Sanitari** | Riservatezza garantita dei dati clinici e anamnestici del paziente. | Cifratura AES-256 campo-per-campo (Art. 32 GDPR). | Protezione da Data Breach e conformità al Garante Privacy. |
| **Copilot AI (Rel. 1.x)** | Velocizzazione burocrazia, sintesi anamnesi e verbalizzazione. | LLM su cloud privato dedicato con isolamento tenant. | Conforme a EU AI Act (Risk Minimization & Human Oversight). |
| **AI Radiologica (Rel. 2.x)** | Rilevamento guidato di carie e patologie parodontali/periapicali. | Reti neurali Computer Vision integrate su DICOM Web. | Certificazione MDR UE 2017/745 (Software Medicale SaMD). |
| **Piani di Cura & Preventivi** | Chiarezza nella comunicazione del piano terapeutico al paziente. | Calcolo dinamico costi/prestazioni e integrazione prontuari. | Trasparenza contrattuale ed evidenza del consenso informato. |

---

## 4. Perché Adottare DentalCare Pro: Vantaggi Strategici per lo Studio

1. **Riduzione del Rischio Medico-Legale**: Ogni atto clinico e consenso è protetto da cifratura e tracciamento immodificabile.
2. **Efficienza Operativa**: Fino al **35% di tempo risparmiato** nelle mansioni burocratiche e di digitazione grazie agli assistenti AI.
3. **Qualità Diagnostica Avanzata**: L'AI radiologica di seconda opinione riduce la percentuale di patologie sub-cliniche non diagnosticate.
4. **Sicurezza Informatica a Prova di Futuro**: Protezione totale contro ransomware e furto dati, sollevando il Medico Titolare da sanzioni GDPR.

---

> **Conclusione**: DentalCare Pro non è un semplice software di gestione, ma una piattaforma clinica integrata progettata per proteggere l'operato del medico, valorizzare la qualità delle cure e garantire la massima compliance legale e tecnologica.
