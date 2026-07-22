# 04b — Ranking Competitor (ricerca web, luglio 2026)

**Versione:** 1.0 · **Data snapshot:** 2026-07-22 · **Stato:** fotografia di mercato a un istante (point-in-time).

> Companion operativo di [04-Competitor](04-Competitor.md) (narrativa/SWOT). Questo file riporta l'esito di una **ricerca web strutturata** con classificazione per importanza. I dati di traction sono **dichiarati dai vendor** (siti/PR/review), non auditati — vedi §7 caveat.

## 1. Metodo

Pipeline a due stadi:

1. **Ricerca** — tre agenti web in parallelo, per segmento: (a) gestionali odontoiatrici italiani, (b) PMS cloud internazionali, (c) AI-native dentistry (radiologia AI + receptionist vocale AI). 37 prodotti trovati, ognuno con fonte reale verificata.
2. **Scoring esperto** — consolidamento + deduplica (37→36) + punteggio importanza/minaccia per DentalCare Pro.

**Rubrica score (0-100):**

| Componente | Peso | Criterio |
|---|---|---|
| **Prossimità mercato** | 40% | già in Italia = 90-100 · EU/EU-adjacent (UK/IE/FR/ES/DE) = 55-80 · solo US/altro = 15-45 |
| **Overlap feature** | 35% | match del bundle DentalCare Pro (PMS cloud + Copilot + segretaria vocale + radiologia AI). Full gestionale + più AI = 80-100 · forte su un asse AI = 45-75 · adiacente/parziale = 15-45 |
| **Traction/forza** | 25% | funding, n° studi, ownership/parent, quota. Grande/ben finanziato/incumbent = 70-100 · medio = 40-70 · early = 10-40 |

`score = 0.40·prossimità + 0.35·overlap + 0.25·traction`

**Tier:** Critical ≥75 · High 60-74 · Medium 45-59 · Low <45.

## 2. Lettura esecutiva

Le minacce **reali e in Italia oggi** sono gli **incumbent domestici**, non le AI-startup USA:

- **XDENT/CGM (93)** è il più pericoloso: già oggi spedisce una segretaria vocale AI (AIDA), dettatura (SPEAKY) e imaging AI a 8.000+ dentisti italiani — rispecchia l'intera tesi di DentalCare Pro.
- **Docplanner/Gipo (90)** e **OrisDent/Henry Schein One (87)** abbinano gestionale completo a muscolo distributivo (funnel MioDottore; reach globale HS One) che DentalCare Pro non ha.
- **Alfadocs (83)** è l'insurgent cloud-native con AI-scribe nella stessa identica corsia.

Sull'asse AI, la minaccia singola più affilata è **Pearl (80)**: radiologia **CE-marcata, vendibile in Italia oggi**, mentre il modulo radiologia di DentalCare Pro è congelato pre-CE. **Diagnocat** e la francese **Allisone** sono i successivi entranti radiologia EU-credibili.

I benchmark USA (Curve, Archy, Denti.AI, CareStack, Arini) mostrano dove va il mercato ma la **geografia** (prossimità 25-40) li tiene fuori dal board a breve — finché uno non si internazionalizza.

**Due pattern strategici:**
- **Accerchiamento Henry Schein One:** possiede OrisDent (IT) + Dentally (UK) + Dentrix Ascend (US). Un'estensione EU di Dentally è a una decisione corporate di distanza.
- **Corsia vocale EU aperta:** nessun receptionist vocale AI ha presenza IT/EU confermata (i più vicini sono Aerona-NI, Allisone-FR voice). Giulia ha una lane relativamente libera sul lato voce — al contrario del lato radiologia, già presidiato CE.

## 3. Scoreboard (36, ordinati per score)

Sub-score: **P**=prossimità · **O**=overlap · **T**=traction.

| # | Competitor | Score | Tier | Segmento | P | O | T | Fonte |
|---|---|:---:|---|---|:--:|:--:|:--:|---|
| 1 | XDENT (CompuGroup / CGM) | 93 | 🔴 Critical | IT PMS | 98 | 88 | 90 | [xdent.it](https://www.xdent.it/) |
| 2 | GipoDental/GipoNext (Docplanner+MioDottore) | 90 | 🔴 Critical | IT PMS | 98 | 78 | 95 | [gipo.it](https://gipo.it/it/prodotto/il-software/gipodental) |
| 3 | OrisDent Air (OrisLine, Henry Schein One) | 87 | 🔴 Critical | IT PMS | 96 | 75 | 88 | [orisline.com](https://orisline.com/it/gestionale-per-dentisti-in-cloud/) |
| 4 | Alfadocs | 83 | 🔴 Critical | IT PMS | 96 | 76 | 70 | [alfadocs.com](https://www.alfadocs.com/it/) |
| 5 | Pearl (Second Opinion) | 80 | 🔴 Critical | AI radiologia | 82 | 72 | 88 | [hellopearl.com](https://hellopearl.com/products/second-opinion) |
| 6 | Windent (Zucchetti) | 79 | 🔴 Critical | IT PMS | 95 | 55 | 88 | [zucchetti.it](https://www.zucchetti.it/it/cms/settori/sanita/dipartimentali-diagnostica/gestione-studi-dentistici/gestione-studi-dentistici-descrizione.html) |
| 7 | UNO (Dental Trey) | 75 | 🔴 Critical | IT PMS | 94 | 50 | 78 | [dentaltrey-uno.it](https://www.dentaltrey-uno.it/) |
| 8 | Dentally | 73 | 🟠 High | Intl cloud PMS | 65 | 80 | 75 | [dentally.com](https://www.dentally.com/en-gb/) |
| 9 | MedicHub | 73 | 🟠 High | IT PMS | 94 | 68 | 45 | [medichub.it](https://www.medichub.it/gestionale-odontoiatrico) |
| 10 | Doctolib (Italia / Pro) | 72 | 🟠 High | Booking | 90 | 40 | 88 | [doctolib.it](https://www.doctolib.it/) |
| 11 | MIND (ANDI) | 71 | 🟠 High | IT PMS | 95 | 58 | 50 | [andi.it](https://mindgestionaleodontoiatrico.andi.it/) |
| 12 | Diagnocat | 70 | 🟠 High | AI radiologia | 72 | 70 | 65 | [diagnocat.com](https://diagnocat.com/us) |
| 13 | Allisone AI | 68 | 🟠 High | AI radiologia | 75 | 74 | 50 | [allisone.ai](https://en.allisone.ai/produit) |
| 14 | CareStack | 67 | 🟠 High | Intl cloud PMS | 55 | 76 | 72 | [carestack.com](https://carestack.com/) |
| 15 | Aerona | 62 | 🟠 High | Intl cloud PMS | 68 | 72 | 40 | [aerona.com](https://aerona.com/cloud-dental-practice-management-software-for-uk-eu-global-practices/) |
| 16 | DentalOpera | 61 | 🟠 High | IT PMS | 92 | 48 | 30 | [dentalopera.it](https://www.dentalopera.it/) |
| 17 | Curve Dental | 60 | 🟠 High | Intl cloud PMS | 30 | 80 | 80 | [curvedental.com](https://www.curvedental.com/) |
| 18 | Open Kanino | 60 | 🟠 High | IT PMS | 92 | 48 | 25 | [openkanino.it](https://www.openkanino.it/) |
| 19 | Overjet | 59 | 🟡 Medium | AI radiologia | 40 | 70 | 75 | [overjet.com](https://www.overjet.com/) |
| 20 | VideaHealth | 59 | 🟡 Medium | AI radiologia | 35 | 72 | 78 | [videa.ai](https://videa.ai/) |
| 21 | Denti.AI | 58 | 🟡 Medium | AI radiologia | 35 | 82 | 60 | [denti.ai](https://www.denti.ai/) |
| 22 | Dentrix Ascend | 56 | 🟡 Medium | Intl cloud PMS | 28 | 70 | 82 | [dentrixascend.com](https://www.dentrixascend.com/) |
| 23 | Denticon (Planet DDS) | 56 | 🟡 Medium | Intl cloud PMS | 28 | 72 | 78 | [planetdds.com](https://www.planetdds.com/denticon/) |
| 24 | tab32 | 54 | 🟡 Medium | Intl cloud PMS | 30 | 80 | 55 | [tab32.com](https://tab32.com/) |
| 25 | Archy | 53 | 🟡 Medium | Intl cloud PMS | 28 | 76 | 62 | [archy.com](https://www.archy.com/) |
| 26 | Oryx Dental | 53 | 🟡 Medium | Intl cloud PMS | 28 | 76 | 60 | [oryxdental.com](https://www.oryxdental.com/) |
| 27 | Arini | 47 | 🟡 Medium | AI voice | 30 | 68 | 45 | [arini.ai](https://www.arini.ai/) |
| 28 | Simplifeye | 46 | 🟡 Medium | AI voice | 35 | 48 | 60 | [prnewswire](https://www.prnewswire.com/news-releases/simplifeye-expands-technology-suite-for-retail-healthcare-practices-301336696.html) |
| 29 | NexHealth | 46 | 🟡 Medium | Booking | 28 | 38 | 85 | [nexhealth.com](https://www.nexhealth.com/) |
| 30 | Cloud 9 Ortho (Planet DDS) | 42 | ⚪ Low | Intl cloud PMS | 25 | 45 | 65 | [planetdds.com](https://www.planetdds.com/cloud9/) |
| 31 | Eaglesoft | 40 | ⚪ Low | Intl cloud PMS | 22 | 30 | 82 | [softwareadvice](https://www.softwareadvice.com/medical/patterson-dental-eaglesoft-profile/) |
| 32 | Voiceoc | 40 | ⚪ Low | AI voice | 28 | 60 | 30 | [voiceoc.com](https://www.voiceoc.com/voice-ai) |
| 33 | Open Dental | 39 | ⚪ Low | Intl cloud PMS | 25 | 42 | 58 | [opendental.com](https://www.opendental.com/) |
| 34 | Peerlogic (Aimee) | 39 | ⚪ Low | AI voice | 28 | 58 | 30 | [peerlogic.com](https://www.peerlogic.com/dental) |
| 35 | Newton | 38 | ⚪ Low | AI voice | 25 | 60 | 28 | [ycombinator](https://www.ycombinator.com/companies/newton) |
| 36 | Annie AI (NowBookable) | 37 | ⚪ Low | AI voice | 25 | 60 | 25 | [nowbookable.com](https://nowbookable.com/annie_ai) |

## 4. Perché contano (per tier)

### 🔴 Critical (≥75)
- **XDENT (CGM):** gestionale IT cloud/desktop, 8.000+ dentisti. AIDA (segretaria vocale AI), SPEAKY (dettatura), imaging AI via Dürr Dental. Match 1:1 dell'intero stack, gruppo health-IT pan-europeo (~30.000 clienti IT). Minaccia incumbent più completa sul terreno di casa.
- **GipoDental/GipoNext (Docplanner):** gestionale cloud + marketplace MioDottore (~11M visite/mese IT) + AI note "Noa". Funnel acquisizione pazienti che DentalCare Pro non può eguagliare, sotto il più grande gruppo booking sanitario al mondo.
- **OrisDent Air (Henry Schein One):** brand storico IT, cloud, Sistema TS/GDPR, firma elettronica, AI "dentIA". Parent HS One possiede anche Dentally e Dentrix — il gruppo più "accerchiante".
- **Alfadocs:** gestionale cloud-native IT, 11.000+ professionisti, AI "Scribe" (trascrizione ambientale) + "Sintesi IA". Overlappa quasi identico le ambizioni Copilot.
- **Pearl (Second Opinion):** prima radiologia AI dentale **CE-marcata**, sito EU, 23.000+ studi. Vende oggi in Italia ciò che la radiologia di DentalCare Pro (pre-CE) non può.
- **Windent (Zucchetti):** gestionale completo, 5.000+ studi, 70+ integrazioni imaging, **niente AI**. Incumbent legacy da spiazzare, vulnerabile sull'asse AI.
- **UNO (Dental Trey):** ~8.000 professionisti, forte su magazzino e catene, niente AI. Canale distributore + base installata. *(borderline Critical/High, raw 74.6)*

### 🟠 High (60-74)
- **Dentally:** cloud AI PMS UK/IE, note AI + imaging AI, Henry Schein One. Reach corporate = rischio estensione IT.
- **MedicHub:** gestionale cloud IT, AI "Molarìx" (comandi vocali IT), da 79€/mese. Stesso segmento del piano Essential. *(traction non verificata)*
- **Doctolib:** marketplace booking pan-EU, directory dentisti IT + Doctolib Pro. Compete sul layer prenotazione/reminder che serve Giulia.
- **MIND (ANDI):** gestionale distribuito dall'associazione dentisti IT, sconto soci. Canale fiducia difficile da replicare.
- **Diagnocat:** radiologia AI CBCT/3D, FDA + CE, siti EU. Profondità 3D oltre lo scope DentalCare Pro; footprint EU.
- **Allisone:** AI dentale francese **CE Classe IIa** + voice assistant, cloud HDS/MDR/GDPR. Già nel regime regolatorio non superato dalla radiologia DentalCare Pro.
- **CareStack:** cloud all-in-one US/UK/AU, "VoiceStack" (voce AI 24/7 ≈ Giulia), ~$145M. Global player meglio finanziato con presenza EU-adjacent.
- **Aerona:** PMS cloud Nord Irlanda, marketing UK/EU, "RoboReception" (voce AI ≈ Giulia). Prova che il concetto Giulia si vende già in Europa.
- **DentalOpera:** gestionale cloud made-in-IT (2017), da ~88€, no AI. Stesso core, stesso paese, piccolo.
- **Curve Dental:** cloud US #1, imaging AI + Ambient AI, 80.000+ prof. Analogo funzionale, solo-US.
- **Open Kanino:** cloud IT low-cost (free fino 100 pazienti, da ~29€), no AI. Caccia gli switcher price-sensitive.

### 🟡 Medium (45-59) — benchmark di categoria, geografia lontana
- **Overjet / VideaHealth:** radiologia AI FDA leader USA, no CE/EU. **Denti.AI:** unico su **entrambi** i pilastri AI (Detect FDA + AI Receptionist ≈ Giulia), US/Canada. **Dentrix Ascend / Denticon / tab32 / Archy / Oryx:** cloud+AI USA, solo-US. **Arini:** receptionist vocale AI (YC), analogo funzionale più vicino a Giulia, US/Canada. **Simplifeye / NexHealth:** layer engagement/booking USA.

### ⚪ Low (<45) — overlap minimo o geografia/architettura sbagliata
- **Cloud 9 Ortho** (ortho, NA) · **Eaglesoft** (legacy desktop US) · **Open Dental** (open-source self-hosted US) · **Voiceoc / Peerlogic / Newton / Annie AI** (voce AI US, early/analytics).

## 5. Deep-dive: i 4 critici italiani vs DentalCare Pro

| | Ha che DentalCare Pro NON ha | DentalCare Pro ha che loro NON hanno | Takeaway |
|---|---|---|---|
| **XDENT (CGM)** | Segretaria vocale AI (AIDA) e dettatura (SPEAKY) **in produzione**; 8.000 dentisti; gruppo pan-EU | Radiologia AI proprietaria (YOLO) su panoramiche; odontogramma con provenienza Aic; stack più integrato/moderno | È lo scenario "già arrivato": non differenzi sull'*esistenza* dell'AI vocale, ma su qualità/prezzo/integrazione. La radiologia AI è l'unico asse dove sei avanti — ma è congelata pre-CE. |
| **GipoDental (Docplanner)** | Funnel acquisizione pazienti (MioDottore, ~11M visite/mese); scala e capitale | Segretaria vocale outbound/inbound (Giulia); radiologia AI; controllo verticale dello stack | Non li batti sull'acquisizione. Differenzia su automazione clinica + voce, non su marketing/lead. |
| **OrisDent (Henry Schein One)** | Profondità compliance (Sistema TS, firma), brand storico, backing multinazionale | AI-native trasversale (Copilot in ogni processo), voce, radiologia | Rischio = reach del parent (Dentally pronto per l'EU). Velocità AI è il tuo vantaggio; la compliance loro è il tuo gap da chiudere (audit trail, cap. 13). |
| **Alfadocs** | AI "Scribe" ambientale già live; 11.000 professionisti; cloud-first IT maturo | Segretaria vocale telefonica (loro fanno scribe, non voice inbound); radiologia AI | Il concorrente più simile per DNA. La voce telefonica (Giulia) e la radiologia sono i due assi dove hai qualcosa che loro non mostrano. |

## 6. Implicazioni strategiche

1. **La radiologia AI è il tuo asset più difendibile ma bloccato:** è l'unico asse dove batti gli incumbent IT — ma Pearl (CE) la vende in Italia mentre tu no. Il gate **MDR/CE (Fase 2)** non è solo compliance: è ciò che sblocca il tuo unico vantaggio radiologia. Priorità competitiva, non solo regolatoria.
2. **La voce (Giulia) ha una lane EU aperta:** nessun receptionist vocale AI ha presenza IT confermata. Finestra da occupare prima che Aerona/Allisone/CareStack arrivino.
3. **Non competere su acquisizione pazienti** (Docplanner/Doctolib vincono). Competi su automazione clinica + voce inbound + integrazione.
4. **Chiudi il gap compliance** (audit trail, finalizzazione, consensi — Release 1.x): è ciò che gli incumbent storici (OrisDent, Windent) hanno e tu no; è il prezzo d'ingresso per gli studi strutturati.
5. **Sorveglia Henry Schein One:** un'estensione IT di Dentally cambierebbe il board da "incumbent locali lenti sull'AI" a "multinazionale con cloud+AI pronto".

## 7. Caveat qualità dati

- **Traction gonfiata/non verificata:** MedicHub ("migliaia di dentisti"), MIND/ANDI (contatore adozione = placeholder vuoto), Docplanner (240k professionisti / 9M booking da snippet secondari). Scorati conservativi sulla traction.
- **Regolatorio da verificare:** CE di Diagnocat da letteratura terza (non da sito ufficiale); Overjet **senza** CE confermato, "Voice AI Suite" nuova/immatura — non sovrappesare come minaccia EU.
- **Fonti deboli/datate:** Simplifeye (PR 2021, prodotto rinominato); Eaglesoft (aggregatore SoftwareAdvice); traction Peerlogic/Voiceoc/Annie/Arini solo case-study o self-reported.
- **Tier soft ai confini:** UNO (74.6→Critical) e Open Kanino (59.9→High), spinti su dalla prossimità IT nonostante l'assenza di AI.
- **Copertura:** nessun competitor confermato *operante in Italia* tra gli internazionali (i più vicini UK/IE/FR). Non coperti in questa passata: player continentali (FR "Julie", ES "Logosw"), Weave, Modento, iDentalSoft — candidati per un secondo giro EU-native.

---

## Riferimenti

- [04-Competitor](04-Competitor.md) — narrativa/SWOT competitiva · [05-SWOT](05-SWOT.md) · [03-Analisi-Mercato](03-Analisi-Mercato.md)
- [Business Plan → 03-Market-Strategy](../02-Business-Plan/03-Market-Strategy.md)
- Snapshot generato via ricerca web strutturata (3 agenti ricerca + scoring esperto), 2026-07-22. Dati traction dichiarati dai vendor, non auditati.
