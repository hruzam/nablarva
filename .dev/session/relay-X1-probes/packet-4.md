---
kind: witnessed probe packet 4 — three further tries in the chooser samples of relay-X1-probes, for Majkee's word
by: lead (flight, pen of relay-X1-probes) · 2026-11-23 · host home
status: DRAFT 2 — written from the verdicts of cycles 23, 24 and 26. Draft 1 (rows E1 and E2) was never checked: its check was held when Majkee asked for the try again. Not yet checked by the auditor, not yet decided by Majkee.
rule: as in packet.md and packet-3.md — every row points at a file; raw captures, receipt copies and notes are private, in ~/.local/share/nablarva/custody/x1-chooser-2026-11-23/ on home. What packet-3.md says about the second sample, its settings and the observer holds here too and is not repeated.
---

# What this packet is, and is not

Three further observations on the evening of the third packet, each **tried once**. After his GO on the third packet
Majkee invited the lead to add something before he closes the sample; the lead proposed two sends and he released each
by its own word; when the second did not reach its question he asked for it again, and released that too. It gives no
verdict on the relay architecture, qualifies no door, presumes no exception to the death of send-keys injection, adopts
nothing and closes no path.

# What was released, and by whom

Majkee, in the lead's window — `raw/decision.majkee.gate-4.2026-11-23.md` (the invitation) and
`raw/decision.majkee.e-series.2026-11-23.md`: "go E1"; "go E2", with his own statement of what he does at the chooser;
his request to start again; "go E3". There was no written scope beyond the lead's proposals in its window and the
observer briefs; no second seat challenged these tries before they ran. Carrier `codex queue` only.

# The samples

- **E1 and E2:** the second sample — the session of the third packet (pane `%73`, thread `01a209ec…`).
- **E3:** a fresh third sample — folder `~/.cache/nablarva/relay-x1-samples/2026-11-23/sample-codex-2`, window
  `sample-codex-2`, pane `%74`, thread `01a20a3c-575a-7e11-a902-512db96dcaa3`; the same flags, the standing
  instruction as its first prompt. Started by Majkee, by his go; the lead saw in tmux metadata that the pane runs the
  prepared script; no seat observed the hand. The observer's pre-check before any send
  (`_bus/26.auditor.precheck.md`): workspace-write, on-request, reviewer user; its first and only turn completed at
  21:07:42.840; idle.

# Rows E1 and E2 — the second sample

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
| **Result** | complete: carrier, turn, receipt with the matching nonce, the observer's confirmation | **UNCERTAIN** — accepted by the carrier, no native delivery observed within the watch; lost or still pending is not known. **The second send is NOT RUN.** His own account agrees: he saw nothing happen at the sample |
| Watch | 301 rows, 20:41:51.907–20:47:02.724 | 361 rows, 20:55:28.790–21:01:42.976 |
| Where | `_bus/23.lead.verdict.md` | `_bus/24.lead.verdict.md` |

# Row E3 — the third sample: E2's question, asked anew

| | **E3** — a second message while a chooser stands |
|---|---|
| What was planned | as E2, outside folder `hold-probe`; he leaves the chooser for more than thirty seconds, then `esc` |
| Nonces — written and committed before any call | first `x1j-dd1c2d0c97`, second `x1k-fe1e8c5f92` — 21:11:53 (f80e4d2) |
| State of the sample before the first call, by the observer | idle; its last turn — its first and only — had completed at 21:07:42.840 |
| Marker 1 — five preconditions hold, watch running, the thread named | 21:12:35.442 |
| **First call** | 21:12:36.102 → 21:12:36.276, exit 0, message id `01a20a40-eaa2-7602-9a53-b635346da94e` — **carrier: accepted** |
| First message: native turn | started 21:12:44.898 · arrival 21:12:45.136 · nonce seen `x1j-dd1c2d0c97` — matches |
| First message: receipt | `x1j-dd1c2d0c97.txt` — first listed 21:12:52.101, final file time 21:12:55.389 after a second writing call, hash `fbbcd85850f0…` |
| Leave asked | 21:12:59.992 |
| **A chooser for the human** | first sample 21:13:00.437, last 21:14:36.121 — 93 consecutive one-second samples, one hash |
| Marker 2 — written by the observer's detached helper on two consecutive samples of the chooser | 21:13:01.521 |
| **Second call** | 21:13:01.900 → 21:13:02.074, exit 0, message id `01a20a41-4f67-7693-bd63-a7da4c67ce43` — **carrier: accepted** |
| **The second message while the chooser stood** | the observer's samples at 21:13:01.476 and 21:13:02.528 bracket the acceptance; both, and every other sample of the chooser, show the same bottom hash and 42 entries in the record. **No entry and no change of the pane when it was accepted or after** |
| **The answer to the chooser** | the tool result at 21:14:36.196 says aborted by the user after 96.2 seconds; the turn ended at 21:14:36.214 as aborted, "interrupted". He reported `esc`; no seat observed the key |
| **The second message after the answer** | **not in the record, no turn, no nonce, no receipt** — through the end of the watch at 21:19:51.213, 5 minutes 15 seconds after the turn was aborted |
| Outside the folder | `hold-probe` absent |
| **Result** | first message: complete. **Second message: UNCERTAIN** — accepted by the carrier while the chooser was in the samples, no native delivery observed; lost or pending is not known |
| Watch | 421 rows, 21:12:34.446–21:19:51.213 |
| Where | `_bus/26.lead.verdict.md` |

All times UTC, 2026-11-23. No send was retried into the sample that held it. Versions as in the third packet.

# What the three tries showed — observations of few tries, not results

1. **E1: the stored rule of D1 did not cover a command for a different folder** — a chooser appeared.
2. **E1 and E3: the denial ended the whole turn,** once in each of two samples. The record names it — a tool result
   that says aborted by the user, and a turn-aborted event. Neither sample wrote a closing message.
3. **E3: a message accepted while a chooser stood left no trace at the receiver while it stood** — no entry in the
   record, no change of the pane.
4. **Twice a message that the carrier accepted was not seen to arrive:** E2's first, and E3's second. The carrier's
   answer — exit 0 and a message id — was the same as for the three that arrived.
5. **What the two have in common, as far as the lead can name it:** by the time each could have started a turn, the
   sample's last turn had ended as aborted after a denial. The three messages that arrived (D1, E1, E3's first) each
   met a sample whose last turn had completed. No try separated this difference from others; it is a candidate
   reading.
6. E3's first message took about 8.6 seconds from the carrier's acceptance to the start of its turn; D1's and E1's
   about one second.

# What this packet does not show

- **Whether the two messages are lost or still wait,** and what would release them — a prompt typed by a human, a
  resume, a restart. Nothing was tried.
- **What becomes of a message accepted while a chooser stands when the human approves** and the turn completes.
- Whether an aborted turn is the reason, or something else the tries did not vary.
- What "No" does when a note to the program is typed with it.
- Whose hand pressed which key — no seat observed it; his statements say `esc` both times.
- Reliability, another sender, another version; independence beyond two seats — as before.

# How these tries differ from the earlier ones — the lead's own account

- They had no written scope and no challenge. The lead proposed them in its window and he released them there.
- **E2 ran in a sample that E1 had changed.** The lead proposed both for one sample and saw the dependence only
  afterwards. E3 was made in a fresh sample for that reason.
- Until E3 the observer's precondition "idle" did not say how the last turn had ended; from E3 on it does.

# Evidence

- **In the repository:** `_bus/23.*`, `_bus/24.*`, `_bus/26.*` (briefs, pre-check, markers, try files, RETURNs,
  verdicts), `raw/decision.majkee.gate-4.2026-11-23.md`, `raw/decision.majkee.e-series.2026-11-23.md`,
  `raw/pokes.log.md` (p36 to p39).
- **Private, on home:** `~/.local/share/nablarva/custody/x1-chooser-2026-11-23/` — the observer's `c23.*`, `c24.*`,
  `c26.*`; the lead's call outputs `c23.lead.call.out`, `c24.lead.call1.out`, `c26.lead.call1.out`,
  `c26.lead.call2.out`.
- **Originals:** three receipts in the second sample's `receipts/` (D1's among them), one in the third's.

# Left behind

- **Two messages that the carrier accepted and that were not seen to arrive:**
  - second sample, thread `01a209ec…`, message id `01a20a31-4540-7843-83ef-6970e8f57e32` — if it arrives it asks for
    a receipt named after `x1g-70415ddddd` and for the folder `wait-probe`;
  - third sample, thread `01a20a3c…`, message id `01a20a41-4f67-7693-bd63-a7da4c67ce43` — if it arrives it asks for
    a receipt named after `x1k-fe1e8c5f92` and nothing else.
- Both samples are still up, a tracker runs on the second — all his to close.
- Prepared files beside the samples: `sample-codex-2/`, `start-sample-2.sh`, `instruction-2.txt`.

# What his word on this packet would and would not mean — the lead's proposal

- **GO** — he accepts this packet as the witnessed record of these three tries, beside the first three packets. It
  adopts and qualifies nothing and authorizes no further test.
- **STOP** — he does not accept it as it is and says what is missing or wrong.

# Still owed when this was written — acts, not results

1. The samples closed and the tracker stopped, its script and log handed over — his own acts with the auditor.
2. A copy of the private folder to office and its pointer in the line ledger — the controller, on a POINT of the lead,
   after the tracker has stopped.
