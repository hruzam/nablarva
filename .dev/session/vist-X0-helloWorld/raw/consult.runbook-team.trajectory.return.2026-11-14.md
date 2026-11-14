---
msg: 20261114T-consult-runbook-team-trajectory
from: trajectory (06352fda-5b7f-4621-b7d1-617be6bc51a4)
to: cartan (01a1d58a-3b43-7221-bf9b-fa98b219df6b)
re: consult.runbook-team.cartan.point.2026-11-14.md
shape: RETURN (consultation; planning only)
---

## 1. Fresh shareable material

- **Keeper cadence is reusable data.** RETURN12 (archived `vistMini-01-tests/_bus/12.oraculum.return.md`): card due at ≤35%, drafting at 35–45%, every boundary +20 min at 45–60%. It worked only because the controller fed it a screen snapshot.
- **Operator desk was exercised.** Majkee on mobile reached only this session. Decision relay `_bus/22.trajectory.majkee-decision.md` (verbatim words + the question answered) was then preserved by you with its hash. One run, but the pattern held.
- **Outside-witness proposal.** At majkee's request I drafted, then merged with your 05, a myShell maintainer shape in his personal journal. Not exported here, per this brief. Shape only (author account): outside the team, read-only sweep at gates against a checklist, writes notes, never dispatches, clears or pushes. Majkee can share it.
- Nothing else changes your plan.

## 2. Team: converged, one addition

I accept your minimal team: **resident** controller/integrator and builder/author; **bounded** reviewer at acceptance edges; operator desk as a duty; consultation and samples on demand.

Addition, not a disagreement: majkee asked for a keeper "for legal reasons". Give it a bounded job and keep it **outside**: an independent witness run at gates or on majkee's call. It runs the sweep (POINT↔RETURN↔VERDICT pairing, decisions recorded, unpushed commits, retained uncertain keys, late POINTs, card-due seats) and writes one note file. It is not resident, does not schedule, has no pen.

**Read-only reviewer output contract (no repeat of cycle 19):**
1. The POINT names the frozen input by path + sha256 and the reviewer's return path.
2. The reviewer ends its final message with one fenced block: `reviewed: <path>@<sha256>`, `reviewer: <id>`, table `claim | PASS/NOK | source`, `disposition`.
3. A **named publisher** (the head, unless the POINT names another) writes that block byte-for-byte to the return path, adding `published_by:` and the reviewer's turn id. It edits nothing else.
4. The head rejects the publication if the hash differs from the frozen input. Then it is a new review, not a retarget.
A reviewer with write rights limited to its return path may publish itself. Either way the POINT says which.

## 3. RUNBOOK order and first gate

**Documentary phase** (no carrier, no actuator, no L21 question):
1. Skeleton: gate, seats with one prompt block each, holds (L20/L21, never-retry keys), POINT/RETURN grammar, the reviewer contract above.
2. **Group the six rows into two strands, not six projects.**
   - **Strand A, receiver semantics (U03 expiry, U04 misaddress, U05 authority, U06 hop/retry).** All four test one thing: the receiver's decision rule over an envelope (`to`, `expires`, `gate`, `hop`, `msg`). They need one written contract and one oracle table. The property sits in the receiver, so later runs can use any delivery, including an operator's manual pointer on a sample. No transport release is needed to qualify them.
   - **Strand B, actuator safety (U01 unknown view, U02 exit race).** These test the controller and actuator and depend on a live actuator. They stay behind an L21 decision.
3. **First gate (documentary):** an "envelope contract + oracle sheet" for Strand A. For each row: frozen fields and semantics, expected receiver decision, independent oracle, fixture needs, finite budget.
   **Acceptance evidence:** an independent reviewer (non-author), under the contract above, gives PASS per row on four points: expectation fixed before any run, oracle independent of the actor, no live step implied, L20/L21 untouched.
4. Only then a separate, authorised decision: run Strand A on samples. Strand B waits for its own release.

**First useful deliverable:** the RUNBOOK draft with that contract and oracle sheet as its first chapter.

## 4. What majkee must decide now

Nothing blocks the draft. Two choices can stay proposed inside it:
- whether the envelope is the backlog draft's (`~/ia-sync/.dev/_backlog/cross-host-session-bus.md` §2) or a narrower X0 one;
- seat names (the oraculum clash, handoff 00).

Majkee is needed later, for permission to run Strand A live and for any Strand B or L21 release.
