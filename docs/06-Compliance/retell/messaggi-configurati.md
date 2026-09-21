# Messaggi configurati su Retell — Giulia REL 1.0

**Agente:** DentalCare Giulia Agent · `agent_14cb1240b7296e87a6718d7d11`
**Ambiente:** preproduzione · **Rilevato il:** 28/07/2026 16:13

> **Perché questo file esiste.** I testi che il paziente sente vivono nei **campi messaggio della
> console Retell**, non in un file del repository. Lo screenshot li fotografa ma li tronca. Senza
> una trascrizione, il repository non può dimostrare *cosa* fosse configurato in una certa data —
> ed è esattamente ciò che l'art. 50 chiede di poter provare.
>
> ⚠️ **Stato: da confermare.** Le parti marcate sono ricostruite, non lette per intero. Vanno
> verificate parola per parola sulla console prima di valere come evidenza.

---

## 1. Welcome Message (primo turno, «AI speaks first»)

**Modalità configurata:** `AI speaks first` → `Custom message`

Testo visibile nello screenshot, **troncato dal campo**:

> Buongiorno, sono Giulia, l'assistente virtuale basata su intelligenza artificiale di questo
> studio. Posso aiutarla con appuntamenti e informazioni amministra**[…]**

Continuazione **da confermare**. Il testo prescritto dalla direttiva originale era:

> […] e informazioni amministrative.
> In qualsiasi momento può chiedere di parlare con un operatore umano.

⚠️ **Da verificare sulla console:** se la frase sull'operatore umano sia effettivamente presente
nel Welcome Message. È il secondo requisito dell'art. 50 — sapere di parlare con un'IA e poter
chiedere un umano — e se manca qui deve stare da un'altra parte, dichiarata.

## 2. Clausola di identità nel system prompt

Verificata sullo screenshot, §20 *Regole vincolanti*, righe 1-2 — **leggibile per intero**:

> - dichiara di essere una segreteria virtuale basata sull'intelligenza artificiale
> - se il paziente chiede esplicitamente se sei un essere umano, rispondi sempre chiaramente che
>   sei un sistema basato sull'intelligenza artificiale — senza eccezioni (EU AI Act art. 50)

Testo completo del prompt: [`system-prompt-REL1.0-2026-07-28.md`](system-prompt-REL1.0-2026-07-28.md).

---

## Da fare

| | Azione | Perché |
|---|---|---|
| 1 | Confermare il Welcome Message **per esteso** e sostituire qui il testo troncato | Senza, l'evidenza #2 resta parziale |
| 2 | Screenshot del **solo campo** Welcome Message, non tagliato | L'attuale mostra il campo ma lo tronca |
| 3 | Verificare che l'escalation a operatore umano sia dichiarata da qualche parte | Secondo requisito dell'art. 50 |
| 4 | Rifare questa trascrizione **a ogni modifica** dei messaggi su Retell | Il testo autorevole sta in un servizio esterno: il repository diverge in silenzio |

> **Il rischio strutturale.** La configurazione autorevole vive in una console SaaS, il repository
> ne conserva una copia. Le due divergono appena qualcuno modifica l'una senza aggiornare l'altra,
> e **nessuno se ne accorge** — è lo stesso difetto che in #59 rendeva falsa l'etichetta
> «Appuntamento fissato». La procedura in
> [`directives/procedura-aggiornamento-giulia-retell.md`](../../../directives/procedura-aggiornamento-giulia-retell.md)
> esiste per questo: va seguita, o la copia non vale nulla.
