---
research: EVENTS map — the shared event vocabulary for session observation
version: v0.1 · 2026-10-02 · oraculum (task from majkee journal 2026-10-01 §1 item 4 · flag L14 D3 · docket 8) · smoothed with majkee 2026-10-02
status: DRAFT for docket 8 — rows confirmed by majkee 2026-10-02 as reversible; v1 after per-vendor event research + first fixture run
vendors: Claude Code · Codex CLI · Gemini CLI (majkee 2026-10-02 — NOT agy); agy optional, "the app can count with agy also"
sources: card.H (doc 04 §4.13/§4.15 · Claude Code hooks · Codex hooks · agy hooks · onion study §2/§4 · termbrana provenance) · research.epoch.hooks-vs-pty-meaning.2026-10-01 · onion study ch.0 rules
rule: an event earns a slot only if at least one real source emits it today, or it is the only way to derive one of the four states. Rows nobody can emit are wishes, not events.
---

# EVENTS map v0.1 — 20 events, 4 states

## 0 · Shape of one event (every tap, every CLI)

```
ts · session_id (join key) · event · phase? · source · certainty · grade? · anchor · payload
```

- `source`: `hook` · `record` (on-disk session file) · `mux` (tmux/zellij) · `pty` (raw bytes) · `proc` (/proc, fds) · `kernel` (signals, wait status)
- `certainty` (doc 04 §4.13): `confirmed` · `observed` · `correlated` · `inferred` · `unknown`
- `grade` only when payload carries text (termbrana): `raw_pty` · `rendered_ansi` · `rendered_text` · `derived`
- `anchor`: `{cli_pid, pane, tty}` — the L5↔L1 seam (hook `$PPID` ↔ `pane_tty`/`$ZELLIJ_PANE_ID`)
- `payload`: small; paths over content (#ax5). Final text lives in the record, not in the event.

One writer per session file (study:655). Events are append-only facts; state is derived, never stored.

## 1 · The map

Legend: CC = Claude Code hook · CX = Codex hook · GM = Gemini CLI (open — research pass 2026-10-02) · AG = agy hook (optional vendor) · PTY/mux = tap below L5 · L0/L1 = process/kernel. `—` = no source · `?` = not yet researched. Certainty = best available from that source.

| # | event | CC | CX | GM | AG | PTY / mux | L0 / L1 | base certainty |
|---|---|---|---|---|---|---|---|---|
| 1 | `session_started` | SessionStart | SessionStart | ? | — | new pane with CLI child (registry) | new PID, `/proc` | confirmed / observed |
| 2 | `session_ended` {exited·killed·crashed, code} | SessionEnd † | SessionEnd(reason) | ? | — | `pane_closed` / `pane-died` | **SIGCHLD · wait4 · pidfd — mandatory backstop** | confirmed / observed |
| 3 | `turn_started` | UserPromptSubmit | UserPromptSubmit | ? | PreInvocation | input bytes then viewport change | — | confirmed / inferred |
| 4 | `turn_ended` (+ `last_assistant_message` ref) | Stop | Stop | ? | Stop | viewport stable after activity | — | confirmed / inferred |
| 5 | `turn_failed` {reason} | StopFailure | — | ? | — | — | — | confirmed (CC only) |
| 6 | `interrupted` | — (→ Stop/SessionEnd) | Interrupt | ? | — | `0x03` → SIGINT via ISIG | SIGINT delivered | confirmed / observed |
| 7 | `tool_started` {tool} | PreToolUse | PreToolUse | ? | PreToolUse | viewport change | child PID appears | confirmed / observed |
| 8 | `tool_ended` {ok·failed} | PostToolUse / PostToolUseFailure | PostToolUse | ? | PostToolUse | — | SIGCHLD · wait4 status | confirmed / observed |
| 9 | `process_spawned` {pid, comm} | — | — | — | — | — | descendant walk tick | observed |
| 10 | `process_exited` {pid, status} | — | — | — | — | — | SIGCHLD · wait4 | observed |
| 11 | `approval_requested` {tool?} | PermissionRequest | PermissionRequest | ? | **—** (gap) | stall heuristic only | — | confirmed / **inferred (agy)** |
| 12 | `approval_resolved` {allowed·denied} | PermissionDenied; allow ⇒ next PostToolUse | — (derived) | ? | — | — | — | confirmed / correlated |
| 13 | `attention_requested` {kind: input·idle·elicitation·other} | Notification(matcher) · Elicitation | — | ? | — | stall | — | confirmed / inferred |
| 14 | `agent_spawned` {agent_id, type} | SubagentStart | SubagentStart | ? | — | — | child PID | confirmed / observed |
| 15 | `agent_stopped` {agent_id} | SubagentStop | SubagentStop | ? | — | — | SIGCHLD | confirmed / observed |
| 16 | `compaction` {phase: pre·post, trigger} | PreCompact / PostCompact | PreCompact / PostCompact | ? | — | status-line change | — | confirmed |
| 17 | `output_changed` | MessageDisplay | — | ? | — | `pane_update` · `-CC %output` · pipe-pane bytes | fdinfo `pos` advancing | observed |
| 18 | `stall` {secs} | Notification(idle_prompt) confirms | — | ? | — | **viewport unchanged N s ∧ process alive** | `/proc/PID/stat` state | inferred |
| 19 | `file_changed` {path} | FileChanged | — | ? | — | — | inotify / fanotify | confirmed / observed |
| 20 | `unknown_activity` | — | — | — | — | bytes moved, unclassified | — | unknown |

† CC `SessionEnd`: present in the onion study (study:337), absent from Epoch's fetched list — re-verify against live docs before relying on it. Until then `session_ended` for CC rests on L0.

**Dropped (real emitters, but not needed for any state; lab extensions, not base):** `cwd_changed` · `model_switch` · `instruction_loaded` · `skill_discovered/activated` · `prompt_expanded` · `config_changed` · `worktree_*`. They re-enter as lab research events (doc 04), never as base vocabulary.

## 2 · The four states — derivation (D3: classify, never comprehend)

| state | from events | minimum | PTY-only fallback (no hooks) |
|---|---|---|---|
| **working** | `turn_started` without later `turn_ended`; `tool_started`/`output_changed` extend evidence | 3 | input bytes seen, viewport changing |
| **waiting** | `approval_requested` or `attention_requested`, unresolved | 11 or 13 | `stall` while process alive — **cannot distinguish approval from slow tool** |
| **idle** | `turn_ended` and no `turn_started` since; `stall` confirms | 4 | viewport stable, no input since last change |
| **exited** | `session_ended` — **always confirmed by L0** (hooks do not fire on `kill -9`, hang, OOM) | 2 + L0 | `pane_closed` · pidfd readable |

`stall` is an **event** (PTY-sourced, `inferred`), not a state: it is the base layer's own contribution and the only idle/waiting signal for a hook-less CLI. A state is never stored — it is recomputed from the last events on read. *(majkee 2026-10-02: agreed, reversible.)*

## 3 · Decisions taken on this map (majkee, 2026-10-02 — reversible unless gaveled into flag)

- `stall` = event, not state.
- `approval_requested` and `attention_requested` stay split — approval defines `waiting` and has a hook on two vendors.
- **Margin note (majkee):** projecting vendor-specific events into the app is chasing vendors; the race looks unsustainable — the future may teach otherwise. Keep the base vocabulary vendor-neutral; vendor hooks are *sources*, never *words*.
- agy was out of scope; the app can count with it as an optional vendor. Target set = Claude Code · Codex · Gemini CLI.
- Event details must be known for all intended vendors before v1 → per-vendor research pass opened 2026-10-02 (`.dev/research/vendor-events/`).

## 4 · Known gaps (carry into HYPOTHESES)

- **Gemini CLI column empty** — research pass 2026-10-02.
- **agy approval gap** — no permission/notification hook; `waiting` only by stall; fixture needed if agy is kept.
- **CC SessionEnd** — source conflict; verify.
- **Codex rollout JSONL** — reverse-engineered, event names drift; `record` source for Codex is `correlated` at best.
- **Hooks never fire on crash** — L0 backstop is not optional for any CLI.
- **tmux pane↔PID join** on `pane_tty` string vs Zellij `$ZELLIJ_PANE_ID` (study:583) — reliability untested under tmux (loop 1.4).

## 5 · What this map is not

Not a parser spec, not a schema freeze, not the doc 04 lab vocabulary (that stays richer, for research). It is the ≤20 words every tap must be able to say; the relay (stridulatrix) reads states derived from them, never the screen.
