<!-- card.H · @Field synthesis · 2026-10-02
     Sources — 04_LAB = raw.nablarva/oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md
               epoch  = .dev/session/nablarva-X0-restarted/raw/research.epoch.hooks-vs-pty-meaning.2026-10-01.md
               onion  = ia-sync/.dev/session/voice-meetings-01-threshold/meeting-themes/onion-terminal/terminal-onion.study.2026-09-17.md
               tpd    = toolbox/termbrana/research/termbrana.project-definition.md -->
# card.H — Event vocabularies synthesis

## A. §4.13 Normalized event vocabulary
`04_LAB.md:345–360`

`turn_started` · `turn_completed` · `skill_discovered` · `skill_activated` · `instruction_loaded` · `tool_requested` · `tool_started` · `tool_completed` · `file_read` · `file_changed` · `subprocess_started` · `subprocess_completed` · `assistant_text` · `prompt_returned` · `unknown_activity`

Certainty scale `04_LAB.md:170–176`: `confirmed` · `observed` · `correlated` · `inferred` · `unknown`
Each event records `source` and `confidence`; e.g. `"certainty":"observed"` (syscall source, `04_LAB.md:367–378`) vs `"certainty":"inferred"` + float `"confidence":0.91` (correlator source, `04_LAB.md:379–392`).

## B. §4.15 Capability handshake fields
`04_LAB.md:424–434` — adapter publishes; pipeline selects strongest available signal.

Fields: `native_turn_events` (bool) · `native_skill_events` (bool) · `structured_output` (bool) · `pty_required` (bool) · `process_observation` (string; e.g. `"lab-only"`)

## C. Event-to-source mapping

Footnotes: ¹ `epoch.md:L13–L19` + `onion.md:L335–L376`  ² `epoch.md:L21–L27`  ³ `epoch.md:L30–L37`  ⁴ `onion.md:L528–L556`  ⁵ `onion.md:L215–L229`

| Candidate norm. event | CC hook ¹ | Codex hook ² | agy hook ³ | Mux / PTY tap ⁴ | L0/L1 ⁵ |
|---|---|---|---|---|---|
| turn start | `UserPromptSubmit` | `UserPromptSubmit` | `PreInvocation` | viewport change (subscribe/pipe-pane) | — |
| turn end | `Stop` | `Stop` | `Stop` | viewport stable | — |
| tool start | `PreToolUse` | `PreToolUse` | `PreToolUse` | viewport change | new child PID `/proc` |
| tool end | `PostToolUse` | `PostToolUse` | `PostToolUse` | viewport change | `SIGCHLD`; `wait4` |
| tool failed | `PostToolUseFailure` | — | — | — | `wait4` non-zero exit |
| permission/approval requested | `PermissionRequest` | `PermissionRequest` | — (no hook) | viewport-unchanged stall heuristic | — |
| permission denied | `PermissionDenied` | — | — | — | — |
| notification/needs input | `Notification` | — | — | viewport change | — |
| subagent start/stop | `SubagentStart` / `SubagentStop` | `SubagentStart` / `SubagentStop` | — | — | new child PID `/proc` |
| compaction pre/post | `PreCompact` / `PostCompact` | `PreCompact` / `PostCompact` | — | status-line viewport change | — |
| session start/end | `SessionStart` / `SessionEnd` †  | `SessionStart` / `SessionEnd` | — (no hook) | `pane-died` hook / `pane_closed` | `SIGCHLD`; `pidfd` |
| interrupt | — (→ `SessionEnd` or `Stop`) | `Interrupt` | — | `SIGINT` via ISIG | `SIGINT` |
| crash/exit | `StopFailure` / `SessionEnd` | `SessionEnd(reason)` | — | `pane_closed` (subscribe) | `SIGCHLD`; `wait4` |
| stall | `Notification(idle_prompt)` | — | — | viewport-unchanged + process-alive | `/proc/PID/stat` state letter |
| output changed | `MessageDisplay`; `FileChanged` | — | — | `pane_update` (subscribe); `tmux -CC %output` | inotify |
| prompt submitted | `UserPromptSubmit` (same hook as turn start) | `UserPromptSubmit` | — | — | — |
| model switch | `PreModelSwitch` / `PostModelSwitch` | — | — | — | — |
| cwd changed | `CwdChanged` | — | — | `list-panes` polled | `/proc/PID/cwd` polled |
| file changed | `FileChanged` | — | — | — | inotify / fanotify |

† `SessionEnd` confirmed `onion.md:L337`; ⚡ CONFLICT: absent from epoch's fetched CC hook list (`epoch.md:L15`) — re-verify against live docs before relying on it.
⚡ CONFLICT (agy approval gap): no PermissionRequest/Notification hook in agy; approval state approximated only by stall heuristic; cannot distinguish waiting-for-approval from slow tool without transcript or screen — `epoch.md:L63–L64`.

## D. Termbrana provenance grades
`tpd.md:122–127` — verbatim:
- `raw_pty` — future PTY owner only
- `rendered_ansi` — host-rendered representation retaining ANSI styling
- `rendered_text` — host-rendered plain text
- `derived` — structure produced from another record

## E. Minimum rows to derive each discrete state
Per `epoch.md:L57–L64` + `onion.md:L335–L376`:
- **idle** — turn_end (`Stop`) confirms turn finished; stall (`Notification(idle_prompt)`) confirms process alive and waiting. Minimum: turn_end.
- **working** — turn_start (`UserPromptSubmit`) opened; no turn_end yet. Tool start/end rows extend evidence of activity within the turn. Minimum: turn_start (absence of subsequent turn_end).
- **waiting** — permission/approval_requested (`PermissionRequest` CC/CDX; stall heuristic for agy only). Minimum: permission/approval_requested row.
- **exited** — session_end + crash/exit rows. Hooks may not fire on `kill -9` or hang (`epoch.md:L63`); L0 `SIGCHLD`/`pidfd` is the mandatory liveness backstop. Minimum: session_end + L0/L1 confirmation.
