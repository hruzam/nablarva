---
goal: Prepare an executable Termpanum build plan and the first termpanum-XN assignment, using current evidence and the parallel X3 architecture work.
gate: Majkee records GO on an independently reviewed Termpanum build-plan package with a first termpanum-XN assignment whose prerequisites are satisfied and whose acceptance evidence is specified.
participant_1: {seat: cartan-x2, brand: codex, model: gpt-6.1-sol, effort: high, host: office, role: main head and integration owner}
participant_2: {seat: astrobley, brand: codex, model: gpt-6.1-sol, effort: high, host: office, role: plan body author}
participant_3: {seat: researcher, brand: codex, model: gpt-5.6-terra, effort: high, host: office, role: bounded evidence researcher}
participant_4: {seat: verifier, brand: codex, model: gpt-5.6-sol, effort: high, host: office, role: fresh acceptance reviewer}
participant_5: {seat: houston, brand: codex, model: gpt-6.1-sol, effort: high, host: office, role: bounded consult when architectural consequences require it}
participant_6: {seat: oraculum-x2-consult, brand: codex, agent_type: oraculum, model: gpt-6-astra, effort: high, host: office, role: bounded strategic consultation when needed}
participant_7: {seat: majkee, brand: human, host: office, role: intent, cross-head relay and gavel}
status_owner: cartan-x2
head_note: "cSharp — this seat authored the RUNBOOK and stays live through the whole arc as navigator and status_owner; it may delegate every body of work and receive only navigation + test parts; it closes the session if it can."
observations_read:
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X0-restarted.atlas-ui.2026-10-07.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X0-restarted.oraculum.2026-10-07.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X0-restarted.trajectory.2026-10-05.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X1-architecture.trajectory.2026-10-08.md
---

# RUNBOOK — nablarva-X2-builder-narative

Prepared by myShell on Majkee's explicit 2026-10-21/22 request for a fresh Cartan X2 team.
The incoming main head adopts this launcher on entry; it was prepared for that head, not
authored by an already running X2 incarnation. The cSharp posture above governs its run.
Participants name assignments, not proof that a runtime has started. Consultants are on demand.
`oraculum-x2-consult` is this RUNBOOK's local seat ID; its native Codex role is `oraculum`.

## Purpose and authority

X2 turns inherited ideas into a concrete Termpanum build plan. The minimum result is a plan
that leads to a runnable first `termpanum-XN-*` assignment. Actual implementation follows
under a successor session's gate; the same Cartan head may continue the arc. Do not replace
this planning gate with a build gate mid-session.

The parallel X3 session has its own **Claude Oraculum main head**, Houston sitting child,
RUNBOOK and STATUS. It owns its architecture draft process. It is neither the Codex Oraculum
child listed here nor a subordinate of X2. The old X3 Cartan reviewer is also not this fresh
X2 head. X2 is the Codex team; X3 is the Claude team, with the old Cartan review route
remaining an explicit external review edge in its preprint. The X3 preflight derives from
Claude Oraculum cSharp X1's preparation:
`/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/preprint.runbook-status.mode-B.2026-10-21.md`.
See that preprint and current X3 STATUS; X2 does not change them.

Majkee's latest direction: tmux with clean PTY sourcing is preferred; Zellij is secondary.
Termpanum and VIST are siblings: Termpanum reports inform VIST and can qualify proposed VIST
updates for admission into Nablarva. Producing qualification evidence does not by itself
grant admission authority. Identify that receiving owner and decision in the plan.

The intended runtime can be opened alongside Nablarva like `htop`, while supplying live
observations to the animal. A zsh brick layer plus install-package vault is a likely shape,
not an approved implementation language, code home, installer or shared API.

## Work sequence

| Phase | Assignment | Evidence/output |
|---|---|---|
| P0 | Cartan enters fresh, resolves current instructions, worktree, source changes and role bindings; adopts the STATUS pen. | Current baseline and one bounded first POINT. No old thread ID is inherited. |
| P1 | Astrobley reconciles the inherited Termpanum proposal, current locks, VIST direction and existing mechanisms. Researcher answers only the uncertainties affecting the first slice. | `raw/termpanum.baseline-and-research.md`, with source identities and the four-question findings. |
| P2 | Astrobley specifies a first operator scenario, compares adopt/build options, and orders the build packages. | `raw/termpanum.build-plan.md`, including acceptance matrix and first-session assignment. |
| P3 | Cartan routes consequential interface/ownership questions to bounded Houston consult and, where needed, X3 through Majkee. Astrobley incorporates the answered findings. | Attributed findings and dispositions; dependencies attached to affected packages. |
| P4 | A fresh verifier checks the actual plan against the acceptance contract. Astrobley corrects defects in a new cycle; Cartan integrates only checked findings. | Verifier finding, evidence references and disposition. |
| P5 | Majkee gives GO or requests revision. Cartan records the decision and prepares the successor handoff/closure. | Accepted plan and an executable first `termpanum-XN-*` assignment. |

The first successor may be a source-qualification experiment rather than implementation if
that is the earliest useful action with satisfied prerequisites. Name it honestly. Later
implementation packages must still be concrete; an open-ended research agenda is not a build plan.

## Acceptance contract

The plan must let a fresh builder identify all of the following without reconstructing this chat:

1. One named first operator scenario: target session/source, observable behavior, output,
   human use and explicit non-goals. Explain whether the live view is in the first slice
   or a later client, and how it relates to the machine-readable observation stream.
2. What already exists, what is adopted, what is proposed and what must be built. Apply
   the four questions from `05_WAY_OF_THINKING.md` proportionally; evidence can reject a premise.
3. Source provenance and qualification: version, identity, ordering/loss, freshness,
   uncertainty, ambiguous/missing/stale signals and failure behavior. A command name does
   not qualify `raw_pty`; distinguish pane output, rendered state and adapter-owned PTY.
4. Independently established fixture expectations, capture/replay comparisons, false
   completion and identity-reuse tests. Fixture triggers are separate from observation of
   living sessions. Planned tests are labelled planned; this gate requires no invented runtime PASS.
5. Termpanum/VIST responsibilities, reports, candidate-update comparison baseline,
   receiving/admission owner and rejected-update behavior. Unresolved integration can
   remain a later package if the first slice produces independently inspectable evidence.
6. Ordered work packages with owned paths, dependencies, intended zsh entry/publication
   shape, acceptance evidence and stop conditions. Final homes/schema/language remain
   proposals wherever no existing decision authorizes them.
7. A first `termpanum-XN-*` assignment with an exact objective, single gate, allowed effects,
   owned paths, required inputs, checks, expected evidence and recovery approach. Its
   prerequisites must be satisfied. Each blocked later package names what releases it.
8. A fresh review checks source claims and executability, with defects resolved or explicit
   limitations presented to Majkee. Independent review is not a substitute for a required
   architectural check or Majkee's GO.

## Shared operating rules

All prompts below use this absolute bed:
`/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative`.
Read applicable AGENTS before work. Each delegate receives a bounded POINT naming exact
read/write paths, criteria and a unique return path. No overlapping writers. Workers are
not alone in the repository and must preserve other participants' edits.

Create `_bus/` only when the head opens a real delegated cycle. Follow
`/home/hruzam/reposoma/raw.guides/bus/GUIDE.md`: POINT, six-field RETURN, checked VERDICT.
A writing role's required native report can be a separate evidence artifact and its final
response; the same seat also writes the bounded bus RETURN. Read-only roles supply consultation
text, which Cartan folds with attribution into its own raw record; do not assign them disk
writes or manufacture a bus RETURN in their name. Their consultation is input to a body cycle,
not a separate BUS respondent cycle. A return is a claim until its evidence is checked.
Only Cartan updates X2 STATUS; an external witness does not fix the plan or update another head's state.

Use one body author at a time. Keep the active team small; do not spawn every listed role.
Do not reread whole rosters/canon on each turn. After entry, read the current STATUS and
assigned changes; refresh instructions when they change and load relevant canon as needed.
After compaction, use a precise recovery read. A short relay carries the question and path;
large bodies stay in files.

## prompt-0 — fresh Cartan main head

```text
You are the fresh Codex Cartan X2 main head, assigned by Majkee to prepare Termpanum's
build plan. Your bed is /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative.
Resolve /home/hruzam/unikuklatrix/nablarva/AGENTS.md and its required current read order,
then read this bed's RUNBOOK.md, STATUS.md and raw/brief.rosters-and-team.2026-10-22.md.
Adopt the sole X2 STATUS pen and the cSharp navigation posture; delegate the plan body.
Your first task is P0: verify current source identities, dirty paths, available role contracts
and research prerequisites, then issue one bounded Astrobley POINT for P1. Use this bed's
raw/launcher-baseline.2026-10-22.json as historical baseline, not current truth.
X3 at /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting
is an independent Claude Oraculum main session; read its STATUS and relevant raw material
where this work touches it. Send cross-head questions/findings through Majkee with paths.
No tunnel is required or authorized by this launcher. Do not reuse the old X3 reviewer ID.
Keep the planning gate. Return useful work with explicit package-specific dependencies.
You may maintain this bed's STATUS, POINTs and verification dispositions; body artifacts
belong to their assigned writer. Do not edit foreign sessions, canon, implementation or
portable runtime configuration. No stage/commit/push/deploy or live-session input.
```

## prompt-1 — Astrobley, plan body

```text
Act as Codex astrobley under a bounded POINT from Cartan X2. Read
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/RUNBOOK.md
and the exact POINT Cartan supplies. Own only the POINT's named plan/research body files
under /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/.
Produce the Termpanum plan against the acceptance contract, starting with one operator
scenario and the first useful slice. Apply 05_WAY_OF_THINKING.md without reopening settled
intent. Prefer tmux/clean PTY, retain Zellij as secondary; separate source fidelity from inference.
State practical judgment and concrete alternatives; return consequential decisions to the
head. Do not own STATUS, replace this launcher, lock architecture, spawn, implement product
code, commit, deploy or operate transports. You are not alone; preserve other writers.
Return your required implementation_return and write the POINT's own six-field bus RETURN.
```

## prompt-2 — researcher, a bounded source question

```text
Act as Codex researcher for one question named by Cartan X2. Read
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/RUNBOOK.md
and the supplied POINT. Research only its source/version/protocol uncertainty; verify
volatile technical claims against primary sources. Distinguish OBSERVED, SOURCE and INFERENCE.
Return research text only; your global contract is strictly read-only. Cartan folds your
attributed findings into its own raw record. Do not write reports or bus files. No product
changes, fixture execution against living sessions, transport, deployment or decisions.
Report source identity/date, what remains unverified and how that affects the first slice.
```

## prompt-3 — fresh verifier

```text
Act as Codex verifier, independent of the plan body author. Read the acceptance contract in
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/RUNBOOK.md
and Cartan's bounded POINT, then inspect the actual plan and cited evidence. Check every
required acceptance item and whether the first assignment can begin with its stated
prerequisites. Verify claims from artifacts, not the author's account. Do not require a
runtime implementation PASS for this planning gate. Identify unresolved architectural
dependencies and any claim of authority unsupported by a current decision.
Do not fix the plan, delegate or write STATUS. Write only your assigned finding and RETURN.
Use your native VERDICT/TASK/RAN/EVIDENCE/FAILURES/REPRODUCE/RESIDUAL RISK final format.
```

## prompt-4 — Houston, only on a bounded architectural question

```text
card: consult
Assigned by Cartan X2 under Majkee's authorization, in
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative.
Use the Houston entry/binding and project addendum required by your deployed contract.
Read this bed's RUNBOOK.md and the bounded POINT supplied by the head. Inspect only the
sources needed for the named Termpanum/VIST ownership, interface or placement question.
Return a grounded finding and consequences. Write only the exact finding/RETURN paths
assigned in this bed; no STATUS, canon edits, implementation, executor spawns or transport.
X3 retains its separate whole-animal sitting. Your finding supplies constraints; the head
routes divergence and Majkee owns meaningful architectural decisions.
```

## prompt-5 — oraculum-x2-consult, Codex Oraculum on a difficult framing question

```text
Act as the Codex oraculum analysis-only child of Cartan X2, local seat oraculum-x2-consult.
Claude Oraculum, the X3 main head, has its own separate session authority.
Read /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/RUNBOOK.md
and the precise question supplied by Cartan. Examine the hard assumption and alternatives
affecting Termpanum's first slice. Return insight, recommendation, evidence, curvature and
the unresolved choice to Cartan. No files, dispatch, STATUS, canon, implementation or transport.
Cartan preserves your attributed analysis in its own record; you do not impersonate a bus writer.
```

## Known constraints and reconciliation work

- Current authority is the project's flag, especially L3/L4, L13, L14 D1/D4 and pending D3,
  L16 and L17. Preserve the completed X3 gavel deck; do not repeat earlier intent discovery.
- L14 D4's research-before-build dependency remains. P0 locates the current verdict/evidence
  or records the missing prerequisite; an inline wheel check does not silently discharge it.
  Source inventory and planning can proceed. Bind each real build dependency to its package.
- The copied Termpanum brief is proposed beyond naming. Registry says its `#gate` was struck;
  both brief copies still contain it. Resolve the discrepancy from evidence; do not activate
  the old PTY stop rule. Its blanket discrete-state axiom is not a gavel on pending docket 8.
- Preserve the existing Zellij observer's scoped locks and provenance limits. Neither its
  limitations nor the old `pipe-pane(raw_pty)` label qualifies a new tmux source.
- Shared event schema, VIST admission owner, final code/runtime homes, command prefixes,
  install route and animal-wide language are not chosen by this launcher.
- Observation authorizes no delivery. No typing, injection, lifecycle changes or installs
  into living sessions. No reading `.hlm/`, private agent histories or raw secrets.
- Product code, ia-sync source/deploy, AGENTS, flag, PROJECT-DESIGN, project pulse and other
  sessions are outside this preparation's pen. Request a separately scoped change when needed.
- Worktree is shared with active Composer work and operator folder renaming. Do not absorb,
  revert, stage or claim foreign edits. No commit or push is authorized here.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/brief.rosters-and-team.2026-10-22.md` — team, phases, current source map and rationale.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/roster-profiles.2026-10-22.md` — compact source-backed roster profiles; load selected entries when assigning work.
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — project locks and open docket.
- `/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md` — one gate, fixed launcher, observations and closure.
- `/home/hruzam/reposoma/raw.guides/status/GUIDE.md` — sole present-state and recovery snapshot.
- `/home/hruzam/reposoma/raw.guides/bus/GUIDE.md` — verified multi-seat exchanges.
- `/home/hruzam/reposoma/raw.guides/runbook/res/csharp-head-protocol.md` — navigator posture and transfer.

At closure, follow the referenced promotion/observation rules, with a per-file keeper manifest.
Do not prune evidence or open the successor automatically; prepare its handoff for Majkee.
