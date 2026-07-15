# 09 — Deployment

## 1. Topologia di produzione

- **Macchina applicativa**: `192.168.0.72`, cartella `~/docker/dentalcarepro`.
- **Database**: `dentalcare_prod` su PostgreSQL `192.168.0.173`.
- **Backend** non esposto sull'host: l'nginx del frontend proxa `/api` al
  backend interno. Solo il **frontend** è pubblicato, via due percorsi verso lo
  stesso container:
  - **pubblico**: `https://paaplef.duckdns.org:8181` (HTTPS, reverse proxy TLS);
  - **diretto (server o LAN)**: `http://192.168.0.72:<FRONTEND_PORT>` (HTTP,
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
./setup.sh            # aggiornamento completo (pull + install)
./setup.sh --update   # solo pull + rebuild app (no config, no DB)
```

## 4. Creazione database

```bash
psql -U postgres -h 192.168.0.173 -d postgres \
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
