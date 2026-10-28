# DentalCare Pro — Guida per il titolare e l'amministratore

> Versione 28 ottobre 2026. Generato dalle lezioni dell'**Academy**, il manuale ufficiale dentro il programma (`tools/genera_manuale.py`): per correggerlo si corregge la lezione e si rigenera. Le schermate vengono dall'ambiente dimostrativo: nomi e dati dei pazienti sono fittizi.

Il percorso dice cosa fare e in che ordine; le lezioni che richiama seguono, nell'ordine in cui compaiono. Il resto è nel [manuale integrale](MANUALE_UTENTE.md).

## Indice

- [Percorso del titolare](#lezione-percorso-titolare)
- [Clinica e professionisti](#lezione-impostazioni-studio)
- [Agenda e visibilità](#lezione-impostazioni-agenda)
- [Prestazioni e listino](#lezione-prestazioni-listino)
- [Preventivi, fatture, richiami e sistema](#lezione-impostazioni-documenti)
- [Copilot e AI](#lezione-impostazioni-ai)
- [La dashboard](#lezione-dashboard)
- [Preventivi e avanzamento](#lezione-preventivi)
- [I richiami](#lezione-richiami)
- [Fatture, acconti e storni](#lezione-fatturazione)
- [Il magazzino](#lezione-magazzino)
- [Cosa fa il Copilot e cosa no](#lezione-copilot-limiti)
- [Ambiente di prova e amministrazione dell'account](#lezione-ambiente-prova-studio)
- [Percorso della segreteria](#lezione-percorso-segreteria)
- [Percorso del medico](#lezione-percorso-medico)
- [Percorso dell'igienista](#lezione-percorso-igienista)

---

<a id="lezione-percorso-titolare"></a>

## 2.4 Percorso del titolare

*Avvio dell'account e delle cliniche, configurazione, controllo dell'andamento, cura dei dati.*

Il percorso di chi è responsabile dello studio: avvio, configurazione, controllo dell'andamento e cura dei dati.

**Per:** titolare e amministratore dello studio. Nell'ambiente di prova scegli **il tuo nome — Amministratore** nel menu in alto.

#### 1. Avvio dello studio (una volta)

| Tappa | Cosa fai | Lezione |
|---|---|---|
| Dati dello studio | ragione sociale, partita IVA, SDI, IBAN, intestazione delle fatture | [Studio e professionisti](#lezione-impostazioni-studio) |
| Professionisti | medici, igienisti, segreteria, con ruolo e dati di fatturazione | [Studio e professionisti](#lezione-impostazioni-studio) |
| Agenda | orario di lavoro, giorni, durata dello slot, visibilità dei pazienti | [Agenda e visibilità](#lezione-impostazioni-agenda) |
| Listino | prestazioni, prezzi, durate, effetto sul dente | [Prestazioni e listino](#lezione-prestazioni-listino) |
| Documenti | validità dei preventivi, IVA, pagamenti, richiami | [Preventivi, fatture, richiami e sistema](#lezione-impostazioni-documenti) |
| Copilot | modalità (spento, amministrativo, clinico) e istruzioni | [Copilot e AI](#lezione-impostazioni-ai) |

#### 2. Il controllo dell'andamento

- Ogni giorno: [La dashboard](#lezione-dashboard) (occupazione, piani da decidere, preventivi inviati).
- Ogni settimana: preventivi **fatturabili** e non ancora fatturati, richiami scaduti: [Preventivi e avanzamento](#lezione-preventivi), [I richiami](#lezione-richiami).
- Ogni mese: fatture, note di credito, scorte: [Fatture, acconti e storni](#lezione-fatturazione), [Il magazzino](#lezione-magazzino).

#### 3. Cura dei dati e responsabilità

- Chi vede quali pazienti (per medico o condivisi): [Agenda e visibilità](#lezione-impostazioni-agenda).
- Il Copilot clinico e la riservatezza delle conversazioni: [Copilot e AI](#lezione-impostazioni-ai), [Cosa fa il Copilot e cosa no](#lezione-copilot-limiti).
- Ambiente di prova, **cliniche dell'account** (si creano solo dalla pagina del titolare), esportazione dei dati e chiusura dell'account: [Ambiente di prova e amministrazione dell'account](#lezione-ambiente-prova-studio).

#### 4. Conoscere il lavoro degli altri

Il titolare risponde di tutto lo studio: conviene conoscere anche i percorsi di [segreteria](#lezione-percorso-segreteria), [medico](#lezione-percorso-medico) e [igienista](#lezione-percorso-igienista).

#### Prova nel programma

Scegli **Amministratore** nel menu in alto, apri **Impostazioni → Agenda** e controlla orario di lavoro e durata dello slot: tutta l'agenda segue questi due valori.

<a id="lezione-impostazioni-studio"></a>

## 9.1 Clinica e professionisti

*Dati della clinica, modalità di fatturazione, professionisti, poltrone e catalogo dell'anamnesi.*

![Un professionista: profilo, ruolo, dati di fatturazione e azioni.](img/academy/32-impostazioni-professionisti.png)

*Un professionista: profilo, ruolo, dati di fatturazione e azioni.*

I dati dello studio e le persone che ci lavorano. Si impostano una volta all'avvio e si aggiornano quando cambia qualcosa.

**Per:** amministratore (menu **Impostazioni**). Nell'ambiente di prova scegli **Amministratore** nel menu in alto.

#### Clinica

Scheda **Clinica** (i dati della clinica in cui sei entrato): ragione sociale, partita IVA, codice fiscale, indirizzo, telefono, e-mail, sito, **PEC**, **codice SDI** e **IBAN**. Sono i dati che compaiono su preventivi e fatture: vanno compilati prima di emettere il primo documento.

Nella stessa scheda c'è la **modalità di fatturazione**:

- **Clinica (predefinito)** — le fatture sono intestate alla clinica;
- **Medico** — le fatture sono intestate al medico del preventivo (parcella), con i dati di fatturazione del medico e le sue [tariffe](MANUALE_UTENTE.md#lezione-tariffe-medico).

#### Professionisti

Scheda **Professionisti**: l'elenco delle persone dello studio con il loro ruolo. Selezionandone una:

- **Profilo anagrafico** — nome, cognome, **ruolo** (dentista, igienista, ortodontista, chirurgo, assistente, segreteria, amministratore, altro), telefono, e-mail, *professionista attivo*;
- **Dati fatturazione** — partita IVA e dati per le parcelle, se lo studio fattura a nome dei medici;
- **Riassegna pazienti** — passa i pazienti a un altro medico (per esempio quando un collega lascia lo studio);
- **Disattiva** — il professionista non compare più nelle scelte, ma la sua storia resta;
- **Elimina** — solo per chi non ha storia.

**+ Nuovo Professionista** crea una persona; **Pazienti senza medico** elenca i pazienti senza un medico di riferimento, da assegnare.

#### L'account di un nuovo professionista

Se indichi un'**e-mail**, il programma crea un account e spedisce una **password temporanea**: al primo accesso il professionista ne sceglie una sua ([Accesso e password](MANUALE_UTENTE.md#lezione-accesso-e-password)). Il ruolo decide cosa vede e come risponde il Copilot.

Nello **studio di prova** l'e-mail non si può impostare: i professionisti sono persone fittizie e non devono diventare account veri.

#### Anagrafiche

Le cliniche dell'account non si creano qui: le crea il titolare dalla sua pagina ([Amministrazione account](#lezione-ambiente-prova-studio)), poi ci entra e completa qui dati, orari, poltrone e il resto.

Scheda **Anagrafiche**:

- **Poltrone** — le poltrone della clinica in cui sei entrato: aggiungile, rinominale (gli appuntamenti seguono il nuovo nome), disattivale quando non si usano più. Si prenota solo sulle poltrone attive; una poltrona con appuntamenti non si elimina, si disattiva. Una clinica nuova parte con *Poltrona 1*. Oltre 8 poltrone attive il programma avvisa prima di aggiungerne: l'agenda giornaliera non le mostra più tutte insieme nemmeno su un monitor grande;
- **Anamnesi** — il catalogo delle voci dell'anamnesi, uguale per tutte le sedi: categorie, voci, quali sono **allerta**.

#### Prova nel programma

Come **Amministratore**, apri **Impostazioni → Professionisti**, seleziona *Gentili Michele* e guarda profilo e dati di fatturazione. Prova **Riassegna pazienti** senza confermare.

#### Codice della segreteria vocale

Giulia, la segreteria vocale, risponde da un **numero unico** per tutti gli studi DentalCare. Chi chiama arriva al vostro studio così:

1. dice nome e cognome: se il numero da cui chiama e il cognome sono di un vostro paziente, Giulia propone il vostro studio e chiede conferma;
2. altrimenti indica il **codice a 5 cifre** dello studio, a voce o con la tastiera del telefono;
3. oppure dice il nome dello studio o del dentista e la città.

Il codice è nella scheda **Clinica**, riquadro *Codice segreteria vocale*: scrivetelo sui promemoria, sul sito e alla reception. **Genera un nuovo codice** lo sostituisce (dopo una conferma): quello vecchio smette subito di funzionare.

Giulia nomina lo studio solo se numero **e** cognome corrispondono, così chi usa il telefono di un altro non scopre da quale dentista è in cura. Negli studi di prova i pazienti sono fittizi: si arriva allo studio solo con il codice.

**Nello studio di prova** Giulia può fare in tutto un numero limitato di **prenotazioni o spostamenti** (di base 5; le cancellazioni non contano). Il codice dello studio e quante operazioni restano sono nella **Dashboard**, nel riquadro *Prova Giulia al telefono*, e nell'e-mail di benvenuto; Giulia lo ricorda anche all'inizio della chiamata. Finite le operazioni, Giulia può solo cancellare appuntamenti. Generare un nuovo codice non le rimette a disposizione.

<a id="lezione-impostazioni-agenda"></a>

## 9.2 Agenda e visibilità

*Slot, orario e giorni di lavoro, chi vede quali pazienti.*

![Durata dello slot, orario di lavoro, giorni lavorativi.](img/academy/31-impostazioni-agenda.png)

*Durata dello slot, orario di lavoro, giorni lavorativi.*

Orario di lavoro, giorni, durata dello slot e visibilità dei pazienti: quattro scelte che cambiano l'agenda e il lavoro di tutti.

**Per:** amministratore (Impostazioni → **Agenda**).

#### Durata dello slot

**15, 20, 30 o 60 minuti.** È il passo della griglia dell'agenda e di tutte le scelte di orario:

- gli orari d'inizio si scelgono solo a passi di slot (con 15 minuti: 08:00, 08:15, 08:30…);
- le durate sono multipli dello slot, e la durata di una prestazione viene arrotondata per eccesso;
- *Proponi orario*, il Copilot e l'assistente telefonica propongono solo orari della griglia;
- un orario fuori griglia (per esempio 14:10) viene rifiutato, con i due slot vicini da proporre.

Uno slot corto dà più flessibilità; uno lungo un'agenda più ordinata. 15 minuti va bene per la maggior parte degli studi.

#### Orario e giorni di lavoro

**Inizio** e **Fine** delimitano la giornata: l'agenda mostra quelle ore e non propone orari fuori. **Giorni lavorativi**: i giorni aperti; gli altri vengono saltati dalle proposte di orario. Sabato e domenica restano comunque non prenotabili.

#### Modalità di gestione pazienti

Chi vede e gestisce quali pazienti, fra i medici della sede:

- **Per medico (predefinito)** — ogni medico vede e gestisce solo i propri pazienti;
- **Condivisi** — tutti i medici vedono e gestiscono tutti i pazienti della sede, cartella inclusa.

La segreteria vede sempre tutti i pazienti, ma non la cartella clinica. È una scelta che riguarda la riservatezza: va decisa con il responsabile della privacy dello studio.

#### Da sapere

- Cambiare orario o slot non sposta gli appuntamenti già fissati: un vecchio appuntamento fuori griglia resta com'è e si può modificare senza cambiarne l'orario.
- Dopo **Salva** le schermate dell'agenda usano subito i nuovi valori.

#### Prova nel programma

Come **Amministratore**, apri **Impostazioni → Agenda**, porta lo slot a **30 minuti** e salva. Apri **+ Appuntamento** e guarda l'elenco degli orari. Poi riporta lo slot a 15 minuti.

<a id="lezione-prestazioni-listino"></a>

## 7.5 Prestazioni e listino

*Prezzi, durate, denti ammessi, effetto sul dente e default per condizione.*

![Il listino, con categorie, prezzi, durate e default per condizione.](img/academy/33-prestazioni.png)

*Il listino, con categorie, prezzi, durate e default per condizione.*

Il listino è l'elenco delle prestazioni dello studio: nome, prezzo, IVA, durata e regole cliniche. Da lui dipendono piani di cura, preventivi, agenda e odontogramma.

**Per:** amministratore e medici (menu **Prestazioni**).

#### Le prestazioni

Le prestazioni sono raggruppate per **categoria** (Conservativa, Endodonzia, Igiene, Implantologia…; le categorie si gestiscono con **Categorie**). Per ognuna:

| Campo | A cosa serve |
|---|---|
| **Prezzo** e **IVA** | il prezzo di listino che arriva nei preventivi |
| **Durata** | propone la durata dell'appuntamento (arrotondata allo slot) |
| **Denti** | su quali denti si può fare (per esempio solo molari, anche decidui, solo denti naturali): il piano di cura offre solo prestazioni ammesse per quel dente |
| **Lascia sul dente** | lo stato del dente dopo l'esecuzione (per esempio *otturazione*): è la proposta che la scheda di seduta fa per l'odontogramma |
| **Attiva** | una prestazione disattivata non compare più nelle scelte, ma resta nei documenti passati |

**+ Nuova Prestazione** ne aggiunge una; la matita modifica, il cestino elimina (solo se non è mai stata usata).

#### Default per condizione

In fondo alla pagina, **Default per condizione** dice al programma quale prestazione proporre per ogni condizione dell'odontogramma, per esempio *carie su una superficie → otturazione monofacciale*, *carie su due superfici → bifacciale*. È la tabella che usa [Genera piano di cura](MANUALE_UTENTE.md#lezione-genera-piano). **Ordine** decide quale proposta compare per prima quando ce n'è più d'una.

#### Da sapere

- Cambiare un prezzo vale per i **nuovi** preventivi: quelli già fatti mantengono il prezzo con cui sono nati.
- Un medico può avere **prezzi suoi** diversi dal listino: [Le tariffe del medico](MANUALE_UTENTE.md#lezione-tariffe-medico).
- La configurazione di *Lascia sul dente* è clinica: la modificano solo i ruoli clinici e l'amministratore.

#### Prova nel programma

Apri **Prestazioni**, trova *Otturazione composito monofacciale* e guarda cosa lascia sul dente. Poi scorri fino a **Default per condizione**.

<a id="lezione-impostazioni-documenti"></a>

## 9.4 Preventivi, fatture, richiami e sistema

*Valori predefiniti dei documenti, intervalli dei richiami, preferenze.*

Le impostazioni che decidono come nascono preventivi, fatture e richiami, e alcune preferenze dell'applicazione. Preventivi, fatturazione e richiami valgono per **tutta la sede**: le salva il server e le applica a chiunque lavori nella sede, da qualunque computer.

**Per:** amministratore (menu **Impostazioni**).

#### Preventivi

- **Validità** — per quanti giorni vale un nuovo preventivo; la data si può cambiare su ciascuno. Oltre la data il preventivo diventa *Scaduto*.
- **Prefisso numero** — la parte fissa della numerazione dei nuovi preventivi (lettere e cifre, massimo 8). Vuoto: le prime lettere della città della sede.
- **Aliquota IVA predefinita** — 0%, 4%, 5%, 10% o 22%: quella proposta quando crei una nuova prestazione nel listino. Le voci del preventivo usano l'IVA della loro prestazione, se non ne scrivi una diversa (le prestazioni sanitarie sono di norma esenti). Cambiare l'aliquota non tocca le prestazioni già in listino: per portarla su tutte premi **Applica al listino**, che salva e ti chiede conferma. I preventivi e le fatture già fatti non cambiano.

#### Fatturazione

- **Metodo di pagamento predefinito** — contanti, bonifico, carta di credito, assegno, RID/SDD: quello delle nuove fatture.
- **Scadenza predefinita** — quanti giorni dopo la creazione scade il pagamento, quando la fattura nuova non ha una scadenza.
- **Prefisso fatture studio** — la parte fissa del numero delle fatture intestate allo studio (per esempio FATT-2026-00001). Cambiarlo non fa ripartire il numero progressivo dell'anno.

A chi è intestata la fattura (studio o medico) si sceglie nella scheda Studio: [Studio e professionisti](#lezione-impostazioni-studio).

#### Richiami

- **Intervallo primo richiamo** — 3, 6, 9 o 12 mesi dall'ultima visita;
- **Intervallo secondo richiamo** — mesi dall'ultima visita oltre i quali un richiamo ancora aperto diventa *Secondo richiamo*, a priorità alta;
- **Template messaggio richiamo** — il testo del messaggio al paziente, con {paziente}, {studio} e {telefono} al posto di nome del paziente, nome e telefono della sede. Lo trovi in **Registra contatto**, da copiare o da inviare per e-mail o WhatsApp.

Sono i valori che usa **Genera richiami**: [I richiami](#lezione-richiami). Un medico o un igienista può impostare intervalli e testo propri (**Impostazioni → I miei richiami**): valgono per i pazienti la cui ultima visita è stata con lui.

Allo stesso modo, nella fatturazione a nome dei medici, ciascuno può avere metodo di pagamento, scadenza, prefisso e IBAN propri (**Impostazioni → La mia fatturazione**). L'amministratore li vede e li cambia in **Impostazioni → Per professionista**.

#### Sistema

- **WhatsApp** — impostazione generale della sede, la cambia l'amministratore:
  - **WhatsApp attivo**: spento, i pulsanti WhatsApp spariscono da richiami, appuntamenti e «Avvisa il paziente»; restano e-mail e «non serve».
  - **Numero WhatsApp Business dello studio**: quello del titolare. I messaggi si aprono su questo account (telefono o WhatsApp Web) con il testo pronto, la segreteria preme invio, e lì arrivano le risposte dei pazienti.
  - **Modalità**: oggi **Manuale** (gratis, lo invia una persona). **Automatico** arriverà più avanti: i messaggi partiranno da soli e le risposte andranno alla segreteria e al medico che segue il paziente, con un costo a messaggio fissato da Meta.

- **Errori intelligenti** — quando un'operazione fallisce, il messaggio tecnico viene riscritto in linguaggio semplice dall'AI. Spento, compare il messaggio originale e non viene inviato nulla.
- **Righe appuntamenti in Dashboard** — quante righe mostrare per pagina.
- **Versione applicazione** — utile quando si scrive all'assistenza.

#### Da sapere

Ogni scheda ha il suo **Salva**: salva prima di uscire dalle Impostazioni. Valori fuori misura (per esempio un prefisso con trattini o una validità di 0 giorni) vengono rifiutati con un messaggio accanto al pulsante.

#### Prova nel programma

Come **Amministratore**, apri **Impostazioni → Richiami** e guarda gli intervalli. Poi apri **Richiami** dal menu e prova **Genera richiami**.

<a id="lezione-impostazioni-ai"></a>

## 9.5 Copilot e AI

*Modo del Copilot (spento, amministrativo, clinico) e istruzioni.*

Come si comporta il Copilot nello studio: se risponde, a chi, e con quali istruzioni.

**Per:** titolare dello studio (Impostazioni → **AI**). Nello studio di prova: **Amministratore**.

#### Modo del Copilot

Una scelta per tutto lo studio:

| Modo | Cosa succede |
|---|---|
| **Spento** | il Copilot non risponde a nessuno, in nessuna sede |
| **Amministrativo** | agenda, pazienti senza dati sanitari, preventivi, richiami, fatture, magazzino |
| **Clinico** | in più odontogramma, anamnesi, diagnosi e prescrizioni, **solo per i medici** |

Il modo clinico tratta dati sanitari: prima di attivarlo serve la **valutazione d'impatto privacy (DPIA)** aggiornata dello studio. Igienisti e segreteria restano comunque in modalità amministrativa. Ogni cambio di modo viene registrato, con nome e data.

#### Le istruzioni del Copilot

Nella stessa scheda, **Prompt Assistente AI** mostra i testi con cui il Copilot viene istruito (per esempio il tono, le regole di prudenza), per ogni lingua:

- **Salva** — lo studio usa la sua versione, segnata *Personalizzato per lo studio*;
- **Ripristina predefinito** — torna al testo di fabbrica.

Modificarli cambia il comportamento del Copilot per tutti: farlo con prudenza, e provare dopo ogni modifica. Alcune regole non dipendono da questi testi e restano sempre valide (per esempio: in modalità amministrativa niente indicazioni cliniche).

#### Da sapere

- Le domande al Copilot passano da un filtro che sostituisce nomi e dati identificativi con pseudonimi prima di raggiungere il servizio di intelligenza artificiale esterno: [Cosa fa il Copilot e cosa no](#lezione-copilot-limiti).
- Gli **errori intelligenti** si accendono a parte, in Impostazioni → Sistema.

#### Prova nel programma

Come **Amministratore**, apri **Impostazioni → AI**, passa a **Amministrativo** e salva. Torna al tuo nome, apri il Copilot e leggi il messaggio di apertura. Poi rimetti **Clinico**.

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

Compare solo quando c'è qualcosa da fare: i pazienti a cui va comunicata una **prenotazione**, uno **spostamento** o una **cancellazione** e che nessuno ha ancora avvisato. Ci finiscono le operazioni fatte da **Giulia** al telefono (l'e-mail l'ha già mandata lei: resta da decidere WhatsApp) e quelle per cui qualcuno ha scelto «Più tardi». **Avvisa** apre la finestra [Avvisa il paziente](MANUALE_UTENTE.md#lezione-gestire-appuntamenti); se gli avvisi sono più d'uno, **Avvisa uno dopo l'altro** li propone in fila.

#### Prossimi appuntamenti

L'elenco degli appuntamenti da ora in poi, con orario, paziente, prestazione, poltrona e stato. Le icone avvisano di un'**allerta clinica** (⚠), di una terapia in corso o di un **richiamo scaduto**. I pulsanti *Programmato*, *Confermato*, *Presente* filtrano l'elenco per stato.

Cliccando un appuntamento, a destra compare la sua scheda: motivo, trattamento, orario e poltrona, **alert clinici**, contatti del paziente e **scadenze** (richiami scaduti, preventivi in attesa). È il riassunto da leggere prima di chiamare il paziente o di farlo accomodare.

#### Da sapere

- Quante righe mostrare e quanti giorni considerare lo decide l'amministratore in Impostazioni → Sistema.
- Il menu del punto di vista (lezione successiva) cambia anche la dashboard: come segreteria vedi tutto lo studio.

#### Prova nel programma

Apri la dashboard, clicca il primo appuntamento della giornata e controlla se il paziente ha un'allerta clinica o una scadenza.

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

Con e-mail e WhatsApp il contatto si registra da solo (canale e «messaggio lasciato») e compare nello storico; se l'e-mail non parte, il programma lo dice e non registra niente. Il testo si cambia in [Impostazioni → Richiami](#lezione-impostazioni-documenti).

#### Da sapere

**Genera richiami** crea i richiami per i pazienti senza un controllo recente, con l'intervallo impostato dallo studio (sei mesi, se non è cambiato). Se un paziente ha già un richiamo aperto e ha superato anche il secondo intervallo, il richiamo diventa *Secondo richiamo* ad alta priorità. Nell'ambiente di prova nessun messaggio parte davvero verso i pazienti: l'e-mail arriva a te, e in WhatsApp scegli tu a chi mandarlo (i numeri dei pazienti sono fittizi).

#### Prova nel programma

Apri i richiami, prendi il primo *da contattare* ad alta priorità e registra una telefonata con esito *messaggio lasciato*.

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

<a id="lezione-copilot-limiti"></a>

## 8.3 Cosa fa il Copilot e cosa no

*Limiti, conferme e riservatezza delle conversazioni.*

Un assistente utile è anche un assistente di cui si conoscono i limiti.

**Per:** tutti.

#### Cosa fa

- Cerca e riassume i dati dello studio: agenda, pazienti, richiami, preventivi, piani; in modalità clinica anche la cartella.
- Prepara azioni ripetitive (spostare un appuntamento, creare un richiamo o un preventivo) e le esegue **solo dopo la tua conferma**.
- Ti segnala cose da fare, per esempio i richiami scaduti.

#### Cosa non fa

- **Non registra atti clinici**: non segna prestazioni come eseguite e non cambia l'odontogramma. Diagnosi, prescrizioni e note le prepara solo in modalità clinica, e solo come anteprima.
- **In modalità amministrativa non dà indicazioni cliniche**, nemmeno generiche: niente farmaci, terapie o valutazioni di rischio. Rimanda al medico.
- **Non ha l'ultima parola**: un'informazione del Copilot si verifica nella scheda da cui proviene, come un appunto di un collega. Le risposte possono contenere errori.
- **Non esce dallo studio**: vede solo i dati del tuo studio, con i permessi del tuo ruolo.

#### Riservatezza

Le domande e i dati necessari a rispondere vengono elaborati da un servizio di intelligenza artificiale esterno. Prima di uscire passano da un **filtro** dello studio che sostituisce nomi e dati identificativi con pseudonimi, e li rimette nella risposta. Anche così, la regola resta: **non scrivere nelle domande dati che non servono**, e nell'ambiente di prova solo pazienti inventati.

L'assistente si presenta come intelligenza artificiale (obbligo di trasparenza dell'AI Act europeo): non è una persona, e lo dice.

#### Prova nel programma

Chiedi al Copilot di segnare come eseguita una prestazione di un paziente: guarda come risponde, poi fallo tu dalla scheda di seduta.

<a id="lezione-ambiente-prova-studio"></a>

## 9.6 Ambiente di prova e amministrazione dell'account

*Esercitarsi senza toccare i dati veri; sedi, esportazione, chiusura.*

Per chi usa DentalCare Pro con i propri pazienti: provare senza rischi, gestire le sedi, esportare i dati e, se serve, chiudere l'account.

**Per:** titolare dello studio.

#### L'ambiente di prova dello studio

Quando è attivo, in alto compare il pulsante **Ambiente di prova**. Apre una copia dello studio con **pazienti di esempio**: i dati veri non si toccano. È il posto dove il personale nuovo si esercita e dove provi una funzione prima di usarla con i pazienti. Per tornare allo studio vero usa **Torna a …** in alto.

L'Academy funziona anche lì: le lezioni con **Prova ora** ti portano nell'ambiente di prova.

#### Amministrazione dell'account

Il titolare ha una pagina in più, **Amministrazione account**, per l'account nel suo insieme:

- **Cliniche** — crea, modifica o elimina una clinica (*Nuova clinica*, *Modifica dati della clinica*, *Elimina clinica*), ed entra in una clinica per completarne le impostazioni (orari, poltrone, documenti…). È l'unico posto in cui si creano cliniche;
- **Utenti** — aggiunge gli utenti di una sede: ricevono per e-mail una password temporanea;
- **Esportazione dei dati** — una copia completa dei dati, in un archivio protetto da una **password monouso** che compare una sola volta: va salvata subito;
- **Chiusura dell'account** — richiede prima di scaricare la copia dei dati, poi una conferma. La cancellazione definitiva avviene dopo un periodo di ripensamento, durante il quale si può annullare.

#### Da sapere

- La copia dei dati serve anche per gli obblighi del GDPR (portabilità) e prima di un trasferimento a un altro sistema.
- Nello studio di prova dell'Academy queste funzioni non ci sono: lo studio di prova scade da solo dopo 14 giorni, e viene cancellato con tutti i suoi dati dopo un ulteriore periodo.

#### Prova nel programma

Questa lezione descrive funzioni dello studio vero: nell'ambiente di prova non c'è niente da provare. Torna al [percorso del titolare](#lezione-percorso-titolare).

<a id="lezione-percorso-segreteria"></a>

## 2.1 Percorso della segreteria

*Agenda, accoglienza, preventivi, incassi e richiami, giorno per giorno.*

Il percorso di chi organizza lo studio: telefono, agenda, accoglienza, preventivi, incassi e richiami. Segui le tappe nell'ordine: ogni tappa rimanda alla lezione che la spiega.

**Per:** segreteria. Nell'ambiente di prova scegli **Segreteria** nel menu in alto.

#### 1. Le basi (primo giorno)

1. [L'interfaccia in un minuto](MANUALE_UTENTE.md#lezione-interfaccia) e [La dashboard](#lezione-dashboard).
2. [Trovare un paziente](MANUALE_UTENTE.md#lezione-cercare-paziente) e [Registrare un nuovo paziente](MANUALE_UTENTE.md#lezione-nuovo-paziente): la registrazione è un tuo compito.
3. [Le viste dell'agenda](MANUALE_UTENTE.md#lezione-viste-agenda) e [Fissare un appuntamento](MANUALE_UTENTE.md#lezione-nuovo-appuntamento).

#### 2. La giornata tipo

| Momento | Cosa fai | Lezione |
|---|---|---|
| Apertura | dashboard: appuntamenti di oggi, allerte, scadenze e pazienti **da avvisare** (prenotazioni fatte da Giulia al telefono) | [La dashboard](#lezione-dashboard) |
| Mattina | conferme telefoniche: lo stato passa a *Confermato* | [Gestire gli appuntamenti](MANUALE_UTENTE.md#lezione-gestire-appuntamenti) |
| Arrivo del paziente | lo segni **Presente**: il medico sa che è in sala | [Dal paziente in sala alla visita](MANUALE_UTENTE.md#lezione-inizia-visita) |
| Telefonate | nuovi appuntamenti, spostamenti, annullamenti; dopo ognuno, *Avvisa il paziente* (WhatsApp o e-mail) | [Gestire gli appuntamenti](MANUALE_UTENTE.md#lezione-gestire-appuntamenti) |
| Uscita del paziente | preventivo, acconto o fattura | [Preventivi](#lezione-preventivi), [Fatture](#lezione-fatturazione) |
| Pomeriggio | richiami da contattare: telefono, oppure il testo pronto per e-mail o WhatsApp | [I richiami](#lezione-richiami) |

#### 3. La settimana e il mese

- Preventivi **inviati** senza risposta e preventivi **fatturabili** (lavoro finito, non ancora fatturato): [Preventivi e avanzamento](#lezione-preventivi).
- Documenti da emettere, acconti, note di credito: [Fatture, acconti e storni](#lezione-fatturazione).
- Generazione dei richiami e contatti: [I richiami](#lezione-richiami).
- Scorte e carichi di magazzino: [Il magazzino](#lezione-magazzino).

#### 4. I casi particolari

- Il paziente non si presenta: [Paziente non presentato](MANUALE_UTENTE.md#lezione-paziente-non-presentato).
- Spostare un appuntamento legato a un piano di cura, o cambiare medico: [Spostare o annullare un appuntamento collegato](MANUALE_UTENTE.md#lezione-spostare-appuntamento-collegato).
- L'orario chiesto non è libero, è fuori orario o non è sulla griglia: [I vincoli dell'agenda](MANUALE_UTENTE.md#lezione-vincoli-agenda).
- Una fattura da correggere: [Fatture, acconti e storni](#lezione-fatturazione).

#### 5. Il Copilot come aiuto

Per te il Copilot è **amministrativo**: trova orari liberi, sposta appuntamenti (con conferma), dice chi richiamare. Non dà indicazioni cliniche. [Chiedere al Copilot](MANUALE_UTENTE.md#lezione-copilot).

#### Prova nel programma

Scegli **Segreteria** nel menu in alto, apri la dashboard e segui la tabella della giornata tipo dall'inizio alla fine.

<a id="lezione-percorso-medico"></a>

## 2.2 Percorso del medico

*Dalla prima visita alla fine della cura, con le sedute e i loro casi particolari.*

Il percorso del medico (dentista, chirurgo, ortodontista): dalla prima visita alla fine della cura, con le sedute e i loro casi particolari.

**Per:** medici. Nell'ambiente di prova sei la dottoressa Ferretti (dentista); per gli altri ruoli scegli il collega nel menu in alto.

#### 1. Le basi

1. [L'interfaccia](MANUALE_UTENTE.md#lezione-interfaccia), [La dashboard](#lezione-dashboard), [Medico, segreteria o amministratore](MANUALE_UTENTE.md#lezione-punto-di-vista).
2. [La scheda paziente](MANUALE_UTENTE.md#lezione-scheda-paziente) e [L'anamnesi e le allerte](MANUALE_UTENTE.md#lezione-anamnesi).

#### 2. Il ciclo di una cura

| Tappa | Cosa fai | Lezione |
|---|---|---|
| Prima visita | anamnesi, odontogramma, radiografie | [L'odontogramma](MANUALE_UTENTE.md#lezione-odontogramma), [Analisi AI delle radiografie](MANUALE_UTENTE.md#lezione-analisi-ai-radiografie) |
| Diagnosi | diagnosi e prescrizioni | [Diagnosi, prescrizioni e documenti](MANUALE_UTENTE.md#lezione-diagnosi-prescrizioni-documenti) |
| Piano | dal dente al piano di cura | [Genera piano di cura](MANUALE_UTENTE.md#lezione-genera-piano), [Il piano di cura](MANUALE_UTENTE.md#lezione-piano-di-cura) |
| Preventivo | la segreteria lo prepara dal piano; tu lo verifichi | [Preventivi e avanzamento](#lezione-preventivi) |
| Sedute | prenoti dal piano, esegui, registri | [Fissare un appuntamento](MANUALE_UTENTE.md#lezione-nuovo-appuntamento), [La scheda di seduta](MANUALE_UTENTE.md#lezione-scheda-seduta) |
| Controllo | cosa è cambiato visita dopo visita | [Lo storico degli episodi](MANUALE_UTENTE.md#lezione-storico-episodi) |

#### 3. La giornata in poltrona

1. Apri l'agenda o la dashboard: le **allerte** dei pazienti di oggi sono in evidenza.
2. Paziente *Presente* in sala → apri la **scheda di seduta** → **Inizia visita**: [Dal paziente in sala alla visita in corso](MANUALE_UTENTE.md#lezione-inizia-visita).
3. A fine visita registra gli esiti e chiudi la seduta: [La scheda di seduta](MANUALE_UTENTE.md#lezione-scheda-seduta).
4. Le sedute rimaste da registrare le trovi in **Già trascorsi oggi**.

#### 4. I casi particolari delle sedute

- La prestazione prevista non si fa: [Prestazione rinviata o non eseguita](MANUALE_UTENTE.md#lezione-prestazione-rinviata).
- Fai qualcosa che non era previsto, o registri la seduta di un collega: [Seduta fuori programma](MANUALE_UTENTE.md#lezione-seduta-fuori-programma).
- Hai dimenticato di iniziare la visita o di registrare la seduta: [Seduta dimenticata o già chiusa](MANUALE_UTENTE.md#lezione-seduta-dimenticata).
- Il paziente non è venuto: [Paziente non presentato](MANUALE_UTENTE.md#lezione-paziente-non-presentato).
- L'appuntamento va spostato ma è legato al piano: [Spostare o annullare un appuntamento collegato](MANUALE_UTENTE.md#lezione-spostare-appuntamento-collegato).
- Paziente con condizione a rischio infettivo, conflitti d'orario: [I vincoli dell'agenda](MANUALE_UTENTE.md#lezione-vincoli-agenda).

#### 5. Il Copilot clinico

Per te il Copilot legge anche anamnesi, odontogramma e piani, e prepara scritture cliniche da confermare: [Copilot clinico](MANUALE_UTENTE.md#lezione-copilot-clinico) e [Cosa fa il Copilot e cosa no](#lezione-copilot-limiti).

#### 6. Le tue impostazioni

In **Impostazioni** trovi le tue schede personali; dove non imposti nulla valgono quelle dello studio:

- **Le mie tariffe** — prezzi tuoi diversi dal listino, se lo studio fattura a nome dei medici: [Le tariffe del medico](MANUALE_UTENTE.md#lezione-tariffe-medico);
- **I miei richiami** — intervalli e testo dei richiami per i pazienti la cui ultima visita è stata con te;
- **La mia fatturazione** — metodo di pagamento, scadenza, prefisso e IBAN delle parcelle a tuo nome;
- **Il mio calendario** — i giorni e le ore in cui sei in sede e le assenze: [Calendario delle presenze](MANUALE_UTENTE.md#lezione-calendario-presenze).

#### Prova nel programma

Apri la scheda di *Alessandro Neri*: guarda l'odontogramma, genera un piano di cura e prenota la prima prestazione. È il ciclo della cura in tre gesti.

<a id="lezione-percorso-igienista"></a>

## 2.3 Percorso dell'igienista

*Sedute di igiene, mantenimento, richiami e collaborazione con il medico.*

Il percorso dell'igienista: sedute di igiene e mantenimento, richiami periodici, collaborazione con il medico.

**Per:** igienisti. Nell'ambiente di prova scegli **Gentili Michele — Igienista** nel menu in alto.

#### 1. Le basi

1. [L'interfaccia](MANUALE_UTENTE.md#lezione-interfaccia) e [La dashboard](#lezione-dashboard).
2. [La scheda paziente](MANUALE_UTENTE.md#lezione-scheda-paziente) e [L'anamnesi e le allerte](MANUALE_UTENTE.md#lezione-anamnesi): prima di ogni seduta leggi le allerte (anticoagulanti, cardiopatie, allergie).

#### 2. La seduta di igiene

1. Paziente *Presente* → apri la **scheda di seduta** → **Inizia visita**: [Dal paziente in sala alla visita in corso](MANUALE_UTENTE.md#lezione-inizia-visita).
2. Registra l'esito delle prestazioni (igiene professionale, levigatura, fluoroprofilassi) e chiudi: [La scheda di seduta](MANUALE_UTENTE.md#lezione-scheda-seduta).
3. Se trovi qualcosa da segnalare al medico (una carie, una lesione), aggiorna l'odontogramma o scrivi nel diario clinico: [L'odontogramma](MANUALE_UTENTE.md#lezione-odontogramma), [Diagnosi, prescrizioni e documenti](MANUALE_UTENTE.md#lezione-diagnosi-prescrizioni-documenti).

#### 3. Il mantenimento

- Il richiamo successivo (sei mesi, di norma): [I richiami](#lezione-richiami).
- La prenotazione della seduta successiva: [Fissare un appuntamento](MANUALE_UTENTE.md#lezione-nuovo-appuntamento).

#### 4. I casi particolari

- [Prestazione rinviata o non eseguita](MANUALE_UTENTE.md#lezione-prestazione-rinviata) (per esempio paziente con sanguinamento che richiede il parere del medico).
- [Seduta fuori programma](MANUALE_UTENTE.md#lezione-seduta-fuori-programma): una fluoroprofilassi non prevista.
- [Paziente non presentato](MANUALE_UTENTE.md#lezione-paziente-non-presentato).

#### 5. Il Copilot

Per l'igienista il Copilot è **amministrativo**: agenda, richiami, anagrafica. Non legge i dati clinici e non dà indicazioni cliniche: per quelle c'è il medico. [Cosa fa il Copilot e cosa no](#lezione-copilot-limiti).

#### Prova nel programma

Scegli **Gentili Michele — Igienista** nel menu in alto e apri l'agenda: trova la prossima seduta di igiene e apri la sua scheda di seduta.
