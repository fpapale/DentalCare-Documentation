# 01 — Guida Dottoressa (medico)

Guida clinica per il medico (dentista, igienista, ortodontista, chirurgo). Copre
la giornata tipo: dall'agenda alla visita, dall'odontogramma al piano di cura e
al preventivo, fino all'analisi AI delle radiografie e al Copilot.

**▶️ Account demo:** `ferretti@demo.dentalcare.it` — password demo fornita
dall'amministratore (Laura Ferretti, dentista).

---

## 0. Accesso e orientamento

1. Vai su `https://paaplef.duckdns.org:8181`.
2. Inserisci email `ferretti@demo.dentalcare.it` e la password demo (fornita
   dall'amministratore), premi **Accedi**.
3. Arrivi alla **Dashboard**: KPI della giornata (appuntamenti, richiami in
   scadenza, indicatori).

**Layout a tre colonne:** menu a sinistra · contenuto al centro · pannello destro
(KPI/scorciatoie) quando disponibile. Su schermi piccoli il pannello destro si
nasconde.

---

## 1. Agenda: la giornata clinica

**Percorso** → **Agenda**

L'agenda mostra gli appuntamenti per poltrona/medico. La Dottoressa la usa per
vedere i propri pazienti in programma e aprirne la scheda al volo.

1. Apri **Agenda**. Scegli la vista (giorno/settimana).
2. Clicca su un appuntamento per vederne i dettagli (paziente, prestazione, note).
3. Dal dettaglio appuntamento premi **Scheda di seduta** (o apri la scheda paziente) per iniziare la visita.
4. L'agenda si aggiorna **in tempo reale**: se la segreteria sposta un
   appuntamento mentre la tieni aperta, lo vedi senza ricaricare.

> Il medico può anche **creare** un appuntamento (**Agenda → Nuovo
> appuntamento**), utile per fissare il controllo successivo a fine visita. Se l'appuntamento nasce da un piano di cura, le prestazioni selezionate restano agganciate alla prenotazione.

**▶️ Prova nel demo:** apri Agenda, clicca un appuntamento esistente, poi
"Scheda di seduta".

---

## 1.1 Scheda di seduta clinica e chiusura (#56-#62)

La **Scheda di seduta** è il momento operativo in cui la pianificazione (l'appuntamento) incontra la clinica reale (il piano di cura).

### Chi può firmare l'atto clinico (#62)
Solo i ruoli clinici autorizzati (`dentist`, `hygienist`, `orthodontist`, `surgeon`, `tenant_admin`) possono registrare esiti o chiudere la seduta. La segreteria e gli utenti amministrativi puri non possono chiamare queste funzioni: il confine è blindato server-side.

### Visita svolta per conto di un collega
Se stai visitando un paziente in una seduta assegnata a un collega (sostituzione, urgenza o consulto), l'interfaccia mostra un avviso chiaro:
> *«Questa seduta è assegnata al Dr. Marchetti. Registrando, l'esecuzione risulterà a tuo nome.»*

Puoi procedere regolarmente senza attriti operativi, ma nel registro clinico e probatorio (`performed_by_provider_id`) risulterà con certezza il nome di chi ha effettivamente visitato ed eseguito la prestazione.

### Registrare le prestazioni ed esiti
Nella scheda di seduta trovi le prestazioni collegate previste dal piano:
1. Per ciascuna prestazione seleziona l'esito:
   - **Eseguita** (`completed`): la prestazione è stata completata;
   - **Parzialmente eseguita** (`partially_completed`);
   - **Non eseguita** (`not_performed`) o **Annullata** (`cancelled`).
2. Premi **Registra seduta**: il sistema aggiorna lo stato clinico nel piano di cura, associando autore e seduta d'origine.

### Azione autonoma «Chiudi seduta» (#60)
La chiusura della seduta è un'azione propria. Se hai già registrato le prestazioni o se non c'era nulla da dichiarare, premi direttamente **Chiudi seduta**. Una seduta chiusa o annullata non ammette ulteriori registrazioni retroattive per prevenire falsificazioni.

### Prestazioni rimaste in sospeso (#61)
Se chiudi una seduta lasciando prestazioni collegate senza esito completato, il sistema non le abbandona nel limbo:
- **Riprogramma**: assegna la prestazione a un nuovo appuntamento futuro;
- **Togli dal piano di cura**: stralcia la voce dal piano, richiedendo l'inserimento di una **motivazione clinica obbligatoria**. L'evento viene storicizzato in `treatment_plan_item_events`.

---

## 2. Scheda paziente

**Percorso** → **Pazienti → (cerca) → clic sul paziente**

La scheda è il centro del lavoro clinico. In alto i dati anagrafici; sotto i
**tab**:

| Tab | Cosa contiene |
|-----|---------------|
| **Panoramica** | Riepilogo: prossimi appuntamenti, ultime visite, avvisi |
| **Cartella clinica** | Storico visite e prestazioni erogate |
| **Odontogramma** | Mappa denti e condizioni |
| **Anamnesi** | Scheda clinica generale (patologie, allergie, farmaci) |
| **Documenti** | Radiografie, referti, consensi, foto |
| **Preventivi** | Preventivi del paziente |
| **Richiami** | Promemoria di controllo/igiene |
| **Fatture** | Documenti fiscali emessi |

> La ricerca per **codice fiscale** funziona a **match esatto** (il CF è cifrato
> e indicizzato): digita il CF completo. La ricerca per nome/cognome è invece
> parziale.

**▶️ Prova nel demo:** **Pazienti**, apri un paziente (es. un cognome della lista),
scorri i tab.

---

## 3. Anamnesi

**Percorso** → **scheda paziente → tab Anamnesi**

Prima di operare, controlla e aggiorna l'anamnesi.

1. Apri il tab **Anamnesi**.
2. Compila/aggiorna le sezioni: patologie (ipertensione, diabete, cardiopatie…),
   **allergie** (penicillina, lattice, anestetico…), farmaci in uso
   (anticoagulanti, bifosfonati, cortisone), abitudini (fumo, bruxismo…),
   gruppo sanguigno.
3. Salva. La scheda registra chi e quando ha aggiornato.

> Le allergie e gli anticoagulanti sono evidenziati come **avvisi clinici**:
> controllali sempre prima di prescrivere o operare.

---

## 4. Odontogramma

**Percorso** → **scheda paziente → tab Odontogramma**

Mappa dei denti con le condizioni per dente/superficie.

1. Seleziona un dente (numerazione FDI).
2. Imposta la **condizione** (carie, otturazione, corona, impianto, dente
   incluso, radice residua…) ed eventualmente la **superficie**.
3. Salva: la condizione compare colorata sull'odontogramma.

**Origine AI vs manuale:** i denti con condizione suggerita dall'**analisi AI**
di una radiografia hanno un **badge "AI"**. Se modifichi a mano una condizione
AI, il dente passa a **manuale** (ne prendi possesso). Le condizioni AI non
toccate restano marcate come AI.

**▶️ Prova nel demo:** apri Odontogramma, clicca un dente, cambia condizione,
salva; osserva il colore aggiornato.

---

## 5. Analisi AI delle radiografie

**Percorso** → **scheda paziente → tab Documenti → (apri un'ortopanoramica) →
Analizza con AI**

Il sistema analizza l'ortopanoramica con un modello di visione e propone i
riquadri (bounding box) delle evidenze.

1. Nel tab **Documenti** apri (o carica) un'**ortopanoramica**.
2. Premi **Analizza con AI** (o **Ri-analizza** per rifare).
3. Attendi l'esito: sull'immagine compaiono i **riquadri** delle evidenze con
   la classe (es. carie, lesione periapicale, dente incluso) e la confidenza %.
4. **Verde** = approvato, **ambra** = da verificare. Clicca un riquadro per
   confermare, rimuovere o cambiare classe.
5. Le evidenze confermate possono **sincronizzarsi sull'odontogramma** (con badge
   AI). Le tue correzioni alimentano il miglioramento del modello.

> L'immagine e le annotazioni **non escono dal server** (elaborazione locale) →
> conforme alla privacy.

---

## 6. Cartella clinica: registrare una visita

**Percorso** → **scheda paziente → tab Cartella clinica → Nuova visita**

1. Apri **Nuova visita**.
2. Indica data, prestazione/e erogata/e (dal listino), dente/i coinvolto/i,
   **note cliniche**, materiali usati, note per la visita successiva.
3. Salva: la visita entra nello **storico** della cartella clinica.
4. Da una visita puoi aprirne il **dettaglio** per rivederla o correggerla.

**▶️ Prova nel demo:** **Cartella clinica → Nuova visita**, compila una
prestazione con nota, salva; ricontrolla nello storico.

---

## 7. Diagnosi

**Percorso** → **scheda paziente → Diagnosi**

1. Apri **Diagnosi**.
2. Aggiungi una diagnosi: dente, titolo, descrizione, eventuale codice, stato
   (attiva/risolta).
3. Salva. La diagnosi resta collegata al paziente e alla cronologia clinica.

---

## 8. Prescrizioni

**Percorso** → **scheda paziente → Prescrizioni**

1. Apri **Prescrizioni**.
2. Compila la prescrizione (farmaco/indicazioni). **Controlla prima le allergie**
   in Anamnesi.
3. Salva/stampa per il paziente.

---

## 9. Piani di cura e preventivi

Il piano di cura raccoglie le prestazioni previste; da lì nasce il preventivo.

**Percorso** → **scheda paziente → Piano di cura** e **Preventivi**

1. Costruisci il **piano di cura** con le prestazioni previste (voci dal listino,
   quantità, dente).
2. Genera il **preventivo** dal piano ("**Genera piano/preventivo**").
3. Rivedi importi, sconti, IVA, validità.
4. Il preventivo mostra lo stato di avanzamento delle prestazioni eseguite (es. *"2 di 4 eseguite"*) e l'importo dinamico **Fatturabile** calcolato sulle sole prestazioni effettivamente completate in seduta.

> Il flusso economico completo (invio, accettazione, fattura a saldo o acconto) è tipicamente
> gestito **con la segreteria**: vedi [Guida Segretaria](02-Guida-Segretaria.md).

**▶️ Prova nel demo:** apri un preventivo esistente in **Preventivi** e osserva
le voci, gli importi e la colonna Avanzamento/Fatturabile.

---

## 10. Listino prestazioni

**Percorso** → **Prestazioni**

Il medico può consultare e gestire il **listino** (prestazioni, prezzi, default,
bundle) usato in piani di cura e preventivi.

1. Apri **Prestazioni**.
2. Consulta/aggiorna una voce (nome, prezzo, categoria).
3. Le modifiche si riflettono su nuovi piani e preventivi.

---

## 11. Copilot AI

**Percorso** → **Segreteria (Copilot AI)** — icona chat

Il Copilot è un assistente conversazionale: chiedi informazioni cliniche e
operative in linguaggio naturale.

Esempi di richieste:
- *"Mostrami i prossimi appuntamenti di oggi."*
- *"Apri la scheda del paziente Rossi."*
- *"Riassumi l'anamnesi del paziente selezionato."*
- *"Quali richiami scadono questa settimana?"*

> Con l'account **medico** il Copilot abilita anche gli **strumenti clinici**
> (letture su anamnesi, odontogramma, ecc.). Con l'account amministratore il
> Copilot **non** è disponibile (è pensato per chi opera su pazienti/agenda).

**▶️ Prova nel demo:** apri il Copilot e scrivi *"appuntamenti di oggi"*.

---

## 12. Gestione errori ed Errori intelligenti (#51, #54)

Quando un'azione non può essere completata (ad es. tentativo di registrare una prestazione già completata o modifica non consentita):
- Viene visualizzata una striscia di avviso in posizione fissa in alto.
- Con la funzione **Errori intelligenti** attiva, il messaggio tecnico incomprensibile (es. violazioni di integrità del database) viene tradotto istantaneamente dall'AI in un suggerimento chiaro in italiano che spiega cosa è accaduto e come risolvere.
- Il link *"Dettaglio tecnico"* resta sempre disponibile per visualizzare il codice errore esatto (es. `SESSION_ALREADY_CLOSED`, `SESSION_ITEM_ALREADY_PERFORMED`) utile per l'assistenza IT.

---

## Riepilogo giornata tipo (Dottoressa)

1. **Dashboard** → colpo d'occhio su appuntamenti e richiami.
2. **Agenda** → apri la **Scheda di seduta** del paziente.
3. **Anamnesi** → verifica allergie/farmaci e alert clinici.
4. **Documenti → Analizza AI** → controlla l'ortopanoramica e i reperti rilevati.
5. **Odontogramma** → aggiorna condizioni cliniche per dente e superficie.
6. **Scheda di seduta** → dichiara le prestazioni eseguite, gestisci eventuali sospesi e chiudi la seduta.
7. **Diagnosi / Prescrizioni** → se necessario emetti ricetta o prescrizione.
8. **Piano di cura → Preventivo** → verifica l'avanzamento e l'importo fatturabile.
9. **Agenda → Nuovo appuntamento** → fissa il controllo successivo collegato al piano.
