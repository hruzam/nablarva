---
kind: planning check — observation consumer
by: @Field · claude-sonnet-4-6 · 2026-11-27
for: architecture-X2-goal-plan raw/
did_not_read: >-
  flag.md, pulse.md, first-blind-triangulation-relay/ files, architecture-X1-bookkeeping/,
  ovitmugen sources, ia-sync/claude/hooks/statusline.sh direct text. Findings from files
  that reference these are used; source anchors named where load-bearing.
source_abbreviations: >-
  V = research-verdict.md §4,§7,§9 · EM = events-map.v0.2026-10-02.md ·
  MS = master.symmetry.relay-and-floor.collision.2026-11-26.md ·
  F1 = asymmetry.session-telemetry-floor.blind-review.md ·
  F2 = asymmetry.session-telemetry-floor.round-2.md ·
  T0 = termpanum-X0-source-contract/raw/research-disposition.md
---

# Check: observation consumer

## 1. What to track

Code notes used below: hooks = programs the CLI calls on internal events (turn start, tool use,
permission request, session end, etc.); OSC 7501 = a terminal control sequence a program
emits to report its own state; pipe-pane = a tmux command that copies a pane's output bytes
to a file or command; L14 D4 = the research gate "does the relay program open?" (answered
REFUSE by relay-X2-research, 2026-11-27).

### From a signal the CLI itself emits

| Event / state | Signal | CLI | Measured on this host | Source |
|---|---|---|---|---|
| Session started / ended | `SessionStart`, `SessionEnd` hooks | Claude Code, Codex | No — documented, not tested | EM rows 1–2 |
| Turn started / ended | `UserPromptSubmit`, `Stop` hooks | Claude Code, Codex | No | EM rows 3–4 |
| Tool started / ended | `PreToolUse`, `PostToolUse` hooks | Claude Code, Codex | No | EM rows 7–8 |
| Approval or question outstanding | `PermissionRequest` hook | Claude Code, Codex | No | EM row 11; V §4 |
| Approval/question (declared, real-time) | `claude agents --json`: `status: waiting`, `waitingFor: permission prompt\|input needed` | Claude Code 2.1.332 | No — documented, untested on host | V §4; F2 §7 |
| Compaction (context-window reduction) | `PreCompact`/`PostCompact` hooks | Claude Code, Codex | No | EM row 16 |
| Progress (working indicator) | `pane_pb_state` / `pane_pb_progress` tmux format variables (from OSC 9;4 that Claude emits) | Claude Code, Codex (optional) | No | V §4; MS §4 |
| Session exited | Kernel: SIGCHLD / wait4 / pidfd — fires even when hooks miss | — (kernel) | No fixture run on host | EM row 2; F1 signal table |

**Hook caveat.** Codex hooks must be listed as trusted in the operator's config before they fire.
One report (different platform/mode) shows three missed SessionEnd events in ten clean exits. (V §4)

**OSC 7501 and Claude.** Claude 2.1.332 checks whether tmux supports the sequence; tmux 3.7c has
no handler. No blocked-state report is expected from Claude inside tmux 3.7c. (F2 §7; MS §4)

### From terminal bytes or the screen (no cooperation from the program)

| Signal | What it gives | Key limit | Source |
|---|---|---|---|
| OSC 7501 record in raw pane bytes | `state=blocked:app=codex:kind=permission\|question\|auth` from Codex — visible because tmux 3.7c copies bytes BEFORE parsing, so a pipe-pane tap sees it even though tmux's own display does not | Scope is the displayed thread only; a late tap misses the only copy | F2 §7; MS §4,§6 |
| Output silence over a measured window | Process alive and producing nothing | Does NOT distinguish "free, waiting for a new command" from "blocked, waiting for an answer" | F1 local observations |
| `pane_dead_status` / `pane_dead_signal` tmux format | Pane exit status and signal | Pane disappearing has other causes; version-dependent | F1 signal table |

### Not knowable today

| Gap | Reason | Source |
|---|---|---|
| "Free input" vs "blocking question" | Two real TUI programs in both states showed identical signals on every passive channel (bytes, CPU, wait-channel, terminal mode, foreground group) in a live fixture | F1 §86 and local observations |
| "Hung" vs "very slow" | No finite passive proof for programs the observer did not write | F1 §81 |
| Whether any hook fires as documented on this host | No session was started, no door was tested in relay-X2-research | V §9 |
| Whether `claude agents --json` lists a tmux-attached session | Undocumented; not tested | V §9 |

---

## 2. The record — shape assumed and where pieces disagree

The events-map (EM §0) defines the shared event envelope:
`ts · session_id · event · phase? · source · certainty · grade? · anchor · payload`

Four assumptions are consistent across all files:

- **Append-only.** Events are facts; state is derived on read, never stored. (EM §0; X5 = nablarva-X5-spine-slice — the bed that builds the shared spine — RUNBOOK §scope item 3)
- **Per-writer files.** One writing process per file; writer id in filename and every line. (EM §0; X5 RUNBOOK E3)
- **Address registry.** Seat-addressed, not PID or pane id. (X5 RUNBOOK §scope item 1)
- **Payload is a path, not content.** Text lives in the record, not in the event. (EM §0)

⚡ CONFLICT 1 — stored state. DRAFT 2 of the relay verdict proposed a state file; the auditor
opposed it as contradicting the "state derived, never stored" rule. The rule prevailed. (V §7)

⚡ CONFLICT 2 — envelope format. The jev decision model (a callee the system uses for structured
decisions, not an observed session) uses a different field set:
`schema · event_id · sequence · at · session_id · kind · actor · data`.
These two shapes cover the same idea but are not aligned. Resolution is OPEN and explicitly named
as a cross-repo item needing a decision before the first production writer is coded. (EM §3)

⚡ CONFLICT 3 — four states are not a partition. The events-map lists four states (working,
waiting, idle, exited) as if they are exclusive. The floor research (F1, F2; MS §4) showed they
are independent dimensions: a question can be outstanding while a worker computes. The events-map
(still on DRAFT status) has not been updated with this finding.

---

## 3. Which existing bed is the natural home

Code: X5 = nablarva-X5-spine-slice · termpanum-X1 = termpanum-X1-source-qualification ·
seswin-X1 = session-window-X1-surface · sublime-X1 = sublime-observer-X1-file-publish

| Bed | What it gives a consumer if finished | What it lacks | Owner / host | Current state |
|---|---|---|---|---|
| **X5** (builds the shared observe→record→view spine: address registry + per-writer record + one producer + one view) | Infrastructure any consumer that reads from the shared record would need | Component disk name (Majkee's GO needed); architecture-X1-bookkeeping completion; no code or folder exists yet | Cartan, Codex · office | Authored, no seat entered |
| **termpanum-X1** (qualifies the tmux pipe-pane byte source against frozen expectations) | Qualified byte source with known timing limits and failure cases | P2 blocked (cleanup step unverified); P3 and P4 not run; D4 verdict now given | Cartan, Codex · office | P2 partial, blocked |
| **seswin-X1** (checks what fields a tmux status surface can really display, by which route) | Field list with source and freshness; three display routes compared; one recommended smallest first version, with the alert slot | Sandbox release from Majkee; three-route trial not yet run | lead.seswin, Claude · home | Waiting on Majkee to read the sheet |
| **sublime-X1** (publishes Sublime editor views as plain files for agents to read) | A way for CLI agents to read shared editor views by absolute path | Smoke test with Majkee still pending | oraculum, Claude · home | Near-complete |

**Natural home: seswin-X1.** Its stated goal is exactly the consumer question — what can a session
status surface show today, and by which route. It is active on the home host (where the sessions
run), has a field list drafted, and has an audit seat already assigned. The first consumer is a
natural output of this bed's packet, not a new bed.

**Alternative: X5.** If the consumer is meant to read from the shared observation record (per-writer
files from hooks or the byte collector), X5 is the right deeper home. A consumer that only polls
`claude agents --json` and reads Codex's raw pane bytes does NOT need X5 first.

---

## 4. The smallest consumer — three candidates

**Candidate A — a one-shot command that prints the current state of each seat** (ranked first)

Reads: `claude agents --json` for Claude sessions; `tmux display-message -p '#{pane_pb_state}'`
per pane for progress. For Codex's blocked state: a raw byte tap (pipe-pane) already attached
to that pane would have to be running.

Already exists: `claude agents --json` works today on the installed 2.1.332. Pane format
variables work in tmux 3.7c.

Must write: a 10–20 line script joining the two. No new infrastructure needed.

Cannot show: Codex's blocked/question state unless a pipe-pane tap is already attached; short
waits missed between polls; the distinction between "free input" and "blocking question" is not
reliable without the declared OSC 7501 signal.

**Candidate B — a live row in the tmux status line**

Reads: hooks output + `claude agents --json`; extends the already-deployed `statusline.sh`.

Already exists: Claude status line is running; `pane_pb_state` from OSC 9;4 is available in
tmux format variables.

Must write: a Codex state reader integrated into the refresh cycle; Codex OSC 7501 blocked state
still needs the raw byte tap.

Cannot show: same limits as A; additionally: nothing if hooks are not trusted.

**Candidate C — an append-only event file read by a small watcher**

Reads: the shared observation record (per-writer files from X5 or from hooks directly).

Already exists: nothing. X5 has no code, no folder, no producer.

Must write: a producer (tmux hook writer), the record format, a view script. This is the whole
X5 work sequence.

Cannot show: more than what the hooks and byte tap together show; depends on hooks being trusted.

---

## 5. Continuity between tests and measurements

| Test / pass | What was measured | Leading to |
|---|---|---|
| relay-X1-probes (October 2026, 5 pointers) | 3 arrived in seconds; 1 arrived 2 days later; 1 unresolved. All samples at set-up recipients. | Showed the file-poke composition works but left a timing gap open; established the poke log format |
| relay-X2-research live run (8 pointers, 2026-11-26) | All 8 returned; operator carried none; 39–705 s each | Showed routine use is served; underpins the REFUSE verdict for the relay program (V §3) |
| F1 — blind floor research (fixture on Linux 6.18.57, no agent TUI exercised) | Two TUI programs in "free input" and "blocking question" showed identical signals on every passive channel | Proved the core limit: the pair cannot be split from below without cooperation; this is load-bearing for the ADOPT condition in the verdict |
| events-map v0.3 (October 2026, office) | 20 events, 4 states; sources confirmed per vendor from documentation; no host fixture | Established the vocabulary; named the gaps and the unresolved summarizer-fetch rows |
| termpanum-X1 P2 (October 2026, office) | pipe-pane captures byte-identical to oracle for normal and burst workloads; ONLCR capture done but cleanup unverified | Qualified the byte source for healthy runs; left failure modes and ONLCR cleanup open |
| F2 — open round-2 (pinned Codex 0.172.0 source, 2026-11-26) | Codex writes OSC 7501 without waiting for terminal reply; tmux 3.7c copies bytes before parsing → OSC 7501 is visible in a raw tap today (predicted, untested on host); `claude agents --json` documents live sessions with reason field | Gave the two concrete "answer owed" surfaces |

**Next on this host (not yet run):** test 1 from F2 — `tmux list-panes -a -F '#{pane_id} #{pane_pid}
#{pane_tty} #{pane_pipe} #{pane_pb_state} #{pane_pb_progress}'` to identify targets and existing
taps. Then test 2 — read `claude agents --json` during a real Claude approval and verify the
reason field appears and clears. These two are read-only and need no release beyond the sandbox
already proposed in seswin-X1.

---

Also noticed: the events-map v0.3 is DRAFT and reversible; it has not been gaveled into flag.md.
The jev envelope convergence question (EM §3) needs a decision before the first production record
writer is coded — it is a cross-repo item.
