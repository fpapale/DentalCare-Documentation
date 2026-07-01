# 06 - Analisi dei Rischi
## DentalCare Pro

**Versione:** 1.0  
**Data:** Luglio 2026

---

# 1. Scopo del documento

Questo documento identifica, valuta e classifica i principali rischi associati allo sviluppo, alla commercializzazione e alla crescita di DentalCare Pro.

L'obiettivo è definire una strategia di **Risk Management** che permetta di ridurre la probabilità di eventi negativi e limitarne l'impatto sul progetto.

---

# 2. Metodologia

I rischi sono classificati secondo:

- Strategici
- Commerciali
- Tecnologici
- Operativi
- Finanziari
- Normativi
- Cybersecurity
- AI e Clinical
- Reputazionali

Per ogni rischio vengono riportati:

- Descrizione
- Probabilità
- Impatto
- Livello di rischio
- Azioni preventive
- Piano di mitigazione

---

# 3. Registro dei rischi

| ID | Categoria | Rischio | Probabilità | Impatto | Livello |
|----|-----------|----------|-------------|----------|----------|
| R1 | Commerciale | Adozione iniziale lenta | Media | Alto | Alto |
| R2 | Strategico | Reazione dei competitor | Alta | Medio | Alto |
| R3 | Tecnologico | Ritardi nello sviluppo AI | Media | Alto | Alto |
| R4 | Normativo | Evoluzione AI Act / MDR | Media | Alto | Alto |
| R5 | Cyber | Violazione dati sanitari | Bassa | Molto Alto | Critico |
| R6 | Finanziario | Insufficiente liquidità | Media | Alto | Alto |
| R7 | Operativo | Dipendenza dal fondatore | Alta | Alto | Critico |
| R8 | Clinico | Prestazioni AI insufficienti | Media | Alto | Alto |
| R9 | Cloud | Indisponibilità infrastruttura | Bassa | Medio | Medio |
| R10 | Reputazionale | Feedback negativi primi clienti | Media | Alto | Alto |

---

# 4. Analisi per categoria

## 4.1 Rischi Strategici

### Dipendenza dalla differenziazione AI

Il vantaggio competitivo deriva dall'AI. Se il mercato convergesse rapidamente verso funzionalità analoghe offerte dai competitor, il differenziale potrebbe ridursi.

**Mitigazione**
- Innovazione continua
- Partnership scientifiche
- Roadmap accelerata
- Protezione del know-how

---

## 4.2 Rischi Commerciali

### Adozione lenta

Gli studi dentistici tendono a cambiare gestionale con cautela.

**Mitigazione**
- Studi pilota
- Trial gratuiti
- Migrazione assistita
- Case study e testimonial

---

## 4.3 Rischi Tecnologici

### Complessità della piattaforma AI

L'integrazione di LLM, DICOM, ONNX Runtime e servizi cloud aumenta la complessità architetturale.

**Mitigazione**
- Architettura modulare
- Test automatici
- CI/CD
- Versionamento dei modelli

---

## 4.4 Rischi Normativi

### AI Act

L'evoluzione della normativa europea sull'Intelligenza Artificiale può richiedere modifiche organizzative e tecniche.

### GDPR

Gestione di dati sanitari particolarmente sensibili.

### MDR

Il modulo AI Radiology dovrà essere valutato rispetto al quadro regolatorio dei dispositivi medici software.

**Mitigazione**
- Privacy by Design
- Security by Design
- Audit periodici
- Consulenza legale specialistica

---

## 4.5 Cybersecurity

Possibili eventi:

- ransomware
- data breach
- furto credenziali
- attacchi API
- supply chain attack

Contromisure:

- MFA
- cifratura dati
- logging centralizzato
- backup
- disaster recovery
- penetration test
- vulnerability assessment

---

## 4.6 Rischi AI

### Hallucination

Gli LLM possono generare informazioni non corrette.

### Bias

Dataset non rappresentativi possono produrre risultati distorti.

### Explainability

Ogni suggerimento AI dovrà essere interpretabile dal professionista.

**Mitigazione**
- Human-in-the-loop
- Validazione clinica
- Dataset annotati
- Monitoraggio continuo delle performance

---

## 4.7 Rischi Clinici

L'AI non deve sostituire il giudizio clinico.

Principi:

- supporto decisionale
- supervisione umana
- tracciabilità
- auditabilità

---

## 4.8 Rischi Operativi

- crescita troppo rapida
- supporto insufficiente
- documentazione incompleta
- onboarding lento

Mitigazioni:

- Knowledge Base
- Academy
- Customer Success
- Automazione supporto

---

## 4.9 Rischi Finanziari

- ricavi inferiori alle attese
- aumento costi cloud/GPU
- ritardo raccolta capitali

Mitigazione:

- sviluppo incrementale
- controllo cash flow
- pricing modulare
- ricavi ricorrenti SaaS

---

# 5. Matrice Probabilità / Impatto

| Impatto \ Probabilità | Bassa | Media | Alta |
|-------------------------|-------|-------|------|
| Alto | R5 | R3 R4 R6 R8 R10 | R2 R7 |
| Medio | R9 | R1 | - |

I rischi prioritari sono R5 (cybersecurity), R7 (dipendenza dal fondatore), R3/R4 (AI e compliance).

---

# 6. Piano di mitigazione

## Breve termine (0-12 mesi)

- Costruzione Clinical Advisory Board
- Penetration Test
- Backup e Disaster Recovery
- Studi pilota
- Rafforzamento documentazione

## Medio termine (12-24 mesi)

- Certificazioni di sicurezza
- Governance tecnica
- Team Customer Success
- Partnership universitarie

## Lungo termine (24-36 mesi)

- Compliance avanzata
- Espansione europea
- Riduzione rischio operativo attraverso team strutturato

---

# 7. Governance del rischio

Si propone un processo continuo composto da:

1. Identificazione
2. Valutazione
3. Mitigazione
4. Monitoraggio
5. Riesame trimestrale

Ogni rischio dovrà avere un responsabile, indicatori di controllo e stato di avanzamento.

---

# 8. Conclusioni

DentalCare Pro presenta rischi tipici di una startup HealthTech ad alta innovazione, ma dispone anche di importanti leve di mitigazione: architettura moderna, roadmap modulare, validazione clinica, attenzione alla cybersecurity e modello SaaS scalabile.

La gestione proattiva del rischio dovrà essere considerata parte integrante della governance del progetto, accompagnando ogni fase dello sviluppo e della crescita commerciale.
