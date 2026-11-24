# Shared-terminal organ: builders' handoff card

Version: 2, 2026-11-22. Replaces version 1 of 2026-11-19.
Status: design agreed, nothing built yet.
Reader: a CLI builder starting cold. Vendor does not matter.
Working name: "shared-terminal organ". Rename freely.
Changes in v2: amendments accepted from Wave's review (2026-11-19).
Wave's proposals that were not accepted are listed at the end.

## What it is

One organ of nabLarva. An agent that can write a file into the organ's
inbox can have a command run in a real, living terminal pane, and can
read the result back. The human shares the same pane and controls the gate.

    inbox -> gate -> exec pane -> result

It sits beside each CLI's native bash and does not replace it. Native bash
stays the right tool for one agent's quick, stateless command. Use this
organ when one of these matters:

- shared state: one shell where `cd`, a venv, an export survive between
  commands and between agents of different vendors
- a program the human must attend: ssh, sudo, a debugger
- one history of what every agent and the human ran, in one format

## Topology

Two panes, kept separate:

- **control pane**: runs the executor script and reads the approval key
- **exec pane**: a persistent interactive zsh, dedicated to the organ

## Decisions already made

Do not reopen these without the human.

- The exec pane is dedicated, not the human's daily shell. Hooks are
  active only there. If the organ breaks, his own terminal is untouched.
- The channel is vendor-neutral: files, a shell command, the send-keys
  doorbell. No vendor hooks and no local model in the required path.
- Same envelope as the existing CLI-to-CLI bus. The executor is one more
  consumer on the bus.
- zsh split: submit verbs are sourced bricks; the executor is a script in
  the control pane and fails loudly if the exec pane is missing.
- Keep it light. Build v0 first and stop. A cage around the organ is a
  failure too.

## Four conventions that replace a state framework

1. **The filename is the request id.** The submitter chooses it and holds
   it from the moment of submit.
2. **Directories are the states:** `inbox`, `inflight`, `done`, `denied`,
   `unknown`. Where a file sits is its status. Anyone can look up an id.
3. **Files are moved, never deleted.** A denied or discarded request is
   still findable under its id.
4. **An id that exists in any directory is refused.** A retry with the
   same id is a status lookup, never a second run.

## Build order

### v0: the first dependable slice

1. **Open / close.** The executor dispatches only while the human has
   opened the organ. Closing stops new dispatch. A command already running
   finishes and is still recorded. Files may land in the inbox while
   closed; they wait.
2. **Backlog on open.** On open, list what is waiting, with age and
   submitter. Run nothing until the human confirms or discards. Confirming
   the backlog only permits processing; each request still passes the
   gate. A discard is moved to `denied` with reason "discarded".
3. **Atomic submit.** A submitter writes to a temp name and renames into
   the inbox, on the same filesystem. A watcher event is only a wake-up:
   the executor scans the inbox on every wake-up and on start.
4. **Claim.** The executor moves the request to `inflight` and takes its
   sha256. From here the bytes are frozen: what was reviewed is what runs.
5. **Ask gate, by keypress.** The executor shows the id, the submitter,
   the exec pane's current directory and the command, with control
   characters made visible, then waits for a key in the control pane.
   Approval is never a file. This gate governs the cooperative path: it
   stops a write-only agent, not one that can send keys through tmux.
6. **Run by `source`, foreground only.** The executor sends one line,
   `source` plus the quoted absolute path of the frozen file. This keeps
   `cd`, exports, functions and options in the shared shell.
7. **The pane reports itself.** `preexec` and `precmd` hooks in the exec
   pane's zsh write begin, end, exit code, current directory and the
   shell's pid. Register them with `add-zsh-hook`, read `$?` first, keep
   them minimal. "Done" means the shell returned. The exit code is that of
   the last command in the file, not proof the task succeeded.
8. **Idle check.** Dispatch only when the last event from the current
   shell pid was a prompt. A prompt event from an older shell authorizes
   nothing. This is a heuristic, not a lock: it does not see a half-typed
   line or a second tmux client. The human is trusted not to fight the
   queue.
9. **A busy pane blocks the queue.** ssh, a debugger or a server in the
   foreground holds the pane. Nothing is sent into it. The human takes
   over by hand. v0 has no "start and release".
10. **Serial, FIFO, one executor.** Order is the executor's arrival order.
    A lock ensures a single executor per exec pane.
11. **Result before doorbell.** Write the result record, then ring. A
    missed bell loses nothing. Fields: id, submitter, hash, gate decision,
    outcome, reason, directory before and after, shell pid, exit code
    (empty when nothing ran), start, end, output path.
12. **Refusals are results.** Denied, discarded, malformed and duplicate-id
    requests each get a record with a reason.
13. **Restart recovery.** On start, anything found in `inflight` is moved
    to `unknown` and never re-run. If reporting from the pane disappears,
    stop dispatch and mark the running request `unknown`. Never invent an
    exit code.
14. **Method card, short.** A vendor-neutral skill for agents: when to
    choose the organ, how to submit, how to find a request by id. Three
    rules for the consumer: on timeout, look up the same id and never
    resubmit; do not rephrase and resend a denied command; "done" is not
    success, so verify the effect.

### v1: make it comfortable to live with

15. **Named operations and instant mode.** Automatic approval only for a
    few named, reviewed operations with checked arguments. Arbitrary shell
    stays in ask mode. Instant mode is an explicit opt-in per session and
    is shown in the status line. This replaces the string allowlist of v1
    of this card.
16. **Pause / resume.** Stops dispatch while the human works by hand in
    the exec pane, without closing the organ.
17. **Queue edit.** A waiting request may be edited in place; the hash is
    taken at claim, so this is safe. Withdrawing one is a verb that moves
    it to `denied` with reason "withdrawn". An `inflight` request is
    frozen.
18. **Interrupt.** Record "interrupt requested" first, then what was
    observed. Write "killed" only when the prompt came back.
19. **Launch kinds.** A background launch, or a launch in a second pane.
    Only the launch is observed, never the completion. A second pane does
    not inherit the living shell's state.
20. **Declared directory.** A request may state the directory it expects.
    A mismatch at dispatch returns a blocked result; the command is never
    rewritten to fit.
21. **Output.** Capture is the pane's stream, so attribution to one
    request is by time interval and is best effort; background output can
    overlap. The result carries a truncated tail and the path to the full
    log, with terminal escape sequences stripped.
22. **Status line.** A view of the directories, not a second source of
    truth: open, closed or paused, gate mode, current request, unknown
    work, counts.
23. **Readable queue.** An agent can see that the pane is blocked and hold
    back.
24. **Human typing is logged, best effort.** Direct typing always stays
    available and bypasses the gate. The hooks from rule 7 can log it.
    They do not see commands typed inside ssh or a REPL. If logging makes
    the build fragile, drop the logging, never the typing.
25. **Cleaning.** Owned by the executor; agents never clean. Bulky logs
    may expire. The small per-request records stay, since rule 4 of the
    conventions depends on them. Never clean `inflight` or `unknown`.
26. **Dry-run mode.** Gate and records work normally. The command is
    displayed, not evaluated. The result is marked simulated and has no
    exit code.

### v2: later, each needs its own decision

27. **Markdown runbooks.** A file whose fenced blocks are steps, each
    fence tagged with a step id. Step mode by default. Open point: who
    authorizes continuing to the next step.
28. **Typing gate.** A front layer the human types into, so his input
    becomes requests like any other. Try pause / resume first. It must
    never be able to take the terminal down.
29. **JSON-L store.** A rebuildable projection of the result records.
30. **Remote consumers.** An agent with no access to this host (a cloud
    chat session, for example) needs a bridge that carries requests in
    and records out. That bridge belongs to the bus, not to the executor.

## Security posture, stated plainly

- Every CLI runs as the human's user. Folder permissions keep out other
  users only. Keep the inbox non-world-writable anyway.
- Anything that can write to the inbox reaches the real shell, with its
  ssh agent and tokens, once the gate lets it through. That includes a
  write-only agent steered by content it read somewhere.
- The protection is: organ closed by default, ask mode by default,
  approval by keypress. These govern the cooperative channel. They do not
  isolate an agent that already has its own shell or tmux access.
- The submitter field is a claim, not proof.
- Frozen bytes do not freeze meaning: a command can read files that
  change, or resolve a different executable.
- The output log can capture secrets shown in the pane. Treat it as
  sensitive.

## Acceptance probes for v0

Run in a disposable session with harmless commands.

| Probe | Must be observed |
| --- | --- |
| A request does `cd` and exports a variable | The next request sees both |
| A request is denied, another discarded from backlog | Both are findable under their ids, with a reason |
| The file is changed after claim | The reviewed bytes run, not the changed ones |
| The human changes directory before approval | The prompt shows the new directory |
| Two executors start on one pane | Only one dispatches |
| The same id is submitted twice | No second run |
| The executor is killed after dispatch | The request ends in `unknown`, no replay |
| A foreground program holds the pane | The queue waits; nothing is typed into the program |
| The exec shell is replaced | An old prompt event does not authorize dispatch |
| The doorbell is missed | The result is still retrievable by id |

## Open question for the human

What does the existing bus already provide for ids, status and
correlation? Reuse it where it does; the conventions above fill only
what is missing.

## From Wave's review, not accepted for now

- A manual "review next request" action in place of the watcher. The
  watcher stays: reacting to a new file was the starting idea.
- Session sequence numbers, revision lineage, separate retention classes.
  The four conventions cover the need at this size.

## Prior art worth a look before building

agent-tmux (claim lock on a shared PTY), agent-mux (cross-pane messaging),
NTM (approvals and history over tmux), runme and mdsh (markdown blocks as
steps). These are leads from one search, not verified comparisons. Borrow
formats, not the platform.
