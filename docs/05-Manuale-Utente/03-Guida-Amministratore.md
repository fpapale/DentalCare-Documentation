# 03 — Guida Amministratore (titolare / responsabile studio)

Guida per l'amministratore dello studio: visione d'insieme, configurazioni,
listino prestazioni e gestione dell'AI. L'admin ha accesso a **quasi tutte** le
funzioni operative più le **Impostazioni**, ma **non** al Copilot conversazionale
(pensato per chi lavora su pazienti/agenda).

**▶️ Account demo:** `admin@demo.dentalcare.it` — password demo fornita
dall'amministratore (Admin Demo). In alternativa `demo@demo.dentalcare.it`
(Demo Tutto), identico per permessi.

---

## 0. Accesso e ruolo

1. Vai su `https://paaplef.duckdns.org:8181`.
2. Accedi con `admin@demo.dentalcare.it` e la password demo (fornita
   dall'amministratore).
3. Arrivi alla **Dashboard** con i KPI dello studio.

> **`admin` vs `tenant_admin`:** l'account demo è **admin** (amministratore dello
> studio). Le funzioni di piattaforma multi-studio (**Admin Tenant**) richiedono
> il ruolo `tenant_admin`, non presente negli account demo → quella voce non è
> accessibile in demo. Vedi §6.

---

## 1. Dashboard

**Percorso** → **Dashboard**

Colpo d'occhio sullo studio: appuntamenti del giorno, richiami in scadenza,
indicatori economici e operativi. È la home per capire "come sta andando" prima
di entrare nei singoli moduli.

---

## 2. Impostazioni dello studio

**Percorso** → **Impostazioni** *(solo amministratore)*

Centro di configurazione. A seconda della build trovi:

- **Dati dello studio** (ragione sociale, contatti, dati per la fatturazione).
- **Utenti/medici** dello studio e loro ruoli.
- **Parametri operativi** (agenda, poltrone, orari) se abilitati.
- **Sezione AI** → **Prompt Manager** (vedi §4).

1. Apri **Impostazioni**.
2. Modifica la sezione desiderata.
3. Salva: le modifiche valgono per tutto lo studio (tenant).

**▶️ Prova nel demo:** apri **Impostazioni** e scorri le sezioni disponibili.

---

## 3. Listino prestazioni

**Percorso** → **Prestazioni**

Il listino alimenta piani di cura, preventivi e fatture. Tenerlo aggiornato è
compito chiave dell'amministratore.

1. Apri **Prestazioni**.
2. Aggiungi/modifica una voce: **nome**, **prezzo**, **categoria**, eventuali
   **default** e **bundle** (pacchetti).
3. Salva: le nuove voci sono subito disponibili per medici e segreteria.

> Prezzi coerenti = preventivi e fatture coerenti. Rivedi il listino
> periodicamente.

**▶️ Prova nel demo:** apri **Prestazioni**, modifica il prezzo di una voce e
verifica l'aggiornamento.

---

## 4. Prompt Manager AI

**Percorso** → **Impostazioni → sezione AI (Prompt)**

I comportamenti del Copilot AI sono guidati da **prompt** editabili dall'admin,
con possibilità di **override per studio** (tenant).

1. Apri la sezione **AI / Prompt** nelle Impostazioni.
2. Seleziona il prompt da personalizzare.
3. Modifica il testo. Sono disponibili **segnaposto dinamici** (es. `{{oggi}}`,
   `{{ora}}`) che vengono sostituiti a runtime.
4. Salva: il Copilot userà la versione personalizzata per lo studio.

> Personalizzare i prompt permette di adattare tono e regole dell'assistente allo
> studio senza toccare il codice.

---

## 5. Supervisione operativa

L'amministratore può entrare in tutti i moduli operativi per controllo e
correzione:

| Modulo | Uso tipico dell'admin |
|--------|-----------------------|
| **Agenda** | Verifica carico poltrone, riorganizza |
| **Pazienti** | Consulta anagrafiche, apre schede (crea anche nuovi pazienti) |
| **Cartella clinica** | Controllo clinico-amministrativo |
| **Preventivi** | Monitoraggio conversione (inviati → accettati) |
| **Fatturazione** | Controllo incassato / da incassare |
| **Richiami** | Verifica copertura dei controlli periodici |
| **Magazzino** | Controllo scorte e riordini |

> A differenza della segreteria, l'admin **può** creare pazienti e accedere alla
> cartella clinica; a differenza del medico, **non** ha il Copilot
> conversazionale.

---

## 6. Multi-studio (Admin Tenant) — nota

**Percorso** → **Admin Tenant** *(richiede ruolo `tenant_admin`)*

La gestione a livello di **piattaforma** (creazione/gestione studi, configurazioni
cross-studio) è riservata al ruolo `tenant_admin`. Gli account demo sono `admin`
(studio), quindi **questa sezione non è provabile in demo**. In un ambiente reale
con un `tenant_admin` si accede a:

- provisioning di nuovi studi (tenant);
- configurazioni globali di piattaforma;
- funzioni amministrative sovra-studio.

---

## 7. Sicurezza e privacy (cosa deve sapere l'admin)

- **Dati cifrati a riposo:** data di nascita e codice fiscale dei pazienti sono
  **cifrati** nel database (GDPR art. 32). Nell'app restano leggibili.
- **Ruoli lato server:** i permessi sono verificati dal backend, non solo
  nascondendo voci di menu. Un ruolo non abilitato non può accedere via URL.
- **Fatture inalienabili:** i documenti fiscali non si cancellano con il paziente
  (obbligo di conservazione).
- **Account demo:** `demo@demo` ("Demo Tutto") è l'account vetrina con login
  facilitato; `admin@demo` è l'amministratore "standard". Stessi permessi.

Dettagli tecnici nell'handbook: `04-Architecture-Handbook/07-Security.md` e
`11-Data-Encryption.md`.

---

## Riepilogo attività (Amministratore)

1. **Dashboard** → stato generale dello studio.
2. **Impostazioni** → dati studio, utenti, parametri.
3. **Prestazioni** → listino aggiornato.
4. **Impostazioni → AI/Prompt** → personalizza il Copilot.
5. **Preventivi / Fatturazione** → monitora la parte economica.
6. **Richiami / Magazzino** → controllo copertura e scorte.
