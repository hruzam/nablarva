---
kind: witnessed probe packet 4 — two further tries in the second sample of relay-X1-probes, for Majkee's word
by: lead (flight, pen of relay-X1-probes) · 2026-11-23 · host home
status: DRAFT 1 — written from the verdicts of cycles 23 and 24. Not yet checked by the auditor, not yet decided by Majkee.
rule: as in packet.md and packet-3.md — every row points at a file; raw captures, receipt copies and notes are private, in ~/.local/share/nablarva/custody/x1-chooser-2026-11-23/ on home. What packet-3.md says about the sample, its settings and the observer holds here too and is not repeated.
---

# What this packet is, and is not

Two further observations in the sample of the third packet, each **tried once**, on the same evening. After his GO on
the third packet Majkee invited the lead to add something before he closes the sample; the lead proposed two sends and he
released each by its own word. It gives no verdict on the relay architecture, qualifies no door, presumes no exception to
the death of send-keys injection, adopts nothing and closes no path.

# What was released, and by whom

Majkee, in the lead's window — `raw/decision.majkee.gate-4.2026-11-23.md` (the invitation) and
`raw/decision.majkee.e-series.2026-11-23.md` ("go E1"; "go E2", with his own statement of what he does at the chooser).
There was no written scope beyond the lead's proposal in its window and the two observer briefs; no second seat
challenged these two tries before they ran. Carrier `codex queue` only.

# The rows

| | **E1** — a denial at a chooser | **E2** — a second message while a chooser stands |
|---|---|---|
| What was planned | one message that asks for a receipt and for a file in a new outside folder, `denial-probe`; he counts to five at the chooser and denies | a first message that brings up a chooser (`wait-probe`); he leaves it for more than thirty seconds and then denies; meanwhile, on the observer's second marker, a second message that asks for a receipt only |
| Nonce(s) — written and committed before any call | `x1f-bbe89a2066` — 20:40:47 (4642130) | first `x1g-70415ddddd`, second `x1h-8756bbba9f` — 20:54:16 (11898ff) |
| Observer's marker — five preconditions hold, watch running, the thread named | 20:41:52.904 | 20:55:29.788 |
| State of the sample at that marker, by the observer | idle; its last turn (D1) had completed | no turn in progress; its last turn (E1) had ended as aborted |
| The call — `codex queue`, without `--resume`; one shell command of the lead that waited for the marker | 20:41:53.813 → 20:41:53.979, exit 0, message id `01a20a24-ce27-7942-9591-68c46c51f9f9` | first: 20:55:30.701 → 20:55:30.897, exit 0, message id `01a20a31-4540-7843-83ef-6970e8f57e32` · **second: NOT RUN** |
| **Carrier** | accepted | first: accepted |
| **Native turn** | started 20:41:54.783 · ended 20:42:28.219 as aborted | **none observed** — no new entry in the record, no change of the bottom rows, in 361 one-second samples from 20:55:28.790 to 21:01:42.976 |
| **Receipt** | `x1f-bbe89a2066.txt`, 20:42:01.095, hash `dad7b7a646d7…` | none |
| **Nonce the observer saw arrive** — it was told none | `x1f-bbe89a2066` — matches | none |
| **Leave asked** | yes, 20:42:04.586 | no |
| **A chooser for the human** | yes, in the observer's samples: first 20:42:05.443, last 20:42:27.193 — 22 consecutive one-second samples, unchanged; the same three choices as in D1 | none in any sample; the observer's second marker was therefore never written |
| **The answer** | a denial, inferred by the observer from the outcome; by his own later statement he pressed `esc`. No seat observed the key | — |
| **What the turn did with it** | the tool result at 20:42:28.199 says the command was aborted by the user after 23.6 seconds; the turn ended 20 ms later as aborted, reason "interrupted". No closing message, no retry, no later turn within the watch | — |
| **Outside the folder** | `denial-probe` absent at baseline and at the end | `wait-probe` absent at baseline and at the end |
| **The rules file** | modification time unchanged | unchanged |
| **Result** | complete: carrier, turn, receipt with the matching nonce, the observer's confirmation | **UNCERTAIN** — accepted by the carrier, no native delivery observed within the watch; lost or still pending is not known. **The second send, the one the try was for, is NOT RUN** |
| Watch | 301 rows, 20:41:51.907–20:47:02.724 | 361 rows, 20:55:28.790–21:01:42.976 |
| Where | `_bus/23.lead.verdict.md` | `_bus/24.lead.verdict.md` |

All times UTC, 2026-11-23. Neither send was retried, and nothing was sent after the uncertain result. Versions as in the
third packet.

# What the two tries showed — observations of one try each, not results

1. **E1: the stored rule of D1 did not cover a command for a different folder** — a chooser appeared.
2. **E1: the denial ended the whole turn.** The record names it: a tool result that says aborted by the user, and a
   turn-aborted event. The sample wrote no closing message.
3. **E2: a message that the carrier accepted was not seen to arrive.** D1 and E1 had each arrived about a second after
   the call.
4. **The one difference the lead can name between E2 and the two that arrived:** the sample's last turn had been
   aborted, not completed. Whether that is the reason, one try cannot say.

# What this packet does not show

- **What happens to a message that arrives while a chooser stands.** That was E2's question; the try never reached it.
- Why the first message of E2 did not arrive, and whether it is lost or will arrive later.
- Whether a turn that ended as aborted holds back the carrier's messages — the candidate reading, untested.
- What "No" does when a note to the program is typed with it; whether another denial behaves the same.
- Whose hand pressed which key in E1 — no seat observed it; his statement says `esc`.
- Reliability, another sender, another version; independence beyond two seats — as before.

# How these two tries differ from the earlier ones — the lead's own account

- They had no written scope and no challenge. The lead proposed them in its window and he released them there.
- **E2 ran in a sample that E1 had changed.** The two tries are not two tries under one condition.
- The observer's precondition "idle" did not separate "last turn completed" from "last turn aborted".

# Evidence

- **In the repository:** `_bus/23.*` and `_bus/24.*` (briefs, markers, try files, RETURNs, verdicts),
  `raw/decision.majkee.gate-4.2026-11-23.md`, `raw/decision.majkee.e-series.2026-11-23.md`, `raw/pokes.log.md` (p36,
  p37).
- **Private, on home:** `~/.local/share/nablarva/custody/x1-chooser-2026-11-23/` — the observer's `c23.*` and `c24.*`,
  the lead's call outputs `c23.lead.call.out` and `c24.lead.call1.out`. There is no output of a second call.
- **Originals:** two receipts more in the sample's `receipts/` — three in all with D1's.

# Left behind

- **A message that the carrier accepted and that was not seen to arrive** — thread `01a209ec…`, message id
  `01a20a31-4540-7843-83ef-6970e8f57e32`. If it arrives later it asks the sample for a receipt named after
  `x1g-70415ddddd` and for the folder `wait-probe`. He is told.
- The sample is still up and a tracker runs on it — both his to close.

# What his word on this packet would and would not mean — the lead's proposal

- **GO** — he accepts this packet as the witnessed record of these two tries, beside the first three: E1 complete, E2
  uncertain in its first send and not run in its second. It adopts and qualifies nothing and authorizes no further
  test.
- **STOP** — he does not accept it as it is and says what is missing or wrong.

# Still owed when this was written — acts, not results

1. The sample closed and the tracker stopped, its script and log handed over — his own acts with the auditor.
2. A copy of the private folder to office and its pointer in the line ledger — the controller, on a POINT of the lead,
   after the tracker has stopped.
