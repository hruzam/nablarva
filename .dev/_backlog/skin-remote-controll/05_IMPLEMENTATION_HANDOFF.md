---
title: Implementation handoff — inspect first, extend narrowly
date: '2026-10-23'
author: Wave
language: en
type: agent handoff / execution brief
scope: Termbrana continuation
status: advisory; not approved repository canon
source_check_date: '2026-10-23'
host_validation: not performed
new_work_status: documentation only
---

# Implementation handoff — inspect first, extend narrowly

## Mission

Help majkee navigate and hand off file-backed work to existing living CLI sessions without replacing their session host, terminal, editor, transport or authoritative project files.

This document prepares a future execution task. The present request authorized Markdown artifacts only. No application build, deployment, service installation or repository modification has been performed.

## Read first

Read this file and [02_SSH_TMUX_RELAY_ARCHITECTURE.md](02_SSH_TMUX_RELAY_ARCHITECTURE.md). Consult [03_NATIVE_UI_OPTIONS_BRIEF.md](03_NATIVE_UI_OPTIONS_BRIEF.md) only when a frontend decision becomes necessary. The desktop and RustDesk-reuse reports are separate scopes, not prerequisites.

**Repository files win.** This pack is advisory. Discover the actual repository and existing handoff/state documents; do not invent paths or overwrite another agent's active work.

## Preserved context

The conversation describes Linux/KDE, zsh, Sublime pins, thematic notes, Tailscale/SSH and tmux-hosted agents. The preferred direction is a disposable interface over workstation-owned execution. These are context constraints, not a current inventory.

Preserve existing pin identifiers, file/position anchors, queued notes, vendor-native terminal commands and direct terminal access. Discover what the existing `tso` helper actually does; do not assume ordinary SSH over a tailnet and Tailscale SSH are interchangeable configurations.

## Step 0 — inspect before changing

Produce a bounded inventory, with secrets excluded:

- Read the repository instructions, state/handoff files, existing adapters and tests. Inspect `git status` and relevant diffs before editing.
- Identify the actual host route, SSH configuration, tmux version/socket, session identities, CLI runtimes and native transcript locations/formats.
- Locate the existing pin and note formats, transfer mechanism, request/result contract, signalling adapter, deadlines and any existing deduplication.
- Check session-survival configuration, user hooks, resize effects and what closing an attached client does in this environment.

Record unknowns rather than substituting assumptions. Do not resolve uncertainty by creating replacement sessions or a new bus.

## First bounded work order

**Goal:** discover an existing session, inspect its associated files, and open it in the native terminal, with no automated agent input.

| Included | Explicitly excluded |
|---|---|
| Read-only discovery and selected bounded snapshots | Autonomous input, automatic Enter, or active prompt interception |
| Mapping to existing files and pins | New pin database or migration of the editor |
| Explicit human attach/open action | Killing, replacing or detaching other sessions |
| Clear connection/error state | Inferring task completion from terminal text |
| Tests with a disposable scratch session | RustDesk fork, custom transport, service installation or broad refactor |

Use existing shell infrastructure first. A new Rust/C++ component must solve an identified need, not merely satisfy the language preference. No GUI toolkit selection is a prerequisite for this first work order.

## Phase gates

### A. Discovery and native access

Implement only the missing link between current session discovery, associated files and native terminal access. Host, socket and target must remain visible enough to catch mistakes. A missing or ambiguous target is an error, not a reason to fall back to another pane.

**Exit:** acceptance tests A1–A6 below pass with recorded evidence.

### B. Reviewed file handoff

Only after a separate execution decision, reuse the existing contract for publishing a request and signalling a validated receiver. Transfer the file first, verify the remote content, then send the minimal pointer through the supported adapter.

Record publication, signal attempt, acknowledgement and task outcome separately. Preserve the current budget/deadline and outcome conventions instead of inventing parallel ones. Failed/uncertain transport must not trigger blind replay.

**Exit:** tests B1–B5 pass in a scratch environment before use with a working agent.

### C. Optional native panel or streaming view

Choose the interface only after A and B expose a concrete need. A Slint companion panel is one candidate; an embedded terminal is a distinct scope. Streaming observation requires correct parsing and bounded buffers, not merely appending received text to a widget.

A control-mode client receives framed commands and terminal-byte notifications, not semantic conversation records.[^T2] Check supported attachment flags and commands against the installed tmux manual.[^T3]

**Exit:** lifecycle, resource and target-identity tests still pass; the panel remains removable without changing the underlying workflow.

## Acceptance tests — planned, not executed

| ID | Test | Required observation |
|---|---|---|
| A1 | Discover with multiple sessions and non-default socket configuration | Correct host/socket/IDs; no silent default-socket substitution. |
| A2 | Open an existing session | The same process continues; no replacement and no forced detachment of another client. |
| A3 | Close the viewer or adapter, then reconnect | Remote session remains; no input is replayed. |
| A4 | Rename or remove the target; restart the scratch tmux server | Stale identities are rejected; the user must select a valid target again. |
| A5 | Observe alongside a human client | No unsolicited input, resize or focus change; relevant hooks are understood. |
| A6 | Access files and pins | Existing IDs/anchors survive; remote/local path mapping is explicit. |
| B1 | Publish a request containing Czech text, spaces, quotes and multiline content | Receiver-visible content matches the reviewed request; no shell interpolation. |
| B2 | Interrupt the connection around the signal step | The result distinguishes failure from uncertain delivery; no automatic resend. |
| B3 | Present a stale result or misleading terminal success message | It is not accepted as completion for the current request. |
| B4 | Receiver is a shell, modal dialog, or has unsent human input | Automatic typing is refused or handled through a verified safe existing adapter. |
| B5 | Repeat a previously attempted request intentionally | Behaviour follows the actual receiver contract; no invented exactly-once guarantee. |
| C1 | Flood output or pause the consumer | Memory stays bounded; lost continuity is explicit and resynchronization is labelled. |
| C2 | Crash/restart the panel | Notes/results remain recoverable from files and direct CLI access still works. |
| C3 | Inspect outputs, logs and connectivity | No new unapproved listeners, credential copies or uncontrolled transcript logging. |

Use harmless processes and isolated scratch sessions for destructive failure tests. Do not restart a production tmux server to prove A4.

## Required implementation evidence

Leave a focused diff, actual commands and outcomes, tests for parsing/addressing/reconnect boundaries, and a concise handoff. Record any environment-specific skips. Show how to stop/remove the new viewer without deleting remote sessions or task files.

A successful command exit is not sufficient evidence of correct targeting, safe reconnect or accepted task execution. Conversely, document-generation validation in this pack is not a runtime test of the proposed relay.

## Stop conditions

Stop the proposed change and report the conflict when the existing contract cannot be established, the receiver is ambiguous, notes might be executed as shell input, another agent owns the relevant modifications, or the first experiment unexpectedly requires a new transport/service.

Treat RustDesk extraction, full terminal emulation, editor replacement and a new orchestration database as separate decisions—not hidden prerequisites discovered halfway through a small task.

## AI HANDOFF

**Goal:** Preserve the research and a narrow route toward session navigation and deliberate file handoff.

**Current state:** Seven Markdown documents have been prepared. No target host or repository has been inspected; no new relay/UI code exists as a result of this task.

**Decisions made:** The pack separates desktop access, terminal transport, UI and component reuse. The proposed implementation retains existing sessions/files and begins with discovery/native access. No toolkit or migration was approved by this handoff.

**Files changed:** New artifact files `00_README.md` through `06_SOURCES_AND_EVIDENCE.md` in this delivery folder. No project source files, uploaded guidance files, configuration or services were changed.

**Validation performed:** Primary documentation was checked. Artifact metadata, Markdown structure, source references, local links and ZIP contents were validated during packaging. No target commands, application builds, network tests or benchmarks were run.

**Open questions / risks:** Actual repository contract, pin format, host/socket identity, installed versions, session lifecycle configuration, safe receiver signalling, package compatibility, measured resource use and eventual licence choice.

**Recommended next move:** Once implementation is requested, inspect the actual repository and execute only the Phase A discovery/native-access experiment first.

**Agent:** Wave

## Primary sources

Checked on 2026-10-23. Documentation is evidence of documented capability, not a test of an installed build.

[^T2]: [tmux control-mode protocol](https://github.com/tmux/tmux/wiki/Control-Mode).
[^T3]: [tmux manual, OpenBSD publication](https://man.openbsd.org/tmux).
