<!-- Controller preservation metadata: native role researcher; observed handle
/root/terminal_approaches_research; consolidated final reply, following scope correction.
Original broad recommendation is superseded by this handoff; actual model/effort not
independently observed. Reply body below is preserved verbatim. -->

# Terminal task-shell research — consolidated handoff

**Question.** What can give Claude Code and Codex a persistent, human-shareable task shell or interactive program separate from the agent conversation, with file-authored requests and an operator-selected permission regime?

**Frame / evidence standard.** Research-only, retrieved 2026-11-17; no vendor CLI, container, or live-session action occurred. **OBSERVED** claims are local repository artifacts. **SOURCE** claims are current primary documentation. **INFERENCE** marks a design conclusion needing a probe.

## Local constraints

- **OBSERVED:** L3/L4 reject `tmux send-keys` as regulated delivery and distinguish protocol truth from terminal tooling. L17 assigns ovitmugen view/layout and protected process-lifetime ownership; Termbrana is currently read-only observation, not a sender or raw-PTY owner.
- **OBSERVED:** `docs/ARCHITECTURE.md` says content-in-files / PTY-as-impulse is a **plan, not a lock**. Do not overstate L14 as locking the impulse mechanism.
- **OBSERVED:** `apps/session-console/contracts/live.md` already treats ttyd as a fixed rendering/attach seam, with target revalidation and no queued-input or reconnect replay. It cannot be silently promoted into a task broker.
- **OBSERVED:** Termbrana distinguishes raw PTY bytes, rendered ANSI/text, and derived observations. A terminal view is not raw-byte evidence and neither is semantic task receipt.

## Native task-shell matrix

| Facility | Documented task-shell facts | Human attachment to that same task terminal | Status |
|---|---|---|---|
| Codex unified `exec_command` + `write_stdin` | **SOURCE:** long-lived PTY for streaming, REPLs, interactive sessions; resumable command execution is stable and enabled by default, subject to managed requirements. | **UNKNOWN:** reviewed documentation does not specify a human terminal attach endpoint, concurrent writers, or attach/reconnect semantics. | Strong native process candidate; qualification needed. |
| Codex App Server `command/exec` | **SOURCE:** sandboxed command execution with persistent process follow-ups for stdin, resize, terminate, and streamed output. | **UNKNOWN:** a client could render the API, but that bridge is not documented as native human terminal attach. | Candidate manager/control API. |
| Codex App Server `process/*` | **SOURCE:** experimental PTY process spawn/stdin/resize/kill/output API. | **UNKNOWN:** no human attach documented. | Unsafe default: explicitly outside Codex sandbox. |
| Claude background Bash | **SOURCE:** asynchronous background task ID; output written to file; cleaned up when Claude exits. | **UNKNOWN for full terminal attachment:** no documented stdin/resize/renderer API. Agent View can direct a reply to an active shell job as typed input. | Narrow mediated input path, not a shared terminal. |
| Claude Agent View / `claude attach` | **SOURCE:** persistent background Claude session and conversation attach. | Attaches the Claude session, not a separately specified shell/TUI endpoint. | Adjacent, not substitute. |
| Zellij terminal/web attach | **SOURCE:** persistent session, local/remote attach, window closure without necessarily ending session, resurrection. | Yes, to a Zellij-managed task session. | Actual reusable terminal manager; does not establish vendor control or authorization. |

## Primary sources

- **SOURCE:** [Using GPT-5.3-Codex — OpenAI API](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.3-codex), retrieved 2026-11-17, shell-tool guidance: `exec_command` launches a “long-lived PTY”; `write_stdin` supplies additional keystrokes/polls. It does not describe human attach.

- **SOURCE:** [Configuration Reference — ChatGPT Learn](https://learn.chatgpt.com/docs/config-file/config-reference), retrieved 2026-11-17, `features.unified_exec`: resumable execution is stable and enabled; managed requirements can remove resumable processes and `write_stdin`. This is tool-session persistence, not proof of external human attachment.

- **SOURCE:** [Codex App Server — ChatGPT Learn](https://learn.chatgpt.com/docs/app-server), retrieved 2026-11-17, “Command execution” and “Process execution”: `command/exec` can expose process stdin/resize/terminate/output under server sandbox. `process/*` is experimental and runs “outside Codex’s sandbox.” The same page’s remote TUI section attaches the Codex **conversation UI** to App Server, not a human terminal to a spawned process.

- **SOURCE:** [Interactive mode — Claude Code Docs](https://code.claude.com/docs/en/interactive-mode), retrieved 2026-11-17, “Background Bash commands”: tasks run asynchronously, have IDs, write output to files, and are cleaned up on Claude exit. The reviewed page contains no documented generic stdin/resize/attach API.

- **SOURCE:** [Agent View — Claude Code Docs](https://code.claude.com/docs/en/agent-view), retrieved 2026-11-17, attach/dispatch and supervisor sections: an Agent View reply to a shell job reaches its terminal “as typed input”; attaching opens the interactive Claude session. The supervisor deliberately does not restart an active shell command, since it could re-run it.

- **SOURCE:** [Claude Code CLI reference](https://code.claude.com/docs/en/cli-usage), retrieved 2026-11-17: `claude attach` attaches a background session; it does not specify a shell-task endpoint.

- **SOURCE:** [Zellij Terminal](https://zellij.dev/documentation/zellij-terminal.html) and [Web Client](https://zellij.dev/documentation/web-client.html), retrieved 2026-11-17: attach can select a named session; closing a terminal window can keep its session alive; remote/web clients can attach or resurrect. Process incarnation after resurrection remains distinct and must not be guessed.

- **SOURCE:** [Docker bind mounts](https://docs.docker.com/engine/storage/bind-mounts/) and [Docker security](https://docs.docker.com/engine/security/), retrieved 2026-11-17: mounts are writable by default unless read-only, and daemon/socket authority can imply host-root-equivalent control. Containerization is therefore an optional isolation axis, not a default authorization answer.

## Four approach families

| Family | What persists | Strength | Main limitation |
|---|---|---|---|
| 1. Native facility | Vendor-owned process/tool session | Lowest new mechanism; Codex persistent exec/control is documented | Human attach to the same shell is unproven; Claude’s documented shell interaction is conversation-mediated |
| 2. Reusable manager + qualified bridge | Existing terminal-manager session/PT Y | Zellij-like manager can own a real task TUI and human attachment | Bridge must be separately qualified for agent interaction, identity, resize, signals, and security |
| 3. File-fed fresh jobs | Request artifact, not terminal | Good for batch/disposable execution; container may fit | Fundamentally poor fit for persistent cwd/env, alternate screen, REPLs, or long-lived interactive programs |
| 4. File-fed persistent worker | Worker/manager task session | Can retain a task shell while files carry requests | A candidate only; lifetime, target binding, duplicate handling, and authorization remain unbuilt/open |

**INFERENCE:** a disposable container/job cannot replace a living interactive terminal without retaining the process and its terminal state—at which point it becomes family 4. Containers can support either family 3 or 4, but mounts, Docker socket, credential forwarding, namespaces, and network determine whether isolation is real.

## Boundaries and unknowns

- **SOURCE/OBSERVED:** raw-byte ownership belongs to the PTY-master owner from spawn. That may be an existing manager, a vendor facility with a qualified API, or a future adapter; it need not be a Nablarva-created PTY. Renderers/scrollback observers normally see a later parsed representation.
- **UNKNOWN:** whether Codex unified exec or `command/exec` has process identity durable enough for human reconnect, alternate-screen fidelity, external attachment, shared resize behavior, or exact Ctrl-C/EOF semantics.
- **UNKNOWN:** whether Claude’s shell-job input route handles full-screen TUIs, preserves input across Agent View detach, supplies readable output in real time, or exposes a safe interrupt/EOF distinction.
- **UNKNOWN:** concurrent human/agent writers for any native facility. No reviewed source establishes arbitration; no input-lease mechanism is adopted by this report.
- **INFERENCE:** a request file, prompt, Markdown policy, or terminal output is not executable authorization. Vendor permission/sandbox controls apply only in documented scope; task-shell authorization needs demonstrated OS/process controls if built.

## Narrow recommendation

**ADOPT nothing new architecturally. QUALIFY existing facilities first.** Treat Codex unified exec/`command/exec`, Claude background shell jobs, and Zellij as distinct candidates, not one interoperable platform. Agent View, `claude attach`, `codex queue`, Codex threads, and remote conversation TUIs remain useful adjacent controls but are not answers to the shared-task-shell question.

Compatibility with current project ownership is conditional: an existing native manager can be proposed as a task-process owner only if it does not displace ovitmugen’s view/layout and protected-lifetime role without a separate decision. Zellij is presently the documented reusable task-terminal manager; Termbrana remains observation-only. No broker architecture, request schema, inbox/outbox, lease, container stack, or delivery protocol is selected here.

## Smallest next experiment

If separately authorized, run one isolated, disposable per-facility qualification—not a live relay:

1. **Codex:** start a single task-shell fixture through unified exec or `command/exec`; record process identity, cwd/env, TTY resize, raw output, stdin, Ctrl-C, EOF, exit, and post-disconnect behavior. Test whether any supported human attach exists without inventing one.
2. **Claude:** run one bounded interactive fixture as a background shell job; exercise Agent View input, `claude attach`, detach, output visibility, Ctrl-C/EOF, and cleanup. Record whether it is a terminal attachment or merely message-mediated input.
3. **Zellij:** attach/detach a fixture TUI and separately record resize, alternate-screen, process survival, and resurrection-as-new-incarnation behavior.

A native facility that lacks a documented or measured human attach surface remains a process/control candidate only; it does not justify a project lock or an automatic custom bridge.
