# Metodo di sviluppo ad agenti

**Stato:** in prova · prima prova #124 il 04/11/2026 (esito in §8) · da rivalidare su #18 Blocco 1
**Per chi:** il committente e le sessioni di Claude che coordinano lo sviluppo.

## 1. Idea

La sessione principale (il **coordinatore**) pianifica con il committente, scrive la specifica e integra. Il codice lo scrivono **implementatori** su modelli meno costosi. Un **revisore** Opus indipendente controlla ogni slice prima dell'integrazione. Il committente può continuare a discutere con il coordinatore mentre gli agenti lavorano in background.

## 2. Ruoli

| Ruolo | Chi | Cosa fa | Cosa non fa |
|---|---|---|---|
| Coordinatore | sessione principale (modello scelto dal committente) | specifica, decisioni sui termini e sui contratti, lancio degli agenti, correzioni minori, integrazione, documenti | non scrive il grosso del codice |
| Implementatore | `backend-dev`, `frontend-dev`, `database-dev`, `general-purpose` | scrive codice e test nel suo perimetro, lancia build e test | commit, push, file fuori perimetro, scritture sui DB condivisi |
| Revisore | `reviewer` (Opus, sforzo extra-high, sola lettura) | rilancia build e test, controlla il diff contro specifica e regole, verifica i report | modificare file |

Le definizioni stanno in `.claude/agents/` (fuori da git). Contengono le regole del progetto, perché i subagenti non leggono la memoria del coordinatore.

## 3. Quale modello per quale lavoro

| Lavoro | Modello dell'implementatore |
|---|---|
| Codice applicativo, test, testi con giudizio (anche Academy) | **Sonnet** (predefinito) |
| Lavoro meccanico su un elenco chiuso: sostituzioni già decise riga per riga, raccolta di dati, ricerche | **Haiku** |
| Slice di sicurezza e privacy: ruoli, audit, cifratura, titolarità, MFA, webhook di pagamento | **Opus** (da validare su #18 Blocco 1) |

Il revisore è sempre Opus a sforzo extra-high.

## 4. Procedura

1. **Specifica** in un file condiviso (scratchpad della sessione), letta da implementatori e revisore. Contiene:
   - cosa cambia e cosa non cambia;
   - **il contratto già deciso**: termini, etichette esatte, DTO, nomi di endpoint. Le scelte di nomenclatura le prende il coordinatore **prima**, non gli agenti durante il lavoro;
   - i perimetri, per file;
   - i comandi di verifica.
2. **Perimetri.** Agenti in parallelo solo su file disgiunti **e** su lavori indipendenti. Un contenuto che cita un altro perimetro (l'Academy cita le etichette del frontend, il frontend usa i DTO del backend) parte **dopo**, oppure riceve dalla specifica la lista esatta di ciò che cita.
3. **Implementazione.** Ogni agente consegna: file modificati, scelte e dubbi, comandi lanciati con l'esito reale.
4. **Revisione** dopo ogni slice, con un revisore nuovo. Riceve la specifica, il diff e le dichiarazioni degli implementatori da verificare.
5. **Correzioni.** Il coordinatore decide i dubbi e rimanda le correzioni agli **stessi** agenti (`SendMessage`: ricordano il lavoro). Poi il revisore ricontrolla, sempre via `SendMessage`. **Due giri al massimo**: dopo, la slice passa a Opus. Le correzioni minori dopo un «APPROVATO» le applica il coordinatore.
6. **Integrazione.** Il coordinatore aggiorna i documenti (registro delle proposte, DPIA se serve, Academy). Fa il commit solo col via del committente, separando le correzioni fuori tema.

## 4bis. Ricognizione del codice

Prima di una ricognizione, o di una parte di lavoro, il coordinatore aggiorna il grafo del codice (`graphify update .`: solo codice, senza LLM, quindi quasi gratis). Gli agenti interrogano prima il grafo (`graphify query`) e usano `git grep` solo per i dettagli mirati. Indicazione del committente del 04/11/2026: due ricognizioni fatte solo con `git grep` sono costate circa 700 mila token.

## 5. Isolamento e sicurezza

- Agenti in parallelo sullo stesso working tree solo con file disgiunti. Altrimenti cloni `--shared` su C:, perché i worktree su D: falliscono (dubious ownership). Mai `safe.directory` globale.
- Ricerca solo con `git grep`: le cartelle di configurazione locale, escluse da git, contengono chiavi vere.
- Nessun segreto nelle definizioni degli agenti né nelle specifiche.
- Le scritture sui DB condivisi le lancia il committente: gli agenti preparano la patch.

## 6. Cosa misurare a ogni slice

Tempo per agente e totale; contatore dei token per agente; difetti del revisore per gravità e per agente; giri di correzione; correzioni fatte dal coordinatore; affidabilità dei report (dichiarato contro verificato).

## 7. Limiti noti

- Il contatore dei token degli agenti è cumulativo per agente e non distingue ingresso e uscita: serve per confronti, non per un costo esatto. Il lavoro del coordinatore non ha un contatore.
- Una decisione presa in chat non arriva a un agente già partito: va mandata con `SendMessage`.

## 8. Esito della prova #124 (04/11/2026)

Slice di testi: «Richiami» diventa «Visite di controllo», 48 file. Stima ~2-3h agente; **reali ~35 minuti** (09:14 → 09:48).

| | Frontend | Academy | Backend | Revisore |
|---|---|---|---|---|
| Modello | Sonnet | Haiku | Sonnet | Opus extra-high |
| Tempo, giro 1 + giro 2 | 6,7 + 1 min | 5,3 + 8,9 min | 4,5 + 4 min | 8,2 + 6,5 min |
| Contatore token a fine lavoro | ~156k | ~268k | ~124k | ~228k |
| Difetti al giro 1 | 3 (una scelta di termine sbagliata, una concordanza, stile) | 4 (etichette inesistenti, stati, termini) | 3 (concordanze, anteprima del Copilot) | — |
| Difetti al giro 2 | 0 | 3 minori, uno fuori tema | 2 miglioramenti alla patch | — |
| Affidabilità del report | alta | media | alta | — |

**Cosa ha funzionato**
- Il revisore ha trovato **tutti e 4** i difetti che il coordinatore conosceva, più 3 nuovi. Ha anche trovato due problemi che nessuno aveva previsto: l'ambiguità del Copilot fra visite di controllo e appuntamenti con la stessa nota, e la cache dei prompt che avrebbe reso la patch inefficace fino al riavvio.
- Sonnet ha dato codice, test e report affidabili. Il backend ha scoperto da solo che il prompt nel DB non si aggiorna dal file.
- Haiku ha scoperto un difetto preesistente (lo script del catalogo disallineato) e si è fermato senza correggerlo, come chiedeva la specifica.
- La seconda revisione via `SendMessage` è stata più rapida della prima.

**Cosa non ha funzionato**
- La maggior parte dei difetti del giro 1 viene da **termini non decisi nella specifica** («Primo richiamo», genere degli stati) e da **perimetri dipendenti lanciati in parallelo**: l'Academy citava etichette del frontend che non esistevano ancora.
- Per l'Academy, Haiku ha consumato più token di tutti, ha fatto più sviste di Sonnet ed è uscito dal tema.

**Regole adottate dopo la prova**
- I termini e le etichette si decidono nella specifica; gli agenti non scelgono la nomenclatura.
- I contenuti che citano altri perimetri partono dopo, o ricevono la lista esatta.
- Haiku solo per lavoro meccanico su un elenco chiuso. L'Academy la scrive Sonnet.
