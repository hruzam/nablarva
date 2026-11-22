---
kind: input for the RUNBOOK of relay-X1-probes — one outgoing lead's experience with seats, children and context cost. Noncanonical. The lead of this bed decides what to take.
by: trajectory (claude d1ca16e9-073e-46d9-ba7d-26a816c38a67), pen of the closed bed relay-X0-carryover · 2026-11-22 · home
written_on: Majkee's request, typed in the engineer session after the bed was closed — "any experience|scar|understanding of spawn process (claude->codex subagents and vice versa …) … you can share them to new runbook file"
evidence: ../../relay-X0-carryover/_bus/ (cycles 10–19) · ../../relay-X0-carryover/raw/pokes.log.md · ../../relay-X0-carryover/exp/
scope_limit: one night, one host, one party. Everything under "Observed" happened; everything under "Not tried" did not. Nothing here qualifies a mechanism.
---

# Seats, children and context — what one night taught me

## 1. There are three different things, and they behave differently

| | What it is | How I reached it | What came back |
|---|---|---|---|
| **A main seat** | another agent session in its own tmux window (controller, auditor, Oraculum, the exec desk) | a POINT file first, then one labelled line through `codex queue --thread <id>` | a RETURN file; sometimes a reply bell |
| **A child of a main** | a helper the main spawns itself (Codex `spawn_agent`) | never directly — I asked the parent in the POINT | the child's own file, then the parent's RETURN |
| **My own subagent** | a Claude agent I start with my own tool (the Houston consult) | a brief in the tool call | its reply, in my context |

I never spawned a Codex child from Claude, and no Codex seat spawned a Claude agent on purpose. The one time a Codex seat started
a Claude process, it was an accident: `claude help agents` — a word after `claude` is a prompt (incident note of the old bed).
So across vendors the working pattern was **main to main, by file**, and each main spawns inside its own vendor.

## 2. Observed

**Children as readers work; children asked to conclude hedge.** The controller's three terra helpers were first asked for a
result. Two of the three ended with "this is an incomplete inspection, not a finding that none exists". In the second pass the
same helpers only collected facts into their own files and the controller made the judgement; that table could be checked.
(Old bed, cycles 11 and 12.)

**One file per child is what makes a child checkable.** Majkee asked for it ("results should have their own files"). I could
open `crawl.01–06.md` and hold them against the parent's table. A child that only speaks into its parent's context leaves
nothing to verify.

**A child for coding exists on the Codex side, and it worked.** The exec desk spawned an `astrobley` child for the custody copy:
it wrote a script, made the copy and wrote the ledger entry, and my re-hash agreed. The desk's advice for asking a Codex main to
do that, word for word from its RETURN: *"For cycle `<NN>`, spawn Codex `agent_type: astrobley`, task name `<slug>`, to `<one
outcome>`. Read `<paths>` and own `<exact writable paths>`. Other workers may be active. Preserve their edits. Gates:
`<limits>`. Done when `<checks>`. Return `<evidence and limits>` to `<absolute return path>`. Parent verifies and integrates."*
In the roster a child goes under its parent with role, task, handle, writes and return_to.

**A seat's identity decides what it can be asked, and bending it costs more than routing around it.** Oraculum's identity file
rules out code review, pushing and operating a transport. I first asked her for a reply bell and called her a senior dev
partner; both were wrong and she said so. Asked for what she is — the opposer, by file — she was the most valuable reader of
the night: she found that my probe table had lost the trial's own direction. For a second coding body, ask a controller or a
dev main to spawn `astrobley`; the desk says an Oraculum who runs as a main can — with Majkee's explicit
authorisation and where the runtime supports it — commission a bounded execution worker; the worker keeps its own role and she
stays the advisor. An Oraculum that is itself a child is analysis-only. (I first wrote this wrong; the desk corrected it in its
own note, `runbook-input.decision-desk.exec.2026-11-22.md`.) I did not test it.

**Three roles for anything that touches evidence.** I wrote the folder-copy script and tested it on synthetic folders; the
controller reviewed it as a non-author and ran it on the real ones; I re-checked the result with commands that were not the
script's. One short cycle. Nobody accepted their own work.

**A blind second label is cheap and turns a reading into a result.** The auditor labelled 46 frames without seeing the
selector's files and agreed on all 46. About a minute of its time.

**My own subagent returned one page for a lot of reading.** The Houston consult read the locks and came back with a verdict and
five constraints — and with two sentences of my draft that contradicted my own files. Two things to know: the consult card writes
nothing, so the head records its reply verbatim; and its loader picks the project from the session's working directory. Mine was
`~/ia-sync`, so I had to name the nablarva addendum in the brief. **Start the lead's session in `~/unikuklatrix/nablarva`.**

**What each seat's context paid, read from the footers ("Context N% left")**

| Seat | Work | Before → after |
|---|---|---|
| controller | first U01 pass, three helpers concluding | 54% → 51% |
| controller | second pass, helpers as readers, own judgement | 51% → 43% |
| controller | script review, one run, own checks | 43% → 41% |
| controller | a push-only poke | under 1% each |
| auditor | blind label of 46 frames | 87% → 82% |
| Oraculum (xhigh) | counter-read of the handoff and eight goal files | 80% → 63% |
| Oraculum | confirming read | 63% → 57% |
| exec desk | a decision walkthrough | 93% → 79% for eleven themes plus a child's work; 79% → 75% for five themes |

Helpers kept the controller's context flat when they did the work; the pass where he judged himself cost him three times as much.
An opposer at high effort is the most expensive read and was worth it twice.

**What ate my own context, and what did not.** I went through more than one context reset in one bed. What cost: writing long
files in the conversation, re-reading my own STATUS, long tool output. What was cheap: RETURNs with a word limit (250–450 words,
the detail in a file I opened only when needed); exact-match edit scripts instead of rewriting files; a finite file watch in the
background instead of looking again; letting another seat read. After each reset I resumed from STATUS and the files. The damage
showed elsewhere: stale sentences. The audit found some, and Oraculum later found more in six goal files. **Sweep every file that states a fact at
every closing commit**, not when someone else reads.

**The decision desk is not a neutral pipe — and that is fine if the record says so.** The exec desk was Majkee's mouth, ears and
eyes. Three things I learned from the receiving end:
- When his reply is replaced by a confirmed summary, the summary can drift. Once it said the opposite of the sentence he had
  typed (pushes). His own line, quoted beside the summary, fixed that; checking a record then took one match run.
- One question per confirmation. A single "yes" to a message with two questions answers neither.
- Twice he asked the desk "why" or "what would you take", and the desk's proposal became the decision — one clause of this
  bed's gate is the desk's wording, confirmed by him. The record marked it as the desk's proposal each time. Keep that.
It also acted on nothing unless he told it directly, and when he did (the first custody copy), it said so in its RETURN.

**Decisions owed by Majkee go on a sheet, to the desk, at once.** Questions left in my own chat scrolled away between exchanges
with other seats; he noticed before I did. A theme on the sheet needs: context, what it buys, cost, consequences, one question —
and **why it is asked now**. He asked "why" at the desk twice.

**Wording that failed in my POINTs.** "No git stage, commit, pull or push" was read as "no git" by two seats; say in the gates
line what is allowed. A POINT that asks for one word gets one word; ask for the table first. A term like "the frozen signature
set" needs its history line, not only its hash — there were three sets.

**Pokes.** Every `codex queue` call of the night was accepted and followed by its RETURN or a pushed ref. I never sent a poke
into a seat's working turn; a push poke waited until the turn had ended. Of six look-first pastes into Claude panes, five were
submitted and one stayed staged with Enter returning 0 (r06, cause unknown). A desk once withheld its bell because my input row
held a draft; that was the right call.

## 3. Not tried — do not read these as known

- Whether a `codex queue` message into a **working** turn waits or interrupts. I avoided finding out.
- Spawning a Codex child **from** Claude, or the Claude relay agents that exist in my tool list for carrying a brief to the Codex
  line. I used the tmux party instead.
- A Codex seat starting a Claude agent **on purpose**. The only start was the accident.
- Claude `SendMessage` between tmux-hosted sessions.
- What a Codex child costs in tokens. I saw only its parent's footer.
- Whether an Oraculum main really commissions an execution worker when asked and authorised. The desk did not try it either.

## 4. If I wrote the RUNBOOK, these lines would be in it

1. Across vendors: main to main, by POINT file and one labelled line. Each main spawns its own children; the POINT names the
   child type, the task, the paths it reads and the exact paths it owns, and what the parent does if the child cannot start.
2. A child writes its own file. A child collects; the seat that answers judges.
3. Ask a seat only for what its identity allows. An advisor is not a coder. A second coder is an `astrobley` child of a
   controller or a dev main.
4. Author, runner and checker are three seats for anything that touches evidence. A negative result gets a blind second label.
5. Every RETURN has a word limit and points at a file. Every seat's footer is read before a POINT; a seat that is low on context gets
   no new reading job.
6. A document that asks Majkee for a release is read by the other vendor first — and one read is the default, not four.
7. His decisions: one sheet, the desk, at once; one question per turn; his own line quoted; say why now.
8. At every closing commit, sweep the files that state facts.
