---
kind: read-back and release sheet 1 — the plan read back to Majkee, the sandbox release and the start scripts, one theme at a time
by: lead.seswin (flight, pen of session-window-X1-surface) · 2026-11-26 · host home
for: the exec desk and Majkee
status: >-
  DRAFT 2. Draft 1 was read once by audit.seswin. Her verdict was "send with changes", with seven points, all taken
  (_bus/11.audit.seswin.return.md). Each change against draft 1 is marked "(draft 2)". The lead disclosed a fault of its own:
  draft 1, as committed in 699c6f7, still said the Codex provider is "switched on in `/experimental`" in "Why now", while its
  status claimed the wording was corrected. A two-step edit of the lead's wrote the file twice from the same text. Draft 2
  carries the corrected wording.
rule: every line here points at or sums up a file. This sheet decides nothing and releases nothing. "Lead's view" is marked
  as such and is only a view.
order: S0 to S4, as numbered. If S1 is not given, S2 is skipped and steps 3 and 4 of the RUNBOOK stay NOT RUN. S4 closes.
  Nothing is started or typed on the test server before S4 is written down. (draft 2)
asked: the plan as he holds it (S0); the sandbox release as worded on sheet 2, A3 (S1); the start commands, each approved
  now and typed only after the read-back (S2); two narrow confirmations (S3).
not_asked: GO or STOP on the packet (that is the gate, step 6); the home of the helper; one helper per CLI or one dashboard;
  the Codex MCP status-line provider (selecting one in a sample is an activation of its own, L20 and L21 — the packet names
  it as the Codex counterpart of Claude's command status line, and a later sheet can ask for one try).
runbook: /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/RUNBOOK.md
---

# Why now

The lead was bound on your word at about 02:43 UTC (`raw/decision.majkee.pen.2026-11-26.md`). Step 1 is written: the field
list `raw/fields.2026-11-26.md`. Every row in it is provisional until a sample shows it. On your note, its Codex column went
to audit.seswin, who read it in Codex's own release source and wrote "holds with corrections"
(`_bus/07.audit.seswin.return.md`). The field list takes her corrections, and a fresh-eyes child (assay) checked it to PASS.
Two of her findings matter here:
- Codex wraps its footer within a budget of up to four rows and cuts with "…" once that is full. No row is kept for a single
  item.
- Codex 0.172.0 also has a second footer route, an MCP status-line provider. It is exposed in `/experimental` and selected
  with `/statusline` after a restart. A local program can feed the footer and receives a snapshot of the thread: id, name,
  directory, model, effort, context and limits. (draft 2: wording corrected)

Neither changes what this sheet asks. Versions today: Claude Code 2.1.332, codex-cli 0.172.0, tmux 3.7c.

# S0 — The plan, read back

- **The gate, unchanged.** You record GO or STOP on a witnessed status-surface packet. It shows what the installed Claude
  status line receives and shows, and the same fields for one Codex session by reading only. It tries the three display
  routes side by side on your test server: the native status line, a second tmux status row and a metadata pane. Each route
  is checked for whether inspection and one pointer line still reach the intended pane. It ends with one recommended smallest
  first version, with the place for the chess clock. No helper is built.
- **Step 3, capture.** You start one Claude sample and one Codex sample from the prepared scripts (S2). The Claude sample's
  status line writes what it receives into the scratch folder and shows your own status line unchanged. The group sends no
  input to the Codex sample. What Codex would receive stays NOT RUN. (draft 2)
- **Step 4, the three routes.** Before the first check, the lead writes one note that fixes:
  - how a seat inspects a pane, and how it sends a pointer line, by name and by id;
  - the pane each check expects to reach, and two fixed widths;
  - the text of the pointer line: one line naming a scratch file that asks for a one-word reply.

  Then, for each route:
  - what it shows at both widths, and whether long text is wrapped or cut;
  - which pane the inspection really read, and which pane the pointer line really reached;
  - which window tmux marked as active;
  - how it refreshes and what that costs.

  For the metadata pane, the same checks are repeated while that pane has focus and prints fresh output and the sample is
  idle.
- **Step 5, the witness** (draft 2, her point 6). For each check, the lead sends audit.seswin the check id, the expected
  target, the widths and a time to look, with the result left blank. The lead either holds the state for her read-only look
  or keeps the original, unannotated evidence in the scratch folder. She writes PASS, FAIL or NOT RUN, with a reason for
  NOT RUN, before she opens the lead's account. A known mismatch is FAIL. The recommendation is the lead's and cites her rows.
- **Stops** (draft 2, her point 6):
  - A misroute rules that route out for the first version and stops all further input through it.
  - A process nobody started stops the run.
  - A dialog on a sample pauses the run until your hand clears it.
  - If every route fails a required check, STOP is a useful result.
  - *Lead's proposal, not in the RUNBOOK:* an uncertain result is recorded as uncertain and not tried again in this run.
    Say if you want it.
- **What changed in the RUNBOOK since the frame** (the lead's pen; each change is in the file):
  - the roster, with the models as launched and your wider spawn word;
  - the test server as it now stands: session `sandbox` with three windows, group 2 in `sandbox-terwor`;
  - server options of your real tmux setup are listed as differences, not copied;
  - read-only tmux queries are allowed before the release;
  - versions;
  - what the samples still load and write outside the scratch folder (S2);
  - the fixed pointer text.
- **Ask (one answer):** is this the plan as you hold it — yes, or what is different?

# S1 — The sandbox release

- **The wording, as sheet 2, A3 proposed it** (`eSharp/answers.sheet-2.majkee.2026-11-25.md`, A3): "Inside its own tmux
  server and its own scratch folder (`~/.cache/nablarva/<line>/`), with harmless commands, the group may build, run and stop
  what it needs without asking — including typing into its own test panes there. Everything outside — `helloWorld`, any
  seat's pane, your daily shell, ia-sync and its deploy, office — returns to you. Sample CLI sessions are started by you
  from a prepared script, as in the relay probes."
- **What it would cover here, and no more.** Steps 3 and 4, on `tmux -L sandbox-server`, in the session `sandbox` only. The
  scratch folder is `~/.cache/nablarva/session-window/`. The scope narrows from the whole server to group 1's session.
  (draft 2)
  - Setting options of that session and its windows (the second status row is one).
  - The two width changes, the focus changes and the route checks.
  - Making and closing the group's own panes and windows there: the metadata pane, and a disposable shell that runs a
    receive-only fixture, so that a pointer line meant for a CLI is never run as a command.
  - Input: only the fixed pointer line, into the Claude sample or that disposable shell.
  - Before each change, the command checks the named server, the exact session and the intended pane or window. (draft 2)
- **Outside the release.** Typing into the Codex sample, `sandbox-terwor` and group 2, any server-wide option,
  `kill-server`, and any seat's pane.
- **What stays with you.** Starting and closing both samples, every trust or startup dialog, and everything outside the test
  server and the scratch folder.
- **Ask:** give the release in your own words, or say no. If you narrow it, say what is left out. A check your words do not
  cover stays NOT RUN. (draft 2)

# S2 — The start commands

- **Where.** `~/.cache/nablarva/session-window/`, outside Git. There are two start scripts, two status-line scripts, two
  settings files and a `README.md` of one screen. A child wrote them and another child checked them in their final form:
  assay, PASS on nine checks, including the pane pin, the Enter prompt before any start, and `nohooks` against `plain`
  (`_bus/09.assay-start-script.return.md`, attempt 2). The lead ran `codex --disable hooks features list` itself; the flag is
  accepted and reports hooks off. The scripts have never been run, and no check has tried a CLI starting. (draft 2)
- **Before each start, the script asks for Enter.** Ctrl+C or Ctrl+D at that prompt starts nothing and leaves only an empty
  sample folder in the scratch folder. (draft 2)
- **Each script refuses to start** unless it runs on your test server, in session `sandbox`, in its own window and in its
  original pane (`%1` for Claude, `%0` for Codex). It says what it starts and how to stop it, after those checks pass.
  (draft 2)
- **The three starts, to be approved now and typed only after S4** (draft 2, her point 2):
  1. In window `claude-sample`: `bash ~/.cache/nablarva/session-window/start-claude-sample.sh baseline` (step 3).
  2. Later, in the same window, after you close the first: the same command with `multiline` in place of `baseline` (step 4,
     native route).
  3. In window `codex-sample`, once: `bash ~/.cache/nablarva/session-window/start-codex-sample.sh nohooks`, or `plain`
     (below).
- **Claude's choices.** `--model sonnet --effort low` is the cheapest setting that should report an effort; the first record
  shows whether it does. There is no permission-mode flag, so the CLI uses its own start mode. Plugins and connectors load as
  every day.
- **Codex: hooks on or off** (draft 2, her point 1). Started plain, Codex runs your global SessionStart hook: a time-limited
  `git pull` in `~/.remote`, which can read the task file there into the sample before anyone types. Its off switch,
  `~/.remote/OFF`, is not present. The lead checked this in `~/.codex/hooks.json` and confirmed that `codex --disable hooks`
  reports hooks off at 0.172.0.
  - `nohooks` starts `codex --disable hooks`: your footer configuration as every day, hooks off. The packet records the
    difference.
  - `plain` starts plain `codex`: the hook may act outside the scratch folder, as it does every day.
  - *Lead's view:* `nohooks`. The gate needs the footer, not the hook.
- **What the samples carry and leave, stated plainly** (draft 2, her points 3 and 4):
  1. **Effort.** For Claude, effort is read from the record, not from the pane: your status line falls back to the effort
     in your settings, so the pane can show "high" when the session sent nothing. For Codex, a visible effort is display
     evidence only.
  2. **Context.** The samples are not clean of your everyday context. Claude loads your global instruction files. Codex
     loads its ordinary home, base config and global instructions, but no Oraculum profile. Its footer may therefore leave
     out the profile, an unnamed thread or unknown context, so not all six of your configured items should be expected.
  3. **Dialogs.** No trust entry exists for the Codex sample's folder, so a folder-trust prompt may appear. Accepting it
     saves that folder as trusted in your config, and quitting is also an answer. Claude may ask the same, and a yes is
     recorded in `~/.claude.json`. Both dialogs are your hand. The group sends nothing to Codex.
  4. **Writes outside the scratch folder.** Each CLI writes its own state in its home: Claude its session record; Codex its
     state, logs, local databases and session metadata. A Codex rollout may be absent before a first turn, which is a valid
     result. A start marker in the scratch folder lets the closing step list *candidate* changes in the searched places. Only
     what a sample-specific identifier ties to a sample is attributed to it. Another live CLI can write there in the same
     interval, and a file outside those places, or one made and removed in between, is missed. Other sessions' file names
     stay out of the public packet.
- **Ask:** approve the three starts as listed, with `nohooks` or `plain` for Codex; or change the Claude model or effort (say
  which); or no.

# S3 — Two narrow confirmations

1. **The session `sandbox` is group 1's alone.** Your act says so: group 2's `terminal` now sits in `sandbox-terwor`, and
   `sandbox` holds three windows (seen read-only on 2026-11-26 at 02:44 UTC). S1's scope depends on this. **Ask:** yes, or
   how it is.
2. **Who may spawn under roster chapter 5** (draft 2, her point 7). Your pen word, point 3, names `$45 | 1 audit @81 | %83`,
   and live tmux gives those coordinates to audit.terwor (group 2). Point 2 names `$44 | 1 audit @79 | %81`, which is
   audit.seswin. The lead reads point 3 as audit.seswin. This settles only that permission, not the witness. **Ask:**
   audit.seswin, or did you mean audit.terwor?

# S4 — Read back

The desk reads back what you gave, theme by theme, in your words. The lead writes each answer into a decision file in this
bed's `raw/`, the release as `decision.majkee.release.2026-11-26.md`. A start is typed only when two things hold: your S1
yes covers that action, and your S2 approval names that start and mode. A file that records a no, or a narrower release,
leaves the excluded checks NOT RUN. (draft 2, her point 2)
