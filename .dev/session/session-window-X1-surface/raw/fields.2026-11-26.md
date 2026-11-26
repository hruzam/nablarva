# Status-line field list — 2026-11-26

Versions: Claude Code 2.1.332 · codex-cli 0.172.0 · tmux 3.7c. Every row is PROVISIONAL until a sample has shown, separately, that the field is received and that it is displayed (RUNBOOK step 1).

Source keys: `01` = 01.epoch-claude.return.md · `02` = 02.epoch-codex.return.md · `03` = 03.field-local.return.md · `07` = 07.audit.seswin.return.md · `cfg` = /home/hruzam/.codex/config.toml, lines 23–27 only. Numbers after the key are line numbers in that file. `07` findings are read in Codex release source (DOC); nothing in `07` is observed.

State is the union across both vendors. Per-vendor detail sits in the Claude and Codex cells.

## Fields

| field | Claude (key or "not documented") | Codex (status item, hook field or "not documented") | how fresh | state | source |
|---|---|---|---|---|---|
| model and effort | model: `model.display_name`, `model.id`; effort: `effort.level`, absent if the model lacks effort; script reads both, effort falls back to settings `effortLevel` | status items `model-with-reasoning` (model, effort and optional processing-tier label) and `reasoning` (effort alone), selectable independently; hook `model`; `model-with-reasoning` in cfg | Claude: on new assistant message, `/compact`, permission-mode change, vim toggle, `command` change, `refreshInterval` tick; effort is session-set. Codex: footer recomputes on events (see Display) | DOC+SCRIPT+CONFIG | 01:13, 01:17, 01:21-22; 02:14, 02:18, 02:30; 03:11, 03:24; 07:9, 07:24, 07:25; cfg:27 |
| working directory | `workspace.current_dir` (= `cwd`); `workspace.project_dir` = launch dir; script reads `.workspace.current_dir // .cwd`, `~` substituted | status item `current-dir`; hook `cwd`; notify `cwd`; `current-dir` in cfg | Claude: as model row. Codex: footer recomputes on events; hook `cwd` arrives per hook event | DOC+SCRIPT+CONFIG | 01:13, 01:41, 01:21-22; 02:17, 02:18, 02:31; 03:11, 03:26; 07:11, 07:26; cfg:27 |
| context left | `context_window.remaining_percentage` (may be null early); script shows integer percent, "?" if absent | status item `context-remaining` (footer and title); `/status` context usage; not in hooks or notify; `context-remaining` in cfg (both lists) | Claude: from the most recent API response, so it lags until the next response. Codex: reflects the latest token report; idle footer may keep its last value | DOC+SCRIPT+CONFIG | 01:14, 01:22, 01:43; 02:12, 02:32; 03:12, 03:22, 03:27; 07:11, 07:30; cfg:26-27 |
| session name | `session_name` (custom or AI title; absent otherwise); script reads `.session_name // .session.name`, "-" if absent, re-read every render | `thread-name` (present only if a name exists; may disappear when unnamed); `thread-title` (alias `thread`; falls back to the ID); `/rename` sets the name; both in cfg | Claude: as model row; re-read every render. Codex: recomputes on thread rename (see Display) | DOC+SCRIPT+CONFIG | 01:13, 01:14, 01:44; 02:33; 03:13, 03:17, 03:28; 07:11, 07:43, 07:44, 07:59; cfg:26-27 |
| session id | `session_id`; script reads `.session_id`, dim colour | `thread-id` (UUID once assigned; alias `session-id`); hook `session_id`; notify `thread-id`; `/status` "chat ID"; `thread-id` in cfg | Claude: as model row. Codex: hook fields arrive per hook event | DOC+SCRIPT+CONFIG | 01:13, 01:45; 02:12, 02:17, 02:18; 03:14, 03:30; 07:40, 07:59; cfg:27 |
| transcript path | `transcript_path`; script reads `.transcript_path`, dim, `~` substituted | hook `transcript_path` (string or null), a separate consumer (02:35, 07:9); no status or title picker offers a transcript or rollout path; feedback screen shows the rollout filename if known; `/rollout` prints the full path only in debug-assertion builds (07:9) | Claude: as model row. Codex: per hook event | DOC+SCRIPT | 01:13, 01:46; 02:35; 03:15, 03:31; 07:9 |
| clock and timers | clock: not documented as a field (no wall-clock key; `date +%s` must come from the script). Timers: `cost.total_duration_ms` (session running time); `rate_limits.*.resets_at` and `prompt_cache.expires_at` (epoch seconds); `refreshInterval` (min 1 s) | no clock, chess clock, countdown or poke item in either selector (07:13); working indicator shows elapsed time separately; rate-limit reset timestamps available to providers | Claude: `refreshInterval` timer; also fires when a rate-limit `resets_at` or warm cache `expires_at` is reached. Codex: rate-limit polling and headline schedules (see Display) | DOC+NOT KNOWN | 01:18, 01:22, 01:47, 01:48; 07:11, 07:13; 03:33-35 |
| poke status | not documented | not documented; no project poke receipt item in either selector (07:13) | not documented | NOT KNOWN | 03:33-35 (no poke field in any file read); cfg:26-27 (no poke item); 07:13 |
| alerts | no alert primitive; only thresholds the script computes (doc example: green <70, yellow 70–89, red 90+); not documented as a field | notification channels: `tui.notifications`, `notification_method` (auto/osc9/bel), `notification_condition` (unfocused/always); `notify` on `agent-turn-complete` only; hook `systemMessage` shown as a UI warning; footer `workspace-headline` (Enterprise); title `activity` shows an action-required signal | Claude: thresholds computed each run. Codex: `notify` on `agent-turn-complete` only; condition filter applies to notifications | DOC+NOT KNOWN | 01:19, 01:21, 01:49; 02:17, 02:18, 02:19, 02:37; 07:13, 07:55, 07:57; 03:33-35 |

## Display

**Claude**
- Multiline: "Multiple lines: each echo or print statement displays as a separate row." No maximum line count: not documented (01:25).
- Wider than pane: "To keep a line from being cut off with …, make it at least four columns narrower than the terminal." Tips say "long output may get truncated or wrap awkwardly" (01:26). Wrap versus cut is not stated definitively (01:51). The local script prints one line through a single `printf` with no wrapping or `COLUMNS` input (03:16) and no `…` logic (03:18).
- Refresh: event-driven, plus optional `refreshInterval` (min 1 s); debounced at 300 ms; a new trigger cancels the in-flight script (01:22). Output shows only after exit code 0; otherwise a blank line (01:22). Idle sessions "can go quiet" and fields can be stale (01:22).
- Colour: ANSI escape codes and OSC 8 links. "Multi-line status lines with escape codes are more prone to rendering issues" (01:27).
- Notifications "share the row outside fullscreen rendering and move to a row below when they do not fit" (01:28).

**Codex** (DOC, from release source, 07)
- Multiline: the footer joins its configured values in order into one logical line; if that exceeds the columns and several rows are available, it wraps (07:7). The composer shares a budget of up to four rows with hints; the upstream test expects four or three status rows in fullscreen and two or one inline, depending on the mode indicator (07:7).
- Wider than pane: with one row available, or with more content than the allotted rows can hold, the renderer truncates with an ellipsis (07:7).
- Refresh: the footer recomputes on selection changes, thread renames, turn transitions, completed Git lookups and rate-limit reports; an idle footer can keep its last value (07:11). Other schedules: rate-limit polling at 60, 30, 15 or 5 seconds by consumption; the workspace headline every five minutes when eligible (07:11).
- Placement: `tui.status_line` selects built-in items; an empty selection disables status content; TOML has no `null` literal (07:15). When unset, the footer defaults to `model-with-reasoning`, `current-dir`, `thread-name`, and the title to `activity`, `thread-name`, `project-name` (07:15). 02:12 gives a different footer default (`model-with-reasoning`, `context-remaining`, `current-dir`); this is unresolved.
- Configured IDs: all six footer IDs and all five title IDs in cfg:26-27 are canonical (07:9).

**Codex MCP status-line provider** (row-independent; a separate interface)
- Codex 0.172.0 also has an MCP status-line provider (07:5, DOC). It is separate from `tui.status_line`. #62387 exposes it in `/experimental`; the connected app server supplies its flag at TUI startup, and after a restart `/statusline` can select a provider (07:5). Whether a sample must change a setting first is not stated there. [lead's correction: the earlier wording came from the lead's brief, not from 07]
- A local program can supply it over stdio MCP and returns a JSON UI tree. A Claude-style shell command that prints a line is a different interface (07:5).
- Its snapshot carries thread ID and name, cwd, model, optional reasoning level, optional context figures and account limits, and has no rollout path (07:5).
- Its loop takes a fresh snapshot per read, allows one second for the reply, waits one second after success, continues while idle, and stops on error or timeout (07:11).
- Capability alone does not establish receipt in the read-only Codex sample (07:5).

## Codex item ids

The canonical IDs that serve the nine rows. The full table is at 07, "Complete built-in item IDs" (07:17–59, DOC); it is not copied here.
- `model-with-reasoning` (footer and title): model, effort and optional processing-tier label (07:24).
- `reasoning` (footer and title): effort alone (07:25).
- `current-dir` (footer and title) (07:26).
- `context-remaining` (footer and title) (07:30).
- `thread-id` (footer and title): UUID once assigned; alias `session-id` (07:40, 07:59).
- `thread-name` (footer and title): absent when unnamed (07:43).
- `thread-title` (footer and title): alias `thread`; falls back to the ID (07:44, 07:59).
- `run-state` (footer and title): runtime state such as ready, working or thinking (07:29).
- `activity` (title only): spinner while working; action-required signal while blocked (07:57).
- `workspace-headline` (footer only; Enterprise) (07:55).
- `project-name` (footer and title) (07:27).
Transcript and rollout paths, clock and poke have no ID in either selector (07:9, 07:13).

## The open conflict

The Claude docs say each echo is a separate row (01:25). They also imply that a line is cut when it is not at least four columns narrower than the terminal (01:26); the docs do not state wrap versus cut definitively (01:51). The local return reports that the claim "cuts its text with … at the pane width" is a STATUS.md:27 observation from 2026-11-13, not derived from script code, and does not say which vendor's line was seen to cut (03:18-20).

Reading to try at step 3, not a finding: a single over-wide row is not ruled out by the docs, so the multiline promise and a width cut can both hold. For Codex, the footer's wrap and ellipsis behaviour is documented (07:7), so a cut there is a documented truncation once the row budget is known. The conflict becomes real only if a Claude cut hit a row the docs say should stand alone.

## Not known

- Claude: maximum row count for multiline output (01:25).
- Claude: whether over-wide rows wrap or are cut (01:51).
- Claude: the version that introduced effort, `session_name`, multiline, and COLUMNS/LINES (01:34).
- Claude: whether COLUMNS is supplied at 2.1.332 (01:26, 01:34).
- Claude and Codex: poke status (03:33-35; 07:13 for Codex).
- Codex: whether any status line (built-in footer or MCP provider) is received and displayed in a sample; NOT RUN (07 header, 07:5).
- Codex: whether extra width brings `profile` back onto the preceding row; 07:7 gives this as a prediction for the width check, not a tested result.
- Codex: the unset footer default, given the conflict between 07:15 and 02:12.
- Codex: whether hooks can feed the status line (02:18).
