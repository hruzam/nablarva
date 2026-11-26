# Status-line field list — 2026-11-26

Versions: Claude Code 2.1.332 · codex-cli 0.172.0 · tmux 3.7c. Every row is PROVISIONAL until a sample has shown, separately, that the field is received and that it is displayed (RUNBOOK step 1).

Source keys: `01` = 01.epoch-claude.return.md · `02` = 02.epoch-codex.return.md · `03` = 03.field-local.return.md · `cfg` = /home/hruzam/.codex/config.toml, lines 23–27 only. Numbers after the key are line numbers in that file.

State is the union across both vendors. Per-vendor detail sits in the Claude and Codex cells.

## Fields

| field | Claude (key or "not documented") | Codex (status item, hook field or "not documented") | how fresh | state | source |
|---|---|---|---|---|---|
| model and effort | model: `model.display_name`, `model.id`; effort: `effort.level`, absent if the model lacks effort; script reads both, effort falls back to settings `effortLevel` | status item `model-with-reasoning` (name only; documented only partially, semantics not spelled out); hook `model`; `model-with-reasoning` in cfg | Claude: on new assistant message, `/compact`, permission-mode change, vim toggle, `command` change, `refreshInterval` tick; effort is session-set. Codex: not documented | DOC+SCRIPT+CONFIG | 01:13, 01:17, 01:21-22; 02:14, 02:18, 02:30; 03:11, 03:24; cfg:27 |
| working directory | `workspace.current_dir` (= `cwd`); `workspace.project_dir` = launch dir; script reads `.workspace.current_dir // .cwd`, `~` substituted | status item `current-dir`; hook `cwd`; notify `cwd`; `current-dir` in cfg | Claude: as model row. Codex: status item not documented; hook `cwd` arrives per hook event | DOC+SCRIPT+CONFIG | 01:13, 01:41, 01:21-22; 02:14, 02:17, 02:18, 02:31; 03:11, 03:26; cfg:27 |
| context left | `context_window.remaining_percentage` (may be null early); script shows integer percent, "?" if absent | status item `context-remaining`; `/status` context usage; not in hooks or notify; `context-remaining` in cfg (both lists) | Claude: from the most recent API response, so it lags until the next response. Codex: not documented | DOC+SCRIPT+CONFIG | 01:14, 01:22, 01:43; 02:14, 02:32; 03:12, 03:22, 03:27; cfg:26-27 |
| session name | `session_name` (custom or AI title; absent otherwise); script reads `.session_name // .session.name`, "-" if absent, re-read every render | not a documented status item; `/rename` sets it; title item `thread`; `thread-name` in cfg (both lists), ID not enumerated in docs | Claude: as model row; re-read every render. Codex: not documented | DOC+SCRIPT+CONFIG | 01:13, 01:14, 01:44; 02:14, 02:33; 03:13, 03:17, 03:28; cfg:26-27 |
| session id | `session_id`; script reads `.session_id`, dim colour | hook `session_id`; notify `thread-id`; `/status` "chat ID"; status item session-id in prose only; `thread-id` in cfg; exact status item ID string not documented (see Not known) | Claude: as model row. Codex: hook fields arrive per hook event | DOC+SCRIPT+CONFIG | 01:13, 01:45; 02:12, 02:14, 02:17, 02:18; 03:14, 03:30; cfg:27 |
| transcript path | `transcript_path`; script reads `.transcript_path`, dim, `~` substituted | hook `transcript_path` (string or null) only; not in any status item list; not in cfg | Claude: as model row. Codex: per hook event | DOC+SCRIPT | 01:13, 01:46; 02:14, 02:35; 03:15, 03:31 |
| clock and timers | clock: not documented as a field (no wall-clock key; `date +%s` must come from the script). Timers: `cost.total_duration_ms` (session running time); `rate_limits.*.resets_at` and `prompt_cache.expires_at` (epoch seconds); `refreshInterval` (min 1 s) | not documented; no clock or timer item in the status or title lists | Claude: `refreshInterval` timer; also fires when a rate-limit `resets_at` or warm cache `expires_at` is reached. Codex: not documented | DOC+NOT KNOWN | 01:18, 01:22, 01:47, 01:48; 02:21, 02:36; 03:33-35 |
| poke status | not documented | not documented | not documented | NOT KNOWN | 03:33-35 (no poke field in any file read); cfg:26-27 (no poke item) |
| alerts | no alert primitive; only thresholds the script computes (doc example: green <70, yellow 70–89, red 90+); not documented as a field | documented as notifications, not a status item: `tui.notifications`, `notification_method` (auto/osc9/bel), `notification_condition` (unfocused/always); `notify` on `agent-turn-complete` only; hook `systemMessage` shown as a UI warning | Claude: thresholds computed each run. Codex: `notify` on `agent-turn-complete` only; condition filter applies to notifications | DOC+NOT KNOWN | 01:19, 01:21, 01:49; 02:17, 02:18, 02:19, 02:37; 03:33-35 |

## Display

**Claude**
- Multiline: "Multiple lines: each echo or print statement displays as a separate row." No maximum line count: not documented (01:25).
- Wider than pane: "To keep a line from being cut off with …, make it at least four columns narrower than the terminal." Tips say "long output may get truncated or wrap awkwardly" (01:26). Wrap versus cut is not stated definitively (01:51). The local script prints one line through a single `printf` with no wrapping or `COLUMNS` input (03:16) and no `…` logic (03:18).
- Refresh: event-driven, plus optional `refreshInterval` (min 1 s); debounced at 300 ms; a new trigger cancels the in-flight script (01:22). Output shows only after exit code 0; otherwise a blank line (01:22). Idle sessions "can go quiet" and fields can be stale (01:22).
- Colour: ANSI escape codes and OSC 8 links. "Multi-line status lines with escape codes are more prone to rendering issues" (01:27).
- Notifications "share the row outside fullscreen rendering and move to a row below when they do not fit" (01:28).

**Codex**
- Multiline: not documented (02:14).
- Wider than pane: not documented (02:14, 02:25).
- Refresh: not documented for the status line (02:14).
- Placement: `tui.status_line = []` hides the footer; `null` disables it (02:14). `tui.terminal_title` defaults to `["spinner","project"]` (02:14).

## The open conflict

The Claude docs say each echo is a separate row (01:25). They also imply that a line is cut when it is not at least four columns narrower than the terminal (01:26); the docs do not state wrap versus cut definitively (01:51). The local return reports that the claim "cuts its text with … at the pane width" is a STATUS.md:27 observation from 2026-11-13, not derived from script code, and does not say which vendor's line was seen to cut (03:18-20).

Reading to try at step 3, not a finding: a single over-wide row is not ruled out by the docs, so the multiline promise and a width cut can both hold. The conflict becomes real only if the cut hit a row the docs say should stand alone, or if the cut line was the Codex footer, where nothing is documented (02:14).

## Not known

- Claude: maximum row count for multiline output (01:25).
- Claude: whether over-wide rows wrap or are cut (01:51).
- Claude: the version that introduced effort, `session_name`, multiline, and COLUMNS/LINES (01:34).
- Claude: whether COLUMNS is supplied at 2.1.332 (01:26, 01:34).
- Claude and Codex: poke status (03:33-35).
- Codex: multiline and overflow behaviour of the status line (02:14, 02:25).
- Codex: full status-line ID list, and whether `thread-name`, `thread-id`, `profile`, `activity`, `project-name`, `thread-title` in cfg are valid IDs (02:14; cfg:26-27).
- Codex: exact status-item ID string for session id (02:14).
- Codex: whether `/experimental` custom status lines (0.172.0, #62387) are the same mechanism as `tui.status_line` (02:23).
- Codex: status-line refresh timing (02:14).
- Codex: whether hooks can feed the status line (02:18).
- Codex: any clock or timer item (02:21, 02:36).
