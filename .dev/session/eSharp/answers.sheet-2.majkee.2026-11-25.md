---
kind: answer file for Majkee — provisional, second sheet. Write after each `to trajectory:` tag, in any words; by voice is fine too.
by: the eSharp manager (engineer session d1ca16e9) · 2026-11-25, after reading your answers to sheet 1 and your roster
state: buffering cycle, smoothing. Nothing is written, started or poked on the strength of this sheet until you say go.
after: your answers go verbatim into ../eSharp.decisions.majkee.2026-11-22.md; then this file can go
---

# Sheet 2 — five things that need your word, five I decide unless you object

One word is enough to start: **"go"** lets me write group 1's RUNBOOK and briefs from what you already answered.
A1–A5 can follow; only A1 is urgent.

## A — needs your word

### A1 — This repository is public, and the caches are on it (urgent only if it was not meant)
`nablarva` on GitHub is public. Your commit of 24 Nov (`eb26f28`) carried four files that are now on the remote:
`relay-X1-probes/CACHE.lead.md` (241 kB, a cut of the lead's transcript), `CACHE.md`, `CACHE.exec.md`, and
`vist-X0-helloWorld/majkee-personal-notes.md`. I did not read any of them. A count-only scan of the three caches found no
token- or key-shaped string; the only mail address in them is the commit trailer's. I did not scan the personal notes.
Meant so? If not, the quickest full stop is yours alone: set the repository to private. Taking the files out of future commits
(stop tracking, one ignore rule) I can prepare; taking them out of the history is a rewrite, which L12 forbids without your word.

> to trajectory:
> to trajectory END

### A2 — "FLR"
You wrote that `session-window-X0-substrate` must at least be closed "FLR". I do not know the letters and found them in no
guide. My reading: X0 gets a closing STATUS — closed, its gate never recorded, its open points carried into X1 — and stays in
place. Right? And what do the letters stand for?

> to trajectory:
> to trajectory END

### A3 — The release you asked me to recommend (E8): one sandbox release per group
> Inside its own tmux server and its own scratch folder (`~/.cache/nablarva/<line>/`), with harmless commands, the group may
> build, run and stop what it needs without asking — including typing into its own test panes there. Everything outside —
> `helloWorld`, any seat's pane, your daily shell, ia-sync and its deploy, office — returns to you. Sample CLI sessions are
> started by you from a prepared script, as in the relay probes.

Why this and not "release when the design is done": it keeps a group running while you are away, which is what you ask for;
the written scope satisfies L21; the two groups cannot hit each other; and a release after the design would cost you a sitting
for a yes you would give anyway. What the groups share is files only: one list of status fields (group 1 writes it, group 2
reads it for its status line), the helper inventory, and myShell's tracker proposal in `.dev/_backlog/`.
Give it to group 1 as worded — yes, no, or reword?

> to trajectory:
> to trajectory END

### A4 — Group 2: what I was asking in E7, in plain words
A gate is the one sentence that says when the session is finished and what you look at to say GO. Proposed:
*"Majkee opens the shared terminal himself, sends harmless commands through it and records GO or STOP; beside it lies the
auditor's table of the card's ten probes."* Inside, the order you wrote: small research spawns → axioms and steps on one page
for you → build v0 in the sandbox → the probes. Bed: `terminal-workspace-X1-v0`. The old bed `…-X0-approaches` is closed by
the new lead (it is Cartan's pen) on your E5 word: the card is master, older material counts only where it does not contradict.
Confirm, or reword?

> to trajectory:
> to trajectory END

### A5 — Your approval ladder against the card you named master
The card says: "No vendor hooks and no local model in the required path", and its rule 15 replaced the string allowlist by a
few named, reviewed operations. Your rung "record type to approved" is close to the allowlist the card dropped, and "only
potential risk" needs a classifier. The card also says: do not reopen these without the human — you are the human.
Recommended: v0 stays as the card has it, every request approved by key. The ladder is written down now as an axis the request
record must be ready for (a type, and room for a risk mark) and is built from v1: rung 2 = the card's named operations;
rung 3 = a classifier that may only add a warning to the gate prompt and never approves by itself — beside the path, not in
it. Laya: I do not know this model and cannot confirm the description. It goes on `lead.terwor`'s list as its first research
spawn (`researcher`); the result is input for v1 and does not hold v0.
Agree, or do you want the ladder in v0?

> to trajectory:
> to trajectory END

## B — decided so unless you object (you asked, or it was left to me)

### B1 — One shared supervisor (your roster §4: "one shared or per group?")
One `supervisorCli` for the relay line and both groups. One checkout and one remote: one pusher cannot race another. One
full-permission seat is one authority to watch. The relay bed is at its last step, and the groups start one after the other.
A second one only when a request has had to wait twice. A fresh session, not today's `supervisor-relay` (%59), which has
carried two beds. Window `supervisorCli`, no slug while it is shared. I write its brief: pushes on a head's poke, runs bounded
work on a POINT, makes caches on request, and takes its authority from the assignment, never from its permissions.
Note: the 006 intake in ia-sync kept `supervisor` as the seat's name and did not adopt `supervisorcli`; your roster of today
uses `supervisorCli` as nick and window. I follow the roster.

> to trajectory:
> to trajectory END

### B2 — Caches `CACHE.<posture>.md` — yes, but outside Git
A second stream beside STATUS, made by the supervisor with the existing `build-cache.js`, on request: before a clear, a fork,
a handoff. Written to `~/.cache/nablarva/<line>/CACHE.<posture>.md`, with only a pointer line in the bed — because of A1.
It is never authority; STATUS wins.

> to trajectory:
> to trajectory END

### B3 — Where the seats live (your E4 question)
All seats in `helloWorld` on the usual server, one place for you — me too, in my pane; the window can be renamed `eSharp` at the
clear. `tmux -L session-window` and `tmux -L terminal-workspace` hold only what is being built and tested, never a seat. So a
status row or an option tried there cannot touch a seat, pointer lines keep working by pane id, and you can attach to a test
server in a second terminal to watch.

> to trajectory:
> to trajectory END

### B4 — send-keys (E6): Houston by spawn; and one correction
One bounded question is Houston's `consult` card, so a spawn — a window would be a sitting. `lead.terwor` spawns it.
I did not say a shared pane breaks the relay design. The point is that the card types twice, and the two are different:
a `source <file>` line into the organ's own shell pane, where there is no agent's input row and nobody's draft; and a bell into
a seat's pane, the same class as today's pokes. They may get different answers. Inside the sandbox both are covered by A3; your
ruling is needed only when the organ leaves the sandbox.
Taken for group 1's design from your E6: text that must be read or copied is written whole and wrapped, never cut at the pane edge.

> to trajectory:
> to trajectory END

### B5 — Roster and start
Your syntax stays (`seat|who it may spawn`, `a-><b> : [task]`); each RUNBOOK gets a one-line legend and the exact roster.
One fix: §3's lead posture says `lead.seswin`; it should be `lead.terwor`. "Can provide tests" for an Oraculum auditor: she
does not write code herself, so I record your roster line as the authorisation to commission tests through the spawn named in
her posture. `audit.seswin` should be a fresh Codex Oraculum session: the one in `seniorDev` (%60) has 32% of its context left,
and the relay auditor 21%. Start as agreed on 22 Nov: group 1's seats first (`lead.seswin`, `audit.seswin`, `supervisorCli`),
group 2's two when group 1 has closed a cycle.

> to trajectory:
> to trajectory END
