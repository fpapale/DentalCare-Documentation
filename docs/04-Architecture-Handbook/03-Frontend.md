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
`public`. Ogni feature è caricata in lazy loading per route.

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
- **Guard**: autenticazione e autorizzazione per ruolo (protezione aree
  amministrative).
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
