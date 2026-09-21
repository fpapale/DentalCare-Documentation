# 05 — Manuale Utente (tenant demo)

Guida pratica all'uso di **DentalCare Pro** per i tre ruoli operativi di uno
studio: **Dottoressa** (medico), **Segretaria** e **Amministratore**. Tutti gli
esempi usano il **tenant demo** e sono riproducibili passo-passo.

> Approfondito ma usabile: ogni sezione ha il **percorso a menu**, i **passi
> numerati** e un riquadro **▶️ Prova nel demo** con l'account giusto.

## Indice

| # | Guida | Per chi | Contenuti principali |
|---|-------|---------|----------------------|
| 1 | [Guida Dottoressa](01-Guida-Dottoressa.md) | Dentista / Igienista / Ortodontista / Chirurgo | Agenda clinica, scheda di seduta (#56-#62), cartella clinica, odontogramma, anamnesi, piani di cura, preventivi, analisi AI radiografie, Copilot |
| 2 | [Guida Segretaria](02-Guida-Segretaria.md) | Segreteria / Front-office | Appuntamenti, anagrafica pazienti, richiami, preventivi, fatturazione conforme (saldo, acconto, nota credito #50-#52), magazzino, Copilot AI |
| 3 | [Guida Amministratore](03-Guida-Amministratore.md) | Titolare / Responsabile studio | Dashboard, impostazioni, listino prestazioni, Prompt Manager AI, Errori intelligenti (#54), export protetto (#47) |
| 4 | [**Manuale Utente Integrale**](MANUALE_UTENTE.md) | Tutti i ruoli | **Documento completo e dettagliato (1120 righe)** con tutti i moduli, schermate, ciclo seduta, gestione errori e glossario stati |

## Manuale con schermate reali (per la presentazione)

Manuale a **percorsi guidati** con le **schermate reali** dell'applicazione per i tre ruoli, pensato come materiale di presentazione:

- **[MANUALE_UTENTE.md](MANUALE_UTENTE.md)** — **Manuale utente completo di riferimento**, aggiornato a tutte le feature recenti (#50-#62, ciclo seduta, fatturazione, AI error humanize).
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

- **Scheda paziente**: pagina centrale con tab (Panoramica, Cartella clinica,
  Odontogramma, Anamnesi, Documenti, Preventivi, Richiami, Fatture).
- **Cartella clinica**: storico delle visite e delle prestazioni erogate.
- **Odontogramma**: mappa dei denti con le condizioni (carie, corone, impianti…),
  compilabile a mano o **suggerita dall'AI** da una radiografia.
- **Anamnesi**: scheda clinica generale (patologie, allergie, farmaci, abitudini).
- **Piano di cura → Preventivo → Fattura**: il flusso economico. Dal piano di
  cura si genera il preventivo; accettato, diventa fatturabile.
- **Richiamo (recall)**: promemoria di controllo/igiene periodico per il paziente.
- **Copilot AI**: assistente conversazionale che legge e (con i permessi giusti)
  scrive sui moduli — agenda, pazienti, preventivi, ecc.
