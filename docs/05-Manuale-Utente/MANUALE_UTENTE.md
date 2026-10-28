# DentalCare Pro — Manuale utente

> Versione 28 ottobre 2026. Generato dalle lezioni dell'**Academy**, il manuale ufficiale dentro il programma (`tools/genera_manuale.py`): per correggerlo si corregge la lezione e si rigenera. Le schermate vengono dall'ambiente dimostrativo: nomi e dati dei pazienti sono fittizi.

## Indice

1. [Primi passi](#modulo-primi-passi) — Com'è fatto l'ambiente di prova, come ci si muove, chi sei e come si entra.
   - [1.1 Benvenuto nella prova](#lezione-benvenuto)
   - [1.2 L'interfaccia in un minuto](#lezione-interfaccia)
   - [1.3 La dashboard](#lezione-dashboard)
   - [1.4 Medico, segreteria o amministratore](#lezione-punto-di-vista)
   - [1.5 Accesso e password](#lezione-accesso-e-password)
2. [Percorsi di lavoro](#modulo-percorsi) — Le tappe per ruolo, dalle basi ai casi particolari: da qui si sceglie cosa studiare.
   - [2.1 Percorso della segreteria](#lezione-percorso-segreteria)
   - [2.2 Percorso del medico](#lezione-percorso-medico)
   - [2.3 Percorso dell'igienista](#lezione-percorso-igienista)
   - [2.4 Percorso del titolare](#lezione-percorso-titolare)
   - [2.5 Il viaggio del paziente](#lezione-percorso-paziente)
3. [Pazienti](#modulo-pazienti) — Trovare, registrare e conoscere un paziente, anamnesi compresa.
   - [3.1 Trovare un paziente](#lezione-cercare-paziente)
   - [3.2 Registrare un nuovo paziente](#lezione-nuovo-paziente)
   - [3.3 La scheda paziente](#lezione-scheda-paziente)
   - [3.4 L'anamnesi e le allerte](#lezione-anamnesi)
4. [Agenda e seduta](#modulo-agenda-e-seduta) — Dalla prenotazione alla registrazione di ciò che è stato fatto in poltrona.
   - [4.1 Le viste dell'agenda](#lezione-viste-agenda)
   - [4.2 Fissare un appuntamento](#lezione-nuovo-appuntamento)
   - [4.3 Gestire gli appuntamenti](#lezione-gestire-appuntamenti)
   - [4.4 Dal paziente in sala alla visita in corso](#lezione-inizia-visita)
   - [4.5 La scheda di seduta](#lezione-scheda-seduta)
5. [Sedute: casi particolari](#modulo-sedute-casi-particolari) — Quando le cose non vanno come previsto: assenze, rinvii, spostamenti, dimenticanze, vincoli.
   - [5.1 Paziente non presentato](#lezione-paziente-non-presentato)
   - [5.2 Prestazione rinviata o non eseguita](#lezione-prestazione-rinviata)
   - [5.3 Seduta fuori programma](#lezione-seduta-fuori-programma)
   - [5.4 Seduta dimenticata o già chiusa](#lezione-seduta-dimenticata)
   - [5.5 Spostare o annullare un appuntamento collegato](#lezione-spostare-appuntamento-collegato)
   - [5.6 I vincoli dell'agenda](#lezione-vincoli-agenda)
6. [Clinica](#modulo-clinica) — Odontogramma, piani di cura, storico degli episodi, documenti e analisi AI.
   - [6.1 L'odontogramma](#lezione-odontogramma)
   - [6.2 Dal dente al piano: «Genera piano di cura»](#lezione-genera-piano)
   - [6.3 Il piano di cura](#lezione-piano-di-cura)
   - [6.4 Lo storico degli episodi](#lezione-storico-episodi)
   - [6.5 Diagnosi, prescrizioni e documenti](#lezione-diagnosi-prescrizioni-documenti)
   - [6.6 Analisi AI delle radiografie](#lezione-analisi-ai-radiografie)
7. [Amministrazione](#modulo-amministrazione) — Preventivi, fatture, richiami, magazzino, listino e tariffe.
   - [7.1 Preventivi e avanzamento](#lezione-preventivi)
   - [7.2 Fatture, acconti e storni](#lezione-fatturazione)
   - [7.3 I richiami](#lezione-richiami)
   - [7.4 Il magazzino](#lezione-magazzino)
   - [7.5 Prestazioni e listino](#lezione-prestazioni-listino)
   - [7.6 Le tariffe del medico](#lezione-tariffe-medico)
8. [Copilot AI](#modulo-copilot) — L'assistente che legge i dati dello studio: modalità, domande, conferme e limiti.
   - [8.1 Chiedere al Copilot](#lezione-copilot)
   - [8.2 Copilot clinico](#lezione-copilot-clinico)
   - [8.3 Cosa fa il Copilot e cosa no](#lezione-copilot-limiti)
9. [Impostazioni della clinica](#modulo-impostazioni) — Per il titolare e l'amministratore: dati, persone, agenda, documenti, Copilot.
   - [9.1 Clinica e professionisti](#lezione-impostazioni-studio)
   - [9.2 Agenda e visibilità](#lezione-impostazioni-agenda)
   - [9.3 Calendario delle presenze](#lezione-calendario-presenze)
   - [9.4 Preventivi, fatture, richiami e sistema](#lezione-impostazioni-documenti)
   - [9.5 Copilot e AI](#lezione-impostazioni-ai)
   - [9.6 Ambiente di prova e amministrazione dell'account](#lezione-ambiente-prova-studio)
10. [Riferimento](#modulo-riferimento) — Le parole del programma, con il loro significato preciso.
   - [10.1 Glossario](#lezione-glossario)

---

<a id="modulo-primi-passi"></a>

## 1. Primi passi

*Com'è fatto l'ambiente di prova, come ci si muove, chi sei e come si entra.*

<a id="lezione-benvenuto"></a>

### 1.1 Benvenuto nella prova

*Cosa trovi nel tuo ambiente e come usare l'Academy.*

Questo è il **tuo** ambiente di prova di DentalCare Pro. È uno studio completo, già avviato: pazienti con la loro storia clinica, un'agenda piena, piani di cura, preventivi, fatture, richiami e magazzino. Il medico principale dello studio sei tu: appuntamenti, visite e piani a nome della dottoressa Ferretti sono i tuoi.

L'Academy è il **manuale del corso**: ogni lezione spiega una funzione o un caso, e i **percorsi di lavoro** mettono in fila le lezioni per ruolo, dal primo giorno ai casi particolari.

#### Come usare l'Academy

1. Leggi le lezioni di **Primi passi** (questa e le tre successive): bastano dieci minuti.
2. Scegli il **percorso** del tuo ruolo: [segreteria](#lezione-percorso-segreteria), [medico](#lezione-percorso-medico), [igienista](#lezione-percorso-igienista) o [titolare dello studio](#lezione-percorso-titolare).
3. Ogni lezione finisce con **Prova ora**, che ti porta nel punto esatto dell'applicazione di cui parla.

#### Cosa puoi fare nell'ambiente di prova

- **Tutto.** Crea pazienti, sposta appuntamenti, registra sedute, emetti fatture. Niente esce dall'ambiente: nessun paziente riceve messaggi o e-mail. Le e-mail destinate ai pazienti, come l'invio di una fattura, arrivano a te, all'indirizzo con cui hai attivato la prova.
- **Guardare lo studio con gli occhi degli altri.** Dal menu in alto a destra puoi diventare la segreteria, un collega o l'amministratore dello studio: lo spiega la lezione [Medico, segreteria o amministratore](#lezione-punto-di-vista).
- **Ricominciare da capo.** Dalla pagina iniziale dell'Academy, **Ripristina i dati di esempio** riporta lo studio com'era il primo giorno, con le date di oggi (fino a 10 volte al giorno). I tuoi progressi nell'Academy restano.

#### Da sapere

- La prova dura **14 giorni**. I giorni che restano sono indicati in alto, accanto ad *Ambiente demo*.
- È un ambiente dimostrativo: **non inserire dati di pazienti reali**. I pazienti che trovi sono inventati.
- Gli altri professionisti (un chirurgo, un'ortodontista, un igienista, la segreteria) servono a rendere lo studio realistico: non possono accedere, l'ambiente è solo tuo. Per lo stesso motivo nello studio di prova i professionisti non hanno un indirizzo e-mail.

#### Prova nel programma

Apri la dashboard e guarda cosa c'è in programma oggi. Poi torna qui: la prossima lezione spiega com'è fatta l'interfaccia.

<a id="lezione-interfaccia"></a>

### 1.2 L'interfaccia in un minuto

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

### 1.3 La dashboard

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

<a id="lezione-punto-di-vista"></a>

### 1.4 Medico, segreteria o amministratore

*Guardare la clinica con gli occhi degli altri ruoli; il Copilot segue la persona.*

In uno studio vero medico, igienista, segreteria e amministratore usano lo stesso programma in modo diverso. Nell'ambiente di prova li provi tutti senza cambiare utente.

**Per:** chi usa l'ambiente di prova o lo studio dimostrativo.

#### Il menu in alto

In alto, accanto alla campanella, c'è un menu a tendina con il ruolo di ognuno tra parentesi:

- **Il tuo nome — Dentista**: la vista del medico, con agenda, pazienti e cartella clinica.
- **Gli altri professionisti** (ortodontista, chirurgo, igienista): lo studio dal loro punto di vista.
- **Segreteria**: l'intero studio, tutti gli appuntamenti e i pazienti, preventivi e fatture di tutti.
- **Il tuo nome — Amministratore**: le **Impostazioni** dello studio (orari, slot, professionisti, fatturazione, Copilot). Solo nel tuo studio di prova.

Il cambio è immediato e non richiede di uscire.

#### Cosa cambia davvero

- **Le schermate**: ogni ruolo vede le sue voci di menu e i suoi dati. La **scheda di seduta** e lo **storico degli episodi** sono clinici; la **registrazione di un nuovo paziente** è un compito della segreteria.
- **Il Copilot**: risponde come la persona scelta. Con un medico è **clinico** (legge anamnesi, odontogramma, piani); con igienista e segreteria è **amministrativo** (agenda, anagrafica, preventivi, fatture, richiami). Lo spiega la lezione [Copilot clinico](#lezione-copilot-clinico).
- **Con Amministratore** compaiono le Impostazioni, e il server ti riconosce come amministratore del solo studio di prova.

#### Da sapere

Il menu cambia **cosa vedi e come risponde il Copilot**, non **chi firma**: ciò che registri (una seduta, una nota) resta a tuo nome. In uno studio vero ognuno entra con le proprie credenziali.

#### Prova nel programma

Apri l'agenda, scegli **Segreteria** e guarda come cambiano gli appuntamenti mostrati. Poi passa a **Amministratore** e apri le Impostazioni dal menu. Torna infine al tuo nome.

<a id="lezione-accesso-e-password"></a>

### 1.5 Accesso e password

*Primo accesso, password temporanea, password dimenticata.*

Come si entra, come si cambia la password e cosa fare se la si dimentica.

**Per:** tutti.

#### Il primo accesso

1. Nella pagina di accesso scrivi e-mail e password. Al primo ingresso la password è **temporanea**: l'hai ricevuta per e-mail quando è stato creato il tuo account.
2. Il programma chiede subito una **password definitiva** (almeno 8 caratteri), da scrivere due volte. Fino a quel momento non si prosegue.

Se la stessa e-mail appartiene a più studi o sedi, dopo la password scegli **dove vuoi accedere**.

#### Password dimenticata

1. Nella pagina di accesso premi **Password dimenticata?** e scrivi la tua e-mail.
2. Ricevi un **codice temporaneo**, valido **30 minuti**. Se l'e-mail non arriva, guarda anche nella posta indesiderata.
3. Entra scrivendo il codice al posto della password: il programma ti chiede subito di sceglierne una nuova.

#### Casi particolari

- **Non sei stato tu a chiedere il codice?** Ignora l'e-mail: la tua password continua a funzionare. Il codice smette di valere dopo 30 minuti o appena scegli una nuova password.
- **Hai chiesto il codice due volte?** Vale solo l'ultimo.
- **Il codice è scaduto?** Ripeti la richiesta: ne arriva uno nuovo.
- **La prova è terminata?** All'accesso compare *La tua prova è terminata*: i dati restano per un periodo, poi l'ambiente viene cancellato.

#### Da sapere

- Per motivi di sicurezza la pagina risponde allo stesso modo anche quando l'e-mail non è registrata: non rivela chi ha un account.
- Le e-mail del programma arrivano dal mittente dello studio, con il logo DentalCare Pro: diffida di messaggi che chiedono la password in altro modo.

#### Prova nel programma

Esci dal programma (dal tuo nome in alto a destra) e prova **Password dimenticata?** con il tuo indirizzo. Rientra pure con la tua password: resta valida.

---

<a id="modulo-percorsi"></a>

## 2. Percorsi di lavoro

*Le tappe per ruolo, dalle basi ai casi particolari: da qui si sceglie cosa studiare.*

<a id="lezione-percorso-segreteria"></a>

### 2.1 Percorso della segreteria

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

<a id="lezione-percorso-medico"></a>

### 2.2 Percorso del medico

*Dalla prima visita alla fine della cura, con le sedute e i loro casi particolari.*

Il percorso del medico (dentista, chirurgo, ortodontista): dalla prima visita alla fine della cura, con le sedute e i loro casi particolari.

**Per:** medici. Nell'ambiente di prova sei la dottoressa Ferretti (dentista); per gli altri ruoli scegli il collega nel menu in alto.

#### 1. Le basi

1. [L'interfaccia](#lezione-interfaccia), [La dashboard](#lezione-dashboard), [Medico, segreteria o amministratore](#lezione-punto-di-vista).
2. [La scheda paziente](#lezione-scheda-paziente) e [L'anamnesi e le allerte](#lezione-anamnesi).

#### 2. Il ciclo di una cura

| Tappa | Cosa fai | Lezione |
|---|---|---|
| Prima visita | anamnesi, odontogramma, radiografie | [L'odontogramma](#lezione-odontogramma), [Analisi AI delle radiografie](#lezione-analisi-ai-radiografie) |
| Diagnosi | diagnosi e prescrizioni | [Diagnosi, prescrizioni e documenti](#lezione-diagnosi-prescrizioni-documenti) |
| Piano | dal dente al piano di cura | [Genera piano di cura](#lezione-genera-piano), [Il piano di cura](#lezione-piano-di-cura) |
| Preventivo | la segreteria lo prepara dal piano; tu lo verifichi | [Preventivi e avanzamento](#lezione-preventivi) |
| Sedute | prenoti dal piano, esegui, registri | [Fissare un appuntamento](#lezione-nuovo-appuntamento), [La scheda di seduta](#lezione-scheda-seduta) |
| Controllo | cosa è cambiato visita dopo visita | [Lo storico degli episodi](#lezione-storico-episodi) |

#### 3. La giornata in poltrona

1. Apri l'agenda o la dashboard: le **allerte** dei pazienti di oggi sono in evidenza.
2. Paziente *Presente* in sala → apri la **scheda di seduta** → **Inizia visita**: [Dal paziente in sala alla visita in corso](#lezione-inizia-visita).
3. A fine visita registra gli esiti e chiudi la seduta: [La scheda di seduta](#lezione-scheda-seduta).
4. Le sedute rimaste da registrare le trovi in **Già trascorsi oggi**.

#### 4. I casi particolari delle sedute

- La prestazione prevista non si fa: [Prestazione rinviata o non eseguita](#lezione-prestazione-rinviata).
- Fai qualcosa che non era previsto, o registri la seduta di un collega: [Seduta fuori programma](#lezione-seduta-fuori-programma).
- Hai dimenticato di iniziare la visita o di registrare la seduta: [Seduta dimenticata o già chiusa](#lezione-seduta-dimenticata).
- Il paziente non è venuto: [Paziente non presentato](#lezione-paziente-non-presentato).
- L'appuntamento va spostato ma è legato al piano: [Spostare o annullare un appuntamento collegato](#lezione-spostare-appuntamento-collegato).
- Paziente con condizione a rischio infettivo, conflitti d'orario: [I vincoli dell'agenda](#lezione-vincoli-agenda).

#### 5. Il Copilot clinico

Per te il Copilot legge anche anamnesi, odontogramma e piani, e prepara scritture cliniche da confermare: [Copilot clinico](#lezione-copilot-clinico) e [Cosa fa il Copilot e cosa no](#lezione-copilot-limiti).

#### 6. Le tue impostazioni

In **Impostazioni** trovi le tue schede personali; dove non imposti nulla valgono quelle dello studio:

- **Le mie tariffe** — prezzi tuoi diversi dal listino, se lo studio fattura a nome dei medici: [Le tariffe del medico](#lezione-tariffe-medico);
- **I miei richiami** — intervalli e testo dei richiami per i pazienti la cui ultima visita è stata con te;
- **La mia fatturazione** — metodo di pagamento, scadenza, prefisso e IBAN delle parcelle a tuo nome;
- **Il mio calendario** — i giorni e le ore in cui sei in sede e le assenze: [Calendario delle presenze](#lezione-calendario-presenze).

#### Prova nel programma

Apri la scheda di *Alessandro Neri*: guarda l'odontogramma, genera un piano di cura e prenota la prima prestazione. È il ciclo della cura in tre gesti.

<a id="lezione-percorso-igienista"></a>

### 2.3 Percorso dell'igienista

*Sedute di igiene, mantenimento, richiami e collaborazione con il medico.*

Il percorso dell'igienista: sedute di igiene e mantenimento, richiami periodici, collaborazione con il medico.

**Per:** igienisti. Nell'ambiente di prova scegli **Gentili Michele — Igienista** nel menu in alto.

#### 1. Le basi

1. [L'interfaccia](#lezione-interfaccia) e [La dashboard](#lezione-dashboard).
2. [La scheda paziente](#lezione-scheda-paziente) e [L'anamnesi e le allerte](#lezione-anamnesi): prima di ogni seduta leggi le allerte (anticoagulanti, cardiopatie, allergie).

#### 2. La seduta di igiene

1. Paziente *Presente* → apri la **scheda di seduta** → **Inizia visita**: [Dal paziente in sala alla visita in corso](#lezione-inizia-visita).
2. Registra l'esito delle prestazioni (igiene professionale, levigatura, fluoroprofilassi) e chiudi: [La scheda di seduta](#lezione-scheda-seduta).
3. Se trovi qualcosa da segnalare al medico (una carie, una lesione), aggiorna l'odontogramma o scrivi nel diario clinico: [L'odontogramma](#lezione-odontogramma), [Diagnosi, prescrizioni e documenti](#lezione-diagnosi-prescrizioni-documenti).

#### 3. Il mantenimento

- Il richiamo successivo (sei mesi, di norma): [I richiami](#lezione-richiami).
- La prenotazione della seduta successiva: [Fissare un appuntamento](#lezione-nuovo-appuntamento).

#### 4. I casi particolari

- [Prestazione rinviata o non eseguita](#lezione-prestazione-rinviata) (per esempio paziente con sanguinamento che richiede il parere del medico).
- [Seduta fuori programma](#lezione-seduta-fuori-programma): una fluoroprofilassi non prevista.
- [Paziente non presentato](#lezione-paziente-non-presentato).

#### 5. Il Copilot

Per l'igienista il Copilot è **amministrativo**: agenda, richiami, anagrafica. Non legge i dati clinici e non dà indicazioni cliniche: per quelle c'è il medico. [Cosa fa il Copilot e cosa no](#lezione-copilot-limiti).

#### Prova nel programma

Scegli **Gentili Michele — Igienista** nel menu in alto e apri l'agenda: trova la prossima seduta di igiene e apri la sua scheda di seduta.

<a id="lezione-percorso-titolare"></a>

### 2.4 Percorso del titolare

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

<a id="lezione-percorso-paziente"></a>

### 2.5 Il viaggio del paziente

*Dal primo contatto al richiamo di controllo: chi fa cosa, e dove.*

Il viaggio del paziente nello studio, dal primo contatto alla fine della cura e al controllo successivo. È il filo che lega il lavoro di tutti i ruoli: per ogni tappa, chi la fa e dove.

**Per:** tutti. Utile soprattutto per capire come il lavoro di uno diventa il punto di partenza dell'altro.

#### Le tappe

| # | Tappa | Chi | Dove |
|---|---|---|---|
| 1 | Primo contatto e registrazione | segreteria | [Registrare un nuovo paziente](#lezione-nuovo-paziente) |
| 2 | Prima visita fissata | segreteria | [Fissare un appuntamento](#lezione-nuovo-appuntamento) |
| 3 | Conferma e arrivo (*Confermato*, *Presente*) | segreteria | [Gestire gli appuntamenti](#lezione-gestire-appuntamenti) |
| 4 | Anamnesi | medico | [L'anamnesi e le allerte](#lezione-anamnesi) |
| 5 | Visita: odontogramma, radiografie | medico | [L'odontogramma](#lezione-odontogramma), [Analisi AI delle radiografie](#lezione-analisi-ai-radiografie) |
| 6 | Piano di cura | medico | [Genera piano di cura](#lezione-genera-piano) |
| 7 | Preventivo e accettazione | segreteria | [Preventivi e avanzamento](#lezione-preventivi) |
| 8 | Sedute di cura, prenotate dal piano | segreteria e medico | [Il piano di cura](#lezione-piano-di-cura), [La scheda di seduta](#lezione-scheda-seduta) |
| 9 | Acconti e fattura finale | segreteria | [Fatture, acconti e storni](#lezione-fatturazione) |
| 10 | Richiamo di controllo | segreteria, igienista | [I richiami](#lezione-richiami) |

#### Cosa tiene insieme le tappe

- Il **piano di cura** collega preventivo, appuntamenti e sedute: ogni prestazione sa se è da pianificare, con appuntamento fissato, completata, in sospeso o annullata.
- Le **allerte** dell'anamnesi seguono il paziente in dashboard, agenda e scheda di seduta.
- Lo **storico degli episodi** fotografa il paziente prima e dopo ogni visita.

#### Dove il viaggio si interrompe

Un paziente che non si presenta, una prestazione rinviata, un appuntamento da spostare: sono i casi del modulo **Sedute: casi particolari**, a partire da [Paziente non presentato](#lezione-paziente-non-presentato).

#### Prova nel programma

Segui *Luca Romano*: scheda paziente, piano di cura, preventivo, appuntamenti. Ritrovi le tappe 4-9 di questa tabella.

---

<a id="modulo-pazienti"></a>

## 3. Pazienti

*Trovare, registrare e conoscere un paziente, anamnesi compresa.*

<a id="lezione-cercare-paziente"></a>

### 3.1 Trovare un paziente

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

### 3.2 Registrare un nuovo paziente

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

<a id="lezione-scheda-paziente"></a>

### 3.3 La scheda paziente

*Le schede della cartella e gli appuntamenti del paziente.*

La scheda paziente raccoglie tutto ciò che riguarda una persona, diviso in schede.

**Per:** tutti. Alla segreteria non compaiono le schede cliniche: Cartella Clinica, Storico episodi, Anamnesi e Odontogramma.

#### Le schede

| Scheda | Cosa contiene |
|--------|---------------|
| **Panoramica** | anagrafica, contatti, indicatori clinici e lo storico degli appuntamenti |
| **Cartella Clinica** | il diario clinico, visita per visita |
| **Storico episodi** | la situazione prima e dopo ogni visita (solo ruoli clinici) |
| **Anamnesi** | la storia medica, con le allerte |
| **Odontogramma** | la mappa dei denti |
| **Piani di Cura** | le terapie previste e il loro avanzamento |
| **Richiami**, **Preventivi**, **Documenti** | ciò che il nome dice |

In testa, accanto al nome, compaiono le **allerte** (per esempio un'allergia) e, quando c'è, l'episodio aperto: *Visita in corso* o *Contatto aperto*.

#### Gli appuntamenti del paziente

Nella Panoramica c'è l'elenco degli appuntamenti del paziente, dal più recente, con **+ Nuovo** per fissarne un altro. Da ogni riga:

- **cambi lo stato** dal menu a tendina: *Programmato*, *Confermato*, *Presente* (in sala d'attesa), *In corso* (in poltrona: avvia la visita), *Completato*, *Cancellato*, *Non presentato*;
- **modifichi** data, ora di inizio e fine e poltrona (icona del calendario con la matita);
- **cancelli** l'appuntamento (icona del calendario barrato), dopo una conferma.

Cosa succede in ognuno di questi casi, soprattutto se l'appuntamento è legato a un piano di cura, lo spiegano [Gestire gli appuntamenti](#lezione-gestire-appuntamenti) e il modulo **Sedute: casi particolari**.

#### Prova nel programma

Apri la scheda di *Marco Rossi* e passa da una scheda all'altra. Quante visite ha avuto negli ultimi mesi?

<a id="lezione-anamnesi"></a>

### 3.4 L'anamnesi e le allerte

*Compilare l'anamnesi e far comparire le allerte dove servono.*

L'anamnesi è la storia medica del paziente. In DentalCare Pro è organizzata per categorie (cardiovascolare, allergie, farmaci…) con voci da spuntare.

**Per:** medici e igienisti. La segreteria non vede la scheda Anamnesi, ma le **allerte** le compaiono dove servono (dashboard, agenda).

#### Come si compila

1. Nella scheda **Anamnesi** premi **Modifica anamnesi**.
2. Apri le categorie che ti servono e spunta le voci che valgono per il paziente; per ognuna puoi aggiungere una nota.
3. Indica il gruppo sanguigno e le note generali.
4. Premi **Salva**.

#### Le allerte

Alcune voci sono marcate come **allerta**: allergie (penicillina, lattice, anestetico), anticoagulanti, bifosfonati, diabete, patologie cardiache. Una voce d'allerta non resta chiusa nell'anamnesi: compare in testa alla scheda paziente, nella dashboard, nell'agenda e soprattutto nella **scheda di seduta**, sopra ogni altra cosa. È il modo per non dimenticarla quando conta.

#### Da sapere

- Ogni salvataggio conserva la versione precedente: l'anamnesi ha una sua storia.
- Se modifichi l'anamnesi quando per il paziente non c'è una visita in corso, il programma ti chiede se aprire un episodio. Lo vedrai nella lezione sullo storico degli episodi.

#### Prova nel programma

Apri l'anamnesi di *Marco Rossi*, aggiungi un'allergia al lattice e salva. Poi guarda la testata della scheda: l'allerta è lì.

---

<a id="modulo-agenda-e-seduta"></a>

## 4. Agenda e seduta

*Dalla prenotazione alla registrazione di ciò che è stato fatto in poltrona.*

<a id="lezione-viste-agenda"></a>

### 4.1 Le viste dell'agenda

*Prossimi, giorno, settimana, mese; stati, filtri e griglia degli slot.*

![La vista Giorno: una colonna per poltrona, i pulsanti per scegliere le poltrone mostrate, una riga tratteggiata per ogni slot.](img/academy/03-segreteria-agenda.png)

*La vista Giorno: una colonna per poltrona, i pulsanti per scegliere le poltrone mostrate, una riga tratteggiata per ogni slot.*

L'agenda mostra gli appuntamenti dello studio in quattro modi, scelti dalla barra in alto.

**Per:** tutti. Il medico e l'igienista vedono i propri appuntamenti; segreteria e amministratore l'intero studio.

#### Le viste

- **Prossimi** — gli appuntamenti da ora in poi, in ordine di orario, con il pulsante **Seduta** per i ruoli clinici. In fondo, **Già trascorsi oggi** raccoglie quelli finiti: è il posto dove registrare le sedute a fine mattinata.
- **Giorno** — la griglia oraria, una colonna per poltrona. Le ore sono quelle di lavoro dello studio e una linea tratteggiata segna ogni **slot** (per esempio ogni 15 minuti). La linea rossa è l'ora attuale. Le poltrone sono quelle attive della clinica, nell'ordine e con i colori dell'anagrafica ([Impostazioni → Anagrafiche → Poltrone](#lezione-impostazioni-studio)). Se non ci stanno tutte, l'agenda scorre in orizzontale e la colonna degli orari resta ferma; con i pulsanti **Poltrone** sopra la griglia scegli quali mostrare (la scelta resta su quel computer o tablet).
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

### 4.2 Fissare un appuntamento

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

Fissa un controllo per *Marco Rossi* con **Proponi orario**. Poi apri il piano di cura di *Silvia Conti* (lezione [Il piano di cura](#lezione-piano-di-cura)) e prova **Pianifica appuntamento** su una prestazione da pianificare: confronta le due strade.

<a id="lezione-gestire-appuntamenti"></a>

### 4.3 Gestire gli appuntamenti

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

### 4.4 Dal paziente in sala alla visita in corso

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

<a id="lezione-scheda-seduta"></a>

### 4.5 La scheda di seduta

*Registrare gli esiti e chiudere la seduta.*

![Gli esiti di una seduta prima della registrazione.](img/academy/13-scheda-seduta-esiti.png)

*Gli esiti di una seduta prima della registrazione.*

La scheda di seduta è la schermata del medico con il paziente in poltrona: dice **cosa fare oggi** e registra **cosa è stato fatto**.

**Per:** medici e igienisti.

#### Cosa mostra

In alto paziente, data, orario, poltrona e medico e, in evidenza, gli **alert clinici**. Il pulsante **Scheda paziente** apre una sintesi sopra la seduta, senza uscire: allerte e anamnesi, odontogramma attuale (con i denti di oggi evidenziati), piani di cura aperti, ultime visite. Si chiude con la ✕ o con Esc.

Sotto, la seduta si legge in **tre passi numerati**. Il passo a cui sei arrivato è evidenziato; gli altri restano usabili.

#### 1 · Prima della visita

Le prestazioni previste per oggi, ognuna con dente, superfici, note e l'etichetta del **piano di cura** da cui viene. **Aggiungi prestazione** elenca le prestazioni aperte del paziente **raggruppate per piano** (con «Tutte» per prenderle tutte); toglierne una dalla seduta la lascia nel piano. Quando il paziente è in poltrona premi **Inizia visita**.

#### 2 · Esito

Per ogni prestazione scegli un esito con i tre pulsanti, e una nota se serve:

| Esito | Cosa succede nel piano |
|-------|------------------------|
| **Eseguita** | la prestazione è completata, con data e nome di chi l'ha fatta |
| **Rinviata** | resta aperta, da rifissare |
| **Non eseguita** | resta aperta, con il motivo |

Nessun esito è preselezionato: una prestazione eseguita è una dichiarazione clinica, la fai tu. Un secondo clic sullo stesso esito lo toglie.

#### 3 · Odontogramma

Qui compaiono le prestazioni **eseguite su un dente**. Per ognuna vedi lo stato attuale del dente e la **proposta** del listino (per esempio *carie → otturato*): premi **Applica**, scegli un altro stato, oppure non fare nulla. **Se non fai nulla, il dente resta com'è.** A destra della riga leggi cosa succederà: «Diventerà: …» oppure «Resta invariato».

#### Registrare e chiudere

In fondo alla pagina, sempre visibile, il riepilogo (quante eseguite, rinviate, senza esito) e i due pulsanti:

- **Registra seduta** dichiara gli esiti, dopo un **riepilogo** da leggere prima di confermare. Nel riepilogo c'è la casella **Chiudi anche la seduta**, mai spuntata in partenza: spuntala se hai finito.
- **Chiudi seduta** porta l'appuntamento a *Completato*.

Sono due cose diverse: puoi registrare gli esiti in più momenti e chiudere alla fine.

#### Casi particolari

Prestazioni rinviate, prestazioni non previste, la seduta di un collega, la seduta dimenticata o già chiusa: sono le lezioni del modulo **Sedute: casi particolari**, a partire da [Prestazione rinviata o non eseguita](#lezione-prestazione-rinviata).

#### Prova nel programma

Apri la seduta di *Silvia Conti*. Non ci sono prestazioni previste: aggiungine una dal suo piano di cura, segnala **Eseguita** e registra la seduta. Poi guarda il piano: la prestazione è completata.

---

<a id="modulo-sedute-casi-particolari"></a>

## 5. Sedute: casi particolari

*Quando le cose non vanno come previsto: assenze, rinvii, spostamenti, dimenticanze, vincoli.*

<a id="lezione-paziente-non-presentato"></a>

### 5.1 Paziente non presentato

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

<a id="lezione-prestazione-rinviata"></a>

### 5.2 Prestazione rinviata o non eseguita

*I tre esiti, le prestazioni in sospeso e quando togliere dal piano.*

![Un piano con prestazioni in sospeso.](img/academy/09-piano-cura-in-sospeso.png)

*Un piano con prestazioni in sospeso.*

In poltrona non sempre si fa quello che era previsto. La scheda di seduta lo registra senza perdere il lavoro da fare.

**Per:** medici e igienisti.

#### I tre esiti

Per ogni prestazione prevista scegli un esito, con una nota se serve:

| Esito | Quando | Cosa resta nel piano |
|---|---|---|
| **Eseguita** | l'hai fatta | completata, con data e nome di chi l'ha eseguita |
| **Rinviata** | la farai in un'altra seduta (tempo, condizioni del paziente) | aperta, da riprogrammare |
| **Non eseguita** | non si è fatta, e vuoi dire perché | aperta, con il motivo |

Nessun esito è preselezionato: un'esecuzione è una dichiarazione clinica, la fai tu.

#### E se non scegli nessun esito?

Se chiudi la seduta lasciando una prestazione senza esito, la prestazione non sparisce: diventa **In sospeso · seduta del …**. Nel piano compare l'avviso, e da lì:

- **Riprogramma** fissa una nuova seduta già collegata;
- **Togli dal piano**, con un motivo obbligatorio, la toglie conservandone la traccia: chi, quando, perché.

#### Casi particolari

- **Una prestazione eseguita è un fatto acquisito.** Una volta registrata come eseguita non si cambia più esito da qui.
- **Il paziente rinuncia a quella cura.** Non usare *Non eseguita* seduta dopo seduta: dal piano usa **Togli dal piano** con il motivo *il paziente ha rinunciato*.
- **La prestazione va sostituita con un'altra** (per esempio un'otturazione diventata devitalizzazione): togli la prima con il motivo *sostituita*, poi aggiungi la nuova al piano.

#### Da sapere

Il preventivo segue l'avanzamento: una prestazione rinviata o non eseguita non conta come eseguita e non rende fatturabile il lavoro.

#### Prova nel programma

Apri la seduta di *Silvia Conti*, aggiungi una prestazione dal piano, scegli **Rinviata** con una nota e registra la seduta. Poi guarda il piano.

<a id="lezione-seduta-fuori-programma"></a>

### 5.3 Seduta fuori programma

*Prestazioni non previste e la seduta di un collega.*

![Una seduta senza prestazioni previste: si aggiungono dal piano.](img/academy/11-scheda-seduta-vuota.png)

*Una seduta senza prestazioni previste: si aggiungono dal piano.*

Due situazioni frequenti: in poltrona fai qualcosa che non era previsto, oppure registri la seduta di un collega.

**Per:** medici e igienisti.

#### Una prestazione non prevista

1. Nella scheda di seduta premi **Aggiungi prestazione**.
2. Scegli fra le prestazioni **aperte nei piani di cura del paziente**, anche di un altro piano. Puoi sceglierne più di una.
3. **Aggiungi**: compaiono fra le prestazioni della seduta, pronte per l'esito.

#### E se la prestazione non è in nessun piano?

La scheda di seduta registra solo prestazioni di un piano: così ogni lavoro eseguito ha un posto nel piano, nel preventivo e nella fattura. Prima aggiungila al piano di cura del paziente (dal dettaglio del piano), poi torna alla seduta e aggiungila. Se il paziente non ha un piano, crealo: anche una sola prestazione basta.

#### La seduta di un collega

Puoi registrare la seduta di un appuntamento di un collega: succede nelle sostituzioni e nelle urgenze. La prestazione risulta **eseguita da chi la registra**, con il suo nome e la data. È questo, e non l'appuntamento, a dire chi ha fatto cosa.

#### Togliere una prestazione dalla seduta

Una prestazione aggiunta per sbaglio si toglie dalla seduta finché non ha un esito: torna al piano com'era.

#### Quando l'esito cambia il dente

Se esegui una prestazione legata a un dente, il programma **propone** il nuovo stato del dente nell'odontogramma (per esempio *carie → otturazione*): **Applica** per accettarlo. Se non lo applichi, l'odontogramma non cambia.

#### Prova nel programma

Apri la seduta di *Silvia Conti*: non ci sono prestazioni previste. Aggiungine una dal suo piano, segnala **Eseguita** e guarda la proposta per l'odontogramma.

<a id="lezione-seduta-dimenticata"></a>

### 5.4 Seduta dimenticata o già chiusa

*Ingresso tardivo, registrazione a fine giornata, seduta da riaprire.*

![Il riepilogo prima di registrare la seduta.](img/academy/14-riepilogo-chiusura.png)

*Il riepilogo prima di registrare la seduta.*

La giornata è piena: capita di non premere *Inizia visita*, di registrare la seduta a fine mattinata o di chiuderla troppo presto. Ecco come rimediare senza perdere niente.

**Per:** medici e igienisti.

#### Non hai premuto Inizia visita

Non succede nulla di grave. Quando registri la seduta, il programma scatta la **fotografia d'ingresso** prima di salvare gli esiti; l'episodio della visita è segnato *ingresso tardivo*. La fotografia d'uscita viene scattata alla chiusura come sempre. Vedi [Lo storico degli episodi](#lezione-storico-episodi).

#### Registri le sedute a fine giornata

Nell'agenda, vista **Prossimi**, la sezione **Già trascorsi oggi** raccoglie gli appuntamenti finiti della giornata: da lì apri ogni seduta con **Seduta** e registri gli esiti. Puoi registrare in più momenti e chiudere alla fine.

#### Hai chiuso la seduta troppo presto

Una seduta **Completata** non accetta altri esiti: il programma lo dice e spiega cosa fare. Se la chiusura è stata un errore:

1. apri la **scheda del paziente**, Panoramica, elenco degli appuntamenti;
2. riporta lo stato dell'appuntamento a **In corso**;
3. torna alla scheda di seduta, registra ciò che mancava e chiudi di nuovo.

#### Hai registrato sulla seduta sbagliata

Un esito *Eseguita* non si cancella dalla seduta: è una dichiarazione clinica. Registra il lavoro sulla seduta in cui è stato davvero eseguito e scrivi una nota nel diario clinico che spieghi l'errore; per correzioni più profonde rivolgiti all'amministratore dello studio.

#### Seduta di un appuntamento annullato o mancato

Sulla seduta di un appuntamento **Cancellato** o **Non presentato** non si registra nulla: non si è svolta. Se in realtà il paziente c'era, correggi prima lo stato dell'appuntamento. Vedi [Paziente non presentato](#lezione-paziente-non-presentato).

#### Prova nel programma

Apri l'agenda in vista **Prossimi** e guarda la sezione **Già trascorsi oggi**: apri la prima seduta e registra un esito senza aver premuto *Inizia visita*.

<a id="lezione-spostare-appuntamento-collegato"></a>

### 5.5 Spostare o annullare un appuntamento collegato

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

### 5.6 I vincoli dell'agenda

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

---

<a id="modulo-clinica"></a>

## 6. Clinica

*Odontogramma, piani di cura, storico degli episodi, documenti e analisi AI.*

<a id="lezione-odontogramma"></a>

### 6.1 L'odontogramma

*Superfici, condizioni del dente e legenda.*

![L'odontogramma con la legenda: da curare, già curato, assente.](img/academy/22-odontogramma.png)

*L'odontogramma con la legenda: da curare, già curato, assente.*

L'odontogramma è la mappa dei denti del paziente, in notazione **FDI** (11-18, 21-28, 31-38, 41-48; i decidui con l'apposito interruttore).

**Per:** medici e igienisti.

#### Due gesti

- **Clic su una superficie** (occlusale, vestibolare, linguale, mesiale, distale) per segnare **carie**, **otturazione** o **sano** su quella superficie.
- **Clic sul pallino** in alto a destra del dente per le condizioni del **dente intero**: corona, mancante, estratto, impianto, ponte (pilastro o elemento), devitalizzato, da estrarre, incluso.

Le modifiche si vedono subito ma diventano definitive solo con **Salva**.

#### La legenda

I colori sono divisi in tre famiglie, che contano per il resto del programma:

- **da curare** — carie, da estrarre, incluso;
- **già curato** — otturazione, corona, impianto, ponte, devitalizzato;
- **assente** — mancante, estratto.

Il pulsante **Genera piano di cura** parte proprio da qui: propone cure solo per ciò che è *da curare*.

#### Da sapere

- Quando in seduta registri come eseguita una prestazione su un dente, il programma **propone** il nuovo stato del dente: non lo cambia da solo.
- Se salvi l'odontogramma mentre per il paziente non c'è una visita in corso, compare una finestra che ti chiede come registrare la modifica (visita, contatto o fuori episodio). Lo vedrai nella lezione sullo storico.

#### Prova nel programma

Apri l'odontogramma di *Elena Mancini*, segna una carie sulla superficie occlusale del 36 e salva. Leggi con attenzione la finestra che compare.

<a id="lezione-genera-piano"></a>

### 6.2 Dal dente al piano: «Genera piano di cura»

*Cosa viene proposto, cosa no e perché.*

Dall'odontogramma salvato il programma può **proporre** un piano di cura: tu scegli cosa tenere.

**Per:** medici.

#### Come ragiona

1. Solo le condizioni **da curare** generano una proposta: carie, da estrarre, mancante, incluso. Corone, impianti e devitalizzazioni sono cure già fatte e non vengono riproposte.
2. Le carie di uno stesso dente si raggruppano con le loro superfici: la prestazione proposta (otturazione mono, bi o trifacciale) dipende da quante sono. Le superfici arrivano nel piano e da lì nella scheda di seduta.
3. Una carie su un dente mancante, estratto o da estrarre **non** viene proposta: compare fra le **Non proposte**, con il motivo.
4. Se la stessa prestazione è già aperta sullo stesso dente in un altro piano, la riga è **esclusa** e dice in quale piano si trova. Puoi comunque riprenderla con **Aggiungi comunque**.
5. Per ogni dente le tendine offrono solo le prestazioni ammesse: niente otturazioni su un impianto.

Alla fine scegli **Nuovo piano** o **Aggiungi a piano esistente** e confermi.

#### Da sapere

Il pulsante è disattivato se ci sono modifiche non salvate: il piano parte sempre da ciò che è registrato, non da ciò che stai ancora disegnando. Le proposte seguono i **Default per condizione** del listino, che trovi in **Prestazioni**.

#### Prova nel programma

Apri l'odontogramma di *Alessandro Neri*: ha carie, un dente mancante, un incluso e una corona. Premi **Genera piano di cura** e osserva cosa viene proposto, cosa no e perché.

<a id="lezione-piano-di-cura"></a>

### 6.3 Il piano di cura

*Stati, prestazioni, Pianifica appuntamento e prestazioni in sospeso.*

![Un piano con prestazioni in sospeso.](img/academy/09-piano-cura-in-sospeso.png)

*Un piano con prestazioni in sospeso.*

Il piano di cura è l'elenco delle prestazioni previste per un paziente, con il loro avanzamento.

**Per:** medici; la segreteria vede i piani per prenotare e preparare i preventivi.

#### Il piano

Ogni piano ha uno **stato** (bozza, proposto, accettato, in corso, completato, rifiutato) e una barra che dice quanta parte del lavoro è fatta. Dalla scheda **Piani di Cura** del paziente lo crei, lo rinomini, lo apri.

#### Le prestazioni

Nel dettaglio trovi, per ogni prestazione, dente e superfici, stato (*Da pianificare*, *Appuntamento fissato*, *Completato*, *Annullato*…), professionista e note. L'icona **Pianifica appuntamento** (il calendario con la spunta) crea un appuntamento **collegato** alla prestazione: il giorno della visita la ritrovi nella scheda di seduta.

#### Le prestazioni in sospeso

Se una seduta viene chiusa senza dare un esito a una prestazione, quella non sparisce: diventa **In sospeso dal …**, e in testa al piano compare un avviso. Hai due strade:

- **Riprogramma** — fissi una nuova seduta;
- **Togli dal piano** — con un **motivo obbligatorio** (il paziente ha rinunciato, non più necessaria, sostituita, inserita per errore, o un motivo tuo).

«Togli dal piano» non cancella nulla: la prestazione resta nel piano come annullata, con motivo, data e nome di chi ha deciso. Anche a distanza di anni si ricostruisce perché un lavoro previsto non è stato fatto.

#### Da sapere

Un piano collegato a una fattura emessa non si elimina: si **archivia**. Cancellarlo farebbe sparire il documento fiscale.

#### Prova nel programma

Apri il piano di *Silvia Conti* e prenota una delle prestazioni da fare. Poi torna al piano: la prestazione è *Appuntamento fissato*.

<a id="lezione-storico-episodi"></a>

### 6.4 Lo storico degli episodi

*Com'era il paziente prima di una visita, e cosa è cambiato.*

![Un episodio: odontogramma prima e dopo, cambiamenti e riepilogo.](img/academy/21-storico-episodi.png)

*Un episodio: odontogramma prima e dopo, cambiamenti e riepilogo.*

Lo **storico degli episodi** risponde a una domanda che la cartella da sola non sa rispondere: *com'era il paziente prima di quella visita, e cosa è cambiato?*

**Per:** medici e igienisti (la segreteria non vede lo storico).

#### Cos'è un episodio

- **Visita** — si apre quando l'appuntamento passa a *In corso* (con **Inizia visita**) e si chiude con la seduta.
- **Contatto fuori visita** — una telefonata, una radiografia arrivata da fuori, altro. Lo apri tu, con un motivo, e lo chiudi con **Chiudi contatto**; si chiude da solo se nel frattempo inizia una visita.

Per ogni paziente c'è al massimo un episodio aperto.

#### Le due fotografie

All'apertura il programma salva la **situazione d'ingresso** (anamnesi e allerte, diagnosi, terapie, odontogramma, piani aperti); alla chiusura quella **d'uscita**. Le fotografie non si modificano più: una correzione fatta dopo compare nell'episodio successivo e non riscrive il passato.

#### Cosa vedi

- l'elenco degli episodi, filtrabile per visite o contatti, con il numero di cambiamenti;
- per l'episodio scelto, **cosa è cambiato** area per area e l'**odontogramma prima e dopo** affiancati;
- il **riepilogo**, una riga per cambiamento (per esempio *36 O, M, D: carie → otturazione*), composto dal programma a partire dai dati;
- **Confronta**, per mettere a confronto due episodi qualsiasi.

#### Quando il programma ti chiede di aprire un episodio

Se salvi una modifica clinica senza un episodio aperto, compare una finestra: metti *in corso* la visita di oggi, apri un contatto, oppure **salva fuori episodio** — la modifica sarà segnalata come *cambiata fuori episodio*. Nessuna di queste scelte è automatica.

#### Prova nel programma

Apri lo storico di *Martina Giordano* e seleziona la visita: guarda il 36 prima e dopo, e leggi il riepilogo.

<a id="lezione-diagnosi-prescrizioni-documenti"></a>

### 6.5 Diagnosi, prescrizioni e documenti

*Il diario clinico, le terapie in corso e i documenti del paziente.*

Oltre a odontogramma e piani, la cartella del paziente raccoglie diagnosi, prescrizioni, diario e documenti.

**Per:** medici e igienisti; i documenti li carica anche la segreteria.

#### Il diario clinico

La scheda **Cartella Clinica** è il diario, visita per visita: data, professionista, dente, prestazione, note cliniche e indicazioni per la volta successiva. Le note d'ingresso e d'uscita degli episodi compaiono qui con la loro etichetta.

#### Diagnosi e prescrizioni

Le **diagnosi** registrano cosa hai riscontrato, con il dente quando serve; quelle attive entrano nella fotografia di ogni episodio. Le **prescrizioni** raccolgono farmaci, dosaggi e durata: sono le *terapie in corso* che la scheda di seduta ti mostra fra gli alert.

#### I documenti

Nella scheda **Documenti** carichi radiografie, foto, consensi, referti (JPEG, PNG, WebP o PDF, fino a 50 MB) con **Aggiungi documento**. Ogni documento ha un tipo, un titolo, una data dell'esame e, se riguarda un dente, il suo numero. Un documento caricato mentre è aperto un episodio vi resta collegato. Le immagini si aprono in anteprima; gli altri file con **Scarica**.

Su una **Radiografia panoramica** c'è anche **Analisi AI**: lo spiega [Analisi AI delle radiografie](#lezione-analisi-ai-radiografie).

#### Da sapere

Nell'ambiente di prova i documenti di esempio sono **segnaposto** (un PDF e un'immagine sintetica): puoi aprirli, scaricarli e caricarne di tuoi, purché non contengano dati di pazienti veri.

#### Prova nel programma

Apri i documenti di *Marco Rossi*, aprine uno, poi carica un file qualsiasi come *foto clinica*.

<a id="lezione-analisi-ai-radiografie"></a>

### 6.6 Analisi AI delle radiografie

*Lanciare l'analisi di un'ortopanoramica e rivederla da medico.*

Su un'ortopanoramica il programma può cercare con l'intelligenza artificiale le possibili lesioni, dente per dente. È un **aiuto alla lettura**, non una diagnosi: ogni evidenza va verificata dal medico.

**Per:** medici.

#### Come si lancia

1. Nella scheda del paziente apri **Documenti**.
2. Su un documento di tipo **Radiografia panoramica** (un'immagine JPEG, PNG o WebP) premi **Analisi AI**.
3. Nella finestra *Analisi AI ortopanoramica* premi **Analizza con AI**. L'elaborazione richiede di solito meno di un minuto: la finestra si aggiorna da sola.

#### Cosa mostra

- Sull'immagine, un **riquadro colorato** per ogni evidenza, con il numero del dente in notazione FDI.
- Sotto, l'elenco delle **Evidenze rilevate**: dente, tipo di lesione e **affidabilità** in percentuale. Le evidenze meno sicure sono segnate *da verificare*.
- **Schermo intero** per leggere l'immagine nei dettagli.

#### La revisione del medico

Letta l'analisi, il medico preme **Conferma revisione**: l'analisi risulta *Rivista dal medico*, con il suo nome e la data. Le evidenze **non** entrano da sole nell'odontogramma: una carie che riconosci la segni tu, come sempre ([L'odontogramma](#lezione-odontogramma)). Così l'odontogramma contiene solo ciò che un medico ha visto e deciso.

**Rianalizza** (l'icona di aggiornamento) crea una nuova analisi della stessa immagine, senza cancellare la precedente.

#### Casi particolari

- **«Il file della radiografia non è nell'archivio»** — il documento esiste ma il file no (per esempio nei dati d'esempio dell'ambiente di prova): carica di nuovo l'immagine come nuovo documento.
- **«Immagine non leggibile»** — il file non è una radiografia valida o è danneggiato.
- **«Analisi interrotta: rilanciala»** o **servizio non disponibile** — riprova più tardi; se succede di nuovo avvisa l'assistenza.
- **Un PDF** non si analizza: serve l'immagine.

#### Da sapere

- L'analisi gira su un servizio dello studio dedicato alle immagini: la radiografia non viene inviata al Copilot.
- Nell'ambiente di prova le radiografie d'esempio sono segnaposto senza un'immagine vera: per provare l'analisi carica un'ortopanoramica anonima di esempio, mai di un paziente reale.

#### Prova nel programma

Apri i documenti di *Luca Romano*, carica un'ortopanoramica di esempio come **Radiografia panoramica** e lancia **Analizza con AI**.

---

<a id="modulo-amministrazione"></a>

## 7. Amministrazione

*Preventivi, fatture, richiami, magazzino, listino e tariffe.*

<a id="lezione-preventivi"></a>

### 7.1 Preventivi e avanzamento

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

### 7.2 Fatture, acconti e storni

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
- **Medico** — i documenti sono intestati al medico del preventivo (parcella), con i suoi dati di fatturazione; i preventivi propongono le sue tariffe: [Le tariffe del medico](#lezione-tariffe-medico).

Metodo di pagamento e scadenza proposti nei nuovi documenti si impostano in Impostazioni → Fatturazione.

#### Prova nel programma

Apri la fatturazione, filtra i documenti **Emessi** e aprine uno: prova **Storna con nota di credito** e guarda il risultato nell'elenco.

<a id="lezione-richiami"></a>

### 7.3 I richiami

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

<a id="lezione-magazzino"></a>

### 7.4 Il magazzino

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

<a id="lezione-prestazioni-listino"></a>

### 7.5 Prestazioni e listino

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

In fondo alla pagina, **Default per condizione** dice al programma quale prestazione proporre per ogni condizione dell'odontogramma, per esempio *carie su una superficie → otturazione monofacciale*, *carie su due superfici → bifacciale*. È la tabella che usa [Genera piano di cura](#lezione-genera-piano). **Ordine** decide quale proposta compare per prima quando ce n'è più d'una.

#### Da sapere

- Cambiare un prezzo vale per i **nuovi** preventivi: quelli già fatti mantengono il prezzo con cui sono nati.
- Un medico può avere **prezzi suoi** diversi dal listino: [Le tariffe del medico](#lezione-tariffe-medico).
- La configurazione di *Lascia sul dente* è clinica: la modificano solo i ruoli clinici e l'amministratore.

#### Prova nel programma

Apri **Prestazioni**, trova *Otturazione composito monofacciale* e guarda cosa lascia sul dente. Poi scorri fino a **Default per condizione**.

<a id="lezione-tariffe-medico"></a>

### 7.6 Le tariffe del medico

*Prezzi personali diversi dal listino, quando si fattura a nome del medico.*

Ogni medico può avere prezzi propri per alcune prestazioni, diversi dal listino dello studio: tipico quando un collaboratore fattura in proprio.

**Per:** medici e igienisti, per le proprie tariffe; l'amministratore.

#### Dove si impostano

Medici e igienisti trovano **Le mie tariffe** in **Impostazioni**, tra le loro schede personali; l'amministratore nella scheda omonima di **Impostazioni**. La pagina elenca le prestazioni attive, per ogni prestazione:

- **Prezzo studio** — quello del listino;
- **Il mio prezzo** — il tuo, se lo imposti.

Scrivi il tuo prezzo e salva la riga. **Lascia vuoto** per usare il prezzo del listino: svuotare il campo e salvare toglie la tua tariffa.

#### Come vengono usate

Solo con la **fatturazione intestata al medico** (Impostazioni → Clinica, modalità *Medico*): aggiungendo una prestazione a un tuo preventivo, il prezzo proposto è **il tuo**, se ne hai uno, altrimenti quello del listino. Resta modificabile riga per riga.

Con la fatturazione intestata allo **studio** (la modalità predefinita) i preventivi usano sempre il listino, e le tariffe personali non hanno effetto.

#### Da sapere

- Se lo studio fattura a proprio nome, la pagina lo ricorda in alto: le tariffe restano salvate, ma i preventivi usano il listino.
- Ogni cambio di tariffa crea una nuova versione e chiude la precedente: i preventivi già fatti non cambiano, e resta la storia dei prezzi.
- La modalità di fatturazione la sceglie l'amministratore: [Studio e professionisti](#lezione-impostazioni-studio).

#### Prova nel programma

Apri **Impostazioni → Le mie tariffe**, metti un prezzo tuo a una prestazione e salva. Poi svuotalo e salva di nuovo: torna il prezzo del listino.

---

<a id="modulo-copilot"></a>

## 8. Copilot AI

*L'assistente che legge i dati dello studio: modalità, domande, conferme e limiti.*

<a id="lezione-copilot"></a>

### 8.1 Chiedere al Copilot

*Modalità amministrativa e clinica, domande, anteprime e suggerimenti.*

Il **Copilot AI** è l'assistente dello studio: legge i dati di DentalCare Pro e risponde in linguaggio naturale. Prepara anche le modifiche, ma le salva solo dopo la tua conferma.

**Per:** segreteria, medici, igienisti (menu **Copilot AI**).

#### Le due modalità

| Modalità | Per chi | Cosa legge |
|---|---|---|
| **Amministrativa** | segreteria, igienisti; tutti, se lo studio non ha attivato il clinico | agenda, anagrafica (senza dati sanitari), preventivi, fatture, richiami, magazzino |
| **Clinica** | medici (dentista, ortodontista, chirurgo), se lo studio l'ha attivata | in più anamnesi, allerte, odontogramma, diagnosi, prescrizioni, piani di cura |

Il messaggio di apertura dice in quale modalità sei. Nell'ambiente di prova la modalità segue la persona scelta nel menu in alto. La modalità clinica ha una sua lezione: [Copilot clinico](#lezione-copilot-clinico).

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

<a id="lezione-copilot-clinico"></a>

### 8.2 Copilot clinico

*Interrogare la cartella in linguaggio naturale, da medico.*

![Il Copilot clinico: appuntamenti di oggi con le allerte di ogni paziente.](img/academy/34-copilot-clinico.png)

*Il Copilot clinico: appuntamenti di oggi con le allerte di ogni paziente.*

Con il Copilot clinico il medico interroga la cartella in linguaggio naturale: allerte, anamnesi, odontogramma, piani. È un **supporto alla decisione**: diagnosi e scelte restano del medico.

**Per:** medici (dentista, ortodontista, chirurgo). L'igienista e la segreteria usano il Copilot amministrativo.

#### Quando è disponibile

Servono tre condizioni insieme:

1. il **titolare** ha scelto la modalità **Clinico** in Impostazioni → AI ([Copilot e AI](#lezione-impostazioni-ai));
2. la funzione è attiva nell'installazione;
3. chi scrive è un **medico**.

Se manca una delle tre il Copilot resta amministrativo, e il messaggio di apertura lo dice. Lo studio di prova nasce in modalità clinica; se l'installazione non ha attivato la funzione, anche lì il Copilot resta amministrativo.

#### Cosa chiedergli

- *Quali appuntamenti ho oggi? Segnalami le allerte cliniche.*
- *Riassumimi anamnesi, diagnosi aperte e piano di cura di Luca Romano.*
- *Quali denti di Elena Mancini hanno carie in odontogramma?*
- *Luca Romano prende anticoagulanti e deve fare un impianto sul 36: cosa devo verificare prima?*

Le risposte citano i dati della cartella. Quando un dato manca (per esempio il nome dell'anticoagulante) il Copilot lo dice e lo chiede, invece di inventarlo.

#### Scritture cliniche

Il Copilot clinico può **preparare** una diagnosi, una prescrizione, una nota di diario o una bozza di preventivo dalle carie dell'odontogramma. Come ogni scrittura, è un'**anteprima** da confermare. Non segna prestazioni come eseguite e non cambia l'odontogramma: quello si fa nella [scheda di seduta](#lezione-scheda-seduta).

#### Casi particolari

- **Chiedi un consiglio clinico come segreteria o igienista.** Il Copilot amministrativo non dà indicazioni cliniche, nemmeno generiche: rimanda al medico e propone, per esempio, di fissare un consulto.
- **Il primo messaggio dopo un riavvio è lento o non risponde.** Il servizio che protegge i nomi si sta avviando: riprova dopo qualche secondo.

#### Prova nel programma

Come dottoressa Ferretti, chiedi al Copilot: *«Quali appuntamenti ho oggi? Segnalami le allerte cliniche.»* Poi passa a **Segreteria** nel menu in alto e fai la stessa domanda: confronta le risposte.

<a id="lezione-copilot-limiti"></a>

### 8.3 Cosa fa il Copilot e cosa no

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

---

<a id="modulo-impostazioni"></a>

## 9. Impostazioni della clinica

*Per il titolare e l'amministratore: dati, persone, agenda, documenti, Copilot.*

<a id="lezione-impostazioni-studio"></a>

### 9.1 Clinica e professionisti

*Dati della clinica, modalità di fatturazione, professionisti, poltrone e catalogo dell'anamnesi.*

![Un professionista: profilo, ruolo, dati di fatturazione e azioni.](img/academy/32-impostazioni-professionisti.png)

*Un professionista: profilo, ruolo, dati di fatturazione e azioni.*

I dati dello studio e le persone che ci lavorano. Si impostano una volta all'avvio e si aggiornano quando cambia qualcosa.

**Per:** amministratore (menu **Impostazioni**). Nell'ambiente di prova scegli **Amministratore** nel menu in alto.

#### Clinica

Scheda **Clinica** (i dati della clinica in cui sei entrato): ragione sociale, partita IVA, codice fiscale, indirizzo, telefono, e-mail, sito, **PEC**, **codice SDI** e **IBAN**. Sono i dati che compaiono su preventivi e fatture: vanno compilati prima di emettere il primo documento.

Nella stessa scheda c'è la **modalità di fatturazione**:

- **Clinica (predefinito)** — le fatture sono intestate alla clinica;
- **Medico** — le fatture sono intestate al medico del preventivo (parcella), con i dati di fatturazione del medico e le sue [tariffe](#lezione-tariffe-medico).

#### Professionisti

Scheda **Professionisti**: l'elenco delle persone dello studio con il loro ruolo. Selezionandone una:

- **Profilo anagrafico** — nome, cognome, **ruolo** (dentista, igienista, ortodontista, chirurgo, assistente, segreteria, amministratore, altro), telefono, e-mail, *professionista attivo*;
- **Dati fatturazione** — partita IVA e dati per le parcelle, se lo studio fattura a nome dei medici;
- **Riassegna pazienti** — passa i pazienti a un altro medico (per esempio quando un collega lascia lo studio);
- **Disattiva** — il professionista non compare più nelle scelte, ma la sua storia resta;
- **Elimina** — solo per chi non ha storia.

**+ Nuovo Professionista** crea una persona; **Pazienti senza medico** elenca i pazienti senza un medico di riferimento, da assegnare.

#### L'account di un nuovo professionista

Se indichi un'**e-mail**, il programma crea un account e spedisce una **password temporanea**: al primo accesso il professionista ne sceglie una sua ([Accesso e password](#lezione-accesso-e-password)). Il ruolo decide cosa vede e come risponde il Copilot.

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

### 9.2 Agenda e visibilità

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

<a id="lezione-calendario-presenze"></a>

### 9.3 Calendario delle presenze

*Orario di ogni professionista, assenze e appuntamenti da spostare.*

Ogni professionista ha il suo **calendario delle presenze**: in quali giorni e a che ora è in sede, e quando è assente. Gli appuntamenti si fissano solo quando è presente.

**Per:** medici e igienisti (**Impostazioni → Il mio calendario**, per sé) e amministratore (**Impostazioni → Per professionista**, per tutti).

#### L'orario settimanale

L'amministratore sceglie prima il professionista. Poi:

- **Come lo studio** — vale l'orario dello studio ([Agenda e visibilità](#lezione-impostazioni-agenda)). È il punto di partenza di tutti;
- **Orario proprio** — per ogni giorno una o più **fasce** (per esempio lunedì 9-13 e 14-18, mercoledì solo 9-13). Un giorno senza fasce è un giorno in cui non è in sede. **+ Fascia** ne aggiunge una, il cestino la toglie.

Premi **Salva orario**. Due fasce dello stesso giorno non possono sovrapporsi.

#### Le assenze

Ferie, congressi e altre assenze si registrano a giorni interi: **Dal**, **Al** e **Tipo** (*Ferie*, *Congresso / formazione*, *Altra assenza*), poi **Aggiungi assenza**. Non scrivere mai il motivo di una malattia: basta *Altra assenza*.

Se nell'assenza cadono appuntamenti già fissati, il programma li **elenca** (giorno, ora, paziente): vanno spostati dall'agenda. Non li sposta mai da solo.

#### Cosa cambia nel resto del programma

- **Nuovo appuntamento** propone solo gli orari in cui il professionista scelto è in sede; se quel giorno non c'è, lo dice sotto l'orario.
- **Proponi orario**, il Copilot e Giulia cercano posti liberi solo nelle presenze.
- Un appuntamento fuori presenza viene **rifiutato** con il motivo e i primi orari liberi dello stesso professionista, da proporre al paziente.
- Gli appuntamenti già fissati **restano dove sono** anche se cambi l'orario: il controllo vale quando si fissa un appuntamento o se ne cambiano orario o professionista.

#### Prova nel programma

Come **Amministratore**, apri **Impostazioni → Per professionista**, scegli *Serena Amato* e guarda il suo orario. Prova a registrare un giorno di ferie in una data con appuntamenti e leggi l'elenco di quelli da spostare; poi togli l'assenza con il cestino.

<a id="lezione-impostazioni-documenti"></a>

### 9.4 Preventivi, fatture, richiami e sistema

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

### 9.5 Copilot e AI

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

<a id="lezione-ambiente-prova-studio"></a>

### 9.6 Ambiente di prova e amministrazione dell'account

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

---

<a id="modulo-riferimento"></a>

## 10. Riferimento

*Le parole del programma, con il loro significato preciso.*

<a id="lezione-glossario"></a>

### 10.1 Glossario

*I termini del manuale, in ordine alfabetico.*

Le parole del programma, con il loro significato preciso. Il resto del manuale le usa sempre in questo senso.

**Per:** tutti.

| Termine | Significato |
|---|---|
| **Allerta** | voce dell'anamnesi da ricordare prima di trattare il paziente (allergia, anticoagulanti, cardiopatia…); compare in dashboard, agenda, scheda di seduta |
| **Account** | l'abbonamento a DentalCare Pro, con una o più cliniche; lo crea e lo gestisce il **titolare** |
| **Amministratore** | chi configura la clinica (Impostazioni); il **titolare** gestisce in più, dalla pagina *Amministrazione account*, cliniche, utenti, esportazione e chiusura dell'account |
| **Ambiente di prova** | copia dello studio con dati di esempio, per esercitarsi senza toccare i dati veri |
| **Anteprima** | ciò che il Copilot mostra prima di una modifica; niente è salvato finché non confermi |
| **Appuntamento collegato** | appuntamento creato dal piano di cura, che porta con sé le sue prestazioni |
| **Avviso al paziente** | messaggio da mandare dopo una prenotazione, uno spostamento o una cancellazione (WhatsApp o e-mail); chi non lo manda subito lo ritrova in Dashboard, *Da avvisare* |
| **Clinica** | la sede fisica in cui lavori: dati, orari, poltrone e professionisti sono suoi. Un account può averne più d'una; si creano dalla pagina del titolare |
| **Episodio** | una visita o un contatto fuori visita, con la fotografia del paziente prima e dopo |
| **Esito** | ciò che dichiari per una prestazione in seduta: *Eseguita*, *Rinviata*, *Non eseguita* |
| **Fatturabile** | preventivo con tutte le prestazioni eseguite e non ancora fatturato |
| **FDI** | numerazione internazionale dei denti (11-18, 21-28, 31-38, 41-48; decidui 51-85) |
| **In sospeso** | prestazione rimasta senza esito in una seduta chiusa o mancata: da riprogrammare o togliere dal piano |
| **Ingresso tardivo** | episodio la cui fotografia d'ingresso è stata scattata alla registrazione, perché la visita non era stata avviata |
| **Listino** | elenco delle prestazioni con prezzi, durate e regole (menu Prestazioni) |
| **Modalità del Copilot** | *spento*, *amministrativo* (dati organizzativi) o *clinico* (anche la cartella, solo medici) |
| **Nota di credito** | documento che storna una fattura emessa, per intero |
| **Persona** | nell'ambiente di prova, il ruolo da cui guardi lo studio (menu in alto) |
| **Piano di cura** | elenco delle prestazioni previste per un paziente, con il loro stato |
| **Poltrona** | il posto di lavoro in cui si svolge l'appuntamento (*Poltrona 1*, *Poltrona 2*…), una colonna dell'agenda; l'elenco si gestisce in Impostazioni → Anagrafiche → Poltrone |
| **Pseudonimo** | nome sostitutivo con cui i dati di un paziente escono verso il servizio AI, al posto di quello vero |
| **Richiamo** | promemoria per ricontattare un paziente (controllo, igiene, terapia da completare) |
| **Scheda di seduta** | schermata in cui il medico registra cosa è stato fatto all'appuntamento |
| **Sede** | sinonimo di *clinica* |
| **Seduta** | l'appuntamento visto dal lato clinico: si avvia, si registra, si chiude |
| **Slot** | passo della griglia dell'agenda (15, 20, 30 o 60 minuti): orari e durate si scelgono a slot |
| **Stato dell'appuntamento** | *Programmato, Confermato, Presente, In corso, Completato, Cancellato, Non presentato* |
| **Tariffa del medico** | prezzo personale di un medico, diverso dal listino, usato quando si fattura a nome del medico |

#### Prova nel programma

Tieni aperto il glossario quando leggi le altre lezioni: ogni parola in grassetto che non conosci è qui.

---
