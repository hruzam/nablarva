---
research: EVENTS map — the shared event vocabulary for session observation
version: v0.2 · 2026-10-02 · oraculum (task from majkee journal 2026-10-01 §1 item 4 · flag L14 D3 · docket 8) · smoothed with majkee 2026-10-02 · corrected from Epoch vendor catalogue 2026-10-02
status: DRAFT for docket 8 — rows confirmed by majkee as reversible; v1 after first fixture run
vendors (majkee 2026-10-02): FIRST-CLASS Claude Code · Codex CLI — SECOND-LEVEL Gemini CLI (paid API tokens; personal tiers ended 2026-06-18) · agy (Antigravity, Google's wider successor) — CANDIDATE `jev` (different case; reachable via zsh; UI + harness under construction; surface unknown)
sources: card.H · research.epoch.hooks-vs-pty-meaning.2026-10-01 · .dev/research/vendor-events/vendor-events.catalogue.2026-10-02.md · .dev/research/pty-community/pty-observation.prior-art.2026-10-02.md · onion study ch.0/§4 · doc 04 §4.13/§4.15 · termbrana provenance
rule: an event earns a slot only if at least one real source emits it today, or it is the only way to derive one of the four states. Rows nobody can emit are wishes, not events.
---

# EVENTS map v0.2 — 20 events, 4 states

## 0 · Shape of one event (every tap, every CLI)

```
ts · session_id (join key) · event · phase? · source · certainty · grade? · anchor · payload
```

- `source`: `hook` · `record` (on-disk session file) · `mux` (tmux/zellij) · `pty` (raw bytes) · `proc` (/proc, fds) · `kernel` (signals, wait status)
- `certainty` (doc 04 §4.13): `confirmed` · `observed` · `correlated` · `inferred` · `unknown`
- `grade` only when payload carries text (termbrana): `raw_pty` · `rendered_ansi` · `rendered_text` · `derived`
- `anchor`: `{cli_pid, pane, tty}` — the L5↔L1 seam (hook `$PPID` ↔ `pane_tty`/`$ZELLIJ_PANE_ID`). Claude Code's own `~/.claude/sessions/<pid>.json` is keyed by the same PID (Epoch 10-02, undocumented, M).
- `payload`: small; paths over content (#ax5). Final text lives in the record, not in the event.

One writer per session file (study:655). Events are append-only facts; state is derived, never stored.

## 1 · The map

Legend: CC = Claude Code hook · CX = Codex hook · GM = Gemini CLI hook · AG = agy hook · PTY/mux = tap below L5 · L0/L1 = process/kernel. `—` = no source · `?` = not yet researched. Certainty = best available from that source. (S) = Epoch row from a summarizer fetch, capped M — re-read primary before gaveling a field name.

| # | event | CC | CX | GM | AG | PTY / mux | L0 / L1 | base certainty |
|---|---|---|---|---|---|---|---|---|
| 1 | `session_started` | SessionStart | SessionStart | SessionStart (S) | — | new pane with CLI child (registry) | new PID, `/proc` | confirmed / observed |
| 2 | `session_ended` {exited·killed·crashed, code} | SessionEnd (reasons clear·resume·logout·prompt_input_exit·other; sole hook on SIGTERM of `-p`) | SessionEnd(reason) — **missed 3/10 `exec` runs, #49003** | SessionEnd (S) | — | `pane_closed` / `pane-died` | **SIGCHLD · wait4 · pidfd — load-bearing backstop** | confirmed / observed |
| 3 | `turn_started` | UserPromptSubmit | UserPromptSubmit | UserPromptSubmit (S) | PreInvocation | input bytes then viewport change | — | confirmed / inferred |
| 4 | `turn_ended` (+ `last_assistant_message` ref) | Stop | Stop | Stop (S) | Stop {terminationReason, fullyIdle} | viewport stable after activity | — | confirmed / inferred |
| 5 | `turn_failed` {reason} | StopFailure | — | ? | — | — | — | confirmed (CC only) |
| 6 | `interrupted` | — (Esc→Stop? unverified) | Interrupt (≥0.150.0) | ? | — | `0x03` → SIGINT via ISIG | SIGINT delivered | confirmed / observed |
| 7 | `tool_started` {tool} | PreToolUse | PreToolUse | PreToolUse (S) | PreToolUse | viewport change | child PID appears | confirmed / observed |
| 8 | `tool_ended` {ok·failed} | PostToolUse / PostToolUseFailure | PostToolUse | PostToolUse (S) | PostToolUse | — | SIGCHLD · wait4 status | confirmed / observed |
| 9 | `process_spawned` {pid, comm} | — | — | — | — | — | descendant walk tick | observed |
| 10 | `process_exited` {pid, status} | — | — | — | — | — | SIGCHLD · wait4 | observed |
| 11 | `approval_requested` {tool?} | PermissionRequest · `sessions/<pid>.json status=waiting` (record) | PermissionRequest · app-server `waitingOnApproval` (record) | Notification(ToolPermission) (S) — its only waiting signal | **—** (gap) | stall heuristic; BEL / OSC 9/777 if passed through | — | confirmed / **inferred (agy)** |
| 12 | `approval_resolved` {allowed·denied·auto_denied} | allowed ⇒ next PostToolUse (derived); PermissionDenied = **auto mode only**, not a human "no" | derived from next PostToolUse | ? | — | — | — | correlated / confirmed (auto) |
| 13 | `attention_requested` {kind: input·idle·elicitation·other} | Notification(matcher) · Elicitation | — | ? | — | stall | — | confirmed / inferred |
| 14 | `agent_spawned` {agent_id, type} | SubagentStart | SubagentStart | ? | — | — | child PID | confirmed / observed |
| 15 | `agent_stopped` {agent_id} | SubagentStop | SubagentStop | ? | — | — | SIGCHLD | confirmed / observed |
| 16 | `compaction` {phase: pre·post, trigger} | PreCompact / PostCompact | PreCompact / PostCompact | ? | — | status-line change | — | confirmed |
| 17 | `output_changed` | MessageDisplay | — | ? | — | `pane_update` · `-CC %output` · pipe-pane bytes | fdinfo `pos` advancing | observed |
| 18 | `stall` {secs} | Notification(idle_prompt) confirms | — | ? | — | **viewport unchanged N s ∧ process alive** | `/proc/PID/stat` state | inferred |
| 19 | `file_changed` {path} | FileChanged | — | ? | — | — | inotify / fanotify | confirmed / observed |
| 20 | `unknown_activity` | — | — | — | — | bytes moved, unclassified | — | unknown |

**Record sources (state without screen):** CC `~/.claude/sessions/<pid>.json` → `status: busy|idle|waiting|shell` (undocumented; `sessionId` stale after `/clear`, #36213) · CC `claude agents --json` (preview) → `state/status/waitingFor` · Codex rollout JSONL (reverse-engineered, drifts) · Codex app-server `waitingOnApproval` · agy `brain/<uuid>/.system_generated/logs/transcript.jsonl` (third-party).

**Dropped (real emitters, not needed for any state; lab extensions):** `cwd_changed` · `model_switch` (CC ≥2.1.251) · `instruction_loaded` · `skill_discovered/activated` · `prompt_expanded` · `config_changed` · `worktree_*`.

## 2 · The four states — derivation (D3: classify, never comprehend)

| state | from events | minimum | PTY-only fallback (no hooks) |
|---|---|---|---|
| **working** | `turn_started` without later `turn_ended`; `tool_started`/`output_changed` extend evidence | 3 | input bytes seen, viewport changing |
| **waiting** | `approval_requested` or `attention_requested`, unresolved | 11 or 13 | `stall` while process alive — **cannot distinguish approval from slow tool** |
| **idle** | `turn_ended` and no `turn_started` since; `stall` confirms | 4 | viewport stable, no input since last change |
| **exited** | `session_ended` — **always confirmed by L0** (hooks miss `kill -9`, hangs, OOM — and Codex missed 3/10 clean exits) | 2 + L0 | `pane_closed` · pidfd readable |

Per vendor, without screen reading (Epoch 10-02): **CC all 4** · **CX working·waiting·idle, exited needs L0** · **GM all 4 on paper (M, no fixture)** · **AG working·idle only**.

`stall` is an **event** (PTY-sourced, `inferred`), not a state. A state is never stored — recomputed from the last events on read. *(majkee 2026-10-02: agreed, reversible.)*

## 3 · Decisions taken on this map (majkee, 2026-10-02 — reversible unless gaveled into flag)

- `stall` = event, not state.
- `approval_requested` and `attention_requested` stay split.
- **Margin note (majkee):** projecting vendor-specific events into the app is chasing vendors — a race, likely unsustainable; the future may teach otherwise. Base vocabulary stays vendor-neutral; vendor hooks are *sources*, never *words*.
- **Vendor tiers:** first-class Claude Code · Codex; second-level Gemini CLI (paid tokens) · agy; candidate `jev` (zsh-reachable, surface unknown — row pending).
- Multiplexers: tmux · zellij · others — taken into account (loop 1.4).
- Event details must be known for all intended vendors before v1 → vendor catalogue 2026-10-02 (file A) attached.

## 4 · Known gaps → fixtures (carry into lab HYPOTHESES)

- CC: does Esc-interrupt fire `Stop`? · `sessions/<pid>.json` schema stability.
- CX: do rollout files record approvals? · can an interactive TUI attach to app-server? · `exec --json` names from a third-party sheet (official doc 404).
- GM: when did hooks ship? no fixture run yet.
- AG: real payload + config path on the installed version; approval gap.
- `jev`: everything.
- PTY: does any agent CLI emit OSC 133 itself? tmux 3.8 (OSC 133 hook events) still rc. BEL/OSC 9/777 passthrough in tmux.
- tmux pane↔PID join on `pane_tty` vs Zellij `$ZELLIJ_PANE_ID` (study:583) — untested under tmux.
- Summarizer-derived rows (S) — re-read primaries before any field name is gaveled.

## 5 · What this map is not

Not a parser spec, not a schema freeze, not the doc 04 lab vocabulary (that stays richer, for research). It is the ≤20 words every tap must be able to say; the relay (stridulatrix) reads states derived from them, never the screen.
