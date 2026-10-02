# @Epoch research report
Date: 2026-10-01
Triggered by: termpanum (#ax2/#ax3/#gate/#weather) vs driller (2026-08-05) — is PTY meaning extraction still needed?
Scope: default radar + brief-pointed (hooks, session records, prior art). Live-fetched this run unless marked INFERRED.
Caveat: WebFetch returns small-model summaries; items marked (summary) were not read verbatim. Primary-doc quotes should be re-read before gaveling.

## 0. What "agy" is
agy = the single binary of Google's **Antigravity CLI** (Gemini-family terminal coding agent; successor line to Gemini CLI, state under ~/.gemini/antigravity-cli/).
Sources: https://computingforgeeks.com/antigravity-cli-cheat-sheet/ ; https://realpython.com/antigravity-cli/ (2026). CONFIDENCE H on identity.

## 1. Hook surface

### Claude Code — H (official docs, fetched 2026-10-01)
Source: https://code.claude.com/docs/en/hooks
- Events (32 listed in fetched summary): SessionStart, Setup, UserPromptSubmit, UserPromptExpansion, PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, PostToolBatch, Notification, MessageDisplay, SubagentStart, SubagentStop, TaskCreated, TaskCompleted, Stop, StopFailure, TeammateIdle, InstructionsLoaded, ConfigChange, CwdChanged, DirectoryAdded, FileChanged, WorktreeCreate, WorktreeRemove, PreCompact, PostCompact, PreModelSwitch, PostModelSwitch, Elicitation, ElicitationResult.
- NOTE: SessionEnd was NOT in the fetched list (summary may have dropped it; not verified). Re-check before relying on it. Exit is covered by L0 anyway; a crash fires no hook.
- Config: ~/.claude/settings.json, .claude/settings.json, .claude/settings.local.json, managed policy, plugin hooks/hooks.json, skill/subagent frontmatter.
- Stability: no label on hooks generally; only "agent hooks" flagged experimental. Treat as stable.
- Payload: Stop carries `transcript_path`, `last_assistant_message`, `stop_reason`, `prompt_id`. Notification carries `notification_type` (permission_prompt, idle_prompt, agent_needs_input, agent_completed, ...). PermissionRequest carries tool_name/tool_input/tool_use_id.

### Codex CLI — H for events, M for version claims
Source: https://learn.chatgpt.com/docs/hooks (301/308 redirect from developers.openai.com/codex/hooks), fetched 2026-10-01.
- Events (12), all labelled Stable: SessionStart, SessionEnd, PreToolUse, PostToolUse, PermissionRequest, PreCompact, PostCompact, UserPromptSubmit, SubagentStart, SubagentStop, Stop, Interrupt.
- Config: hooks.json or inline [hooks] in config.toml (also requirements.toml per changelog).
- Payload common: session_id, transcript_path (nullable), cwd, hook_event_name, model, permission_mode, turn_id (turn events). Stop/SubagentStop: last_assistant_message. SubagentStop: agent_transcript_path. Tool events: tool_input/tool_response. SessionEnd: reason.
- PermissionRequest "can allow, deny, or decline to decide and let the normal approval prompt continue" => it fires when an approval prompt is about to show.
- History: hooks became stable in v0.124.0 (2026-04-23); 0.150.1 (2026-08-27) lists twelve events, non-managed hooks need review/trust, enabled by default. Source (secondary, M): web-search results citing https://www.gradually.ai/en/changelogs/codex-cli/ and https://codex.danielvaughan.com/ (not opened directly).
- Gotcha: non-managed hooks require trust review before running (a lab must pre-trust fixtures).

### agy (Antigravity CLI) — M (third-party + one Google Cloud author; no official doc fetched)
Sources: https://atamel.dev/posts/2026/07-16_where_agy_hooks/ (2026-07-16) ; https://github.com/automatis-tools/agents-can-communicate/issues/171 ; https://github.com/thedotmack/claude-mem/issues/4196 ; https://gist.github.com/tanaikech/004f4bcdb530f1a07706c85c13dc8205 (mirror of the Google Cloud Medium guide; Medium itself returned 403).
- Events (5): PreInvocation, PostInvocation, PreToolUse, PostToolUse, Stop. Stop fires "when the execution loop terminates" and can block (reason fed back as new prompt).
- NO PermissionRequest / Notification / SessionStart / SessionEnd / subagent / compaction hook. Gemini-CLI/Claude event names silently ignored.
- Config: SOURCES CONFLICT. Global `~/.gemini/config/hooks.json` (atamel 2026-07-16; issue #171) vs `~/.gemini/antigravity-cli/hooks.json` (Medium guide via gist). Project: `<root>/.agents/hooks.json` (both agree). Unresolved: possibly changed between versions, or both read. Fixture must test both.
- Schema is picky: integration as top-level key; PreToolUse/PostToolUse = matcher-grouped arrays; Pre/PostInvocation/Stop = flat arrays; timeout in seconds; wrong schema => silent ignore (claude-mem #4196).
- Payload: session_id, transcript_path, cwd, timestamp, hook_event_name (atamel says the event name is missing for some events - contradiction with the guide), toolCall.args for tool events.
- Stability label: none found. Atamel: "hook events quite limited".

## 2. On-disk session records

### Claude Code — M/H
- ~/.claude/projects/<project>/<session>.jsonl, plaintext, 30-day default retention. Source: https://allaboutcoding.ghinda.com/where-ai-coding-clis-store-session-logs/ (M; "best documented" of six CLIs). The hook payload hands the path (`transcript_path`) so no path discovery needed (H).
- Contents: user/assistant messages, tool_use/tool_result. Pending permission prompt in the file: NOT verified this run. Lag: not measured.

### Codex — M (reverse-engineered; not vendor-documented)
- ~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl; line = {timestamp, type, payload}; types ResponseItem, EventMsg, SessionMeta, TurnContext (approval/sandbox policy), Compacted. Default persistence "limited" (UserMessage, AgentMessage, TokenCount, TurnComplete); "extended" adds ExecCommandEnd, Error, McpToolCallEnd.
- Sources: https://dev.to/milkoor/reverse-engineering-codex-cli-rollout-traces-3b9b (v0.130.0; found real names task_started/task_complete/agent_message/function_call/function_call_output differ from protocol.rs names; "documented vs real don't match"); search summary of https://codex.danielvaughan.com/2026/06/08/... ; https://github.com/openai/codex/discussions/3827 (no format doc).
- Approval prompts persisted? UNVERIFIED (dev.to explicitly unanswered). codex_monitor_skill reads an `event_msg` "input_wait" (summary of scripts/sessions.py) — suggests some wait marker exists, unproven for approvals.
- Format drift risk is real (names changed; compaction bloat issue #24948).

### agy — M (reverse-engineered by third parties)
- ~/.gemini/antigravity-cli/brain/<uuid>/.system_generated/logs/transcript.jsonl (+ transcript_full.jsonl when fields truncated), history.jsonl, conversation_summaries.db (SQLite), conversations/*.pb (encrypted/protobuf) or conversations/<id>.db (agy-acp says SQLite with protobuf records). Row fields: step_index, source (USER_EXPLICIT/MODEL/SYSTEM), type (USER_INPUT/PLANNER_RESPONSE...), status (DONE/ERROR), created_at, content, thinking, tool_calls.
- Sources: web-search results citing https://github.com/mjacobs/agy-reader, https://agentgrep.org/backends/antigravity-cli/, https://www.codeagentswarm.com/en/guides/antigravity-cli-conversation-history, https://github.com/shindgew/agy-acp. Storage layout inconsistency (.pb vs .db vs brain jsonl) = version-dependent; M-L.
- Pending approval in transcript: not documented anywhere I found. Lag: unknown.
- Known bug: `agy -p` emits nothing to stdout when piped; adapters recover the answer from the on-disk transcript (https://github.com/marceldarvas/cc-multi-cli-plugin README).

## 3. Four states from hooks + records alone (no screen)
| CLI | idle | working | waiting-for-approval | exited | verdict |
|---|---|---|---|---|---|
| Claude | Stop / Notification idle_prompt | UserPromptSubmit..Stop | PermissionRequest or Notification permission_prompt (H) | SessionEnd (unverified in list) + L0 | YES (H on waiting; resolution of approval = PostToolUse/PermissionDenied) |
| Codex | Stop | UserPromptSubmit..Stop, task_started/complete in rollout | PermissionRequest (H, stable) | SessionEnd, Interrupt + L0 | YES (M/H) |
| agy | Stop | PreInvocation / PreToolUse..Stop | NONE: no permission hook found | no SessionEnd; L0 only | PARTIAL: gap = waiting-for-approval (and interrupt/cancel, which may not fire Stop) |
Edge for all: hooks are push events; a hook that never fires (hang, crash, kill -9, user Esc) leaves a stale "working". Needs L0/L1 liveness + a stall timer. That is the PTY's legitimate role, not meaning.
agy waiting gap candidates: PreToolUse fired with no PostToolUse + PTY quiet (stall heuristic = liveness-class, acceptable under #ax3), but cannot distinguish "waiting for approval" from "tool running slowly"; only the screen/transcript could. Under agy auto-approve modes the state may not exist (aibuilderclub guide mentions auto-approve; not read).

## 4. Content (final answer, file changes, test results) without PTY
- Claude: YES. Stop.last_assistant_message (H). File changes: PostToolUse tool_input/tool_response for Edit/Write; test results: PostToolUse on Bash (H).
- Codex: YES. Stop.last_assistant_message (H); PostToolUse tool_response; rollout function_call_output (M).
- agy: PARTIAL/YES-via-file. Stop hook payload fields beyond the common envelope are not documented to include the final message; but transcript_path -> transcript.jsonl PLANNER_RESPONSE content, and PostToolUse gives toolCall.args (M). File-change diffs: CodeAction steps in the store (agy-reader). Reverse-engineered, version-fragile.

## 5. CLI with no hooks AND no record?
None of the three. All have a hook surface and an on-disk record. agy is the thinnest (5 events, no approval hook, record format unofficial, headless stdout bug). Brief #gate premise "agy: no known hook surface" is OUTDATED: agy hooks exist (documented since at least 2026-07-16).

## 6. Prior-art check (#weather)
Only contradictions/qualifications to the brief's claim "None reads state off the screen":
- keepmind9/clibot — QUALIFIED. Hook mode and polling mode exist. Polling mode (`use_hook: false`) = "Periodic tmux capture when output becomes stable" to detect completion, then reads transcript.jsonl for the content. So it does use the screen (as a stability trigger) when hooks are off. Source: https://pkg.go.dev/github.com/keepmind9/clibot/internal/cli (M). Hooks are supported for Claude, Gemini, OpenCode; not stated for Codex. Not "meaning off the screen", but not strictly "never reads the screen" either. (A first fetch of the repo README garbled this; the pkg.go.dev reading is the more specific one.)
- aelaguiz/codex_monitor_skill — CONFIRMED files-only, but fragile: infers WORKING/WAITING/IDLE from last 50 lines / 500KB tail of rollout JSONL (reasoning/function_call = working; event_msg input_wait = waiting; else idle). Heuristic, not documented semantics. (summary of scripts/sessions.py, M)
- shindgew/agy-acp — CONFIRMED, README says steps come from agy's conversation SQLite DB, PTY output is diagnostic only, never parsed; no hooks used (README says none). Note: it chose DB over hooks, i.e. it ignores agy hooks. (M)
- marceldarvas/cc-multi-cli-plugin — CONFIRMED: agy read back from on-disk transcript because `agy -p` prints nothing when piped (upstream bug). (M)
- Not re-verified (no contradiction surfaced; not fetched): codex-wake, kherep #66, claude-peers-mcp, interlink-mcp, codex-agent.

## VERDICT
Evidence supports "PTY for liveness only, meaning from hooks/files" TODAY for:
- Claude Code — confidence H (official hooks incl. PermissionRequest/Notification/Stop with last_assistant_message).
- Codex CLI — confidence M-H (hooks stable since 0.124.0; PermissionRequest + Stop.last_assistant_message; rollout path is reverse-engineered, so keep hooks as primary, rollout as backup).
- agy — confidence M-L: does NOT fully hold. Gap = waiting-for-approval (no permission/notification hook; approval prompts not documented in transcript) and interrupt/exit events. Content is obtainable (transcript.jsonl), but the approval state can only be approximated by stall heuristics unless fixture measurement shows the transcript records a pending tool step.
=> Driller's meaning-extraction is redundant for Claude and Codex. It stays a live, but NARROW, contingency for agy ONLY, and only for the one state "waiting-for-approval" (a classifier on paint, if the fixture falsifies both the transcript and the stall-timer approaches). Recommended before building anything: run termpanum's EXPECT/TRIGGER/OBSERVE on an agy fixture: trigger an approval prompt, check (a) transcript.jsonl step status during the wait, (b) whether PreToolUse is emitted before the prompt, (c) which hooks.json path the installed version reads, (d) Stop on Esc/interrupt. Also fixture-verify Claude SessionEnd and Codex approval record in rollout.

Sections to refresh: [Claude SessionEnd presence; Codex rollout approval persistence; agy hooks.json path + payload; agy official docs (none read); agy version number (not captured); clibot polling-mode detail; unfetched prior art (codex-wake, kherep #66, claude-peers-mcp, interlink-mcp, codex-agent)]
