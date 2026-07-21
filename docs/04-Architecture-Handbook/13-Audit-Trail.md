# 13 — Audit trail clinico (modello probatorio)

> Questo capitolo documenta il **modello probatorio** dell'audit trail clinico —
> lo *stato-obiettivo* completo — e il **taglio operativo** che lo porta al
> go-live: cosa entra davvero nel gate della
> [Release 1.x](../03-Product-Roadmap/Release-1.x.md) (**Tier 1**) e cosa è
> deliberatamente differito (**Tier 2**). La descrizione sintetica dell'entità
> *Audit event* dentro il modello dati è in
> [12 §4](12-Clinical-Record-Model.md#4-audit-trail); qui si spiega il **perché**
> e il **quanto**: forza probatoria, decisioni di design ancora aperte,
> dipendenza dagli altri interventi della cartella.
>
> **Stato: 🔨 non implementato.** È la **prima milestone tecnica** della
> Release 1.x. Nessuno studio usa la piattaforma su pazienti reali finché questo
> livello non è chiuso.

## 1. "Probatorio" non è "salvare i log"

Un modello probatorio non consiste nello scrivere righe in una tabella di log. È
un insieme **coordinato** di registrazioni tecniche, identificazione certa degli
operatori, versionamento dei dati clinici, garanzie di integrità e data certa,
procedure organizzative e modalità controllate di estrazione della prova.

L'obiettivo è poter dimostrare, anche anni dopo:

> **chi** ha fatto **cosa**, **quando**, su **quale paziente**, con **quale
> autorizzazione**, per **quale finalità**, e **senza che le registrazioni siano
> state alterate.**

Due conseguenze guidano tutto il resto:

- **Le consultazioni (letture) vanno registrate**, non solo creazione, modifica e
  cancellazione. Il Garante ha ribadito nel 2026 che i sistemi sanitari devono
  tracciare automaticamente accessi *e consultazioni* e prevedere alert per i
  comportamenti anomali. È il singolo requisito che costa di più (§4, T1.6).
- **Nel log non finisce il contenuto clinico.** Non *"il paziente ha una lesione
  periapicale"*, ma identificativo del documento, versione, hash, tipo di
  modifica, codice del campo. Il contenuto resta nel repository clinico
  versionato ([12 §3](12-Clinical-Record-Model.md#3-ciclo-di-vita-dellinformazione-clinica));
  ISO 27789 raccomanda proprio riferimenti, non duplicazione del dato sanitario.

## 2. Stato attuale (verificato sul codice)

| Cosa | Stato |
|---|---|
| **`ai_audit_log`** (per-tenant) | Esiste ma traccia **solo il Copilot**: colonne piatte (`clinic_id, provider_id, action_type, tool_name, args_summary, result, created_at`). **Non** append-only enforced, **niente** hash chain. È il §11 del modello (inferenza AI): da **assorbire e irrobustire**, non da buttare. |
| **Audit clinico su accessi / letture / scritture** della cartella | **Assente.** È il buco che la Release 1.x chiude. |
| **Versionamento / finalizzazione** delle note cliniche | **Assente** → intervento correlato (finalizzazione + addendum, [12 §3.1](12-Clinical-Record-Model.md#31-stati-di-una-nota-clinica)). Vedi la dipendenza in §5. |
| **Architettura di riferimento** | Schema-per-tenant, evoluzione via `patchSchema` idempotente (colonne/tabelle `IF NOT EXISTS` a ogni avvio, vedi [06-Multitenancy](06-Multitenancy.md)). |

## 3. Il taglio: Tier 1 (gate) vs Tier 2 (differito)

Il modello completo, preso alla lettera per il go-live, tira dentro **terze parti
a pagamento** (timestamp e sigilli qualificati eIDAS, che richiedono un contratto
QTSP) fuori dai tempi della Release 1.x. Il taglio isola il **minimo legale**.

> **Regola del taglio.** **Tier 1** = condizione d'ingresso del go-live: nessun
> paziente reale senza. **Tier 2** = si fa *dopo* il go-live, o quando un evento
> concreto lo richiede (contenzioso, ispezione, apertura Release 2.x). Mettere il
> Tier 2 nel gate significa non arrivare alla data di go-live.

L'MVP è difendibile senza QTSP: **DB append-only + hash chain interna** soddisfa
il requisito legale di tracciabilità inalterabile; il livello eIDAS **alza** la
data da "server" a "opponibile a terzi", ma è un rafforzamento, non la soglia
d'ingresso.

## 4. Tier 1 — obbligatorio per il go-live

Ordinato per **costo di implementazione**, non per importanza: tutte le voci sono
obbligatorie.

| # | Requisito | Scope MVP | Fonte | Costo |
|---|---|---|---|---|
| T1.1 | **Retention** ≥ 24 mesi (accessi al dossier) · ≥ 6 mesi (admin) | Policy di conservazione; nessuna cancellazione sotto soglia | Garante 10262049 / 1577499 | banale |
| T1.2 | **Contenuto minimo evento** | operatore, `occurred_at` UTC ms, postazione/IP, paziente, tipo operazione, esito | Garante 10262049 · ISO 27789 | basso |
| T1.3 | **Append-only enforced a livello DB** | tabella `clinical_audit_log` per-tenant; grant applicativo **solo INSERT**; nessuna vista che consenta modifica | modello §3–§4 | basso |
| T1.4 | **Hash chain interna** | ogni evento porta `event_hash` (SHA-256 su JSON canonico); tamper-evidence **senza** QTSP | modello §4 | basso–medio (vedi §6, decisione A) |
| T1.5 | **Attribuzione reale** | non solo `user_id`: ruolo-al-momento, metodo auth/MFA, `session_id`, e **perché la policy ha concesso** (`rule`, relazione di cura) | modello §5 | medio |
| T1.6 | **Logging delle CONSULTAZIONI** (letture) | apertura paziente / anamnesi / odontogramma / referto / documento → evento. **Costo dominante**: trasversale ai service clinici | Garante 10262049 (esplicito) | **alto** |
| T1.7 | **Alert base anomalie** | versione batch/query, non realtime: "N pazienti in M minuti", accesso senza relazione di cura, negati ripetuti, break-glass | Garante 10262049 | medio |
| T1.8 | **Eventi break-glass + admin** | accesso straordinario con motivazione obbligatoria + evento; accessi amministrativi nominativi tracciati | modello §5 | medio |

**Definizione di "fatto" (mappa sul gate della [Release 1.x §29](../03-Product-Roadmap/Release-1.x.md)):**
audit clinico **append-only** attivo (T1.3), che copre le **consultazioni** oltre
alle scritture (T1.6), con contenuto minimo e attribuzione (T1.2, T1.5); ogni
accesso **negato** registrato **con la ragione** (T1.5, accoppiato
all'enforcement dei ruoli lato server, [07-Security §2](07-Security.md));
break-glass tracciato (T1.8); retention configurata (T1.1); alert base (T1.7).

## 5. Tier 2 — differito (eccellente, ma non blocca il go-live)

| Requisito | Perché è Tier 2 | Trigger per farlo |
|---|---|---|
| **Audit Evidence Service** separato + transactional outbox + SIEM | Infrastruttura, settimane. L'MVP per-tenant append-only regge il requisito legale | Scala / SOC / più tenant reali |
| **Timestamp e sigilli qualificati eIDAS** + radici Merkle | Richiede **contratto QTSP** (costo + integrazione). Alza la data da "server" a "opponibile a terzi" | Primo contenzioso / richiesta legale |
| **Evidence Package generator** (pacchetto di prova firmato) | Feature intera; serve quando c'è una prova da produrre | Reclamo / ispezione / causa |
| **Catena di custodia con tooling** | Il minimo procedurale (log dell'export) è già in T1.6/T1.8; il tooling completo è dopo | Con l'Evidence Package |
| **Log inferenza AI clinica** | La radiologia è **spenta** in Fase 1 → roba Release 2.x. Il copilot (AI amministrativa) è già in `ai_audit_log` | Apertura Release 2.x (MDR) |
| **Alert realtime / ML anomalie** | L'MVP batch (T1.7) soddisfa il Garante | Volumi reali |

## 6. Decisioni di design aperte

Quattro scelte cambiano la forma del codice e vanno chiuse in fase di progetto,
non decise implicitamente. Ognuna ha una raccomandazione di partenza.

### A — Concorrenza della hash chain

"Ogni evento porta l'hash del precedente" presuppone un **ordine totale**. Due
scritture cliniche in parallelo si contendono il "precedente" → catena rotta,
oppure lock globale per-tenant (collo di bottiglia).

- **A1** — sequenza single-writer per tenant: chain per-riga vera, ma serializza
  le scritture di audit.
- **A2** *(raccomandato per l'MVP)* — nessuna chain per-riga bloccante; **sigillo
  periodico** (radice Merkle a fine ora/giorno) su un batch ordinato. Nessun
  lock, e prepara naturalmente il livello probatorio forte del Tier 2.
  `event_hash` per-riga sì, `previous_event_hash` bloccante solo se e quando
  serve.

### B — Dove vive il log

- **B1** *(raccomandato per Tier 1)* — `clinical_audit_log` **dentro ogni schema
  tenant**, via `patchSchema`. Coerente con l'esistente, isolamento per-tenant
  gratuito.
- **B2** — schema globale unico per l'audit. Più vicino al Tier 2 ma rompe il
  pattern schema-per-tenant e mescola i tenant.

### C — Come si instrumentano le letture (T1.6)

È il costo vero, perché tocca molti punti del codice clinico.

- **C1** — intercettore/aspect trasversale su controller/service clinici: poco
  codice ripetuto, ma rischio di loggare troppo o troppo poco.
- **C2** — chiamata esplicita `auditService.logRead(...)` nei punti clinici:
  verboso ma preciso.
- *Da decidere in base a quanti e quali endpoint contano come "consultazione del
  dossier".*

### D — Modulo interno vs servizio separato (riuso)

L'audit come modulo dentro il backend, o come **servizio separato** che
DentalCare usa applicativamente e che un altro applicativo medico potrebbe
riusare?

- **D1** *(raccomandato per Tier 1)* — **modulo interno dietro un'interfaccia
  stretta** `AuditService.record(event)`, con contratto d'evento stabile. Scrive
  su `clinical_audit_log` per-tenant. **L'interfaccia È già la cucitura del
  riuso.**
- **D2** *(Tier 2)* — servizio separato, dominio di sicurezza distinto (auditor ≠
  audited). Si ottiene **cambiando l'implementazione dietro l'interfaccia D1**: i
  punti di chiamata non si toccano. Precedente identico già in codice:
  `MasterKeyProvider` / `ConfigMasterKeyProvider`, seam pronto per Vault (vedi
  [07-Security §3](07-Security.md)).
- **Il ponte tra i due è il transactional outbox.** Chiamare un microservizio
  audit in sincrono crea il *dual-write*: la scrittura clinica committa, l'audit
  fallisce → si perde la prova; oppure l'audit giù blocca lo studio. Soluzione:
  l'evento va in tabella **nella stessa transazione** della modifica clinica; un
  relay lo spedisce dopo, async e ritentabile. **La `clinical_audit_log` del
  Tier 1 è già quell'outbox:** il Tier 2 aggiunge solo il relay, zero rilavoro.
- **Non generalizzare adesso.** Con un solo applicativo, progettare l'astrazione
  "servizio audit medico generico" significa indovinare i requisiti del secondo
  (YAGNI / regola del tre). L'estrazione si fa quando il secondo caso è reale;
  l'interfaccia D1 la rende economica.
- **Caveat compliance del riuso:** un servizio audit che ospita dati sanitari di
  più applicativi diventa **lui stesso** responsabile del trattamento — sua
  DPIA, suo DPA, sua postura di sicurezza. Il riuso moltiplica il perimetro che
  il DPO deve coprire: è una decisione di prodotto, non solo tecnica. In nessun
  caso l'ambizione del riuso deve far ritardare il gate.

## 7. Dipendenza con finalizzazione e versionamento

L'evento di audit del modello contiene `version_before` / `version_after`. Quei
numeri **esistono solo se** la cartella è versionata — cioè la finalizzazione +
addendum ([12 §3.1](12-Clinical-Record-Model.md#31-stati-di-una-nota-clinica)).

Conseguenza: audit e versionamento **non sono del tutto indipendenti**, ma **non**
vanno fatti in blocco.

- L'MVP dell'audit logga l'azione **senza** i numeri di versione all'inizio
  (`version_before` / `version_after` nullable).
- Quando atterra la finalizzazione, l'evento si **arricchisce** puntando alla
  versione.

Ordine: **audit prima (fondazione), finalizzazione dopo, l'audit si completa
retroattivamente sui nuovi eventi.** Non serve attendere il versionamento per
chiudere il Tier 1.

## 8. Schema di partenza (bozza, non definitivo)

Concretezza per la fase di progetto; da rivedere con le decisioni §6.

```sql
-- per-tenant, creata da patchSchema. Append-only: grant solo INSERT.
CREATE TABLE <schema>.clinical_audit_log (
    id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    clinic_id         uuid NOT NULL,
    event_type        text NOT NULL,        -- READ | UPDATE | CREATE | FINALIZE | EXPORT | BREAK_GLASS | ...
    occurred_at_utc   timestamptz NOT NULL DEFAULT now(),
    -- attore (T1.5)
    actor_provider_id uuid,
    actor_role        text NOT NULL,        -- ruolo AL MOMENTO, dal JWT
    auth_level        text,                 -- PASSWORD | MFA
    session_id        text,
    ip_address        inet,
    -- soggetto
    patient_id        uuid,
    encounter_id      uuid,
    resource_type     text,                 -- ODONTOGRAM | ANAMNESIS | HISTORY_ENTRY | DOCUMENT | ...
    resource_id       uuid,
    version_before    integer,              -- nullable finché non c'è la finalizzazione (§7)
    version_after     integer,
    -- operazione + autorizzazione (T1.2, T1.5)
    action            text NOT NULL,
    purpose           text,                 -- PATIENT_CARE | ADMIN | ...
    result            text NOT NULL,        -- SUCCESS | DENIED | ...
    authz_rule        text,                 -- perché la policy ha concesso/negato
    reason            text,                 -- motivazione (obbligatoria per BREAK_GLASS)
    -- integrità (T1.4, decisione A)
    event_hash        text NOT NULL         -- SHA-256 su rappresentazione canonica
    -- previous_event_hash text  -- solo se si sceglie A1
);
```

I documenti formali di governance (politica di audit, catalogo eventi, matrice
ruoli/finalità, procedura di estrazione, retention policy approvata da titolare /
DPO / legale) sono **Tier 2 / governance** — non codice, non bloccano l'MVP
tecnico, ma sono il prodotto del percorso con il DPO.

## 9. Sintesi

> **Database clinico versionato + audit log append-only + hash chain + (Tier 2)
> manifest periodici sigillati e timestampati + procedura documentata di
> estrazione e verifica.**

La blockchain non serve: architettura WORM, hash concatenati, e — al Tier 2 —
sigillo e validazione temporale qualificati con conservazione governata sono più
semplici, controllabili e difendibili. Il collo di bottiglia del percorso **non è
il codice** (settimane), ma l'ingaggio del **DPO** per la governance.

---

## Riferimenti

- [12-Clinical-Record-Model §4](12-Clinical-Record-Model.md#4-audit-trail) —
  l'entità *Audit event* nel modello dati · [07-Security](07-Security.md) ·
  [06-Multitenancy](06-Multitenancy.md) · [04-AI](04-AI.md)
- [Release 1.x](../03-Product-Roadmap/Release-1.x.md) — scope e criteri di go-live
- [Garante — provvedimento Doc-Web 10262049](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10262049)
  (tracciamento accessi/consultazioni, alert, retention ≥ 24 mesi)
- [Garante — amministratori di sistema, Doc-Web 1577499](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/1577499)
  (access log inalterabili, retention ≥ 6 mesi)
- [ISO 27789:2021](https://www.iso.org/standard/75313.html) — audit trail per EHR ·
  [ISO/IEC 27037:2012](https://www.iso.org/standard/44381.html) — evidenze digitali
- [Regolamento eIDAS (UE) 910/2014, testo consolidato](https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX%3A02014R0910-20241018)
  — timestamp e sigilli qualificati
- [CAD — D.Lgs. 82/2005, art. 20](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art20=)
  — valore probatorio del documento informatico
