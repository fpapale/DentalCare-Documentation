# 09 — Deployment

> **Nota:** `<app-server-lan>` e `<db-host-lan>` sono segnaposto per gli indirizzi
> LAN reali (macchina applicativa e host DB), volutamente non pubblicati. I valori
> effettivi sono documentati internamente.

## 1. Topologia di produzione

- **Macchina applicativa**: `<app-server-lan>`, cartella `~/docker/dentalcarepro`.
- **Database**: `dentalcare_prod` su PostgreSQL `<db-host-lan>`.
- **Backend** non esposto sull'host: l'nginx del frontend proxa `/api` al
  backend interno. Solo il **frontend** è pubblicato, via due percorsi verso lo
  stesso container:
  - **pubblico**: `https://paaplef.duckdns.org:8181` (HTTPS, reverse proxy TLS);
  - **diretto (server o LAN)**: `http://<app-server-lan>:<FRONTEND_PORT>` (HTTP,
    `8081` in prod, mapping `0.0.0.0:8081->4200`). Usare questa via HTTP per
    script/migrate (evita il proxy TLS pubblico).

## 2. Servizi (docker-compose)

| Servizio | Porta | Note |
|----------|-------|------|
| `dentalcarepro-backend` | 8080 (interna) | profilo `prod`, config montata, healthcheck |
| `dentalcarepro-frontend` | `${FRONTEND_PORT}:4200` (8081 in prod) | nginx, `depends_on` backend healthy |
| `dentalcare-ai-service` | interna | FastAPI + ONNX |
| MinIO | — | object storage documenti |

## 3. Script di deploy

### Produzione
- **`setup.sh`**: bootstrap — prepara `~/docker/dentalcarepro`, clona/aggiorna il
  repo, lancia `install.sh`.
- **`install.sh`**:
  1. verifica requisiti (docker, git, compose);
  2. clone o `git pull origin master`;
  3. crea `config/application-prod.properties` da `.example` se assente
     (avvisa di configurare password DB, `app.jwt.secret`, **`app.encryption.master-key`**);
  4. (opzionale, con doppia conferma) drop+ricrea `dentalcare_prod` da
     `database/install.sql`;
  5. copia i modelli AI ONNX se assenti;
  6. `docker compose up -d --build` + attesa healthcheck.

Comandi tipici sul server:
```bash
cd ~/docker/dentalcarepro
./setup.sh            # aggiornamento completo prod (pull + install)
./setup.sh --update   # solo pull + rebuild app prod (no config, no DB)
```

### Collaudo (#41)
- **`setup-coll.sh`**: bootstrap dello stack di collaudo in `~/docker/dentalcarepro-coll`.
- **`install-coll.sh`**: esegue il build e deployment su `docker-compose.coll.yml` (porta host 8082, profilo backend `coll`, DB `dentalcare_coll`).

Comandi per collaudo:
```bash
cd ~/docker/dentalcarepro-coll
./setup-coll.sh            # aggiornamento collaudo completo
./setup-coll.sh --update   # rebuild veloce collaudo
```

### Accesso al repository
Dal 24/09/2026 il repository applicativo è **privato**: i server lo leggono con una **deploy key
in sola lettura**, una per macchina. Alla prima esecuzione `setup.sh` / `setup-coll.sh` creano
la chiave e l'alias SSH, stampano la chiave pubblica e si fermano finché non è aggiunta su
GitHub (*Settings → Deploy keys*, senza accesso in scrittura); poi convertono l'`origin` dei
clone esistenti. Per revocare una macchina basta eliminarne la chiave. La documentazione resta
pubblica.

### Registrazione, prova gratuita, ambiente di prova degli studi (#69, #70)
Tre porte indipendenti, in `config/application-prod.properties`:

| Proprietà | Ambiente di prova pubblico | Produzione con pazienti reali |
|---|---|---|
| `app.registration.customer-enabled` | `true` | `true` |
| `app.demo-workspace.public-registration` | `true` | **`false`** (aperta a chiunque) |
| `app.demo-workspace.public-url` | vuoto | indirizzo dell'istanza di prova |
| `app.sandbox.enabled` | `true` | `true` |
| `app.academy.enabled` | `true` | `true` |
| `app.academy.editor-emails` | chi scrive le lezioni | idem |
| `app.demo-workspace.sales-email` | destinatario delle richieste di attivazione | idem |
| `app.mail.send-real-emails` | `true`: la password temporanea arriva solo per e-mail | `true` |

Durata, pulizia, tetti giornalieri e limiti per IP hanno default nel codice
(`app.demo-workspace.*`, `app.rate-limit.*`). Il backend deve vedere l'IP vero del client:
nginx inoltra `X-Forwarded-For`, che il backend legge solo se arriva dal proxy interno.

## 4. Creazione database

```bash
psql -U postgres -h <db-host-lan> -d postgres \
     -v dbname=dentalcare_prod -f database/install.sql
```
`install.sql` è parametrico (`-v dbname=...`), self-contained (crea il DB, lo
schema globale, la funzione `create_tenant`, il tenant demo con dati di esempio).

## 5. Deploy della cifratura GDPR (#7)

Prerequisito **critico**: la master key deve essere in
`config/application-prod.properties` **prima** del deploy, altrimenti il backend
va in crash-loop (fail-fast). Sequenza:
1. backup DB;
2. genera master key prod (`openssl rand -hex 32`, in secret store sicuro);
3. `./setup.sh --update` (patch schema a startup);
4. `POST /api/admin/encryption/migrate` per tenant (JWT admin) → cifra i dati
   esistenti (`{"birthDate":N,"fiscalCode":M}`, idempotente);
5. verifica (pending = 0, decrypt corretto in app).

Runbook dettagliato nel repo applicativo:
`directives/deploy-gdpr-slice1-prod.md`. Rollback: il codice precedente legge
ancora il plaintext (colonne mantenute) → nessuna perdita dati.

## 6. Rollback applicativo

`git checkout <commit>` + `./setup.sh --update`. Le migrazioni di cifratura non
cancellano il plaintext, quindi il downgrade è sicuro finché le colonne
plaintext esistono.
