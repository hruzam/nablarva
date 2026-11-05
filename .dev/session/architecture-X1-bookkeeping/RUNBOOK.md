# RUNBOOK: architecture-X1-bookkeeping

```yaml
goal: >-
  docs/ARCHITECTURE.md reaches r8 and the wrapper docs stop contradicting the flag: what L18–L21
  locked and what the architecture-X0 briefing decided (majkee, 2026-10-24) is written where the
  next beds will cite it, so nablarva-X5-spine-slice starts on canon, not on a prunable raw/ file.
gate: >-
  Majkee records GO on one reviewed diff — docs/ARCHITECTURE.md r8 (C1, M3, M4 payable pins, C4,
  §7 organ table, §9 stale lines, the X0 decisions as `said: majkee`), PROJECT-DESIGN.md §3.4
  removal + §3.8 one-cell touch, toolbox/termbrana/README.md C2 — every changed line mapped to one
  item of the edit list, Houston `card: consult` returning fits or stretches with no break — and
  commits it himself together with his one flag.md line retiring "stridularium" as a cultural name.
participant_1: {seat: cartan-x1, brand: codex, model: operator-selected at wake, effort: per runtime at wake, host: office, role: main working head using Medusa; sole STATUS pen; issues bounded POINTs; integrates; does not edit the three target docs or flag}
participant_2: {seat: implementer-x1, brand: codex, model: per native implementer definition at wake, effort: per native definition, host: office, role: surgical editor of the three docs and writer of its own RETURN; returns ambiguity to the head}
participant_3: {seat: houston-x1, brand: codex, model: per native houston definition at wake, effort: per native definition, host: office, role: card consult on the r8 diff; fits · stretches · breaks · unclear; writes nothing}
participant_4: {seat: majkee, brand: human, host: office, role: intent · decisions on the costed deck · the flag line · staging · the commit}
status_owner: cartan-x1
head_note: "Single-session working head, no cSharp arc; Medusa at execution wake. MANNED only while majkee drives; unclear presence means UNMANNED."
schema_note: runbook GUIDE verified 2026-09-17; status GUIDE gaveled 2026-08-27
observations_read:
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X1-X3-closure.oraculum.2026-10-24.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X3-architecture-sitting.oraculum.2026-10-23.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/harvest.2026-10-24.agol.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/architecture-X0-spine-and-skin.oraculum.2026-10-24.md
```

## Why this session exists

Three documents say things the flag no longer says. docs/ARCHITECTURE.md header still reads "DRAFT r7 — not promoted" though r7 was promoted at f20dda5; §2 item 5 and §9 still treat L17's edge as undecided though L21 adopted P5-b on 2026-10-23; the §7 organ table lists reposoma as an organ (it is an older RAG project) and leaves instarmux `unknown:` (it is the skin). The architecture-X0 briefing (majkee, 2026-10-24, deck X0-1…X0-7 all = a) produced four rulings that have no home yet: the termbrana/stridulatrix working split, the shared-substrate component with an interim steward, the substrate home + config rule, and the cultural retirement of the name "stridularium". nablarva-X5-spine-slice will cite all of this. One evening of pen work gives it a floor. Originally authored by oraculum(arch-X0) under `/runbook` on majkee's word ("X1+X5 authorized", 2026-10-24 13:10 CEST). Adapted for Codex by myShell on Majkee's explicit 2026-10-25 rewrite request; the gate and edit-list scope are unchanged. Preparation receipt: `raw/preparation.codex.2026-10-25.md`. Execution starts only when Majkee wakes the X1 head with prompt-0.

## Fixed facts

- Order is majkee's (deck X0-5 = a): this bed runs BEFORE nablarva-X5-spine-slice opens.
- L13 is a lock: this bed renames nothing. "Retired as a cultural name" is majkee's own flag.md line plus a doc note; the phone-app organ keeps its body under its old name with "new name pending".
- Every X0 ruling lands as `said: majkee (2026-10-24, architecture-X0 deck X0-n)` — never as `locked:`. A `locked: L<n>` tag never reaches past that lock's text (dominant defect class of X3: eleven instances).
- Source of the rulings: this bed's `raw/dragged.arch-x0/answers.majkee.deck.2026-10-24.md` and `answers.majkee.organs.2026-10-24.md`. X0 is already pruned; its originals are preserved at `nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/<file>`. Read the copies directly; use the original commit paths for durable citations, after `git cat-file -e` and byte comparison. The SHA-256 inventory is `raw/dragged.arch-x0/README.dragged.md`.
- The X2 source pins of M4 (termpanum.build-plan.md, disposition.x3-vectors…) wait until the X2 head commits those files — out of this bed.

## Edit list (the yardstick — every diff line maps to one row)

| id | file · place | edit | source |
|---|---|---|---|
| M3 | `docs/ARCHITECTURE.md` `:3` state line | "DRAFT r7 … not promoted" → "r8 bookkeeping candidate · promoted r7 at f20dda5 · <clock-read date> · awaiting majkee GO"; replace the pending qualifier only after his actual GO, then recheck that hunk | dock 2026-10-24 M3 |
| C1 | `docs/ARCHITECTURE.md` §2 item 5 (`:102–104`), §4.7, §9 lines on L17/P5 | replace "L17 holds unchanged until a GO names one" with the L21 wording by pointer ("see flag L21, adopted P5-b 2026-10-23"); three `said:` tags that now have locks behind them → `locked: L18/L19/L20` **only where the lock text says it** | dock C1; Houston consult 2026-10-24 "the flag wins" |
| M4 | `docs/ARCHITECTURE.md` §Sources and pins | add the pins payable at 519a211 after the head enumerates each exact path and verifies its blob; leave the X2 pins listed as "owed, X2 head"; no guessed pin | dock M4 |
| C4 | `docs/ARCHITECTURE.md` §8 | "root stub" → `docs/decisions/README.md` sits under docs/ | dock C4 |
| O1 | `docs/ARCHITECTURE.md` §7 organ table `:366` instarmux | `unknown:` → "the skin — UI only if zsh + tmux + the simplified way are not enough; Slint a candidate under it" `said: majkee X0 organs §7` | organs §2, §7; deck X0-6 |
| O2 | `docs/ARCHITECTURE.md` §7 `:367` reposoma row | remove the row; one-line note under the table: "reposoma is an older RAG project; `~/reposoma/` is the pre-RAG common store, not an organ" `said: majkee X0 organs §8` | organs §8 |
| O3 | `docs/ARCHITECTURE.md` §7 `:364` stridularium row + §9 `:463` | row note before the flag exists: "cultural retirement requested (said: majkee, 2026-10-24, X0 organs §5–6); body and lock L13 unchanged; new name pending"; after Majkee writes his line, cite that actual line and recheck the final hunk | organs §5, §6 |
| O4 | `docs/ARCHITECTURE.md` §7 after `:371–372` | Antensor: "implementation candidate → **translator** termpanum → body" · Nablarva Boost: add "working name; rename pending (Laravel Boost collision)" · VIST: "protocol name only" | organs §9 |
| S1 | `docs/ARCHITECTURE.md` §4 seam ledger, compose + deliver rows (or a new §4.x note) | the working split: termbrana composes + submits, ends at a packet file in the bus; stridulatrix sends (journal L3 S1, cursors, adapters S5, receipts, process/API boundary); termbrana never writes into a session; stridulatrix never composes; stridulatrix requests a pane, ovitmugen performs (L17) — `said: majkee (X0 deck X0-2)` | deck X0-2; organs §4, §5 |
| S2 | `docs/ARCHITECTURE.md` §4 observe row + §7 | the shared-substrate component: address registry + shared observation record; own thin folder per L18; disk name after sweep (X5 P1); steward interim = X5 head (U-steward); Houston's five constraints as `inferred: houston (consult 2026-10-24)` — `said: majkee (X0 deck X0-3)` | deck X0-3; consult |
| S3 | `docs/ARCHITECTURE.md` §3 principles or §4 substrate row | substrate home `<project>/.nablarva/` + `~/.nablarva/`; config rule "no path in a script; resolved from nabLarva settings" — `said: majkee (X0 organs §1; deck X0-4)` | deck X0-4 |
| P1 | `PROJECT-DESIGN.md` §3.4 (`:237`) | remove the reposoma section; leave a one-line tombstone pointing to ARCHITECTURE §7 note | organs §8 |
| P2 | `PROJECT-DESIGN.md` §3.8 (`:282`) heading | one-cell touch: "stridularium *(phone app — cultural retirement requested by majkee 2026-10-24; new name pending)*"; finalize the retirement wording together with O3 after Majkee writes his flag line | organs §5 |
| C2 | `toolbox/termbrana/README.md` §"Layering B — L17", §Composition | replace the superseded L17 phrase ("narrow integration edge … not a framework") with a pointer to flag L21 | dock C2 |

Not in this list: J1b (PROJECT-DESIGN §2.2/§3.6/§3.8 pre-architecture prose — a wrapper sitting, majkee's) · N6/N8 (dock 2026-10-23) · any rename · any lock text.

## Codex team and communication

`cartan-x1` is the main thread; `implementer-x1` uses the existing native agent type
`implementer`; `houston-x1` uses `houston` with explicit `card: consult`. Seat labels distinguish
this session's assignments; they are not new global agents, CLI profiles or persona files.
Check availability and the effective model/effort at wake; record observations in STATUS or
assignment evidence, not here. A custom role never enlarges inherited sandbox permissions.

The head dispatches the editor and then Houston, sequentially. No child dispatches another.
The head owns integration and STATUS; the editor owns only the three target files plus its own
numbered RETURN. Houston returns text, which the head lands verbatim. The myShell preparation
team is advisory support, not the X1 execution team or a second STATUS owner.

Use native collaboration for an available authorized child. Record its observed handle with
its session/role in the POINT or STATUS; reuse only a matching binding. If it is unavailable,
recover from the POINT, RETURN, actual diff and VERDICT before starting a replacement. Names
and historical handles do not prove a surviving instance. Independent CLI heads communicate
through Majkee's relay or a separately authorized route. File presence proves no delivery,
acceptance or completion. No transport or watcher is introduced by this RUNBOOK.

Use the existing bus GUIDE: `_bus/NN.cartan-x1.point.md`,
`_bus/NN.implementer-x1.return.md`, `_bus/NN.cartan-x1.verdict.md`.
The head verifies claims against bytes and writes the VERDICT; only it advances STATUS.
A new correction after handoff is a new numbered cycle. Native role output requirements remain
in force; the implementer's assumptions and remaining gate fit inside the six RETURN headings.

## prompt-0 — cartan-x1 (main working head)

```text
You are Cartan, main working head cartan-x1, executing this fixed RUNBOOK under the Medusa
skill. Majkee is waking you for /home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping.
Read /home/hruzam/unikuklatrix/nablarva/AGENTS.md and its full required read order, then
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/RUNBOOK.md and
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/STATUS.md.
Read /home/hruzam/reposoma/raw.guides/status/GUIDE.md and
/home/hruzam/reposoma/raw.guides/bus/GUIDE.md before their first writes. Work from the Nablarva
root so Houston's project addendum resolves from the actual cwd. Confirm effective tools,
permissions and native implementer/houston roles; never manufacture missing capabilities.
Adopt the declared STATUS pen. Read the clock for timestamps. MANNED means Majkee is actually
driving; absent or unclear presence means UNMANNED. No inference of GO from silence.

First assignment: inspect current git status, staged and unstaged target diffs, then verify
all Edit-list anchors against current bytes. Read the founding sources in
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/raw/dragged.arch-x0/.
Write /home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/raw/anchors.<date>.md:
one row per id, current file/line/quoted text, proposed replacement, source passage and pin.
For M4 enumerate every payable path at 519a211 and check git cat-file -e for each; keep X2's
owed pins separate. For M3/O3/P2 use the pending wording until the actual human acts occur.
Save target before-hashes and your expected-change list before receiving the editor's diff.
A missing or ambiguous anchor/source, changed gate, or foreign target hunk holds its dependent
edit: record it in STATUS and return the exact question to Majkee; do not guess.

Next, issue one bounded POINT for the whole verified list to native implementer (prompt-1).
Name exactly the three target files and its own RETURN path. Include before-hashes, exact
anchors/replacements, stop rules and the id-to-hunk report. You are not alone in the worktree:
never absorb or revert foreign edits. No staging by agents. Set STATUS in_flight before dispatch.
Read the RETURN, inspect actual bytes and run the bounded checks yourself. Generate
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/raw/diff.r8.<date>.patch
using git -C /home/hruzam/unikuklatrix/nablarva diff -- docs/ARCHITECTURE.md PROJECT-DESIGN.md
toolbox/termbrana/README.md. Check against your held-back list and sweep every changed locked:
tag against the exact lock text. Write the bus VERDICT with evidence and disposition.

Only after that self-check, spawn native houston with prompt-2. Preserve its complete returned
text, including entry proof, in a new
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/raw/consult.r8.houston.<date>.md.
Check that the actual cwd/addendum matches Nablarva. A missing entry proof is an unresolved
route check, not evidence of a successful consult. fits permits progression; stretches requires
each constraint to be satisfied and recorded; breaks/unclear holds the affected path. If the
consult needs evidence or a correction, give a new bounded assignment; never self-clear it.

Present the reviewed diff to Majkee as a costed deck of at most three blocks (accept / change a
cell / drop). Land each actual reply verbatim in its own new raw/answers.majkee.x1.<date>.<n>.md
under the X1 bed, with your interpretation separately labelled inferred: cartan-x1. On GO,
propose the flag line in chat; Majkee writes it. Route the authorized M3/O3/P2 final wording
through the editor, recheck the complete diff, and obtain a fresh Houston check if meaning or
constraints changed. Record which exact patch was reviewed and which final diff Majkee accepts.
Hand Majkee the explicit file list for his staging and commit. Verify that his commit contains
the accepted doc bytes and flag line together, and record the SHA in STATUS only after observing
it. No agent stages, commits, pushes or deploys. You never edit the three docs or flag yourself.
Do not alter pulse except for this row's closure on Majkee's word. Do not rename anything.
The preparation rewrite did not start execution or satisfy this gate. Done only when the
unchanged gate is proved; keep STATUS at the verified edge, never ahead of the act.
```

## prompt-1 — implementer-x1 (native implementer)

```text
You are native implementer, session seat implementer-x1, under cartan-x1. Read
/home/hruzam/unikuklatrix/nablarva/AGENTS.md and its required read order, then
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/RUNBOOK.md and the
exact absolute POINT path supplied by the head under that bed's _bus/. The head supplies a
concrete cycle NN and return_to path; unresolved placeholders are not executable authority.

You are not alone in the codebase. Preserve other participants' work; never revert their
edits. File ownership: /home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md,
/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md,
/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/README.md, plus your own exact
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/_bus/NN.implementer-x1.return.md
named in POINT return_to. No other writes. No STATUS, flag, pulse, staging, commit, push,
deploy, subdelegation or transport. Confirm effective write permission before the cut; a
role definition cannot override the parent's sandbox. Return any denial to the head.

Check all target before-hashes and anchors before any edit. STOP on a mismatch, ambiguous
replacement, or need for a line outside the edit list. Revise from disk, never memory. Make
only the assigned changes: no reflow or neighbouring improvements. Every changed line,
including formatting, maps to an edit-list id. Report assumptions, changed files, checks and
remaining gate using the bus GUIDE's six mandatory RETURN headings: 1. Files changed;
2. Commands and outcomes; 3. Evidence paths; 4. Mismatches discovered;
5. Recommended next task; 6. Remaining uncertainty. Include the id-to-hunk map and full scoped
output of git -C /home/hruzam/unikuklatrix/nablarva diff -- docs/ARCHITECTURE.md
PROJECT-DESIGN.md toolbox/termbrana/README.md, its scoped --stat, and expected versus observed
checks. Return your RETURN path to cartan-x1. The head verifies and integrates.
```

## prompt-2 — houston-x1 (native houston, card: consult)

```text
card: consult
Assigned by cartan-x1, the authorized X1 main head, under Majkee's execution wake.
Working repository: /home/hruzam/unikuklatrix/nablarva. Session:
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping.
Follow your deployed loader in order: identity, Codex binding, nearest project addendum,
consult card. Verify effective cwd resolves the Nablarva addendum; return a mismatch instead
of guessing the project. Preserve your Route/canary first line, all actual file stamps and cwd
in your return. No wrapper or stamp is supplied by this prompt as a substitute for reading.

Read /home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/RUNBOOK.md,
/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md L13, L16–L23, and the exact absolute
raw/diff.r8.<date>.patch path supplied by the head in this bed. Read current touched document
sections and the relevant raw/dragged.arch-x0/ sources there. Does the diff cite each lock only
within its text, record X0 rulings as said: majkee rather than locks, preserve L13, and remove
the L21-superseded assertions within the assigned edit list? Check pending-versus-completed GO
and flag wording against actual evidence. Return fits · stretches · breaks · unclear with at
most five constraints and source-grounded findings, as text only. No writes, no helper, no
STATUS, no canon edit. The head records your complete reply verbatim; you do not land a file.
```

## Known constraints + destructive holds

- flag.md: only majkee writes it (the stridularium line is his). pulse.md: router row removed by the head only at closure, on his word.
- Shared worktree: other heads' uncommitted files are present. Agents inspect and preserve them; no index manipulation, staging or unstaging. If target files contain foreign changes, hold the affected edit and obtain an ownership resolution. Majkee alone selects and stages the accepted doc/flag diff.
- No staging, commit, push or deploy by agents. Canon diff is shown to Majkee before his commit, always. A prior GO does not approve later substantive changes.
- No `.hlm/`, `.majkee/` reads (L22). No tmux input into any living session.
- Generate patches with `git diff`; do not hand-write unified diffs. The predecessor observed stripped blank-context whitespace on a Claude route; that observation is not asserted as Codex tool behaviour.
- Over-wide lock citation is the known failure: the head's self-sweep of the diff for `locked:` is mandatory before Houston sees it.

## Acceptance evidence

- A1 `rg -n "not promoted" docs/ARCHITECTURE.md` → no hit; the state line names r8 and f20dda5. It says awaiting GO until approval is actually recorded; final wording matches the observed human act.
- A2 `rg -n "L17 holds unchanged" docs/ARCHITECTURE.md` → no hit; §2 item 5 points at L21. C1/C2/C4 and each payable M4 pin match the verified anchor/source map.
- A3 §7 contains no reposoma organ row and carries the one-line explanatory note; PROJECT-DESIGN §3.4 is a tombstone. Source paths containing reposoma are not defects.
- A4 O1–O4/S1–S3 and P1/P2 match their named X0 source passages; the new X0 claims carry `said: majkee`, Houston constraints remain `inferred: houston`, and no `locked:` citation exceeds its text. No invented flag number or organ rename.
- A5 `git diff` id→hunk map complete: no hunk without an id, no id without a hunk or a verified already-satisfied finding. A moved/missing anchor is not completion: resolve it and re-POINT before acceptance. Editor RETURN and head VERDICT name the same exact diff.
- A6 Houston's complete consult return is landed with entry proof: fits or stretches, no break or unclear; every stretches constraint is discharged with evidence. Any changed semantic diff is checked again before final acceptance.
- A7 Majkee's actual answers are landed verbatim; `git show --name-only <sha>` and the committed blobs prove that his single commit contains the accepted three-document diff and his flag line together. Compare committed bytes with the accepted patch/snapshot; file names or a SHA alone are insufficient. Only then record that SHA and gate completion in STATUS.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — L13 (stridularium lock), L17–L21 (the locks r8 cites)
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/dock.md` §2026-10-24 — the carried items C1/M3/M4/C4/C2/J1b (uncanonical scratch: the item list, not truth)
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/raw/dragged.arch-x0/` — `answers.majkee.deck.2026-10-24.md`, `answers.majkee.organs.2026-10-24.md`, `consult.d1-observation-record.houston.2026-10-24.md` and `decision-package.r2.oraculum.2026-10-24.md`; original paths pinned at 1ceceee, hash inventory in README.dragged.md.
- `/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md` · `/home/hruzam/reposoma/raw.guides/status/GUIDE.md` · `/home/hruzam/reposoma/raw.guides/bus/GUIDE.md`

## What this session deliberately does not do

- Rename stridularium or Nablarva Boost; touch any lock text; decide docket 8 or N6/N8.
- J1b (PROJECT-DESIGN §2.2/§3.6/§3.8 pre-architecture prose) — a wrapper sitting, majkee's.
- Pay the X2 source pins (M4 second half) — waits for the X2 head's commits.
- Any edit to ovitmugen, termbrana code, or any organ body file.

Wake recommendation: **Cartan as the Codex main working head, using Medusa**, with native `implementer` for the bounded doc edit and native `houston` for the required consult. Majkee retains approval, flag, staging and commit. This is a single fixed-gate execution task; no cSharp arc, Oraculum strategy cycle or new agent definition is required.

## Pin (added at arch-X0 prune, 2026-10-24 15:30 CEST)

The architecture-X0-spine-and-skin bed is preserved in git at **1ceceee** (`git show 1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/<file>`). Byte-identical copies of its basic stones are in this bed at `raw/dragged.arch-x0/` (sha256 table in `README.dragged.md` there) — point at those directly; cite the pin for provenance.
