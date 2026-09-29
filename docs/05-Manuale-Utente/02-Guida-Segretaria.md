# 02 — Guida Segretaria (front-office)

Guida per la segreteria: gestione appuntamenti, anagrafica pazienti, richiami,
preventivi da inviare, fatturazione e magazzino. È il ruolo che **apre** il
paziente nel sistema e coordina agenda e parte economica.

**▶️ Account demo:** `segreteria@demo.dentalcare.it` — password demo fornita
dall'amministratore (Maria Rossi, segretaria).

---

## 0. Accesso

1. Vai su `https://paaplef.duckdns.org:8181`.
2. Accedi con `segreteria@demo.dentalcare.it` e la password demo (fornita
   dall'amministratore).
3. Arrivi alla **Dashboard** con i KPI della giornata.

> La segreteria **non** accede alla parte clinica (cartella clinica, diagnosi,
> prescrizioni, **Storico episodi**, **scheda di seduta**): quei tab sono in sola lettura o
> nascosti, e il confine è verificato dal server. Non vede nemmeno la finestra che chiede di
> aprire un episodio clinico: quella riguarda i medici. Vede però tutto ciò che serve al
> front-office.

---

## 1. Nuovo paziente (anagrafica)

**Percorso** → **Pazienti → Nuovo paziente**

La registrazione anagrafica è compito della segreteria.

1. Apri **Pazienti → Nuovo paziente**.
2. Compila: nome, cognome, **data di nascita**, **codice fiscale**, telefono,
   email, indirizzo.
3. **Paziente straniero:** se non ha CF italiano, spunta la casella
   *paziente straniero* → il CF diventa opzionale e non viene validato.
4. **Validazione CF italiano:** il formato viene controllato e, se possibile,
   confrontato con la data di nascita (anno/mese/giorno). Se non coincide,
   compare un errore.
5. Salva. Il paziente entra in anagrafica ed è subito prenotabile.

> **Privacy:** data di nascita e codice fiscale vengono **cifrati** nel database.
> Nell'app restano leggibili; nel DB sono protetti.

**▶️ Prova nel demo:** crea un paziente di test (es. "Mario Verdi"), poi cercalo
in **Pazienti**.

---

## 2. Agenda e appuntamenti

**Percorso** → **Agenda** e **Agenda → Nuovo appuntamento**

### Creare un appuntamento
1. Apri **Agenda → Nuovo appuntamento**.
2. Scegli **paziente**, **medico/poltrona**, **data e ora**, **prestazione**,
   eventuali **note**.
3. Salva: l'appuntamento compare in agenda.

### Spostare / modificare / annullare
1. In **Agenda** clicca l'appuntamento.
2. Modifica orario o stato (confermato, presente, annullato…). Per l'annullamento
   indica la **motivazione**.
3. Le modifiche sono **immediate**: i medici che tengono l'agenda aperta le vedono
   in tempo reale.

### Presente e In corso (#67)
Quando il paziente arriva in studio, segnalalo come **Presente** (anche dallo storico appuntamenti in
fondo alla scheda paziente). **In corso** significa che è in poltrona: di solito lo mette il medico
con **Inizia visita**, perché in quel momento il programma fotografa la situazione clinica
d'ingresso. Per un'urgenza senza appuntamento: crea l'appuntamento al momento, poi il medico lo
porta «In corso».

> Gli appuntamenti creati dall'assistente telefonico/AI (se attivo) arrivano nella
> stessa agenda: nessuna doppia gestione.

**▶️ Prova nel demo:** crea un appuntamento per il paziente di test, poi spostalo
di un'ora.

---

## 3. Richiami (recall)

**Percorso** → **Richiami** (anche dal tab **Richiami** della scheda paziente)

I richiami sono i promemoria di controllo/igiene periodici.

1. Apri **Richiami**: vedi l'elenco con le **scadenze**.
2. Filtra per periodo/stato o **cerca** per nome per capire chi va contattato. Clic
   sull'intestazione di una colonna per ordinarla (le date partono dalle più urgenti).
3. Da un richiamo puoi contattare il paziente e, dopo il contatto,
   aggiornarne lo stato o fissare l'appuntamento.
4. Per creare un richiamo dedicato: apri la **scheda paziente → tab Richiami** e
   aggiungi il promemoria (tipo controllo, data prevista).

**▶️ Prova nel demo:** apri **Richiami**, filtra "questa settimana", apri un
paziente in scadenza.

---

## 4. Preventivi

**Percorso** → **Preventivi** (e scheda paziente → tab Preventivi)

La segreteria gestisce l'iter del preventivo verso il paziente.

1. Apri **Preventivi**: elenco con stato (bozza, inviato, accettato, rifiutato).
2. Apri un preventivo per vederne le **voci**, gli **importi**, gli **sconti**,
   l'**IVA** e la **validità**.
3. **Invia** il preventivo al paziente.
4. Registra l'esito: **accettato** o **rifiutato**. Un preventivo accettato è la
   base per la **fattura**.

> Le prestazioni e i prezzi provengono dal **listino** (gestito da
> medico/amministratore). La segreteria non modifica il listino.

**▶️ Prova nel demo:** apri un preventivo esistente e simula l'invio.

---

## 5. Fatturazione e incassi (#50, #52, #53)

**Percorso** → **Fatturazione** (e scheda paziente → tab Fatture)

1. Apri **Fatturazione**: visualizzi l'elenco dei documenti emessi, gli stati e gli importi.
   Ogni colonna si ordina con un clic sull'intestazione: date e importi partono dal più
   recente/alto, le celle vuote restano in fondo, gli stati seguono il ciclo di vita (Bozza →
   Emessa → Pagata). Lo stesso vale per **Preventivi**, **Richiami** e **Magazzino**. I KPI
   tengono separato lo stornato.
2. Premi **+ Nuovo documento** e seleziona la tipologia corretta:
   - **Fattura a saldo (da piano/preventivo)**: emette la fattura solo per le prestazioni che il medico ha **già completato in seduta clinica** (#50). Il sistema calcola l'importo fatturabile effettivo ed impedisce la fatturazione anticipata di prestazioni cliniche non ancora eseguite.
   - **Acconto**: permette di emettere una fattura per un anticipo concordato con il paziente, prima dell'esecuzione delle cure.
   - **Nota di credito (#52)**: serve per stornare **per intero** una fattura emessa. Non si crea da zero: si apre la fattura da rettificare e si preme **Storna con nota di credito** (causale facoltativa). Il sistema genera il documento di pari importo con segno invertito, numerato nella serie `NC-` e collegato alla fattura, che passa ad *Annullata* ma resta in archivio. Ogni fattura si storna una sola volta.
3. **Regola di conservazione fiscale e non eliminabilità**:
   - Una fattura o nota di credito **emessa non si elimina mai**: l'azione "Elimina" è consentita solo per le **bozze**.
   - **Numerazione (#63)**: il numero si assegna all'emissione, dopo l'ultimo emesso. Una bozza eliminata non è mai entrata nella sequenza, quindi non lascia buchi e non fa riusare numeri.
   - I preventivi e i piani di cura collegati a documenti fiscali emessi non possono essere cancellati, per garantire la tracciabilità probatoria e fiscale.
4. Registra pagamento e metodo quando incassi (contanti, POS, bonifico).

> **Confine tra segreteria e atto clinico (#62):** La segreteria emette fatture e gestisce i pagamenti, ma **non ha accesso alla registrazione della Scheda di Seduta** (eseguito/non eseguito). Questo confine è garantito dal server (`CLINICAL_WRITE_ROLES`): solo i professionisti clinici possono firmare l'atto sanitario.

**▶️ Prova nel demo:** apri **Fatturazione**, entra in una fattura e osserva le
voci e il totale; prova a creare una nota di credito da una fattura emessa.

---

## 6. Magazzino

**Percorso** → **Magazzino**

Gestione scorte dei materiali di studio.

1. Apri **Magazzino**: elenco prodotti con **giacenza** e soglie, ordinabile per colonna.
2. Registra un **movimento**: carico (nuovo arrivo) o scarico (consumo).
3. Tieni d'occhio i prodotti **sotto scorta** per riordinare in tempo.

**▶️ Prova nel demo:** apri **Magazzino**, registra un carico di un prodotto e
verifica la giacenza aggiornata.

---

## 7. Copilot AI

**Percorso** → **Segreteria (Copilot AI)**

L'assistente conversazionale aiuta nelle attività di front-office.

Esempi:
- *"Che appuntamenti ci sono domani mattina?"*
- *"Sposta l'appuntamento di Rossi alle 15."*
- *"Quali pazienti hanno un richiamo in scadenza?"*
- *"Crea un preventivo per il paziente selezionato con una pulizia."*

> Il Copilot esegue letture e, con i permessi giusti, **scrive** sui moduli
> (agenda, preventivi…). Verifica sempre l'esito prima di confermare col paziente.

**▶️ Prova nel demo:** apri il Copilot e scrivi *"appuntamenti di domani"*.

---

## 8. Ambiente di prova e Academy (#69, #70)

**Ambiente di prova dello studio.** Pulsante **Ambiente di prova** in alto: si apre un ambiente
con pazienti e dati **inventati**, separato da quelli veri. Serve per imparare o far pratica
(nuovo appuntamento, preventivo, fattura) senza toccare i pazienti reali. Entri come la
segreteria d'esempio; in alto restano l'etichetta **Ambiente di prova** e la fascia *non inserire
dati di pazienti reali*. Per rientrare: **Torna a …** con il nome dello studio. L'ambiente è
condiviso con i colleghi: ripristinarlo (pagina Academy) cancella anche ciò che hanno fatto loro.

**Academy.** Voce *Academy* nel menu: lezioni brevi su pazienti, agenda, preventivi, fatturazione,
richiami, magazzino e Copilot. **Prova ora** apre il punto giusto **nell'ambiente di prova**;
*Segna come completata* aggiorna i tuoi progressi.

---

## Riepilogo giornata tipo (Segretaria)

1. **Dashboard** → richiami in scadenza e agenda del giorno.
2. **Agenda** → conferma/riorganizza gli appuntamenti; segna **Presente** chi arriva.
3. **Pazienti → Nuovo paziente** → registra i nuovi arrivi.
4. **Richiami** → contatta chi è in scadenza e fissa i controlli.
5. **Preventivi** → invia e registra accettazioni.
6. **Fatturazione** → emetti e incassa.
7. **Magazzino** → registra consumi e riordini.
