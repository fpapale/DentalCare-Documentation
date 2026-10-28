# 15 — Servizio del manuale per ChatGPT e Claude (`dentalcare-docs-service`)

Microservizio che rende il **manuale di DentalCare Pro** interrogabile da ChatGPT (Custom GPT o connettore MCP) e da Claude (connettore MCP). Codice nel repository applicativo, cartella `dentalcare-docs-service/`; in collaudo dal 28/10/2026.

| | |
|---|---|
| Indirizzo pubblico | `https://papalef.duckdns.org:8085` |
| Fonte | lezioni dell'Academy (`backend/src/main/resources/academy/v1`: `catalog.json` + `lessons/*.md`), le stesse da cui si genera il [manuale utente](../05-Manuale-Utente/MANUALE_UTENTE.md) |
| Tecnologia | Node 20, Express, SQLite FTS5 in memoria |
| Autenticazione | nessuna: il contenuto è il manuale, già pubblico |

---

## 1. Cosa fa

All'avvio legge `catalog.json` e le lezioni, le indicizza per testo pieno e risponde con titolo, modulo, sommario, estratto e **link pubblico alla lezione** nel manuale (`MANUALE_UTENTE.md#lezione-<slug>`). graphify, directives e documenti di progetto **non** entrano: ai clienti va solo il manuale.

| Endpoint | Uso |
|---|---|
| `GET /api/search?q=…` | ricerca (Action `searchDocs`) |
| `GET /api/page?slug=…` | testo completo di una lezione (Action `getDocPage`) |
| `GET /api/topics` | elenco dei moduli e delle lezioni (Action `listTopics`) |
| `POST /mcp` | MCP JSON-RPC: `search_docs`, `get_page`, `list_topics` |
| `GET /privacy` | informativa, richiesta da OpenAI per condividere il GPT |
| `GET /health` | stato e numero di lezioni indicizzate |
| `POST /api/reindex` | reindicizza a caldo; solo con header `X-Reindex-Token` uguale a `DOCS_REINDEX_TOKEN` (vuoto = spento) |

Lo schema per la Action del Custom GPT è `dentalcare-docs-service/openapi.yaml`.

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

## 3. Collegarlo a ChatGPT: Custom GPT (consigliato)

Serve un abbonamento ChatGPT Plus o Team. Il GPT si crea una volta e si condivide con un link.

1. chatgpt.com → **Esplora GPT** → **Crea** → scheda **Configura**.
2. Compilare:
   - **Nome:** «Manuale DentalCare Pro»
   - **Istruzioni:**
     ```text
     Sei l'assistente del manuale di DentalCare Pro. Per ogni domanda sul programma
     usa searchDocs, poi getDocPage sulla lezione più pertinente. Rispondi in italiano,
     solo con quello che trovi nel manuale, e cita sempre il link "url" della lezione.
     Se il manuale non copre la domanda, dillo chiaramente. Non dare consigli clinici.
     ```
   - togliere **Ricerca web** e **Generazione immagini**, così risponde solo dal manuale.
3. **Azioni** → **Crea nuova azione**:
   - **Autenticazione:** Nessuna;
   - **Schema:** incollare tutto `dentalcare-docs-service/openapi.yaml`; devono comparire `searchDocs`, `getDocPage`, `listTopics`;
   - **Informativa sulla privacy:** `https://papalef.duckdns.org:8085/privacy`.
4. Provare nell'anteprima, per esempio «Come si crea un preventivo?». Alla prima chiamata ChatGPT chiede il permesso per `papalef.duckdns.org`: **Consenti sempre**.
5. **Crea** → **Condividi**: «Chiunque abbia il link» (per gli studi) oppure «Solo io».

Se cambia `openapi.yaml` (nuovi parametri o endpoint) lo schema va incollato di nuovo nella Action; se cambiano solo le lezioni non serve fare nulla.

---

## 4. Collegarlo a ChatGPT: connettore MCP

Adatto per uso personale o di prova; per gli studi è meglio il Custom GPT.

1. **Impostazioni** → **App e connettori** → **Avanzate** → attivare **Modalità sviluppatore**.
2. **Crea connettore**: URL `https://papalef.duckdns.org:8085/mcp`, autenticazione **Nessuna**.
3. In una chat attivarlo dal pulsante **+**.

## 5. Collegarlo a Claude: connettore MCP

1. claude.ai → **Impostazioni** → **Connettori** → **Aggiungi connettore personalizzato**.
2. URL `https://papalef.duckdns.org:8085/mcp`, nessuna autenticazione.
3. In una chat attivarlo dal menu degli strumenti.

---

## 6. Sicurezza e privacy

- **Nessun login**, per scelta: il servizio espone solo le lezioni del manuale, già pubbliche in questo wiki. Nessun dato dei pazienti, nessun codice, nessun documento di progetto.
- **Cosa riceve:** i termini di ricerca che ChatGPT o Claude ricavano dalle domande degli utenti. Il servizio non li registra; Caddy non ha log degli accessi per questo sito. Un utente potrebbe comunque scrivere dati di un paziente nella domanda: per questo l'informativa e le istruzioni del GPT parlano solo del programma. Voce **D-71** nel [registro DPIA](../06-Compliance/dichiarazioni-dpia.md).
- **Reindicizzazione** chiusa da token; senza `DOCS_REINDEX_TOKEN` l'endpoint risponde sempre 403.
- **Nessun limite di richieste** oggi. Il servizio gira sullo stesso host della vetrina: se venisse martellato, rallenterebbe anche quella. Caddy non ha un limite di richieste di serie (serve il modulo `rate_limit`); da valutare se il GPT viene condiviso ampiamente.

## 7. Aperti

- Limite di richieste (vedi §6).
- Passaggio alla vera produzione: oggi il servizio è nello stack di collaudo, che segue il ramo `staging`.
