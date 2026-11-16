#!/usr/bin/env python3
"""Integrazione idempotente dei documenti Fase 4 nel wiki DentalCare.

Eseguire dalla root di fpapale/DentalCare-Documentation DOPO aver estratto lo ZIP.
Il programma aggiorna solo indici/roadmap/registro DPIA, e non modifica dati reali.
"""
from __future__ import annotations
import argparse
from pathlib import Path


def append_section(root: Path, relative: str, marker: str, section: str) -> str:
    file = root / relative
    if not file.is_file():
        raise FileNotFoundError(f"File esistente atteso: {relative}")
    text = file.read_text(encoding="utf-8")
    if marker in text:
        return f"SKIP (gia' presente) {relative}"
    file.write_text(text.rstrip() + "\n\n---\n\n" + section.strip() + "\n", encoding="utf-8")
    return f"UPDATE {relative}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="root del repository documentale")
    args = parser.parse_args()
    root: Path = args.root.resolve()
    required = [
        "docs/03-Product-Roadmap/Progetti/2026-11-12-fase-4-clinical-intelligence.md",
        "docs/04-Architecture-Handbook/17-Clinical-Event-Model-and-Predictive-AI.md",
        "docs/06-Compliance/Fase-4-Clinical-Intelligence-DPIA-Addendum.md",
    ]
    for p in required:
        if not (root / p).is_file():
            raise FileNotFoundError(f"Estrarre lo ZIP nella root prima di eseguire: {p}")

    edits = [
        (
            "README.md", "## 📌 Fase 4 — Clinical Intelligence",
            """## 📌 Fase 4 — Clinical Intelligence (progetto evolutivo)

📋 Specifica **pianificata e non implementata**. La Fase 2 rimane dedicata all'AI Copilot clinico e all'analisi delle ortopanoramiche. La Fase 4 non corrisponde automaticamente alla Release 4.x commerciale.

- [Progetto, scelte architetturali e roadmap Fase 4](docs/03-Product-Roadmap/Progetti/2026-11-12-fase-4-clinical-intelligence.md)
- [Architecture Handbook 17 — DC-CEM, pgvector, FHIR e ML](docs/04-Architecture-Handbook/17-Clinical-Event-Model-and-Predictive-AI.md)
- [Addendum DPIA per la Fase 4](docs/06-Compliance/Fase-4-Clinical-Intelligence-DPIA-Addendum.md)"""
        ),
        (
            "docs/03-Product-Roadmap/Product-Roadmap.md", "## Addendum — Fase 4 Clinical Intelligence (12/11/2026)",
            """## Addendum — Fase 4 Clinical Intelligence (12/11/2026)

📋 È stata definita la [Fase 4 — Clinical Intelligence](Progetti/2026-11-12-fase-4-clinical-intelligence.md), con DC-CEM longitudinale, RAG su pgvector, possibilità FHIR R4/HAPI PoC e modelli prognostici ML. **Non è implementata né autorizzata per uso clinico**. La Fase 2 resta Copilot clinico + analisi ortopanoramiche soggetti ai gate vigenti. Fase 4 (programma funzionale) e Release 4.x (visione commerciale) sono nomenclature distinte. [Specifica tecnica](../04-Architecture-Handbook/17-Clinical-Event-Model-and-Predictive-AI.md)."""
        ),
        (
            "docs/03-Product-Roadmap/AI-Roadmap.md", "## Addendum — Progetto Fase 4 Clinical Intelligence",
            """## Addendum — Progetto Fase 4 Clinical Intelligence

📋 Pianificato, non implementato. [Progetto completo](Progetti/2026-11-12-fase-4-clinical-intelligence.md). I modelli predittivi della Fase 4 utilizzano il Clinical Event Model derivato dalla cartella (patient/tooth/site/care pathway), con pgvector per retrieval e modelli ML distinti dall'LLM. Tutti i suggerimenti su complicanze, piani e richiami richiedono valutazione regolatoria/clinica e approvazione del medico. La Fase 2 resta dedicata al Copilot clinico e alle ortopanoramiche."""
        ),
        (
            "docs/03-Product-Roadmap/Release-4.x.md", "## Nota di perimetro: Fase 4 Clinical Intelligence",
            """## Nota di perimetro: Fase 4 Clinical Intelligence

La [Fase 4 — Clinical Intelligence](Progetti/2026-11-12-fase-4-clinical-intelligence.md) è una specifica evolutiva funzionale datata 12/11/2026 e non implica la programmazione o il rilascio della **Release 4.x** delineata in questo documento. Ne approfondisce gli aspetti di odontoiatria predittiva, eventi clinici e decision intelligence, ma non sostituisce la visione della release. Stato: 📋 non implementata."""
        ),
        (
            "docs/03-Product-Roadmap/Progetti/README.md", "Fase 4 — DentalCare Clinical Intelligence",
            """## Fase 4 — DentalCare Clinical Intelligence

📋 [Specifica funzionale, architettura, ADR, roadmap e acceptance criteria](2026-11-12-fase-4-clinical-intelligence.md) — pianificata, non implementata. [Specifica tecnica DC-CEM/FHIR/ML](../../04-Architecture-Handbook/17-Clinical-Event-Model-and-Predictive-AI.md)."""
        ),
        (
            "docs/04-Architecture-Handbook/Architecture-Handbook.md", "## Estensione 17 — Clinical Event Model",
            """## Estensione 17 — Clinical Event Model, FHIR e Predictive AI

📋 [17 — Specifica architetturale Fase 4](17-Clinical-Event-Model-and-Predictive-AI.md): schema-per-tenant, Clinical Event Model a granularità anatomica, Care Pathway distinto dagli episodi visita/contatto già implementati, pgvector, adapter FHIR R4/HAPI PoC, ML predittivo validato e controllo umano. **Solo progetto**; non descrive componenti già rilasciati."""
        ),
        (
            "docs/04-Architecture-Handbook/12-Clinical-Record-Model.md", "## Estensione futura — DC-CEM Fase 4",
            """## Estensione futura — DC-CEM Fase 4

📋 [17 — Clinical Event Model, FHIR e Predictive AI](17-Clinical-Event-Model-and-Predictive-AI.md). Il progetto introduce siti anatomici e Care Pathway longitudinali e deriva eventi dagli oggetti esistenti. **Non** ridefinisce gli episodi #67 (visita/contatto e snapshot entry/exit); fonte originale e workflow probatori restano immutati."""
        ),
        (
            "docs/04-Architecture-Handbook/04-AI.md", "## Estensione futura — Clinical Intelligence Fase 4",
            """## Estensione futura — Clinical Intelligence Fase 4

📋 [Progetto Clinical Intelligence](../03-Product-Roadmap/Progetti/2026-11-12-fase-4-clinical-intelligence.md): RAG scientifico/paziente con pgvector, ML prognostico separato dall'LLM, FHIR via adapter e supporto a piani/richiami. Nessun componente della Fase 4 è dichiarato implementato o abilitato all'uso clinico."""
        ),
        (
            "docs/06-Compliance/inventario-flussi-ai-per-dpo.md", "## Addendum — Flussi Fase 4 NON in esercizio",
            """## Addendum — Flussi Fase 4 NON in esercizio

Questo inventario descrive i flussi correnti documentati; il [progetto Fase 4](../03-Product-Roadmap/Progetti/2026-11-12-fase-4-clinical-intelligence.md) introduce solo **flussi futuri**, non ancora attivati: proiezioni storiche degli eventi clinici, embeddings di referti per account/paziente, retrieval con pgvector, eventuale server HAPI FHIR isolato, dataset derivati per ML e proposte di richiami. Vedere [D-105..D-109](Fase-4-Clinical-Intelligence-DPIA-Addendum.md). Nessun uso cross-tenant per training autorizzato da questa specifica."""
        ),
        (
            "docs/06-Compliance/dichiarazioni-dpia.md", "## 11. Fase 4 — Clinical Intelligence (proposta 12/11/2026)",
            """## 11. Fase 4 — Clinical Intelligence (proposta 12/11/2026)

Fonte: [Progetto Fase 4](../03-Product-Roadmap/Progetti/2026-11-12-fase-4-clinical-intelligence.md) e [addendum di dettaglio](Fase-4-Clinical-Intelligence-DPIA-Addendum.md). **Valgono solo dopo eventuale sviluppo e rilascio**, previa revisione DPO. Non sono funzioni già in esercizio.

| ID | Scelta/rischio da valutare | Mitigazione progettuale | Stato |
|---|---|---|---|
| D-105 | Analisi predittiva di complicanze e richiami su dati sanitari, possibile MDSW | Definizione intended purpose, valutazione MDR, DPIA, validazione, supervisione e audit | da dichiarare |
| D-106 | Training su dati storici, possibili finalità ulteriori e dataset cross-tenant | Nessun pooling di default; verifica giuridica, responsabilità dei titolari e minimizzazione | da dichiarare |
| D-107 | Embedding/referti e retrieval semantico possono esporre dati tra pazienti | Separazione per account, filtri clinica/paziente/ruolo, audit e test di leakage | da dichiarare |
| D-108 | FHIR/HAPI potrebbe duplicare dati o ampliare le superfici di accesso | PoC con dati sintetici, rete privata e governance delle repliche | da dichiarare |
| D-109 | Richiami e supporto decisionale possono generare falsi allarmi o decisioni inique | Conferma medica, override, monitoraggio e separazione del rischio clinico dal no-show | da dichiarare |"""
        ),
    ]
    for entry in edits:
        print(append_section(root, *entry))
    print("\nCompletato. Rivedere il diff prima di commit e push:")
    print("git diff -- README.md docs/")


if __name__ == "__main__":
    main()
