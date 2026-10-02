---
card: G · onion study + build plan → termpanum adopt/delta check
sources:
  study: /home/hruzam/ia-sync/.dev/session/voice-meetings-01-threshold/meeting-themes/onion-terminal/terminal-onion.study.2026-09-17.md
  plan:  /home/hruzam/ia-sync/.dev/session/voice-meetings-01-threshold/meeting-themes/onion-terminal/build-plan.md
  brief: /home/hruzam/unikuklatrix/nablarva/.dev/session/toolbox-termpanum-00-brief/raw/brief-substrate-for-RUNBOOK.termpanum.2026-10-01.md
date: 2026-10-01
---

## 1. Study chapters (all released)
| Ch | Title | Released | Dominant flags |
|---|---|---|---|
| 0 | The map | yes | [NABLA] [TIMELESS] [MEASURED] [VERIFIED 2026-09-17] |
| 1 | Bedrock: kernel, processes, descriptors, PTY, signals | yes | [TIMELESS] [MEASURED] [NABLA] |
| 2 | The multiplexer | yes (2026-09-18) | [TIMELESS] [VERIFIED 2026-09-17/18] [INFERRED] [NABLA] |
| 3 | The vertical: one byte and one signal, end to end | yes (2026-09-18) | [TIMELESS] [MEASURED] [INFERRED] |
| 4 | The agent CLI: hooks, transcripts, session files | yes (2026-09-17, out of order) | [VERIFIED 2026-09-17] [INFERRED] [NABLA] |
| 5 | The lens rack: architecture, language, routing | yes (2026-09-18) | [NABLA] |
| 6 | The context bus | yes (2026-09-18) | [NABLA] [VERIFIED 2026-09-17] [OPEN] |
| 7 | Reading the board with an AI | yes (2026-09-18) | — |
Flag definitions: study:13-15

## 2. Design rules and PTY (L2)
Three rules [NABLA]: tap high for meaning, tap low for liveness; events are append-only, state is a snapshot; JSONL is truth, board is disposable. study:80-87
PTY can yield: raw byte stream via multiplexer master-read, `script`, or ptrace — push. study:71, study:207-209
PTY cannot yield: stdout/stderr separation ("already merged at L2" study:71), exact bytes written (`\n`→`\r\n` via OPOST study:195), causal meaning ("rendering surface: what you read from the master is what a terminal would paint" study:205 [TIMELESS]), or semantics ("Scraping the PTY for semantics is now strictly worse than subscribing." study:435 [VERIFIED 2026-09-17]).

## 3. Multiplexer (Ch 2) — 3 lines
Detached server owns PTY masters; registry (pane↔tty↔PID) + viewport (rendered grid); "never semantics" [TIMELESS]. study:449, study:481-485
Taps: tmux `pipe-pane` (raw escape stream), `-CC` control mode (line-oriented events), lifecycle hooks; Zellij `subscribe --format json` (NDJSON pane_update/closed, cross-session) [VERIFIED 2026-09-17]. study:530-555
PID↔pane bridge: tmux joins on `pane_tty` string; Zellij exposes `$ZELLIJ_PANE_ID` inherited by hook — "Zellij is the easier target here." [VERIFIED 2026-09-18] study:525, study:583-585

## 4. Context bus (Ch 6) — 3 lines
Two moments: `PreCompact` hook writes checkpoint (facts + last-N turns); `SessionStart` matcher `resume|compact|clear` prints newest checkpoints — stdout injected into context [VERIFIED 2026-09-17]. study:904-909
Bus is `~/.rack/bus/<sid>/`; routing via symlinks in `links/`; every injection logged as event; no broker. study:913-924, study:940-944
[OPEN]: who writes the checkpoint — cheap (copy events.jsonl facts) vs rich (model self-summary at limit = "Last Standing Man" anti-pattern); brief drops the question entirely without resolving it. study:922-935

## 5. Build plan
Phases: 0 ground (repo+probes, no code); 1 v0 sensors (sh+jq, no compilation); 2 v1 Rust picker+board; 3 context bus; 4 other CLIs + Zellij plugin. plan:12-118
sh+jq: sensors (append.sh), pollers (tree/fds/view), readers (tail|jq pipelines), slices. study:679-683; plan:35-75
Rust: ulx-pick (≤300 lines, inotify+keys, atomic write to `selected`) + ulx-board (~400 lines, optional). "A language earns its place only when a component needs residency or a grid." study:683; plan:81-93
Assumptions: Zellij as host; XDG (`~/.config/ulx`, `~/.local/state/ulx`); repo `~/unikuklatrix/unilarvatrix/`. plan:7

## 6. Brief #adopt delta check
| # | Delta | Corresponds to something real? | Contradiction? |
|---|---|---|---|
| 1 | name+home: unilarvatrix/ulx → termpanum at toolbox/termpanum/ | yes — plan:7 names repo explicitly | none |
| 2 | host: Zellij rack → tmux window | feasible (tmux taps documented study:530-539) but study §2.6 verdict is inverted: "Zellij is the easier target" [VERIFIED 2026-09-18] study:583-585; brief flips without citing counter-evidence | ⚡ CONFLICT: study verdict inverted |
| 3 | Phase 3 context bus → stridulatrix | yes — study ch 6 + plan Phase 3 are discrete; handoff is clean | none |
| 4 | Phase 4 hook search for Codex/agy = only external sweep | yes — plan:108-110 | none |
| 5 | events take shared format #ax4, not plan's {kind,src} envelope | yes — plan §5.2 uses {kind,src}; brief extends with certainty/provenance fields | none, genuine extension |
Silent drops (present in sources, absent from brief without contradiction): "v0 is buildable today with zero compilation" study:765; one-writer-per-file invariant study:655; tmux `wait-for` synchronisation primitive study:541.

## 7. "PTY is the base layer; hooks and on-disk records enrich it" — contradiction check
None found. Study §4.0: "You do not scrape; you subscribe. Everything in Chapters 1–3 becomes a cross-check on this stream, not a substitute for it." study:278-280. Brief #ax2 ("hooks and on-disk session records for meaning; PTY, process tree and kernel for liveness") matches exactly. brief:27-29. Brief #falsification-gate proposes stopping PTY tap if hooks cover all states. brief:102-107.

## 8. [OPEN] items (verbatim, study)
- "[OPEN]: drill-down into live things (a pid's fd table) means a detail pane that re-polls on select. That's a poller spawned on demand, i.e. the picker or board must spawn processes." study:714-716
- "Who writes the checkpoint — the honest problem [OPEN]" study:922
