---
kind: witnessed probe packet — the result rows of relay-X1-probes, for Majkee's GO or STOP
by: lead (flight, pen of relay-X1-probes) · 2026-11-23 · host home
status: FOR THE GATE — written from the verdicts of cycles 02, 06, 07 and 08. Draft 1 was compared with its sources by a fresh-eyes child of the lead. Draft 2 was checked by the auditor, the seat of the other brand — REVISE; the gate evidence holds and no rerun is needed; its points on wording, times, custody and what is asked are all taken here (_bus/09.auditor.return.md, _bus/09.lead.verdict.md). The auditor has not read this revision. DECIDED — Majkee, at the exec desk, 2026-11-23: GO, in his word "ok, than `GO`" (raw/decision.majkee.gate-2.2026-11-23.md, G2; _bus/10.lead.verdict.md). By his answer at G9 the bed is not retired: it stays open for further tests and a second packet. Nothing in this file is changed after his GO but this line.
rule: every row points at a file. Raw captures, receipts and notes are private, in ~/.local/share/nablarva/custody/x1-probes-2026-11-22/ on home; this file carries times, values, hashes and categories only.
---

# What this packet is, and is not

It reports two observations, **each tried once**, on one day, on one host, into one disposable receiver. It gives **no
verdict on the relay architecture**, **qualifies no door** as a transport or as a replacement for the file-poke,
**presumes no exception** to the recorded death of send-keys injection, **adopts nothing** and — Majkee's own condition
on line 5 — **closes no path**. Any later relay architecture decision follows L14 and may cite it as evidence.

# What was released, and by whom

Majkee, at the exec desk, 2026-11-22: lines 2, 3, 6, 4, 5 and 7 of the handoff's menu
(`raw/decision.majkee.walkthrough-1.2026-11-22.md`; read into rows by `_bus/02.lead.verdict.md`). Lines 8 to 19 were not
asked. He reports that he started the sample himself on 2026-11-23 (`raw/decision.majkee.sample-up.2026-11-23.md`).

# The rows

| Line | What | Result | Where |
|---|---|---|---|
| 2 | Start of `sample-codex` by Majkee's hand — `codex -C <folder> -m gpt-6.1-terra`, no sandbox flag, no approval flag | **DONE** — on 2026-11-23. Window `sample-codex`, pane `%72`, folder `~/.cache/nablarva/relay-x1-samples/2026-11-22/sample-codex/`; the model name was accepted. When: the lead's own tmux watch first saw codex in the foreground of the pane at 11:05:04 UTC — no second source for that time. Whose hand: he says it was his own; nobody else witnessed the start. The command without flags is what he released; the observer read the resulting configuration, not the command line. | his word, `raw/decision.majkee.sample-up.2026-11-23.md`; `_bus/02.lead.verdict.md`; `_bus/06.auditor.return.md` (pane, folder); `_bus/07.auditor.return.md` (configuration) |
| 2 | Close of the sample by the same hand | **NOT YET DONE** — an act still owed, not a result: the sample still runs. Asked on the gate sheet. | — |
| 3 | The standing NONCE instruction, by his hand | **DONE** — the first input of the sample's record carries the `NONCE:` trigger and the path of the sample's own `receipts/` folder (the observer: yes and yes; the text is not in the repository). The record's first entry is at 11:21:55.646 UTC; the first look, at 11:17, found no record at all. | `_bus/06.lead.verdict.md`; `_bus/07.auditor.return.md`; `_bus/09.auditor.return.md` |
| 6 | The auditor as observer, its reads, the private folder | **DONE** — the folder exists, 0700, files 0600. The observer was told neither nonce. It states that it read no evidence of the sender before it wrote either note. For B its blindness ended at the paste, where the line was visible on the input row. | `_bus/06.auditor.return.md`, `_bus/07.auditor.return.md`, `_bus/08.auditor.return.md`, `_bus/09.auditor.return.md` |
| 4 | **Observation A** — `codex queue`, lead → `sample-codex`, once | **carrier: accepted · native turn: seen · receipt: present, nonce matches · observer: confirms** | `_bus/07.lead.verdict.md` |
| 5 | **Observation B** — tmux paste, then Enter as a separate step, lead → `sample-codex`, once; one explicit exception to L4 | **staged: seen · the paste alone submitted nothing · submit by the separate Enter: seen · native turn: seen · receipt: present, nonce matches · observer: confirms** | `_bus/08.lead.verdict.md` |
| 7 | The sample's session record | **KEPT** on home through the gate — `~/.codex/sessions/2026/11/23/rollout-2026-11-23T12-04-52-01a20814-8698-75a1-9754-e976fb0cea82.jsonl`. What happens to it after the gate is asked on the gate sheet. | `_bus/07.auditor.return.md` |
| 8–19 | The second sample, the six deferred rows, the U01 capture and its classification | **NOT RUN** — not released, not asked | handoff §6 |

No row is UNCERTAIN and none is MISSING. Nothing was retried; no sender and no carrier was switched.

## Row A in full — line 4

| | Time (UTC, 2026-11-23) | Source |
|---|---|---|
| Nonce `x1a-a320ba65f3` written into the try file and committed (5041275) | 11:24:50 | `_bus/07.lead.try.md`; `git log` |
| Observer's marker: five preconditions hold, watch running | 11:25:46.191 | `_bus/07.auditor.ready.md` |
| The one call — `codex queue --thread 01a20814-… --message "NONCE:x1a-a320ba65f3"`, without `--resume`. One shell command of the lead waited for the marker and then called; no turn of the lead sat between the two. | 11:25:48.953 → 11:25:49.123, exit 0 | try file |
| Its whole output | `Queued message 01a20827-b2ab-74d1-82ff-c5a793ce3b71 for thread 01a20814-8698-75a1-9754-e976fb0cea82.` | try file |
| Turn started in the sample | 11:25:49.113 | observer, from the record |
| The message is an entry of the sample's record; the observer reads the value `x1a-a320ba65f3` | 11:25:49.400 | observer |
| Receipt `x1a-a320ba65f3.txt`, content `x1a-a320ba65f3 2026-11-23T11:25:52Z` | 11:25:52.717 — 3.8 s after the call | observer; hash `c08a870fb96684c5…`, the same for the private copy (lead) |
| Turn completed | 11:25:53.996 | observer |
| Dialog | none visible in any sample of the watch; the record shows the write carried out and no approval asked | observer |
| Watch | 271 rows at nominal 2-second steps plus the time each sample took, to 11:34:55; the budget of 180 s ended 11:28:48.953 | observer |

## Row B in full — line 5

| | Time (UTC, 2026-11-23) | Source |
|---|---|---|
| Nonce `x1b-11022ca3bc` written into the try file | 11:38:10 | `_bus/08.lead.try.md` |
| That file committed (b684179) — before the marker and the paste | 11:40:22 | `git log` |
| Observer's marker: five preconditions hold, watch running | 11:41:49.823 | `_bus/08.auditor.ready.md` |
| Look 1 — codex in the foreground, input row empty (dim placeholder only), no dialog, not working, cursor (2,38) | 11:42:00.839 | try file |
| Stage — `tmux set-buffer -b x1b "NONCE:x1b-11022ca3bc"`, `tmux paste-buffer -p -b x1b -t %72`, both exit 0 | 11:42:11.668 → 11:42:11.676 | try file |
| Staged, as the observer saw it — the complete line alone, cursor column 2 → 22, the record unchanged at 34 entries | 11:42:12.635, the first sample that shows it | observer |
| Look 2 — the line on the input row once and alone, cursor (22,38), no turn | 11:42:18.894 | try file |
| The line was still on the row, the record still unchanged | in the last such sample, 16.6 s after the first | observer |
| Submit — `tmux send-keys -t %72 Enter`, one key, exit 0, 18 s after the paste | 11:42:29.659 → 11:42:29.665 | try file |
| Turn started in the sample | 11:42:29.687 | observer, from the record |
| The message is an entry of the record; the observer reads the value `x1b-11022ca3bc` | 11:42:29.984 | observer |
| The first sample that shows the row cleared and the record grown | 11:42:30.268 — 17.6 s after the first staged sample | observer |
| Receipt `x1b-11022ca3bc.txt`, content `x1b-11022ca3bc 2026-11-23T11:42:33Z` | 11:42:33.370 — 3.7 s after the Enter | observer; hash `f458c82bb36aaae4…`, the same for the private copy (lead) |
| Turn completed; the record at 49 entries | 11:42:36.231 | observer |
| Look 3 — the line left the input row, cursor back at (2,38); look 4 at 11:43:01.216 the same | 11:42:36.228 | try file |
| Dialog | none visible in any sample of the watch or in the lead's four looks; the record shows the write carried out and no approval asked | both |
| Watch | 541 rows at nominal 1-second steps plus the time each sample took, to 11:51:09; the budget of 180 s ended 11:45:29.659 | observer |

# The receiver as it actually ran — observed, not chosen

| | Value | Source |
|---|---|---|
| CLI | codex-cli 0.171.0 (sender side read at 11:24:50 and 11:38:10; the sample's record says the same) | try files; observer |
| Other versions on the sender's side | Claude Code 2.1.330 · tmux 3.7c | try files |
| Model | `gpt-6.1-terra`; the program's footer shows "GPT-6.1 Terra high" | observer |
| Sandbox | `workspace-write`, network off | observer, from the record |
| Approval | the granular kind — permission requests and MCP elicitations allowed; sandbox approval, rules and skill approval off. Majkee describes it as the mode that asks for approval. | observer; his word |
| State at each try | idle, input row empty, no dialog, one completed turn before A and two before B | observer's preflights |

The results of A and B hold for this configuration only.

# The environment during the tries

- **Two tracker runs, by the observer's account both requested by Majkee directly.** He had told the lead that morning
  that he wants the sample's behaviour tracked at a basic level. Everything in this paragraph is the observer's word
  (RETURNs 07, 08, 09); the lead did not open the tracker's files. Three processes read the sample's pane, record and
  receipt metadata, its process chain, runtime metadata of its thread and byte counts of its terminal output. All three
  were running at A's preflight. During B the first run ended at 11:42:24 — between the paste and the Enter — and a
  replacement started at 11:45:01. **In the gap, 11:42:24 to 11:45:01, no tracker ran: that covers B's Enter, its turn
  and its receipt.** The private folder holds two tracker folders, `tracker.2EvwcVSe/` and `tracker-manual.u7ady8az/`.
  Neither is the evidence of any row.
- **The auditor did that work for him inside its observation turn of B.** Its watch was a detached process and went on
  independently of the replacement; it shows no gap and an empty error file.
- **tmux showed seven grouped sessions** (`helloWorld-37` to `-43`) beside `helloWorld` — the lead's own reading of
  `tmux list-panes -a` at 05:46 UTC on 2026-11-23, written down here for the first time. They show the same windows.
  They prove nothing about who attached; the lead has told Majkee and has no answer yet.
- **After the tries** the auditor relayed a wish of Majkee's for one approval-dialog side test in the sample for his
  tracker (`raw/request.auditor.tracker-approval.2026-11-23.md`). No seat sends anything for it: both released tries are
  spent. If he types it himself, it is his own act in his own sample, outside the rows of this packet
  (`raw/reply.lead.tracker-approval.2026-11-23.md`). At the auditor's check no such test was visible in the record.
- **A fork of the exec desk's session as his tutor** (his word at S7): it is not a seat of this party.

# What the tries showed beside their rows — observations, not results

1. **No dialog was seen at the write.** Majkee and the lead expected the sample to ask before writing a receipt. In
   neither try was a dialog visible, and the record shows no approval asked: the sample runs with `workspace-write`, and
   both writes were inside its own folder. What this approval mode does ask for was not touched.
2. **In this sample the thread id was in the footer before any turn**, and no session record existed until the first
   turn. The predecessor expected the id only after the first turn.
3. **In these two turns tmux metadata did not tell the working pane from the idle one** — the foreground command and
   the cursor did not move. The cursor did move with staged text on the input row.
4. **In this one try, `codex queue` without `--resume` started a turn in the idle sample within a fraction of a second**
   of the call.
5. **A window can hide a seat's turns.** On 2026-11-22 the exec desk had asked its question and its window did not show
   it for eight hours, because an old text selection pinned the view (`raw/pokes.log.md`, p10). "The seat answered" and
   "the human saw it" are two facts.

# What this packet does not show

- Anything about a **busy** receiver. What a queued message or a paste does in a working turn is not known.
- Anything about an input row that already holds text, longer or multi-line text, a paste without bracketed paste, a
  Claude receiver, a Codex sender, another host, or another version.
- Why the trial's three Claude → Codex attempts through the archived adapter failed (0 of 3 verified, Codex 0.167.2 —
  handoff §3).
- Reliability. Each door was tried once. One success is not a rate.
- **Independence beyond two seats.** The sender of both tries is also the author of this packet, and the observer of both
  tries is also its last checker. Everything ran on one host, under one user, in one tmux server. The observer did not
  witness the start of the sample, Majkee's presence, or the sender's shell.
- **What a sampled watch cannot see.** A dialog, or a paste arriving in parts, that begins and ends between two samples
  — one or two seconds apart — would not show. The packet says "none visible" and "no approval recorded"; it does not
  say "none occurred".

# Evidence

- **In the repository:** `_bus/02.*` (the release), `_bus/06.*` (the observer bound), `_bus/07.*` (A), `_bus/08.*` (B),
  `_bus/09.*` (the final check), `raw/pokes.log.md` (every poke, p01–p18), `raw/decision.majkee.*.md` (his words).
- **Private, on home only:** `~/.local/share/nablarva/custody/x1-probes-2026-11-22/` — the observer's notes
  (`c06.first-look.md`, `c06.after-standing-instruction.md`, `c07.note.md`, `c08.note.md`), its watches and captures, the
  two receipt copies, the lead's own looks of B (`c08.lead.*`), the call output of A (`c07.lead.call.out`), and the two
  tracker folders. It has no second copy on another host.
- **The originals of the receipts:** `~/.cache/nablarva/relay-x1-samples/2026-11-22/sample-codex/receipts/`.

# What GO and STOP would mean — the lead's proposal; the sheet asks Majkee to confirm or change it

- **GO** — he accepts this packet as the witnessed record of the stage. The gate of `relay-X1-probes` is met and the bed
  is retired: out of the router, kept on disk. The rows stand as "tried once" and may be cited as evidence under L14.
  GO adopts nothing, qualifies nothing, releases nothing further and runs none of lines 8 to 19.
- **STOP** — he does not accept it as it is, and says what is missing or wrong. The bed stays open. Nothing is sent
  again and nothing is rerun without a new release; the two tries stay spent either way.

# What the gate sheet asks beside GO or STOP — each on its own

1. **His tracker** — whether it is stopped now, and by whom.
2. **Closing `sample-codex`** by his hand (line 2).
3. **The sample's session record** after the gate — keep or delete (line 7 kept it through the gate).
4. **The private folder of this stage** — a second copy on office, as the other custody folders have.
5. **The old capture originals in `/tmp`** from the predecessor bed — keep or delete; the hold stands until he says.
6. **The exception to L4** — spent, and returned to him with this evidence, as `docs/ARCHITECTURE.md` lines 216–219 ask.
   No later gate may presume it.
7. **The open work this bed owns and did not run** — lines 8 to 19, the cases X0-U01 to U06, and the two further
   samples he has in mind — where it goes if the bed is retired.

Not asked, and not changed by this packet: **L14 D4 stays an architecture gate.** The handoff's table of locks says the
packet is offered as "evidence input only"; his own gate sentence says a later decision "may cite this packet as
evidence". The gate sentence is the one this packet was written to.
