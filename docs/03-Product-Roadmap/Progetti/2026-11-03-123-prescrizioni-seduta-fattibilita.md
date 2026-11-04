# #123 — Prescrizioni farmacologiche a fine seduta, da catalogo farmaci ATC

**Stato:** Confermata — 03/11/2026 (decisioni in §6) · **Fase:** 1 (nessuna AI) · **Registro:** proposte-modifiche.md (registro interno delle proposte) #123

## 1. Richiesta del committente (03/11/2026)

- Il medico prescrive farmaci **al termine di una seduta, prima della chiusura**, in una sezione **sotto le note**.
- I farmaci si **scelgono da un elenco**: serve un'**anagrafica dei farmaci** con i **codici ATC** più usati dai dentisti, **divisa in categorie** come le voci dell'anamnesi.

## 2. Cosa esiste oggi (verificato sul codice)

| Pezzo | Stato | Dove |
|---|---|---|
| Tabella `patient_prescriptions` (per sede, con `clinic_id`) | Esiste. `drug_name` è **testo libero**, come dosaggio, frequenza e durata. Mancano il legame con l'appuntamento, il codice ATC e il riferimento a un catalogo | `install.sql`, `PrescrizioneService` |
| Scheda **Prescrizioni** nella cartella del paziente | Esiste. Inserimento manuale a testo libero, con allegato | `features/pazienti/prescrizioni/` |
| Cancellazione | **`DELETE` fisico** (`PrescrizioneService.delete`). Va contro la regola del soft delete sui dati clinici (#18 Blocco 1) | `PrescrizioneService.java:125` |
| Chi altro legge le prescrizioni | Fotografia dell'episodio (`EpisodeSnapshotService`) ed elenco tabelle del paziente (`PatientService:252`) | — |
| Scheda di seduta | Esiti per prestazione con «Note sull'esito», poi la barra «Registra seduta» / «Chiudi seduta». Non c'è nessuna sezione per i farmaci | `scheda-seduta.component.html` |
| Catalogo anamnesi | Due livelli: modello globale `dentalcare.anamnesis_categories/items` e copia **per tenant** `t_xxx.anamnesis_*`, condivisa fra le sedi (senza `clinic_id`), modificabile con `AnamnesisCatalogService` | modello da riusare |

**Discrepanza trovata.** La lezione Academy `diagnosi-prescrizioni-documenti.md` dice che le prescrizioni «sono le *terapie in corso* che la scheda di seduta ti mostra fra gli alert». Nel codice gli alert della seduta arrivano da `ClinicalAlertService`, che legge l'**anamnesi** (flag anticoagulanti/bisfosfonati/cortisone e `current_medications`), non `patient_prescriptions`. O si fa diventare vera la frase (vedi §4, slice C), o si corregge la lezione.

## 3. Verdetto

**Fattibile in Fase 1, rischio basso.** Non serve AI e non cambia l'architettura: si riusano tre schemi già collaudati:
1. il catalogo a due livelli dell'anamnesi (modello globale + copia per tenant);
2. il ciclo della seduta di #56/#62 (autore dal JWT, vincolo di ruolo, versione della scheda);
3. il soft delete chiesto da #18.

L'unico punto delicato è normativo: in Fase 1 il sistema **registra** la prescrizione e può stamparne un promemoria. **Non sostituisce la ricetta** firmata dal medico e **non la trasmette** al Sistema TS. L'eventuale obbligo di ricetta bianca elettronica va verificato con il committente e collocato con #21 (terminologia, FSE).

## 4. Proposta tecnica

### 4.1 Dati

**Catalogo farmaci: per tenant, condiviso fra le sedi, come l'anamnesi.**

```sql
-- Modello globale (seed gestito da noi) e copia per tenant (stessa struttura, senza clinic_id)
CREATE TABLE IF NOT EXISTS <schema>.drug_categories (
    id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    code        text,
    name        text NOT NULL CHECK (length(trim(name)) > 0),
    icon        text NOT NULL DEFAULT 'medication',
    sort_order  integer NOT NULL DEFAULT 100,
    enabled     boolean NOT NULL DEFAULT true,
    created_at  timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS <schema>.drug_items (
    id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    category_id        uuid NOT NULL REFERENCES <schema>.drug_categories(id),
    atc_code           varchar(7) NOT NULL CHECK (atc_code ~ '^[A-Z][0-9]{2}[A-Z]{2}[0-9]{2}$'),
    active_ingredient  text NOT NULL,          -- principio attivo
    label              text NOT NULL,          -- es. «Amoxicillina 1 g compresse»
    pharmaceutical_form text,                  -- compresse, bustine, collutorio, gel…
    default_dosage     text,                   -- proposte modificabili, mai confermate da sole
    default_frequency  text,
    default_duration   text,
    sort_order         integer NOT NULL DEFAULT 100,
    enabled            boolean NOT NULL DEFAULT true,
    created_at         timestamptz NOT NULL DEFAULT now()
);
```

L'ATC classifica il **principio attivo**, non la confezione. Il catalogo resta quindi a livello di principio attivo e forma; il codice AIC della confezione non serve in Fase 1.

**`patient_prescriptions`: colonne aggiunte, nessuna tolta.**

| Colonna | Perché |
|---|---|
| `appointment_id uuid NULL` | Legame con la seduta. `NULL` per le prescrizioni fatte dalla cartella e per quelle storiche |
| `drug_item_id uuid NULL` | Voce di catalogo scelta. `NULL` per le righe storiche a testo libero |
| `atc_code varchar(7) NULL`, `active_ingredient text NULL` | **Copia** di ciò che è stato prescritto: se la voce di catalogo cambia o viene disattivata, la prescrizione resta com'era |
| `drug_name` (esiste) | Resta: diventa la copia dell'etichetta della voce. Gli altri lettori (fotografie, Copilot) non cambiano |
| `voided_at`, `voided_by_provider_id`, `void_reason` | Soft delete al posto del `DELETE` fisico |

Applicazione: `EstimateSchemaInitializer`, DDL idempotente, **prima le colonne e poi le viste** (regola di #7). Poi rigenerare `install.sql`.

### 4.2 Backend

- `DrugCatalogService` + controller `/api/drug-catalog` (categorie, voci, ricerca per principio attivo, etichetta o ATC). Lettura: ruoli clinici e segreteria. Scrittura: `TENANT_ADMIN`. Copia del pattern di `AnamnesisCatalogService`.
- Prescrizioni di seduta: `GET/POST /api/appointments/{id}/session/prescriptions` e `POST .../{prescriptionId}/void`.
  - **Solo `DOCTOR`**: l'igienista non prescrive farmaci (da confermare, §6).
  - Autore **dal contesto autenticato**, mai dal body (come #56).
  - Rifiuto (409) su seduta annullata o chiusa: dopo la chiusura si prescrive dalla cartella (§6, decisione 3).
  - Senza `drug_item_id` valido e attivo nel catalogo del tenant → 400, anche dalla cartella (decisione 1).
- `SessionSheetDto` + `prescriptions`; la risposta di `close` le riporta, così la chiusura dice tutto quello che contiene.
- `PrescrizioneService.delete` → annullamento (soft delete); l'elenco della cartella nasconde le annullate, salvo filtro.
- Test: ruolo, autore, isolamento per sede/tenant, catalogo disattivato, seduta annullata, copia dei dati del farmaco.

### 4.3 Frontend

- **Scheda di seduta**: sezione «Prescrizioni» **sotto le note**, prima della barra finale.
  - Ricerca nel catalogo raggruppata per categoria (principio attivo, nome, ATC).
  - Alla scelta: posologia, frequenza e durata **proposte e modificabili**.
  - Ogni prescrizione si aggiunge con un'azione esplicita.
  - Elenco delle prescrizioni della seduta, ciascuna annullabile finché la seduta è aperta.
  - La conferma di chiusura le elenca.
- **Impostazioni → Anagrafiche → Farmaci** (`TENANT_ADMIN`): categorie e voci, come il catalogo anamnesi.
- **Cartella → Prescrizioni**: colonna ATC, «da seduta del gg/mm» con collegamento, nuove prescrizioni solo da catalogo, «Annulla» al posto di «Elimina».

### 4.4 Storico delle prescrizioni della seduta (richiesta del committente, 03/11/2026)

Lo storico non è una tabella a parte: sono le righe stesse, che **non si modificano più dopo l'emissione**.

- **Prescrizione emessa = immutabile.** Non si aggiornano più principio attivo, posologia, frequenza e durata. Si corregge **annullando e sostituendo**: la nuova riga ha `replaces_prescription_id` verso la vecchia, la vecchia ha `voided_at` / `voided_by_provider_id` / `void_reason` (motivo obbligatorio). Il `PUT` attuale resta solo per le righe storiche a testo libero, finché non vengono sostituite.
- **Colonne in più** rispetto a §4.1: `replaces_prescription_id uuid NULL`, `issued_by_provider_id` (dal JWT; oggi `provider_id` arriva dal body), `warnings_acknowledged jsonb NULL` (avvisi di §5 slice D mostrati al medico e da lui presi visione), `printed_at timestamptz NULL` (ultima stampa).
- **Scheda di seduta**: l'elenco mostra tutte le prescrizioni della seduta, le annullate barrate con chi, quando e perché, e «sostituita da». Si annulla o sostituisce **solo a seduta aperta** (decisione 3).
- **Cartella → Prescrizioni**: raggruppate **per seduta** (data, medico, collegamento alla seduta) più il gruppo «dalla cartella». Le annullate si vedono con il filtro «mostra annullate». Dopo la chiusura della seduta l'annullamento si fa da qui, con motivo, e resta nello storico della seduta d'origine.
- **Lettori esistenti**: le fotografie degli episodi (#67, `EpisodeSnapshotService`) e gli alert della seduta (slice C) leggono solo le prescrizioni **non annullate**.
- **Stampa** (decisione 4): si stampa la versione in vigore; un'annullata non si stampa. Ogni stampa aggiorna `printed_at`.
- Quando arriverà l'audit trail di #18 Blocco 1, emissione, annullamento e stampa vi entrano come eventi. Lo storico qui sopra non lo sostituisce, ma ne è già compatibile.

### 4.5 Catalogo di partenza (seed) — **da validare clinicamente dal committente**

Proposta di ~30 voci. Ogni codice ATC va verificato sull'indice OMS ATC/DDD (o AIFA) prima del seed.

| Categoria | Principio attivo | ATC |
|---|---|---|
| Antibiotici | Amoxicillina | J01CA04 |
| | Amoxicillina + acido clavulanico | J01CR02 |
| | Azitromicina | J01FA10 |
| | Claritromicina | J01FA09 |
| | Clindamicina | J01FF01 |
| | Cefalexina | J01DB01 |
| | Spiramicina + metronidazolo | J01RA04 |
| | Metronidazolo (orale) | P01AB01 |
| Antinfiammatori (FANS) | Ibuprofene | M01AE01 |
| | Naprossene | M01AE02 |
| | Ketoprofene | M01AE03 |
| | Diclofenac | M01AB05 |
| | Ketorolac | M01AB15 |
| | Nimesulide | M01AX17 |
| Analgesici | Paracetamolo | N02BE01 |
| | Paracetamolo + codeina | N02AJ06 |
| | Tramadolo | N02AX02 |
| Corticosteroidi | Betametasone | H02AB01 |
| | Desametasone | H02AB02 |
| | Metilprednisolone | H02AB04 |
| | Prednisone | H02AB07 |
| Antisettici del cavo orale | Clorexidina | A01AB03 |
| Antimicotici | Miconazolo (gel orale) | A01AB09 |
| | Nistatina | A07AA02 |
| | Fluconazolo | J02AC01 |
| Antivirali | Aciclovir (sistemico) | J05AB01 |
| | Aciclovir (crema) | D06BB03 |
| Gastroprotettori | Omeprazolo | A02BC01 |
| | Pantoprazolo | A02BC02 |
| Emostatici | Acido tranexamico | B02AA02 |
| Ansiolitici (premedicazione) | Diazepam | N05BA01 |
| Prevenzione | Sodio fluoruro | A01AA01 |

## 5. Slice e stima (ore agente)

| Slice | Contenuto | Stima |
|---|---|---|
| **A — Catalogo** | Tabelle globali e per tenant, seed, copia alla creazione del tenant e per i tenant esistenti, CRUD backend, Impostazioni → Farmaci | ~7-9h |
| **B — Prescrizione di seduta** | Colonne su `patient_prescriptions`, endpoint di seduta, ruoli, soft delete, sezione nella scheda di seduta, cartella aggiornata, test | ~9-11h |
| **C — Coerenza** | Prescrizioni attive fra gli alert della seduta (rende vera la lezione Academy), `install.sql`, demo seed, lezione Academy | ~3-4h |
| **D — Avvisi** (in Fase 1, decisione 5) | Avviso (non blocco) se il farmaco urta l'anamnesi: allergia alle penicilline → J01C*, anticoagulanti → M01A*. Regole per prefisso ATC ↔ codice voce di anamnesi, da mappare e far validare. Il medico prende visione con un'azione esplicita, mai una casella pre-spuntata; la presa visione resta nella prescrizione | ~4-6h |
| **E — Stampa** (in Fase 1, decisione 4) | PDF «promemoria terapia» per il paziente, per seduta, con intestazione della sede | ~3-4h |
| **F — Storico** | §4.4: immutabilità, annulla e sostituisci, viste per seduta, filtri, lettori aggiornati, test | ~3-4h |

**Totale A–F ≈ 29-38h agente (~4-5 giornate).**

Dipendenze: nessuna bloccante. Si appoggia a #56/#62, già fatte. Il soft delete anticipa un pezzo di #18 Blocco 1 e non lo ostacola.

## 6. Decisioni del committente (03/11/2026)

1. **Farmaco non in elenco: vietato.** Né in seduta né dalla cartella; il titolare aggiunge la voce da Impostazioni → Farmaci.
2. **Prescrive solo il medico** (`DOCTOR`). L'igienista e la segreteria vedono, non prescrivono.
3. **Seduta chiusa: si prescrive dalla cartella.** In seduta niente aggiunte, annullamenti o sostituzioni dopo la chiusura.
4. **Stampa del promemoria per il paziente: sì**, in Fase 1 (slice E).
5. **Avvisi su allergie e interazioni: in Fase 1** (slice D).
6. **Catalogo: modello globale gestito da noi**, copiato in ogni tenant e modificabile dal titolare, come l'anamnesi.
7. **Storico delle prescrizioni della seduta** (aggiunta): §4.4, slice F.

Resta da fare prima del seed: verifica dei codici ATC sull'indice OMS e validazione clinica dell'elenco e delle regole di avviso.

## 7. Privacy

Le prescrizioni sono già dati sanitari in `patient_prescriptions`, per sede. Legarle alla seduta non aggiunge categorie di dati né destinatari. **Se** si sceglie di **inviare** il promemoria al paziente per e-mail o WhatsApp, è un trattamento nuovo: serve una voce D-xx nel registro DPIA, nella stessa sessione. La sola stampa non lo richiede.
