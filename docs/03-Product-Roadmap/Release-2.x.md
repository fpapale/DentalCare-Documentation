# Release 2.x — AI radiologica certificata (percorso MDR)

**Fase 2** · **Target: 2029** · **Stato: non aperta** · **Versione doc:** 1.0 (17 luglio 2026)

---

## 1. Executive Summary

Release 2.x aggiunge a DentalCare Pro il **modulo di analisi radiologica** come
**dispositivo medico marcato CE**: supporto all'identificazione di reperti su
ortopanoramiche, verificato dall'odontoiatra.

Il modulo **esiste già e funziona** (modelli ONNX per identificazione dentale FDI e
rilevamento patologie, con revisione umana e tracciabilità della versione del modello).
Non è il software a mancare: manca il **percorso regolatorio**.

> **Regola che governa questa Release: non si apre finché la Release 1.x non vende.**
> Il percorso MDR costa più dell'intero prodotto costruito finora, non è comprimibile
> ed è dominato da code d'attesa, studi clinici e organismi notificati. Aprirlo prima di
> aver dimostrato la domanda è il modo più rapido di esaurire il progetto.

Fino ad allora il modulo resta un **asset dimostrativo**: attivo in demo su dati fittizi,
**disattivato in produzione clinica**.

---

## 2. Vision della Release

L'odontoiatra legge la radiografia. Il software gli segnala cosa potrebbe avergli
sfuggito, dichiara quanto è sicuro, e non decide mai al posto suo. Ogni reperto resta
attribuibile: chi l'ha proposto (modello e versione), chi l'ha confermato o rifiutato,
quando.

## 3. Obiettivi Strategici

1. Ottenere la **marcatura CE** del modulo come Medical Device Software.
2. Costruire un **QMS** realmente operativo, non una collezione di documenti.
3. Dimostrare con evidenza clinica che il modulo porta un beneficio e non introduce rischi
   inaccettabili.
4. Allineare la conformità **AI Act high-risk** (Annex I) al percorso MDR.

---

## 4. Scope

- **Qualificazione e classificazione MDR**: intended purpose, qualification memo,
  classification memo (ipotesi iniziale ragionevole: **classe IIa** ai sensi della Rule
  11 — da confermare, non da assumere).
- **QMS** coerente con MDR: controllo documenti, sviluppo software, verifica e
  validazione, gestione rischi, data governance, annotazione, cybersecurity, fornitori,
  reclami, vigilanza, CAPA, audit interni, post-market, change control.
- **Fascicolo tecnico** completo.
- **Risk management** (hazard analysis, controlli, rischio residuo, beneficio/rischio).
- **Data governance**: provenienza, licenze, base giuridica, separazione dei dataset,
  prevenzione del leakage, rappresentatività, dataset card.
- **Validazione**: metriche per patologia e per sottogruppo, per dispositivo, per centro;
  calibrazione; tasso di astensione; performance uomo vs AI vs uomo+AI.
- **Valutazione clinica**: CEP, protocollo, SAP, CER, validazione esterna multi-centro.
- **Supervisione umana**: piano documentato + usability engineering.
- **Logging di inferenza**: hash input, modello, versione pesi, runtime, preprocessing,
  soglie, output, confidenza, qualità input, revisore, conferma/override.
- **Post-market**: PMS, PMCF, vigilanza, gestione incidenti.
- **Conformity assessment** con organismo notificato → **marcatura CE**.
- **Supporto DICOM nativo** (prerequisito pratico: le ortopanoramiche nascono DICOM).

## 5. Out of Scope

- Riaddestramento automatico in produzione: **vietato**. Una modifica del modello può
  essere una modifica sostanziale e richiedere una nuova valutazione di conformità.
- Estensione a patologie o popolazioni non coperte dall'evidenza.
- Uso su modalità di acquisizione non validate.
- Diagnosi autonoma: fuori dall'intended purpose, per costruzione.

## 6. Evoluzione rispetto alla Release 1

Release 1.x prepara il terreno in tre modi:

1. **Separazione del modulo**: il gate no-clinical costruito in Release 1.x è ciò che
   rende dimostrabile quale parte del prodotto è soggetta a MDR. Senza quella
   separazione, l'intero prodotto diventerebbe ambiguo.
2. **Tracciabilità già presente**: versione del modello, revisione dell'odontoiatra,
   distinzione tra output AI e osservazione umana esistono già nel prodotto. Sono
   l'ossatura della supervisione umana richiesta dal MDR e dall'AI Act.
3. **La dipendenza che non si recupera** ⚠️ — la **data governance del dataset deve
   iniziare dentro la Release 1.x**:

> La validazione clinica richiede dati annotati con provenienza, licenza e **base
> giuridica** documentate. Le annotazioni raccolte durante le demo **non sono
> utilizzabili**: non hanno una base giuridica per il training, e la pseudonimizzazione
> non le rende anonime. **Una base giuridica non si retro-adatta a dati già raccolti.**

Quindi, se si intende aprire la Release 2.x, in Release 1.x va predisposto — mentre il
DPO è già ingaggiato — quanto segue: base giuridica per la raccolta a fini di
sviluppo/ricerca separata da quella assistenziale; informativa che la copra; SOP di
annotazione (qualifiche, doppia lettura, adjudication, accordo inter-rater); dataset card
e provenienza; separazione degli ambienti clinico e ricerca.

Costa poco farlo allora. Costa un anno recuperarlo nel 2028.

**Corollario:** se si decide che la Release 2.x non si farà mai, la scelta coerente è
smettere di raccogliere annotazioni e rimuovere il modulo dal prodotto — mantenerlo ha un
costo che non ripaga un asset non vendibile.

---

## 7. Nuovi Moduli

Nessun modulo nuovo: la Release 2.x **certifica** un modulo esistente. Il lavoro è
regolatorio, clinico e di qualità, non di sviluppo.

## 8. AI Radiology

Modelli: identificazione dentale (numerazione FDI) + rilevamento patologie, su
ortopanoramica. Output: riquadri con classe e confidenza, sempre sottoposti a revisione.
Le evidenze confermate possono sincronizzarsi sull'odontogramma restando **marcate come
di origine AI**.

Intended purpose (bozza, da approvare con Regulatory Affairs): supporto
all'identificazione e localizzazione di reperti radiografici predefiniti su
ortopanoramiche digitali, per odontoiatri qualificati; fornisce indicazioni visive e
punteggi di confidenza da verificare; non formula la diagnosi definitiva, non sostituisce
l'interpretazione clinica, non determina il trattamento.

## 9. DICOM Platform

Supporto nativo `.dcm`: parsing, **anonimizzazione in memoria** (il file originale non si
modifica mai), windowing, normalizzazione. PNG/JPEG solo per sviluppo e retrocompatibilità.
Controllo di coerenza tra metadati DICOM e paziente selezionato.

## 10. Annotation Platform

L'interfaccia di revisione esiste. Va portata dentro il QMS: SOP, qualifiche degli
annotatori, tassonomia, doppia lettura, adjudication, misura dell'accordo, blind review,
versione delle linee guida.

## 11. AI Training Platform

Ambiente **separato** dalla produzione clinica. Nessun accesso diretto ai dati
assistenziali. Split per paziente (non per immagine), controllo dei duplicati e delle
immagini derivate, nessun tuning sul test set finale.

## 12. AI Knowledge Platform

*Non definita.* Dipende dalla strategia di riuso secondario dei dati, che richiede base
giuridica propria.

## 13. Voice AI

Invariata rispetto alla Release 1.x: resta **amministrativa**. Introdurre triage clinico
la riclassificherebbe come dispositivo medico.

## 14. Workflow Automation

Invariata. Vincolo permanente: nessuna azione autonoma su dati clinici senza conferma
umana.

## 15. Analytics Platform

KPI di studio su dati aggregati/anonimizzati. Fuori dal perimetro del dispositivo.

## 16. Clinical Platform

Eredita il nucleo di Release 1.x. Il modulo AI vi si innesta **senza** poter scrivere
direttamente il referto: l'output resta proposta finché il professionista non decide.

## 17-19. Enterprise / API Platform / Marketplace

*Non definiti.*

## 20. Security Evolution

Sicurezza ML: firma e hash dei pesi, repository modelli protetto, prevenzione della
sostituzione del modello, controllo del poisoning, provenance degli artefatti,
validazione prima del deploy, monitoraggio del drift, isolamento degli ambienti.

## 21. Compliance Evolution

| Regime | Release 1.x | Release 2.x |
|---|---|---|
| GDPR | ✅ | ✅ + base giuridica dataset |
| AI Act — trasparenza, literacy | ✅ | ✅ |
| **AI Act — high-risk (Annex I)** | non applicabile | ✅ **obbligatorio dal 2 agosto 2028** |
| **MDR** | non applicabile | ✅ **marcatura CE** |

Le due scadenze convergono: se il CE arriva nel 2029, gli obblighi AI Act high-risk
(2 agosto 2028) sono già maturati e vanno soddisfatti insieme.

## 22-25. Scalabilità / Performance / DevOps / AI Infrastructure

Requisiti derivati dal QMS: ambienti segregati (sviluppo, validazione, produzione
clinica, ricerca), release firmate, rollback documentato, tracciabilità completa
dell'inferenza. *Dettagli da definire con il QMS.*

## 26. Product KPIs

Post-market: tasso di uso, tasso di override, errori confermati per patologia e per
dispositivo, immagini rifiutate, drift, incidenti, casi fuori intended purpose.

## 27-28. Piano Commerciale / Marketing

*Da definire.* Vincolo assoluto: **nessun claim medico prima del CE**, e nessun claim più
ampio dell'evidenza dopo. "Beta clinica" non esiste come categoria: una beta usata su
pazienti è uso clinico.

## 29. Clinical Validation

Il pezzo più lungo e più costoso della Release. Deve dimostrare: validità
dell'associazione tra output e condizione clinica, prestazioni tecniche e cliniche,
sicurezza, beneficio, rapporto beneficio/rischio, generalizzabilità e limiti. Richiede
validazione **esterna multi-centro** e, per prove su dati reali, valutazione di comitato
etico, consenso ove richiesto, autorizzazioni e assicurazione.

---

## Timeline (se aperta a inizio 2027)

| Periodo | Attività |
|---|---|
| **2027 H1** | decisione + budget · ingaggio Regulatory Affairs · intended purpose · qualification + classification memo · **scelta organismo notificato** (code di 6-12 mesi: ci si mette in fila presto) |
| **2027 H2 – 2028 H1** | QMS ISO 13485 · risk file ISO 14971 · lifecycle IEC 62304 · usability IEC 62366 · cybersecurity IEC 81001-5-1 · data governance |
| **2028** | validazione interna ed esterna multi-centro · CEP/CER |
| **2 agosto 2028** | obblighi AI Act high-risk (Annex I) |
| **2028 H2 – 2029** | conformity assessment · audit organismo notificato · remediation · **marcatura CE** |

**CE realistica: 2029.** Chi promette il 2028 partendo da zero nel 2027 non ha
considerato le code degli organismi notificati.

---

## 30. Roadmap verso Release 3

Non pianificata. La Release 3.x presuppone un dispositivo certificato, un mercato e un
QMS maturo: nessuna delle tre condizioni è oggi verificata.

## 31. Lessons Learned

*(da compilare a valle)* — la lezione già disponibile oggi: **la qualifica di dispositivo
medico dipende dallo scopo dichiarato, non dal linguaggio tecnico interno.** Un software
che cerca reperti in immagini mediche a supporto di un'ipotesi diagnostica è MDSW, e
nessuna etichetta — beta, prototipo, "solo supporto", "non sostituisce il medico" —
cambia questo fatto.

---

## Riferimenti

- [Product Roadmap](Product-Roadmap.md) · [Release 1.x](Release-1.x.md) · [AI Roadmap](AI-Roadmap.md)
- [04-AI](../04-Architecture-Handbook/04-AI.md) · [05-DICOM](../04-Architecture-Handbook/05-DICOM.md)
- Regolamento (UE) 2017/745 (MDR) · Regolamento (UE) 2024/1689 (AI Act) · MDCG 2019-11 ·
  MDCG 2020-1 · MDCG 2025-6
