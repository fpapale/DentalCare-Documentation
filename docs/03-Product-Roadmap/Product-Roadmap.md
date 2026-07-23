# Product Roadmap — DentalCare Pro

**Versione:** 1.1 · **Data:** 22 luglio 2026 · **Orizzonte:** 2026-2029
**Base:** stato dell'arte verificato su codice e database reali, non su documentazione.

---

## 1. Executive Summary

DentalCare Pro è una piattaforma gestionale odontoiatrica multi-tenant con moduli di
intelligenza artificiale. Il prodotto è oggi in **stato dimostrativo**: nessuno studio
lo usa su pazienti reali.

La roadmap è organizzata in **due fasi separate da un confine regolatorio**, non da una
data:

| | Fase 1 — *Release 1.x* | Fase 2 — *Release 2.x* |
|---|---|---|
| **Cosa** | gestionale + AI **amministrativa** | AI **radiologica certificata CE** |
| **AI inclusa** | Copilot, assistente vocale | analisi ortopanoramiche (MDSW) |
| **Regime** | AI Act (non high-risk) + GDPR | AI Act high-risk + **MDR** |
| **Fine prevista** | **gennaio 2027** | **2029** |
| **Vincolo dominante** | disponibilità di un DPO | organismo notificato + evidenza clinica |

**Le tre cose da sapere su questa roadmap:**

1. **La scadenza non è una data, è un evento.** L'AI Act si applica quando un sistema è
   immesso sul mercato o messo in servizio. Finché DentalCare è una demo con dati
   fittizi, gli obblighi non scattano. Scattano tutti insieme **il giorno in cui il primo
   paziente reale entra nel sistema**. La Fase 1 è quindi ordinata verso un **gate di
   go-live**, non verso un calendario normativo.
2. **Il collo di bottiglia non è lo sviluppo.** Il debito tecnico residuo della Fase 1
   vale settimane di lavoro. DPIA, contratti con i fornitori AI e informative dipendono
   da terzi e non sono comprimibili. Il percorso critico passa per l'**ingaggio di un
   DPO**.
3. **La Fase 2 non si apre finché la Fase 1 non vende.** Il percorso MDR costa più
   dell'intero prodotto costruito finora ed è dominato da code d'attesa e studi clinici.
   Aprirlo prima di validare la domanda è il modo più rapido di esaurire il progetto.

---

## 2. Product Vision

Un gestionale odontoiatrico in cui l'informazione clinica è **corretta, attribuibile,
ricostruibile e protetta**, e in cui l'AI riduce il carico operativo senza mai
sostituirsi alla decisione del professionista.

La visione a lungo termine (ecosistema, digital twin, dentistry predittiva) è tracciata
nelle Release 3.x-5.x ed è **fuori dall'orizzonte pianificabile** di questo documento.

---

## 3. Product Philosophy

- **Il nucleo prima dei satelliti.** FSE, portale paziente, AI e automazioni si
  costruiscono *sopra* un nucleo clinico affidabile, non al suo posto.
- **Il dato e il documento.** Dati strutturati per ricerca, alert e interoperabilità;
  documenti leggibili per comunicazione, firma e conservazione. Servono entrambi.
- **L'AI propone, il professionista dispone.** Ogni output algoritmico è conservato come
  proposta distinta dalla decisione clinica, con la sua provenienza.
- **La prova vale quanto la funzione.** Una funzione che non lascia traccia verificabile
  non è completa.

---

## 4. Product Principles

1. Il tenant è un confine di sicurezza, non una colonna di comodo.
2. Il codice fiscale non è una chiave primaria.
3. Una nota clinica finalizzata non si modifica: si integra con un addendum.
4. Nessuna cancellazione fisica ordinaria del dato clinico.
5. La segreteria non vede il contenuto clinico; l'amministratore tecnico nemmeno.
6. L'output AI è sempre distinguibile dall'osservazione umana.
7. Nessuna scrittura AI senza conferma umana esplicita.
8. Nessun dato sanitario esce verso un fornitore senza base giuridica e contratto.

---

## 5. Product Strategy

**Strategia a gate**, non a scadenze:

```text
        [ Demo / dati fittizi ]
                  |
                  |  GATE 1 — go-live clinico
                  |  (tutto il pacchetto Fase 1 verde, vedi Release-1.x §29)
                  v
    [ Release 1.x — studi paganti, AI amministrativa ]
                  |
                  |  GATE 2 — trigger commerciale
                  |  (la domanda per l'AI clinica è dimostrata)
                  v
     [ Release 2.x — percorso MDR, AI radiologica CE ]
```

Nessun gate si attraversa "provvisoriamente". Il Gate 1 in particolare è binario: nel
momento in cui entra il primo paziente reale, o il pacchetto è completo o il prodotto è
non conforme dal primo giorno.

---

## 6. Platform Strategy

| Piano | Stato | Fase |
|---|---|---|
| **Core Platform** — anagrafica, agenda, cartella, fatturazione, magazzino, richiami | ✅ implementato, da completare sul valore probatorio | 1 |
| **AI Platform (amministrativa)** — Copilot e assistente vocale telefonico | ✅ implementato, da mettere a norma | 1 |
| **Chairside Agent “Ehi Giulia”** — canale vocale hands-free del Copilot in poltrona | 📋 pianificato, attivabile dopo pilota | 1 |
| **Clinical Platform** — encounter, consensi, audit, finalizzazione | 🔨 in costruzione | 1 |
| **AI Platform (clinica)** — radiologia | 🔒 congelata fuori dall'uso clinico | 2 |
| **Interoperability Platform** — FHIR, DICOMweb, FSE | ⏸️ rimandata | post-1 |
| **Enterprise / Developer / Marketplace** | ⚪ non definita | — |

---

## 7. Ecosystem Vision

*Da definire.* Richiede input commerciale non ancora disponibile. La direzione tecnica
abilitante (API REST già presenti, modello interno normalizzato e disaccoppiato dagli
standard di scambio) non preclude nessuna delle opzioni.

---

## 8. Customer Journey

*Parzialmente definita.* I percorsi operativi per ruolo (dottoressa, segretaria,
amministratore) sono documentati nel [Manuale Utente](../05-Manuale-Utente/README.md).
Il journey commerciale (acquisizione, onboarding, retention) è da definire.

---

## 9. Product Portfolio

Un solo prodotto, due configurazioni:

- **DentalCare Pro** (Release 1.x): gestionale + AI amministrativa. Modulo radiologico
  disattivato.
- **DentalCare Pro + Imaging Assistant** (Release 2.x): come sopra, più il modulo
  radiologico certificato CE, attivabile per tenant.

La separazione non è commerciale ma **regolatoria**: il modulo clinico deve essere
attivabile, versionabile, autorizzabile e tracciabile in modo indipendente, così che il
perimetro certificato sia dimostrabile con precisione.

---

## 10-15. Core / AI / Clinical / Enterprise / Developer / Marketplace

Vedi §6. Enterprise, Developer e Marketplace non sono definiti e non hanno data.

---

## 16. API Strategy

Oggi: API REST interne protette da JWT, consumate dal frontend Angular e dalle
automazioni. Il modello dati interno è deliberatamente **non modellato su uno standard di
scambio**: gli standard evolvono, il dominio interno deve restare stabile.

Roadmap: adapter FHIR verso l'esterno (post Release 1.x), mai come modello interno.

---

## 17. Product Lifecycle

| Stadio | Criterio d'ingresso |
|---|---|
| Demo | dati fittizi, nessun paziente reale |
| **Pilota clinico** | **Gate 1 completo** (Release-1.x §29) |
| Produzione | pilota validato + formazione + supporto |
| Modulo clinico AI | marcatura CE (Gate 2 + Release 2.x) |

---

## 18. Innovation Framework

*Da definire.* Oggi l'innovazione è guidata dal registro `proposte-modifiche.md` nel repo
applicativo: ogni proposta ha stato Proposta → Confermata → Fatta.

---

## 19. Product Governance

Decisioni che richiedono approvazione esplicita e non possono essere prese in
implementazione:

- attivazione del modulo radiologico su un tenant clinico → **vietata fino al CE**;
- estensione del Copilot a suggerimenti diagnostici/terapeutici → riclassifica il
  prodotto come dispositivo medico;
- uso di dati di produzione per il training → richiede base giuridica e DPIA dedicata;
- introduzione di triage clinico nell'assistente vocale → come sopra;
- go-live con pazienti reali → richiede Gate 1 completo.

Ruoli minimi da nominare: **AI Compliance Owner**, DPO. In Fase 2 si aggiungono
Regulatory Affairs e Clinical Safety Officer.

---

## 20. Prioritization Framework

Priorità per **rischio**, non per attrattiva:

1. cosa impedisce un danno al paziente o un illecito;
2. cosa serve al Gate 1;
3. cosa aumenta il valore per lo studio;
4. cosa apre mercati futuri.

Il modulo radiologico è la funzione più attraente del prodotto ed è ultima in questa
scala: la scala funziona.

---

## 21. Release Strategy

| Release | Contenuto | Data |
|---|---|---|
| **1.x** | Fase 1 — gestionale + AI amministrativa, conforme e vendibile | gennaio 2027 |
| **2.x** | Fase 2 — AI radiologica CE + DICOM | 2029 |
| 3.x-5.x | visione a lungo termine | non pianificate |

---

## 22. Roadmap 2026

| Periodo | Milestone |
|---|---|
| Luglio | **Ingaggio DPO** (percorso critico) · gate no-clinical sul modulo radiologico · disclosure assistente vocale |
| Agosto-Settembre | Audit trail clinico · finalizzazione note + addendum · segregazione ruoli server-side · soft delete |
| Settembre-Ottobre | Encounter · consensi versionati · odontogramma temporale · anamnesi tri-stato |
| Settembre-Novembre | *(binario parallelo #39)* Chairside Agent: conversazione Copilot condivisa → impostazioni voce/lingua → push-to-talk/STT → TTS → hotword locale → doppio gate clinico |
| Ottobre-Novembre | MFA · merge duplicati · integrità documenti · export paziente (art. 15) |
| Settembre-Dicembre | *(binario parallelo, dipende dal DPO)* DPIA · informative · DPA fornitori · contratti studi |
| Dicembre | Pen test · restore test · test cross-tenant · formazione · pilota Chairside su una postazione |

## 23. Roadmap 2027

| Periodo | Milestone |
|---|---|
| **Gennaio** | **GATE 1 — go-live: primo studio pagante** |
| H1 | consolidamento, feedback pilota · conservazione a norma · politica documentale |
| H1-H2 | *(se Gate 2)* decisione MDR, ingaggio Regulatory Affairs, scelta organismo notificato |
| H2 | interoperabilità: DICOMweb · FHIR adapter · terminology service |

## 24. Roadmap 2028

- QMS ISO 13485 operativo · risk file ISO 14971 · lifecycle IEC 62304
- Validazione interna ed esterna multi-centro del modulo radiologico
- Clinical Evaluation Plan / Report
- **2 agosto 2028**: obblighi AI Act high-risk per prodotti Annex I
- Connettore FSE (proof of concept → accreditamento)

## 25. Roadmap 2029-2035

- **2029**: conformity assessment, marcatura CE, Release 2.x
- Oltre: portale paziente, EHDS readiness, federazione multi-sede. Le Release 3.x-5.x
  restano visione.

---

## 26. Technical Milestones

- [ ] Audit trail clinico append-only
- [ ] Note cliniche finalizzabili con hash e addendum
- [ ] Encounter come perno del modello
- [ ] Consensi versionati
- [ ] Odontogramma temporale (storia, non snapshot)
- [ ] MFA
- [ ] Export paziente art. 15
- [ ] Modulo radiologico attivabile/disattivabile per tenant
- [ ] Restore testato
- [ ] DICOMweb · FHIR adapter · FSE *(post Release 1.x)*

## 27. Clinical Milestones

- [ ] Validazione del workflow clinico con odontoiatri reali su casi realistici
- [ ] Pilota clinico con studio reale
- [ ] *(Fase 2)* dataset con base giuridica documentata
- [ ] *(Fase 2)* validazione esterna multi-centro
- [ ] *(Fase 2)* Clinical Evaluation Report

## 28. Commercial Milestones

- [ ] **Primo studio pagante — gennaio 2027**
- [ ] Registro claim approvato (nessun claim medico senza CE)
- [ ] Contratto studio con clausole deployer
- [ ] *(Gate 2)* domanda dimostrata per l'AI clinica

---

## 29. KPI di Prodotto

**Clinico-operativi:** cartelle complete · anamnesi aggiornata · note finalizzate in
giornata · procedure con dente/sito valorizzato · piani con consenso collegato · duplicati
per 1.000 pazienti.

**Sicurezza e privacy:** copertura MFA · access review completate · tentativi cross-tenant
· tempo di revoca account · esito restore test · richieste degli interessati e tempi.

**AI:** tasso di uso del Copilot · tasso di override · azioni confermate vs proposte ·
incidenti.

Nessuno di questi è misurato oggi: la misurazione dipende dall'audit trail (Milestone 1).

---

## 30. Product Vision 2035

*Fuori orizzonte.* Vedi Release 3.x-5.x. La condizione perché quella visione sia
raggiungibile è una sola: che il nucleo clinico costruito nel 2026-2027 sia
**dimostrabile**. Tutto il resto si costruisce sopra.
