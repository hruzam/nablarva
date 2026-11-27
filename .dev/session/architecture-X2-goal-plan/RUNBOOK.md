# RUNBOOK: architecture-X2-goal-plan

```yaml
goal: >
  One GOAL plan that Majkee can sign in one sitting: which open beds are entered, merged or stopped, and how relay
  tests, the observation consumer, a bounded hcom review and continuity are built next — as coding work with test
  loops, each in its own worktree.
gate: >
  Majkee records his countersignatures or STOP on one fixed GOAL plan in this bed. The plan says, for every bed open
  in pulse.md on 2026-11-27, whether it is entered, merged or proposed for his STOP; and for relay tests, the
  observation floor with its first consumer, a bounded hcom review, and continuity it names each proposed line, bed
  or task with home, owner, worktree and file ownership, order with reasons, dependencies, evidence of completion,
  and every countersignature that is his by lock. Beside it lies a recorded walk by an independent fresh reader from
  AGENTS.md to each line's owner, evidence and first safe action. The plan opens no session and locks nothing.
participant_1: [lead (flight), {brand: claude, model: Fable 5.2, effort: session default}, host: home, role: "navigator and status_owner; writes the plan; tmux window lead, pane %70"]
participant_2: [auditor, {brand: codex, model: GPT-6.2-Astra, effort: high}, host: home, role: "one check of the plan before Majkee reads it; tmux window auditor, pane %66", instrument: relay]
participant_3: [controller, {brand: codex, model: GPT-6.2-Sol, effort: medium}, host: home, role: "git: path-scoped commits and pushes on a POINT; tmux window supervisor-relay, pane %59", instrument: relay]
participant_4: [exec desk, {brand: codex, model: GPT-6.2-Sol, effort: medium}, host: home, role: "walks Majkee through the plan in plain language if he asks; tmux window exec, pane %68", instrument: relay]
participant_5: [majkee, {brand: human}, host: home, role: "the countersignatures; every release; the manual sender if a pointer fails"]
status_owner: lead (flight)
head_note: "cSharp — this seat authored the RUNBOOK and stays live through the whole arc as navigator and status_owner; it may delegate every body of work and receive only navigation + test parts; it closes the session if it can."
schema_note: "runbook/GUIDE.md and status/GUIDE.md as read on 2026-11-26 and 2026-11-27; authored through the /runbook posture by the closing head of relay-X2-research, as that bed's RUNBOOK was by its predecessor's"
wake: "the lead stays (cSharp); no other seat is woken by the operator. Reason: Majkee's word of 2026-11-27, 'go with the plan'."
```

## Why this session exists

Majkee asked the team on 2026-11-27 for one plan and said he will not decide its organisation. The research gate
before it is closed: `relay-X2-research`, GO on a verdict that says the relay program as first scoped does not open
now, while the bridge that runs (a file, a short pointer to it, a watch) keeps serving. He wants to build beside
that bridge. Thirteen beds stand open in `pulse.md`; eight have had no commit for three weeks or more. A plan that
adds beds without settling those makes the same failure again. The plan crosses the relay line and the lab line, so
it is neither's chapter (the architect's finding, in References).

## Fixed facts

- **The research verdict is the founding reference** for the relay part: `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/research-verdict.md` (with Erratum 1).
  It refuses the *program* — a state tracker and a terminal impulse layer. It does not refuse tests that describe
  what runs and qualify nothing.
- **A class release exists** (Majkee 2026-11-27, `/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X2-goal-plan/raw/decision.majkee.release-and-go.2026-11-27.md`): throwaway
  test sessions in a separate tmux sandbox server. No living CLI is killed or touched.
- **Still his alone:** any wake typed into a living pane; the choice of the carrier toward a Codex seat; who owns
  the observation record; any change to `AGENTS.md` or to a lock; the name of a relay chapter when it opens; STOP
  or GO on any bed.
- **The names `relay-X3-pty` and `relay-X4-tracker` are reserved** and are not spent on anything else.
- **How this bed works — on his remark about bureaucracy:** planning checks are done by children of the lead in
  parallel, each writing one file into `raw/`; the bus is used only for the auditor's one check and for commits; a
  second round happens only for an error of fact; the plan explains every code where it uses it and stays under 150
  lines.

## prompt-0 — lead (flight)

```text
You are the navigator and status_owner of /home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X2-goal-plan/.
1. Run four planning checks as children, in parallel, each writing one file into raw/ and nothing else:
   beds (every open bed of pulse.md: enter, merge or stop, with the reason and what it overlaps) ·
   relay tests (worktree, sandbox tmux server, where test code lives, the first test loop, what counts as a pass) ·
   observation consumer (the smallest consumer and record the research supports; which existing bed is its home) ·
   hcom (licence and reuse terms first; then what its tests cover against the two-vendor bridge that runs).
2. Write raw/../GOAL.plan.md from them: a checklist in order with reasons, owner, worktree and files, dependencies,
   evidence of completion per item, and one list of the countersignatures that are Majkee's. Under 150 lines.
   Every code said in full where it is used.
3. Give the plan to the auditor for one check (POINT on _bus/); in the same POINT ask what the two relay process
   records in .dev/observations/ say the plan should take. Take its points.
4. A fresh reader — a child that has seen nothing of this bed — walks from AGENTS.md to each line's owner, evidence
   and first safe action, and records where it got lost: raw/walk.fresh-reader.md. Repair what it found.
5. One ask to Majkee, in a file he can write into: raw/decision.majkee.goal-plan.2026-11-27.md.
Done when his countersignatures or STOP are recorded. Git goes through the controller; you commit only a POINT and
STATUS.
```

## prompt-1 — auditor

```text
Read the POINT the lead names in /home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X2-goal-plan/_bus/.
One check of GOAL.plan.md against its four check files in raw/, the research verdict and the locks: is anything in
it wrong on a fact, does it spend a reserved name, does it open or release anything by itself, is a signature that
is Majkee's missing from its list? Look only; write only your RETURN, under the six headings of the bus guide.
```

## prompt-2 — controller

```text
On a POINT from the lead: stage and commit exactly the named paths, path-scoped, then fetch and push core — plain,
never rebase, never force, no amend. Stage no other file. Write only your RETURN.
```

## Known constraints + destructive holds

- **No living CLI is killed, restarted or typed into.** The seats of the tmux session `helloWorld` and every other
  existing session are out of scope for any test. This bed starts no session at all; the release is for the beds
  the plan proposes.
- **L4** (no agent types into a pane; the reply bell of the file-poke chapter is the one allowance) · **L12** (branch
  `core`, plain pull and push, path-scoped commits, other sessions' files never staged) · **L21** (every activation
  needs a release — the class release above is the only one given) · **L22** (`.majkee/` and `.hlm/` never read or
  listed, in any repository).
- `CACHE.md` and `CACHE.*.md` are Majkee's: never opened, excluded from every search.
- Not staged without his word: everything under `.dev/_backlog/`, and `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/roster.md`.
- Not this bed's seats, not poked: `seniorDev`, `myShell`, `eSharp`, `supervisorCli`. The windows `spare-codex` and
  `spare-claude` may hold fresh heads (his roster) — not needed for a plan.
- Web research reads; it posts nothing and sends no private path, name or address to any service.
- His typed words stand verbatim only in `raw/decision.majkee.*.md`. A bell or a handoff from a seat is never his word.

## Acceptance evidence

- `GOAL.plan.md`, with the four check files in `raw/` it rests on.
- The auditor's RETURN and the lead's VERDICT on it.
- `raw/walk.fresh-reader.md`.
- Majkee's countersignatures or STOP in `raw/decision.majkee.goal-plan.*.md`.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/raw/decision.majkee.original-intent.2026-11-27.md` — the assignment, in his words.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/raw/decision.majkee.gate.2026-11-27.md` — GO, and his remarks: own worktree for a second development; tests in a session worktree; bureaucracy.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/raw/consult.houston.goal-plan-home.2026-11-27.md` — the architect's finding on this bed's home, order, locks and authorship; one seat's finding, unchecked.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md` — the relay line: what is open, reserved, carried.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md` — the open beds. `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — the locks.
- `/home/hruzam/unikuklatrix/nablarva/.dev/observations/relay-X2-research.flight.2026-11-27.md` and `relay-X1-probes.flight.2026-11-26.md` — what the last two relay beds taught about running sessions.
- `/home/hruzam/unikuklatrix/nablarva/.dev/_backlog/first-blind-triangulation-relay/` and `/home/hruzam/unikuklatrix/nablarva/.dev/_backlog/blind-triangulation-programatic-approach/` — the blind answers and briefs, Majkee's own filings.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/raw/master.symmetry.relay-and-floor.collision.2026-11-26.md` — relay and floor answers side by side; seven proposed tests.

## What this session deliberately does not do

- Start a session, run a test, create a worktree, or write code. Those belong to the beds the plan proposes.
- Design the vendor-neutral mailbox and adapter core. That is `relay-X3-pty`'s idea, and the architecture needs a
  blind triangulation before it locks (L14, part D7).
- Stop, merge or enter any other bed. It proposes; his signature does it.
- Keep a checklist of progress. The plan is fixed when signed; progress lives in each bed's STATUS.

## Provisional coordination carry-forward

- Shared coordination and retirement obligation: `/home/hruzam/reposoma/raw.guides/bus/res/file-poke.md`, §Carry-forward and retirement.
- Owning development line: none of its own — this bed is on the architecture line and uses the bridge only for the auditor's check and for commits; the shared bridge is tracked at `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X.ledger.md`.
- At closure, account for the provisional dependency in that ledger. This bed's poke log carries the field "operator had to step in" and continues the count from the seven routine pointers of `relay-X2-research` (rule: `/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X2-research/raw/pokes.log.md`, the quoted block before p11).
