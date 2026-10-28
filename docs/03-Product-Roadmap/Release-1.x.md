# Release 1.x — Gestionale odontoiatrico con AI amministrativa

**Fase 1** · **Target: gennaio 2027** · **Versione doc:** 1.2 (28 ottobre 2026, allineata alle proposte fino a #117)

---

## 1. Executive Summary

Release 1.x porta DentalCare Pro dallo stato **demo** al primo **studio pagante con
pazienti reali**. Il prodotto include il gestionale completo e l'AI **amministrativa**
(Copilot conversazionale in modalità amministrativa e Giulia, la segreteria telefonica). Il **Copilot clinico** è
spento in Fase 1 (decisione del committente, #114) e passa con il resto dell'AI clinica alla
[Release 2.x](Release-2.x.md). Il modulo di analisi radiologica resta
**disattivato in produzione clinica**: senza marcatura CE non può essere usato su
pazienti reali (vedi [Release 2.x](Release-2.x.md)).

Il lavoro della Release non è costruire funzioni nuove — il gestionale c'è già — ma
completare ciò che rende la cartella clinica **difendibile**: tracciabilità,
immutabilità, consensi, segregazione degli accessi. E mettere a norma l'AI che è già in
produzione.
---

## 2. Obiettivi della Release

1. Superare il **Gate 1** (§29): nessun paziente reale prima che il pacchetto sia completo.
2. Rendere la cartella clinica **ricostruibile e attribuibile** nel tempo.
3. Portare l'AI amministrativa in conformità con l'AI Act (trasparenza, literacy,
   informativa, governance).
4. Separare tecnicamente il modulo clinico AI dal prodotto commercializzato.
5. Chiudere il pacchetto privacy: DPIA, informative, contratti fornitori e studi.

## 3. Vision della Release

Uno studio odontoiatrico deve poter rispondere, in qualsiasi momento e a un controllo:
*chi ha visto cosa, chi ha scritto cosa, quando, e sulla base di quale consenso.* Oggi
DentalCare non può. Al termine di Release 1.x, sì.

---

## 4. Scope

### Nucleo clinico (valore probatorio)
- **Audit trail clinico** append-only: accessi, letture, scritture, finalizzazioni,
  download, stampe, export, azioni AI.
- **Finalizzazione delle note** con hash e stati (bozza → da revisionare → finalizzata →
  rettificata/annullata) e **addendum** come unica via di correzione.
- **Consensi versionati**: template, versione, collegamento a piano/procedura, firma,
  revoca.
- **Encounter / Ciclo della seduta** — ✅ **Fatta (dev, #56-#62)**: perno relazionale tra appuntamento e piano di cura (`appointment_treatment_items`), firma reale dell'atto (`performed_by_provider_id`), chiusura autonoma seduta (#60), gestione prestazioni in sospeso con riprogrammazione o rimozione motivata (#61).
- **Odontogramma temporale**: storia dei reperti, non snapshot corrente; confronto tra date.
  Il confronto tra date è coperto dallo **storico degli episodi (#67)**, che fotografa
  l'odontogramma all'ingresso e all'uscita di ogni episodio; la storia per singolo reperto
  (`supersedes_id`, certezza) resta da fare.
- **Storico degli episodi clinici** — ✅ **Fatta (dev, #67, Fase 1)**: ogni visita e ogni
  contatto fuori visita è un episodio con la situazione del paziente **prima e dopo**
  (anamnesi, diagnosi, terapie, odontogramma, piani di cura) in fotografie **append-only con
  hash**; differenze e riepilogo testuale composti dai dati, senza AI; richiesta di apertura
  prima di un salvataggio clinico fuori episodio. Il riepilogo scritto dall'AI è Fase 2.
- **Anamnesi tri-stato**: presente / assente / non noto, con fonte e data.
- **Soft delete & export con password monouso**: ✅ **Fatta (dev, #47)**: archivio ZIP AES-256 e grace period con congelamento JWT.
- **Odontogramma da seduta clinica** — ✅ **Fatta (dev, #65)**: il listino dichiara lo stato che
  ogni prestazione lascia sul dente; in seduta è una **proposta** che il medico applica, cambia o
  ignora (mai applicata da sola), con superfici per le otturazioni. La riga scritta in
  odontogramma porta autore e seduta (`source='session'`).
- **«Genera piano di cura» verificato** — ✅ **Fatta (dev, #66)**: dall'odontogramma si propone
  solo ciò che è da fare (carie, da estrarre, mancante, incluso), con le superfici e la prestazione
  secondo il loro numero; doppioni e carie su denti assenti restano visibili ed esclusi, con il
  motivo. Il server applica le stesse regole (`422 SERVICE_NOT_APPLICABLE`) e l'aggiunta a un piano
  esistente è atomica.

### Identità, accessi e usabilità operativa
- **MFA** per professionisti e amministratori.
- **Segregazione dei ruoli verificata lato server** — ✅ **Fatta (dev, #42, #44, #62)**: `AccessScopeService` per visibilità pazienti e `/api/appointments/*/session/**` protetto da `CLINICAL_WRITE_ROLES` (la segreteria non può firmare atti clinici).
- **Relazione di cura** come criterio di autorizzazione.
- **Merge dei duplicati** paziente con approvazione e audit.
- **Layout tablet 10" e mobile** — ✅ **Fatta (dev, #72)**: menu con etichette da `md`, logout sempre visibile,
  target touch; menu riducibile alle icone e pannello destro nascondibile.
- **Account e cliniche** — ✅ **Fatta (dev, #117)**: le cliniche dell'account si creano, modificano ed eliminano
  solo dalla pagina del titolare (*Amministrazione account*); dalle Impostazioni di una clinica e dagli ambienti di
  prova non si creano cliniche. Terminologia fissata (28/10/2026): **account** → **clinica** (= sede) →
  **poltrona**; nell'interfaccia mai «Centro» né «Studio» da solo.
- **Ordinamento e ricerca liste operative** — ✅ **Fatta (dev)**: ordinamento per colonna intelligente (date/importi decrescenti per default, celle vuote in fondo), ricerca testuale e filtri rapidi su Fatturazione, Richiami, Magazzino, Preventivi e Prestazioni; separazione dello stornato nei KPI contabili.

### Agenda, poltrone e comunicazione con i pazienti
- **Poltrone come anagrafica della clinica** — ✅ **Fatta (dev, #115)**: tabella `clinic_chairs`; si prenota solo su
  poltrone attive (`422 CHAIR_UNKNOWN`); rinomina propagata agli appuntamenti; una poltrona con appuntamenti si
  disattiva, non si elimina. Agenda, disponibilità, Giulia e Copilot usano l'anagrafica. Vista Giorno con orari
  fissi a sinistra, colori per posizione e filtro delle poltrone; avviso oltre 8 poltrone attive.
- **Calendario delle presenze** — ✅ **Fatta (dev, #99)**: fasce orarie e assenze per professionista; fuori presenza
  l'appuntamento è rifiutato con alternative (`422 PROVIDER_NOT_PRESENT`), anche da Copilot e Giulia.
- **Appuntamenti a passi di slot** — ✅ **Fatta (dev, #90)**: orari e durate a multipli dello slot della clinica;
  fuori griglia `422 OFF_GRID` con i due slot vicini. Solo professionisti clinici assegnabili (#95).
- **Stati automatici degli appuntamenti** — ✅ **Fatta (dev, #108)**: la notte dopo, «Non presentato» per gli
  appuntamenti senza seguito, con il segno «automatico» e la conferma manuale; registrare esiti in seduta porta a
  «In corso». Ordine cronologico nella scheda paziente (#107).
- **Scheda di seduta in tre passi** — ✅ **Fatta (dev, #106)**: prima della visita, esito, odontogramma; sintesi del
  paziente in una finestra; prestazioni raggruppate per piano; barra fissa con «Registra» e «Chiudi».
- **Avvisi ai pazienti** — ✅ **Fatta (dev, #111, modalità manuale)**: ogni prenotazione, spostamento o cancellazione
  (gestionale, Copilot, Giulia) lascia un avviso (`appointment_notices`); WhatsApp con link `wa.me` dal WhatsApp
  Business della clinica, oppure e-mail dal server; quelli non mandati restano in Dashboard, *Da avvisare*.
  WhatsApp si attiva per clinica in Impostazioni → Sistema, con il numero WhatsApp Business. Gli SMS non sono un
  canale (#110). La modalità automatica (API Meta) è fuori scope (§5).
- **Richiami** — ✅ **Fatta (dev, #97, #98, #104, #111)**: intervalli e testo della clinica o del medico; storico dei
  contatti con autore; invio del testo per e-mail o WhatsApp con registrazione del contatto.
- **E-mail ai pazienti in prova** — ✅ **Fatta (dev, #103)**: con dati fittizi l'e-mail va a chi prova il programma.

### Ciclo economico e fatturazione
- **Fatturazione conforme** — ✅ **Fatta (dev, #50, #52, #53, #63)**: fattura a saldo vincolata all'avanzamento reale delle prestazioni completate in seduta, documento di acconto, flusso di storno con nota di credito, e numerazione documentale robusta (#63, `nextProgressive` per eliminare collisioni su bozze cancellate).
- **Acconto e saldo coerenti** — ✅ **Fatta (dev, #102)**: l'acconto è l'importo incassato, entro il residuo del
  preventivo; il saldo scala gli acconti emessi con righe di storno.
- **PDF ed e-mail del documento** — ✅ **Fatta (dev, #101)**: PDF generato dal server, inviato al paziente dal server
  di posta, data d'invio registrata (DPIA D-23).
- **Impostazioni dei documenti applicate dal server** — ✅ **Fatta (dev, #97, #98)**: validità e prefissi, IVA,
  pagamento e scadenza della clinica o del medico; «Le mie tariffe» e impostazioni personali per i professionisti
  (#96, #98).

### Infrastruttura e affidabilità
- **Zero-downtime schema patching** — ✅ **Fatta (dev, #64)**: esecuzione DDL transazionale per le viste in `EstimateSchemaInitializer`, azzerando i ritardi e gli errori 500 transitori nei riavvii.
- **Vincolo nota di credito → fattura stornata sui tenant successivi al primo** — ✅ **Fatta (dev, #68)**: il vincolo si cerca sulla tabella giusta e c'è in ogni tenant.
- **Rilascio continuo** — ✅ GitHub Actions: push su `staging` → collaudo, push su `master` → istanza di prova
  pubblica; le patch di schema sono idempotenti e girano all'avvio (gli ambienti di prova al primo accesso).

### Ambiente pubblico di prova e formazione
- **Prova gratuita, ambiente di prova degli studi e Academy** — ✅ **Fatta (dev, #69, #70)**, in
  attesa di integrazione sul branch principale. Tre porte indipendenti: registrazione di un
  nuovo studio (`/registrati`), **prova gratuita** (`/prova`: ogni medico riceve un tenant demo
  personale con dati di esempio, ripristinabile, attivo **14 giorni**, poi accesso bloccato con
  richiesta di attivazione e cancellazione dopo altri **30**) e **ambiente di prova dello studio**
  per chi è già cliente (uno per studio, dati di esempio, aperto dall'app senza seconda password,
  dura quanto lo studio). La prova gratuita, aperta a chiunque, al go-live resta su un'istanza
  separata dalla produzione. L'**Academy** (oggi 10 moduli e 47 lezioni, manuale ufficiale del corso dal 22/10/2026,
  #85) è per tutti: «Prova ora» apre
  la schermata della lezione sempre sui dati di esempio; i contenuti li cura il ruolo di
  piattaforma `ACADEMY_EDITOR`. Dettagli in
  [06-Multitenancy §8](../04-Architecture-Handbook/06-Multitenancy.md#8-tenant-demo-e-workspace-demo).
  Aggiornamenti: creazione della prova in ~30 secondi (#84); il titolare della prova può fare da amministratore
  (#87, DPIA D-20) ma non creare account né cliniche (#117); Giulia nella prova con un limite di prenotazioni e
  spostamenti (5, impostabile), comunicato in Dashboard, nell'e-mail di benvenuto e da Giulia (#109). I manuali
  utente in `05-Manuale-Utente` si generano dalle lezioni (`tools/genera_manuale.py`).

### Integrità dei documenti
- Impronta **SHA-256**, verifica del MIME reale, scansione malware, controllo di coerenza
  paziente↔immagine sugli upload.

### Diritti dell'interessato
- **Export completo per paziente** (art. 15 GDPR) e report degli accessi.

### AI amministrativa a norma
- **Registro AI**, AI Use Policy, programma di **AI literacy**.
- **Inventario tecnico flussi AI per DPO** — ✅ **Fatta (dev, #55)**: censimento completo flussi, classificazione Art. 9 GDPR e tabella per ROPA/DPIA.
- **Disclosure** dell'assistente vocale a inizio interazione + fallback umano sempre
  disponibile (✅ **Fatta, Art. 50 AI Act** con Inspection Binder Retell Cartella 13).
- **Errori intelligenti** — ✅ **Fatta (dev, #54)**: riscrittura AI dei messaggi d'errore applicativi e conflitti DB in linguaggio comprensibile.
- **Copilot amministrativo senza indicazioni cliniche** — ✅ **Fatta (dev, #88)**: regola fissa nel codice, valida
  anche con prompt personalizzati; pannello con dati veri (#92); tutti gli strumenti esposti al modello (#79,
  DPIA D-16).
- **Copilot clinico spento in Fase 1** — 📋 **Confermata (#114)**: la modalità clinica (anamnesi, odontogramma,
  piani) passa alla Release 2.x; gli studi di prova non nasceranno più in modalità clinica (oggi D-19).
- **Limiti operativi**: nessun triage, nessuna diagnosi, nessuna prescrizione.
- **Informativa al paziente** sull'uso dell'AI (L. 132/2025).
- **Kill switch** per modulo e **gate no-clinical** sul modulo radiologico.
- Logging AI esteso (paziente, esito, correlation ID).

### Chairside Agent “Ehi Giulia”

Canale vocale hands-free del **Copilot esistente**, disponibile dalla postazione di
poltrona. La richiesta pronunciata viene trascritta nella stessa chat e sessione del
Copilot; la sintesi vocale è abilitabile dal pannello e configurabile nelle impostazioni
per voce, lingua di riconoscimento, lingua di sintesi e modalità `off`/`brief`/`full`.

Ordine di sviluppo: audit e autorizzazioni server-side → chiusura del gate di conferma
Copilot → conversazione condivisa e policy → push-to-talk/STT → TTS → hotword locale →
revisione dettatura e doppia conferma → test avversi e pilota. La hotword viene elaborata
localmente e nessun audio è conservato per default.

**Stima:** backend 11-18, frontend 17-26 e test/QA 15-25 giornate-agente; totale
**43-69 giornate-agente**, circa **4-5 settimane calendario** con tre agenti dedicati in
parallelo. L'attivazione non è bloccante per il resto della Release: se il pilota non è
verde, la funzione resta installata ma disabilitata tramite policy server-side.

### Giulia centralizzata (#100)

Un solo agente vocale e **un numero unico** per tutte le cliniche, al posto di un agente e un numero per tenant.
Giulia si presenta come segreteria AI (AI Act art. 50) e riconosce la clinica dal **codice a 5 cifre** (a voce o
da tastiera), dal numero chiamante con il cognome, o da nome e città, con conferma a voce. Il riconoscimento rilascia
un **biglietto firmato** (30 minuti, una chiamata) con cui si ottiene un token di servizio ristretto alla clinica
(`VoiceAgentScope`); un modello linguistico non può scegliere la clinica. Le e-mail di conferma partono dal server
di posta di DentalCare (D-26). Stato: in collaudo; go-live con la vera produzione (gennaio 2027). Il
`retell-provisioner` per-tenant è **in dismissione**.

### LLM Gateway (`dentalcare-llm-gateway`)

✅ **Fatta (dev, #74)**: servizio `llm-ner-gateway` (repo `llm-rizzo-gateway`, riconoscitore 0.3B). Aperto: n8n
usa ancora una propria chiave OpenAI per gli agenti di Giulia (#105).

Trust boundary tra DentalCare e i provider LLM (OpenAI). Intercetta ogni chiamata
Copilot/AI, pseudonimizza PII/PHI prima dell'invio al provider e detokenizza la
risposta prima di restituirla al backend. API OpenAI-compatible (`POST /v1/chat/completions`).
Dopo la migrazione **nessuna API key LLM risiede in DentalCare**. Obbligatorio per il
Gate 1: senza gateway il trasferimento di dati clinici verso OpenAI non è coperto da
adeguate misure tecniche per il DPA. Spec completa: `directives/dentalcare-llm-gateway/`.

### Governance e privacy
- **DPIA** approvata · ROPA · informative · **DPA + SCC + TIA** con i fornitori AI ·
  contratti studi con clausole deployer · registro claim.

---

## 5. Out of Scope

Rimandati consapevolmente al post-Release 1.x:

- conservazione a norma dei documenti (backup ≠ conservazione);
- firma elettronica avanzata/qualificata e PAdES;
- DICOM / DICOMweb / PACS;
- FHIR API;
- connettore FSE 2.0;
- portale paziente;
- terminology service;
- charting parodontale avanzato ed esame obiettivo strutturato;
- **WhatsApp automatico** (API Meta: promemoria del giorno prima, stato di consegna, risposte) e **prenotazioni e
  disdette via WhatsApp** dei pazienti registrati (#111 fasi B-D, #112);
- interfaccia nelle **lingue dell'UE** con traduzione assistita (#71);
- **AI clinica**: Copilot clinico (#114), sintesi del percorso clinico scritta dall'AI (#67), proposta delle
  condizioni dall'analisi radiografica (#94 B);
- **modulo radiologico AI** → [Release 2.x](Release-2.x.md).

Sono funzioni per crescere, non per il primo studio.

---

## 6. Target Clienti

Studio odontoiatrico singolo o piccolo studio associato, italiano, che oggi lavora con
carta o con un gestionale legacy. Un solo studio pilota per il go-live.

## 7. Value Proposition

*Da definire* (input commerciale). La proposta tecnica: un gestionale completo in cui
l'AI toglie lavoro alla segreteria senza toccare la responsabilità clinica, e in cui la
cartella regge un controllo.

## 8. User Personas

Tre ruoli operativi, documentati nel [Manuale Utente](../05-Manuale-Utente/README.md) (generato dall'Academy):
**medico e igienista**, **segreteria**, **titolare e amministratore**.
Le personas commerciali sono da definire.

## 9. User Journey

Percorsi operativi per ruolo: vedi Manuale Utente. Journey commerciale da definire.

---

## 10. Architettura

Vedi [Architecture Handbook](../04-Architecture-Handbook/Architecture-Handbook.md).
In sintesi: Angular 21 → API Spring Boot 3.5 / Java 25 → PostgreSQL multi-tenant
schema-per-tenant; MinIO per documenti e immagini; servizi AI disaccoppiati.

## 11. Moduli Core

Agenda (poltrone, presenze, slot, stati automatici) · Pazienti · Cartella clinica · Scheda di seduta · Storico
episodi · Odontogramma · Anamnesi · Diagnosi · Prescrizioni · Piani di cura · Preventivi · Fatturazione · Richiami ·
Avvisi ai pazienti (e-mail, WhatsApp manuale) · Magazzino · Prestazioni · Impostazioni della clinica e personali ·
Amministrazione account · Academy. **Tutti implementati**; il lavoro di Release 1.x è sul livello probatorio,
non sulle funzioni.

## 12. Moduli AI

| Modulo | In Release 1.x |
|---|---|
| **Copilot conversazionale** | ✅ modalità amministrativa, con conferma umana obbligatoria per ogni scrittura; modalità clinica spenta in Fase 1 (#114) |
| **Giulia, segreteria telefonica** (prenotazioni, spostamenti, cancellazioni) | ✅ inclusa, con disclosure e fallback umano — un agente e un numero per tutte le cliniche (#100); limite nelle prove (#109) |
| **Chairside Agent “Ehi Giulia”** (Copilot hands-free in poltrona) | 📋 incluso nello scope; attivazione subordinata a doppio gate, DPIA e pilota |
| **Analisi radiologica** | 🔒 **disattivato** in produzione clinica → Release 2.x |

Vedi [AI-Roadmap](AI-Roadmap.md) per la classificazione regolatoria di ciascuno.

## 13. Sicurezza

Vedi [07-Security](../04-Architecture-Handbook/07-Security.md).
Novità di Release 1.x: MFA, audit trail clinico, segregazione verificata lato server,
integrità dei documenti, pen test.

## 14. Compliance

- **GDPR**: cifratura a riposo dei dati identificativi già attiva (vedi
  [11-Data-Encryption](../04-Architecture-Handbook/11-Data-Encryption.md)); DPIA,
  informative, DPA e diritti dell'interessato in Release 1.x.
- **AI Act**: perimetro non high-risk (AI amministrativa). Trasparenza art. 50, AI
  literacy art. 4, governance, registro AI.
- **MDR**: **non applicabile** in Release 1.x, perché il modulo clinico AI è escluso dal
  prodotto commercializzato.
- **L. 132/2025**: informativa sull'uso dell'AI in sanità; la decisione resta al
  professionista.

## 15. DICOM

Fuori scope. Le immagini sono gestite in formati standard (JPEG/PNG/PDF). Il supporto
DICOM nativo è prerequisito pratico della Release 2.x.

## 16. Clinical Workflow

Accettazione → identificazione → aggiornamento anamnesi e consensi → **encounter** →
osservazioni, odontogramma, immagini, diagnosi, piano, procedure → revisione →
**finalizzazione** → follow-up e addendum. Gli anelli in grassetto sono quelli che
Release 1.x introduce.

## 17. Funzionalità Dettagliate

Vedi §4 e il [Manuale Utente](../05-Manuale-Utente/README.md).

## 18. UX/UI

Layout a tre colonne (menu · contenuto · pannello contestuale), Angular standalone +
signals + Tailwind. Requisiti UX introdotti dalla Release: stato della nota sempre
visibile, distinzione netta tra pianificato ed eseguito, nessuna pre-selezione di
"assenza patologie", avvisi su allergie e farmaci critici.

## 19. API

REST/JSON con JWT; ruoli verificati lato server. Nessuna entità di persistenza esposta
direttamente. Adapter verso standard esterni: fuori scope.

## 20. Database

PostgreSQL, schema per tenant, patch idempotente a runtime. Modifiche di Release 1.x:
nuove entità (audit, consensi, encounter), colonne di stato/versione/hash sulle note,
stato di annullamento al posto della cancellazione fisica.

## 21. Integrazioni

Assistente vocale (fornitore esterno) e automazioni di workflow; server di posta per le e-mail ai pazienti;
WhatsApp in modalità manuale con link `wa.me` (DentalCare non scambia dati con Meta: il messaggio lo invia la
clinica dal proprio WhatsApp Business, D-28). Ogni fornitore che tratta
dati personali richiede DPA, valutazione del trasferimento e divieto di training: è parte
del Gate 1.

## 22. AI Services

Copilot (LLM con function calling) e assistente vocale. Il servizio di visione
radiologica resta deployato ma **non raggiungibile dai tenant clinici**.

Le chiamate LLM transitano obbligatoriamente per **`dentalcare-llm-gateway`** (privacy
engine, pseudonimizzazione, audit). Giulia è un unico agente per tutte le cliniche (#100): il
**`retell-provisioner`** per-tenant è in dismissione. Il gateway è indipendente da DentalCare e riutilizzabile da
altri prodotti futuri.

## 23. Performance

Requisiti da fissare su: apertura cartella, rendering odontogramma, caricamento immagini,
export. Non ci sono oggi soglie dichiarate.

## 24. Quality Gates

- build verde (backend + frontend);
- test cross-tenant automatici superati;
- test di segregazione dei ruoli superati (una chiamata diretta alle API cliniche da un
  ruolo non autorizzato deve essere negata **e registrata**);
- restore del database eseguito e verificato;
- pen test senza findings critici aperti.

## 25. Piano di Test

Funzionali (workflow, stati, finalizzazione, rettifiche, export) · clinici (prima visita,
urgenza, paziente anticoagulato, allergia, minore, rettifica, duplicato) · privacy e
sicurezza (accesso non autorizzato, cross-tenant, IDOR, export massivo, log tampering) ·
migrazione · performance.

## 26. Piano di Validazione

Ogni scenario clinico eseguito da **odontoiatri reali** con criteri di accettazione
dichiarati. La validazione non è una demo: è una prova documentata.

## 27. Studi Pilota

Uno studio, selezionato, con parallel run limitato e verbale di accettazione. Il pilota
inizia **dopo** il Gate 1, non prima: un pilota con pazienti reali *è* go-live.

## 28. KPI della Release

Vedi [Product-Roadmap §29](Product-Roadmap.md#29-kpi-di-prodotto). La misurazione dipende
dall'audit trail: è la prima milestone tecnica per questo motivo.

---

## 29. Criteri Go Live — **Gate 1**

Nessun paziente reale prima che **tutte** le voci siano verdi:

- [ ] modulo radiologico disattivato in produzione clinica (flag + claim + contratto)
- [ ] audit trail clinico attivo e append-only
- [ ] note finalizzabili, immutabili dopo la firma, addendum funzionante
- [ ] consensi versionati collegati ai piani
- [ ] segreteria non vede anamnesi/diagnosi/odontogramma/note (**verificato lato server**)
- [ ] MFA attiva
- [ ] DPIA approvata dal DPO
- [ ] informative aggiornate (privacy + uso AI)
- [ ] DPA firmati con tutti i fornitori AI
- [ ] disclosure assistente vocale + fallback umano
- [ ] `dentalcare-llm-gateway` attivo: nessuna API key LLM in DentalCare, privacy engine operativo
- [ ] Giulia centralizzata (#100) collaudata: riconoscimento della clinica, biglietto firmato, numero dedicato
- [ ] Copilot clinico spento in produzione (#114)
- [ ] AI literacy erogata, con evidenze
- [ ] contratto studio con clausole deployer
- [ ] restore testato almeno una volta
- [ ] pen test eseguito, remediation chiusa
- [ ] export paziente (art. 15) funzionante
- [ ] fotografie degli episodi clinici (#67) attive dal primo paziente: una visita senza
      fotografia d'ingresso non si recupera dopo
- [ ] prova gratuita (#69) separata dalla produzione: in produzione
      `app.demo-workspace.public-registration=false` e `public-url` verso l'istanza di prova;
      account demo condiviso spento dove ci sono dati reali

> Il Gate è **binario**. Non esiste "andiamo live e sistemiamo dopo": nel momento in cui
> entra il primo paziente reale, o il pacchetto è completo o il prodotto è non conforme
> dal primo giorno. Il rischio operativo più concreto è il pilota informale — due pazienti
> veri caricati "tanto per provare" sono go-live a tutti gli effetti.

---

## 30-31. Piano Commerciale / Marketing

*Da definire.* Vincolo che il marketing eredita dalla compliance: **nessun claim medico**
sul modulo radiologico finché non c'è marcatura CE. Formulazioni come "diagnosi
automatica", "individua tutte le patologie", "clinicamente validato" sono vietate senza
evidenza. Il registro claim è parte del Gate 1.

---

## 32. Roadmap verso Release 2

Il passaggio alla Release 2.x non è automatico: richiede il **Gate 2** (domanda
dimostrata per l'AI clinica). Una sola attività della Release 2.x deve però iniziare
**dentro** la Release 1.x, perché non è recuperabile a posteriori: la **data governance
del dataset** (base giuridica, informativa, SOP di annotazione, provenienza). Vedi
[Release 2.x §6](Release-2.x.md).

## 33. Lessons Learned

- Il prodotto è stato costruito molto più velocemente della sua governance. La parte
  comprimibile dall'AI (il codice) è corsa; la parte non comprimibile (DPIA, contratti,
  firme) è rimasta al via. È il profilo di rischio tipico dello sviluppo accelerato.
- La funzione più attraente del prodotto (l'AI radiologica) è quella che non si può
  vendere per prima.
- Le decisioni tecniche prese bene fin dall'inizio (tenant come confine, CF non chiave,
  provenienza dell'output AI, conferma umana strutturale) stanno reggendo il peso della
  compliance senza rilavorazione.

## 34. Allegati

- [Architecture Handbook](../04-Architecture-Handbook/Architecture-Handbook.md)
- [Manuale Utente](../05-Manuale-Utente/README.md)
- [Modello della cartella clinica](../04-Architecture-Handbook/12-Clinical-Record-Model.md)
- [Cifratura dati & GDPR](../04-Architecture-Handbook/11-Data-Encryption.md)
