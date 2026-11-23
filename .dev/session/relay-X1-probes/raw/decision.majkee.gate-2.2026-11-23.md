---
kind: operator decisions, verbatim with confirmed summaries under R1 where applicable
from: majkee, typed in the exec session (codex 01a1fefc-0356-7ea1-860c-783a66a91211)
recorded_by: exec
date: 2026-11-23
scope: relay-X1-probes, cycle 10 gate walkthrough, G0–G10
---

## G0 — Read-back of the probe packet

asked: **Is this the packet as you understand it, or is anything unclear?**

majkee:
> Its ok, understand.

status: decided

## G1 — What GO and STOP mean here

asked: **Do these meanings match yours, or would you change them?**

Context presented: Flight proposed GO as acceptance of the witnessed packet and retirement of the bed, with files preserved. STOP leaves the bed open to address what is missing. The two attempts are spent either way.

majkee:
> GO, but I prepared two different situation (approval modes), and this test did not count on approval message can happend.

status: decided

## G2 — The gate decision

asked: **On this packet, GO or STOP? If STOP, what needs to be added or corrected?**

Context presented: The packet covers the two released attempts. Approval prompts and the two further approval modes remain open as stated in G1.

majkee:
> ok, than `GO`

status: decided

## G3 — The tracker

asked: **Should the auditor stop the tracker now, stop it after your side test, or leave it running?**

majkee:
> No, I want to continue, can you poke `myShell`: `Fable 5.2 medium . ~/reposoma/.majkee . ctx 100% left . Nablarva relay ledger merge and journal . a857e21d-3f9d-4cf3-93f4-bbe9aa33ec66` by poke - she as also cluade agent can ask probe by queue or another method (poke) to call approval situation. Than I will switch to another approval mode and make another similar situation again, after that we close script with auditor, I will ask him to report anywhere else his script as same as ful log itself and than we can close sample and report back we are finished with this loop. Is it ok, for you?

status: decided

## G4 — Closing the sample

asked: **G4 — Will you close `sample-codex` yourself after the approval-mode tests and the auditor’s final capture?**

majkee:
> Yes.

status: decided

## G5 — The sample’s Codex session record

asked: **Keep the session record, or delete it after the sample closes?**

majkee:
> keep

status: decided

## G6 — A second copy of the private evidence

asked: **Keep a second private copy on `office`?**

Context presented: The stage evidence stays outside Git. The person who makes the copy can be named separately.

majkee:
> yes

status: decided

## G7 — The predecessor’s original captures in `/tmp`

asked: **Keep the originals, delete them now, or compare them with the private copy first and delete only if they match?**

majkee:
> compare , if identical tmp can be erased .

status: decided

## G8 — Returning the one-time L4 exception

asked: **Do you acknowledge that the exception is spent, or would you add anything to the record?**

majkee:
> Let as is.

status: decided

## G9 — Where the remaining work belongs

asked: **Which should we record: A, B, C, or another arrangement?**

Context presented: A hands the open work to a successor. B keeps `relay-X1-probes` open for further sample work and a second packet. C parks the work in the line ledger.

majkee:
> B, because that is taking a lot of time, create new new runbooks for small steps, I would be glad if we make more testests inside one roof-umbrella although its little not canonical, but spare time and tokens for bureocracy - this is in fact still pain (record me this time verbatim, pls).

status: decided

## G10 — Closing read-back

asked: **Is this what you decided, or is anything different?**

majkee:
> yes

confirmed summary: GO accepts the first packet as the witnessed record of two attempts. Approval prompts and other approval modes remain open. The one-time L4 exception is spent. Keep relay-X1-probes open under the same umbrella for further tests and a second packet. Keep the tracker up during the approval-mode tests. Flight routes Majkee's request to involve myShell in a separately scoped test. Majkee switches approval modes himself, asks the auditor to preserve the tracker script and full log and then stop the tracker, and closes sample-codex after the final capture. Keep its session record on home. Make a second private copy on office, with the hand still to be named. Compare the predecessor's /tmp folders against the private copies and erase the originals only if identical.

status: decided
