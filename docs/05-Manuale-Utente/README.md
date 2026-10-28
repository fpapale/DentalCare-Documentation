# 05 — Manuale Utente

Guida all'uso di **DentalCare Pro** per i ruoli di una clinica: **medico e igienista**, **segreteria**,
**titolare e amministratore**. Gli esempi usano l'ambiente dimostrativo e sono riproducibili.

> **Fonte unica: l'Academy.** Dal 22/10/2026 il manuale ufficiale è l'Academy dentro il programma (47 lezioni in
> 10 moduli). I documenti di questa cartella si **generano** dalle lezioni con
> `python tools/genera_manuale.py <repo dentalcare>`: per correggerli si corregge la lezione e si rigenera.
> Ultima generazione: 28 ottobre 2026 (allineata alle proposte fino a #117).

## Indice

| # | Documento | Per chi | Contenuti |
|---|-----------|---------|-----------|
| 1 | [Guida per il medico e l'igienista](01-Guida-Dottoressa.md) | Dentisti, ortodontisti, chirurghi, igienisti | Percorsi del medico e dell'igienista e le lezioni che richiamano: agenda, presenze, scheda di seduta in tre passi, odontogramma, piani di cura, storico episodi, casi particolari, tariffe e impostazioni personali, Copilot |
| 2 | [Guida per la segreteria](02-Guida-Segretaria.md) | Segreteria, front-office | Percorso della segreteria: appuntamenti e stati (anche automatici), avvisi ai pazienti per WhatsApp o e-mail, pazienti, preventivi, fatture con acconto e saldo, PDF via e-mail, richiami, magazzino, Copilot |
| 3 | [Guida per il titolare e l'amministratore](03-Guida-Amministratore.md) | Titolare dell'account, amministratore della clinica | Percorso del titolare: cliniche dell'account, impostazioni della clinica (dati, poltrone, orari, presenze, documenti, WhatsApp, AI), professionisti, listino, esportazione e chiusura dell'account |
| 4 | [**Manuale integrale**](MANUALE_UTENTE.md) | Tutti | Tutti i moduli e le lezioni dell'Academy, con le schermate |
| 5 | [Sintesi del manuale](Manuale-Completo.md) | Tutti | Una riga per lezione e le schermate principali: per una presentazione |
| 6 | [Versione Word](Manuale_Utente_DentalCare_Pro.docx) | Tutti | Il manuale integrale in .docx, da stampare o inviare |

Le schermate (`img/academy/`) vengono dall'ambiente dimostrativo: nomi e dati dei pazienti sono fittizi. Le cartelle
`img/` e `screenshots/` contengono le schermate delle versioni precedenti del manuale, non più aggiornate.

## Accesso all'applicazione

- **Indirizzo pubblico (browser):** `https://paaplef.duckdns.org:8181`

(L'indirizzo diretto in LAN è riservato al personale interno e non è pubblicato qui.)

Alla pagina di login del tenant demo le credenziali sono **precompilate**
(account demo). Per provare i ruoli, sostituisci email e password con quelle
della tabella sotto.

## Account demo (tenant demo)

Password demo: **fornita separatamente dall'amministratore** (non pubblicata qui
per sicurezza).

| Ruolo nel manuale | Email | Nome | Ruolo tecnico |
|-------------------|-------|------|---------------|
| **Medico** | `ferretti@demo.dentalcare.it` | Laura Ferretti | dentist |
| **Segreteria** | `segreteria@demo.dentalcare.it` | Maria Rossi | secretary |
| **Amministratore** | `admin@demo.dentalcare.it` | Admin Demo | admin |
| (demo vetrina) | `demo@demo.dentalcare.it` | Demo Tutto | admin |
| Altri medici | `amato@…` (ortodontista), `marchetti@…` (chirurgo) | | medical |

> **Nota:** cambiando account devi fare **logout** e re-login. Ogni ruolo vede un
> menu diverso: sotto la matrice completa.

## Matrice funzioni × ruolo

Legenda: ✅ accesso pieno · 🔎 solo lettura/consultazione · — nessun accesso.

| Funzione (voce di menu) | Medico / igienista | Segreteria | Amministratore |
|-------------------------|:------------------:|:----------:|:--------------:|
| Dashboard (anche «Da avvisare») | ✅ | ✅ | ✅ |
| Agenda (appuntamenti, poltrone, filtro) | ✅ | ✅ | ✅ |
| Nuovo appuntamento e avviso al paziente (WhatsApp / e-mail) | ✅ | ✅ | ✅ |
| Pazienti (lista + scheda) | ✅ | ✅ | ✅ |
| Nuovo paziente (anagrafica) | — | ✅ | ✅ |
| Cartella clinica | ✅ | — | ✅ |
| Odontogramma | ✅ | 🔎 | ✅ |
| Anamnesi | ✅ | 🔎 | ✅ |
| Diagnosi | ✅ | — | ✅ |
| Prescrizioni | ✅ | — | ✅ |
| Piani di cura | ✅ | 🔎 | ✅ |
| Preventivi | ✅ | ✅ | ✅ |
| Fatturazione (PDF ed e-mail al paziente) | ✅ (i propri) | ✅ | ✅ |
| Richiami (e-mail, WhatsApp, storico contatti) | ✅ | ✅ | ✅ |
| Magazzino | ✅ | ✅ | ✅ |
| Listino prestazioni | ✅ | — | ✅ |
| Copilot AI | ✅ | ✅ | — |
| Scheda di seduta | ✅ | — | ✅ |
| Storico episodi | ✅ | — | ✅ |
| Ambiente di prova | ✅ | ✅ | ✅ |
| Academy | ✅ | ✅ | ✅ |
| Impostazioni della clinica (dati, poltrone, orari, presenze, documenti, WhatsApp, AI) | — | — | ✅ |
| Impostazioni personali (Le mie tariffe, I miei richiami, La mia fatturazione, Il mio calendario) | ✅ | — | ✅ (per professionista) |
| Amministrazione account (cliniche, utenti, esportazione, chiusura) | — | — | solo il **titolare** |

> **Perché il medico NON crea l'anagrafica paziente?** Per separazione dei
> compiti: la registrazione anagrafica è della segreteria; il medico lavora sulla
> parte clinica. In demo puoi comunque provare tutto usando i tre account.

## Convenzioni del manuale

- **Percorso** → in grassetto la sequenza di menu, es. **Impostazioni → Anagrafiche → Poltrone**.
- **Prova nel programma** → in fondo a ogni lezione, cosa provare nell'ambiente di prova.
- I dati sensibili del paziente (data di nascita, codice fiscale) sono **cifrati
  a riposo** nel database: nell'app li vedi in chiaro, ma nel DB sono protetti
  (vedi handbook tecnico `04-Architecture-Handbook/11-Data-Encryption.md`).

## Concetti chiave (glossario rapido)

Il glossario completo è la lezione [Glossario](MANUALE_UTENTE.md#lezione-glossario). Termini concordati con il committente:

- **Account** (tenant): l'abbonamento, con una o più **cliniche**; lo gestisce il **titolare** dalla pagina
  *Amministrazione account*, l'unico posto in cui si creano cliniche.
- **Clinica** (= sede): il luogo fisico in cui si lavora; dati, orari, **poltrone** e professionisti sono suoi.
  Nell'interfaccia non si usa «Centro» né «Studio» da solo.
- **Poltrona**: il posto di lavoro, una colonna dell'agenda; anagrafica in Impostazioni → Anagrafiche → Poltrone.
- **Scheda paziente**: pagina centrale con le schede Panoramica, Cartella clinica, Storico episodi, Anamnesi,
  Odontogramma, Piani di cura, Richiami, Preventivi, Documenti.
- **Scheda di seduta**: la registrazione della visita in tre passi (prima della visita, esito, odontogramma).
- **Piano di cura → Preventivo → Fattura**: il flusso economico; acconti e saldo si scalano a vicenda.
- **Avviso al paziente**: messaggio dopo una prenotazione, uno spostamento o una cancellazione (WhatsApp in modalità
  manuale, o e-mail); quelli non mandati restano in Dashboard, *Da avvisare*.
- **Richiamo**: promemoria per ricontattare il paziente; il testo si manda per e-mail o WhatsApp dal programma.
- **Episodio clinico**: una visita o un contatto fuori visita, con la situazione del paziente prima e dopo.
- **Ambiente di prova**: dati inventati, separati da quelli veri, per imparare e provare.
- **Copilot AI**: assistente che legge i dati della clinica e prepara le modifiche, salvate solo dopo conferma.
- **Giulia**: la segreteria telefonica AI, un numero unico per tutte le cliniche (riconosce la clinica dal codice).
