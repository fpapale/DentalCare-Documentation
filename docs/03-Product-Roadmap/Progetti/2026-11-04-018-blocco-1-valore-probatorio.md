# #18 Blocco 1 — Valore probatorio della cartella clinica

**Data:** 04/11/2026 · **Stato:** 📋 progetto completo (decisioni D1-D7 del 04/11/2026), da approvare · **Gate di go-live:** sì, nessun paziente reale prima della chiusura
**Per chi:** chi pianifica e costruisce (coordinatore e agenti) e il committente.
**Fonti:** [13 — Audit trail](../../04-Architecture-Handbook/13-Audit-Trail.md) (modello probatorio, taglio Tier 1/Tier 2), [12 — Modello cartella clinica](../../04-Architecture-Handbook/12-Clinical-Record-Model.md), guida alla digitalizzazione della cartella (§6.1 stati di una nota, §6.2 addendum, §12 audit trail, §26.2 segreteria), ricognizione del codice del 04/11/2026.
**Allegato riservato:** lo stato attuale dei punti scoperti sta nel repo applicativo (privato). Qui si descrive solo lo stato da raggiungere.

---

## 1. Perché

Un domani bisogna poter dimostrare **chi ha fatto cosa, quando, su quale paziente, con quale autorizzazione, e che nessuno ha cambiato le carte dopo**. I casi tipici indicati dal committente:
- un paziente che contesta una cura;
- un paziente che chiede chi ha visto i suoi dati.

Oggi la cartella non regge nessuno dei due:
- non c'è un registro delle consultazioni;
- una nota del diario si può cambiare o cancellare per sempre, senza traccia;
- la separazione fra segreteria e dati clinici non è garantita dal server;
- le cancellazioni sono fisiche.

## 2. Obiettivi, non obiettivi, anti-obiettivi

**Obiettivi**
1. Registro degli accessi clinici: letture e scritture, append-only, con integrità verificabile (voce di gate «audit trail clinico attivo e append-only»).
2. Note cliniche finalizzabili, non modificabili dopo la firma, con addendum (voce di gate «note finalizzabili…»).
3. Segreteria senza accesso ai dati clinici, garantito dal server, con ogni tentativo negato e registrato (voce di gate «segreteria non vede…», criterio §26.2).
4. Cancellazione logica al posto di quella fisica per i dati clinici e per i pazienti.

**Non obiettivi** (sono di altri blocchi o del Tier 2)
- Report degli accessi per il paziente ed export art. 15: #18 Blocco 3, punto 3.2. Il registro deve solo renderli possibili.
- Amministratore tecnico e break glass: #18 Blocco 3, punto 3.3. Qui si riserva solo il tipo di evento.
- Odontogramma con storia: #18 Blocco 2, punto 2.4.
- Consensi versionati ed encounter: #18 Blocco 2.
- Sigilli qualificati eIDAS, servizio di audit separato, SIEM, pacchetto di prova: Tier 2.
- MFA: #73. Il registro prevede il campo, vuoto finché non c'è.
- Titolare dell'account non clinico: #126 S1. Fino ad allora il titolare mantiene l'accesso clinico di oggi.
- **Relazione di cura come autorizzazione** (un medico vede solo i «suoi» pazienti): #18 punto 3.6, Blocco 3. In questo blocco l'autorizzazione è **per ruolo**. Registrare la seduta di un collega resta legittimo (decisione di #62).

**Anti-obiettivi** (sarebbe un fallimento anche se funziona)
- Lo studio rallenta o si blocca per colpa del registro: niente lock globali, niente chiamate sincrone a servizi esterni.
- Il registro duplica i contenuti clinici: dentro ci sono identificativi, tipi ed esiti. Valori clinici solo dove servono come prova di una modifica (§5.1.6).
- Automatismi silenziosi sugli stati clinici: una nota non diventa definitiva senza un'azione consapevole del medico.
- Il medico deve rifare l'accesso o cambiare il modo in cui lavora in poltrona.
- Una protezione che esiste solo nell'interfaccia.

## 3. Vincoli

- **Schema per tenant**: ogni studio ha il suo schema; le tabelle nuove nascono a ogni avvio con `patchSchema` idempotente. Le viste vanno create dopo le colonne che usano.
- **Ruolo del database**: l'applicazione si collega con un ruolo proprietario degli schemi, che fa anche DDL, `DROP SCHEMA` e `TRUNCATE`. Un `GRANT` «solo INSERT» non basta: servono trigger che rifiutano `UPDATE`, `DELETE` e `TRUNCATE`, come quello che già protegge le fotografie dell'episodio. Un ruolo separato per l'audit è Tier 2.
- **Ambienti con dati fittizi** (demo, studio di prova, ambiente di prova del cliente): il ripristino dei dati d'esempio svuota le tabelle del tenant. Il registro va gestito esplicitamente (§5.1.8).
- **Copilot**: gira su un thread di lavoro con un contesto ridotto, e una sola richiesta può leggere molti pazienti. La registrazione delle sue letture non può dipendere solo da un filtro HTTP.
- **Scritture senza utente**: la callback dell'analisi AI e alcuni job di sistema scrivono dati clinici senza un utente collegato. L'attore è «sistema», con il nome del job.
- **Impostazioni parametriche**: soglie degli avvisi, intervallo dei sigilli e retention minima stanno in proprietà o in Impostazioni, mai come costanti.
- **Niente automatismi silenziosi** su stati clinici e contabili (regola del committente).
- Oggi tutti gli ambienti contengono solo dati fittizi.

## 4. Decisioni già prese

| Decisione | Scelta | Chi |
|---|---|---|
| Ambito | Tier 1 di [13 — Audit trail](../../04-Architecture-Handbook/13-Audit-Trail.md); Tier 2 escluso | committente, luglio 2026 |
| Dove vive il registro | in ogni schema tenant (B1), come il resto dei dati | committente, luglio; confermato il 04/11 |
| Integrità | impronta per evento più **sigillo periodico** che concatena i sigilli fra loro (A2): nessun lock per evento | committente, luglio; confermato il 04/11 |
| Modulo o servizio | modulo interno dietro un'interfaccia stretta (D1); la tabella fa già da outbox per un servizio futuro | committente, luglio |
| Ordine | 1.1 → 1.2 → 1.3 → 1.4 | committente, 04/11 |
| Esecuzione | metodo ad agenti, con Opus come implementatore sulle parti di sicurezza ([16 — Metodo](../../04-Architecture-Handbook/16-Metodo-Sviluppo-Agenti.md)) | committente, 04/11 |

## 5. Il progetto

### 5.1 Registro degli accessi clinici (1.1)

**5.1.1 Tabella.** `<schema>.clinical_audit_log`, creata da `patchSchema`.

| Gruppo | Campi |
|---|---|
| Evento | `id`, `occurred_at` (UTC, millisecondi), `event_type`, `action`, `result` (`SUCCESS`, `DENIED`, `ERROR`) |
| Attore | `actor_provider_id` (null per i job), `actor_kind` (`USER`, `SYSTEM`, `VOICE_AGENT`), `actor_role` (ruolo al momento, dal token), `persona_provider_id` (se attiva una persona di prova), `auth_level` (vuoto fino a #73), `session_id`, `ip_address`, `user_agent`, `channel` (`UI`, `COPILOT`, `SYSTEM`, `VOICE`) |
| Soggetto | `clinic_id`, `patient_id`, `resource_type`, `resource_id`, `patient_ids` (solo per gli eventi aggregati), `encounter_id` (vuoto fino al Blocco 2) |
| Autorizzazione | `authz_rule` (la regola che ha concesso o negato), `purpose`, `reason` (obbligatoria per annullamenti e, in futuro, break glass) |
| Modifica | `changed_fields`, `before_values`, `after_values` (§5.1.6), `version_before`, `version_after` |
| Tracciabilità | `correlation_id` (uno per richiesta), `app_version` |
| Integrità | `event_hash` (SHA-256 su una rappresentazione canonica dei campi), `seal_id` (il sigillo che lo copre, valorizzato alla sigillatura) |

Indici almeno su `(patient_id, occurred_at)`, `(actor_provider_id, occurred_at)` e `(occurred_at)`.

**5.1.2 Append-only.**
- Trigger `BEFORE UPDATE OR DELETE` e `BEFORE TRUNCATE` che rifiutano l'operazione, sul modello di quello delle fotografie dell'episodio.
- Unica eccezione: l'assegnazione di `seal_id` alla sigillatura, consentita solo per le righe con `seal_id` ancora vuoto e solo su quella colonna.

**5.1.3 Sigilli.**
- Tabella `<schema>.clinical_audit_seals`: `id`, `sealed_from`, `sealed_to`, `event_count`, `root_hash`, `previous_seal_hash`, `seal_hash`, `algorithm_version`, `created_at`, anche lei append-only.
- Un job sigilla gli eventi non ancora sigillati, in ordine `(occurred_at, id)`, a intervalli configurabili: `app.audit.seal-interval`, proposta 1 ora.
- `root_hash` è calcolato sulle impronte degli eventi. `seal_hash` concatena `root_hash` e `previous_seal_hash`: chi toglie o cambia un evento, o un sigillo, rompe la catena da lì in avanti.
- **I sigilli sono HMAC-SHA256** con una chiave che **non sta nel database**. La chiave è derivata con HKDF dalla master key della cifratura GDPR, con un'etichetta propria («audit-seal»), e ha lo stesso fail-fast all'avvio. Chi ha accesso al database come proprietario può alterare eventi e impronte, ma non può ricalcolare i sigilli senza la chiave. Scelta del coordinatore.
- Ogni sigillo porta `algorithm_version`: si può cambiare algoritmo senza invalidare i sigilli vecchi.
- Limite dichiarato: la chiave è della piattaforma, quindi la tamper-evidence Tier 1 vale contro chi tocca il database, non contro chi gestisce la piattaforma. L'opponibilità a terzi (timestamp qualificato sui sigilli, o ancoraggio fuori dal sistema) è Tier 2, e si aggancia qui senza rifare nulla.

**5.1.4 Interfaccia.**
- `ClinicalAuditService.record(event)` per le scritture: gira **nella stessa transazione** della modifica clinica.
- `recordRead(...)` per le letture.
- Il registro è **fail-closed**: se l'evento non si scrive, l'operazione fallisce, letture comprese. Il database è lo stesso, quindi un registro irraggiungibile vuol dire comunque uno studio fermo.
- `ai_audit_log` resta per le azioni del Copilot. Le letture e scritture cliniche fatte dal Copilot vanno anche nel registro clinico.

**5.1.5 Cosa si registra.** Il catalogo degli eventi sta nel codice, in un solo posto.

| Famiglia | Eventi |
|---|---|
| Consultazione | apertura della cartella, del diario, dell'anamnesi, dell'odontogramma, dei piani, degli episodi e della seduta; apertura e scaricamento di documenti e analisi; scheda clinica del paziente |
| Scrittura | creazione, modifica e cancellazione logica di diario, diagnosi, prescrizioni, anamnesi, odontogramma, piani e prestazioni, documenti, analisi revisionate; chiusura della seduta; cambio di stato clinico di appuntamenti e prestazioni |
| Note | finalizzazione, addendum, annullamento (§5.2) |
| Accesso negato | ogni rifiuto per ruolo (§5.3), con la regola. La relazione di cura arriverà con il punto 3.6 |
| Sistema | sigillo creato, verifica d'integrità eseguita, ripristino dei dati d'esempio (solo ambienti di prova) |
| Riservati | `EXPORT`, `PRINT`, `BREAK_GLASS` (usati dai Blocchi 2 e 3) |

**Come si aggancia**, scelta del coordinatore che chiude la decisione C di luglio:
- **Un filtro HTTP** dopo quelli di autenticazione, con un **catalogo dei percorsi clinici**. Copre le consultazioni via API (circa 24 GET) e i rifiuti. Ricava il paziente dal percorso.
- **Chiamate esplicite** dove il filtro non vede: i tool del Copilot, le letture indirette fatte per l'utente (allerte cliniche in agenda e dashboard) e le scritture, che hanno bisogno dei valori prima e dopo.
- **Letture di molti pazienti in una sola richiesta** (agenda, dashboard, ricerche del Copilot): **un evento aggregato** con l'elenco dei pazienti in `patient_ids`, non un evento per paziente.
- Le letture interne del sistema che non mostrano nulla a un utente non si registrano. Per esempio la composizione delle fotografie dell'episodio: si registra l'azione dell'utente che l'ha causata.

**5.1.6 Valori nella modifica.**
- Per le scritture si registrano i nomi dei campi cambiati e i loro valori prima e dopo, perché servono a provare che cosa è cambiato.
- Per le note finalizzate la prova sta già nella nota e nelle sue versioni: lì il registro tiene solo gli identificativi e le versioni.
- Le letture non contengono mai contenuti clinici.
- Da dichiarare nel registro DPIA (§8).

**5.1.7 Conservazione.**
- Nessuna cancellazione automatica.
- `app.audit.retention-min-months` (24, come chiede il Garante per gli accessi al dossier) impedisce qualsiasi eliminazione più giovane. L'eliminazione oltre la soglia sarà una procedura documentata, non una funzione dell'interfaccia.
- L'export del tenant (`TenantExportService`) include registro e sigilli, in streaming, perché possono essere milioni di righe.
- **Alla chiusura dell'account** il registro va allo studio con l'export: lo studio è il titolare del trattamento ed è lui a conservarlo per i 24 mesi. Dopo il periodo di grazia la cancellazione dello schema procede come oggi. DentalCare, come responsabile, restituisce e cancella. Scelta del coordinatore, da dichiarare nel registro DPIA e da confermare col DPO.

**5.1.8 Ambienti con dati fittizi.**
- Il ripristino dei dati d'esempio di demo, studio di prova e ambiente di prova ricrea registro e sigilli da zero: toglie i trigger, svuota e li rimette.
- È ammesso solo negli schemi di questi ambienti, ed è registrato nel registro di piattaforma dei tenant.
- Il registro non entra nei dati d'esempio esportati.

**5.1.9 Avvisi.**
- Un job a intervalli configurabili applica regole con soglie in Impostazioni:
  - uno stesso utente apre più di N pazienti in M minuti (proposta: 30 in 10 minuti);
  - più di K accessi negati in un'ora;
  - consultazioni fuori dall'orario dello studio, se l'orario è impostato.
- Produce righe in `<schema>.clinical_audit_alerts`, con stato «da vedere» e «visto da…».
- **Li riceve il titolare dello studio** (D5): elenco in Impostazioni → Sicurezza, e un riepilogo giornaliero via e-mail facoltativo. Vede chi, quando e quanti pazienti; l'elenco dei pazienti solo su richiesta, e la richiesta finisce nel registro.

**5.1.10 Verifica d'integrità.**
- Una funzione, chiamabile da un job e da un endpoint riservato all'amministrazione, ricalcola impronte e catena dei sigilli e dice dove si rompe.
- L'esito è registrato a sua volta.

### 5.2 Note cliniche: firma, addendum, annullamento (1.2)

**Ambito.**
- Le note del diario (`clinical_history_entries`), comprese quelle di entrata e uscita dell'episodio e quelle scritte dal Copilot.
- Diagnosi e prescrizioni non si finalizzano in questo blocco. Le loro modifiche sono registrate con prima e dopo (§5.1.6) e la cancellazione diventa logica (§5.4). Per le prescrizioni, #123 aggiunge «annulla e sostituisci».

**Stati** (sottoinsieme di §6.1 della guida):

| Stato | Cosa si può fare |
|---|---|
| Bozza | modificare; cancellare (cancellazione logica, registrata) |
| Finalizzata | solo leggere; aggiungere un addendum; annullare con motivazione |
| Annullata | solo leggere, con la motivazione in vista |
| Storica | solo leggere; addendum. Sono le note scritte prima del rilascio |

«Da revisionare» serve alla dettatura (#39) e arriverà con lei. «Rettificata» in Fase 1 si ottiene con l'addendum.

**Regole.**
- Chi firma: solo l'**autore** della nota, un clinico. Alla firma la nota prende `finalized_at`, `finalized_by`, `version` e `content_hash`: SHA-256 su una rappresentazione canonica, con lo stesso metodo delle fotografie dell'episodio.
- Addendum: entità separata collegata alla nota (`clinical_history_addenda`). Contiene autore, data e ora, motivo, testo, eventuale impatto sul piano o sul paziente, e la propria impronta. È immutabile dalla nascita. La può aggiungere qualunque clinico.
- Annullamento: solo l'autore, motivazione obbligatoria. La nota resta leggibile e marcata.
- **Il database rifiuta** ogni modifica del contenuto di una nota finalizzata, e ogni cancellazione, con un trigger. Il servizio rifiuta prima, con un messaggio chiaro.
- L'autore viene **sempre dal token**, mai dalla richiesta. Vale anche per diagnosi e prescrizioni.
- Le note scritte dal Copilot nascono **sempre in bozza** e vanno firmate dal medico.
- Una bozza la modifica e la cancella solo il suo autore.
- **Bozza abbandonata** (autore disattivato, o nota mai firmata): nessuno può firmarla al posto dell'autore. Un altro clinico o il titolare può solo **annullarla con motivazione**: resta leggibile e marcata.
- **Note già esistenti** al momento del rilascio: diventano «storiche», cioè di sola lettura, con l'etichetta «precedente alla firma elettronica» e l'impronta calcolata alla migrazione, senza un autore della firma. Non è una firma automatica: è il congelamento dichiarato di ciò che c'era. Oggi in tutti gli ambienti sono dati fittizi. Nei dati d'esempio di demo e prova le note si rigenerano come firmate dal medico che le ha scritte. Scelta del coordinatore.
- **La nota diventa definitiva solo con la firma esplicita del medico (D4, opzione a)**: nessuna firma automatica, nessuna richiesta di firma alla chiusura della seduta.

**Interfaccia.**
- Ogni nota mostra il suo stato.
- Pulsante «Firma» sulle bozze dell'autore, con conferma esplicita: «Dopo la firma la nota non si può più modificare».
- Sulle note firmate: «Aggiungi addendum» e «Annulla nota».
- Le bozze non firmate si vedono in un elenco del medico («Note da firmare»). Non scadono e non si firmano da sole.

### 5.3 Segregazione per ruolo lato server (1.3)

**Matrice da raggiungere.** È la regola, non lo stato di oggi.

| Area | Clinici (dentista, igienista, ortodontista, chirurgo) | Segreteria |
|---|---|---|
| Anagrafica, contatti, appuntamenti (data, ora, poltrona, professionista, prestazione prevista), preventivi, fatture, visite di controllo | leggere e scrivere | leggere e scrivere |
| Diario, diagnosi, prescrizioni, anamnesi, odontogramma, episodi, seduta, analisi dei documenti | leggere e scrivere | **nessun accesso** |
| Allerte cliniche (allergie, farmaci) in agenda, dashboard e intestazione del paziente | vedere | **solo un segnale neutro «Allerta clinica», senza dettaglio** (D1) |
| Documenti del paziente | tutti | **solo «Consenso informato» e «Documento amministrativo»**: li vede e li carica. Mai documenti clinici, né le analisi AI (D2) |
| Piani di cura | leggere e scrivere | **nessun dettaglio** (D3). Vede il preventivo, che è un documento amministrativo; per la prenotazione dal piano vede solo nome e durata della prestazione, senza dente né note cliniche |
| Stato «eseguita» di una prestazione, «completato» di un appuntamento, chiusura e riapertura dell'episodio | sì (il «completato» viene dalla chiusura della seduta) | **no**. Può segnare «presente», «cancellato», «non presentato» (D3) |

Restano da decidere due casi:
- **Assistente alla poltrona (`assistant`)**: vede **solo ciò che riguarda la seduta in corso** (D6): prestazioni della seduta e allerte del paziente, per gli appuntamenti nello stato «in corso». Nient'altro di clinico, e non scrive dati clinici. **`other`**: come la segreteria (scelta del coordinatore).
- **Titolare dell'account** (`tenant_admin`). Fino a #126 S1 mantiene l'accesso di oggi. Con S1 vale la regola già decisa: per la cartella, il titolare non clinico vale come la segreteria.

**Come.**
- **Una sola policy nel codice**, per esempio `ClinicalAccessPolicy`, con la matrice. La usano sia la configurazione della sicurezza (per percorso e metodo) sia i servizi che restituiscono dati misti.
- **Dati misti filtrati alla fonte.** La scheda del paziente, l'agenda e la dashboard restituiscono alla segreteria DTO **senza** i campi clinici. Nasconderli nell'interfaccia non basta.
  - Sono **clinici**: tutto ciò che viene dall'anamnesi (allergie, farmaci, voci del catalogo, malattie), dalla seduta (esiti, note di seduta) e dagli episodi.
  - **Restano visibili** alla segreteria la prestazione prevista, il dente e le note dell'appuntamento. Prestazione e dente stanno già su preventivi e fatture, che la segreteria gestisce; le note dell'appuntamento sono il suo strumento quotidiano. Scelta del coordinatore.
  - Per le allerte la segreteria riceve solo un sì/no (`hasClinicalAlert`), mai il tipo né il testo (D1).
- Ogni rifiuto restituisce 403 e produce un evento `DENIED` con la regola (§5.1.5).
- **Test automatici per ruolo**: un test parametrico che chiama ogni endpoint del catalogo clinico con ogni ruolo e confronta l'esito con la matrice. È il criterio §26.2 della guida e la prova da mostrare al gate.
- Il frontend si allinea alla stessa matrice: nessuna scheda o sezione clinica raggiungibile dalla segreteria, nemmeno dall'indirizzo diretto.

### 5.4 Cancellazione logica (1.4)

**Tabelle.** Diario, diagnosi, prescrizioni, documenti, piani di cura e prestazioni del piano, pazienti.
- Nuove colonne `deleted_at`, `deleted_by`, `delete_reason`.
- Le letture normali escludono le righe cancellate.
- La cancellazione è registrata nel registro.

**Pazienti.**
- «Cancella» diventa cancellazione logica (D7):
  - paziente **senza dati clinici** (inserito per errore): lo cancella chiunque, come oggi;
  - paziente **con dati clinici**: solo il titolare o un clinico, con motivo obbligatorio, e mai se ha appuntamenti futuri;
  - il paziente cancellato sparisce da elenchi, ricerche, Giulia e Copilot; fatture e documenti fiscali restano;
  - il titolare lo ripristina dall'elenco «Pazienti cancellati».
- «Archivia» e «Ripristina» restano. L'elenco dei pazienti deve escludere davvero gli archiviati, salvo filtro esplicito.
- Il controllo dei dati collegati va verificato sulle tabelle attuali dell'odontogramma.

**Documenti.** Il file nell'archivio oggetti **non** si cancella con la cancellazione logica.

**Eliminazione fisica** (purge): procedura eccezionale e documentata, per esempio una richiesta motivata, oltre i tempi di conservazione. Non è una funzione dell'interfaccia, e lascia un evento nel registro.

**Fuori da qui:** l'odontogramma con storia arriva con il Blocco 2 (2.4). Fino ad allora le sue modifiche sono coperte dal registro, con i valori prima e dopo.

## 6. Parti di lavoro e agenti

Ogni parte passa per il revisore Opus, secondo il [metodo](../../04-Architecture-Handbook/16-Metodo-Sviluppo-Agenti.md).

| Parte | Contenuto | Implementatore | Dipende da | Stima |
|---|---|---|---|---|
| **A — Cuore del registro** | tabelle, trigger, `ClinicalAuditService`, impronte, sigilli HMAC con chiave derivata, verifica, eccezione per gli ambienti di prova, export del tenant in streaming | Opus | — | ~9-12h |
| **B — Registrazione delle letture** | filtro con catalogo dei percorsi, chiamate esplicite (Copilot, agenda, dashboard), eventi aggregati | Sonnet | A | ~6-9h |
| **C — Segregazione** | policy unica, configurazione della sicurezza, DTO filtrati (segnale neutro delle allerte, documenti amministrativi, piani senza dettagli), accesso dell'assistente legato alla seduta in corso, eventi `DENIED`, test parametrico per ruolo, allineamento del frontend | Opus | A | ~9-13h |
| **D — Note firmate** | stati, firma, addendum, annullamento, trigger, impronta, autore dal token, migrazione delle note esistenti a «storiche», interfaccia, «Note da firmare» | Opus (integrità) | A | ~8-11h |
| **E — Cancellazione logica** | colonne, filtri, pazienti (regole D7, elenco «Pazienti cancellati» e ripristino), documenti, registro | Sonnet | A | ~5-7h |
| **F — Avvisi** | regole, job, impostazioni, elenco degli avvisi e loro destinatari | Sonnet | A, B, C | ~3-5h |
| **G — Chiusura** | Academy (firma delle note, cosa vede la segreteria), `install.sql`, Architecture Handbook (07, 12, 13), registro DPIA | Sonnet | tutte | ~2-3h |

**Totale ≈ 42-60h agente.** La stima di luglio (~22-29h) non contava:
- i dati clinici misti in scheda paziente, agenda e dashboard;
- le scritture dello stato clinico fuori dalla seduta;
- le cancellazioni fisiche su sei tabelle;
- l'interfaccia di firma e degli avvisi.

**Ordine:**
1. A.
2. B e C in parallelo: file diversi, ma C usa il catalogo dei percorsi di B, quindi il catalogo si scrive per primo, dentro A.
3. D.
4. E.
5. F.
6. G.

## 7. Cosa resta al costruttore

- Nomi esatti di classi, colonne e indici, purché coerenti con §5.
- Forma canonica dell'impronta, riusando quella delle fotografie dell'episodio.
- Come il filtro ricava il paziente dal percorso, e come si propaga il `correlation_id` al thread del Copilot.
- Formato di `patient_ids` e di `before_values`/`after_values` (JSON).
- Struttura del test parametrico per ruolo.

## 8. Documentazione e privacy

- **Registro DPIA**, nuove voci D-xx in [06-Compliance](../../06-Compliance/dichiarazioni-dpia.md):
  - il registro degli accessi stesso, con campi, conservazione e chi lo vede;
  - i valori prima e dopo nelle modifiche;
  - gli avvisi e i loro destinatari;
  - la cancellazione logica e l'eliminazione eccezionale.
- **Architecture Handbook**, a lavoro fatto: 13 (da «non implementato» a implementato, con le scelte A2, B1, C e D1), 12 (stati delle note), 07 (matrice dei ruoli).
- **Academy**: lezioni su firma, addendum e annullamento, e su cosa vede la segreteria.

## 9. Come si verifica (definizione di fatto)

- [ ] Ogni consultazione e scrittura clinica del catalogo produce un evento completo dei campi minimi del Garante.
- [ ] `UPDATE`, `DELETE` e `TRUNCATE` sul registro e sui sigilli sono rifiutati dal database, al di fuori dell'eccezione per gli ambienti di prova.
- [ ] La verifica d'integrità segnala un evento alterato a mano nel database, anche se l'impronta dell'evento è stata ricalcolata.
- [ ] Una nota firmata non si modifica né si cancella, né via API né via SQL. L'addendum e l'annullamento funzionano.
- [ ] Il test parametrico per ruolo passa: la segreteria riceve 403 su ogni endpoint clinico, ogni rifiuto è registrato, e i DTO misti non contengono campi clinici.
- [ ] Nessuna cancellazione fisica dei dati clinici dall'applicazione.
- [ ] Gli avvisi scattano con le soglie impostate.
- [ ] Le voci DPIA sono scritte.

## 10. Decisioni del committente

Risposte del committente del 04/11/2026:

| # | Decisione | Risposta |
|---|---|---|
| D1 | La segreteria e le allerte cliniche | vede solo che c'è un'allerta clinica, senza il dettaglio |
| D2 | Documenti del paziente | solo documentazione amministrativa, mai clinica |
| D3 | Piani di cura | nessun dettaglio; vede il preventivo; per prenotare dal piano solo nome e durata della prestazione; non segna «eseguita» né «completato» |
| D4 | Quando una nota diventa definitiva | solo con la firma esplicita del medico |
| D5 | Chi riceve gli avvisi del registro | il titolare dello studio |
| D6 | Assistente alla poltrona | solo ciò che riguarda la seduta in corso |
| D7 | Chi può cancellare un paziente | senza dati clinici chiunque; con dati clinici titolare o clinico, con motivo, mai con appuntamenti futuri; ripristino dal titolare |

Le funzioni future del titolare dello studio (BI, interrogazioni in linguaggio naturale spiegabili, KPI d'uso) sono annotate a parte: il registro di questo blocco ne sarà una delle fonti.
