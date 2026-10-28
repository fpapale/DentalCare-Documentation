# DentalCare Pro — Guida per la segreteria

> Versione 28 ottobre 2026. Generato dalle lezioni dell'**Academy**, il manuale ufficiale dentro il programma (`tools/genera_manuale.py`): per correggerlo si corregge la lezione e si rigenera. Le schermate vengono dall'ambiente dimostrativo: nomi e dati dei pazienti sono fittizi.

Il percorso dice cosa fare e in che ordine; le lezioni che richiama seguono, nell'ordine in cui compaiono. Il resto è nel [manuale integrale](MANUALE_UTENTE.md).

## Indice

- [Percorso della segreteria](#lezione-percorso-segreteria)
- [L'interfaccia in un minuto](#lezione-interfaccia)
- [La dashboard](#lezione-dashboard)
- [Trovare un paziente](#lezione-cercare-paziente)
- [Registrare un nuovo paziente](#lezione-nuovo-paziente)
- [Le viste dell'agenda](#lezione-viste-agenda)
- [Fissare un appuntamento](#lezione-nuovo-appuntamento)
- [Gestire gli appuntamenti](#lezione-gestire-appuntamenti)
- [Dal paziente in sala alla visita in corso](#lezione-inizia-visita)
- [Preventivi e avanzamento](#lezione-preventivi)
- [Fatture, acconti e storni](#lezione-fatturazione)
- [I richiami](#lezione-richiami)
- [Il magazzino](#lezione-magazzino)
- [Paziente non presentato](#lezione-paziente-non-presentato)
- [Spostare o annullare un appuntamento collegato](#lezione-spostare-appuntamento-collegato)
- [I vincoli dell'agenda](#lezione-vincoli-agenda)
- [Chiedere al Copilot](#lezione-copilot)

---

<a id="lezione-percorso-segreteria"></a>

## 2.1 Percorso della segreteria

*Agenda, accoglienza, preventivi, incassi e richiami, giorno per giorno.*

Il percorso di chi organizza lo studio: telefono, agenda, accoglienza, preventivi, incassi e richiami. Segui le tappe nell'ordine: ogni tappa rimanda alla lezione che la spiega.

**Per:** segreteria. Nell'ambiente di prova scegli **Segreteria** nel menu in alto.

#### 1. Le basi (primo giorno)

1. [L'interfaccia in un minuto](#lezione-interfaccia) e [La dashboard](#lezione-dashboard).
2. [Trovare un paziente](#lezione-cercare-paziente) e [Registrare un nuovo paziente](#lezione-nuovo-paziente): la registrazione è un tuo compito.
3. [Le viste dell'agenda](#lezione-viste-agenda) e [Fissare un appuntamento](#lezione-nuovo-appuntamento).

#### 2. La giornata tipo

| Momento | Cosa fai | Lezione |
|---|---|---|
| Apertura | dashboard: appuntamenti di oggi, allerte, scadenze e pazienti **da avvisare** (prenotazioni fatte da Giulia al telefono) | [La dashboard](#lezione-dashboard) |
| Mattina | conferme telefoniche: lo stato passa a *Confermato* | [Gestire gli appuntamenti](#lezione-gestire-appuntamenti) |
| Arrivo del paziente | lo segni **Presente**: il medico sa che è in sala | [Dal paziente in sala alla visita](#lezione-inizia-visita) |
| Telefonate | nuovi appuntamenti, spostamenti, annullamenti; dopo ognuno, *Avvisa il paziente* (WhatsApp o e-mail) | [Gestire gli appuntamenti](#lezione-gestire-appuntamenti) |
| Uscita del paziente | preventivo, acconto o fattura | [Preventivi](#lezione-preventivi), [Fatture](#lezione-fatturazione) |
| Pomeriggio | richiami da contattare: telefono, oppure il testo pronto per e-mail o WhatsApp | [I richiami](#lezione-richiami) |

#### 3. La settimana e il mese

- Preventivi **inviati** senza risposta e preventivi **fatturabili** (lavoro finito, non ancora fatturato): [Preventivi e avanzamento](#lezione-preventivi).
- Documenti da emettere, acconti, note di credito: [Fatture, acconti e storni](#lezione-fatturazione).
- Generazione dei richiami e contatti: [I richiami](#lezione-richiami).
- Scorte e carichi di magazzino: [Il magazzino](#lezione-magazzino).

#### 4. I casi particolari

- Il paziente non si presenta: [Paziente non presentato](#lezione-paziente-non-presentato).
- Spostare un appuntamento legato a un piano di cura, o cambiare medico: [Spostare o annullare un appuntamento collegato](#lezione-spostare-appuntamento-collegato).
- L'orario chiesto non è libero, è fuori orario o non è sulla griglia: [I vincoli dell'agenda](#lezione-vincoli-agenda).
- Una fattura da correggere: [Fatture, acconti e storni](#lezione-fatturazione).

#### 5. Il Copilot come aiuto

Per te il Copilot è **amministrativo**: trova orari liberi, sposta appuntamenti (con conferma), dice chi richiamare. Non dà indicazioni cliniche. [Chiedere al Copilot](#lezione-copilot).

#### Prova nel programma

Scegli **Segreteria** nel menu in alto, apri la dashboard e segui la tabella della giornata tipo dall'inizio alla fine.

<a id="lezione-interfaccia"></a>

## 1.2 L'interfaccia in un minuto

*Menu, contenuto, pannello laterale, spazio sul tablet e striscia degli errori.*

![La segnalazione di un errore: cosa, perché e cosa fare.](img/academy/20-pannello-errori.png)

*La segnalazione di un errore: cosa, perché e cosa fare.*

Ogni schermata di DentalCare Pro ha la stessa struttura: dopo cinque minuti sai sempre dove guardare.

**Per:** tutti.

#### Le tre zone

- **Menu a sinistra**: Academy, Dashboard, Copilot AI, Agenda, Pazienti, Preventivi, Fatturazione, Richiami, Magazzino, Prestazioni e Impostazioni (per medici e igienisti solo le schede personali: tariffe, richiami, fatturazione e calendario). Le voci cambiano con il ruolo: la segreteria non vede ciò che è solo clinico.
- **Contenuto al centro**: la sezione in cui stai lavorando.
- **Pannello a destra**, sugli schermi larghi: indicatori e scorciatoie della sezione (per esempio i richiami urgenti o le scorte in esaurimento).

In alto trovi il nome dello studio, la data di oggi, il menu del punto di vista (nell'ambiente di prova) e, a destra, il tuo nome: cliccandolo puoi uscire.

#### Più spazio sul tablet

- **Riduci menu**, in fondo al menu, lo riduce alle sole icone; lo stesso pulsante lo riallarga.
- Il pulsante in alto nel pannello destro lo **nasconde**; una striscia sottile sul bordo lo riapre.

Le due scelte restano memorizzate sul dispositivo: sul tablet puoi lavorare con menu ridotto e pannello nascosto, sul computer con tutto aperto.

#### Quando qualcosa non va

Se un'operazione non riesce compare una **striscia rossa in fondo alla schermata**, sempre nello stesso punto. Dice tre cose:

1. **cosa** non è riuscito;
2. **perché**, con i dati concreti che lo impediscono (per esempio il numero della fattura collegata);
3. **cosa fare**, quando c'è un'alternativa.

La striscia resta finché non la chiudi con la ✕. Se l'amministratore ha attivato gli **errori intelligenti** (Impostazioni → Sistema), il messaggio tecnico viene riscritto in linguaggio semplice; il testo originale resta sotto *Dettaglio tecnico*, ed è quello da riportare all'assistenza insieme a orario e codice.

#### Prova nel programma

Riduci il menu, passa da una sezione all'altra e osserva come cambia il pannello a destra. Poi riallarga il menu.

<a id="lezione-dashboard"></a>

## 1.3 La dashboard

*Indicatori, prossimi appuntamenti, allerte e scadenze.*

![La dashboard: indicatori, prossimi appuntamenti e scheda dell'appuntamento scelto.](img/academy/02-segreteria-dashboard.png)

*La dashboard: indicatori, prossimi appuntamenti e scheda dell'appuntamento scelto.*

La dashboard è la prima schermata dopo l'accesso: in un colpo d'occhio dice com'è la giornata e cosa aspetta una decisione.

**Per:** tutti. Il medico vede i propri appuntamenti, la segreteria e l'amministratore l'intero studio.

#### Gli indicatori in alto

- **Pazienti** e **Oggi**: quanti pazienti segue lo studio e quanti appuntamenti ci sono oggi.
- **Preventivi inviati**: offerte consegnate e in attesa di risposta.
- **Piani attivi**, divisi in *Bozza*, *Da decidere*, *Accettati*, *Rifiutati*. Molti piani *da decidere* sono lavoro che aspetta il paziente.
- **Occupazione oggi**: quanto sono piene le poltrone, con previsti, completati e annullati.

#### Da avvisare

Compare solo quando c'è qualcosa da fare: i pazienti a cui va comunicata una **prenotazione**, uno **spostamento** o una **cancellazione** e che nessuno ha ancora avvisato. Ci finiscono le operazioni fatte da **Giulia** al telefono (l'e-mail l'ha già mandata lei: resta da decidere WhatsApp) e quelle per cui qualcuno ha scelto «Più tardi». **Avvisa** apre la finestra [Avvisa il paziente](#lezione-gestire-appuntamenti); se gli avvisi sono più d'uno, **Avvisa uno dopo l'altro** li propone in fila.

#### Prossimi appuntamenti

L'elenco degli appuntamenti da ora in poi, con orario, paziente, prestazione, poltrona e stato. Le icone avvisano di un'**allerta clinica** (⚠), di una terapia in corso o di un **richiamo scaduto**. I pulsanti *Programmato*, *Confermato*, *Presente* filtrano l'elenco per stato.

Cliccando un appuntamento, a destra compare la sua scheda: motivo, trattamento, orario e poltrona, **alert clinici**, contatti del paziente e **scadenze** (richiami scaduti, preventivi in attesa). È il riassunto da leggere prima di chiamare il paziente o di farlo accomodare.

#### Da sapere

- Quante righe mostrare e quanti giorni considerare lo decide l'amministratore in Impostazioni → Sistema.
- Il menu del punto di vista (lezione successiva) cambia anche la dashboard: come segreteria vedi tutto lo studio.

#### Prova nel programma

Apri la dashboard, clicca il primo appuntamento della giornata e controlla se il paziente ha un'allerta clinica o una scadenza.

<a id="lezione-cercare-paziente"></a>

## 3.1 Trovare un paziente

*Ricerca, filtri e cosa dice ogni riga dell'elenco.*

![L'elenco dei pazienti.](img/academy/04-segreteria-pazienti.png)

*L'elenco dei pazienti.*

La sezione **Pazienti** è l'elenco di tutte le persone seguite dallo studio.

**Per:** tutti.

#### Come si cerca

Scrivi nome o cognome nella barra in alto: l'elenco si aggiorna mentre digiti. Puoi cercare anche per **codice fiscale**, scritto per intero: è cifrato nel database, e la ricerca lo confronta in modo esatto.

I filtri rapidi dividono i pazienti in **Tutti**, **Attivi** (con appuntamenti recenti) e **Archiviati**.

#### Cosa dice ogni riga

Iniziali o foto, nome, età, telefono ed e-mail. Un clic apre la **scheda paziente**, il punto di partenza di quasi tutto il lavoro clinico.

#### Prova nel programma

Apri l'elenco, cerca **Rossi** e apri la scheda di *Marco Rossi*: lo ritroverai in diverse lezioni.

<a id="lezione-nuovo-paziente"></a>

## 3.2 Registrare un nuovo paziente

*I tre passi dell'anagrafica e il codice fiscale.*

Registrare un paziente richiede un minuto, in tre passi.

**Per:** segreteria e amministratore.

#### Prima di cominciare

La registrazione è un compito della **segreteria**: se stai guardando lo studio come medico, scegli **Segreteria** (o **Amministratore**) nel menu in alto. Il pulsante **+ Nuovo paziente** compare in alto nell'elenco dei pazienti.

#### I tre passi

1. **Dati anagrafici** — cognome, nome, data di nascita, sesso e codice fiscale. Il codice fiscale viene controllato mentre lo scrivi; per un paziente straniero senza codice italiano c'è l'apposita opzione.
2. **Contatti** — telefono (obbligatorio), e-mail e indirizzo.
3. **Dati clinici** — note e le allergie principali. L'anamnesi completa si compila dopo, dalla scheda.

Premi **Salva** nell'ultimo passo.

#### Da sapere

Data di nascita e codice fiscale sono **cifrati** nel database, con una chiave diversa per ogni studio: sono i dati personali più delicati dell'anagrafica.

#### Prova nel programma

Registra un paziente inventato (per esempio *Mario Prova*, nato il 1° gennaio 1980) e cercalo nell'elenco. Ricorda: niente dati di pazienti veri.

<a id="lezione-viste-agenda"></a>

## 4.1 Le viste dell'agenda

*Prossimi, giorno, settimana, mese; stati, filtri e griglia degli slot.*

![La vista Giorno: una colonna per poltrona, i pulsanti per scegliere le poltrone mostrate, una riga tratteggiata per ogni slot.](img/academy/03-segreteria-agenda.png)

*La vista Giorno: una colonna per poltrona, i pulsanti per scegliere le poltrone mostrate, una riga tratteggiata per ogni slot.*

L'agenda mostra gli appuntamenti dello studio in quattro modi, scelti dalla barra in alto.

**Per:** tutti. Il medico e l'igienista vedono i propri appuntamenti; segreteria e amministratore l'intero studio.

#### Le viste

- **Prossimi** — gli appuntamenti da ora in poi, in ordine di orario, con il pulsante **Seduta** per i ruoli clinici. In fondo, **Già trascorsi oggi** raccoglie quelli finiti: è il posto dove registrare le sedute a fine mattinata.
- **Giorno** — la griglia oraria, una colonna per poltrona. Le ore sono quelle di lavoro dello studio e una linea tratteggiata segna ogni **slot** (per esempio ogni 15 minuti). La linea rossa è l'ora attuale. Le poltrone sono quelle attive della clinica, nell'ordine e con i colori dell'anagrafica ([Impostazioni → Anagrafiche → Poltrone](MANUALE_UTENTE.md#lezione-impostazioni-studio)). Se non ci stanno tutte, l'agenda scorre in orizzontale e la colonna degli orari resta ferma; con i pulsanti **Poltrone** sopra la griglia scegli quali mostrare (la scelta resta su quel computer o tablet).
- **Settimana** — i giorni della settimana affiancati, con la stessa griglia oraria; un clic sull'intestazione di un giorno lo apre in vista Giorno.
- **Mese** — il calendario con gli appuntamenti di ogni giorno; un clic apre quel giorno.

#### Muoversi

- Le frecce ◀ ▶ spostano avanti e indietro di un giorno, una settimana o un mese, secondo la vista.
- L'icona del calendario apre un selettore di date, con **Oggi** in fondo; quando non sei su oggi compare anche il pulsante **Oggi** accanto alle frecce.
- **+ Appuntamento**, in alto a destra, apre la [prenotazione](#lezione-nuovo-appuntamento).

#### Stati e filtri

I pulsanti colorati sotto la barra (**Programmato**, **Confermato**, **Presente**) sono **filtri**: cliccandoli mostri o nascondi gli appuntamenti in quello stato. Nella griglia ogni blocco ha il colore del suo stato:

| Colore | Stato |
|---|---|
| Giallo | programmato, da confermare |
| Blu | confermato |
| Verde | in corso |
| Grigio | completato |
| Rosso | cancellato o paziente non presentato |

Un ⚠ accanto al nome segnala un'**allerta clinica** del paziente.

#### Da sapere

- L'agenda segue le impostazioni dello studio: **orario di lavoro**, **giorni lavorativi** e **durata dello slot** (Impostazioni → Agenda). Cambiandoli cambia la griglia.
- I giorni festivi sono evidenziati: non si possono prenotare.
- Gli appuntamenti non si spostano trascinandoli: si modificano dalla scheda del paziente o con il Copilot. Lo spiega [Gestire gli appuntamenti](#lezione-gestire-appuntamenti).

#### Prova nel programma

Apri l'agenda, passa alla vista **Settimana** e trova il giorno più pieno. Aprilo in vista **Giorno** e guarda dove cadono le linee degli slot.

<a id="lezione-nuovo-appuntamento"></a>

## 4.2 Fissare un appuntamento

*Orari a slot, durata, Proponi orario e prenotazione dal piano.*

![Un nuovo appuntamento: orari a passi di slot e primi orari liberi proposti.](img/academy/35-nuovo-appuntamento.png)

*Un nuovo appuntamento: orari a passi di slot e primi orari liberi proposti.*

Un appuntamento si fissa da **+ Appuntamento** in agenda, da **+ Nuovo** nella scheda del paziente o, meglio ancora, dal piano di cura con l'icona **Pianifica appuntamento** (il calendario con la spunta) accanto alla prestazione.

**Per:** segreteria, medici, igienisti. Un medico prenota per sé: il suo nome è già scelto.

#### I campi

1. **Paziente** — scrivi almeno due lettere del nome o del cognome e scegli dall'elenco.
2. **Prestazione** — facoltativa, ma utile: porta con sé la **durata** e fa partire subito la ricerca del primo orario libero.
3. **Data** e **Ora** — l'ora si sceglie da un elenco a passi di slot (con slot da 15 minuti: 08:00, 08:15, 08:30…), dentro l'orario di lavoro dello studio. Sabati, domeniche e festivi non sono prenotabili.
4. **Durata** — in multipli dello slot (15, 30, 45… minuti). La durata della prestazione viene arrotondata per eccesso: una prestazione da 20 minuti, con slot da 15, occupa 30 minuti.
5. **Medico** (solo i professionisti clinici: dentisti, igienisti, ortodontisti, chirurghi) e **Poltrona**.
6. **Note** — ciò che serve sapere il giorno della visita.

Premi **Conferma Appuntamento**. Il riepilogo a destra mostra paziente, data, ora, durata e poltrona prima di confermare.

Subito dopo si apre **Avvisa il paziente**: WhatsApp (si apre con il messaggio pronto, lo inviate voi), e-mail (parte dal programma), *Non serve avvisarlo* o *Più tardi* (l'avviso resta in Dashboard, *Da avvisare*). Vedi [Gestire gli appuntamenti](#lezione-gestire-appuntamenti).

#### Proponi orario

Il pulsante **Proponi orario** cerca il **primo slot libero** con medico e poltrona disponibili, in base alla durata: oggi solo dopo l'ora attuale, poi nei giorni successivi. Ti propone tre alternative; un clic ne applica una. Resta tutto modificabile a mano.

#### Meglio partire dal piano di cura

Un appuntamento creato con **Pianifica appuntamento** dal dettaglio di un piano di cura resta **collegato** a quella prestazione: il giorno della visita la ritrovi nella scheda di seduta, pronta da registrare, e nel piano la prestazione risulta *Appuntamento fissato*. Un appuntamento creato dall'agenda non porta con sé la prestazione: nella seduta dovrai aggiungerla a mano.

#### Casi particolari

- **L'orario è occupato** (stesso medico o stessa poltrona), **cade in un festivo** o **non è sulla griglia degli slot**: il programma non salva e spiega perché. Vedi [I vincoli dell'agenda](#lezione-vincoli-agenda).
- **Paziente con una condizione a rischio infettivo**: sono prenotabili solo gli ultimi slot della giornata, e *Proponi orario* propone solo quelli.

#### Da sapere

Il programma non invia promemoria automatici al paziente: la conferma dell'appuntamento resta un compito della segreteria (stato *Confermato*).

#### Prova nel programma

Fissa un controllo per *Marco Rossi* con **Proponi orario**. Poi apri il piano di cura di *Silvia Conti* (lezione [Il piano di cura](MANUALE_UTENTE.md#lezione-piano-di-cura)) e prova **Pianifica appuntamento** su una prestazione da pianificare: confronta le due strade.

<a id="lezione-gestire-appuntamenti"></a>

## 4.3 Gestire gli appuntamenti

*Stati, spostamenti, cancellazioni e cosa succede al piano di cura.*

![La modifica di un appuntamento dalla scheda del paziente.](img/academy/36-modifica-appuntamento.png)

*La modifica di un appuntamento dalla scheda del paziente.*

Un appuntamento cambia stato più volte, a volte si sposta, a volte salta. Questa lezione spiega dove si fa ogni cosa e cosa succede.

**Per:** segreteria soprattutto; anche medici e igienisti.

#### Dove si gestisce

Nella **scheda del paziente**, Panoramica, elenco **Appuntamenti**. Da ogni riga:

- **Stato** — il menu a tendina colorato;
- **Modifica** (icona calendario con matita) — data, ora di inizio, ora di fine, poltrona; poi **Salva**;
- **Cancella** (icona calendario barrato) — chiede conferma;
- **WhatsApp** (icona fumetto) — apre WhatsApp, sull'app o su WhatsApp Web dello studio, con il messaggio già scritto: promemoria per un appuntamento futuro programmato o confermato, avviso di annullamento per uno cancellato. Il messaggio lo inviate voi dal vostro WhatsApp Business; il programma non manda niente da solo. Se il paziente non ha un numero di telefono, il programma lo dice.

#### Avvisa il paziente

Ogni volta che un appuntamento viene **prenotato**, **spostato** (giorno, ora o professionista; non la sola poltrona) o **cancellato**, da te, dal Copilot o da Giulia, il programma prepara l'avviso al paziente. Nel gestionale si apre subito la finestra **Avvisa il paziente**:

- **WhatsApp**: si apre WhatsApp (app o WhatsApp Web dello studio) con il messaggio già scritto, con il nuovo orario e, per uno spostamento, quello di prima; lo inviate voi dal vostro WhatsApp Business;
- **E-mail**: parte dal programma, all'indirizzo del paziente;
- **Non serve avvisarlo**: per esempio se l'hai concordato al telefono con lui;
- **Più tardi**: l'avviso resta nell'elenco **Da avvisare** della [Dashboard](#lezione-dashboard).

Conta solo l'ultimo avviso: se sposti un appuntamento prima di aver comunicato la prenotazione, il paziente riceve la conferma con l'orario nuovo, non due messaggi.

Modifica e cancellazione non compaiono su un appuntamento già *Cancellato* o *Completato*. Anche il [Copilot](#lezione-copilot) sposta e annulla appuntamenti, sempre con un'anteprima da confermare.

#### Gli stati e il loro significato

| Stato | Chi lo imposta | Significato |
|---|---|---|
| **Programmato** | alla prenotazione | fissato, da confermare |
| **Confermato** | segreteria | il paziente ha confermato |
| **Presente** | segreteria | è arrivato, è in sala d'attesa |
| **In corso** | medico (anche con *Inizia visita*) | è in poltrona: si apre l'episodio della visita |
| **Completato** | medico, chiudendo la seduta | la visita è finita |
| **Cancellato** | segreteria | l'appuntamento non si terrà |
| **Non presentato** | segreteria | il paziente non è venuto |

#### Spostare un appuntamento

1. **Modifica** sulla riga.
2. Scegli data, inizio e fine fra gli orari a slot (l'elenco della fine parte dopo l'inizio); cambia la poltrona se serve.
3. **Salva**. Se il nuovo orario si sovrappone a un altro appuntamento dello stesso medico o della stessa poltrona, il programma non salva e lo dice.

Un appuntamento vecchio con un orario fuori griglia (per esempio 10:10) si può modificare lasciando invariato l'orario: lo ritrovi in elenco così com'è.

#### Cosa succede al piano di cura

| Cosa fai | La prestazione collegata nel piano |
|---|---|
| sposti l'appuntamento | resta *Appuntamento fissato*, con la nuova data |
| **cancelli** l'appuntamento | torna *da pianificare*: va riprenotata |
| segni **Non presentato** | diventa **In sospeso**: decidi tu se riprogrammarla o toglierla |
| chiudi la seduta senza esito | diventa **In sospeso** |

I dettagli sono in [Spostare o annullare un appuntamento collegato](#lezione-spostare-appuntamento-collegato) e [Paziente non presentato](#lezione-paziente-non-presentato).

#### Prova nel programma

Apri la scheda di *Marco Rossi*, sposta il suo prossimo appuntamento di mezz'ora con **Modifica**, poi segna **Confermato** quello successivo.

<a id="lezione-inizia-visita"></a>

## 4.4 Dal paziente in sala alla visita in corso

*Presente, In corso, Inizia visita e la fotografia d'ingresso.*

![La vista Prossimi con gli appuntamenti già trascorsi oggi.](img/academy/08-medico-agenda-trascorsi.png)

*La vista Prossimi con gli appuntamenti già trascorsi oggi.*

Fra l'arrivo del paziente e la fine della visita l'appuntamento attraversa pochi stati, e ognuno ha un significato preciso.

**Per:** medici e igienisti per la visita; la segreteria segna *Presente*.

#### Gli stati del giorno

- **Confermato** — il paziente ha confermato l'appuntamento.
- **Presente** — è arrivato, è in sala d'attesa. Lo segna di solito la segreteria.
- **In corso** — è in poltrona: la visita è cominciata.
- **Completato** — la seduta è chiusa.

#### Inizia visita

Quando il paziente si siede, apri la **scheda di seduta** e premi **Inizia visita**, in fondo al passo 1 (oppure porta l'appuntamento a *In corso* dalla scheda paziente). In quel momento il programma **fotografa la situazione d'ingresso**: anamnesi e allerte, diagnosi, terapie, odontogramma, piani aperti. Alla chiusura della seduta fotografa la situazione d'uscita. Le due fotografie formano l'**episodio** della visita, che ritrovi nello storico.

Se ti dimentichi di iniziare la visita non succede nulla di grave: la fotografia d'ingresso viene scattata quando registri la seduta, prima degli esiti, e l'episodio è segnato *ingresso tardivo*.

#### Gli appuntamenti già passati

Nella vista **Prossimi**, in fondo, la sezione **Già trascorsi oggi** raccoglie gli appuntamenti finiti della giornata: è il posto dove registrare le sedute a fine mattinata.

#### Prova nel programma

Apri l'agenda sulla giornata di oggi e trova il primo appuntamento a tuo nome: segna il paziente **Presente**, poi apri la seduta e premi **Inizia visita**.

<a id="lezione-preventivi"></a>

## 7.1 Preventivi e avanzamento

*Dal piano al preventivo, stati e lavoro fatturabile.*

![L'avanzamento delle prestazioni di un preventivo.](img/academy/15-preventivo-avanzamento.png)

*L'avanzamento delle prestazioni di un preventivo.*

Il preventivo è l'offerta economica al paziente. In DentalCare Pro nasce di solito dal piano di cura, e ne segue l'avanzamento.

**Per:** segreteria e amministratore; il medico li consulta e li verifica.

#### Creare un preventivo

Da **Preventivi → + Nuovo preventivo**: paziente, titolo, piano di cura collegato, validità. Con **Importa da piano** scegli le prestazioni del piano da includere; ogni riga porta il prezzo di listino, modificabile, con sconto e IVA. Le righe aggiunte a mano sono **righe libere**.

#### Gli stati

*Bozza → Inviato → Accettato* (oppure *Rifiutato*); oltre la data di validità diventa *Scaduto*. Solo un preventivo **accettato** si può fatturare.

#### L'avanzamento

Il preventivo sa quante delle sue prestazioni sono state eseguite in seduta (per esempio *2 di 4 eseguite*). Quando lo sono tutte compare l'etichetta **Fatturabile**: è il lavoro finito e non ancora fatturato, il denaro fermo perché nessuno se n'è accorto.

#### Da sapere

- L'esecuzione si registra nella scheda di seduta, non qui.
- Le righe libere non hanno un'esecuzione e non entrano nel conteggio: un preventivo di 3 righe può dire *1 di 2 eseguite*.
- «Fatturabile» è un'informazione, non un permesso: al momento dell'emissione il programma ricontrolla.

#### Prova nel programma

Apri il preventivo di *Luca Romano*, guarda l'avanzamento riga per riga e portalo ad *Accettato*.

<a id="lezione-fatturazione"></a>

## 7.2 Fatture, acconti e storni

*Saldo e acconto, vita di un documento, note di credito, intestazione.*

![L'elenco dei documenti fiscali.](img/academy/06-fatturazione.png)

*L'elenco dei documenti fiscali.*

La fatturazione parte da un preventivo **accettato** e ne ricopia le voci.

**Per:** segreteria e amministratore.

#### Saldo o acconto

| Documento | Quando | Vincolo |
|-----------|--------|---------|
| **Fattura, ricevuta, parcella** (a saldo) | il lavoro è stato eseguito | tutte le prestazioni del preventivo devono risultare completate |
| **Acconto** | incassi un anticipo su lavoro da fare (tipico in implantologia) | non supera il residuo del preventivo |

Se provi a emettere un documento a saldo su prestazioni non ancora eseguite, il programma rifiuta e **elenca quali mancano**: le registri in seduta, oppure emetti un acconto.

**L'acconto è un importo.** In *Nuova Fattura* scegli *Acconto* e scrivi quanto incassi, IVA compresa: la finestra mostra il totale del preventivo, gli acconti già fatti e il residuo. Il documento ha una riga «Acconto su preventivo …» (una per aliquota, se il preventivo ne ha più d'una, ripartita come nel preventivo).

**Il saldo scala gli acconti.** La fattura a saldo riporta tutte le prestazioni del preventivo e, sotto, una riga negativa «Storno acconto … del …» per ogni acconto emesso: il totale è quello che il paziente deve ancora pagare. Non devi ricalcolare niente. Se c'è un acconto ancora in bozza, il saldo aspetta: emettilo o eliminalo prima. Un preventivo si salda una volta sola: per rifare il saldo elimina la bozza, oppure storna il documento emesso con una nota di credito.

#### La vita di un documento

*Bozza → Emessa → Pagata.* Una bozza si modifica e si elimina liberamente. Un documento **emesso** no: il suo numero è entrato nella sequenza, e un buco nella numerazione è un problema.

#### Inviare il documento al paziente

Dal dettaglio di un documento emesso, **Email** invia il PDF all'e-mail del paziente scritta nel documento: il programma chiede conferma mostrando l'indirizzo, e dopo l'invio il dettaglio riporta «Inviata via e-mail a … il …». Una bozza o un documento annullato non si inviano. **PDF** scarica lo stesso documento, per allegarlo tu o archiviarlo; **Stampa** lo stampa. Il PDF contiene le prestazioni eseguite: invialo solo all'indirizzo del paziente. Nello studio di prova i pazienti sono fittizi: l'e-mail arriva a te, all'indirizzo con cui hai attivato la prova, e la conferma te lo dice.

#### Correggere un errore: la nota di credito

Dal dettaglio di un documento emesso, **Storna con nota di credito**: il programma crea una nota di pari importo con segno opposto, collegata all'originale e con numerazione propria, e porta il documento originale ad *Annullato* conservandolo in archivio. Lo storno è sempre totale, e ogni documento si storna una volta sola.

#### A chi è intestata la fattura

Dipende dalla **modalità di fatturazione** scelta dall'amministratore (Impostazioni → Clinica):

- **Studio** (predefinita) — i documenti sono intestati allo studio, con la sua numerazione.
- **Medico** — i documenti sono intestati al medico del preventivo (parcella), con i suoi dati di fatturazione; i preventivi propongono le sue tariffe: [Le tariffe del medico](MANUALE_UTENTE.md#lezione-tariffe-medico).

Metodo di pagamento e scadenza proposti nei nuovi documenti si impostano in Impostazioni → Fatturazione.

#### Prova nel programma

Apri la fatturazione, filtra i documenti **Emessi** e aprine uno: prova **Storna con nota di credito** e guarda il risultato nell'elenco.

<a id="lezione-richiami"></a>

## 7.3 I richiami

*Chi ricontattare e quando; registrare i contatti.*

![Registra contatto: il testo del richiamo, da copiare o da inviare per e-mail o WhatsApp.](img/academy/07-richiami.png)

*Registra contatto: il testo del richiamo, da copiare o da inviare per e-mail o WhatsApp.*

I richiami ricordano allo studio **chi** va ricontattato e **quando**: controlli semestrali, igiene, terapie da completare.

**Per:** segreteria, igienisti.

#### L'elenco

Ogni richiamo ha paziente, tipo, data prevista, **priorità** (alta, media, bassa) e **stato**:

| Stato | Significato |
|-------|-------------|
| Da contattare | nessun contatto ancora |
| Contattato | c'è stato un tentativo |
| In attesa | si aspetta una risposta |
| Confermato | l'appuntamento è fissato |
| Chiuso / Annullato | concluso |

Il pannello a destra elenca i richiami urgenti.

#### Registrare un contatto

Dal menu del richiamo, **Registra contatto**: canale (telefono, e-mail, WhatsApp), esito (risposto, non risposto, messaggio lasciato, confermato, rifiutato) e note. Lo storico dei contatti resta nel richiamo: chi chiama dopo di te sa cosa è già stato detto. Passando il mouse su una riga, il pannello a destra mostra lo storico di quel richiamo (esito, data e ora, note, chi ha chiamato); un clic sulla riga lo tiene fermo, comodo sul tablet. Dopo il salvataggio il nuovo contatto compare lì e la colonna Contatti mostra il numero e la data dell'ultimo. Il primo contatto porta il richiamo da «Da contattare» a «Contattato» da solo; gli altri passaggi (in attesa, confermato, chiuso) li fai tu dal menu della colonna Stato.

Nella stessa finestra c'è il **testo del richiamo** con il nome del paziente già inserito, e tre modi per mandarlo:

- **Invia per e-mail** — parte dal programma, all'indirizzo del paziente; le risposte arrivano all'e-mail dello studio;
- **Apri in WhatsApp** — si apre WhatsApp (app o WhatsApp Web dello studio) con il testo pronto: lo invii tu dal vostro WhatsApp Business;
- **Copia** — per incollarlo dove vuoi.

Con e-mail e WhatsApp il contatto si registra da solo (canale e «messaggio lasciato») e compare nello storico; se l'e-mail non parte, il programma lo dice e non registra niente. Il testo si cambia in [Impostazioni → Richiami](MANUALE_UTENTE.md#lezione-impostazioni-documenti).

#### Da sapere

**Genera richiami** crea i richiami per i pazienti senza un controllo recente, con l'intervallo impostato dallo studio (sei mesi, se non è cambiato). Se un paziente ha già un richiamo aperto e ha superato anche il secondo intervallo, il richiamo diventa *Secondo richiamo* ad alta priorità. Nell'ambiente di prova nessun messaggio parte davvero verso i pazienti: l'e-mail arriva a te, e in WhatsApp scegli tu a chi mandarlo (i numeri dei pazienti sono fittizi).

#### Prova nel programma

Apri i richiami, prendi il primo *da contattare* ad alta priorità e registra una telefonata con esito *messaggio lasciato*.

<a id="lezione-magazzino"></a>

## 7.4 Il magazzino

*Prodotti, soglie, movimenti e fornitori.*

Il magazzino tiene sotto controllo materiali, scorte e fornitori.

**Per:** tutti i ruoli (il menu Magazzino è aperto a tutti).

#### Prodotti

Ogni prodotto ha unità di misura, categoria, fornitore, costo e due soglie: **quantità minima** e **quantità di riordino**. Il colore dice lo stato della scorta:

- **rosso** — sotto il minimo;
- **giallo** — sotto il doppio del minimo, quasi esaurito;
- **verde** — scorta sufficiente.

#### Movimenti

Ogni variazione è un movimento: **carico** (merce ricevuta, con costo e documento di trasporto), **scarico** (consumo interno), **rettifica** (correzione d'inventario), **rientro** (reso al fornitore). La scorta è la somma dei movimenti: non si modifica a mano, così resta sempre spiegabile.

#### Fornitori

Anagrafica essenziale: ragione sociale, referente, contatti, note.

#### Prova nel programma

Apri il magazzino, trova un prodotto in rosso e registra un **carico** che lo riporti sopra la soglia.

<a id="lezione-paziente-non-presentato"></a>

## 5.1 Paziente non presentato

*Registrare l'assenza e decidere cosa fare delle prestazioni previste.*

Il paziente non è venuto e non ha avvisato. Va registrato, perché cambia lo stato delle prestazioni previste e la storia del paziente.

**Per:** segreteria; il medico per le decisioni sul piano.

#### Cosa fare

1. Apri la **scheda del paziente**, Panoramica, elenco degli appuntamenti.
2. Nel menu dello stato dell'appuntamento scegli **Non presentato**.

Non cancellarlo: *Cancellato* significa «l'appuntamento non si terrà» (disdetto per tempo), *Non presentato* significa «doveva venire e non è venuto». Sono informazioni diverse, e per lo studio la seconda conta.

#### Cosa succede

- La **scheda di seduta** di quell'appuntamento non accetta più esiti: il paziente non c'era, non c'è niente da dichiarare.
- Le prestazioni del piano collegate all'appuntamento diventano **In sospeso · seduta del …**, e in testa al piano compare l'avviso.
- Dal piano, per ogni prestazione in sospeso, decidi:
  - **Riprogramma** → si apre la prenotazione di una nuova seduta, già collegata alla prestazione;
  - **Togli dal piano** → con un **motivo obbligatorio** (per esempio *il paziente ha rinunciato*).

#### Lo fa il programma, la notte dopo

Se nessuno lo segna, ci pensa il programma: ogni notte gli appuntamenti dei giorni precedenti ancora **Programmati** o **Confermati** passano a **Non presentato**. Restano fuori quelli in cui il paziente è stato segnato *Presente*, la visita è stata avviata o la seduta ha già un esito. Il margine per i ritardi è l'intera giornata: chi arriva tardi lo segni *Presente* come sempre.

Lo stato messo dal programma porta il segno **automatico**. Nella scheda paziente premi **Conferma** se è giusto; se il paziente era venuto, scegli lo stato corretto dal menu. In entrambi i casi il segno sparisce.

Allo stesso modo, quando registri gli esiti di una seduta senza aver premuto *Inizia visita*, l'appuntamento passa da solo a **In corso**.

#### Casi particolari

- **Il paziente arriva in ritardo, dopo che lo hai segnato Non presentato.** Riporta lo stato a *Presente* o *In corso*: la seduta torna registrabile.
- **Ha avvisato all'ultimo momento.** Se l'appuntamento non si terrà, è *Cancellato*: la prestazione torna *Da pianificare* e si riprenota normalmente. Vedi [Spostare o annullare un appuntamento collegato](#lezione-spostare-appuntamento-collegato).
- **Vuoi ricontattarlo.** Crea un richiamo o fissa subito il nuovo appuntamento: [I richiami](#lezione-richiami).

#### Da sapere

Le assenze restano nell'elenco degli appuntamenti del paziente, in arancione: chi lo segue vede subito se è un paziente che salta le visite.

#### Prova nel programma

Apri la scheda di *Marco Rossi*, segna **Non presentato** un appuntamento passato, poi riportalo a *Programmato*.

<a id="lezione-spostare-appuntamento-collegato"></a>

## 5.5 Spostare o annullare un appuntamento collegato

*Cosa succede alle prestazioni del piano, e perché il medico non si cambia.*

Un appuntamento creato dal piano di cura porta con sé le sue prestazioni. Spostarlo, annullarlo o cambiare medico ha conseguenze precise.

**Per:** segreteria e medici.

#### Spostare

Dalla **scheda del paziente**, **Modifica** sulla riga dell'appuntamento: nuova data, inizio, fine, poltrona. Le prestazioni restano collegate e nel piano risultano *Appuntamento fissato* con la nuova data. Si può fare anche con il [Copilot](#lezione-copilot): *«Sposta l'appuntamento di Marco Rossi a giovedì alle 10»*; il Copilot mostra un'anteprima e salva solo dopo la tua conferma.

#### Annullare

**Cancella** sulla riga (o scegli *Cancellato* nello stato). Le prestazioni collegate tornano **Da pianificare**: nel piano compare di nuovo l'icona **Pianifica appuntamento** per fissare una nuova seduta. Niente si perde, niente resta «fissato» per finta.

#### Cambiare medico

- Dalla scheda del paziente la modifica non cambia il medico: si cambia con il Copilot (*«sposta l'appuntamento a giovedì alle 10 con il dottor Marchetti»*).
- **Non si può cambiare medico** a un appuntamento legato a un piano di cura o a un preventivo: il piano è del medico che lo segue. Il programma lo dice e propone di spostarlo mantenendo lo stesso medico.
- Un medico, dal Copilot, sposta i propri appuntamenti ma non li riassegna ad altri.

#### Spostare quando l'orario non va bene

Se il nuovo orario si sovrappone a un altro appuntamento, cade in un giorno festivo o non lavorativo, o non è sulla griglia degli slot, lo spostamento non avviene. Il Copilot in questi casi propone poltrone o orari liberi. Vedi [I vincoli dell'agenda](#lezione-vincoli-agenda).

#### Riepilogo

| Cosa fai | Prestazioni collegate |
|---|---|
| sposti | restano *Appuntamento fissato* |
| annulli | tornano *Da pianificare* |
| segni Non presentato | diventano *In sospeso* |
| cambi medico | non consentito se legato a piano o preventivo |

#### Prova nel programma

Apri il piano di *Silvia Conti*, fissa una seduta con **Pianifica appuntamento**, poi cancellala dalla scheda del paziente e torna al piano: la prestazione è di nuovo *Da pianificare*.

<a id="lezione-vincoli-agenda"></a>

## 5.6 I vincoli dell'agenda

*Festivi, orari, griglia degli slot, conflitti, pazienti a rischio infettivo.*

Il programma rifiuta alcuni appuntamenti, e lo dice con un messaggio chiaro. Conoscere i vincoli evita sorprese al telefono.

**Per:** segreteria e medici.

#### I vincoli

| Vincolo | Cosa succede | Cosa fare |
|---|---|---|
| **Sabato, domenica, festivo** | non si prenota | scegli un giorno lavorativo |
| **Giorno non lavorativo** dello studio | *Proponi orario* e il Copilot lo saltano | Impostazioni → Agenda, giorni lavorativi |
| **Fuori orario** di lavoro | l'orario non compare nell'elenco | Impostazioni → Agenda, orario di lavoro |
| **Fuori dalla griglia degli slot** (per esempio 14:10 con slot da 15 minuti) | rifiutato, con i due slot più vicini (14:00 o 14:15) | scegli uno slot |
| **Stesso medico** già occupato | rifiutato | altro orario o altro medico |
| **Stessa poltrona** già occupata | rifiutato | altra poltrona: il Copilot elenca quelle libere |
| **Paziente con condizione a rischio infettivo** attiva in anamnesi | solo gli ultimi slot della giornata | *Proponi orario* propone solo quelli |

#### Perché la fine giornata per il rischio infettivo

Un paziente con una condizione infettiva attiva va visitato per ultimo, così la sanificazione dello studio non ritarda gli altri. Il vincolo nasce dall'anamnesi: quando la condizione non è più attiva, il vincolo sparisce.

#### Il Copilot

Anche il Copilot rispetta gli stessi vincoli. A una richiesta come *«alle 14:10»* risponde proponendo gli slot vicini e chiedendo quale va bene; quando sposta un appuntamento e trova un conflitto, propone gli orari liberi del medico o le poltrone libere. L'assistente telefonica riceve dal programma lo stesso rifiuto, con gli stessi orari da proporre.

#### Prova nel programma

Apri **+ Appuntamento**, scegli un sabato: il programma lo segnala. Poi scegli un giorno feriale e guarda l'elenco degli orari: sono solo quelli della griglia.

<a id="lezione-copilot"></a>

## 8.1 Chiedere al Copilot

*Modalità amministrativa e clinica, domande, anteprime e suggerimenti.*

Il **Copilot AI** è l'assistente dello studio: legge i dati di DentalCare Pro e risponde in linguaggio naturale. Prepara anche le modifiche, ma le salva solo dopo la tua conferma.

**Per:** segreteria, medici, igienisti (menu **Copilot AI**).

#### Le due modalità

| Modalità | Per chi | Cosa legge |
|---|---|---|
| **Amministrativa** | segreteria, igienisti; tutti, se lo studio non ha attivato il clinico | agenda, anagrafica (senza dati sanitari), preventivi, fatture, richiami, magazzino |
| **Clinica** | medici (dentista, ortodontista, chirurgo), se lo studio l'ha attivata | in più anamnesi, allerte, odontogramma, diagnosi, prescrizioni, piani di cura |

Il messaggio di apertura dice in quale modalità sei. Nell'ambiente di prova la modalità segue la persona scelta nel menu in alto. La modalità clinica ha una sua lezione: [Copilot clinico](MANUALE_UTENTE.md#lezione-copilot-clinico).

#### Cosa chiedergli

- *Quali appuntamenti ho domani?*
- *Trova il primo orario libero per un'igiene con Gentili la prossima settimana.*
- *Quali pazienti sono in attesa di richiamo?*
- *Sposta l'appuntamento di Silvia Conti a giovedì alle 10.*
- *Prepara un preventivo per Marco Rossi con una igiene professionale.*

Sotto la casella di scrittura ci sono domande già pronte.

#### Quando deve cambiare qualcosa

Se la richiesta comporta una modifica (creare, spostare o annullare un appuntamento, un preventivo, un richiamo), il Copilot **non la fa da solo**: mostra un'**anteprima** di cosa farà e aspetta la tua conferma (*«sì, conferma»*). Se l'orario chiesto è occupato o fuori dagli slot, propone le alternative invece dell'anteprima.

Dopo aver prenotato, spostato o annullato un appuntamento, la risposta porta il pulsante **Avvisa** con il nome del paziente: apre la finestra [Avvisa il paziente](#lezione-gestire-appuntamenti) (WhatsApp, e-mail o «non serve»). Se non lo usi, l'avviso resta nella Dashboard.

#### Suggerimenti e cronologia

- Ogni mattina il Copilot prepara **suggerimenti** (per esempio i richiami scaduti da contattare): li trovi in alto nella pagina, e puoi usarli o scartarli.
- **Nuova chat** ricomincia da capo; **Cronologia** riapre le conversazioni precedenti.

#### Prova nel programma

Apri il Copilot e chiedigli quali appuntamenti hai domani. Poi chiedigli di spostarne uno e leggi l'anteprima prima di confermare.
