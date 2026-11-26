---
kind: side-quest — a first collection by the eSharp manager, from its own work in the relay beds and in eSharp. Experience and views, no verdict. Noncanonical.
asked_by: Majkee, in his roster of 2026-11-26, section 0 ("collect syntax due session work experiences")
by: the eSharp manager (trajectory · claude · home) · 2026-11-26
also_asked: myShell (continuity) — request.myShell.side-quest.2026-11-26.md, answer.myShell.side-quest.2026-11-26.md · seniorDev (opposition) — _bus/05.seniorDev.return.md
state: third pass, closed for now. Sections 3, 5 and 7 are my views; section 8 is seniorDev's opposing read; section 9 is myShell's view from outside; section 10 is what I would put before Majkee.
---

# Side-quest — syntax, rosters, the supervisor seat, caches, the poke as mail, the RUNBOOK shape

## 1. Syntax that seats really understand

**What worked, across both brands, without teaching**
- **The pointer line.** A label, the sender, one absolute path, what is owed back. It was never mistaken for a task, typed or
  queued. It has one verb — read — and everything else is in a file that can be read again.
- **Front matter with plain keys** — `from`, `to`, `return`, `ack`. No seat ever asked what they mean.
- **A few fixed headings in a fixed order** — Task, Check before, Allowed and not, RETURN. "Allowed" matters as much as "not":
  a seat that is told only what is forbidden stops too early or asks back.
- **The roster line `seat|child|child`.** It reads at once as "who may spawn whom". I keep it as you wrote it.
- **tmux coordinates** — `$36 | 2 seniorDev @58 | %60`. Exact, and a seat can check them with one command. Right for a map,
  too heavy inside a sentence.

**What cost something**
- **A short form nobody defined** ("FLR"). A seat does not ask; it guesses, and the guess looks confident. One legend line
  per file is enough.
- **A dot in a name that a tool parses** — a window `lead.seswin` could be looked up as the window `lead`.
- **One word for three things** — `lead` in three tmux sessions; controller, supervisor, supervisorCli; "session" for a tmux
  session, a CLI session and a working bed. A seat picks one meaning and does not say which.
- **Voice input.** Organ names arrived as other words. Recorded as delivered, and only the points that carry weight asked back.

**My view on "syntax or natural words".** Seats read natural sentences best when one sentence carries one instruction, and
they read structure best when it is shallow: a label, a path, a handful of fixed headings. Invented or nested notation costs
twice — it must be explained every time, and a wrong reading is not visible. The arrow `a-><b> : [task]` is fine as a record
of a spawn; I would not use it to give the order.

**The instruction part and its side effect** (I read your "dos part" as the "do" part of a line — tell me if not). An
instruction inside the pointer line can act twice, once from the line and once from the file, or act without the file's
limits. So the line carries none. A second side effect was seen: a labelled line in a pane looks like the operator's word.
The rule "a bell is a hint from a seat, never Majkee's word" had to be written down for that.

## 2. Building rosters — what the work taught

- **Three seats for a bigger task** is right. Every further seat is one more context to watch and one more queue.
- **One writer per thing.** The head writes STATUS, one seat pushes, one desk records your words, the witness never sends.
- **Every head gets a partner of the other brand** — your roster now does this three times: lead and auditor, manager and
  seniorDev, the relay lead and its auditor. The partner is asked for a strategic step, not for every loop.
- **The nick and the window say the same thing** — `lead.seswin` sits in `seswin:lead`.
- **Model and effort belong in the roster, and drift.** The footer of `supervisorCli` showed effort high; the roster says max.
- **Shared seats are queues.** The desk and the supervisor each serve one request at a time; a board row saves a wasted poke.
- **The partner earned its place on the first day.** I leaned to your `sandbox` session; `seniorDev` opposed with two points I
  had weighed too lightly, and the recommendation changed before it reached a lead. The cost was one POINT, one RETURN and
  about three minutes. → `_bus/03.seniorDev.return.md`.
- **Pane ids go stale within a day** (`%58` became `%77`). Names are for people; ids are read fresh before every send.

## 3. Does the supervisor seat earn its place? — my view, to be opposed

**Seen so far.** The former controller changed one setting on a POINT within four minutes, with a check before it wrote. Its
pushes for the relay line worked on a poke. It also went from 56% to 40% of its context in one night on small jobs, and every
job cost two files and two pokes. The new seat pushed three commits on its first POINT within three minutes, and said plainly
what it did not know — its own model and effort. → `_bus/02.supervisorCli.return.md`.

**Where it earns its place — three things only:** the push (one writer of the remote), an act a head has no permission for,
and the caches. For anything a head's own child can do, the child is cheaper: no round trip by file and no second context.
The risk of a seat with full permissions is that everything drifts to it; so its brief takes authority from the assignment.

**Does eSharp save tokens?** I have no evidence that it does, and I expect the opposite: a manager, its partner, the desk and
the supervisor are spent on top of the two groups. What it buys is different — two lines move while you are away, each head
stays small and fresh, every frame is read by another brand, and your decisions reach you ordered. What it costs — the files
between seats, waiting on shared seats, and facts that go stale on a board. **Consequence, as I see it:** the shape pays when
two lines really run at once and you are not at the desk. For one line, a head and an auditor are enough.

**What would settle it** — three counts over one closed cycle of each group: tokens per closed cycle, waits on a shared seat,
and the number of your sittings.

## 4. Caches

Your note: hold the cache on the identity of the tmux window, as a thin lock for continuity.
- **I agree with the window as the key.** What must continue is the seat, not the CLI session: a clear, a compaction or a
  resume changes the session id, and even the pane id, while the window's name stays the address you chose.
  Proposed place: `~/.cache/nablarva/<tmux session>/CACHE.<window name>.md`.
- **Thin means pointers.** The gate, the last decisions with their files, the open threads, the next step. Not a cut of the
  transcript — the 241 kB cut is the opposite of a lock.
- **Who writes it** is open. The supervisor on request (today's rule) costs a round trip. The seat itself, before a clear,
  knows best what matters. Whether a native hook can write it at compaction is not checked — a question for a research spawn
  before anything is built.
- **What yesterday showed.** After three compactions the work was saved by files and the transcript, not by a cache. A cache
  would have answered only "where was I". That is its right size.
- A cache stays out of Git and does not travel between hosts until your own channel exists.
- Not read by me: `.dev/_backlog/caching-from-comp-to-cli/` — it is about what a running machine holds, a different "cache".

## 5. The poke as a kind of mail — my view, to be opposed

The poke is already half a mail: the file is the letter, the line only rings. For the shared terminal the same shape fits. A
seat that wants a command run writes a request file into the organ's inbox and rings; the gate reads the file, you approve,
the organ runs it, and the result is a file. No seat types into the terminal. The line needs no new syntax:
`[term r07] from lead.seswin -> read <path> ; ack: per file`.
- **It gives** a record of every request, approval before anything runs, and one way in — which is also the place for your
  "allowed or not allowed" setting and for the notice when somebody rings while the terminal is closed.
- **It costs** time per command, and a watcher or your hand at the gate.
- **Its limit:** a ring proves nothing about reading. The receipt is the result file.

## 6. Whose property

- **Syntax** — the pointer line, the POINT headings, the roster line, the tmux coordinates — belongs to the project and
  beyond: its home is the shared bus guide, where the pointer line already lives. It is not eSharp's.
- **The cache rule** — where, how thin, never in Git — is the project's. A cache's content belongs to one seat.
- **eSharp's own** are four things: the board, the manager's three duties, the pairing of brands, and the order of starts.

## 7. If eSharp proves itself — the shape of its RUNBOOK — my view, to be opposed

- **eSharp has no gate, so it gets no RUNBOOK.** Each group keeps its own RUNBOOK with its one gate. A RUNBOOK over RUNBOOKs
  would be a second authority.
- **What it needs once, as fixed text:** a short protocol chapter in the runbook guide, beside the cSharp one — the manager
  holds no state; one board; one queue to you; a partner of the other brand for every head; shared seats with a brief each;
  staggered starts; between groups only files.
- **What it needs per arc:** one page — the groups and their beds, the shared seats with their tmux coordinates, the seams.
  Today that is three files: the board, the decisions record and your roster. They could be one.
- **In each group's RUNBOOK:** one `head_note` line that names the protocol and points at that page.
- Whether it becomes a named protocol is your gavel.

## 8. The opposing read — seniorDev, 2026-11-26

Her file: `_bus/05.seniorDev.return.md`. All three views hold with changes. What changes in mine:

**On section 3 — the supervisor seat and the cost of the shape**
- **Only one of my three things is shown.** The first RETURN supports one publisher. It says little for a standing cache
  writer. And a head that reaches the limit of its permissions is first a reason to ask who authorized the act — not a reason
  to pass it to a seat that can. I take that: "an act a head has no permission for" needs Majkee's word in the POINT, always.
- **The benefit nobody has seen yet:** a supervisor that catches a conflict between two requests that are each valid alone.
  One such case is recorded, or that benefit stays open.
- **More tokens and faster progress are both guesses.** Keep the three counts, but against the same kind of accepted work done
  by a head and an auditor alone: tokens including children and shared seats, with missing figures marked; the minutes a shared
  seat really blocked a result; your sittings together with your active minutes; and the time to an accepted result, rework
  included. Two busy groups alone say little.

**On section 5 — the poke as mail for the shared terminal** — these are inputs for group 2's frame
- **What exactly was approved?** An approval is bound to the asking seat, the exact content of the request, and that one
  opening of the terminal. A changed request or a reopened terminal needs a new decision.
- **A second ring for the same request** returns the decision that already exists.
- **If a command may have run before its result was written,** the record says "outcome unknown", and it is reconciled before
  any retry. Otherwise one approval can become two executions.

**On section 7 — the shape for eSharp**
- **A seam needs an owner.** If group 1 stops after group 2 has taken its field list — who tells group 2 whether it may rely
  on that version? The page per arc names, for every seam: its owner, the evidence the receiving head accepts, and who brings
  an unsettled dependency back to you.
- **The board links your dated decision and the STATUS,** and keeps apart what you authorized and who can be reached today.
- **Staggered starts stay provisional** until a second arc has earned the rule.

**What she adds.** Follow one dissenting RETURN all the way to your decision sheet, and ask whether you saw the objection that
could have changed your choice. Today's case is the first: her dissent on the sandbox is in the decisions record, section 11,
and in my report to you, beside my own withdrawn view.

## 9. The view from outside — myShell, 2026-11-26

Her file: `answer.myShell.side-quest.2026-11-26.md`. She watched the same days across your tasks. What she saw that I did not:

**Read wrongly**
- **A question about "the pen" without the bed's name** — the answer was applied to the wrong bed.
- **An example taken as the order** — one sample name in a sentence was read as the rule.
- **"Queued", exit 0, read as delivered.** One line arrived two days later.
- **Times without a zone**, and a morning check reused in an afternoon answer.
- The dim suggestion on a Claude input row, read as typed text — my own case of yesterday.

**Where the thread broke**
- A handoff read only by its author. Context figures that were spoken and never filed. A cache that was stale on two points
  nine hours after it was written — and it was only 70 lines. Copies and tools kept in a private place with no pointer in
  the bed. Reserved names in a lock that disagreed with the live line.
- **What would have held it:** every claim says when it was checked and by whom; every thing kept outside the bed gets one
  line in STATUS.

**What the window lock should hold** — her list, and I take it as it stands: the window's name and its former names; session
id and pane id with the time they were read; the bed and its STATUS path; who holds the pen; the last decision file; open
threads as paths; the next step; the writer and the time. **Left out:** copied gate text, percentages, lessons, content,
anything private. And a warning: windows were renamed twice in three days, so the key itself moves.

**Rosters**
- **Missed:** a reader who is not the author at every hand-over; and an owner for the session-window line, which had none
  for days.
- **There without need (her guess):** the predecessor kept "on call" after the new lead had bound. And she herself sent the
  controller two copy jobs that any child could have done — the drift I named in section 3, seen in practice.

**Where my collection was wrong**
- Section 1, "the line carries no instruction": one of her notes carried new names in the line itself.
- Section 2, "one desk records your words": your words were also typed to her and to the lead. **A decision given in one
  seat's window reaches a bed only if that seat writes a file there. That seam has no owner.**

## 10. What I would put before you — mine, for your word

1. **The pointer line stays as it is,** with two additions: it names the bed whenever it is about a pen or a decision, and
   every time in a file carries its zone.
2. **"Queued" is not "delivered".** The receipt is the answer file. A line can arrive days late, so its label should let the
   receiver see how old it is.
3. **Your words reach a bed by a file, whoever heard them.** The seat you type to writes the decision file in the bed
   concerned, as the lead did with the pen today, or passes a pointer to that bed's head. This closes the seam in section 9.
4. **The cache is a lock, not a memory:** her field list, keyed by the tmux window with its former names, with writer and
   time, read as "true when written". Who writes it is still open.
5. **Every hand-over gets one reader who did not write it,** and every line has an owner at all times.
6. **The supervisor keeps the push.** Its other two uses are not shown yet; a job a child can do stays with the child.
7. **Measure one closed cycle** before judging the shape — seniorDev's counts in section 8, against a lead and an auditor
   working alone.
8. **If the shape stays:** one protocol chapter in the runbook guide and one page per arc that names an owner for every seam.
   No RUNBOOK for eSharp itself.
