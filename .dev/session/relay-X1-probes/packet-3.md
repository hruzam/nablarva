---
kind: witnessed probe packet 3 — the chooser test of relay-X1-probes, for Majkee's word
by: lead (flight, pen of relay-X1-probes) · 2026-11-23 · host home
status: DRAFT 1 — written from the verdicts of cycles 19 and 20. Not yet checked by the auditor, not yet decided by Majkee.
rule: as in packet.md — every row points at a file; raw captures, the receipt copy and notes are private, in ~/.local/share/nablarva/custody/x1-chooser-2026-11-23/ on home. What packet.md says about the observer, the limits and the environment holds here too and is not repeated.
---

# What this packet is, and is not

One further observation, **tried once**, on the day of the first two packets. The second packet met two approval
situations and no chooser for a human; Majkee asked for one more test that reaches a visible chooser (gate 3, H2 = A).
It gives no verdict on the relay architecture, qualifies no door, presumes no exception to the death of send-keys
injection, adopts nothing and closes no path.

# What was released, and by whom

Majkee — at the exec desk, gate 3, H2 = A (`raw/decision.majkee.gate-3.2026-11-23.md`): the test, to be scoped and
brought back; and in the lead's window, `raw/decision.majkee.chooser-test.2026-11-23.md`: the one send. Scope:
`raw/scope.chooser-test.2026-11-23.md`, draft 2, challenged once by Oraculum (`_bus/18.*`). Carrier `codex queue` only.

# The sample

A fresh, isolated session started by Majkee's hand with the scope's command: folder
`~/.cache/nablarva/relay-x1-samples/2026-11-23/sample-codex`, tmux window `sample-codex`, pane `%73`. By the observer's
pre-check before any send (`_bus/19.auditor.precheck.md`): sandbox `workspace-write`, approval `on-request`, reviewer
`user`; the target folder outside its writable roots; the standing instruction in as its first prompt; idle.

**Why the earlier tries showed no chooser** (the auditor, `_bus/17.*`): in both, the reviewer was the program —
`approvals_reviewer = "auto_review"` in his base configuration. This sample set the reviewer to `user` by flag.

# The message

`NONCE:<value>` followed by one request: after the receipt, create the folder
`~/.cache/nablarva/relay-x1-samples/2026-11-23/approval-probe` and in it an empty file `<value>.txt`; that folder is
outside the working folder; ask for permission if needed and wait; then stop. The exact line is in the try file; it is
the lead's machine-sent test text.

# The row

| | **D1** — a queued message meets a chooser that a human answers |
|---|---|
| Nonce — written into the try file and committed, before the call | `x1e-a20dd80a87` — 19:45:35 (941b803) |
| His word of release — committed before the call | 20:13:12 (6de709a) |
| Observer's marker — five preconditions hold, watch running, the thread named | 20:14:02.929 |
| The one call — `codex queue`, without `--resume`; made by one shell command of the lead that waited for the marker, with no model turn between marker and call | 20:14:03.393 → 20:14:03.675, exit 0, message id `01a20a0b-518e-7fb3-8100-44798ebdb9b1` |
| **Carrier** | accepted |
| **Native turn** | started 20:14:04.789 · completed 20:21:41.469 |
| **Receipt** | `x1e-a20dd80a87.txt` — file time 20:14:12.723, hash `5937bf1d22cf…`; the time written inside it is 20:14:09 |
| **Nonce the observer saw arrive** — it was not told it | `x1e-a20dd80a87` — matches |
| **Leave asked** to act outside the sandbox | yes, 20:14:16.863 |
| **A chooser for the human** | **yes.** First seen 20:14:17.581, last seen 20:21:36.339 — 424 consecutive one-second samples, unchanged. Three choices by the program's own labels: yes once (y) · yes, and do not ask again for commands that begin with this prefix (p) · no, with a note to the program (esc) |
| **The answer** | **the persistent yes (p).** An allow rule for exactly this command prefix was written to `~/.codex/rules/default.rules` at 20:21:36.481, and the record says "Approved command prefix saved" at 20:21:36.690. No seat observed the keypress; by his own account he pressed the number key `2`, option 2 — the same choice as (p) — as he normally does |
| **What the turn did with it** | the command ran, exit 0 at 20:21:36.581; the turn completed five seconds later |
| **The file outside** | `approval-probe/x1e-a20dd80a87.txt`, present from the observer's first sample after the chooser cleared |
| **While the chooser stood** — seven minutes nineteen seconds | the record did not grow (41 entries) and holds no entry for the chooser opening or for its answer; cursor and foreground did not change |
| **Observer** | confirms; it read nothing of the sender before its note |
| Watch | 541 rows at nominal 1-second steps, 20:14:01.936–20:23:22.610 |
| Where | `_bus/19.lead.verdict.md`, `_bus/20.lead.verdict.md` |

All times UTC, 2026-11-23. The row is not UNCERTAIN and not MISSING. The send was not retried. Versions: codex-cli
0.171.0, Claude Code 2.1.330, tmux 3.7c.

# Where the try left the scope — reported, not repaired

1. **The answer.** The scope planned: count to ten, then deny once. Observed: the chooser stood seven minutes nineteen
   seconds and was answered with the persistent yes. He says he answered as he usually does. The row therefore shows
   what an approval does. **It shows nothing about a denial.**
2. **A tracker was started on the sample at 20:17:28, while the chooser stood** — on his direct word to the auditor;
   the scope had none. The observer's samples show the chooser unchanged through it. It is not this packet's evidence.
3. **He asked the lead a question while the chooser stood.** The lead answered in its own window and sent nothing to
   any session.

# What the try showed — observations, not results

1. **With the reviewer set to the human, a message that arrives by `codex queue` can stop at a chooser, and the turn
   stays open until a human answers** — here for more than seven minutes.
2. **The record does not show the wait.** Between the request for leave and the command's result nothing is written:
   no entry for the chooser, none for the answer. In this try only the screen showed that a human was being asked.
3. **The sender saw nothing of it.** The carrier's answer was the queue's acceptance, a quarter of a second after the
   call.
4. **The persistent yes changed a file outside the sample:** a user-level rule that later sessions load.

# What this packet does not show

- What a denial does to the turn.
- What happens to a second message that arrives while a chooser stands — taken out of this test on Oraculum's
  challenge; not released.
- Whether a chooser ever ends by itself — none did within seven minutes.
- Whether the stored rule is applied in a later session.
- Whose hand pressed the key — no seat observed it; his account says it was his, the number key `2`.
- Reliability, another sender, another version; independence beyond two seats — as in the earlier packets: sender and
  author one seat, observer and checker one seat, one host, one user.

# Evidence

- **In the repository:** `raw/scope.chooser-test.2026-11-23.md`, `_bus/17.*` (why no chooser before), `_bus/18.*` (the
  challenge), `_bus/19.*` (pre-check, marker, try, RETURN, verdict), `_bus/20.*` (which option),
  `raw/decision.majkee.chooser-test.2026-11-23.md` (his release and his own account, with the chooser as he pasted it),
  `raw/pokes.log.md` (p32 to p34).
- **Private, on home:** `~/.local/share/nablarva/custody/x1-chooser-2026-11-23/` — the observer's `c19.*` (note, watch,
  captures, the receipt copy, a tracker report), the lead's call output `c19.lead.call.out`, and the tracker's own
  folder.
- **Originals:** the receipt in the sample's `receipts/`; the empty file in `approval-probe/` beside the sample.

# Left behind by the try

- **A rule in `~/.codex/rules/default.rules`, line 59:** commands that begin with
  `mkdir -p /home/hruzam/.cache/nablarva/relay-x1-samples/2026-11-23/approval-probe` are no longer asked about, in any
  session that loads that file. It is his file; no seat touches it.
- The sample is still up and a tracker runs on it — both his to close.
- One receipt; the folder `approval-probe/` with one empty file.

# What his word on this packet would and would not mean — the lead's proposal

- **GO** — he accepts this packet as the witnessed record of the chooser test, beside the first two. It adopts and
  qualifies nothing and authorizes no further test.
- **STOP** — he does not accept it as it is and says what is missing or wrong.

# Still owed when this was written — acts, not results

1. The sample closed and the tracker stopped, its script and log handed over — his own acts with the auditor.
2. A copy of the new private folder to office and its pointer in the line ledger — the controller, on a POINT of the
   lead; covered by his earlier word on the private evidence.
