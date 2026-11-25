# RUNBOOK: session-window-X1-surface

> A thin frame, written on 2026-11-25 by the eSharp manager at Majkee's request, so that the lead of group 1 does not start from
> an empty page. The lead owns this file from the moment Majkee gives it the pen, and may change it until it has read the plan
> back to him. From then on it is fixed. Where things stand is in `STATUS.md`, never here.

```yaml
goal: >
  One witnessed packet that shows what a status surface for Majkee's CLI sessions can really display today, by which route,
  and what each route costs — so that the first small version of the session-window helper is chosen on evidence. It serves
  the decision recorded as T11 on 2026-11-21: a flexible, vendor-neutral status line that can grow to show the clock, alerts
  and other operator information comes first; session generation from a scheme is secondary.
gate: >
  Majkee records GO or STOP on a witnessed status-surface packet — what the installed Claude status line really receives and
  shows; the same fields for one Codex session by reading only; the three display routes (native status line · second tmux
  status row · metadata pane) tried side by side on a separate tmux server, each checked for whether inspection and one
  pointer line still reach the intended pane; one recommended smallest first version, with the place for the chess clock.
  No helper is built yet.
participant_1: [lead.seswin, {brand: claude, model: set by Majkee at launch, effort: set by Majkee at launch}, host: home, role: "head and status_owner — the flight build, window `lead.seswin`; plans, writes the assignments, verifies, commits by file name; asks for every release"]
participant_2: [audit.seswin, {brand: codex, model: set by Majkee at launch, effort: set by Majkee at launch}, host: home, role: "a fresh Oraculum session, window `audit.seswin`; thinks with the lead and criticises honestly while the work is conceptual; witness of the packet when the sandbox part arrives; writes no code herself"]
participant_3: [supervisorCli, {brand: codex, model: gpt-6.1-sol, effort: max}, host: home, role: "one fresh seat shared with the relay line and, later, with group 2; window `supervisorCli`; pushes on a head's poke, runs bounded work a POINT names, makes caches on request"]   # model and effort as his roster names them
participant_4: [majkee, {brand: human}, host: home, role: "every release; starts the seats and the sample sessions; trust and permission dialogs; GO or STOP"]
participant_5: [exec, {brand: codex}, host: home, role: "his decision desk, shared by all lines, window `exec`; takes him through a sheet and records his words"]
participant_6: [manager, {brand: claude}, host: home, role: "the eSharp manager, window `engineer`; carries what one group needs from another and orders the sheets to Majkee; holds no pen in this bed"]
status_owner: lead.seswin
schema_note: runbook GUIDE verified 2026-11-19 · status GUIDE verified 2026-09-05 · bus file-poke chapter verified 2026-11-19, provisional
```

## Why this session exists

The line's first bed gathered substrate under a provisional gate that Majkee never confirmed; it is closed for the record. Since
then his priority moved from launch recipes to the status surface (T11), the chess clock was deferred to this line (T6), and
three display routes stand side by side with one open conflict: the documentation promises a multiline status line with more
fields, and the installed one was seen to cut its text. This session finds out what is true before anything is built. It is
group 1 of the experimental shape `eSharp`; group 2 (the shared terminal) starts after this group has closed a cycle.

## Fixed facts

- **Opened on his word.** Bed name and the closing of the old bed: sheet 1, E1. Gate: sheet 1, E2 — "confirming". Both verbatim in
  `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp.decisions.majkee.2026-11-22.md`, section 7. Generation X, host home.
- **Roster, in his syntax** — `seat|who it may spawn`; `a-><b> : [task]` means a spawns b for that task. Three seats, and he wants
  no more for a bigger task. His file: `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/roster-proposal.eSharp.md`.
  - `lead.seswin|houston|trajectory|delta|epoch`
  - `audit.seswin|houston|astrobley` — "Can provide tests" in his roster is the leave to commission tests from `astrobley`.
  - `supervisorCli|houston|astrobley|oraculum`
- **Where things run.** Every seat lives in `helloWorld` on the usual tmux server. What is built and tested lives only on the
  server `tmux -L session-window` and in the scratch folder `~/.cache/nablarva/session-window/`.
- **The sandbox release is proposed, not given.** Its wording (sheet 2, A3): "Inside its own tmux server and its own scratch
  folder (`~/.cache/nablarva/<line>/`), with harmless commands, the group may build, run and stop what it needs without asking —
  including typing into its own test panes there. Everything outside — `helloWorld`, any seat's pane, your daily shell, ia-sync
  and its deploy, office — returns to you. Sample CLI sessions are started by you from a prepared script, as in the relay
  probes." Until his yes is in a decision file in this bed's `raw/`, steps 3 and 4 below are NOT RUN and nobody starts that server.
- **What needs no release:** reading, the field list, the plan, the sheets, the spawns the roster names, and coordination pokes —
  those are the lead's own call (`/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/raw/decision.majkee.pokes-and-continuity.2026-11-22.md`).
- **Never into Git** — this repository's GitHub remote is public: caches, raw pane captures, transcripts, raw status-line input
  records, personal notes. They stay in the scratch folder. The bed gets field names, types, cleaned examples and a pointer line.
- **Caches** (sheet 2, B2): made by `supervisorCli` on request, at `~/.cache/nablarva/session-window/CACHE.<posture>.md`. A cache
  is never authority — STATUS wins — and it does not travel to another host.
- **Text that must be read or copied is written whole and wrapped, never cut at the pane edge** (his E6). Every route is checked for it.
- **The seam to group 2 is files only.** This group writes the one list of status fields; group 2 reads it for its own status
  line. Majkee also wants to be told when somebody tries to send a command to a shared terminal that is closed, or not expected
  to be open for that sender (decisions, section 8). The packet says where such a notice would be shown; it builds nothing for it.
- Versions when this was written: Claude Code 2.1.332, codex-cli 0.171.0, tmux 3.7c. Read them again on the day.

## The order of work

0. **Bind.** Majkee starts the seats and gives the lead the pen, written into a decision file in this bed's `raw/`. The lead
   checks the party against live tmux, writes its roster with the real models, and rewrites `STATUS.md` as its own.
1. **Read, and write the field list** — no release needed. `raw/fields.<date>.md`, one row per field: model and effort, working
   directory, context left, session name, session id, transcript path (his order), then the slots he wants it to grow into —
   clock and timers, poke status, alerts. For each: where Claude gives it, where Codex gives it, how fresh it is, known or not
   known. Sources, by reading: the deployed `/home/hruzam/ia-sync/claude/hooks/statusline.sh`, the official documentation with
   its date (an `epoch` spawn), and for Codex what a session shows without anything typed into it.
2. **Read back, then ask.** One sheet through the exec desk: the plan read back, the sandbox release as worded above, and the
   script that starts the sample sessions. `audit.seswin` reads the sheet first, once.
3. **Capture what is really received** — needs the release. Majkee starts one sample Claude session and one sample Codex session
   from the prepared script, on the sandbox server. The Claude sample gets its own settings file from the scratch folder
   (`claude --settings <file>`), whose status-line command also writes its input there; the deployed hook is not touched.
   The Codex sample is read only.
4. **The three routes side by side** — needs the release. The same checks for each: what it shows in a narrow and in a wide
   pane, and whether long text is wrapped or cut; whether `capture-pane` inspection still reads the intended pane; whether one
   pointer line still reaches the intended pane; whether tmux marks the agent's window as busy; how it refreshes and what that costs.
5. **The packet.** `packet.status-surface.<date>.md`: one row per check — PASS, FAIL or NOT RUN — written by the witness from her
   own look. Then one recommended smallest first version, which answers: where the chess clock sits; one helper per CLI or one
   dashboard; the helper as a window of its own, started from scratch, and what the old zsh helper keeps as a control window;
   how the helper knows which CLI it serves (the manager's view: from the launch recipe, not by reading the pane — the lead
   may disagree); how the record grows (timers, poke status, context left per vendor); where a shared-terminal notice would show.
6. **The gate.** One sheet takes the packet to Majkee for GO or STOP. Sample sessions are closed by the hand that started them.

## prompt-0 — lead.seswin

```text
You are lead.seswin, the lead of the session bed /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface —
group 1 of the eSharp shape. Start with your working directory in /home/hruzam/unikuklatrix/nablarva. Read AGENTS.md there and
its read chain, then this bed's STATUS.md, then this RUNBOOK, then section 7 (the read-first list) of
/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/brief.session-window.2026-11-22.md.
You do not hold the pen until Majkee says so and his words are in a decision file in this bed's raw/.
You write STATUS.md, the assignments in _bus/, your verdicts and the commits (by file name; supervisorCli pushes on your poke).
You may spawn houston, trajectory, delta and epoch, and you do not work alone: long reads, sweeps and checks go to a child.
Nothing is built, started or typed on the sandbox server until Majkee has given the sandbox release in his own words; you ask
for it on one sheet through the exec desk, after audit.seswin has read the sheet. Coordination pokes are yours to send.
Nothing private goes into Git — the remote is public. Never read .majkee/ or .hlm/.
What you need from another group, or it from you, goes through the eSharp manager (window `engineer`): a file and one pointer line.
Done when Majkee has recorded GO or STOP on the packet.
```

## prompt-1 — audit.seswin

```text
You are audit.seswin, the auditor of /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface — an Oraculum
session of the other brand. Working directory /home/hruzam/unikuklatrix/nablarva. Read AGENTS.md there and its read chain, then
this bed's STATUS.md and RUNBOOK.md. While the work is conceptual you think with the lead and criticise honestly: the lead asks
by a POINT in this bed's _bus/, and you answer with one file at the path it names — your verdict first, then your points with
file and line, strongest first. When the sandbox part arrives you are the witness: you look yourself, you do not read the lead's
account before yours is written, and you write PASS, FAIL or NOT RUN for each check of the packet. You write no code; a test you
want is commissioned from your child astrobley and named in your file. You may spawn houston and astrobley. You read each sheet
that asks Majkee for a release, once, before it goes to the desk. No pane input except one reply bell after a look. Git
read-only queries are allowed. Nothing a person or a project wrote on a screen goes into a file in the repository.
Never read .majkee/ or .hlm/.
```

## prompt-2 — supervisorCli

```text
You are supervisorCli, one seat shared by the lines of /home/hruzam/unikuklatrix/nablarva. Your brief is
/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/brief.supervisorCli.2026-11-25.md — read it whole, then AGENTS.md in
/home/hruzam/unikuklatrix/nablarva and its read chain. For this bed you act only on a POINT in
/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/_bus/ that lead.seswin names in a poke, and you
return to the path that POINT names.
```

## Communication protocol

The shared rule is `/home/hruzam/reposoma/raw.guides/bus/res/file-poke.md` (provisional). The doors and their look-first steps are
the table in `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/RUNBOOK.md`, section "Communication protocol"; they
hold here unchanged. One labelled line, never content: `[<tag> <id>] from <who> -> read <absolute path> ; ack: <none|per file>`.
The file is the truth; a bell is a hint from a seat and never Majkee's word. Every poke goes into `raw/pokes.log.md`. If the
lead opens two branches from one decision, the coordinates are in `/home/hruzam/reposoma/raw.guides/runbook/res/fanout-turns.md`.
The draft chapter on cross-vendor seats would name this exchange `mail`; the participant lines carry a role instead, as in the relay bed.

## Known constraints + destructive holds

- **L12** — branch `core`, plain pull and push, never `pull --rebase`, never force. Commits by file name, never a folder.
- **L20, L21** — what a try shows authorizes nothing; every activation and every delivery needs its own release.
- **L4, L17** — typing into a pane is a recorded death as a way to deliver. Inside the sandbox it is covered by the sandbox
  release only, and only for the group's own test panes. No seat's pane and no pane of `helloWorld` is ever a target of a try.
- **L22** — `.majkee/` and `.hlm/` are never read or listed. The home of the helper there is Majkee's to name.
- **The deployed status line is not changed:** `/home/hruzam/ia-sync/claude/hooks/statusline.sh`, `/home/hruzam/ia-sync/claude/settings.json`,
  the live `/home/hruzam/.claude/settings.json`. No `deploy.sh`.
- **`helloWorld` is not rearranged:** no option, status row, pane or window of the usual tmux server is changed for a test.
  Never `tmux kill-server`, on any server; the sandbox is stopped session by session, by name.
- A trust or permission dialog on a sample is cleared by Majkee's hand only. A process nobody started stops the run.
- ovitmugen (`/home/hruzam/ia-sync/zsh/session/ovitmugen.*`) is read as evidence and not changed; it stays a separate client.
- The closed bed `/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/` is read, never written.
- Majkee's own files are never staged: `eSharp/answers.sheet-1.majkee.2026-11-22.md`, `eSharp/roster-proposal.eSharp.md`.
  Never opened: `vist-X0-helloWorld/majkee-personal-notes.md`, `relay-X1-probes/CACHE*.md`.

## Acceptance evidence

- The field list in `raw/`, with the source and the date of every row.
- Majkee's sandbox release in his own words, in a decision file in `raw/`, before any step on the sandbox server.
- The packet, with the witness's row for every check; raw records and captures in the scratch folder, with one pointer line here.
- Majkee's GO or STOP, in his words, in a decision file.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X.ledger.md` — the line ledger: open points, the chess clock pointers
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp.decisions.majkee.2026-11-22.md` — his words: sections 7 (E1, E2, E4, E6) and 8
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/answers.sheet-2.majkee.2026-11-25.md` — A3 the release; B1 to B5
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/brief.session-window.2026-11-22.md` — the reader's brief; its section 7 is the read-first list
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/` — the substrate; `goal-substrate.2026-11-13.md` (fields, widths), `handoff.senior-advice.trajectory.2026-11-14.md` (rule 3, the second status row)
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/raw/inventory.relay-x1-helpers.2026-11-23.md` — 46 helpers the relay bed made; what exists already
- `/home/hruzam/unikuklatrix/nablarva/.dev/_backlog/termpanum-session-tracker/00_HANDOFF.md` — myShell's tracker proposal
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/goals/G10.friendly-reminder.md` — the chess clock, as defined
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp.board.md` — the shared seats and what one group needs from another
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — locks L4, L12, L17, L20, L21, L22
- `/home/hruzam/reposoma/raw.guides/bus/GUIDE.md` · `/home/hruzam/reposoma/raw.guides/status/GUIDE.md` — POINT, RETURN, VERDICT; the shape of STATUS

observations_read: none exist under `/home/hruzam/unikuklatrix/nablarva/.dev/observations/session-window*`. The closed bed is not
pruned and holds no observation file. The manager's own notes on the eSharp shape:
`/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/observations.manager.2026-11-22.md`.

## What this session deliberately does not do

- It builds nothing: no helper, no chess clock, no reminder, no scheme files, no launch recipes.
- It changes neither ovitmugen nor the deployed status line, and it does not probe office or monitor.
- It does not decide where the helper lives — that is Majkee's.
- It delivers nothing to an agent: no relay, no bus integration. Delivery stays with VIST.
- It does not design the shared terminal or its permission gate — that is group 2.

## Provisional coordination carry-forward

- Shared coordination and retirement obligation: `/home/hruzam/reposoma/raw.guides/bus/res/file-poke.md`, §Carry-forward and retirement.
- Owning development line: `/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X.ledger.md`; the shared bridge is tracked at `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md`.
- At closure, account for the provisional dependency in the ledger and the successor's references until its recorded replacement disposition.
