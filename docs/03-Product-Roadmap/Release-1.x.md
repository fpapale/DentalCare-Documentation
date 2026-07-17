# Release 1.x — Gestionale odontoiatrico con AI amministrativa

**Fase 1** · **Target: gennaio 2027** · **Versione doc:** 1.0 (17 luglio 2026)

---

## 1. Executive Summary

Release 1.x porta DentalCare Pro dallo stato **demo** al primo **studio pagante con
pazienti reali**. Il prodotto include il gestionale completo e l'AI **amministrativa**
(Copilot conversazionale e assistente vocale). Il modulo di analisi radiologica resta
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
- **Encounter** come perno che lega osservazioni, diagnosi, procedure, immagini.
- **Odontogramma temporale**: storia dei reperti, non snapshot corrente; confronto tra date.
- **Anamnesi tri-stato**: presente / assente / non noto, con fonte e data.
- **Soft delete**: stato di annullamento al posto della cancellazione fisica.

### Identità e accessi
- **MFA** per professionisti e amministratori.
- **Segregazione dei ruoli verificata lato server**, non solo in interfaccia.
- **Relazione di cura** come criterio di autorizzazione.
- **Merge dei duplicati** paziente con approvazione e audit.

### Integrità dei documenti
- Impronta **SHA-256**, verifica del MIME reale, scansione malware, controllo di coerenza
  paziente↔immagine sugli upload.

### Diritti dell'interessato
- **Export completo per paziente** (art. 15 GDPR) e report degli accessi.

### AI amministrativa a norma
- **Registro AI**, AI Use Policy, programma di **AI literacy**.
- **Disclosure** dell'assistente vocale a inizio interazione + fallback umano sempre
  disponibile.
- **Limiti operativi**: nessun triage, nessuna diagnosi, nessuna prescrizione.
- **Informativa al paziente** sull'uso dell'AI (L. 132/2025).
- **Kill switch** per modulo e **gate no-clinical** sul modulo radiologico.
- Logging AI esteso (paziente, esito, correlation ID).

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

Tre ruoli operativi, documentati nel [Manuale Utente](../05-Manuale-Utente/README.md):
**dottoressa** (medico), **segretaria** (front-office), **amministratore** (titolare).
Le personas commerciali sono da definire.

## 9. User Journey

Percorsi operativi per ruolo: vedi Manuale Utente. Journey commerciale da definire.

---

## 10. Architettura

Vedi [Architecture Handbook](../04-Architecture-Handbook/Architecture-Handbook.md).
In sintesi: Angular 21 → API Spring Boot 3.5 / Java 25 → PostgreSQL multi-tenant
schema-per-tenant; MinIO per documenti e immagini; servizi AI disaccoppiati.

## 11. Moduli Core

Agenda · Pazienti · Cartella clinica · Odontogramma · Anamnesi · Diagnosi · Prescrizioni
· Piani di cura · Preventivi · Fatturazione · Richiami · Magazzino · Prestazioni ·
Impostazioni. **Tutti implementati**; il lavoro di Release 1.x è sul livello probatorio,
non sulle funzioni.

## 12. Moduli AI

| Modulo | In Release 1.x |
|---|---|
| **Copilot conversazionale** | ✅ incluso, con conferma umana obbligatoria per ogni scrittura |
| **Assistente vocale** (prenotazioni) | ✅ incluso, con disclosure e fallback umano |
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

Assistente vocale (fornitore esterno) e automazioni di workflow. Ogni fornitore che tratta
dati personali richiede DPA, valutazione del trasferimento e divieto di training: è parte
del Gate 1.

## 22. AI Services

Copilot (LLM con function calling) e assistente vocale. Il servizio di visione
radiologica resta deployato ma **non raggiungibile dai tenant clinici**.

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
- [ ] AI literacy erogata, con evidenze
- [ ] contratto studio con clausole deployer
- [ ] restore testato almeno una volta
- [ ] pen test eseguito, remediation chiusa
- [ ] export paziente (art. 15) funzionante

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
