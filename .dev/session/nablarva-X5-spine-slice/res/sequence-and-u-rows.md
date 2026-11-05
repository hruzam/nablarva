# nablarva-X5-spine-slice · res/ — work sequence, stop rules, U-rows

`extending chapter of RUNBOOK.md (runbook GUIDE "Working bound": over ~150 lines → a res/ chapter) · fixed like the RUNBOOK; discovered-mid-bed facts go to STATUS, not here · authored by oraculum(arch-X0) under /runbook, 2026-10-24`

## Work sequence (a shape, not a law — fit it to the team you get; one body author at a time)

| phase | assignment | evidence / output |
|---|---|---|
| P0 | Head enters fresh (prompt-0). Verifies HEAD, dirty paths + owners, ovitmugen.py path, selftests green, X1 state. Adopts STATUS. **Freezes `raw/yardstick.E1-E7.md`** verbatim from the RUNBOOK before any build. Asks majkee the confirmation count for bookkeeping commits. | STATUS first write · yardstick · one bounded POINT |
| P1 | **Sweep + name + contracts** (astrobley): duplicate/cross-interference sweep for the component's disk name (repo, `~/ia-sync`, live zsh configs, KEYS CODE §5); candidates → head → **costed deck → majkee GO on the name**. Contract files: registry schema (seat id · pane id · bed · host · ts), record layout (per-writer naming, line shape, segment rule, head/index), settings file shape + resolver. No code yet. Houston consult (prompt-3, P1 question) if any contract touches a seam you did not expect. | `raw/sweep.<date>.md` · `raw/contract.registry.md` · `raw/contract.record.md` · `raw/contract.settings.md` · `raw/answers.majkee.name.<date>.md` |
| P2 | **Registry writer + reader** (astrobley): ovitmugen writes on pane creation via the resolver; reader shows the registry. Local E1, E2 (not yet the witness). Diff shown to majkee before any commit. | code diff · local E1/E2 output |
| P3 | **Record layout + producer** (astrobley): per-writer files; one hook, own file per pane, installed by ovitmugen; serialization proven (E3). Coordinate with Package Q through majkee if it exists. Researcher, bounded, if O_APPEND atomicity or hook semantics are in doubt. | code diff · E3 output · researcher text landed |
| P4 | **View** (astrobley): derived state per seat from the record. Local E4. **Majkee uses it**; the head asks "one line for the skin note?" at each felt gap. | code diff · E4 output · `raw/skin-requirements.majkee.md` |
| P5 | **Witness** (verifier, fresh, yardstick only): E1–E6 from the bytes. The head writes its own expected list **before** reading the VERDICT, then compares. Houston `card: consult` → E7. Defects → P2–P4 reiterate; the same verifier is resumed. | VERDICT · Houston text landed verbatim · head's held-back list |
| P6 | **Majkee GO/STOP** on the gate (costed deck if anything is mixed). Closure: observations promote before prune · agol once · skin note → handoff for `instarmux-X0-sitting-brief` · U-steward re-asked · `muticula-01-qualify` pulse row alignment handed to majkee · successor handoff for `stridulatrix-X0-hello`. | closure manifest · promoted observations · harvest · handoffs |

## Stop rules (fixed; r1 §3 lens 11, carried)

- Registry cannot be written by ovitmugen without a hardcoded path → **stop, design config first**, re-POINT.
- No producer can write per-writer files without a serializer → Houston c1 bites: **narrow to one producer**, record the limit in STATUS holds.
- The derived state in the view needs tmux polling rather than the record → the record is not yet useful: **stop**, back to P3.
- Any step wants to type into a pane to "make it work" → that is delivery (L4/L17): **STOP, STATUS hold, majkee**. U-send-keys is his decision, on evidence, in the stridulatrix bed.
- A `[usage]`/ctx line goes dark on any relay → log `ctx: unmeasured` in STATUS before the next large ask (Agol U9).

## U-rows (name them in STATUS; do not resolve them in this bed)

| row | item | owner / when |
|---|---|---|
| U-send-keys | is a contentless nudge over the PTY "injection" in L4's sense | majkee, on this bed's evidence — surfaced at closure, decided in stridulatrix-X0 |
| U-steward | real owner of the shared-substrate component (interim: cartan-x5) | majkee; re-asked at closure |
| U-continuity | journaling, rotation of long canon files, planning across sessions; carried requirement: records segment-able, ≤80-line head | majkee, no fixation yet |
| U-vendor-spawn | Claude Code / Codex / Gemini CLI spawn & message internals | bounded @Epoch pass, only when a stridulatrix design needs it |
| docket 8 | envelope — four candidates (ARCHITECTURE §4.5); working default: bounded comparison first | termpanum line |
| U-PackageQ | whether the producer is the hook or Q's collector | P1/P3 with the termpanum line via majkee |
| Agol U8 | clock from `date` in the same turn; record a relay/commit/send only after it happened | head, every turn |
| Agol U9 | dark measurement logged `unmeasured`; counts re-derived from files | head |
| Agol U10 | operator decisions ship as a costed deck, never blank fields | head |
| Agol U11 | head writes its own expected list before reading a drafter's/witness's output; every `@<sha>:<path>` cite checked with `git cat-file -e` before commit | head |
| Agol U5 | if any drafter runs on a long-lived child: name the fresh-child trigger and handoff set at authoring | head, only if applicable |

## Costed deck — the shape majkee decides on (said: majkee 2026-10-24; proven twice)

```
GAVEL <source-qualified id> · <the question, one sentence?>
  options:  a) … b) … c) …      context: <enough to decide without opening a file>
  buys: … cost: … can be lost: … consequence: …
  lean: <seat> → <option> — <one reason>     source: <path[:line]>     answer: ___
```
One block at a time in chat; the whole deck also in a file; his answer lands verbatim in `raw/answers.majkee.<topic>.<date>.md` **before** anything acts on it; "own"/mixed answers → placement table, then the few questions only he can answer.
