# 08 — DevOps

## 1. Build

**Backend** (Maven, wrapper incluso):
```bash
cd backend
./mvnw clean install     # build + test
./mvnw spring-boot:run    # avvio locale (:8080, profilo default)
./mvnw test               # solo test
```
Java 25 (Adoptium). `JAVA_HOME` deve puntare a un JDK 25.

**Frontend** (npm):
```bash
cd frontend
npm install
npm start        # dev server (:4200)
npm run build    # bundle di produzione
```

## 2. Containerizzazione

Immagini Docker multi-stage:
- **backend**: build Maven → runtime JRE, immagine `dentalcarepro-backend`.
- **frontend**: build Angular → nginx (`listen 4200`, proxa `/api` al backend
  interno), immagine `dentalcarepro-frontend`.
- **dentalcare-ai-service**: Python FastAPI + ONNX, immagine
  `dentalcare-ai-service`.

Orchestrazione con `docker-compose.yml` (file unico, niente override). Tag
immagini via `${VERSION}` da `.env`.

## 3. Configurazione e segreti

- I default non sensibili sono nel classpath (`application*.properties`).
- I **segreti reali** stanno in config esterne **gitignored**:
  - dev: `backend/config/` (sovrascrive il classpath);
  - prod: `config/application-prod.properties` **montata** nel container
    (`./config:/app/config:ro` + `SPRING_CONFIG_ADDITIONAL_LOCATION`).
- Segreti gestiti: password DB, `app.jwt.secret`, `app.encryption.master-key`
  (obbligatoria, fail-fast), chiavi OpenAI/n8n/MinIO/HMAC.
- Precedenza: `backend/config/` (e `config/` montata in prod) **override** dei
  default del classpath.

## 4. Ambienti

| Ambiente | Backend | DB | Frontend |
|----------|---------|----|----------|
| dev | `mvnw spring-boot:run` (:8080, profilo default) | `dentalcarepro` @ 192.168.0.173 | `npm start` (:4200) |
| prod | container (profilo `prod`, non esposto) | `dentalcare_prod` @ 192.168.0.173 | nginx :4200 → host :8181 |

## 5. Versioning e convenzioni

- Repo Git unico (`fpapale/dentalcare`), branch principale `master`.
- Commit convenzionali: `feat(...)`, `fix(...)`, `docs(...)`, `refactor(...)`,
  `test(...)`.
- `.gitattributes` forza `eol=lf` su `*.sh` e `*.sql`.
- Modelli AI ONNX gitignored (distribuiti a parte).

## 6. Osservabilità

- Logging via SLF4J (livelli per package); in prod `root=WARN`,
  `com.dentalcare=INFO`.
- Healthcheck backend: `GET /api/public/demo-config` (usato dal compose e da
  `install.sh`).
