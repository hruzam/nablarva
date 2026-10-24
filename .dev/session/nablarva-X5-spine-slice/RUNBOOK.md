# RUNBOOK: nablarva-X5-spine-slice

```yaml
goal: >-
  The body has a running spine — observe → record → view — built on the two shared layers majkee
  named (address registry · shared observation record) under the config rule, each proven by a
  second client, with no byte written into any session. The first construction of nabLarva.
gate: >-
  Majkee records GO or STOP on a witnessed read-only spine slice — one producer writes the shared
  observation record in per-writer files at a config-resolved home, the address registry holds one
  seat-addressed entry per pane written by ovitmugen on `ov-up` and surviving `ov-down`/`ov-up`, a
  second client reads both to show one derived state per seat, and an independent witness confirms
  that no byte was written into any session.
participant_1: {seat: cartan-x5, brand: codex, model: per Cartan's roster at wake, effort: high, host: office, role: main head and integration owner — cSharp; authors nothing above this RUNBOOK; sole STATUS pen; delegates every body of work}
participant_2: {seat: astrobley, brand: codex, model: per roster at wake, effort: high, host: office, role: implementer — contracts, registry writer/reader, record layout, producer, view; flags better approaches; returns consequential choices to the head}
participant_3: {seat: verifier, brand: codex, model: per roster at wake, effort: high, host: office, role: fresh witness of E1–E6 against the frozen yardstick; never fixes; resumed for re-passes}
participant_4: {seat: researcher, brand: codex, model: per roster at wake, effort: high, host: office, role: one bounded source question at a time (tmux hook semantics, O_APPEND atomicity on the target fs) — read-only}
participant_5: {seat: houston, brand: either, model: per binding, effort: high, host: office, role: card consult — P1 contracts if a seam is crossed; E7 at closure; writes nothing}
participant_6: {seat: majkee, brand: human, host: office, role: intent · one-line decisions on the costed deck · GO on the component's disk name · the skin note in his own voice · GO on the gate}
status_owner: cartan-x5
head_note: "cSharp — /home/hruzam/reposoma/raw.guides/runbook/res/csharp-head-protocol.md; authors the bed's STATUS at entry and stays live through the arc as navigator and status_owner"
schema_note: runbook GUIDE verified 2026-09-17; status GUIDE gaveled 2026-08-27; res/ chapter born at authoring (sequence + U-rows)
observations_read:
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X0-restarted.oraculum.2026-10-07.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X1-architecture.oraculum.2026-10-22.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X1-X3-closure.oraculum.2026-10-24.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X2-builder-narative.cartan.2026-10-23.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X3-architecture-sitting.oraculum.2026-10-23.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/harvest.2026-10-24.agol.md
  - (re-run `ls /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva* architecture*` at entry; architecture-X0 and X1 promote theirs before this bed opens)
```

## Why this session exists

nabLarva has a map (docs/ARCHITECTURE.md), law (flag L1–L23) and three bricks that converged on one layering without coordination — composer = service, ovitmugen = view + gates, HELLO r1 = substrate — and no construction: observe and record have zero code. The workflow majkee wants, HELLO ("read this file and give me the message back within the same bash"), is delivery and cannot be built, observed or qualified until something runs underneath it. Every brick built before the shared layers exist births its own addressing and its own signal path — "two mechanisms … destroying the stream" (majkee, 2026-10-24). This bed builds the smallest vertical that forces the two shared layers to exist and be read by a second client, keeps every write out of every session, and leaves HELLO to the next bed. Decided by majkee in the architecture-X0 deck (X0-1…X0-7 all = a, 2026-10-24); head brand Codex by his word ("X5 Head → codex", 13:10 CEST). Authored by oraculum(arch-X0) under `/runbook`.

## Fixed facts

- Prerequisite: `architecture-X1-bookkeeping` writes ARCHITECTURE r8 (split, component, home). If r8 is not on disk at entry, cite the X0 package with a git pin and carry an X1 dependency row in STATUS; do not wait silently.
- Implementing a shared layer needs its own release (locked: L21 (2)). **This bed's GO is that release.** Until then nothing here is canon.
- This is construction, not delivery: no byte enters any session (locked: L4, L17). A step that wants to type into a pane is a STOP.
- The two shared layers live in ONE new shared-substrate component — own thin folder per L18, disk name chosen in P1 after the mandatory duplicate/cross-interference sweep, **majkee GO on the name**; steward interim = cartan-x5 (U-steward). `said: majkee (X0 deck X0-3)`.
- Home: project-scoped state `<project>/.nablarva/`, machine defaults `~/.nablarva/`; every path resolved through the config rule — no literal path in any script. `said: majkee (X0 deck X0-4)`.
- Working split (`said: majkee`, X0-2): termbrana composes/submits, ends at a packet file in the bus; stridulatrix sends. This bed touches neither.
- Houston's five constraints (consult 2026-10-24, `inferred:`): one serialized writing process per file · owner named or gap admitted · timestamp merge is a reader-side view, stage 1 only · the record is never room truth or delivery authority · CLI-hook producers optional, own file, hook→bus parked.
- Package Q (first runnable observation slice) belongs to the termpanum line (Cartan, `termpanum-X0-source-contract` or successor). If its collector lands first it may be this bed's producer; coordinate through majkee with paths.

## Scope (owned paths are proposals until P1 confirms them)

| # | item | first clients | path proposal |
|---|---|---|---|
| 1 | **Address registry** — contract + first writer (ovitmugen on pane creation) + first reader (status reader or termbrana target pick, whichever is cheaper). Seat-addressed, never PID/pane. | ovitmugen · one reader | component folder (name P1); writer code in ovitmugen.py |
| 2 | **Config rule** — settings file + one resolver; `.gitignore` line for `<project>/.nablarva/`. | every slice script | component folder |
| 3 | **Shared observation record** — layout only: per-writer append-only files, one serialized writer each, segment-able, head/index readable in ≤80 lines, envelope-agnostic. **Not docket 8.** | producer · reader | `<project>/.nablarva/<record-dir>/<writer-id>.*` |
| 4 | **One producer** — tmux `set-hook` writing its own per-pane file, OR Package Q's collector. Installed by ovitmugen, never by hand into a living session. | record | hook def in component |
| 5 | **One view** — ovitmugen sessions column or a tiny reader: one derived state per seat (active/idle by last-event age) from the record, not tmux polling. | registry + record | ovitmugen.py or a reader (name after sweep) |
| 6 | **Skin note** — `raw/skin-requirements.majkee.md`, append-only, one line per felt gap, majkee's voice, no analysis. Head asks "one line for the skin note?" whenever majkee says the view is not enough. | later instarmux sitting brief | that file |
| 7 | **Houston `card: consult`** at closure (E7) and on any mid-bed seam crossing. | — | consult text landed verbatim in raw/ |

Work sequence P0–P6, stop rules and U-rows: `res/sequence-and-u-rows.md` (this bed).

## prompt-0 — cartan-x5 (head, cSharp)

```text
You are the fresh Codex Cartan X5 main head, assigned by majkee to build the spine slice. Your bed
is /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X5-spine-slice. Resolve
/home/hruzam/unikuklatrix/nablarva/AGENTS.md and its read order (flag.md L1–L23 — L3, L4, L14, L17,
L18, L20, L21, L22 bind this bed; pulse.md; docs/ARCHITECTURE.md r8 — if still r7, cite flag L21
over §2.5), then this RUNBOOK.md, STATUS.md and res/sequence-and-u-rows.md. Read the substrate
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X0-spine-and-skin/raw/runbook-substrate.nablarva-X5-spine-slice.oraculum.2026-10-24.md
and the operator's words in that bed's raw/answers.majkee.deck.2026-10-24.md and
raw/answers.majkee.organs.2026-10-24.md (prunable bed: pin them by commit once majkee has committed it).
Adopt the sole X5 STATUS pen and the cSharp posture; delegate every body of work.
P0 first: `date`; `git status` and ask majkee whose dirty paths are in the tree; confirm the
ovitmugen.py path and that ov-selftest / rb-selftest are green (one bounded researcher or your own
read-only check); confirm X1's state; write STATUS; FREEZE raw/yardstick.E1-E7.md verbatim from
this RUNBOOK before any build; then issue ONE bounded astrobley POINT for P1 (sweep + name + three
contracts). Ask majkee once at entry how many confirmations he wants for bookkeeping commits, and
present the component's candidate name(s) from the sweep as a costed deck for his GO.
Cross-head traffic (termpanum line, Package Q) goes through majkee with paths. No tunnel is
required or authorized by this launcher. Record every time from `date` in the same turn; record
a send, commit or relay only after it happened. Land every majkee message verbatim in
raw/answers.majkee.<topic>.<date>.md before acting on it. No stage/commit/push/deploy without his
word; canon-touching diffs shown first. No input of any kind into a living session. Do not edit
foreign beds, flag.md, PROJECT-DESIGN.md or AGENTS.md.
```

## prompt-1 — astrobley (implementer, under a POINT)

```text
Act as Codex astrobley under a bounded POINT from cartan-x5. Read
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X5-spine-slice/RUNBOOK.md,
res/sequence-and-u-rows.md and the exact POINT supplied. Own only the POINT's named paths under
the bed's raw/ and, when the POINT says so, the component folder and ovitmugen.py. The config
rule is law from the first line: no literal registry/record path in any script — resolve through
the settings file. One serialized writing process per record file. Never install a hook by hand
into a living session; the installer is ovitmugen. Never type into a pane. State practical
judgment and concrete alternatives; return consequential choices (naming, schema, serializer) to
the head as options, not as decisions. Do not own STATUS, lock architecture, commit, deploy or
touch delivery. You are not alone in the worktree; preserve other writers' edits. Return your
implementation report and the POINT's six-field bus RETURN.
```

## prompt-2 — verifier (fresh witness)

```text
Act as Codex verifier, independent of astrobley. Read the frozen yardstick
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X5-spine-slice/raw/yardstick.E1-E7.md
and the head's POINT. Verify E1–E6 from the bytes and from commands you run yourself; never from
the implementer's account and never from a transcript. For E5 audit tmux hooks and pipe-pane
state of the slice's panes and grep the slice's scripts for send-keys / paste-buffer /
load-buffer. Do not fix anything, do not write STATUS. Return VERDICT / TASK / RAN / EVIDENCE /
FAILURES / REPRODUCE / RESIDUAL RISK, plus the POINT's bus RETURN. On a re-pass you are resumed,
not replaced.
```

## prompt-3 — houston (card: consult)

```text
card: consult
Assigned by cartan-x5 under majkee's authorization, in
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X5-spine-slice. Load identity, binding
and the nablarva addendum per your deployed contract. Read this bed's RUNBOOK.md and the bounded
POINT. Question at P1: do the three contracts (registry · record · settings) stay inside the
observe plane — never room truth (L3 S1), never delivery authority (L17, L20), one serialized
writer per file, owner gap admitted (interim steward)? Question at closure (E7): did the built
slice implement a shared layer within L21 (2) and L18 without crossing into delivery? Return
fits · stretches · breaks · unclear with at most five constraints, text only. Write nothing.
```

## Known constraints + destructive holds

- Locks: L3 S1 (the room journal is stridulatrix's single-writer truth; the record is not it) · L4 (recorded deaths incl. send-keys injection, not reopened by qualification) · L14 D1 (PTY/tmux base; no vendor devices where avoidable) · L17 · L18 · L20 (observations authorize nothing) · L21 · L22 (`.hlm/` `.majkee/` never read).
- Stop rules (fixed): registry needs a hardcoded path → stop, design config first · no producer can write per-writer files without a serializer → narrow to one producer · the view needs tmux polling → stop, back to P3 · any step wants to type into a pane → STOP, STATUS hold, majkee.
- Shared worktree: other heads' uncommitted files present; never absorb, revert or stage them. Partial staging of a shared file → index blob via the implementer with exact preconditions.
- No commit/push/deploy without majkee's word. No `.nablarva/` folder outside the config-resolved home. The component's disk name needs majkee's GO (naming law, AGENTS.md).
- `locked: L<n>` never reaches past that lock's text. Name-locks are not ownership.

## Acceptance evidence (frozen as raw/yardstick.E1-E7.md at P0; the verifier reads only that)

- E1 `grep` over the slice's scripts finds no literal registry/record path; the resolved path (`<project>/.nablarva/…` or `~/.nablarva/…`) comes from the settings file (command + output).
- E2 `ov-up <slug>` → registry gains N seat entries; `ov-down` + `ov-up` → same seat ids, new pane ids (diff of two registry snapshots).
- E3 record directory: one file per writer; a mechanical check shows no two writers share a file (writer id in filename and in every line).
- E4 reader output shows a state per seat derived from the record; killing the producer changes the state without touching tmux state.
- E5 witness: tmux `pipe-pane`/hook audit shows zero `send-keys`/`paste-buffer`/`load-buffer` into any session pane for the slice's lifetime (L4, L17).
- E6 head/index of the record readable with `head -80`.
- E7 Houston closure consult: fits or stretches with constraints carried to flag/dock; no breaks.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — the locks above; L9′ (STATUS owns doing-state)
- `/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md` — r8 after X1 (planes, seam ledger, KEYS CODE §5, organs §7)
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X0-spine-and-skin/raw/` — substrate · decision-package r1/r2 · field r1 (v0 vs law) · inventory (bytes) · Houston consult · majkee's words — **prunable; pin by commit**
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-vist/raw/handoff.csharp-method.cartan.2026-10-24.md` — Codex-side cSharp method · `handoff.csharp-method.oraculum.2026-10-24.md` §2–§3, §6–§7 — subagents, carrier rules, costed deck, Houston by phase
- `/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md` · `status/GUIDE.md` · `bus/GUIDE.md` · `runbook/res/csharp-head-protocol.md`

## What this session deliberately does not do

- Delivery of any kind: HELLO, doorbell, stridulatrix, relay research (L14 D4/D7) — next bed `stridulatrix-X0-hello` (proposal).
- Envelope (docket 8) · router (`nablarva <tool>`) · dashboard · Zellij loader · muticula build (asleep until registry + notifier; worktrees interim, L12) · skin framework (instarmux sitting after the skin note) · phone organ · continuity mechanism.
- Naming the real steward (U-steward, majkee) · renaming stridularium or Boost · editing flag.md, PROJECT-DESIGN.md, AGENTS.md or any foreign bed.
- Aligning the `muticula-01-qualify` pulse row — majkee's, at this bed's closure ("when spine will be finished").

Wake recommendation: **@Cartan via the operator-opened table (Codex, cSharp)** — majkee's pick 13:10 CEST; multi-turn work with continuity, Codex-native implementer (astrobley) and verifier under it. Majkee opens the table and pastes prompt-0 after `architecture-X1-bookkeeping` closes. Reason recorded here per `/runbook` §3.
