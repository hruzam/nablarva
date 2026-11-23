---
kind: witnessed probe packet — the result rows of relay-X1-probes, for Majkee's GO or STOP
by: lead (flight, pen of relay-X1-probes) · 2026-11-23 · host home
status: DRAFT 1 — written from the verdicts of cycles 02, 06, 07 and 08; not yet checked by the auditor (the final check, from the other brand); not yet before Majkee
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
asked. He started the sample himself on 2026-11-23 (`raw/decision.majkee.sample-up.2026-11-23.md`).

# The rows

| Line | What | Result | Where |
|---|---|---|---|
| 2 | Start of `sample-codex` by Majkee's hand — `codex -C <folder> -m gpt-6.1-terra`, no sandbox flag, no approval flag | **DONE** — started 2026-11-23, about 11:04 UTC by the name of its session record; window `sample-codex`, pane `%72`, folder `~/.cache/nablarva/relay-x1-samples/2026-11-22/sample-codex/`; the model name was accepted. Whose hand: his own line, "It was me". | his word of 2026-11-23; `_bus/06.auditor.return.md` |
| 2 | Close of the sample by the same hand | **OPEN** — the sample still runs. It is closed by his hand after the observer's last read; asked on the gate sheet. | — |
| 3 | The standing NONCE instruction, by his hand | **DONE** — the first input of the sample's record carries the `NONCE:` trigger and the path of the sample's own `receipts/` folder (the observer: yes and yes; the text is not in the repository). The first look, before it, found no session record at all. | `_bus/06.lead.verdict.md`; `_bus/07.auditor.return.md` |
| 6 | The auditor as observer, its reads, the private folder | **DONE** — the folder exists, 0700, files 0600. The observer wrote its note of each try before it read anything of the sender, and was told neither nonce. | `_bus/06.auditor.return.md`, `_bus/07.auditor.return.md`, `_bus/08.auditor.return.md` |
| 4 | **Observation A** — `codex queue`, lead → `sample-codex`, once | **carrier: accepted · native turn: seen · receipt: present, nonce matches · observer: confirms** | `_bus/07.lead.verdict.md` |
| 5 | **Observation B** — tmux paste, then Enter as a separate step, lead → `sample-codex`, once; one explicit exception to L4 | **staged: seen · the paste alone submitted nothing · submit by the separate Enter: seen · native turn: seen · receipt: present, nonce matches · observer: confirms** | `_bus/08.lead.verdict.md` |
| 7 | The sample's session record | **KEPT** on home through the gate — `~/.codex/sessions/2026/11/23/rollout-2026-11-23T12-04-52-01a20814-8698-75a1-9754-e976fb0cea82.jsonl`. Its deletion is asked on the gate sheet. | `_bus/07.auditor.return.md` |
| 8–19 | The second sample, the six deferred rows, the U01 capture and its classification | **NOT RUN** — not released, not asked | handoff §6 |

No row is UNCERTAIN and none is MISSING. Nothing was retried; no sender and no carrier was switched.

## Row A in full — line 4

| | Time (UTC, 2026-11-23) | Source |
|---|---|---|
| Nonce `x1a-a320ba65f3` written and committed (5041275) | 11:24:50 | `_bus/07.lead.try.md` |
| Observer's marker: five preconditions hold, watch running | 11:25:46.191 | `_bus/07.auditor.ready.md` |
| The one call — `codex queue --thread 01a20814-… --message "NONCE:x1a-a320ba65f3"`, without `--resume` | 11:25:48.953 → 11:25:49.123, exit 0 | try file |
| Its whole output | `Queued message 01a20827-b2ab-74d1-82ff-c5a793ce3b71 for thread 01a20814-8698-75a1-9754-e976fb0cea82.` | try file |
| Turn started in the sample | 11:25:49.113 | observer, from the record |
| The message is an entry of the sample's record; the observer reads the value `x1a-a320ba65f3` | 11:25:49.400 | observer |
| Receipt `x1a-a320ba65f3.txt`, content `x1a-a320ba65f3 2026-11-23T11:25:52Z` | 11:25:52.717 — 3.8 s after the call | observer; hash `c08a870fb96684c5…`, the same for the private copy (lead) |
| Turn completed | 11:25:53.996 | observer |
| Dialog | none | observer |
| Watch | 271 rows at 2-second steps, to 11:34:55; budget of 180 s ended 11:28:48.953 | observer |

## Row B in full — line 5

| | Time (UTC, 2026-11-23) | Source |
|---|---|---|
| Nonce `x1b-11022ca3bc` written and committed (b684179) | 11:38:10 | `_bus/08.lead.try.md` |
| Observer's marker: five preconditions hold, watch running | 11:41:49.823 | `_bus/08.auditor.ready.md` |
| Look 1 — codex in the foreground, input row empty (dim placeholder only), no dialog, not working, cursor (2,38) | 11:42:00.839 | try file |
| Stage — `tmux set-buffer -b x1b "NONCE:x1b-11022ca3bc"`, `tmux paste-buffer -p -b x1b -t %72`, both exit 0 | 11:42:11.668 → 11:42:11.676 | try file |
| Staged, as the observer saw it — the complete line alone, cursor column 2 → 22, the record unchanged at 34 entries | 11:42:12.635 | observer |
| Look 2 — the line on the input row once and alone, cursor (22,38), no turn | 11:42:18.894 | try file |
| The line stood on the row without the record growing | for 17.6 s | observer |
| Submit — `tmux send-keys -t %72 Enter`, one key, exit 0, 18 s after the paste | 11:42:29.659 → 11:42:29.665 | try file |
| Turn started in the sample | 11:42:29.687 | observer, from the record |
| The message is an entry of the record; the observer reads the value `x1b-11022ca3bc` | 11:42:29.984 | observer |
| Receipt `x1b-11022ca3bc.txt`, content `x1b-11022ca3bc 2026-11-23T11:42:33Z` | 11:42:33.370 — 3.7 s after the Enter | observer; hash `f458c82bb36aaae4…`, the same for the private copy (lead) |
| Turn completed; the record at 49 entries | 11:42:36.231 | observer |
| Look 3 — the line left the input row, cursor back at (2,38); look 4 at 11:43:01.216 the same | 11:42:36.228 | try file |
| Dialog | none | both |
| Watch | 541 rows at 1-second steps, to 11:51:09; budget of 180 s ended 11:45:29.659 | observer |

# The receiver as it actually ran — observed, not chosen

| | Value | Source |
|---|---|---|
| CLI | codex-cli 0.171.0 (sender side read at 11:24:50 and 11:38:10; the sample's record says the same) | try files; observer |
| Other versions on the sender's side | Claude Code 2.1.330 · tmux 3.7c | try files |
| Model | `gpt-6.1-terra`; the footer shows "GPT-6.1 Terra high" | observer; Majkee's line |
| Sandbox | `workspace-write`, network off | observer, from the record |
| Approval | the granular kind — permission requests and MCP elicitations allowed; sandbox approval, rules and skill approval off. Majkee names the mode "Ask for approval". | observer; his word |
| State at each try | idle, input row empty, no dialog, one or two completed turns before it | observer's preflights |

The results of A and B hold for this configuration only.

# The environment during the tries

- **A tracker of Majkee's own** — three reading processes that he asked the auditor to set up — read the sample's pane,
  record and receipt metadata, its process chain and byte counts of its terminal output. It ran through all of A. During B
  it ended at 11:42:24 (between the paste and the Enter); a replacement, again on his direct word, started at 11:45:01. It
  sends nothing and is not the evidence of any row. Its files are in `tracker.2EvwcVSe/` in the private folder; the lead
  did not open them.
- **The auditor did that work for him inside its observation turn of B.** Its watch was a detached process; it shows no
  gap and an empty error file.
- **tmux showed seven grouped sessions** (`helloWorld-37` to `-43`) beside `helloWorld` on the morning of 2026-11-23 —
  further views of the same windows. The lead takes them to be Majkee's attaches and has asked him.
- **The exec desk's fork as his tutor** (his word at S7): it is not a seat of this party. He says the start was his hand.

# What the tries showed beside their rows — observations, not results

1. **No dialog at the write.** Majkee and the lead expected the sample to ask before writing a receipt. It did not, twice:
   under the defaults the sample runs with `workspace-write`, and both writes were inside its own folder. What this
   approval mode does ask for was not touched.
2. **The thread id is in the footer before any turn**, and no session record exists until the first turn. The predecessor
   expected the id only after the first turn.
3. **tmux metadata does not tell a working Codex pane from an idle one** — the foreground command and the cursor did not
   move during either turn. The cursor does move with staged text on the input row.
4. **`codex queue` without `--resume` started a turn in an idle session within a fraction of a second.**
5. **A window can hide a seat's turns.** On 2026-11-22 the exec desk had asked its question and its window did not show
   it for eight hours, because an old text selection pinned the view (`raw/pokes.log.md`, p10). "The seat answered" and
   "the human saw it" are two facts.

# What this packet does not show

- Anything about a **busy** receiver. What a queued message or a paste does in a working turn is not known.
- Anything about an input row that already holds text, longer or multi-line text, a paste without bracketed paste, a
  Claude receiver, a Codex sender, another host, or another version.
- Why the trial's three Claude → Codex attempts through the archived adapter failed (0 of 3 verified, Codex 0.167.2).
- Reliability. Each door was tried once. One success is not a rate.
- The observer's own limit: a watch at one- or two-second steps cannot see a dialog or a partial paste that begins and
  ends between two samples. The record's entries speak against both.

# Evidence

- **In the repository:** `_bus/02.*` (the release), `_bus/06.*` (the observer bound), `_bus/07.*` (A), `_bus/08.*` (B),
  `raw/pokes.log.md` (every poke, p01–p15), `raw/decision.majkee.*.md` (his words).
- **Private, on home only:** `~/.local/share/nablarva/custody/x1-probes-2026-11-22/` — the observer's notes
  (`c06.first-look.md`, `c06.after-standing-instruction.md`, `c07.note.md`, `c08.note.md`), its watches and captures, the
  two receipt copies, the lead's own looks of B (`c08.lead.*`) and the call output of A (`c07.lead.call.out`). It has no
  second copy on another host.
- **The originals of the receipts:** `~/.cache/nablarva/relay-x1-samples/2026-11-22/sample-codex/receipts/`.

# What the gate sheet will ask of Majkee beside GO or STOP

Listed here so that the check can see them; they are decided on the sheet, not in this packet.

1. Closing `sample-codex` by his hand (line 2), and ending his tracker.
2. Keeping or deleting the sample's session record (line 7).
3. Keeping or deleting the old capture originals in `/tmp` from the predecessor bed — the hold stands until he says.
4. A second copy of this stage's private folder on office, as the other custody folders have.
5. The wording for L14 D4 beside his gate sentence — "evidence input only" against "may cite this packet as evidence".
6. That the one exception to L4 is spent and returns to him with this evidence, as `docs/ARCHITECTURE.md` lines 216–219 ask.
