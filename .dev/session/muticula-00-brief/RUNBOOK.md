# RUNBOOK: muticula-00-brief

```yaml
goal: >-
  One master brief for muticula — the cooperative concurrency guard for agent CLI sessions
  sharing one git checkout — that carries every decision majkee made (D1–D5) faithfully,
  decides nothing else, and can open build step 0 in a numbered sibling.
gate: >-
  Majkee records GO or STOP on the muticula master brief after the witness, Cartan, confirms
  that its current revision carries D1–D5 faithfully and decides nothing else.
participant_0: [trajectory, {brand: anthropic, model: operator-selected, effort: operator-selected}, {host: office, role: cSharp head, sole writer of the brief's folds, status_owner}]
participant_1: [cartan, {brand: openai, model: operator-selected, effort: operator-selected}, {host: office, instrument: mail by path, role: standing witness — fold checks only; writes only the verdict path a POINT names}]
participant_2: [delta, {brand: anthropic, model: agent-default, effort: agent-default}, {host: office, role: zero-judgment file tasks spawned by trajectory only, reviewed before report}]
participant_3: [majkee, {brand: human, model: none, effort: none}, {host: office, role: brief owner, operator transport, gavel}]
status_owner: trajectory
head_note: >-
  cSharp (res/csharp-head-protocol.md): this seat authored the RUNBOOK and stays through the
  arc as navigator and status_owner; it folds the brief itself, spawns Delta for zero-judgment
  file work, names Cartan as standing witness, and never self-confirms the gate.
schema_note: >-
  runbook/GUIDE.md Structure + res/csharp-head-protocol.md read 2026-09-27 · status/GUIDE.md
  fixed fields · bus: _bus/<NN>.<seat>.<shape>.md. Session ff-sync.trajectory.cSharp-muticula.
```

## Why this session exists

Muticula restarted on 2026-09-26 from majkee's master brief. The first bed,
`~/ia-sync/.dev/session/runbook-upgrade-02-app/`, aimed at a gate this small cooperative guard
should not promise: atomic reservations, unique writer binding and pre-write refusal. It
closed as gate-changed, with its original gate unmet (Cartan's `VERDICT.md`, 2026-09-27). It is
the same animal, extended: the name stays, and the brief is the design.

## Fixed facts (settled before this session)

- **Decisions.** majkee decided D1–D4 on 2026-09-26 and D5 on 2026-09-27; they are in the
  brief's §6. Do not re-derive them.
- **B0 evidence.** The Claude lane is qualified ACCEPT, the Codex lane STOP. The synthesis is the
  old bed's `VERDICT.md`, and the keepers stay there, preserved by that bed's closure commit.
  Their evidence home is the old bed's committed paths, not a copy here.
- **Placement.** Nablarva flag L6: new experimental agentive shapes build in nablarva, and
  promotion to the surgical table is a reviewed merge.
- **Name.** "'muticula' only" (majkee, 2026-09-26).
- **`claude -p`** is B0 test instrumentation only, never a product dependency.

## Where everything is

| what | where |
|---|---|
| the brief (current revision) | `raw/muticula.master.2026-09-26.md` |
| reviewed revisions, byte-identical | `raw/muticula.master.2026-09-26.reviewed-{7c41b520 r0, 17a2641e r1, 6db74151 r2}.md` |
| gate receipt — Trajectory-reported | `raw/gate-fixture.2026-09-26.md` |
| Trajectory's relays to Cartan | `raw/relays/` — moved from the meeting room 2026-09-27; `move-map.2026-09-27.json` |
| Cartan's challenges, D1 point, r1 verify, r2 challenge | `~/ia-sync/.dev/session/runbook-upgrade-02-app/raw/cartan.*.muticula-*.md` |
| B0 evidence, its synthesis, the keeper inventory | old bed `VERDICT.md` · `promotion-manifest.{md,json}` · `raw/b0-claude/` · `raw/b0-codex/` · `raw/identity-probe4/` |
| lessons from the first bed | old bed `raw/cartan.experience-transfer.2026-09-27.md` |
| this bed's witness exchange | `_bus/` |

## prompt-0 — trajectory (cSharp head · status_owner)

```text
You are Trajectory, cSharp head and status_owner of muticula-00-brief.
Read this bed's RUNBOOK.md and STATUS.md, then the brief raw/muticula.master.2026-09-26.md
and the newest verdict in _bus/. Fold only what the verdict asks, into a new revision; keep
the reviewed revision byte-identical as raw/muticula.master.2026-09-26.reviewed-<sha8>.md.
No new decisions: anything beyond D1–D5 goes to majkee as a question, not into the brief.
Then write the next _bus/<NN>.trajectory-dashboard.point.md to the witness and update STATUS.
Done-when: the witness's latest verdict is PROCEED and STATUS names majkee's GO/STOP as next.
```

## prompt-1 — cartan (standing witness)

```text
You are Cartan, standing witness for muticula-00-brief. Read this bed's RUNBOOK.md, STATUS.md
and the POINT addressed to you in _bus/. Check the brief's current revision against D1–D5 and
the records the POINT names: does it carry them faithfully, and does it decide anything else?
Answer as a CHALLENGE (weakest point · verdict proceed / revise / stop · primary risk · one
alternative) at the exact verdict path the POINT names. No edits elsewhere.
```

## Known constraints and destructive holds

- **Brief only.** No product code, settings, deploy or build step in this session.
- **Git.** Nothing is staged or committed from this session without majkee's explicit word.
  The bed is untracked in nablarva. Nablarva flag L12: plain pull/push on `core`, never
  `pull --rebase`.
- **The old bed.** It is Cartan's until its preservation lands: no moves, edits or prunes there.
- **New decisions** are majkee's: the head asks, it does not fold.

## Acceptance evidence

- The brief's current revision and its reviewed predecessors, byte-identical and hash-pinned.
- The witness's verdict in `_bus/`, PROCEED on the current revision's sha256.
- Majkee's recorded GO or STOP in STATUS.

## What this session deliberately does not do

- Build or qualify anything. Build step 0 opens `muticula-01-<phase>` after GO.
- Preserve or prune the old bed. Its status_owner does that on majkee's Git and log-retention word.
- Decide cross-host exclusion (nablarva Stage 2) or worktree policy (Alternative B).
