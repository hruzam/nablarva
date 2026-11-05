---
title: Majkee–Cartan log
date: 2026-11-05
author: majkee · Cartan
status: draft
session: termbrana-M0-markdown-test
source: operator-provided formalized output
---

# Majkee–Cartan log

Formalized output recorded for the `termbrana-M0-markdown-test` session.

## Update — 2026-11-05

- Added a second log entry to verify the append-and-push path.
- The working branch is expected to remain synchronized with `origin/core` after publication.
- Approval-window observation: `Ctrl+C` cancels the approval prompt, equivalently to `Esc`.
- Resume observation: after the terminal window containing an open approval request was
  killed and the session was resumed, the approval was still available. The one-hour
  relaxation window was not tested; renewal of the session cache on the vendor side is
  therefore only an assumption.

## Zeno deep research — approval persistence

**Date:** 2026-11-05

**Scope.** Read-only investigation of installed Codex CLI `0.166.0` and Claude Code
`2.1.286`, their local state surfaces, vendor documentation/source, and selected public
reports. No files/configuration changed during the research pass.

### Bottom line

- **Codex CLI has two distinct pending-approval representations.** The semantic
  unresolved approval is RAM-only (`oneshot` callbacks in the active turn and app-server
  request map), but its request event is also written to durable rollout history. A live
  shared app-server can replay the original pending approval to a newly attached client
  after `thread/resume`; a true turn interruption or daemon/process death clears the RAM
  callback, so durable history alone does not restore an answerable approval. **Confidence:
  high.**
- **Claude Code clearly persists conversations and permission mode/rules, but this pass
  found no vendor documentation or local transcript record type establishing a stock
  on-disk “pending approval object” for CLI `2.1.286`.** There is a documented, separate
  durable mechanism for a hook-deferred tool call; it must not be mistaken for ordinary
  permission approval. **Confidence: medium for absence-of-evidence; high for the separate
  documented mechanisms.**
- **Esc is generally not an unanswered interruption.** Codex `0.166.0` maps Esc to
  decline in approval UI; Claude’s current permission-prompt documentation labels Esc
  “cancel.” **Confidence: high for these UI mappings, not for every historical version or
  modal.**

### Raw local evidence

**OBSERVED — host, versions, artifacts**

- `codex --version` → `codex-cli 0.166.0`; `claude --version` → `2.1.286 (Claude Code)`.
- Codex local durable surfaces include:
  - `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`
  - `~/.codex/state_5.sqlite`, `thread_history_1.sqlite`, `queue_1.sqlite`,
    `logs_2.sqlite`
  - `~/.codex/app-server-daemon/`, `ipc/ipc.sock`, `thread-writer-locks/`.
- The local Codex databases have durable thread/history/queue/log tables but no table
  named for approval/pending state. This is not proof that no serialized approval payload
  exists.
- Existing Codex `thread-writer-locks/*.lock` files are zero bytes. Earlier read-only
  `lsof` observation attributed active locks to the managed `codex app-server` daemon,
  making them ownership/exclusion locks rather than approval-payload stores.
- Retained Claude session JSONLs are under `~/.claude/projects/.../*.jsonl`; vendor hook
  schema independently names this same path shape. Local transcript record-type inventory
  included `assistant`, `user`, `last-prompt`, `mode`, `permission-mode`,
  `queue-operation`, etc.; the only permission-named record was `permission-mode`, with
  keys `type`, `sessionId`, `permissionMode`. No `approval` or `pending` record type was
  found in that retained corpus.
- `~/.claude/history.jsonl` entries have keys `display`, `pastedContents`, `project`,
  `sessionId`, `timestamp`: prompt-history metadata, not an approval object.
- No locally named `*approval*`, `*permission*`, or `*pending*` file was found beneath
  `~/.claude`. This is negative evidence only; logs, RAM, or opaque binary state may still
  exist.

### Codex CLI

**SOURCE — exact pending object, installed release.** In tag `rust-v0.166.0`, an active
turn’s `TurnState` stores `pending_approvals: HashMap<String,
oneshot::Sender<ReviewDecision>>`; command and patch requests insert a sender, emit
`ExecApprovalRequest`/`ApplyPatchApprovalRequest`, then await the receiver. If the sender
is cleared, the receiver resolves as `ReviewDecision::Abort`, not approval. The request
event carries command/patch details, call/approval/turn IDs, reasons, and offered
decisions. [Turn state](https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/core/src/state/turn.rs), [request path](https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/core/src/session/mod.rs)

**SOURCE — durable event trace, not durable waiter.** The same release’s `send_event`
persists each event as `RolloutItem::EventMsg(event.msg.clone())` before delivery. Thus an
approval *request representation* can be present in the rollout JSONL. This does not
serialize the Rust `oneshot::Sender`, active task, or ability to accept a later answer.
[Rollout persistence](https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/core/src/session/mod.rs)

**SOURCE — app-server RAM cache and immediate replay.** The installed app-server stores
each unresolved client request in `OutgoingMessageSender.request_id_to_callback`, containing
a callback sender, owning thread ID, and cloned `ServerRequest`.
`pending_requests_for_thread` reads that in-memory map;
`replay_requests_to_connection_for_thread` resends its original request and ID to a newly
attached connection. This is the concrete mechanism by which an unanswered approval can
immediately reappear after a client disconnect/reconnect, provided the same daemon and
active turn remain alive. [App-server request cache/replay](https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/app-server/src/outgoing_message.rs)

**SOURCE — current protocol names.** OpenAI’s app-server documentation names the wire
requests `item/commandExecution/requestApproval`, `item/fileChange/requestApproval`, and
`item/tool/requestUserInput`; clients answer them and receive `serverRequest/resolved`.
[App-server protocol](https://learn.chatgpt.com/docs/app-server)

**SOURCE — interruption clears the live cache.** On `EventMsg::TurnAborted`, the
app-server aborts all pending per-thread server requests; the source comments and core
request path treat an interrupted/cleared approval as abort. Therefore, replay applies to a
live disconnected client, not to a turn already interrupted. [Turn-abort handling](https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/app-server/src/bespoke_event_handling.rs)

**SOURCE — daemon scope.** `--no-daemon` is documented in the installed TUI source as
running without the shared background server; local observation found the managed
daemon/socket. Therefore a normal daemon-backed run has a plausible live-process recovery
substrate, whereas an embedded/`--no-daemon` process loses it when killed. [TUI CLI option](https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/tui/src/cli.rs)

**SOURCE — keyboard semantics.** Codex `0.166.0` approval bindings define `Esc`/`n` as
decline, `y` approve, `a` approve-for-session. Esc therefore resolves the approval rather
than preserving it unanswered. [Keymap](https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/tui/src/keymap.rs)

**SOURCE — durable decisions differ from pending state.** An exec-policy amendment
decision is explicitly written to both in-memory and on-disk policy. Session-scoped
permissions are documented as applying to later turns in that session, but the
documentation does not promise persistence across daemon restart. [Policy amendment source](https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/core/src/session/mod.rs), [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)

**INFERENCE — interruption matrix.**

| Situation | Exact pending approval |
|---|---|
| TUI/client disconnect; shared daemon and turn survive; another client performs app-server `thread/resume` | Replayable immediately from app-server RAM, with original request ID. |
| New ordinary `codex resume` attaches to that same daemon | Likely replayable; direct CLI-path probe still needed. |
| Esc on approval modal | Declined/resolved, not pending. |
| Ctrl+C reaches turn-interrupt path | Cleared/aborted; no answerable approval remains. |
| Terminal/window kill leaves daemon alive | Potentially replayable after reattachment. |
| `--no-daemon`, daemon kill, or process/session death | RAM callback lost; rollout JSONL may retain request history but cannot itself restore the waiter. |

**COMMUNITY — supporting but non-authoritative.** OpenAI commit `69d7a45` explicitly
introduced/respecified replay of pending approval/input requests after `thread/resume`,
resolved notifications, and tests; the installed `0.166.0` source contains that replay
machinery. [Commit 69d7a45](https://github.com/openai/codex/commit/69d7a456bbffd019504ab471a8f2a02abefaa0ae) A user report on older `0.149.1` describes Ctrl+C
plus resume encountering an active writer lock, consistent with an old live writer
surviving, but it does not prove approval persistence. [Issue #39823](https://github.com/openai/codex/issues/39823)

### Claude Code CLI

**SOURCE — durable conversation/session history.** Anthropic documents `--continue`/
`--resume` and says sessions are stored locally per project. Its hook documentation gives
the concrete transcript path form `~/.claude/projects/.../<session>.jsonl`. This
establishes durable conversation/session history, not a documented durable pending-permission
object. [CLI usage](https://code.claude.com/docs/en/cli-usage), [FAQ](https://support.claude.com/en/articles/14554922-claude-code-user-faq), [hook input schema](https://code.claude.com/docs/en/hooks)

**SOURCE — permission decisions/rules are separate.** The current permissions reference
says:

- normal approvals last for the current session by default;
- “Yes, and don’t ask again” for Bash/WebFetch writes a durable rule to
  `.claude/settings.local.json`;
- file-modification approval lasts only until session end;
- some prompts offer one-time approval only.

It also shows `Esc to cancel` on a Bash permission prompt. [Permissions documentation](https://code.claude.com/docs/en/permissions)

**SOURCE — hooks can observe or externalize, but are not stock persistence.**
`PermissionRequest` hooks receive session ID, transcript path, tool name/input, and
permission suggestions. A hook may allow/deny, and a delayed `Notification` hook can signal
a pending prompt. A user-installed hook could write its own durable approval ledger, but
Anthropic’s stock hook contract does not say it snapshots/reconstructs the native pending
dialog. [Hook lifecycle and PermissionRequest](https://code.claude.com/docs/en/hooks)

**SOURCE — documented durable deferred tool call, distinct primitive.** A `PreToolUse`
hook can return `defer`; Anthropic documents that the session remains on disk and the single
deferred call remains pending until resumed, subject to retention. This is a genuine
persisted/replayable tool-call mechanism, but it is not the ordinary unanswered manual
permission prompt. [Deferred-tool documentation](https://code.claude.com/docs/en/hooks)

**SOURCE — version boundary.** Claude Code `2.1.288` added recovery of a user composer
draft cleared by Ctrl+C via Up-arrow, and fixed several resume/transcript issues. The
installed `2.1.286` predates it. This concerns draft text, not an approval object, and must
not be overread as permission restoration. [v2.1.288 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.288)

**INFERENCE — Claude interruption matrix.**

| Situation | Exact pending approval |
|---|---|
| Resume a normal local CLI session after process death | Conversation/transcript returns; no authoritative evidence found that a stock pending approval is reconstructed. |
| Esc on documented command prompt | Cancel/decline, not unanswered. |
| Ctrl+C | Vendor says it cancels the current generation; exact behavior while a `2.1.286` permission modal is focused remains unprobed. |
| Another terminal / another client | No authoritative local-CLI handoff/replay contract found. Hooks, remote/cloud products, and external wrappers are separate mechanisms. |
| Hook `defer` | Documented recovery of a deferred tool call, not proof for manual approval. |

**COMMUNITY — weak/qualified.** Public reports claim that pending Claude permission
requests may not appear in transcript logs, while session/IDE/cloud UIs can show “needs
input.” These are useful hypotheses only; they mix CLI, IDE, Desktop, and cloud runtimes
and are not vendor guarantees. Do not promote them to a Claude CLI persistence claim without
a controlled probe.

### Terminal, TUI, and harness distinction

- **Terminal bytes/rendering:** a terminal emulator, tmux, or scrollback may retain
  rendered ANSI text after a prompt appeared. That is display residue, not an addressable
  approval object or decision channel. No vendor-managed terminal cache was found locally.
- **Codex TUI render cache:** source describes an in-memory, render-only live transcript
  tail. It can display an in-flight call but is not the semantic owner; app-server/core RAM
  owns the answerable request. [TUI source](https://raw.githubusercontent.com/openai/codex/rust-v0.166.0/codex-rs/tui/src/chatwidget.rs)
- **Harness/control plane:** Codex app-server has a first-class pending-request/replay
  protocol. Claude hooks provide observation/decision extension points; persistence exists
  only if a hook or another host deliberately records it.

### Confidence and unresolved gaps

- **High:** Codex `0.166.0` exact object locations, rollout event persistence, live
  app-server replay, and abort-on-turn-interrupt behavior.
- **High:** Claude’s transcript/rule/session/deferred-tool documentation and Esc labeling.
- **Medium:** Codex ordinary `codex resume` reconnect behavior after a terminal-only loss,
  because the exact default CLI path was not exercised.
- **Low-to-medium:** claim that Claude `2.1.286` has no hidden pending-approval cache. The
  negative local corpus and documentation gap do not exclude binary RAM, opaque state,
  IDE/Desktop/remote-control state, or telemetry.

**Smallest next probe, if later authorized.** Use isolated temporary Codex/Claude config
homes and a harmless approval-triggering command. Capture state after: (1) client disconnect
with daemon alive, (2) Ctrl+C, (3) daemon/process kill, and (4) resume from another terminal.
Record only paths, record types, request IDs, and status transitions—not command content or
credentials.
