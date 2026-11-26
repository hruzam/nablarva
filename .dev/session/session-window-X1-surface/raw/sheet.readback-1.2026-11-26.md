---
kind: read-back and release sheet 1 — the plan read back to Majkee, the sandbox release and the start script, one theme at a time
by: lead.seswin (flight, pen of session-window-X1-surface) · 2026-11-26 · host home
for: the exec desk and Majkee
status: DRAFT 1. audit.seswin reads it once before it goes to the desk; her points and the lead's answer to each are
  marked "(draft 2)" when taken. At 02:59:22 UTC, after her read was queued, the lead corrected two wordings about the Codex
  provider ("switched on in `/experimental`" was its own overclaim, caught by assay in the field list); she may have read
  the earlier wording.
rule: every line here points at or sums up a file. This sheet decides nothing and releases nothing. "Lead's view" is marked
  as such and is only a view.
order: S0 to S4, as numbered. If S1 is not given, S2 is skipped, and steps 3 and 4 of the RUNBOOK stay NOT RUN. S4 closes;
  nothing starts before it.
asked: the plan as he holds it (S0); the sandbox release as worded on sheet 2, A3 (S1); the start script (S2); two
  confirmations (S3).
not_asked: GO or STOP on the packet (that is the gate, step 6); the home of the helper; one helper per CLI or one dashboard;
  the Codex MCP status-line provider (selecting one in a sample is an activation of its own, L20 and L21 — the packet names
  it as the Codex counterpart of Claude's command status line, and a later sheet can ask for one try).
runbook: /home/hruzam/unikuklatrix/nablarva/.dev/session/session-window-X1-surface/RUNBOOK.md
---

# Why now

The lead was bound on your word at about 02:43 UTC (`raw/decision.majkee.pen.2026-11-26.md`). Step 1 is written: the field
list `raw/fields.2026-11-26.md`, checked by a fresh-eyes child (assay, PASS on the second attempt). Every row in it is
provisional until a sample shows it. On your note, its Codex column went to audit.seswin, who read it in Codex's own release
source and wrote "holds with corrections" (`_bus/07.audit.seswin.return.md`). Her corrections are being folded into the
field list. Two of them matter here:
- Codex wraps its footer within a budget of up to four rows and cuts with "…" once that is full; nothing is said of a row
  kept for one item.
- Codex 0.172.0 also has a second footer route: an MCP status-line provider, switched on in `/experimental`. A local
  program can feed the footer and receives a snapshot of the thread (id, name, directory, model, effort, context, limits).

Neither changes what this sheet asks. Versions today: Claude Code 2.1.332, codex-cli 0.172.0, tmux 3.7c.

# S0 — The plan, read back

- **The gate, unchanged.** You record GO or STOP on a witnessed status-surface packet. It shows what the installed Claude
  status line receives and shows, and the same fields for one Codex session by reading only. It tries the three display
  routes side by side on your test server: the native status line, a second tmux status row and a metadata pane. Each route
  is checked for whether inspection and one pointer line still reach the intended pane. It ends with one recommended smallest
  first version, with the place for the chess clock. No helper is built.
- **Step 3, capture.** You start one Claude sample and one Codex sample from the prepared script (S2). The Claude sample's
  status line writes what it receives into the scratch folder and shows your own status line unchanged. Nothing is typed
  into the Codex sample. What it would receive stays NOT RUN.
- **Step 4, the three routes.** Before the first check, the lead writes down how a seat inspects a pane and how it sends a
  pointer line, by name and by id. The same note fixes the pane each check expects to reach, two fixed widths, and the text
  of the pointer line (one line naming a scratch file that asks for a one-word reply). Then, per route:
  - what it shows at both widths, and whether long text is wrapped or cut;
  - which pane the inspection really read, and which pane the pointer line really reached (the Claude sample or a disposable
    shell, never the Codex sample);
  - which window tmux marked as active;
  - how it refreshes and what that costs.

  For the metadata pane, the same checks are repeated while that pane has focus and prints fresh output and the sample is
  idle.
- **Step 5, the packet.** audit.seswin writes PASS, FAIL or NOT RUN for each check from her own look, before she reads the
  lead's account. The recommendation is the lead's and cites her rows.
- **Stops.** Any of these ends the run:
  - A route that reaches the wrong pane is out for the first version.
  - A dialog on a sample stops the run until your hand clears it.
  - A process nobody started stops the run.
  - An uncertain result is recorded as uncertain and not tried again.

  If every route fails a required check, STOP is a useful result.
- **What changed in the RUNBOOK since the frame** (the lead's pen; each change is in the file):
  - the roster, with the models as launched and your wider spawn word;
  - the test server as it stands now: the session `sandbox` with three windows, and group 2 in `sandbox-terwor`;
  - server options of your real tmux setup are listed as differences, not copied;
  - read-only tmux queries are allowed before the release;
  - versions;
  - what the Claude sample still loads and writes outside the scratch folder (S2);
  - the fixed pointer text.
- **Ask (one answer):** is this the plan as you hold it — yes, or what is different?

# S1 — The sandbox release

- **The wording, as sheet 2, A3 proposed it** (`eSharp/answers.sheet-2.majkee.2026-11-25.md`, A3): "Inside its own tmux
  server and its own scratch folder (`~/.cache/nablarva/<line>/`), with harmless commands, the group may build, run and stop
  what it needs without asking — including typing into its own test panes there. Everything outside — `helloWorld`, any
  seat's pane, your daily shell, ia-sync and its deploy, office — returns to you. Sample CLI sessions are started by you
  from a prepared script, as in the relay probes."
- **What it would cover here.** Steps 3 and 4, on `tmux -L sandbox-server`, in the session `sandbox` only, with
  `~/.cache/nablarva/session-window/` as the scratch folder:
  - setting options of that session and its windows (the second status row is one);
  - making and closing the group's own panes and windows there (the metadata pane, a disposable shell);
  - typing into the Claude sample and into those panes.

  It would not cover typing into the Codex sample, touching `sandbox-terwor`, any server option, or `kill-server`.
- **What stays with you.** Starting and closing both samples, every trust or permission dialog, and everything outside the
  test server and the scratch folder.
- **Lead's view.** One edge of "everything outside" is touched by your own hand, not the group's: a trust answer on a sample
  writes into your everyday files (S2, third point). The group writes nothing there.
- **Ask:** give the release in your own words, or say no. If you narrow it, say what is left out.

# S2 — The start script

- **Where.** `~/.cache/nablarva/session-window/`, outside Git: `start-claude-sample.sh`, `start-codex-sample.sh`, two
  status-line scripts, two settings files and a `README.md` of one screen. They were written by a child, checked by another
  (assay, PASS on six checks: `_bus/09.assay-start-script.return.md`), and never run.
- **What you would type.**
  - In the sandbox window `claude-sample`: `bash ~/.cache/nablarva/session-window/start-claude-sample.sh baseline`. For
    step 4's native route you close it and start it again with `multiline` in place of `baseline`.
  - In the window `codex-sample`: `bash ~/.cache/nablarva/session-window/start-codex-sample.sh`.

  Each script refuses to start unless it runs on your test server, in that exact window, and it says first what it starts
  and how to stop it.
- **The choices in it.**
  - Claude runs on `--model sonnet --effort low`, the cheapest that should report an effort; the first record will show
    whether it does.
  - There is no permission-mode flag, so the CLI starts in its own start mode.
  - Plugins and connectors load as they do every day.
  - Codex starts plain, with no flags, so your own Codex config and its status line show.
- **Four facts, stated plainly** (RUNBOOK step 3):
  1. Effort is read from the record, not from the pane. Your status line falls back to the effort in your settings, so the
     pane can show "high" when the session sent nothing.
  2. The samples are not clean of your everyday context. Claude loads your global instruction files. Codex loads
     `~/.codex/AGENTS.md` and `~/.codex/hooks.json`, so your Codex hooks fire in the sample.
  3. A trust answer writes into your everyday files. Codex adds a project entry to `~/.codex/config.toml` (it already holds
     six), and Claude records it in `~/.claude.json`. At closing the lead lists such entries, and you decide whether they stay.
  4. Each CLI also writes its own session record, under `~/.claude/projects/` and `~/.codex/sessions/`. A start marker in the
     scratch folder lets the closing step list every file each CLI wrote outside it, names only.
- **Ask:** run them as written; or change the model or effort (say which); or no.

# S3 — Two confirmations

1. **The session `sandbox` is group 1's alone.** Your act says so: group 2's `terminal` now sits in `sandbox-terwor`, and
   `sandbox` holds three windows (seen read-only 2026-11-26 02:44 UTC). The RUNBOOK plans on it. **Ask:** yes, or how it is.
2. **The auditor in your pen word, point 3.** It names `$45 | 1 audit @81 | %83`. Live tmux gives those coordinates to
   audit.terwor (group 2). Point 2 names `$44 | 1 audit @79 | %81`, which is audit.seswin. The lead reads point 3 as
   audit.seswin. **Ask:** audit.seswin, or did you mean audit.terwor?

# S4 — Read back

The desk reads back what you gave, theme by theme, in your words. The lead writes each answer into a decision file in this
bed's `raw/`: the release as `decision.majkee.release.2026-11-26.md`. Nothing on the test server starts before that file
exists.
