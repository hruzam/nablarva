---
title: SSH/tmux relay — boundaries, state and interaction
date: '2026-10-23'
author: Wave
language: en
type: architecture brief
scope: terminal relay
status: advisory; not approved repository canon
source_check_date: '2026-10-23'
host_validation: not performed
new_work_status: documentation only
---

# SSH/tmux relay — boundaries, state and interaction

## Recommended boundary

Extend the current relay instead of introducing a remote-desktop transport. The execution host owns the agent processes, tmux server, repositories and credentials. A terminal, mobile device or optional panel observes and interacts with that state; it does not become the session owner.

```text
Human terminal                       Optional Termbrana panel
      |                                 |             |
 existing SSH                        observation   reviewed action
      |                                 |             |
      +---------------- execution host ---------------+
                                      |
                               existing tmux server
                                      |
                               existing CLI sessions
                                      |
                   request/result files + native transcript files
```

This is a design proposal. Inspect the live repository contract before choosing paths, fields or adapter commands.

## What existing tmux/SSH mechanisms provide

An attached tmux client can detach while its session continues, and multiple clients can access the same session.[^T1] This is continuity across client disconnection, not a promise of survival through host reboot, server termination or session-destroying configuration.

The tmux command interface provides discovery, pane capture and targeted input. Server sockets can be selected explicitly; the installed manual is the authority for supported flags.[^T3]

Control mode exposes normal tmux commands, framed responses and asynchronous notifications over a textual channel. `%output` identifies a pane and carries escaped terminal bytes, potentially containing escape sequences and non-UTF-8 data. Its output scope is the attached session, not an automatic stream of every session on the host.[^T2]

OpenSSH supports remote commands; `-t` requests a pseudo-terminal, while `-T` disables allocation.[^T4]

### Illustrative commands — not executed

`HOST_ALIAS`, `SESSION_NAME` and `%123` are placeholders. Discover real values and the correct tmux socket first. These examples address the default socket only.

```sh
# Discover sessions without attaching an interactive viewer.
ssh HOST_ALIAS 'tmux list-sessions'

# Explicit IDs; use actual discovered values for later targeting.
ssh HOST_ALIAS 'tmux list-panes -a -F "#{session_id} #{window_id} #{pane_id}"'

# Human interaction: attach to an existing session, without -d.
ssh -t HOST_ALIAS 'tmux attach-session -t SESSION_NAME'

# Machine-protocol experiment; not a normal terminal display.
ssh -T HOST_ALIAS 'tmux -C attach-session -E -f ignore-size -t SESSION_NAME'

# Bounded snapshot of a selected pane, not a transcript export.
ssh HOST_ALIAS 'tmux capture-pane -p -t %123 -S -100'
```

`-E` avoids the attach-time environment update; `ignore-size` keeps that client from affecting other clients' dimensions. A normal `-r` attachment also sets read-only behaviour, but these flags are not a replacement for a server-side authorization boundary.[^T3] The machine example has command authority and must only be driven by a trusted, narrowly constrained adapter.

## State ownership: four separate things

| State | Authority | Panel behaviour |
|---|---|---|
| Living process/session | Existing host processes and tmux server | Discover and attach; do not create replacements silently. |
| Task request and outcome | Existing project bus/runbook files | Display and validate against the actual contract. |
| Terminal view | tmux observation | Label as a view or snapshot, never as complete task history. |
| Conversation history | Native transcript files where available | Read separately, with provenance; never edit a transcript to inject a request. |

Connection state, visible activity, request delivery and task completion must remain independent. “Connected” does not mean “ready”; “input sent” does not mean “accepted”; a printed success phrase does not establish a completed task.

## Proposed adapter contract

Start with the smallest existing Bash/shell integration that can prove the workflow. Introduce Rust or C++ only where a parser, concurrency requirement or GUI integration justifies it.

**Observation:** discover sessions/panes, inspect selected files, and obtain bounded pane snapshots. Validate the target's host, user, server/socket and current pane identity. Treat names as labels; invalidate cached identities after server restart or lost identity continuity.

**Human access:** open the existing terminal at the chosen session. Preserve native vendor commands, hotkeys and direct intervention. Do not detach another client as a side effect.

**Intent:** preserve existing Sublime pins, their file/position anchors and thematic batches. Map them to a selected session without importing a competing pin database.

**Delivery, later:** publish the reviewed request to the receiver-visible filesystem, verify the intended content is present, then signal the known receiver through its existing supported adapter. A local pathname is not automatically meaningful on the remote host. Keep transfer, signal and acknowledgement separate.

These are conceptual operations, not names of implemented commands or new protocol endpoints.

## Delivery and reconnect safety

Before enabling any automated send, inspect the existing addressing, budget, deadline and outcome contract. Reuse it; do not introduce a second set of terminal states.

A proposed safe sequence is:

```text
review request + exact target
        -> persist under existing contract
        -> verify receiver-visible file
        -> deliberate signal to validated receiver
        -> observe acknowledgement/result through the contract
```

If transport fails after a possible send, report **delivery uncertain**. Reconnect must rediscover state, not automatically replay text or the last Enter key. Exactly-once task execution cannot be inferred from an SSH acknowledgement; any deduplication belongs at the receiving contract boundary.

A pane may have returned to a shell, be showing a permission dialog, or contain unsent human input. Refuse automated typing when the receiver cannot be established safely. Begin with a harmless scratch session, never a production agent.

## Observation must not become hidden control

For a streaming prototype, implement command framing, octal decoding, asynchronous events and bounded buffering; preserve byte provenance and sanitize previews. tmux documents output flow control and recovery by recapturing pane state.[^T2] A recovered view must be marked as resynchronized, not portrayed as a lossless replay.

Proposed safeguards: no unsolicited resize, session switch or input; no interpretation of displayed content as a command; no automatic clipboard actions; no full-screen stream archive by default. Treat filesystem links and terminal text as data. Test whether attach/detach triggers existing user hooks before claiming an observer is non-disruptive.

SSH command quoting is a separate boundary: invoking a local process with an argument array does not by itself make an interpolated remote shell command safe. Use validated identifiers and fixed operations; do not concatenate notes into command strings.

## Adjacent tools, not migration requirements

**tmate** is a tmux fork for instant terminal sharing; its SSH-server implementation is available for self-hosting.[^M1][^M2] It is worth examining for human pairing, not a reason to replace the existing sessions.

**WezTerm** supports ordinary SSH as well as its own remote multiplexer. Its SSH-domain multiplexing requires a compatible remote WezTerm installation.[^W1] Distinguish using it as a terminal from adopting its session-management system.

## First experiment

Inventory existing sessions, select one, inspect associated files, and open it in the existing terminal. Prove that closing and reconnecting the observer leaves the process and human session intact. Only then test a reviewed file handoff in a scratch environment.

See [implementation handoff](05_IMPLEMENTATION_HANDOFF.md) for acceptance criteria and [native UI options](03_NATIVE_UI_OPTIONS_BRIEF.md) for the optional presentation layer.

## Primary sources

Checked on 2026-10-23. Documentation is evidence of documented capability, not a test of an installed build.

[^T1]: [tmux getting-started guide](https://github.com/tmux/tmux/wiki/Getting-Started).
[^T2]: [tmux control-mode protocol](https://github.com/tmux/tmux/wiki/Control-Mode).
[^T3]: [tmux manual, OpenBSD publication](https://man.openbsd.org/tmux).
[^T4]: [OpenSSH client manual](https://man.openbsd.org/ssh).
[^M1]: [tmate project](https://github.com/tmate-io/tmate).
[^M2]: [tmate self-hosted SSH server](https://github.com/tmate-io/tmate-ssh-server).
[^W1]: [WezTerm multiplexing and SSH domains](https://wezterm.org/multiplexing.html).
