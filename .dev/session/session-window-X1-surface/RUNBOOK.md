# RUNBOOK: session-window-X1-surface

> A thin frame, written on 2026-11-25 by the eSharp manager at Majkee's request, so that the lead of group 1 does not start from
> an empty page. The lead owns this file from the moment Majkee gives it the pen, and may change it until it has read the plan
> back to him. From then on it is fixed. Where things stand is in `STATUS.md`, never here.
> The pen passed to lead.seswin on 2026-11-26 (`raw/decision.majkee.pen.2026-11-26.md`); its changes before the read-back
> answer its first read of the frame (`eSharp/_bus/07.lead.seswin.return.md`) and the manager's reply (`eSharp/_bus/09.manager.point.md`).

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
participant_1: [lead.seswin, {brand: claude, model: claude-opus-5-5, effort: xhigh}, host: home, role: "head and status_owner — the flight build; tmux `$44 | 0 lead @78 | %80`; plans, writes the assignments, verifies, commits by file name; asks for every release"]   # model and effort as launched, own record 2026-11-26
participant_2: [audit.seswin, {brand: codex, model: gpt-6.2-astra, effort: high}, host: home, role: "a fresh Oraculum session; tmux `$44 | 1 audit @79 | %81`; thinks with the lead and criticises honestly while the work is conceptual; witness of the packet when the sandbox part arrives; writes no code herself"]   # model and effort from her own session record, eSharp/_bus/08.audit.seswin.return.md:3
participant_3: [supervisorCli, {brand: codex, model: gpt-6.1-sol, effort: max}, host: home, role: "one fresh seat shared with the relay line and, later, with group 2; window `supervisorCli` in `helloWorld`; pushes on a head's poke, runs bounded work a POINT names, makes caches on request"]   # his roster says effort max; its footer showed high on 2026-11-26
participant_4: [majkee, {brand: human}, host: home, role: "every release; starts the seats and the sample sessions; trust and permission dialogs; GO or STOP"]
participant_5: [exec, {brand: codex}, host: home, role: "his decision desk, shared by all lines, window `exec`; takes him through a sheet and records his words"]
participant_6: [manager, {brand: claude}, host: home, role: "the eSharp manager; session `helloWorld`, window `eSharp`; carries what one group needs from another and orders the sheets to Majkee; holds no pen in this bed"]
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
  - `lead.seswin|trajectory|delta|epoch|assay` — the posture in his roster, chapter 2. His pen word widens it: "you may spawn
    whoever you want-need. You can even spawn your `houston` and `oraculum`" (`raw/decision.majkee.pen.2026-11-26.md`). The
    children he lists are in chapter 5 of the roster.
  - `audit.seswin|houston|astrobley` — "Can provide tests" in his roster is the leave to commission tests from `astrobley`.
    Houston is vendor-neutral, so either seat may spawn it for a question; the one whose context window can take the load
    spawns it (pen word, point 2).
  - `supervisorCli|houston|astrobley|oraculum`
- **Where things run.** Every seat lives on the usual tmux server: this group in its own tmux session `seswin` (windows `lead`
  and `audit`, one pane each), the shared seats in `helloWorld` (`supervisorCli`, `exec`, `eSharp`). A window name carries no
  dot — tmux reads a dot in a target as the pane separator; the nicks keep theirs. The tree and its reasons are in the
  decisions record, section 10; Majkee's own map is in his roster.
- **Where things are tried.** On the separate tmux server Majkee made himself on 2026-11-26: `tmux -L sandbox-server`, session
  `sandbox` (`$0`), three shell windows — `codex-sample` (`@0`, `%0`), `claude-sample` (`@1`, `%1`), `session` (`@2`, `%2`).
  Group 2 has a session of its own on the same server, `sandbox-terwor` (`$1`, window `terminal`, `%4`); the earlier fourth
  window `terminal` of `sandbox` is gone (seen read-only 2026-11-26 02:44 UTC). The session `sandbox` therefore serves only
  this group; the lead has asked Majkee to confirm that in words. Window and pane ids there are local to that server and can
  repeat ids of the usual one, so every command names the server, targets the session as `=sandbox`, and checks its target
  there before it changes anything. The server is still shared with group 2, so only options of the session `sandbox` and its
  windows are set, nothing global. Of his real tmux settings, what is a session or window option is copied into the test
  setup; what is a server option is not copied but listed in the packet as a difference, together with every other one. The
  scratch folder is `~/.cache/nablarva/session-window/`. His map: chapter 6 of his roster.
- **The sandbox release is proposed, not given.** Its wording (sheet 2, A3): "Inside its own tmux server and its own scratch
  folder (`~/.cache/nablarva/<line>/`), with harmless commands, the group may build, run and stop what it needs without asking —
  including typing into its own test panes there. Everything outside — `helloWorld`, any seat's pane, your daily shell, ia-sync
  and its deploy, office — returns to you. Sample CLI sessions are started by you from a prepared script, as in the relay
  probes." Until his yes is in a decision file in this bed's `raw/`, steps 3 and 4 below are NOT RUN and nothing is run or typed on that server.
- **What needs no release:** reading, the field list, the plan, the sheets, the spawns the roster names, and coordination pokes —
  those are the lead's own call (`/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/raw/decision.majkee.pokes-and-continuity.2026-11-22.md`).
  Reading includes read-only tmux queries on both servers: `list-*`, `display-message -p`, and `capture-pane -p` of the
  sandbox's own panes; a seat's pane is looked at only in its bottom rows, before a pointer line. The start script for the
  samples and the release sheet may be written before the release, never run (the manager's correction of his brief,
  `eSharp/_bus/09.manager.point.md`, point 3).
- **Never into Git** — this repository's GitHub remote is public: caches, raw pane captures, transcripts, raw status-line input
  records, personal notes. They stay in the scratch folder. The bed gets field names, types, cleaned examples and a pointer line.
- **Caches** (sheet 2, B2): made by `supervisorCli` on request, at `~/.cache/nablarva/seswin/CACHE.<window name>.md` — named by the tmux window,
  as his roster asks. A cache
  is never authority — STATUS wins — and it does not travel to another host.
- **Text that must be read or copied is written whole and wrapped, never cut at the pane edge** (his E6). Every route is checked for it.
- **The seam to group 2 is files only.** This group writes the one list of status fields; group 2 reads it for its own status
  line. Majkee also wants to be told when somebody tries to send a command to a shared terminal that is closed, or not expected
  to be open for that sender (decisions, section 8). The packet says where such a notice would be shown; it builds nothing for it.
- Versions, read on 2026-11-26 at the bind: Claude Code 2.1.332, codex-cli 0.172.0 (the frame had 0.171.0), tmux 3.7c. Read
  them again on the day of every try.

## The order of work

0. **Bind.** Majkee starts the seats and gives the lead the pen, written into a decision file in this bed's `raw/`. The lead
   checks the party against live tmux, writes its roster with the real models, and rewrites `STATUS.md` as its own.
1. **Read, and write the field list** — no release needed. `raw/fields.<date>.md`, one row per field: model and effort, working
   directory, context left, session name, session id, transcript path (his order), then the slots he wants it to grow into —
   clock and timers, poke status, alerts. For each: where Claude gives it, where Codex gives it, how fresh it is, known or not
   known. Sources, by reading: the deployed `/home/hruzam/ia-sync/claude/hooks/statusline.sh`, the official documentation with
   its date (an `epoch` spawn), and for Codex what a session shows without anything typed into it. A row read from
   documentation or from a script is marked provisional until a sample has shown, separately, that the field is received and
   that it is displayed.
2. **Read back, then ask.** One sheet through the exec desk: the plan read back, the sandbox release as worded above, and the
   script that starts the sample sessions. `audit.seswin` reads the sheet first, once.
3. **Capture what is really received** — needs the release. Majkee starts one sample Claude session in the window
   `claude-sample` and one sample Codex session in `codex-sample`, from the prepared script. The Claude sample gets its own settings file from the scratch folder
   (`claude --settings <file>`), whose status-line command also writes its input there; the deployed hook is not touched.
   `--settings` adds to the layers Claude loads; it replaces none of them. Seen on 2026-11-26: no layer (user, user local,
   project, project local) holds a hook, and the live `~/.claude/hooks/statusline.sh` is byte-identical with the ia-sync copy.
   Installed plugins and the account's connectors still load. The start script names its choice on them (`--setting-sources`,
   `--strict-mcp-config`, or neither) and the sample's permission mode, and the packet lists both as differences from his
   everyday session. Chosen in the prepared script (`~/.cache/nablarva/session-window/`, outside Git): neither, and no
   `--permission-mode` flag, so the CLI starts in its own start mode. Four facts the sheet states plainly:
   - Effort is read from the raw record, never from the pane: the deployed script falls back to `effortLevel` from his
     settings when no effort arrives, so the pane can show an effort the session never sent.
   - The samples are not clean of his everyday context: Claude loads the global `~/.claude/CLAUDE.md` and the instruction
     files on the path above its folder; Codex loads `~/.codex/AGENTS.md` and `~/.codex/hooks.json`, so his Codex hooks fire.
   - A trust answer writes into his everyday files: Codex adds a project entry to `~/.codex/config.toml`, Claude records it in
     `~/.claude.json`. That is his hand at his dialog; the closing step lists such entries and he decides whether they stay.
   - Each start script leaves a start marker in the scratch folder before it starts its CLI; at closing,
     `find ~/.claude ~/.claude.json ~/.codex -newer <marker>` lists what each CLI wrote outside the scratch folder, and the
     packet carries that list (names only).
   The Codex sample is read only: nothing is typed into it, and what it would receive stays NOT RUN.
4. **The three routes side by side** — needs the release. Before the first check the lead writes down the two everyday paths —
   how a seat inspects a pane and how it sends a pointer line, by name and by id — the pane each check expects to reach, and
   two fixed widths. The text of the pointer line is fixed in the same note: one labelled line naming a file in the scratch
   folder whose only request is a one-word reply, so that the Claude sample needs no tool beyond reading that file. The same checks for each route: what it shows at both widths, and whether long text is wrapped or cut;
   which pane the inspection really read; which pane the pointer line really reached — sent to the Claude sample or to a
   disposable shell, never to the Codex sample; which window tmux marked as active; how it refreshes and what that costs.
   For the metadata pane the checks are repeated while that pane holds the focus and prints fresh output and the sample is
   idle. A route that reaches the wrong pane is out for the first version. If every route fails a required check, STOP is a
   useful result. Every command names the test server and checks the server and its own target together before it changes anything.
5. **The packet.** `packet.status-surface.<date>.md`: one row per check — PASS, FAIL or NOT RUN — written by the witness from her
   own look, before she reads the lead's account. The recommendation is the lead's: it cites her rows, and she does not sign
   it. One recommended smallest first version, which answers: where the chess clock would sit — its place only; its timing and
   controls are not tried here; the helper as a window of its own, started from scratch, and what the old zsh helper keeps as a control window;
   how the helper knows which CLI it serves (the manager's view: from the launch recipe, not by reading the pane — the lead
   may disagree); how the record grows (timers, poke status, context left per vendor); where a shared-terminal notice would show;
   which spare places the surface keeps, and where the controls of a shared terminal would sit — connect, attach, release,
   its settings (decisions, section 10, point 6; the UI question is open for Majkee). One helper per CLI or one dashboard is
   not settled by this packet — no check here keeps two independent views open side by side — so the sheet names it as open,
   with the trial that would settle it.
6. **The gate.** One sheet takes the packet to Majkee for GO or STOP. Sample sessions are closed by the hand that started them.

## prompt-0 — lead.seswin

```text
You are lead.seswin, the lead of the session bed /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface —
group 1 of the eSharp shape. Start with your working directory in /home/hruzam/unikuklatrix/nablarva. Read AGENTS.md there and
its read chain, then this bed's STATUS.md, then this RUNBOOK, then section 7 (the read-first list) of
/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/brief.session-window.2026-11-22.md.
You do not hold the pen until Majkee says so and his words are in a decision file in this bed's raw/.
You write STATUS.md, the assignments in _bus/, your verdicts and the commits (by file name; supervisorCli pushes on your poke).
You may spawn any child you need — the roster's chapter 5, houston and oraculum included (raw/decision.majkee.pen.2026-11-26.md)
— and you do not work alone: long reads, sweeps and checks go to a child.
Nothing is built, started or typed on the sandbox server until Majkee has given the sandbox release in his own words; you ask
for it on one sheet through the exec desk, after audit.seswin has read the sheet. Coordination pokes are yours to send.
Nothing private goes into Git — the remote is public. Never read .majkee/ or .hlm/.
What you need from another group, or it from you, goes through the eSharp manager (session `helloWorld`, window `eSharp`): a file and one pointer line.
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
  release only, and only for the group's own test panes. No seat's pane and no pane on the usual tmux server is ever a target of a try.
- **L22** — `.majkee/` and `.hlm/` are never read or listed. The home of the helper there is Majkee's to name.
- **The deployed status line is not changed:** `/home/hruzam/ia-sync/claude/hooks/statusline.sh`, `/home/hruzam/ia-sync/claude/settings.json`,
  the live `/home/hruzam/.claude/settings.json`. No `deploy.sh`.
- **The seat sessions are not rearranged:** no option, status row, pane or window of `helloWorld` or `seswin` — nothing on the
  usual tmux server — is changed for a test.
  Never `tmux kill-server`, on any server. The sandbox server and its session are Majkee's; the group closes only the
  panes and windows it made there.
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
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp.decisions.majkee.2026-11-22.md` — his words: sections 7 (E1, E2, E4, E6), 8, 10 (the tmux tree) and 11 (the sandbox question)
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/answers.sheet-2.majkee.2026-11-25.md` — A3 the release; B1 to B5
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/brief.session-window.2026-11-22.md` — the reader's brief; its section 7 is the read-first list
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X0-substrate/raw/` — the substrate; `goal-substrate.2026-11-13.md` (fields, widths), `handoff.senior-advice.trajectory.2026-11-14.md` (rule 3, the second status row)
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/eSharp/raw/inventory.relay-x1-helpers.2026-11-23.md` — 46 helpers the relay bed made; what exists already
- `/home/hruzam/unikuklatrix/nablarva/.dev/_backlog/termpanum-session-tracker/00_HANDOFF.md` — myShell's tracker proposal
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/goals/G10.friendly-reminder.md` — the chess clock, as defined
- `/home/hruzam/unikuklatrix/nablarva/.dev/_backlog/skin-remote-controll/` — Majkee's linked ideas on the skin, UI and UX; read before the recommendation is drawn
- `/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md`, line 386 — the organ `instarmux`, the skin: UI only if zsh and tmux are not enough
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
