# DentalCare Pro — Conformità EU AI Act

**Versione:** 1.0  
**Aggiornato:** 2026-07-28  
**Riferimento normativo:** Regolamento (UE) 2024/1689 — EU AI Act

---

## Classificazione sistemi AI

| Modulo | Classificazione AI Act | MDR | Obblighi principali |
|---|---|---|---|
| Copilot interno (SegretarIA) | AI con obblighi trasparenza | Non MD | Disclosure operatore, AI literacy |
| Giulia voice agent (Retell) | AI con obblighi trasparenza art. 50 | Non MD | Disclosure paziente obbligatoria |
| Analisi ortopanoramica (ONNX) | Probabile high-risk art. 6(1) | Probabile MDSW IIa | Percorso MDR + scadenza 2028-08-02 |
| LLM riassunti clinici | Da valutare | Possibile MDSW | Valutazione Regulatory prima rilascio |

---

## Scadenze operative

| Data | Obbligo | Stato |
|---|---|---|
| **2026-08-02** | Disclosure AI obbligatoria (art. 50) + AI literacy | ✅ implementato |
| 2026-12-02 | Verifica Digital Omnibus e marcatura contenuti sintetici | ⬜ da pianificare |
| 2027-12-02 | Obblighi high-risk sistemi standalone Annex III | ⬜ da pianificare |
| **2028-08-02** | Obblighi high-risk modulo radiologico (product-embedded) | ⬜ percorso MDR in corso |

---

## Misure implementate al 2026-07-28

### Giulia Voice Agent (Retell AI)

**Disclosure art. 50:** Giulia si identifica come sistema AI all'apertura di ogni chiamata:

> "Buongiorno, sono Giulia, la segreteria virtuale basata sull'intelligenza artificiale dello Studio Dentistico DentalCare. Come posso aiutarla?"

**Risposta a "Sei umano?":** risposta esplicita obbligatoria senza eccezioni:

> "No, sono un sistema basato sull'intelligenza artificiale."

**Escalation umana:** su richiesta del paziente, Giulia trasferisce a operatore.  
**Emergenze:** Giulia rimanda al 118 senza valutazioni cliniche autonome.

Documentazione tecnica: `compliance/aiact/retell/` nel repo principale.

### Copilot interno (SegretarIA)

**Disclosure:** messaggio di apertura con badge "Assistente AI · EU AI Act art. 50" ad ogni sessione.  
**System prompt:** clausola esplicita identità AI + divieto fingersi umano.  
**History isolation:** il messaggio di disclosure non viene incluso nella history inviata al backend.

---

## Procedura aggiornamento Giulia

Ogni modifica al system prompt Retell segue questo workflow:

1. Modifica `Segretaria/SmileDesk Agent - retell.ai.md` (working draft)
2. Salva versione in `Segretaria/SmileDesk Agent - retell.ai_REL<X.Y>.md`
3. Verifica clausole AI Act obbligatorie (disclosure + "Sei umano?")
4. Test in preproduzione (3 scenari minimi)
5. Deploy su Retell
6. Snapshot in `compliance/aiact/retell/` + screenshot + `attivazione.md`
7. Commit e push

Procedura completa: `directives/procedura-aggiornamento-giulia-retell.md`

---

## Inspection Readiness Binder

Il binder di ispezione è organizzato in 15 cartelle (§28 del piano compliance).  
Cartella 13 — Trasparenza (Giulia): `compliance/aiact/retell/`

Evidenze presenti:
- ✅ System prompt REL 1.0 (snapshot immutabile)
- ✅ Registro attivazione compilato
- ⬜ Screenshot Retell dashboard (da aggiungere manualmente)
- ⬜ Log test call post-attivazione

---

## Documenti di riferimento (repo principale)

| File | Contenuto |
|---|---|
| `directives/DentalCare_Pro_EU_AI_Act_Compliance_2026.md` | Piano compliance completo |
| `directives/procedura-aggiornamento-giulia-retell.md` | Procedura operativa aggiornamenti |
| `Segretaria/giulia-voice-disclosure-aiact.md` | Script disclosure + checklist binder |
| `Segretaria/SmileDesk Agent - retell.ai_REL1.0.md` | System prompt produzione corrente |
| `compliance/aiact/retell/` | Inspection Binder Cartella 13 |
