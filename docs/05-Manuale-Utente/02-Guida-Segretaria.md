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
> prescrizioni): quei tab sono in sola lettura o nascosti. Vede però tutto ciò
> che serve al front-office.

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
2. Modifica orario o stato (confermato, in corso, annullato…). Per l'annullamento
   indica la **motivazione**.
3. Le modifiche sono **immediate**: i medici che tengono l'agenda aperta le vedono
   in tempo reale.

> Gli appuntamenti creati dall'assistente telefonico/AI (se attivo) arrivano nella
> stessa agenda: nessuna doppia gestione.

**▶️ Prova nel demo:** crea un appuntamento per il paziente di test, poi spostalo
di un'ora.

---

## 3. Richiami (recall)

**Percorso** → **Richiami** (anche dal tab **Richiami** della scheda paziente)

I richiami sono i promemoria di controllo/igiene periodici.

1. Apri **Richiami**: vedi l'elenco con le **scadenze**.
2. Filtra per periodo/stato per capire chi va contattato.
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

## 5. Fatturazione

**Percorso** → **Fatturazione**

1. Apri **Fatturazione**: elenco documenti (fatture, note) con stato e importi.
2. Crea una fattura (tipicamente da un preventivo accettato / prestazioni erogate):
   controlla dati emittente e paziente, voci, imponibile, IVA, totale.
3. Registra pagamento e metodo quando incassi.
4. Apri il **dettaglio fattura** per rivedere o stampare.

> **Nota fiscale:** le fatture non si eliminano insieme al paziente (obbligo di
> conservazione). Restano nel sistema anche se il paziente viene rimosso.

**▶️ Prova nel demo:** apri **Fatturazione**, entra in una fattura e osserva le
voci e il totale.

---

## 6. Magazzino

**Percorso** → **Magazzino**

Gestione scorte dei materiali di studio.

1. Apri **Magazzino**: elenco prodotti con **giacenza** e soglie.
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

## Riepilogo giornata tipo (Segretaria)

1. **Dashboard** → richiami in scadenza e agenda del giorno.
2. **Agenda** → conferma/riorganizza gli appuntamenti.
3. **Pazienti → Nuovo paziente** → registra i nuovi arrivi.
4. **Richiami** → contatta chi è in scadenza e fissa i controlli.
5. **Preventivi** → invia e registra accettazioni.
6. **Fatturazione** → emetti e incassa.
7. **Magazzino** → registra consumi e riordini.
