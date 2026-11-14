---
superseded: "Current staffing/routing and trial disposition: ../RUNBOOK.md, ../STATUS.md and /home/hruzam/ia-sync/ARCHIVE.md; body retained as historical substrate, not execution authority."
kind: handoff
date: 2026-11-13
brand: claude
seat: trajectory|engineer (Claude Opus, home)
from_bed: ~/ia-sync/.dev/session/vistMini-01-tests/ (head: trajectory; partner: cartan|astrobley, Sol)
for: the next VIST team, head oraculum|crawlers (Codex, Astra)
status: experience transfer. Not a RUNBOOK, not a gate verdict, not a transport release.
---

# vistMini → vist-X0-helloWorld: index

vistMini-01-tests was an **unplanned, spontaneous** trial on home (2026-11-12). It tried to get a Claude seat and a Codex
seat to exchange bus pointers on one host, with three ordinary messages each way and no operator relay. It did not
close its gate. It did produce evidence on which doors exist, which fail and why. This set carries that evidence here
as substrate for a real RUNBOOK.

## Read in this order

| # | file | what it gives |
|---|---|---|
| 00 | this file | map, team notes, trajectory's advice |
| 01 | `handoff.vistmini-01-evidence.trajectory.2026-11-13.md` | what was tested, counts, every carrier observed, exit codes |
| 02 | `handoff.vistmini-02-scars.trajectory.2026-11-13.md` | team scars, therapy style: what went wrong in us, not only in code |
| 03 | `handoff.vistmini-03-runbook-substrate.trajectory.2026-11-13.md` | proposed shape for the next RUNBOOK: ladder, resolver, carriers, cases |
| R | `roster.vist-x0.2026-11-13.md` | seat rows (ids, panes, carriers) for majkee to fill. Resolver data |
| C | `handoff.vistmini-cartan.cartan.2026-11-13.md` | **cartan's side**: adapter internals, Codex-side surprises, advice to the fresh Sol head, five amendments to 03 and the roster |

**Trajectory on cartan's amendments (2026-11-13): accepted, all five.** Where they conflict with my files 01, 03 or the roster, his
wording wins: (1) candidate ≠ qualified route, and my "native doors for 3 of 4 directions" overstated it. (2) one logical message id across carriers;
the ladder's "one later retry" needs a released limit, expiry and revalidation. (3) enqueue ≠ submission ≠ consumption. (4) no tmux =
not "absent". (5) the hook copy is unqualified. His auditor qualifier (read / run approved checks / never mutate) replaces my "no execution".
Also from h01: a copy ring needs a payload the adapter grammar accepts. My `[copy h01]` was refused 30. That was my request's flaw.
h01 record: poke = `codex queue` ✓ (no relay). Copy = clean refusal 30, file fallback ✓. Work ✓ (nonce match). Done ring = **cartan's own
labelled manual notice** into Claude pane %3 (majkee was away; allowed after a clean refusal, backlog §4.9). It submitted on the first
try in Claude. Not an adapter success, not counted. Lesson: a bell payload must be in the adapter's grammar, or the bell isn't automatic.
Git in nablarva is L12: plain `git pull`/`push`, **never `--rebase`**.

Source bed (evidence, read-only for you): `~/ia-sync/.dev/session/vistMini-01-tests/`. `_bus/01–05`, `reports/`,
`scripts/bus-poke.sh`, `scripts/handoff-once.sh`, `tests/adapter-test.sh`. VIST design itself: the reading map Oraculum sent
(marker VIST-READING-20261112-01). The main design is `.dev/session/nablarva-X4-vist/raw/vist-01-principle-and-applications.md`,
under L20/L21 in `.dev/session/flag.md`.

## Where vistMini stopped (state at 2026-11-13)

- Codex→Claude: **3/3** through the tmux adapter (cycle 03).
- Claude→Codex: **1** clean delivery (q01, `codex queue`, cycle 05). The 0/3 by tmux keystrokes (cycle 03) stands.
- VERDICT 05 ACCEPT (ia-sync `d48b613`): q01 confirmed, no operator input (majkee). Bed paused, gate open.
- Permissions: not witnessable. The Claude seat ran in auto mode.
- Cross-host: not attempted.

## Team

First proposal by majkee (2026-11-13):

| seat | vendor · model | class | cwd |
|---|---|---|---|
| `oraculum\|crawlers` | Codex · Astra | engineer, head | `~/unikuklatrix/nablarva` |
| `cartan\|astrobley` | Codex · Sol | senior-dev | `~/ia-sync` |
| `trajectory\|delta` | Claude · Opus | senior-dev | `~/unikuklatrix/nablarva` |
| `oraculum` | Claude | auditor | `~/ia-sync` |

Revision under discussion (majkee + trajectory, 2026-11-13; majkee decides):

| seat | vendor · model | role | note |
|---|---|---|---|
| `cartan\|astrobley` | Codex · Sol | **head** | **fresh** session from these handoffs. Issues POINTs, verdicts, STATUS. Delegates the building |
| `oraculum\|crawlers` | Codex · Astra | strategist, **outside** the build | consulted only at gates and direction changes, by brief. Never receives cycle pointers |
| `trajectory\|delta` | Claude · Opus | senior-dev, Claude-side builder | |
| `flight` | Claude · Fable | auditor | replaces Claude `oraculum` (removes the name clash). Briefed **read-only, no execution** |
| 2 × sample | 1 cheap Claude, 1 cheap Codex | live test receivers | receive, write nonce receipt, stop. All disruptive cases run here, never on senior panes |

## Trajectory's seating advice (mine, marked; not canon)

- **[trajectory] Choose the head for judgment and context discipline, not transport.** Once a resolver delivers, the head's vendor
  matters less. Cartan as head is pragmatic (Codex↔Codex is native) on two conditions: a **fresh** session (today's Sol thread
  carries a day of adapter design, i.e. framework memory), and **he does not build or verify his own adapter** (`bus-poke.sh`
  is his. Writer's blindness). The head reads RETURNs and verdict evidence. Children run the checks.
- **[trajectory] Strategist isolation must be strict.** Astra outside the build is right only if she never receives cycle
  pointers. Otherwise she drifts into a second head. Gate consults by brief, answers as files.
- **[trajectory] Cheap samples are the live fixtures.** They fix scar S2 (stand-ins passed, live failed): real receivers that
  are expendable. Run busy/duplicate/dead/`--resume`/writer-conflict cases on them only.
- **[trajectory] `flight` as auditor:** its identity is coordinator and executor. Strong model, wrong reflex for audit. Brief
  it explicitly as read-only verifier, no execution, no fixes. NOK goes back through the head.
- **[trajectory] Claude head later?** Reconsider after the 4-direction matrix. Today a Claude head receives from Codex only
  by tmux or the unexplained delivery worker.

## Trajectory's operating advice (mine, marked; not canon)

1. **[trajectory] Two seats named `oraculum`** (first proposal). In any envelope `from: oraculum` becomes ambiguous, and so do
   STATUS writer lines and receipts. **Resolved in the revision** by seating `flight` as auditor. Keep the rule anyway: full seat ids
   everywhere and `vendor:` required in the envelope. Identity confusion is exactly the failure VIST exists to prevent.
2. **[trajectory] Cwd vs bed.** The work lives in nablarva. cartan and the auditor sit in `~/ia-sync`. Launch cartan with
   `--add-dir ~/unikuklatrix/nablarva`. Start the auditor in nablarva, or give it an explicit read root, or it audits from the wrong
   tree's rules (each repo's AGENTS.md differs).
3. **[trajectory] Decide the Claude permission mode before cycle 01.** In auto mode the allowlist never decides anything,
   so the "allowed vs asked" boundary cannot be witnessed. If the gate wants a permission statement, run at least one Claude seat
   in default mode with a project `.claude/settings.local.json`.
4. **[trajectory] Pick carriers from evidence first, then build.** Native doors exist for 3 of 4 directions (file 01 §3). Do
   not spend cycles 01–03 on keystroke guards the way we did. Keystrokes are the fallback carrier, not the base.
5. **[trajectory] Keep the head off the transport.** With a Codex head, Codex→Codex is native and stable. The temptation is
   to route everything through the head. Don't: the head issues POINTs and verdicts; a hardcoded resolver delivers (file 03 §2).
6. **[trajectory] One push owner, declared on day one**, and Git windows serialized. It worked once we had it. It cost us a
   rebase scare before.
7. **[trajectory] Every POINT carries a `bell:` field.** Our one ambiguity (cycle 04: "no send-keys" vs "ring me") came from
   leaving it implicit.
8. **[trajectory] Watch context budget.** Sol hit 25% mid-trial. Research belongs to child agents. Seats keep task memory, not
   framework memory (majkee's point, and he is right).
9. **[trajectory] Operator views:** two terminals on one tmux session always mirror (the current window belongs to the session).
   Use grouped sessions: `tmux new -t <session> -s <session>-<viewer>`.
10. **[trajectory] Is nablarva public?** ia-sync is. Raw captures of panes contain everything on screen. Redact before commit,
    keep raw frames local (mode 0600), as vist-01 already says.
