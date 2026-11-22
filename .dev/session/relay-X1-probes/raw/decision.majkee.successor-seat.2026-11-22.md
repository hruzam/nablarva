---
kind: operator words, verbatim, with the outgoing lead's answers marked as recommendations — the successor's window, build, protocol briefing, session names, team
from: majkee, typed in the engineer session (claude d1ca16e9-073e-46d9-ba7d-26a816c38a67) on home, 2026-11-22, about 05:20 CET
recorded_by: trajectory (outgoing lead of relay-X0-carryover; predecessor on call)
decides: only what is under "Majkee" below. Everything under "Recommendation" is the predecessor's view and binds nobody.
---

# The successor's seat — what Majkee said and what I answered

## 1. Closed beds are not pruned

**Majkee:**
> pruning was mistake, i am trying to not do them again. Rather thinking, that realy closed older sessions can go to gitignore (STATSU will say, finished here), that is also keeping files on their places when acidentaly any wiring exists.

**What follows for this line.** `relay-X0-carryover` and `vist-X0-helloWorld` stay in place; their STATUS files say closed. Nothing
is pruned and nothing has to be promoted first.

**One thing I flag, once.** A `.gitignore` entry does not touch files Git already tracks: both closed beds would stay tracked and
keep showing changes. Ignoring only works for a bed that was never committed. And the RUNBOOK guide
(`~/reposoma/raw.guides/runbook/GUIDE.md`, "On gate closure") still says "prune the directory". If closed beds stay, that guide
line is his to change.

## 2. A new window for the successor; which build

**Majkee:**
> yes you may poke `exec` desk for new window from where I can start with new session -> your successor. Which agent you would send on it, model is clear for me, but which build will be able to spawn subagents on cheap work. I like cooperation with you, but you are doing whole time all alone, hard to convice (my experiences accross more runs) you to do so :), and `oraculum` has these boundaries pushing on her to spawn, but than she have to dedicate more process work on controller.

**Done.** The exec desk is asked for the window by `request.exec.window-lead.trajectory.2026-11-22.md`.

**Recommendation — the `flight` build.** Read from the agent definitions on home (`~/.claude/agents/`), not from experience of
running it in this role:
- Both `flight` and `trajectory` can spawn subagents when they are the main session. The difference is what the definition tells
  them to do. `trajectory`: "still primarily writes code. Spawns @Delta for surgical subtasks." `flight`: "the working-head that
  reads a RUNBOOK chapter and runs the phase spine", and "Discipline — I do not do it all alone … I plan, route, gate, and hold
  the rail; I do not become the single hand that writes everything."
- This bed's lead writes almost no code. It writes assignments, checks returns, and takes decisions to Majkee. That is the
  `flight` job as its definition describes it, in its MANNED mode.
- He is right about me. My own rules say to hand surgical and repetitive work to `delta`, and in two days I spawned one agent, a
  Houston consult. Validation runs, log lines, exact-match edits and the sweeps for stale sentences were all done inline. The
  sweeps are where it cost: two outside reads found the stale sentences I had no context left to look for.
- Two things to check at launch. `flight` defaults to Sonnet; he sets the model. Its definition carries `maxTurns: 30`; I do not
  know whether that limits an interactive main session — if a long run stops early, that is the first place to look.

**Cheap work, and who takes it from a Claude lead** (names as they exist on home):
- `delta` (Haiku) — log lines, exact-match edits from a spec, YAML and whitespace checks, hash comparisons.
- `field` (Sonnet) — melts a long file or several into the brief the lead needs; the sweep "which sentences in these files are no
  longer true against STATUS" is a `field` job at every closing commit.
- `assay` (Sonnet) — a fresh-eyes check of one file against its task, without the author's context.
- On the Codex side the controller's terra helpers stay the crawlers, as readers with one file each.

## 3. The communication protocol

**Majkee:**
> will you brief successor about `communication protocole` and poke as fallback by poke, or it would be part of runbook/cs.card?

**Done — it is part of the RUNBOOK**, section "Communication protocol", with the shared chapter
`~/reposoma/raw.guides/bus/res/file-poke.md` as the rule behind it and one line on the card. Not a spoken briefing: my context is
the least reliable carrier in this party. The successor can still ask me.

## 4. The name of the lead's tmux window

**Majkee:**
> What should be name for new team leader tmux window?

**Recommendation — `lead`.** It is the seat name in the RUNBOOK, so bus files (`NN.lead.point.md`), the roster and the window say
the same word, and it does not collide with `engineer`, which stays as the predecessor's window.

## 5. Session names with `|` suffixes; a Houston window; the team

**Majkee:**
> FYI, I am trying to put to session names also subagents who could be spawned by session behind `|`, sometimes special duties. Is that naturaly readable - good place, or rather exact roster with exact wording who for what. I realized, that you have some complaints on some `crawling`|`houston` episodes as spawned agents. I can add another one window for `houston` as main, just say the word. Or I should rather say, If you see different team, now is fine time to say so.

**Recommendation on names.** The suffix reads well as a hint and I used it as one. It cannot be the authority, for three reasons
seen this night: a name changes while the thread id does not (Oraculum's went from `oraculum(codex)-audit` to
`oraculum(codex).contraThinking|houston|astrobley`); a name says who *could* be spawned, not for what and with whose word (that
last name reads as if she spawned a coder, which her identity allows only as a main with his explicit authorisation); and long
names wrap in the footer. So: keep `|` short — the two or three children the seat is expected to spawn in this bed — and let the
roster say who spawns whom for what.

**Recommendation on Houston.** No standing window. The consult as a spawned agent worked: one page, the right lock lines, two of
my own contradictions found. The one fault was mine — my session ran from `~/ia-sync`, so his loader would have taken the wrong
project addendum. A lead started in `~/unikuklatrix/nablarva` does not have that problem. This bed needs him once, if the scope
changes. The crawling episode was also a brief problem, not a seat problem: helpers asked to conclude hedged; asked for facts,
they delivered.

**Recommendation on the team.** The same team. One change of habit instead of a change of seats: the lead delegates. And the
controller is at 40% of its context — enough for pushes, which is all the first run asks of it; replace or clear it before a
crawling job or a Codex-origin row.
