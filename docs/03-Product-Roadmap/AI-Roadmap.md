# AI Roadmap — DentalCare Pro

**Versione:** 1.0 · **Data:** 17 luglio 2026
**Principio guida:** l'AI di DentalCare si divide in due mondi separati da un confine
regolatorio — **amministrativa** (oggi) e **clinica** (dopo il CE). Confonderli
riclassifica l'intero prodotto.

---

## 1. Executive Summary

DentalCare ha tre sistemi AI in essere:

| Sistema | Cosa fa | Classificazione | Stato |
|---|---|---|---|
| **Copilot** | assistente conversazionale sui moduli (agenda, pazienti, preventivi…) | AI **non high-risk** | ✅ in Release 1.x |
| **Assistente vocale** | prenotazioni e informazioni amministrative | AI con obblighi di **trasparenza** (art. 50) | ✅ in Release 1.x |
| **Analisi radiologica** | reperti su ortopanoramica | probabile **MDSW** + AI Act **high-risk** | 🔒 congelato → Release 2.x |

La roadmap AI è quindi semplice da enunciare e difficile da rispettare: **portare a norma
i primi due, tenere il terzo fuori dall'uso clinico finché non è certificato.**

## 2. Visione AI

L'AI toglie lavoro ripetitivo alla segreteria e attenzione sprecata al medico. Non
diagnostica al posto suo, non decide, non scrive nulla senza che qualcuno abbia detto sì.

## 3. AI Philosophy

1. **L'output AI è una proposta**, conservata come oggetto distinto dalla decisione clinica.
2. **Conferma umana per ogni scrittura.** Non come istruzione nel prompt: come vincolo del
   codice.
3. **La provenienza è parte del dato.** Chi ha proposto (modello e versione), chi ha
   confermato, quando.
4. **Il feedback non è ground truth.** La correzione di un odontoiatra è un segnale, non
   un'etichetta di addestramento.
5. **Nessun dato sanitario esce senza contratto.**

## 4. AI Platform

- **Copilot**: LLM con function calling; una superficie tool unica che espone i moduli.
- **Assistente vocale**: fornitore esterno per voce e trascrizione + orchestrazione dei
  workflow.
- **Visione radiologica**: servizio separato con modelli ONNX (identificazione dentale
  FDI + rilevamento patologie), invocato dal backend, mai esposto direttamente.

## 5. AI Architecture

Vedi [04-AI](../04-Architecture-Handbook/04-AI.md). Proprietà rilevanti:
i servizi AI sono **disaccoppiati dal core transazionale**; il modello di visione non è
raggiungibile dall'esterno; il Copilot non accede mai direttamente al database ma solo ai
servizi applicativi, con i controlli di autorizzazione che essi già applicano.

## 6. AI Domains

Amministrativo (agenda, anagrafica, preventivi, fatture, richiami, magazzino) ·
conversazionale (chat e voce) · visione (radiologia, **congelato**).

## 7. AI Copilot

**Classificazione:** AI non high-risk, purché **non produca valutazioni cliniche**.

**Proprietà architetturale chiave** (verificata sul codice): il Copilot **non esegue
scritture dirette**. Ogni azione di scrittura registra una closure server-side e restituisce
un'anteprima con un codice di conferma; solo la conferma esplicita esegue. Il modello
trasporta il codice, non il contenuto: **l'azione confermata è identica per costruzione a
quella mostrata in anteprima**, e l'LLM non può alterarla tra un turno e l'altro. Il
tentativo di confermare un'azione di un altro utente viene rifiutato e registrato.

**Confine da non superare:** i tool che leggono dati clinici (anamnesi, odontogramma,
diagnosi, prescrizioni, cartella) sono ammessi. Un tool che **suggerisca** diagnosi,
terapia o priorità clinica renderebbe il Copilot un probabile dispositivo medico. È una
decisione di governance, non di prodotto.

**Roadmap:** logging esteso (paziente, esito, correlation ID) · test di prompt injection ·
allowlist dei tool · kill switch.

## 8. AI Voice

**Classificazione:** AI soggetta a trasparenza (art. 50).

**Obblighi** (Release 1.x): dichiarare di essere un'AI **prima** di raccogliere
informazioni, in modo comprensibile e non nascosto nelle condizioni · offrire sempre il
passaggio a un operatore umano · informativa sulla registrazione distinta da quella
sull'AI.

**Limiti operativi:** nessuna diagnosi, nessuna valutazione di urgenza, nessuna
prescrizione, nessuna interpretazione di referti. Escalation deterministica verso una
persona per ogni richiesta clinica. Un agente di prenotazione non deve trasformarsi
informalmente in triage.

## 9. AI Radiology

**Classificazione:** probabile Medical Device Software (ipotesi iniziale classe IIa,
Rule 11) e, di conseguenza, sistema AI **high-risk** ai sensi dell'art. 6(1).

**Stato: congelato.** Attivo in demo su dati fittizi, **disattivato in produzione
clinica**. Senza marcatura CE non può essere usato su pazienti reali né presentato con
finalità mediche — e nessuna etichetta ("beta", "prototipo", "solo supporto") cambia
questo.

**Cosa c'è già di buono:** versione dei modelli registrata per ogni analisi · revisione
esplicita dell'odontoiatra (accetta / modifica / rifiuta) persistita · output AI
distinguibile dall'osservazione manuale, con collegamento all'analisi che l'ha prodotto.
Sono le fondamenta della supervisione umana richiesta dal MDR: vanno documentate, non
riscritte.

**Percorso:** [Release 2.x](Release-2.x.md) → CE 2029.

## 10. AI Knowledge

*Non definita.* Presuppone una base giuridica per il riuso secondario dei dati.

## 11. AI Workflow

Automazioni amministrative. Vincolo permanente: nessuna azione autonoma su dati clinici;
nessuna cancellazione o modifica massiva senza conferma.

## 12. Multi-Agent System

*Non definito.* Ogni estensione in questa direzione aumenta la superficie di azione
autonoma: richiederebbe autorizzazioni per tool e conferme più stringenti, non meno.

## 13. Model Strategy

Modelli di visione **proprietari** (ONNX, on-premise: le immagini non lasciano il
server). LLM di terze parti per il conversazionale, con vincolo contrattuale di
**no-training** sui dati DentalCare.

Nota di responsabilità: usare un modello open source o l'API di un terzo **non** trasferisce
la responsabilità al fornitore. Chi commercializza il sistema con il proprio marchio è il
provider.

## 14. Data Strategy

- **Dati assistenziali**: trattati per la cura. Non riutilizzabili per il training senza
  base giuridica propria.
- **Dati per lo sviluppo**: richiedono base giuridica separata, informativa, minimizzazione,
  pseudonimizzazione e DPIA dedicata.
- **La pseudonimizzazione non produce dati anonimi.**

⚠️ **Dipendenza critica**: se si intende aprire la Release 2.x, la data strategy va
costruita **in Release 1.x**. Una base giuridica non si retro-adatta a dati già raccolti.

## 15. MLOps

Oggi: modelli versionati e distribuiti come artefatti; nessun training in produzione.
Roadmap (Release 2.x): dataset registry · model registry · artefatti firmati ·
approvazione di release · deployment controllato · rollback · monitoraggio del drift.

## 16. Model Registry

*Da costruire in Release 2.x.* Requisito: da ogni risultato si deve poter ricostruire
esattamente quale modello, quale codice, quale configurazione, quale dataset di
validazione e quale approvazione l'hanno prodotto.

## 17. Dataset Strategy

Separazione rigorosa: training · validation · test interno · test esterno · test per sito
· challenge set · post-market set. Prevenzione del leakage: **split per paziente**, non
per immagine; controllo di duplicati e immagini derivate; nessun tuning sul test set
finale. Rappresentatività da analizzare (età, qualità radiografica, dispositivo, centro,
restauri/impianti, edentulia, distribuzione delle classi).

## 18. Annotation Platform

Esiste l'interfaccia; manca la **SOP**: qualifiche degli annotatori, tassonomia, doppia
lettura, adjudication, accordo inter-rater, blind review, versione delle linee guida.
Prerequisito della validazione clinica.

## 19. Continual Learning

**Vietato in produzione.** Il modello di produzione è congelato. Le correzioni degli
odontoiatri sono feedback: passano per review, adjudication e data governance prima di
diventare dati di addestramento. Un aggiornamento del modello può costituire una modifica
sostanziale e richiedere una nuova valutazione di conformità.

## 20. Federated Learning

*Non definito.*

## 21. Explainable AI

Oggi: localizzazione dei reperti e punteggio di confidenza. Requisiti da introdurre in
Release 2.x: soglie validate, **astensione** sotto soglia, indicatore di qualità
dell'immagine, dichiarazione dei limiti, nessuna evidenziazione eccessivamente persuasiva
(prevenzione dell'automation bias).

## 22. AI Governance

Registro AI · AI Use Policy · AI Compliance Owner · classificazione per modulo ·
registro claim · change control su modelli e prompt · incident intake. **Tutto in
Release 1.x.**

## 23. AI Security

Prompt injection testing · allowlist dei tool · conferma umana per le azioni sensibili
(già presente) · nessun accesso diretto al database · validazione dell'output · redazione
dei dati · protezione dei system prompt · audit delle tool call · kill switch · test di
esfiltrazione. Per i modelli: firma e hash dei pesi, prevenzione della sostituzione,
controllo del poisoning.

## 24. AI Ethics

Nessuna profilazione discriminatoria né accesso differenziato alle cure. Attenzione
all'automation bias: un medico che si fida troppo è un rischio clinico introdotto dal
software. Il paziente ha diritto di sapere che l'AI è stata usata (L. 132/2025) e la
decisione resta al professionista.

## 25. AI Compliance

| | Copilot | Voce | Radiologia |
|---|---|---|---|
| AI Act art. 4 (literacy) | ✅ dovuta | ✅ dovuta | ✅ dovuta |
| AI Act art. 50 (trasparenza) | ✅ | ✅ **centrale** | ✅ |
| AI Act high-risk | ❌ se resta amministrativo | ❌ | ✅ (dal 2 ago 2028) |
| MDR | ❌ se non suggerisce clinica | ❌ | ✅ **CE necessaria** |
| GDPR + DPIA | ✅ | ✅ | ✅ |

## 26. AI Infrastructure

Visione on-premise (le immagini non escono). LLM conversazionale esterno → richiede DPA,
valutazione del trasferimento, no-training. Ambienti separati per clinica, sviluppo e
ricerca.

## 27. AI KPIs

Tasso di uso · **tasso di override** (indicatore di fiducia e di qualità) · azioni
confermate vs proposte · incidenti · *(Release 2.x)* errori per patologia e per
dispositivo, immagini rifiutate, drift, casi fuori intended purpose.

## 28-29. AI Research / Partnership

*Non definiti.*

---

## 30. AI Roadmap 2026

- **Gate no-clinical** sul modulo radiologico (default OFF in produzione) ← *prima cosa*
- Disclosure e limiti dell'assistente vocale
- Registro AI · AI Use Policy · AI literacy
- Informativa al paziente sull'uso dell'AI
- Kill switch per modulo · logging AI esteso
- DPA con i fornitori AI · avvio DPIA
- *(se Release 2.x)* impostazione della data governance del dataset

## 31. AI Roadmap 2027

- Gennaio: **go-live** con AI amministrativa a norma
- Monitoraggio override e incidenti in campo
- *(se Gate 2)* intended purpose · qualification/classification memo · Regulatory Affairs
  · organismo notificato

## 32. AI Roadmap 2028

- QMS · risk file · validazione interna ed esterna · CEP/CER
- **2 agosto 2028**: obblighi AI Act high-risk (Annex I)
- DICOM nativo

## 33. Vision 2035

*Fuori orizzonte.* La condizione perché sia raggiungibile: che ogni output prodotto oggi
resti ricostruibile domani — quale modello, quale versione, chi ha deciso. Senza quella
catena, nessuna delle visioni successive è difendibile.

---

## Riferimenti

- [Product Roadmap](Product-Roadmap.md) · [Release 1.x](Release-1.x.md) · [Release 2.x](Release-2.x.md)
- [04-AI](../04-Architecture-Handbook/04-AI.md) · [07-Security](../04-Architecture-Handbook/07-Security.md)
- Regolamento (UE) 2024/1689 (AI Act) · Regolamento (UE) 2017/745 (MDR) · L. 132/2025
