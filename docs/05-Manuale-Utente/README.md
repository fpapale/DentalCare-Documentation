# 05 — Manuale Utente (tenant demo)

Guida pratica all'uso di **DentalCare Pro** per i tre ruoli operativi di uno
studio: **Dottoressa** (medico), **Segretaria** e **Amministratore**. Tutti gli
esempi usano il **tenant demo** e sono riproducibili passo-passo.

> Approfondito ma usabile: ogni sezione ha il **percorso a menu**, i **passi
> numerati** e un riquadro **▶️ Prova nel demo** con l'account giusto.

## Indice

| # | Guida | Per chi | Contenuti principali |
|---|-------|---------|----------------------|
| 1 | [Guida Dottoressa](01-Guida-Dottoressa.md) | Dentista / Igienista / Ortodontista / Chirurgo | Agenda clinica, scheda di seduta con «Inizia visita» e aggiornamento del dente (#56-#62, #65), storico episodi (#67), odontogramma e «Genera piano» (#66), anamnesi, piani di cura, preventivi, listino, analisi AI radiografie, Copilot, ambiente di prova e Academy (#70) |
| 2 | [Guida Segretaria](02-Guida-Segretaria.md) | Segreteria / Front-office | Appuntamenti e stati Presente / In corso, anagrafica pazienti, richiami, preventivi, fatturazione conforme (saldo, acconto, nota credito, numerazione #50-#53, #63), liste ordinabili, magazzino, Copilot AI, ambiente di prova e Academy (#70) |
| 3 | [Guida Amministratore](03-Guida-Amministratore.md) | Titolare / Responsabile studio | Dashboard, impostazioni, listino con le impostazioni cliniche (#65, #66), Prompt Manager AI, Errori intelligenti (#54), export protetto (#47), prova gratuita, ambiente di prova dello studio e Academy (#69, #70) |
| 4 | [**Manuale Utente Integrale**](MANUALE_UTENTE.md) | Tutti i ruoli | **Documento completo e dettagliato (circa 1270 righe)** con tutti i moduli, schermate, ciclo seduta, gestione errori e glossario stati |

## Manuale con schermate reali (per la presentazione)

Manuale a **percorsi guidati** con le **schermate reali** dell'applicazione per i tre ruoli, pensato come materiale di presentazione:

- **[MANUALE_UTENTE.md](MANUALE_UTENTE.md)** — **Manuale utente completo di riferimento**, aggiornato a tutte le feature recenti (#50-#70: ciclo seduta, dente da seduta, «Genera piano», storico episodi, fatturazione, errori intelligenti, ambiente di prova e Academy).
- **[Manuale-Completo.md](Manuale-Completo.md)** — sintesi percorsi con gli screenshot embedded.
- **[Manuale_Utente_DentalCare_Pro.docx](Manuale_Utente_DentalCare_Pro.docx)** — versione Word (12 schermate), pronta da stampare o inviare.

Le schermate provengono dall'ambiente dimostrativo: nomi e dati dei pazienti sono fittizi.

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
| **Dottoressa** | `ferretti@demo.dentalcare.it` | Laura Ferretti | dentist |
| **Segretaria** | `segreteria@demo.dentalcare.it` | Maria Rossi | secretary |
| **Amministratore** | `admin@demo.dentalcare.it` | Admin Demo | admin |
| (demo vetrina) | `demo@demo.dentalcare.it` | Demo Tutto | admin |
| Altri medici | `amato@…` (ortodontista), `marchetti@…` (chirurgo) | | medical |

> **Nota:** cambiando account devi fare **logout** e re-login. Ogni ruolo vede un
> menu diverso: sotto la matrice completa.

## Matrice funzioni × ruolo

Legenda: ✅ accesso pieno · 🔎 solo lettura/consultazione · — nessun accesso.

| Funzione (voce di menu) | Dottoressa | Segretaria | Amministratore |
|-------------------------|:----------:|:----------:|:--------------:|
| Dashboard | ✅ | ✅ | ✅ |
| Agenda (appuntamenti) | ✅ | ✅ | ✅ |
| Nuovo appuntamento | ✅ | ✅ | ✅ |
| Pazienti (lista + scheda) | ✅ | ✅ | ✅ |
| Nuovo paziente (anagrafica) | — | ✅ | ✅ |
| Cartella clinica / Nuova visita | ✅ | — | ✅ |
| Odontogramma | ✅ | 🔎 | ✅ |
| Anamnesi | ✅ | 🔎 | ✅ |
| Diagnosi | ✅ | — | ✅ |
| Prescrizioni | ✅ | — | ✅ |
| Piani di cura | ✅ | 🔎 | ✅ |
| Preventivi | ✅ | ✅ | ✅ |
| Fatturazione | ✅ | ✅ | ✅ |
| Richiami | ✅ | ✅ | ✅ |
| Magazzino | ✅ | ✅ | ✅ |
| Listino prestazioni | ✅ | — | ✅ |
| Copilot AI (Segreteria) | ✅ | ✅ | — |
| Scheda di seduta | ✅ | — | ✅ |
| Storico episodi | ✅ | — | ✅ |
| Ambiente di prova dello studio | ✅ | ✅ | ✅ |
| Academy | ✅ | ✅ | ✅ |
| Impostazioni (studio + AI) | — | — | ✅ |

> **Perché la Dottoressa NON crea l'anagrafica paziente?** Per separazione dei
> compiti: la registrazione anagrafica è della segreteria; il medico lavora sulla
> parte clinica. In demo puoi comunque provare tutto usando i tre account.

## Convenzioni del manuale

- **Percorso** → in grassetto la sequenza di menu, es. **Pazienti → scheda →
  tab Cartella clinica**.
- **▶️ Prova nel demo** → account e passi esatti per riprodurre.
- I dati sensibili del paziente (data di nascita, codice fiscale) sono **cifrati
  a riposo** nel database: nell'app li vedi in chiaro, ma nel DB sono protetti
  (vedi handbook tecnico `04-Architecture-Handbook/11-Data-Encryption.md`).

## Concetti chiave (glossario rapido)

- **Scheda paziente**: pagina centrale con tab (Anagrafica, Cartella clinica,
  Storico episodi, Anamnesi, Odontogramma, Piani di cura, Preventivi, Documenti).
- **Cartella clinica**: storico delle visite e delle prestazioni erogate.
- **Odontogramma**: mappa dei denti con le condizioni (carie, corone, impianti…),
  compilabile a mano o **suggerita dall'AI** da una radiografia.
- **Anamnesi**: scheda clinica generale (patologie, allergie, farmaci, abitudini).
- **Piano di cura → Preventivo → Fattura**: il flusso economico. Dal piano di
  cura si genera il preventivo; accettato, diventa fatturabile.
- **Richiamo (recall)**: promemoria di controllo/igiene periodico per il paziente.
- **Episodio clinico**: una visita o un contatto fuori visita, con la situazione del paziente
  fotografata prima e dopo (tab Storico episodi).
- **Ambiente di prova**: pazienti e dati inventati, separati da quelli veri, per imparare e
  provare; si apre dal pulsante in alto e si torna con **Torna a …**.
- **Copilot AI**: assistente conversazionale che legge e (con i permessi giusti)
  scrive sui moduli — agenda, pazienti, preventivi, ecc.
