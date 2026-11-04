# Piano «Freelance»: chi è titolare dei dati dei pazienti — proposta per il DPO

**Data:** 03/11/2026 · **Da:** DentalCare Pro (committente e sviluppo) · **Per:** il DPO · **Riferimento interno:** proposta #126
**Cosa chiediamo:** di validare il modello del §4 e di rispondere alle domande del §6 **prima del rilascio** del piano. Oggi nessun dato reale è trattato con questo piano: il lavoro è in progettazione.

Il documento descrive le scelte di progetto e le ipotesi del committente. Le valutazioni giuridiche e le basi di liceità restano al DPO.

---

## 1. Il piano in breve

- **Freelance** è un abbonamento per l'odontoiatra o l'igienista **senza uno studio proprio**. Il professionista lavora in più studi dentistici di terzi, gli «studi ospitanti», in giorni e orari diversi.
- Il professionista ha in DentalCare un **proprio spazio dati**, separato da quello di ogni altro cliente: schema di database dedicato; data di nascita e codice fiscale cifrati con una chiave propria del cliente.
- **Gli studi ospitanti non accedono a questo spazio**, anche quando sono a loro volta clienti DentalCare. Nessun dato passa da un cliente all'altro.
- Nel suo spazio il professionista tiene:
  - agenda, con una colonna per ogni studio ospitante;
  - anagrafica dei pazienti;
  - cartella clinica: anamnesi, diagnosi, odontogramma, piani di cura, sedute, prescrizioni;
  - documenti e immagini;
  - preventivi e fatture.
- Sono **dati relativi alla salute** (art. 9).
- **Utenti:** il professionista e, al massimo, **una** persona di segreteria incaricata da lui.
- **Fornitori:** sono gli stessi di ogni altro cliente DentalCare (hosting, e-mail transazionali, assistente telefonico, assistente AI). Sono descritti nell'inventario dei flussi e nel registro delle dichiarazioni DPIA già condivisi.

## 2. Le situazioni reali

Secondo il committente le situazioni seguenti **coesistono**, anche per lo stesso professionista e nello stesso studio ospitante.

| | Situazione | Chi ha il rapporto col paziente | Chi fattura di norma |
|---|---|---|---|
| **A** | **Paziente dello studio ospitante** (situazione prevalente) | Lo studio: il paziente si rivolge allo studio, che lo prende in carico e affida la prestazione al professionista | Lo studio, che poi paga il professionista |
| **B** | **Paziente del professionista**: lo segue da uno studio all'altro | Il professionista | Il professionista |
| **C** | **Passaggi**: un paziente A sceglie di seguire il professionista (per esempio quando la collaborazione con lo studio finisce), oppure un paziente B resta in carico allo studio | Cambia nel tempo | Cambia nel tempo |

## 3. Il punto da chiarire

Per i pazienti **B** il quadro è quello di ogni cliente DentalCare: il professionista è titolare, DentalCare è responsabile (art. 28).

Per i pazienti **A**, chi è titolare del trattamento determina:
- il ruolo del professionista: titolare, contitolare o responsabile per conto dello studio;
- il ruolo di DentalCare: responsabile del professionista, oppure sub-responsabile per conto dello studio;
- quali accordi servono e fra chi;
- chi informa il paziente;
- che cosa succede ai dati quando la collaborazione con lo studio finisce.

## 4. Il modello che proponiamo

**Principio:** il programma **non presume** il ruolo. Registra **per ogni paziente per conto di chi è trattato** e applica a ciascun gruppo le regole indicate dal DPO. Lo stesso programma funziona qualunque sia la risposta per i pazienti A.

### 4.1 Ipotesi sui ruoli (da validare)

| Situazione | Titolare | Ruolo del professionista | Ruolo di DentalCare |
|---|---|---|---|
| **B** | Professionista | Titolare | Responsabile (art. 28), come per ogni cliente |
| **A — ipotesi 1** | Studio ospitante | Responsabile per conto dello studio (art. 28), con accordo scritto | Sub-responsabile (art. 28, parr. 2 e 4), autorizzato dallo studio |
| **A — ipotesi 2** | Studio e professionista contitolari (art. 26) | Contitolare | Responsabile del professionista; l'accordo di contitolarità ne dà conto |
| **A — ipotesi 3** | Titolari autonomi: il professionista per i dati clinici, lo studio per i propri | Titolare | Responsabile del professionista |

**Ipotesi del committente:** la 1, come caso prevalente. Ci serve sapere quale ipotesi vale, e se dipende dal tipo di rapporto (collaboratore abituale, consulente specialista, sostituto occasionale).

### 4.2 Cosa farebbe il programma

1. **Scheda dello studio ospitante.** Contiene:
   - ragione sociale, partita IVA e sede;
   - contatto privacy o DPO dello studio;
   - tipo di accordo: nomina a responsabile, contitolarità o nessuno;
   - data e scadenza dell'accordo;
   - copia firmata dell'accordo, in allegato.
2. **Titolare per ogni paziente.** Due valori: «io (professionista)» oppure «Studio ospitante X».
   - Il campo è **obbligatorio e senza valore predefinito**: lo sceglie il professionista quando crea il paziente.
   - I pazienti creati dall'assistente telefonico nascono «da attribuire» e vanno attribuiti prima della prima seduta.
3. **Accordo mancante.** Per un paziente attribuito a uno studio senza accordo registrato il programma mostra un avviso permanente. In alternativa impedisce di registrare dati clinici (domanda Q4).
4. **Informativa.**
   - Per i pazienti B: il modello di informativa del professionista.
   - Per i pazienti A: il programma indica che vale l'informativa dello studio e ne registra la consegna (domanda Q8).
5. **Comunicazioni al paziente.**
   - I promemoria degli appuntamenti partono per tutti e indicano il luogo («presso Studio X»).
   - Per i pazienti A sono **spente** le visite di controllo periodiche (richiami) e ogni comunicazione non legata a un appuntamento già fissato, salvo che l'accordo le preveda (domanda Q5).
6. **Accessi.** Solo il professionista e la sua segreteria. Per i pazienti A la segreteria è una persona autorizzata dal professionista (art. 29), e l'accordo con lo studio deve consentirlo.
7. **Rendiconto per lo studio.** Le prestazioni eseguite per studio e periodo, base del compenso del professionista. Contiene **solo** i pazienti A di quello studio: i pazienti B visti nei locali dello studio non vi compaiono.
8. **Fine della collaborazione con uno studio.** Procedura guidata, **mai automatica**:
   - elenco dei pazienti A dello studio e dei loro appuntamenti futuri;
   - esportazione delle cartelle per lo studio, in PDF e in formato strutturato;
   - per ciascun paziente, una scelta esplicita: restituito allo studio e poi cancellato, oppure passato al professionista (punto 9).
   - La cancellazione avviene in due tempi: prima i dati smettono di essere visibili, poi vengono eliminati alla scadenza indicata dal DPO, fatti salvi gli obblighi di conservazione (domanda Q6).
9. **Passaggio di un paziente**, da A a B o da B ad A:
   - avviene solo su scelta documentata del paziente (domanda Q7);
   - il programma registra data, documento e chi ha eseguito il passaggio;
   - lo storico delle attribuzioni resta consultabile.
10. **Registro.** Ogni attribuzione e ogni cambio di titolare restano registrati: chi, quando, da quale titolare a quale.
11. **Nessuna condivisione fra spazi dati.** Anche se lo studio ospitante usa DentalCare, i dati non passano da uno spazio all'altro. L'esportazione del punto 8 è l'unico canale.

### 4.3 Sub-responsabili

Con l'ipotesi 1, per i pazienti A i fornitori di DentalCare diventano sub-responsabili ulteriori per conto dello studio. Proponiamo:
- un'**autorizzazione generale scritta** nell'accordo tipo fra studio e professionista;
- l'elenco dei fornitori allegato;
- l'impegno a comunicare ogni modifica dell'elenco (art. 28, par. 2).

## 5. Cosa prepariamo dopo la risposta

- Bozza di **accordo tipo fra studio ospitante e professionista**: nomina a responsabile oppure contitolarità, secondo la risposta a Q1. Sarà sottoposta al DPO.
- **Clausole del piano Freelance** nelle condizioni di servizio.
- **Modello di informativa** del professionista per i pazienti B.
- Aggiornamento della voce **D-90** del registro delle dichiarazioni DPIA con la risposta.

## 6. Domande per il DPO

| # | Domanda |
|---|---|
| Q1 | Pazienti A: quale ipotesi vale (1, 2 o 3)? Cambia secondo il tipo di rapporto fra professionista e studio? |
| Q2 | Pazienti B: confermate professionista titolare e DentalCare responsabile? |
| Q3 | Catena dei sub-responsabili (§4.3): basta l'autorizzazione generale nell'accordo tipo? |
| Q4 | Paziente A senza accordo registrato: basta un avviso, o il programma deve impedire di registrare dati clinici? |
| Q5 | Richiami e altre comunicazioni ai pazienti A non legate a un appuntamento: sono ammessi? A nome di chi partono? |
| Q6 | Fine della collaborazione: chi conserva cosa e per quanto (documentazione sanitaria; dati delle fatture emesse dal professionista)? Il professionista può tenere una copia delle cartelle dei pazienti A che ha curato? |
| Q7 | Passaggio da A a B: che cosa serve dal paziente (richiesta scritta, nuova informativa, esercizio della portabilità presso lo studio)? |
| Q8 | Informativa per i pazienti A: basta quella dello studio, o serve anche quella del professionista? |
| Q9 | Il programma permette di scegliere, per ogni studio, chi fattura al paziente. Questa scelta ha un peso sul ruolo? Deve vincolare il titolare attribuito al paziente? |
| Q10 | Serve una sezione specifica della DPIA per il piano Freelance? |
