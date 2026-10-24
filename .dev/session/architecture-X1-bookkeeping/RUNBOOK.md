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
participant_1: {seat: flight-x1, brand: claude, model: per roster at wake, effort: high, host: office, role: head in project-session mode, MANNED by majkee; sole STATUS pen; issues bounded POINTs; integrates; never edits canon itself}
participant_2: {seat: delta, brand: claude, model: per roster at wake, effort: medium, host: office, role: surgical editor of the three docs from the edit list; reports git diff; no judgment, no extra edits}
participant_3: {seat: houston, brand: either, model: per binding, effort: high, host: office, role: card consult on the r8 diff — fits · stretches · breaks against L17–L21; writes nothing}
participant_4: {seat: majkee, brand: human, host: office, role: intent · one-line decisions on the costed deck · the flag line · the commit}
status_owner: flight-x1
head_note: "none — single-session bed, no arc; Flight MANNED posture (operator drives)"
schema_note: runbook GUIDE verified 2026-09-17; status GUIDE gaveled 2026-08-27
observations_read:
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X1-X3-closure.oraculum.2026-10-24.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva-X3-architecture-sitting.oraculum.2026-10-23.md
  - /home/hruzam/unikuklatrix/nablarva/.dev/observations/harvest.2026-10-24.agol.md
  - (architecture-X0-spine-and-skin's observation file, once promoted — run `ls /home/hruzam/unikuklatrix/nablarva/.dev/observations/architecture*` at entry)
```

## Why this session exists

Three documents say things the flag no longer says. docs/ARCHITECTURE.md header still reads "DRAFT r7 — not promoted" though r7 was promoted at f20dda5; §2 item 5 and §9 still treat L17's edge as undecided though L21 adopted P5-b on 2026-10-23; the §7 organ table lists reposoma as an organ (it is an older RAG project) and leaves instarmux `unknown:` (it is the skin). The architecture-X0 briefing (majkee, 2026-10-24, deck X0-1…X0-7 all = a) produced four rulings that have no home yet: the termbrana/stridulatrix working split, the shared-substrate component with an interim steward, the substrate home + config rule, and the cultural retirement of the name "stridularium". nablarva-X5-spine-slice will cite all of this. One evening of pen work gives it a floor. Authored by oraculum(arch-X0) under `/runbook` on majkee's word ("X1+X5 authorized", 13:10 CEST).

## Fixed facts

- Order is majkee's (deck X0-5 = a): this bed runs BEFORE nablarva-X5-spine-slice opens.
- L13 is a lock: this bed renames nothing. "Retired as a cultural name" is majkee's own flag.md line plus a doc note; the phone-app organ keeps its body under its old name with "new name pending".
- Every X0 ruling lands as `said: majkee (2026-10-24, architecture-X0 deck X0-n)` — never as `locked:`. A `locked: L<n>` tag never reaches past that lock's text (dominant defect class of X3: eleven instances).
- Source of the rulings: `/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md` and `raw/answers.majkee.organs.2026-10-24.md` — majkee's words verbatim. The bed is prunable: after majkee's commit of that bed, cite them with a git pin (`@<sha>:<path>`, checked with `git cat-file -e`).
- The X2 source pins of M4 (termpanum.build-plan.md, disposition.x3-vectors…) wait until the X2 head commits those files — out of this bed.

## Edit list (the yardstick — every diff line maps to one row)

| id | file · place | edit | source |
|---|---|---|---|
| M3 | `docs/ARCHITECTURE.md` `:3` state line | "DRAFT r7 … not promoted" → "r8 · promoted r7 at f20dda5 · r8 bookkeeping <date>, majkee GO" | dock 2026-10-24 M3 |
| C1 | `docs/ARCHITECTURE.md` §2 item 5 (`:102–104`), §4.7, §9 lines on L17/P5 | replace "L17 holds unchanged until a GO names one" with the L21 wording by pointer ("see flag L21, adopted P5-b 2026-10-23"); three `said:` tags that now have locks behind them → `locked: L18/L19/L20` **only where the lock text says it** | dock C1; Houston consult 2026-10-24 "the flag wins" |
| M4 | `docs/ARCHITECTURE.md` §Sources and pins | add the pins payable at 519a211; leave the X2 pins listed as "owed, X2 head" | dock M4 |
| C4 | `docs/ARCHITECTURE.md` §8 | "root stub" → `docs/decisions/README.md` sits under docs/ | dock C4 |
| O1 | `docs/ARCHITECTURE.md` §7 organ table `:366` instarmux | `unknown:` → "the skin — UI only if zsh + tmux + the simplified way are not enough; Slint a candidate under it" `said: majkee X0 organs §7` | organs §2, §7; deck X0-6 |
| O2 | `docs/ARCHITECTURE.md` §7 `:367` reposoma row | remove the row; one-line note under the table: "reposoma is an older RAG project; `~/reposoma/` is the pre-RAG common store, not an organ" `said: majkee X0 organs §8` | organs §8 |
| O3 | `docs/ARCHITECTURE.md` §7 `:364` stridularium row + §9 `:463` | row note: "name retired as a cultural name (majkee 2026-10-24, flag line <n>); body and lock L13 unchanged; new name pending" | organs §5, §6 |
| O4 | `docs/ARCHITECTURE.md` §7 after `:371–372` | Antensor: "implementation candidate → **translator** termpanum → body" · Nablarva Boost: add "working name; rename pending (Laravel Boost collision)" · VIST: "protocol name only" | organs §9 |
| S1 | `docs/ARCHITECTURE.md` §4 seam ledger, compose + deliver rows (or a new §4.x note) | the working split: termbrana composes + submits, ends at a packet file in the bus; stridulatrix sends (journal L3 S1, cursors, adapters S5, receipts, process/API boundary); termbrana never writes into a session; stridulatrix never composes; stridulatrix requests a pane, ovitmugen performs (L17) — `said: majkee (X0 deck X0-2)` | deck X0-2; organs §4, §5 |
| S2 | `docs/ARCHITECTURE.md` §4 observe row + §7 | the shared-substrate component: address registry + shared observation record; own thin folder per L18; disk name after sweep (X5 P1); steward interim = X5 head (U-steward); Houston's five constraints as `inferred: houston (consult 2026-10-24)` — `said: majkee (X0 deck X0-3)` | deck X0-3; consult |
| S3 | `docs/ARCHITECTURE.md` §3 principles or §4 substrate row | substrate home `<project>/.nablarva/` + `~/.nablarva/`; config rule "no path in a script; resolved from nabLarva settings" — `said: majkee (X0 organs §1; deck X0-4)` | deck X0-4 |
| P1 | `PROJECT-DESIGN.md` §3.4 (`:237`) | remove the reposoma section; leave a one-line tombstone pointing to ARCHITECTURE §7 note | organs §8 |
| P2 | `PROJECT-DESIGN.md` §3.8 (`:282`) heading | one-cell touch: "stridularium *(phone app — cultural name retired 2026-10-24; new name pending)*" | organs §5 |
| C2 | `toolbox/termbrana/README.md` §"Layering B — L17", §Composition | replace the superseded L17 phrase ("narrow integration edge … not a framework") with a pointer to flag L21 | dock C2 |

Not in this list: J1b (PROJECT-DESIGN §2.2/§3.6/§3.8 pre-architecture prose — a wrapper sitting, majkee's) · N6/N8 (dock 2026-10-23) · any rename · any lock text.

## prompt-0 — flight-x1 (head, MANNED)

```text
You are Flight in project-session mode, MANNED by majkee, head of
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping. Read
/home/hruzam/unikuklatrix/nablarva/AGENTS.md and its read order (flag.md L13, L16–L23; pulse.md),
then this RUNBOOK and STATUS.md. Run `date` before every time you record. Run `git status` and
ask majkee whose dirty paths are in the tree before anything is staged; never absorb, revert or
stage foreign edits (Cartan's X2/termpanum-X0/X4 raw; the arch-X0 bed). Adopt the STATUS pen.
Your work: (1) verify each Edit-list anchor against the current bytes (line numbers are from
2026-10-24 and may have moved) and write the verified anchor list to raw/anchors.<date>.md;
(2) issue ONE bounded POINT to delta covering the whole list with exact anchors, STOP rules
(stop on any anchor not found; stop on any line outside the list) and the report format
`git diff -- docs/ARCHITECTURE.md PROJECT-DESIGN.md toolbox/termbrana/README.md`;
(3) read the diff yourself FIRST against your own expected list, then spawn houston `card: consult`
with prompt-2; land its text verbatim in raw/consult.r8.houston.<date>.md; (4) present the diff
to majkee in chat as a costed deck of at most three blocks (accept / change a cell / drop),
land his answers verbatim in raw/answers.majkee.x1.<date>.md; (5) on his GO write the flag line
PROPOSAL text for him in chat (you never edit flag.md), then hand him the commit: he commits.
You do not edit docs yourself, do not commit, do not touch pulse.md except on his word, do not
rename anything. Done when the gate line is true and STATUS says so.
```

## prompt-1 — delta (editor, under the head's POINT)

```text
You are Delta. Execute exactly the POINT at
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping/_bus/<point file>
from flight-x1. Files you may edit: /home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md,
/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md,
/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/README.md — nothing else. Preconditions:
the anchors in the POINT exist byte-for-byte; if one does not, STOP and report which. Make only
the edits listed; every changed line must map to an edit-list id, which you cite in your report.
Do not reflow, re-wrap or "improve" neighbouring text. Do not stage or commit. Report:
`git diff --stat` + the full `git diff` of the three files + the id→hunk map.
```

## prompt-2 — houston (card: consult)

```text
card: consult
Assigned by flight-x1 under majkee's authorization, in
/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X1-bookkeeping. Load your identity,
binding and the nablarva addendum per your deployed contract. Read this bed's RUNBOOK.md, the
diff at raw/diff.r8.<date>.patch and flag.md L13, L17–L21. Question: does the r8 diff cite each
lock only within that lock's text, record the X0 rulings as `said: majkee` and not as locks,
leave L13 untouched, and remove every statement L21 superseded? Return fits · stretches · breaks
· unclear with at most five constraints, as text only. Write nothing. No STATUS, no canon edit.
```

## Known constraints + destructive holds

- flag.md: only majkee writes it (the stridularium line is his). pulse.md: router row removed by the head only at closure, on his word.
- Shared worktree: other heads' uncommitted files are present. Stage only this bed's three doc edits; if a shared file must be staged partially, build the index blob via delta (`git hash-object -w` + `git update-index --cacheinfo`).
- No commit, push or deploy by any seat but majkee. Canon diff is shown to him before the commit, always.
- No `.hlm/`, `.majkee/` reads (L22). No tmux input into any living session.
- Write tool strips trailing whitespace: never hand-write a patch; the diff comes from `git diff`.
- Over-wide lock citation is the known failure: the head's self-sweep of the diff for `locked:` is mandatory before Houston sees it.

## Acceptance evidence

- A1 `grep -n "not promoted" docs/ARCHITECTURE.md` → no hit; `:3` names r8 and f20dda5.
- A2 `grep -n "L17 holds unchanged" docs/ARCHITECTURE.md` → no hit; §2 item 5 points at L21.
- A3 `grep -n "reposoma" docs/ARCHITECTURE.md` → only the one-line note; PROJECT-DESIGN §3.4 is a tombstone.
- A4 §7 rows for instarmux, stridularium, Antensor, Boost read as in the edit list; every X0 ruling tagged `said: majkee`.
- A5 `git diff` id→hunk map complete: no hunk without an id, no id without a hunk (or a recorded "anchor moved, re-POINTed").
- A6 Houston consult text landed: fits or stretches, no break.
- A7 majkee's answers landed verbatim; his commit sha recorded in STATUS checkpoint; his flag line present in flag.md.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — L13 (stridularium lock), L17–L21 (the locks r8 cites)
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/dock.md` §2026-10-24 — the carried items C1/M3/M4/C4/C2/J1b (uncanonical scratch: the item list, not truth)
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md` · `raw/answers.majkee.organs.2026-10-24.md` · `raw/consult.d1-observation-record.houston.2026-10-24.md` — majkee's words and Houston's constraints (pin after commit)
- `/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md` · `/home/hruzam/reposoma/raw.guides/status/GUIDE.md` · `/home/hruzam/reposoma/raw.guides/bus/GUIDE.md`

## What this session deliberately does not do

- Rename stridularium or Nablarva Boost; touch any lock text; decide docket 8 or N6/N8.
- J1b (PROJECT-DESIGN §2.2/§3.6/§3.8 pre-architecture prose) — a wrapper sitting, majkee's.
- Pay the X2 source pins (M4 second half) — waits for the X2 head's commits.
- Any edit to ovitmugen, termbrana code, or any organ body file.

Wake recommendation: **@Flight (project-session mode, MANNED)** — multi-line bookkeeping inside one gate with one cheap kraken (Delta) under it; the operator's hands are needed for the flag line and the commit, so Flight runs manned. Reason recorded here per `/runbook` §3.

## Pin (added at arch-X0 prune, 2026-10-24 15:30 CEST)

The architecture-X0-spine-and-skin bed is preserved in git at **1ceceee** (`git show 1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/<file>`). Byte-identical copies of its basic stones are in this bed at `raw/dragged.arch-x0/` (sha256 table in `README.dragged.md` there) — point at those directly; cite the pin for provenance.
