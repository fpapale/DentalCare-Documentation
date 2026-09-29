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

## 1.1 Scheda di seduta clinica e chiusura (#56-#62, #65, #67)

La **Scheda di seduta** è la schermata che usi mentre il paziente è in poltrona: dice **cosa fare
oggi** e registra **cosa è stato fatto**. Si apre dall'agenda con il pulsante **Seduta**; gli
appuntamenti già finiti della giornata sono in fondo alla vista *Prossimi*, sezione **«Già
trascorsi oggi»**.

### Iniziare la visita (#67)
Finché l'appuntamento non è «In corso», in alto compare **Inizia visita**. Premilo quando il
paziente si siede: il programma fotografa la sua situazione d'ingresso (anamnesi, diagnosi,
terapie, odontogramma, piani), che ritrovi nello **Storico episodi** (§2.1). Se registri la
seduta senza averla iniziata, la fotografia d'ingresso si scatta alla registrazione, prima degli
esiti, ed è segnata come *ingresso tardivo*.

### Registrare gli esiti
Per ogni prestazione prevista (con dente, superfici, piano e preventivo) scegli un esito, con
una nota facoltativa. Nessun esito è preselezionato; un secondo clic lo toglie.

| Esito | Effetto sul piano di cura |
|-------|---------------------------|
| **Eseguita** | completata, con data e nome di chi l'ha eseguita |
| **Rinviata** | resta aperta, da ripianificare |
| **Non eseguita** | resta aperta, con la motivazione nelle note |

### Aggiornare il dente (#65)
Su una prestazione **Eseguita** con un dente preciso compare il riquadro del dente: com'è **ora**
e, di partenza, **«L'odontogramma non cambia»**. Il dente non cambia mai da solo.
1. Se il listino prevede uno stato (**Lascia sul dente**), compare la **Proposta** (es.
   *Otturato*): premi **Applica**.
2. Oppure **Scegli altro** / **Aggiorna il dente** e indica lo stato: Otturato, Corona,
   Devitalizzato, Estratto, Mancante, Impianto, Da estrarre, Incluso, Pilastro o Elemento di
   ponte.
3. Per l'otturazione indica le **superfici** (O, M, D, B, L): se il piano le riporta sono già
   selezionate; senza superfici la registrazione si blocca.
4. **Lascia il dente com'è** annulla la scelta.

Il dente si aggiorna in odontogramma **a tuo nome e con il riferimento alla seduta**. Dalla
seduta non si segna una carie né si riporta un dente a sano: si fa dal tab Odontogramma.

### Registra seduta e Chiudi seduta (#60)
- **Registra seduta** dichiara gli esiti. Prima di confermare leggi il riepilogo: conteggio per
  esito, voce per voce, le righe dei denti (es. *Dente 37: Otturato su O, D*) e l'avviso delle
  prestazioni **senza esito**, che restano aperte. Una casella, **mai preselezionata**, chiude
  anche l'appuntamento.
- **Chiudi seduta** porta l'appuntamento a «Completata» anche quando non c'è nulla da
  dichiarare. A seduta chiusa compare **«Seduta chiusa»**.

Su una seduta chiusa non si registra più (si riapre dalla scheda paziente, se chiusa per errore);
su un appuntamento annullato il rifiuto è definitivo. Una prestazione già registrata come eseguita
non si modifica da qui: si interviene dal piano di cura.

### Chi può registrare (#62)
Solo i ruoli clinici (dentista, igienista, ortodontista, chirurgo) e gli amministratori. La
segreteria non vi accede: il confine è sul server. Non serve essere il medico dell'appuntamento:
aprendo la seduta di un collega compare l'avviso

> **Questa seduta è di Paolo Marchetti** — le prestazioni che segni come eseguite risulteranno
> *a tuo nome*, non al suo.

Se un collega registra nello stesso momento, alla conferma il sistema rifiuta una volta, dice
chi è stato e ricarica la scheda.

### Prestazioni rimaste in sospeso (#61)
Una prestazione passata per una seduta chiusa senza esito diventa **«In sospeso dal …»**. Ha due
sole destinazioni:
- **Riprogramma**: apre la prenotazione di una nuova seduta;
- **Togli dal piano**: con un **motivo obbligatorio** (rinuncia del paziente, non più
  necessaria, sostituita, inserita per errore, o testo libero). Non cancella nulla: la voce resta
  nel piano come *annullata*, con motivo, data e autore.

---

## 2. Scheda paziente

**Percorso** → **Pazienti → (cerca) → clic sul paziente**

La scheda è il centro del lavoro clinico. In alto i dati anagrafici, le **allerte** e, quando
c'è, l'episodio aperto (*Visita in corso dalle …* o *Contatto aperto* con **Chiudi contatto**);
sotto i **tab**:

| Tab | Cosa contiene |
|-----|---------------|
| **Anagrafica** | Dati, contatti e storico degli appuntamenti (stato modificabile dalla riga: fra gli stati **Presente** e **In corso**, che avvia la visita) |
| **Cartella clinica** | Diario clinico, visita per visita |
| **Storico episodi** | La situazione prima e dopo ogni visita e contatto (§2.1) |
| **Anamnesi** | Scheda clinica generale (patologie, allergie, farmaci) |
| **Odontogramma** | Mappa denti e condizioni |
| **Piani di cura** | Terapie previste e avanzamento |
| **Preventivi** | Preventivi del paziente |
| **Documenti** | Radiografie, referti, consensi, foto |

> La ricerca per **codice fiscale** funziona a **match esatto** (il CF è cifrato
> e indicizzato): digita il CF completo. La ricerca per nome/cognome è invece
> parziale.

**▶️ Prova nel demo:** **Pazienti**, apri un paziente (es. un cognome della lista),
scorri i tab.

### 2.1 Storico episodi (#67)

**Percorso** → **scheda paziente → tab Storico episodi** *(ruoli clinici e amministratori)*

Ogni **visita** (dall'«In corso» alla chiusura della seduta) e ogni **contatto fuori visita**
(telefonata, documento o RX esterno, altro) è un episodio. All'apertura e alla chiusura il
programma fotografa la situazione del paziente; le fotografie non si modificano più.

1. Scegli un episodio dall'elenco (filtro *Visite* / *Contatti*).
2. Leggi **cosa è cambiato** per area e l'**odontogramma prima e dopo**, con i denti cambiati
   evidenziati. A lato: prestazioni della seduta, note d'ingresso e d'uscita (**Aggiungi nota**),
   documenti e il **riepilogo** una riga per cambiamento (es. *Odontogramma: 36 O, M: carie →
   otturazione*), composto dai dati e non dall'AI.
3. **Confronta** mette a confronto la situazione dopo due episodi qualsiasi.

Avvisi: **Aperto** (manca ancora l'uscita), **Ingresso tardivo** (visita mai passata da «In
corso»), **Cambiato fuori episodio** (modifiche fatte senza episodio aperto).

**Quando il programma chiede di aprire un episodio.** Se salvi una modifica clinica
(odontogramma, anamnesi, diagnosi, prescrizioni, diario, documenti) senza episodio aperto, una
finestra propone: **Metti «in corso» la visita delle … e salva** (se il paziente ha un
appuntamento oggi), **Apri un contatto e salva** (tipo e motivo), **Salva fuori episodio** o
**Annulla**. Per un'urgenza senza appuntamento: crealo al momento e mettilo «In corso».

**▶️ Prova nel demo:** apri un paziente, **Storico episodi**, seleziona l'ultima visita e premi
**Confronta** con una precedente.

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

**Dalla seduta (#65):** gli stati confermati in scheda di seduta arrivano qui con autore e
seduta. Dal tab li puoi correggere (diventano manuali) o cancellare.

### Genera piano di cura (#66)
Il pulsante **Genera Piano di Cura** propone le prestazioni dall'odontogramma **salvato** (con
modifiche non salvate è disattivato).
1. Propone solo ciò che è **da fare**: carie (con le superfici, e la prestazione secondo quante
   sono: mono-, bi-, trifacciale), da estrarre, mancante, incluso. Corone, impianti, ponti e
   devitalizzati non si ripropongono.
2. Ciò che scarta resta visibile con il motivo: una carie su un dente mancante o da estrarre va
   in **Non proposte**; una prestazione già aperta sullo stesso dente parte **esclusa** («già nel
   piano …») e si riprende con **Aggiungi comunque**.
3. Le tendine offrono solo prestazioni ammesse per posizione e stato del dente.
4. **Nuovo piano** o **Aggiungi a piano esistente**: l'aggiunta avviene tutta insieme o per
   niente.

Le stesse regole valgono aggiungendo una prestazione dal tab **Piani di cura**: se non è ammessa,
il messaggio dice dente e motivo.

**▶️ Prova nel demo:** apri Odontogramma, clicca un dente, cambia condizione,
salva; poi **Genera Piano di Cura** e guarda proposte, esclusi e non proposte.

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

1. Apri **Prestazioni** (con ricerca e filtro per categoria).
2. Consulta/aggiorna una voce (nome, prezzo, categoria).
3. Le modifiche si riflettono su nuovi piani e preventivi.

Tre impostazioni guidano la parte clinica:
- **Lascia sul dente** (#65) — colonna dell'elenco: lo stato che la prestazione lascia sul dente,
  proposto in scheda di seduta. Salvataggio immediato; la modificano i ruoli clinici e
  l'amministratore.
- **Richiede il dente naturale** (#66) — casella nella scheda della prestazione: la prestazione
  non si propone su un dente mancante, estratto, impianto o elemento di ponte.
- **Default per condizione → Superfici** (#66) — per la carie, a quante superfici si applica una
  riga (1, 2, «3 o più»); le righe «qualsiasi» (es. radiografia) si aggiungono sempre.

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

## 13. Ambiente di prova e Academy (#69, #70)

**Ambiente di prova dello studio.** Pulsante **Ambiente di prova** in alto: si apre un ambiente
con pazienti e dati **inventati**, separato da quelli veri, per imparare o provare senza rischi.
La prima volta si prepara in circa mezzo minuto. Dentro vedi l'etichetta **Ambiente di prova** e
la fascia *non inserire dati di pazienti reali*; entri come il medico d'esempio. Per rientrare:
**Torna a …** con il nome dello studio. L'ambiente è condiviso con i colleghi e chiunque può
ripristinarne i dati d'esempio (pagina Academy).

**Academy.** Voce *Academy* nel menu: 23 lezioni brevi in sei moduli. **Prova ora** apre il punto
giusto dell'applicazione **nell'ambiente di prova**, mai sui pazienti veri; *Segna come completata*
aggiorna i tuoi progressi, che restano tuoi anche quando provi nell'ambiente di prova.

---

## Riepilogo giornata tipo (Dottoressa)

1. **Dashboard** → colpo d'occhio su appuntamenti e richiami.
2. **Agenda** → apri la **Scheda di seduta** e premi **Inizia visita** quando il paziente è in poltrona.
3. **Anamnesi** → verifica allergie/farmaci e alert clinici.
4. **Documenti → Analizza AI** → controlla l'ortopanoramica e i reperti rilevati.
5. **Odontogramma** → aggiorna condizioni cliniche per dente e superficie; **Genera piano** se serve.
6. **Scheda di seduta** → dichiara le prestazioni eseguite, conferma lo stato del dente, gestisci eventuali sospesi e chiudi la seduta.
7. **Diagnosi / Prescrizioni** → se necessario emetti ricetta o prescrizione.
8. **Storico episodi** → rileggi cosa è cambiato nella visita, aggiungi la nota d'uscita.
9. **Piano di cura → Preventivo** → verifica l'avanzamento e l'importo fatturabile.
10. **Agenda → Nuovo appuntamento** → fissa il controllo successivo collegato al piano.
