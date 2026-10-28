# 15 — Servizio del manuale per ChatGPT e Claude (`dentalcare-docs-service`)

Microservizio che rende il **manuale di DentalCare Pro** interrogabile da Claude e da ChatGPT tramite un **connettore MCP**. Codice nel repository applicativo, cartella `dentalcare-docs-service/`; in collaudo dal 28/10/2026.

| | |
|---|---|
| Indirizzo pubblico | `https://papalef.duckdns.org:8085` |
| Fonte | lezioni dell'Academy (`backend/src/main/resources/academy/v1`: `catalog.json` + `lessons/*.md`), le stesse da cui si genera il [manuale utente](../05-Manuale-Utente/MANUALE_UTENTE.md) |
| Tecnologia | Node 20, Express, SQLite FTS5 in memoria |
| Autenticazione | nessuna: il contenuto è il manuale, già pubblico |
| Stato | **in sospeso** (28/10/2026): attivo e raggiungibile sulla 8085, ma Claude non si collega (vedi §7) |

---

## 1. Cosa fa

All'avvio legge `catalog.json` e le lezioni, le indicizza per testo pieno e risponde con titolo, modulo, sommario, estratto e **link pubblico alla lezione** nel manuale (`MANUALE_UTENTE.md#lezione-<slug>`). graphify, directives e documenti di progetto **non** entrano: ai clienti va solo il manuale.

| Endpoint | Uso |
|---|---|
| `POST /mcp` | **MCP** (Streamable HTTP, JSON-RPC): `search_docs`, `get_page`, `list_topics`, tutti in sola lettura (`readOnlyHint`); versioni del protocollo 2025-06-18, 2025-03-26, 2024-11-05 |
| `GET /api/search?q=…`, `/api/page?slug=…`, `/api/topics` | le stesse funzioni in REST (schema `openapi.yaml`), nate per la Action del Custom GPT |
| `GET /privacy` | informativa |
| `GET /health` | stato e numero di lezioni indicizzate |
| `POST /api/reindex` | reindicizza a caldo; solo con header `X-Reindex-Token` uguale a `DOCS_REINDEX_TOKEN` (vuoto = spento) |

> [!WARNING]
> **Niente Custom GPT.** OpenAI ritira i Custom GPT l'11/12/2026 e gli account personali (Free, Go, Plus, Pro) non possono più crearne né pubblicarne; le Action non passano ai nuovi plugin. L'unica strada per ChatGPT è il connettore MCP (§3). L'API REST e `openapi.yaml` restano solo per prove e integrazioni future.

---

## 2. Deploy

Il servizio è nello stack di collaudo (`docker-compose.coll.yml`, servizio `dentalcare-docs-service`, container `dentalcare-coll-docs-service`):
- porta `18085` dell'host → `8085` del container;
- lezioni montate in sola lettura dal checkout del repository;
- il workflow `deploy-coll.yml` lo avvia e, a ogni deploy, lo **riavvia**: se l'immagine non cambia il container non verrebbe ricreato e l'indice resterebbe quello delle lezioni vecchie.

Aggiornare il manuale quindi è automatico: si modifica la lezione, si fa push su `staging`, il deploy riavvia il servizio.

### Esposizione HTTPS (Caddy)

Caddy gira in Docker sullo stesso host e ha già il certificato di `papalef.duckdns.org`. Due modifiche, fatte il 28/10/2026:

1. Nel Caddyfile:
   ```caddy
   papalef.duckdns.org:8085 {
       reverse_proxy http://<server-app>:18085
   }
   ```
2. Nel `docker-compose.yml` di Caddy la porta `"8085:8085"`, poi `docker compose up -d` (una porta nuova richiede di ricreare il container, il reload non basta).

La porta del servizio è pubblicata sulla rete e non solo su `127.0.0.1`: dentro il container di Caddy `127.0.0.1` è Caddy stesso. Il router inoltra la 8085 all'host.

> [!NOTE]
> Anche l'istanza di confronto di `llm-ner-gateway` ([cap. 14](14-LLM-NER-Gateway.md)) usa la 8085. Oggi sull'host la 8085 è di Caddy: se quell'istanza dovesse essere pubblicata sull'host, va messa su un'altra porta.

### Verifica

```bash
curl -s https://papalef.duckdns.org:8085/health          # {"status":"healthy",…,"indexed_documents":47}
curl -s "https://papalef.duckdns.org:8085/api/search?q=agenda"
curl -s -X POST https://papalef.duckdns.org:8085/mcp \
  -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

---

## 3. Collegarlo all'assistente: chi può e con quale piano

La guida per gli studi, passo per passo e scritta per chi non è tecnico, è nel repository applicativo: `dentalcare-docs-service/GUIDA_COLLEGAMENTO_MANUALE.md`. È quella da mandare ai clienti.

Indirizzo da inserire: `https://papalef.duckdns.org:8085/mcp`, autenticazione **nessuna**.

| Assistente | Piani che possono collegarlo (verificato il 28/10/2026) | Note |
|---|---|---|
| **Claude** | **Free**, Pro, Max, Team, Enterprise | Free: un solo connettore personalizzato. Team/Enterprise: lo aggiunge il proprietario dell'organizzazione, poi ognuno preme Connetti |
| **ChatGPT** | **Pro** (strumenti di sola lettura, come i nostri), **Business**, Enterprise, Edu | Free, Go e Plus: non disponibile. Un plugin si condivide solo dentro un workspace Business/Enterprise, non con studi esterni |

**Canale consigliato per gli studi: Claude**, perché basta l'account gratuito. ChatGPT resta per chi ha già Pro o Business.

### Claude

- **Personale:** Impostazioni → Connettori → + Aggiungi → Aggiungi connettore personalizzato; nome e URL; accesso «No sign in».
- **Team/Enterprise:** Impostazioni dell'organizzazione → Connettori → Add → Custom → Web.
- **In chat:** + → Connettori → attivarlo.

Fonte: [Claude Help Center, custom connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).

### ChatGPT

- Plugin (o Impostazioni → App) → + → Aggiungi server MCP personalizzato; nome, URL, autenticazione nessuna; accettare l'avviso, creare, installare.
- Su alcuni account serve prima la Modalità sviluppatore.
- **In chat:** `@` e scegliere il plugin.
- I menu cambiano spesso: verificare sull'account prima di aggiornare la guida.

Fonti: [Connecting custom MCP servers in ChatGPT](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt), [Custom GPT retirement FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq).

---

## 6. Sicurezza e privacy

- **Nessun login**, per scelta: il servizio espone solo le lezioni del manuale, già pubbliche in questo wiki. Nessun dato dei pazienti, nessun codice, nessun documento di progetto.
- **Cosa riceve:** i termini di ricerca che ChatGPT o Claude ricavano dalle domande degli utenti. Il servizio non li registra; Caddy non ha log degli accessi per questo sito. Un utente potrebbe comunque scrivere dati di un paziente nella domanda: per questo la guida per gli studi lo vieta esplicitamente e le istruzioni del server MCP (`instructions`) limitano l'assistente al programma. Voce **D-71** nel [registro DPIA](../06-Compliance/dichiarazioni-dpia.md).
- **Reindicizzazione** chiusa da token; senza `DOCS_REINDEX_TOKEN` l'endpoint risponde sempre 403.
- **Nessun limite di richieste** oggi. Il servizio gira sullo stesso host della vetrina: se venisse martellato, rallenterebbe anche quella. Caddy non ha un limite di richieste di serie (serve il modulo `rate_limit`); da valutare se il collegamento si diffonde tra molti studi.

## 7. Aperti

### Pubblicazione bloccata: serve la porta 443

Il 28/10/2026 la prova con un account Claude è fallita con «Impossibile raggiungere Manuale DentalCare Pro», senza alcuna richiesta nel registro del servizio. **claude.ai raggiunge i server MCP solo sulla porta 443** (risposta di un manutentore Anthropic in [anthropics/claude-ai-mcp #1155](https://github.com/anthropics/claude-ai-mcp/issues/1155)): la 8085 non viene nemmeno contattata. Dagli altri nodi di internet la 8085 risponde regolarmente.

Sul router la 443 è assegnata a un'altra macchina (Home Assistant); da internet oggi risponde «connection refused». Strade possibili, da decidere:

1. spostare l'inoltro della 443 su Caddy e servire il manuale come `https://papalef.duckdns.org/mcp` (blocco nel sito `papalef.duckdns.org` del Caddyfile, filtrato su `Host papalef.duckdns.org` e sui percorsi del servizio). Prima vanno tolti o limitati i blocchi `auth.`/`api.papalef.duckdns.org`, che con la 443 aperta diventerebbero pubblici;
2. tenere la 443 su Home Assistant con l'add-on «NGINX Home Assistant SSL proxy» e una regola `/mcp` verso il servizio;
3. un tunnel con una sua 443 (Tailscale Funnel, indirizzo `*.ts.net`).

Quando l'indirizzo cambia vanno aggiornati: `GUIDA_COLLEGAMENTO_MANUALE.md`, questo capitolo, `openapi.yaml` (`servers`) e il commento in `docker-compose.coll.yml`.

### Altri punti

- Limite di richieste (vedi §6).
- Passaggio alla vera produzione: oggi il servizio è nello stack di collaudo, che segue il ramo `staging`.
- Prova reale del connettore su un account Claude Free e su ChatGPT Pro/Business, da ripetere quando cambiano i menu.
