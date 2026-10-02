# Vendor event catalogue — Claude Code · Codex CLI · Gemini CLI · agy
Date: 2026-10-02 (all "live-verified" = fetched this run, 2026-10-02)
Author: @Epoch · Triggered by: events-map.v0.2026-10-02.md (20 events, 4 states), docket 8
Extends/corrects: research.epoch.hooks-vs-pty-meaning.2026-10-01.md
Caveat: WebFetch returns small-model summaries, not verbatim pages. Rows marked (S) = summary-level; re-read primary before gaveling. Confidence H = vendor doc/changelog read this run; M = third party / secondary / summary-only; L = inferred.

## 0. Headline corrections to the predecessor note and to map v0.1

| # | Claim in predecessor / map | Verdict 2026-10-02 | Source | Conf |
|---|---|---|---|---|
| C1 | CC `SessionEnd` absent from list (map footnote †) | **WRONG. SessionEnd exists.** 33 events total (predecessor's 32 + SessionEnd). Cannot block; matcher = reason `clear`, `resume`, `logout`, `prompt_input_exit`, `other`. Runs on SIGTERM of `claude -p` (exit 143). | https://code.claude.com/docs/en/hooks · https://code.claude.com/docs/en/headless · https://code.claude.com/docs/en/sessions ("A `SessionEnd` hook can archive the transcript") | H |
| C2 | map row 12: CC `PermissionDenied` = approval denied | **Narrower:** fires when **auto mode** denies a tool call (classifier), not when a human presses "no". Human allow/deny has no dedicated hook; allow ⇒ next PostToolUse, human deny ⇒ PostToolUseFailure/none (L, unverified). | hooks doc table "PermissionDenied: Auto mode denies tool call" | H (event def) / L (human deny path) |
| C3 | agy hook config path conflict | **Resolved by official doc:** global `~/.gemini/config/hooks.json`; workspace `<root>/.agents/hooks.json`; plugin-level hooks. `<app_data_dir>` for CLI = `~/.gemini/antigravity-cli`. The `~/.gemini/antigravity-cli/hooks.json` (Medium/gist) is likely stale or app-data-relative. | https://antigravity.google/docs/hooks/ (S) | M-H |
| C4 | agy payload snake_case (`session_id`, `transcript_path`) | Official doc says camelCase: `conversationId`, `workspacePaths`, `transcriptPath`, `artifactDirectoryPath`, `modelName`; PreToolUse adds `toolCall`, `stepIdx`; **Stop adds `terminationReason`, `fullyIdle`**. Fixture must dump a real payload. | same (S) | M |
| C5 | Gemini CLI = dead / agy is successor (map: "Gemini CLI (NOT agy)") | **Half true.** Consumer/personal access to Gemini CLI ended 2026-06-18; the repo is alive, Apache-2.0, still shipping (stable v0.62.0 on 2026-09-29). See §3.0. | links in §3.0 | H |
| C6 | Codex hook events = 12, stable | Confirmed 12 (§2a). `Interrupt` added in **0.150.0 (2026-08-26)** per secondary sources — the only hook-surface change in the last 90 days across Codex. | §2a | M |
| C7 | CC has no PTY-free live status file | **There is an undocumented one:** `~/.claude/sessions/<pid>.json` with `status` busy/idle/waiting/shell (+reason). Directory is mentioned in official docs ("one small file per running session, used to detect concurrent sessions and crashes") but the schema is not. Plus documented `claude agents --json` (research preview) with `state`/`status`/`waitingFor`. See §1b/§1d. | docs below | M (file) / H (agents --json existence) |
| C8 | Codex `StopFailure`/`Notification` | Not in Codex's documented 12. A third-party catalog (purdex PR #1172, codex-cli 0.153.4) lists both as "ignored/retired" — treat as **none**. | §2a | M |

## 1. Claude Code (v2.1.287, 2026-10-01 — changelog fetched)

### 1a. Hook events (live-verified, https://code.claude.com/docs/en/hooks, 2026-10-02) — H

Config: `~/.claude/settings.json` · `.claude/settings.json` · `.claude/settings.local.json` · managed policy · plugin `hooks/hooks.json` · skill/subagent frontmatter. Cloud sessions do not read `~/.claude/settings.json`. Stability: no label on hooks; only `type:"agent"` hooks are labelled experimental.

Common input (all events): `session_id`, `prompt_id` (v2.1.196+), `transcript_path`, `cwd`, `scratchpad_dir` (v2.1.257+), `permission_mode`, `effort.level`, `hook_event_name`; in subagent also `agent_id` (v2.1.266+), `agent_type`.

| Event (exact) | Fires | Extra payload (documented) | Blocks? |
|---|---|---|---|
| Setup | `--init-only`, `-p --init/--maintenance` | `trigger` | no |
| SessionStart | new/resume/clear/compact/fork | `source`, `model`, `agent_type`, `session_title`, `seconds_since_last_response`, `context_tokens`, `prompt_cache_likely_expired`, `estimated_cache_write_usd` (last four v2.1.251+) | no |
| **SessionEnd** | session terminates | reason via matcher: clear/resume/logout/prompt_input_exit/other | no |
| InstructionsLoaded | CLAUDE.md/rules loaded | `file_path`, `memory_type`, `load_reason`… | no |
| ConfigChange | config changes | matcher = source | yes |
| UserPromptSubmit | user submits prompt | `user_input` | yes |
| UserPromptExpansion | slash command expands | `command_name` | yes |
| PreToolUse | before tool | `tool_name`, `tool_input`, `tool_use_id` | yes |
| PermissionRequest | tool needs permission decision | tool_name/tool_input/tool_use_id | no (decision via `decision.behavior`) |
| PermissionDenied | **auto mode** denies | tool fields; `retry:true` | no |
| PostToolUse / PostToolUseFailure | after success / failure | tool fields + result/error | yes |
| PostToolBatch | after parallel batch | — | yes |
| MessageDisplay | assistant message streams | display-only `displayContent` | no |
| Notification | CC sends notification | `notification_type` (permission_prompt, idle_prompt, auth_success, elicitation_dialog, …), `message` | no |
| SubagentStart / SubagentStop | subagent lifecycle | `agent_type`; Stop adds `last_assistant_message` | stop: yes |
| TaskCreated / TaskCompleted / TeammateIdle | agent-teams tasks | — | yes |
| Stop | Claude finishes responding | `last_assistant_message` (+ `stop_reason` per predecessor, not re-seen in this fetch) | yes |
| StopFailure | turn ends on API error | `error_type` ∈ rate_limit, overloaded, authentication_failed, oauth_org_not_allowed, account_on_hold, billing_error, invalid_request, model_not_found, server_error, max_output_tokens, cloud_credential_error (v2.1.267+), unknown | no |
| PreCompact / PostCompact | around compaction | matcher manual/auto | pre: yes |
| CwdChanged · DirectoryAdded · FileChanged · WorktreeCreate · WorktreeRemove | misc | `file_path` / `worktree_path` | mixed |
| PreModelSwitch / PostModelSwitch | model switch | `from_model`, `to_model` | pre: yes |
| Elicitation / ElicitationResult | MCP elicitation | `server_name`, `elicitation_id`, `form_schema` | yes |

Version/date history (secondary, M): MessageDisplay v2.1.152 (≈2026-05-26); Pre/PostModelSwitch v2.1.251 (≈2026-08-28) — source: web-search digest of https://github.com/gabriel-dehan/claude_hooks/issues/64 and changelog mirrors, not read directly.
**Added/renamed in last 90 days (since ≈2026-07-04):** PreModelSwitch/PostModelSwitch (v2.1.251, M). New payload fields: `scratchpad_dir` 2.1.257, `agent_id` 2.1.266, `cloud_credential_error` 2.1.267 (H, hooks doc). No renames found. Latest changelog items (2.1.281–2.1.287, 2026-09-23..10-01) are hook bug-fixes only: `asyncRewake` hooks no longer re-wake repeatedly on missing script (2.1.287); sync hooks no longer hang on background process holding output (2.1.285); failed-hook stderr kept (2.1.283) (S, https://code.claude.com/docs/en/changelog).
Reliability notes (H, headless doc): on SIGTERM of `claude -p`, only `SessionEnd` runs; turn left unfinished with no result recorded. Hooks do not fire on `kill -9`/hang (inferred, L).

### 1b. On-disk session record

| Item | Value | Source | Documented? | Conf |
|---|---|---|---|---|
| Transcript path | `~/.claude/projects/<project>/<session-id>.jsonl`; `<project>` = cwd with non-alphanumerics → `-` (>200 chars: truncated + hash). Move with `CLAUDE_CONFIG_DIR`; name with `CLAUDE_CODE_PROJECT_DIR_NAME` (v2.1.234+). 30-day default (`cleanupPeriodDays`). | https://code.claude.com/docs/en/sessions | **Path documented; entry format explicitly "internal… changes between versions"** | H |
| Hook hands the path | `transcript_path` in every hook | hooks doc | yes | H |
| Contents | one JSON object per message / tool use / metadata entry; `-p`/SDK sessions are written too (hidden from picker) | sessions doc | partly | H |
| Suppress | `--no-session-persistence` (with `-p`), `CLAUDE_CODE_SKIP_PROMPT_HISTORY` | sessions doc | yes | H |
| Write lag | "saved continuously"; not measured. A tool running at crash is recorded as cut off at resume. | sessions doc | — | M |
| Pending permission prompt in file | NOT verified | — | — | L |
| **Per-PID live status file** | `~/.claude/sessions/<pid>.json`: `pid`, `sessionId`, `cwd`, `startedAt` (ms) (+ `status` busy/idle/waiting-with-reason/shell, `procStart`, `bridgeSessionId` per third parties). Used by third-party tools; docs say only "one small file per running session… detect concurrent sessions and crashes". **`sessionId` not updated on `/clear`** (issue #36213, closed not planned; #95439 same class). Schema "observed v2.1.178 / v2.1.284". | https://code.claude.com/docs/en/claude-directory (S, grep of fetched page) · https://github.com/anthropics/claude-code/issues/36213 · https://github.com/rorhcdream/tmux-agent-status · web-search digest of CircuitFlow-io/ng-dev-tools#13, brandon-fryslie/cc-hands#14 | **dir mentioned, schema undocumented** | M |
| Background-session state | `~/.claude/jobs/<id>/state.json`, `~/.claude/daemon/roster.json` | https://code.claude.com/docs/en/agent-view (S) | documented, research preview | M-H |

### 1c. Headless / structured output (H, https://code.claude.com/docs/en/headless)

| Mode | Stream / event names |
|---|---|
| `claude -p --output-format text|json|stream-json` | json: result + `session_id` + usage/cost; `--json-schema` → `structured_output` |
| `stream-json` (+`--verbose`, `--include-partial-messages`) | NDJSON: `system/init` (first; carries `capabilities[]`, `plugins`, `plugin_errors`, `mcp_servers`, `mcp_server_errors`), `assistant`, `user` (with `parent_tool_use_id` for subagents), `stream_event` (partial deltas), `system/api_retry`, `system/plugin_install`, `hook_started`/`hook_progress`/`hook_response` (SessionStart/Setup hooks; SDK message types), `permission_denied` system messages, final `result` (with `permission_denials`). |
| Exit | 0 ok / non-zero fail; SIGTERM → 143 (+SessionEnd) |
| Related | `--bare` (no hooks/skills/MCP discovery; to become default for `-p`), `--resume <id|path.jsonl>`, `--permission-prompts none` (v2.1.259+), `--forward-subagent-text` (v2.1.211+) |

### 1d. Push / wake doors

| Door | Status | Version/date | Source | Conf |
|---|---|---|---|---|
| Channels (`--channels plugin:…`; MCP server pushes events into a running session; permission-relay capability) | **Research preview**; flags hidden from `--help`; allowlist-gated; needs claude.ai/Console auth (not Bedrock/Vertex/Foundry); Team/Enterprise admin must enable (`channelsEnabled`) | no min version stated | https://code.claude.com/docs/en/channels | H |
| Remote Control (claude.ai/app drives local session; outbound relay, not a local socket) | shipped; fixes through 2.1.287 | 2.1.283–2.1.287 changelog | https://code.claude.com/docs/en/remote-control · changelog (S) | H (exists) / not usable as local API |
| Agent view / background sessions (`claude --bg`, `claude agents --json`, `attach`, `logs`, `stop`, `respawn`, supervisor daemon) | **Research preview**; `agents --json` fields: `id`, `sessionId`, `pid`, `cwd`, `kind`, `state` (working/blocked/done/failed/stopped), `status` (busy/waiting/idle), `waitingFor` (permission prompt / input needed / sandbox request / worker request / dialog open) | v2.1.212+ recommended, 2.1.257+ supervisor reliability | https://code.claude.com/docs/en/agent-view (S) | M-H |
| `claude -p --resume <bg-session> "prompt"` queues next turn into a running bg session | documented | ≥2.1.285 | https://code.claude.com/docs/en/sessions | H |
| Hook `asyncRewake` (hook can wake Claude) | mentioned only in changelog fix 2.1.287 | — | changelog (S) | L |
| ACP | Not offered natively per agy issue #31 text ("claude … already provide" ACP — via adapter, unverified) | — | https://github.com/google-antigravity/antigravity-cli/issues/31 | L |

### 1e. Mapping — 20 events → Claude Code
Emitter: hook / record / file (sessions/<pid>.json) / agents-json / none.

| # | event | emitter | cert | note |
|---|---|---|---|---|
| 1 | session_started | SessionStart(source) | H | `source` startup/resume/clear/compact/fork — `clear` = new session id under same pid |
| 2 | session_ended | SessionEnd(reason) | H | reason ≠ exited/killed/crashed; no code. L0 backstop mandatory |
| 3 | turn_started | UserPromptSubmit | H | |
| 4 | turn_ended | Stop (+`last_assistant_message`) | H | |
| 5 | turn_failed | StopFailure(error_type) | H | CC-only |
| 6 | interrupted | none dedicated | L | Esc behaviour vs Stop not verified this run — fixture |
| 7 | tool_started | PreToolUse | H | |
| 8 | tool_ended | PostToolUse / PostToolUseFailure | H | |
| 9/10 | process_spawned/exited | none | — | L0 only |
| 11 | approval_requested | PermissionRequest; Notification(permission_prompt) | H | plus `sessions/<pid>.json` waiting (M) and `agents --json` waitingFor (M) |
| 12 | approval_resolved | derived (PostToolUse / PostToolUseFailure); PermissionDenied only for auto-mode | M | correction C2 |
| 13 | attention_requested | Notification(idle_prompt, elicitation_dialog, auth_success…) · Elicitation | H | |
| 14/15 | agent_spawned/stopped | SubagentStart / SubagentStop (`agent_id` v2.1.266+) | H | |
| 16 | compaction | PreCompact / PostCompact | H | |
| 17 | output_changed | MessageDisplay | M | display-only hook; ≈v2.1.152 |
| 18 | stall | Notification(idle_prompt) (confirms) | M | timing semantics of idle_prompt not read |
| 19 | file_changed | FileChanged | H | **only for watched filenames** (exact strings), not general FS |
| 20 | unknown_activity | none | — | |

**States without screen reading:** working ✔ (UserPromptSubmit…Stop; H) · waiting ✔ (PermissionRequest / Notification; H) · idle ✔ (Stop; H) · exited ✔ (SessionEnd H + L0 for kill -9). **All 4: YES.** Extra non-hook path: `claude agents --json`, `sessions/<pid>.json` (M, version-fragile).

### 1f. SessionEnd re-verification (asked explicitly)
**YES — Claude Code has a `SessionEnd` hook today.** Evidence: https://code.claude.com/docs/en/hooks (fetched 2026-10-02: listed in event table, "Decision control: No control: … SessionEnd", section "SessionEnd"); https://code.claude.com/docs/en/headless ("Claude Code then runs `SessionEnd` hooks and exits" on SIGTERM); https://code.claude.com/docs/en/sessions ("A `SessionEnd` hook can archive the transcript"). Three independent doc pages. Confidence H. Cause of predecessor's miss: summarizer dropped the last table row.

## 2. OpenAI Codex CLI (stable 0.160.0, 2026-10-01; alpha 0.162.0-alpha.1)
Release source: https://github.com/openai/codex/releases (S, H-ish).

### 2a. Hook events
Doc: https://learn.chatgpt.com/docs/hooks (308-redirect from developers.openai.com/codex/hooks), fetched 2026-10-02 (S).

| Event | When | Notes |
|---|---|---|
| SessionStart | session begin | `source`; additionalContext supported |
| SessionEnd | session end | `reason`; **1 s default timeout, 3 s cap** (M) |
| UserPromptSubmit | prompt submitted | turn events carry `turn_id` (predecessor) |
| PreToolUse / PermissionRequest / PostToolUse | tool lifecycle | `tool_name`, `tool_input`, `tool_use_id`; Post adds `tool_response`. PermissionRequest may allow/deny/**decline** → normal prompt continues |
| PreCompact / PostCompact | compaction | |
| SubagentStart / SubagentStop | subagents | SubagentStop: `last_assistant_message`, `agent_transcript_path`, `stop_hook_active` |
| Stop | turn end | `last_assistant_message`, `stop_hook_active` |
| **Interrupt** | active top-level turn interrupted; **main thread only, never subagents**; 1 s default / 3 s cap | added **0.150.0 (2026-08-26)** per search digest (M) |

12 events. Common fields: `session_id`, `cwd`, `hook_event_name`, `model` (+ `transcript_path` nullable, `permission_mode`, `turn_id` per predecessor). Config: `~/.codex/hooks.json` or `[hooks]` in `~/.codex/config.toml`; `<repo>/.codex/hooks.json` / `.codex/config.toml`; plugin hooks; managed (`requirements.toml`/MDM, cannot be disabled). Layers add, not replace. **Trust gate:** non-managed hooks skipped until reviewed (`/hooks`), trust bound to hook hash — changed hook ⇒ silently not run. Feature flag now `features.hooks=true` (old `codex_hooks` dropped) — third-party, purdex PR #1172 for 0.153.4 (M-L). Stability: documented as current; "transcript format isn't a stable interface for hooks" (H, doc). Stable since v0.124.0 (2026-04-23, secondary M; carried from predecessor). 0.158.0 (2026-09-28): "native POSIX spawning for command hooks" (changelogs.info, S, M).
**Added/renamed in last 90 days:** `Interrupt` (0.150.0, 2026-08-26). Nothing else found.
**Reliability:** `SessionEnd` missed in 3/10 `codex exec` runs on macOS 0.158.0 (5 s shutdown budget consumed by FSEvents teardown) — https://github.com/openai/codex/issues/49003 (S). ⇒ SessionEnd is **not** a trustworthy exit signal; L0 mandatory (H-M).
Hook-less notify channels (M): `notify = [...]` external program fires **only `agent-turn-complete`**; `[tui] notifications = ["agent-turn-complete","approval-requested"]`, `notification_method = auto|osc9|bel` → OSC 9/BEL written to the PTY (https://developers.openai.com/codex/config-advanced; digest via https://codex.danielvaughan.com/2026/04/10/codex-cli-agent-notifications-desktop-alerts-monitoring/).

### 2b. On-disk session record
| Item | Value | Source | Documented? | Conf |
|---|---|---|---|---|
| Path | `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl` | https://github.com/rorhcdream/tmux-agent-status (observed) · predecessor sources | **No** (hook doc: transcript format not stable) | M |
| Format | line = `{timestamp, type, payload}`; types `session_meta`, `turn_context`, `response_item`, `event_msg`, `compacted`; names drift vs `protocol.rs` (v0.130.0 study) | https://dev.to/milkoor/reverse-engineering-codex-cli-rollout-traces-3b9b | reverse-engineered | M |
| Turn-boundary markers observed by third party | `task_started` → working, `task_complete` → done, `turn_aborted` → cleared (tmux-agent-status derives status this way); `event_msg/item_completed` carries UserMessage/AgentMessage/CommandExecution on 0.158 | tmux-agent-status README; hindsight#4423 digest | observed | M |
| Approval persisted? | still **UNVERIFIED** (open question in vouchington/vouchington#1203) | — | — | L |
| Write lag | unknown; append-only | — | — | L |
| PID↔file join | no per-pid file; third parties use `lsof` on the rollout fd; shared app-server clients break the join | tmux-agent-status | — | M |

### 2c. Headless / structured
| Mode | Names | Source | Conf |
|---|---|---|---|
| `codex exec --json` (JSONL) | `thread.started`(thread_id) · `turn.started` · `turn.completed`(usage) · `turn.failed`(error.message) · `item.started/updated/completed` · `error`. Items: `agent_message`, `reasoning`, `command_execution`, `file_change`, `mcp_tool_call`, `web_search`, `todo_list`, `error`; status in_progress/completed/failed. | https://takopi.dev/reference/runners/codex/exec-json-cheatsheet/ (third party; official exec page returned 404 at https://learn.chatgpt.com/docs/exec) | M |
| `codex app-server` (JSON-RPC 2.0, JSONL over stdio default; Unix socket; **WebSocket experimental/unsupported**) | `thread/started`, `thread/status/changed` (status `notLoaded`/`idle`/`active`/`systemError`; active flags incl. **`waitingOnApproval`**), `turn/started`, `turn/completed`, `item/started`, `item/completed`, `item/agentMessage/delta`; server-initiated `item/permissions/requestApproval`, `item/fileChange/requestApproval`; opt-out via `initialize…optOutNotificationMethods` | https://learn.chatgpt.com/docs/app-server (S) | H-M |

### 2d. Push / wake doors
App-server (above) is the programmatic door — turn/start into a thread, approvals answered by client. Whether a plain interactive `codex` TUI in a tmux pane is attachable to an app-server is **not verified** (tmux-agent-status mentions "newer Codex clients using shared app-servers" — suggests yes). `codex exec resume` (not re-verified). No channels/ACP equivalent found. Conf L-M.

### 2e. Mapping → Codex
| # | event | emitter | cert | note |
|---|---|---|---|---|
| 1 | session_started | SessionStart | H | |
| 2 | session_ended | SessionEnd(reason) | M | flaky (#49003); L0 mandatory |
| 3 | turn_started | UserPromptSubmit; rollout `task_started` | H / M | |
| 4 | turn_ended | Stop(+last_assistant_message); rollout `task_complete` | H / M | |
| 5 | turn_failed | none in hooks; `turn.failed` only in exec --json | L | |
| 6 | interrupted | **Interrupt** (0.150.0+); rollout `turn_aborted` | M | main thread only |
| 7 | tool_started | PreToolUse | H | |
| 8 | tool_ended | PostToolUse | H | no failure variant documented |
| 11 | approval_requested | PermissionRequest; app-server `waitingOnApproval`; TUI `approval-requested` OSC9/BEL | H | fires when a prompt is about to show (doc wording) |
| 12 | approval_resolved | derived (next PostToolUse / app-server status change) | L-M | |
| 13 | attention_requested | none as hook; `notify` = turn-complete only | L | |
| 14/15 | agent_spawned/stopped | SubagentStart / SubagentStop | H | |
| 16 | compaction | PreCompact / PostCompact | H | |
| 17 | output_changed | none (app-server `item/agentMessage/delta` only if attached) | L | |
| 18 | stall | none | — | |
| 19 | file_changed | none as hook; `file_change` item in exec/app-server | L | |

**States without screen:** working ✔ (UserPromptSubmit…Stop/Interrupt; H) · waiting ✔ (PermissionRequest; H) · idle ✔ (Stop; H) · exited ⚠ (SessionEnd M, flaky → L0). **3 of 4 solid by hooks; exited needs L0.** Gap: no event when approval is *resolved*; no `turn_failed`.

## 3. Gemini CLI (Google `gemini`)

### 3.0 Product status — VERIFIED
| Fact | Detail | Source | Conf |
|---|---|---|---|
| Announcement | 2026-05-19 (Google I/O): Antigravity CLI (`agy`) launches; consolidation under "Antigravity" brand | https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ (S) | H |
| Cutoff | **2026-06-18**: Gemini CLI "stopped serving requests" for Google AI Pro, AI Ultra, free-tier individual accounts, free Gemini Code Assist, Code Assist for GitHub | https://github.com/google-gemini/gemini-cli/discussions/28017 (S) · https://github.com/google-gemini/gemini-cli/discussions/27274 (S) | H |
| Who can still use it | Gemini Code Assist **Standard/Enterprise licence** or Google Cloud; **paid** Gemini API keys / Gemini Enterprise Agent Platform API keys. Free API-key use: not stated in any source read — treat as **unknown** | same | H (enterprise/paid) / L (free key) |
| Maintained? | Yes, narrowly: "updated with latest model releases, bugs and security fixes for our enterprise customers"; **stays Apache-2.0 open source** | discussion #27274 (S) | H |
| Releases (live) | stable **v0.62.0 (2026-09-29)**; preview v0.63.0-preview.0 (2026-09-29); nightly v0.64.0-nightly.20261001 (2026-10-01) | https://github.com/google-gemini/gemini-cli/releases (S) | M-H |
| agy = successor? | Yes: "unified, agent-first terminal experience"; keeps Skills, Hooks, Subagents, Extensions (→ plugins); described as a rewrite, not a port (Go-based per 3rd party) | blog above; https://agentpedia.codes/blog/antigravity-cli-deep-dive | H / M |
| Implication | For a personal-account operator (majkee) Gemini CLI is **not runnable** unless he holds an enterprise licence or pays for an API key. The product is observable (open source, enterprise users) but is a shrinking, enterprise-only target. Decision input for map "target set". | — | — |

### 3a. Hook events (https://geminicli.com/docs/hooks/ and /hooks/reference/, fetched 2026-10-02, S) — H-M
Config: `settings.json` merged: `.gemini/settings.json` (project) → `~/.gemini/settings.json` (user) → `/etc/gemini-cli/settings.json` (system) + extension hooks. JSON on stdin/stdout; stdout must be pure JSON; exit 0 ok / 2 block. **No stability label** on hooks docs. First-shipped version/date: **not found** (L).

| Event | Fires | Fields / notes |
|---|---|---|
| SessionStart | startup/resume/clear | |
| SessionEnd | exit/clear | `reason` ∈ exit, clear, logout, prompt_input_exit, other |
| BeforeAgent | after prompt submitted, before planning | `prompt` |
| AfterAgent | agent loop ends | `prompt`, **`prompt_response`** (final text), `stop_hook_active`; can trigger retry |
| BeforeModel / AfterModel | around each LLM call; AfterModel can filter response **chunks** | |
| BeforeToolSelection | before tool selection | |
| BeforeTool / AfterTool | tool lifecycle | |
| PreCompress | before context compression | (no Post) |
| Notification | system alert | `notification_type` — **only `ToolPermission` documented**; `message`, `details` |

Common input: `session_id`, `transcript_path` ("absolute path to session transcript JSON"), `cwd`, `hook_event_name`, `timestamp` (ISO 8601). 11 events. Last-90-day changes: none verifiable.

### 3b. On-disk session record
| Item | Value | Source | Documented? | Conf |
|---|---|---|---|---|
| Path | `~/.gemini/tmp/<project_hash>/chats/session-<timestamp>-<id>.jsonl` (name pattern `session-*.jsonl` seen in 0.46+ issue); checkpoints separately in `~/.gemini/tmp/<hash>/checkpoints` | web-search digest of https://github.com/google-gemini/gemini-cli/pull/23749 , https://github.com/codeaholicguy/ai-devkit/issues/278 , https://geminicli.com/docs/cli/checkpointing/ | checkpoints documented; chat format **not** | M |
| Format | JSONL since **v0.39.0** (PR #23749 merged 2026-04-09): line 1 metadata (`sessionId`, `projectHash`, `startTime`, `lastUpdated`, `kind`), then message objects / `{"$set":{…}}` update records; legacy monolithic `.json` still read | PR #23749 (S) | no | M |
| Write lag | `fs.appendFileSync` per record ⇒ effectively synchronous (L-M) | PR #23749 (S) | — | M |
| Pending tool-permission in file | unknown | — | — | L |

### 3c. Headless / structured (https://geminicli.com/docs/cli/headless/, S) — H-M
`-p/--prompt` or non-TTY ⇒ headless. `--output-format json` → `{response, stats, error?}`. `--output-format stream-json` → NDJSON `init`, `message`, `tool_use`, `tool_result`, `error`, `result`. Exit codes 0 / 1 / **42** (bad input) / **53** (turn limit).

### 3d. Push / wake doors
`gemini --acp` — ACP JSON-RPC 2.0 over stdio (`initialize`, `authenticate`, `newSession`/`loadSession`, `prompt`, `cancel`, `setSessionMode`, fs proxy); Zed supports it (0.201.5+); no stability label read — https://geminicli.com/docs/cli/acp-mode/ (S). Telemetry to file via `GEMINI_TELEMETRY_OUTFILE`. Conf M. (Whether ACP still works for non-enterprise users post-2026-06-18: the same auth gate applies — inferred, L.)

### 3e. Mapping → Gemini CLI (doc-derived, **no fixture run**; certainty capped M)
| # | event | emitter | cert |
|---|---|---|---|
| 1 | session_started | SessionStart | M |
| 2 | session_ended | SessionEnd(reason) | M (+L0) |
| 3 | turn_started | BeforeAgent | M |
| 4 | turn_ended | AfterAgent (`prompt_response`) | M |
| 5 | turn_failed | none (headless `error`/exit code only) | L |
| 6 | interrupted | none | L |
| 7 | tool_started | BeforeTool | M |
| 8 | tool_ended | AfterTool | M |
| 11 | approval_requested | Notification(ToolPermission) | M |
| 12 | approval_resolved | derived (AfterTool) | L |
| 13 | attention_requested | Notification — only ToolPermission, so = #11 | L |
| 14/15 | subagents | none documented in hooks | — |
| 16 | compaction | PreCompress (pre only) | M |
| 17 | output_changed | AfterModel (per chunk, can fire often) | L |
| 18 | stall / 19 file_changed | none | — |

**States without screen:** working ✔ (BeforeAgent…AfterAgent) · waiting ✔ (Notification ToolPermission) · idle ✔ (AfterAgent) · exited ✔ (SessionEnd + L0). **All 4 on paper (M), unproven by fixture.** Only usable by enterprise/API-key operators.

## 4. agy / Antigravity CLI (optional vendor)
Versions: CLI changelog entries v1.2.7 (2026-09-19), v1.2.9 (09-23), v1.2.10 (09-24), v1.2.12 (2026-09-27); note the same changelog also carries Antigravity-app entries numbered 2.x (v2.6.0 2026-08-07, v2.9.1 2026-08-20, v2.14.0 2026-09-15) — numbering is **per-surface and confusing**; do not assume a single version line. Source: https://antigravity.google/docs/changelog/ (S, M).

### 4a. Hooks (https://antigravity.google/docs/hooks/, S — H on names, M on payload)
Five events, unchanged since the predecessor note: **PreInvocation** (before each model call), **PostInvocation**, **PreToolUse**, **PostToolUse**, **Stop** ("fires when execution terminates"; payload `terminationReason`, `fullyIdle`; may block → reason fed back as new prompt). No SessionStart/SessionEnd/PermissionRequest/Notification/subagent/compaction. Config: workspace `.agents/hooks.json`, global `~/.gemini/config/hooks.json`, plugin-level. Schema pitfalls (flat vs grouped arrays, seconds timeout): https://github.com/thedotmack/claude-mem/pull/4274 , https://github.com/mksglu/context-mode/issues/1206. **Change in window:** v2.6.0 (2026-08-07): hook configs that "could never run" are now rejected at load with an error (was silent ignore); stop hooks that keep blocking no longer hang the agent (changelog S, M). No new events found.

### 4b. On-disk record
Official: hook payload gives `transcriptPath`; app data dir CLI = `~/.gemini/antigravity-cli` (H-M). Third-party (reverse-engineered): `brain/<uuid>/.system_generated/logs/transcript.jsonl`, `conversation_summaries.db`, `conversations/*.pb|.db` (predecessor; M-L, version-dependent). Pending-approval marker: not documented. Fixed: v2.6.0 "conversations stuck showing as still running and never return to idle" (M) — status derivation from record is bug-prone.

### 4c. Headless
`-p/--prompt`; v1.2.12 "unlimited headless run timeouts, structured error reporting"; v1.2.10 headless exit-code fix after partial stream then error; v1.2.9 fixes daemon processes left after `-p` exit, mentions multi-turn **`stream-json`** (event names not found). Known bug (predecessor, M): `agy -p` printed nothing when piped. Conf M-L.

### 4d. Push / wake
No ACP: feature request open since 2026-05-20, no maintainer reply (https://github.com/google-antigravity/antigravity-cli/issues/31, S). **Remote Control**: app 2026-08-20 (v2.9.1), CLI "session-scoped" 2026-09-18, refined v1.2.12 2026-09-27 (changelog S) — relay to another device, not documented as a local API. M.

### 4e. Mapping → agy
| # | event | emitter | cert |
|---|---|---|---|
| 1 | session_started | none (first PreInvocation reveals `conversationId`) | L |
| 2 | session_ended | none → L0 | — |
| 3 | turn_started | PreInvocation (per model call, not per user turn) | L-M |
| 4 | turn_ended | Stop (`fullyIdle` may distinguish true idle from sub-loop end) | M |
| 5/6 | failed / interrupted | `terminationReason` possibly; unverified | L |
| 7/8 | tool_started/ended | PreToolUse / PostToolUse | M |
| 11–13 | approval/attention | **none** | — |
| 14–19 | rest | none | — |

**States without screen:** working ✔ · idle ✔ (Stop, `fullyIdle`) · **waiting ✘** · **exited ✘ (L0 only)**. 2 of 4. Waiting ⇒ PTY stall heuristic or record experiment.

## 5. Cross-vendor summary
| | Claude Code | Codex | Gemini CLI | agy |
|---|---|---|---|---|
| hook events (count) | 33 | 12 | 11 | 5 |
| SessionEnd | yes (H) | yes, flaky (M) | yes (M) | no |
| approval-requested hook | yes (2 ways) | yes | via Notification(ToolPermission) | **no** |
| turn-failed | StopFailure | no | no | maybe |
| interrupt | no dedicated | Interrupt (0.150.0) | no | maybe via Stop |
| last message in hook | Stop.last_assistant_message | Stop.last_assistant_message | AfterAgent.prompt_response | not documented |
| record documented? | path yes, format internal | no | no | no (path via hook) |
| live PID-keyed status | sessions/<pid>.json (undoc) | none | none | none |
| 4 states w/o screen | 4/4 | 3/4 + L0 | 4/4 on paper | 2/4 |
| product usable by personal account | yes | yes | **no** (enterprise/paid key) | yes |
| structured stream | stream-json | exec --json / app-server | stream-json | stream-json (L) |
| local push door | channels (preview), `-p --resume` to bg | app-server | `--acp` | none (ACP open request) |

## 6. Residual unknowns / fixture list (what this pass could NOT settle)
1. CC: does Esc-interrupt fire Stop? Is a pending permission prompt visible in the .jsonl? Stability of `sessions/<pid>.json` `status` across versions (observed 2.1.178 and 2.1.284).
2. Codex: approval prompts in rollout; PermissionRequest ordering vs prompt; whether interactive TUI exposes app-server `waitingOnApproval`; official `exec` doc (404 on learn.chatgpt.com/docs/exec).
3. Gemini: hooks first-shipped version; subagent events; does `--acp` still authenticate for non-enterprise; free API key viability.
4. agy: real hook payload dump (camelCase vs snake); Stop on Esc; transcript step status while approval pending.
5. All: summaries from WebFetch (S) — re-read primaries (hooks pages of CC/Codex/Gemini/agy) before locking field names.

Sections to refresh: [CC changelog hook rows weekly; Codex 0.16x hook doc + Interrupt date; Gemini CLI release stream + enterprise-only status; agy hooks doc + changelog; CC sessions/<pid>.json schema; Codex app-server TUI attach]
