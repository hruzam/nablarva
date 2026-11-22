---
kind: note from the predecessor to the lead of relay-X1-probes — information, not instruction; the files and Majkee win
by: trajectory (claude d1ca16e9-073e-46d9-ba7d-26a816c38a67, window `engineer`, pane %58), outgoing lead of the closed bed relay-X0-carryover
written_on: Majkee's word, 2026-11-22 — "if you want to say anything to new leader, you can poke him"
state: uncommitted when written. It is yours to commit with your first commit or to delete.
---

# Eight short things the files do not say, or say quietly

**1. What to trust, in this order.** The handoff was accepted by Majkee and read by Houston and twice by Oraculum; it wins.
The RUNBOOK is my frame and nobody else has read it — you are its first reader, so read it as a draft. The STATUS is a skeleton I
wrote only so the bed had a router row; rewrite it once the pen is yours. The pen is yours when his words are in a file in `raw/`.

**2. Four holes I know of in my own start lines** (handoff §3, "Proposed start") — check them before you put a release line to him:
- The sample has to **write a receipt file**. I wrote "default approvals" and never checked what a fresh Codex session may write
  without asking. If it asks, that is a dialog on the sample, and the run stops until his hand clears it. Read the sandbox and
  approval flags in `codex --help` first, and say in the release line what the sample may write and where.
- The model names `gpt-6.1-terra` and `haiku` are my guesses. Only the flags `-m` and `--model` are verified.
- Observation A needs the sample's **thread id**. Read it from the sample's footer after its first turn — the NONCE instruction
  gives it one.
- I do not know what a queued message does when it lands in a **working** turn. Make sure the sample is idle before A.

**3. For observation B, do not judge the input row by eye alone.** A dim suggestion sits on an empty row and looks like a draft.
`tmux display-message -p -t <pane> '#{cursor_x}'` shows the cursor at the row start when the row is empty, and
`tmux capture-pane -e` shows the dim styling. I nearly withheld a poke over one today.

**4. About Majkee.** He wants the run to go on without him until an approval, a gavel or a decision is really needed; pokes are
yours to send. His decisions go on a sheet through the exec desk, one question per turn. Twice he asked the desk "why now" —
put the reason on the sheet. Quote him as typed, typos included; a summary once said the opposite of his sentence. He reads
context · buys · cost · consequences.

**5. The seats' context when I stopped** (their footers, 2026-11-22 about 04:40 UTC): controller 40%, Oraculum 57%, exec desk 65%,
auditor 82%. The controller is enough for pushes, which is all the first run asks of it.

**6. The first step I would take.** Bind; re-read the party against live tmux; then one read-back sheet through the exec desk that
asks for release lines 2–7 only — one sample, two observations. Nothing else until those are answered.

**7. Your build.** Your definition says you do not work alone; I did, and others had to find my stale sentences. If a long run
stops early, look at `maxTurns: 30` in `~/.claude/agents/flight.md` — I do not know whether it binds an interactive session.

**8. Asking me.** Write the question into a file in this bed's `raw/` and send one labelled pointer line into pane `%58` (window
`engineer`), look first. I answer with file paths. My context has been compacted several times; where my memory and a file
disagree, the file wins. I hold no pen and start nothing.

Housekeeping: `CACHE.md` in this bed is not mine and I did not open it. The two changed files under `vist-X0-helloWorld/` are
Majkee's — never staged, the notes file never opened. The line's pokes are logged in this bed's `raw/pokes.log.md` from now on;
the file does not exist yet.
