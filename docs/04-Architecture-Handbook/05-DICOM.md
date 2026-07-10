# 05 — DICOM (Imaging)

## Stato attuale: NON implementato (roadmap)

Il supporto **DICOM nativo** non è ancora presente nella piattaforma. Questa
sezione documenta lo stato reale e la direzione pianificata, per evitare
disallineamenti tra documentazione e codice.

## 1. Cosa c'è oggi

- L'analisi radiologica AI (vedi [04-AI](04-AI.md)) opera su **immagini in
  formato standard** (JPG/PNG) caricate come documenti paziente su MinIO.
- I risultati (numerazione FDI, patologie) vengono riconciliati con
  l'odontogramma del paziente.
- Nessun parsing di file `.dcm`, nessun tag DICOM, nessuna integrazione PACS.

## 2. Cosa manca (per il supporto DICOM)

- Ingest di file DICOM (`.dcm`): parsing header/tag, estrazione pixel data.
- Gestione metadati DICOM (studio, serie, istanza; anagrafica paziente nei tag).
- Viewer DICOM lato frontend (finestratura, misure, MPR per CBCT).
- Eventuale interoperabilità PACS / DICOMweb (WADO/QIDO/STOW).
- Conversione DICOM → immagine per il pipeline AI esistente.

## 3. Note di progettazione (quando verrà affrontato)

- Gli asset DICOM, essendo grandi, andranno su MinIO con naming per-tenant
  coerente con l'attuale gestione documenti.
- I metadati paziente presenti nei tag DICOM sono dati personali: rientrano
  nella strategia di cifratura/minimizzazione GDPR (vedi [07-Security](07-Security.md)).
- L'inferenza AI resterebbe nel servizio Python, aggiungendo uno step di
  decodifica DICOM a monte.

> Riferimento roadmap: elemento **#8 (DICOM)** — pianificato, non schedulato in
> una release corrente.
