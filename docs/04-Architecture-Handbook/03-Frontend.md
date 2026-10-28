# 03 — Frontend (Angular)

## 1. Panoramica

SPA Angular 21 con **standalone components** e **signals**. Styling
esclusivamente con **Tailwind CSS** (classi inline, nessun file CSS per
componente). Servita in produzione da nginx che fa da reverse proxy verso l'API.

## 2. Struttura

```
src/app/
├── core/          singleton: auth, interceptor, guard, services HTTP
│   └── services/  un service per dominio (patient, appointment, estimate,
│                  invoice, treatment-plan, odontogram, recall, product,
│                  copilot, chat, layout, ...)
├── shared/        componenti, pipe, direttive riutilizzabili
├── features/      una cartella per modulo funzionale
└── layout/        shell applicativa (menu, header, pannello destro)
```

## 3. Feature

`dashboard`, `agenda`, `pazienti`, `preventivi`, `fatturazione`, `magazzino`,
`richiami`, `prestazioni`, `impostazioni`, `admin-tenant`, `segretaria`, `login`,
`public`, `academy` (#69). Ogni feature è caricata in lazy loading per route.

Componenti condivisi introdotti di recente:
- `shared/components/odontogram-chart/` (#67): odontogramma in **sola lettura** per il
  confronto prima/dopo. Geometria, colori ed etichette stanno in
  `shared/odontogram/odontogram-render.ts`, usato anche dal tab Odontogramma editabile;
- `shared/components/episode-prompt/` + `core/services/episode-guard.service.ts` (#67): la
  richiesta di apertura dell'episodio, montata una volta nella shell. I componenti che salvano
  dati clinici chiamano `ensureEpisode(patientId)` **prima** del salvataggio; per i ruoli non
  clinici risolve subito `true`;
- `features/pazienti/episodi-tab/` (#67): tab «Storico episodi», nascosto alla segreteria;
- `features/academy/` (#69): home, lezione (markdown renderizzato con `marked` e sanitizzato da
  Angular, video con ripresa dal punto lasciato) ed editor delle lezioni con anteprima.
- `shared/components/patient-notice-prompt/` + `core/services/appointment-notice.service.ts` (#111): finestra
  «Avvisa il paziente», montata una volta nella shell come il prompt degli episodi; la aprono il nuovo appuntamento,
  la scheda paziente (spostamento, cancellazione), i pulsanti nelle risposte del Copilot e l'elenco «Da avvisare»
  della Dashboard.
- `core/services/whatsapp-config.service.ts` (#111): configurazione WhatsApp della clinica, condivisa e legata
  alla clinica dell'utente; vale come spenta finché il server non risponde (i link si chiedono dopo). Va letta, non
  caricata, dai metodi chiamati nei template (scrivere un signal durante il rendering dà NG0600).
- `features/agenda/`: colonne della vista Giorno dalle poltrone attive (`GET /api/appointments/chairs`), colonna
  degli orari `sticky`, colori per posizione, filtro delle poltrone in `localStorage` (#115).
- `features/impostazioni/`: schede della clinica (Clinica, Professionisti, Anagrafiche → Poltrone | Anamnesi,
  Agenda, Per professionista, Preventivi, Fatturazione, Richiami, AI, Sistema → WhatsApp) e schede personali per
  medici e igienisti (#98); `features/admin-tenant/` è la pagina del titolare (*Amministrazione account*, #117).

## 4. Service HTTP

Un service Angular per dominio, che:
- incapsula le chiamate `HttpClient`, restituisce `Observable<T>`;
- tipizza request/response con interfacce allineate ai DTO backend;
- usa `environment.apiBaseUrl` come base configurabile per ambiente.

## 5. Layout a tre colonne

Layout: **menu laterale | contenuto centrale | pannello destro opzionale**
(KPI/indicatori/shortcut). Il pannello destro è gestito da `LayoutService`: ogni
feature registra un `TemplateRef` in `ngAfterViewInit` (`setRightPanel(tpl)`) e
lo pulisce in `ngOnDestroy` (`setRightPanel(null)`). Visibile solo da breakpoint
`lg` in su; se nessuno registra un template la colonna centrale si estende.

## 6. Cross-cutting

- **Interceptor HTTP**: aggiunge il JWT (Bearer), intercetta `401/403/500` per
  gestione centralizzata (sessione scaduta, accesso negato).
  Un `403 DEMO_EXPIRED` (#69) chiude la sessione e porta al login con il messaggio di
  prova terminata e la richiesta di attivazione.
- **Guard**: autenticazione e autorizzazione per ruolo (protezione aree
  amministrative). Per l'Academy: `academyEnabledGuard` (Academy accesa) e
  `academyEditorGuard` (ruolo di piattaforma nel token).
- **Porte d'ingresso e ambienti di prova (#69, #70)**: `AppModeService` legge una volta
  `/api/public/demo-config` (registrazione cliente, prova gratuita o suo indirizzo esterno,
  ambiente di prova degli studi, Academy, durata della prova). `/registrati` e `/prova` usano lo
  stesso componente con due moduli. Nella shell: badge «Ambiente demo · restano N giorni» o
  «Ambiente di prova», pulsante «Ambiente di prova» dagli studi veri e «Torna a …» da lì;
  `AuthService.enterSandbox/leaveSandbox` conservano e riprendono la sessione reale.
- **Locale**: registrata la locale `it` in `app.config.ts`
  (`registerLocaleData(localeIt)` + `LOCALE_ID='it'`), obbligatorio: senza,
  `DatePipe`/`number`/`currency` con locale `it` falliscono a runtime.

## 7. Form e stato

- Reactive Forms per i form complessi; validazioni client allineate al backend.
- Gestione esplicita degli stati loading / errore / vuoto / successo.
- Streaming realtime (copilot, chat, notifiche agenda) via SSE.

## 8. Copilot nel frontend

Il copilot AI è integrato come pannello/chat contestuale: invia il contesto del
paziente/schermata corrente e riceve risposte in streaming. Lato backend usa
Spring AI + tool (vedi [04-AI](04-AI.md)).
