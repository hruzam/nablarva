to-X5-cSharp (the fresh head that will author `nablarva-X5-spine-slice/RUNBOOK.md`) from-oraculum(arch-X0)

`2026-10-24 · office · SUBSTRATE for a RUNBOOK, not the RUNBOOK and not rules (rules: flag.md · the RUNBOOK you author · your STATUS) · written on majkee's nod ("Nod first", 11:45 CEST) after the seven-block deck closed all = a · every decision below is sourced to raw/answers.majkee.deck.2026-10-24.md (his words) or raw/decision-package.r2 (my carry) · you author the RUNBOOK in the bed per runbook GUIDE "Authored where it lives"; copy ast/RUNBOOK.template.txt, fill it from this file, point at canon, never reproduce it · this bed (arch-X0) is prunable: pin anything you cite from it`

## 0. Prerequisite and position

- **Bed slug:** `nablarva-X5-spine-slice` (said: majkee 11:43 CEST). Cross-organ → `nablarva-X` line. X = nabLarva generation marker (said: majkee, X0-7 voice).
- **Prerequisite bed:** `architecture-X1-bookkeeping` — ARCHITECTURE r8 writes the split (X0-2), the shared-substrate component + interim steward (X0-3), the home + config rule (X0-4). Order said: majkee (X0-5 = a, "docs bed now, before the spine bed"). If X1 has not closed when X5 opens, cite `raw/decision-package.r2` **with a git pin** and carry an X1 dependency row in STATUS; do not wait silently.
- **What X5 is:** the first **construction** of the body ("from the elementals, not the jump" — said: majkee, X0-1). Not a planning bed: its gate is a witnessed running slice. Implementing a shared layer needs its own release (locked: L21 (2)) — **this bed's GO is that release.**
- **What X5 is not:** delivery of any kind. No byte enters any session (locked: L4, L17). HELLO is the next bed (`stridulatrix-X0-hello`, proposal), not this one.

## 1. Front-matter draft (fill, do not copy blindly)

```yaml
goal: The body has a running spine — observe → record → view — built on the two shared layers majkee named (address registry · shared observation record) under the config rule, with one client each proving the sharing, and no write into any session.
gate: Majkee records GO or STOP on a witnessed read-only spine slice — one producer writes the shared observation record in per-writer files at a config-resolved home, the address registry holds one seat-addressed entry per pane written by ovitmugen on `ov-up` and surviving `ov-down`/`ov-up`, a second client reads both to show one derived state per seat, and an independent witness confirms that no byte was written into any session.
participant_1: {seat: x5-head, brand: <majkee picks>, role: cSharp — authors this RUNBOOK, navigator, sole STATUS pen, integrates; delegates every body of work}
participant_2: {seat: trajectory, brand: claude, role: implementer for code that exists (ovitmugen.py registry writer; reader; producer hook) — flags better approaches, spawns delta}
participant_3: {seat: delta, brand: claude, role: surgical byte edits with preconditions + STOP rules (settings file, .gitignore line, contract files)}
participant_4: {seat: assay, brand: claude, role: fresh-eyes witness of E1–E6 against the frozen yardstick; never fixes; resumed for re-passes}
participant_5: {seat: houston, brand: <either>, role: card: consult — scope item 7 / E7 at closure, and any move that crosses L17/L20/L21 mid-bed}
participant_6: {seat: eagle, brand: claude, role: mechanical facts with a shell (ls, hashes, git), one file, command + verbatim output}
participant_7: {seat: majkee, brand: human, host: office, role: intent · one-line decisions on a costed deck · the skin note (his voice) · GO}
status_owner: x5-head
head_note: "cSharp — res/csharp-head-protocol.md; stays live through the arc as navigator and status_owner"
observations_read:   # run `ls /home/hruzam/unikuklatrix/nablarva/.dev/observations/nablarva*` yourself; at 2026-10-24 11:45 these exist:
  - .dev/observations/nablarva-X0-restarted.{atlas-ui,oraculum,trajectory}.*.md
  - .dev/observations/nablarva-X1-architecture.oraculum.2026-10-22.md (+ trajectory, note-to-trajectory, tunnel-support-pad)
  - .dev/observations/nablarva-X1-to-X3-arc.agol.2026-10-22.md
  - .dev/observations/nablarva-X1-X3-closure.oraculum.2026-10-24.md
  - .dev/observations/nablarva-X2-builder-narative.cartan.2026-10-23.md
  - .dev/observations/nablarva-X3-architecture-sitting.oraculum.2026-10-23.md
  - .dev/observations/harvest.2026-10-23.agol.md · harvest.2026-10-24.agol.md (U5–U11 → §7 below)
  - plus whatever architecture-X0 and architecture-X1 promote before this bed opens
```

Participants name assignments, not running runtimes. Keep the active team small; one body author at a time. Brand of the head is majkee's pick (Claude or Codex); the Codex equivalents are astrobley (implementer) and Cartan-native seats — see `.dev/session/nablarva-X4-vist/raw/handoff.csharp-method.cartan.2026-10-24.md`.

## 2. Scope (r2 §4, carried; owned paths are proposals until P1 confirms them)

| # | item | first client(s) | owned path (proposal) | decided by |
|---|---|---|---|---|
| 1 | **Address registry** — contract + first writer (ovitmugen on pane creation) + first reader (a status reader, or termbrana's target pick, whichever is cheaper). Seat-addressed (durable identity), never PID/pane. | writer: ovitmugen · reader: one | lives in the **shared-substrate component** — own thin folder per L18, **disk name chosen in P1 after the mandatory duplicate/cross-interference sweep** (AGENTS.md naming law); writer code in ovitmugen.py (path per `raw/inventory.what-exists.explore.2026-10-24.md`) | X0-3 = a; said: majkee organs §1 |
| 2 | **Config rule** — the mechanism: a settings file; no literal path in any script. Home: project-scoped state `<project>/.nablarva/` (registry, record segments, bed-local settings) · machine defaults `~/.nablarva/`. One `.gitignore` line for `<project>/.nablarva/`. | every script in the slice | settings file in the component; resolver = one function/shell helper | X0-4 = a; said: majkee organs §1 "common things" |
| 3 | **Shared observation record** — layout only: per-writer append-only files, **one serialized writing process per file** (Houston c1), segment-able, head/index readable in ≤80 lines (U-g), envelope-agnostic lines. **Not docket 8.** | producer (item 4) · reader (item 5) | `<project>/.nablarva/<record-dir>/<writer-id>.*` — exact shape in P1 | X0-3 = a; Houston consult c1, c3 |
| 4 | **One producer** — the cheapest honest one: a tmux `set-hook` writing to **its own per-pane file**, OR Package Q's collector if the termpanum line (Cartan) lands first. Coordination row in STATUS; cross-head traffic through majkee with paths. | record | per-pane file; hook definition in the component, installed by ovitmugen, never by hand into a living session | r2 §4 item 4; Houston c1, c5 |
| 5 | **One view** — ovitmugen's sessions column or a tiny reader shows one derived state per seat (active / idle by last-event age) **from the record, not from tmux polling**. | registry + record | ovitmugen.py or a `nablarva-*` reader (name after sweep) | r2 §4 item 5 |
| 6 | **Skin note** — `raw/skin-requirements.majkee.md`, append-only, one line per felt gap, majkee's voice, no analysis, no framework choice. Head asks "one line for the skin note?" whenever majkee says the view is not enough. | instarmux sitting brief (later bed) | that file | X0-6 = a |
| 7 | **Houston `card: consult` at closure** — implements a shared layer (L21 (2)); touches L17. Also mid-bed on any seam crossing. | — | consult text landed verbatim in raw/ | r2 §4 item 7; handoff §7 |

**Out of scope (fixed at authoring):** delivery of any kind (HELLO, doorbell, stridulatrix) · envelope choice (docket 8) · router (`nablarva <tool>`) · dashboard · Zellij loader · muticula build · skin framework · phone organ · continuity mechanism · naming the real steward (U-steward, majkee) · renaming stridularium/Boost (X1 and later, one-cell edits).

## 3. Work sequence (a shape, not a law — fit it to the team you get)

| phase | assignment | evidence / output |
|---|---|---|
| P0 | Head enters fresh: AGENTS.md read order · flag L1–L23 · pulse · ARCHITECTURE (r8 if X1 closed; else L21 over §2.5) · this substrate · `raw/answers.majkee.*` of arch-X0 (pinned) · observations. Verifies: HEAD, dirty paths and **whose** they are, ovitmugen.py path + `ov-selftest` green, X1 state. Adopts STATUS pen. **Freezes E1–E7 as the yardstick file before any build.** | STATUS first write; `raw/yardstick.E1-E7.md`; one bounded first POINT |
| P1 | **Sweep + name + contracts.** Duplicate/cross-interference sweep for the component's disk name (grep repo, `~/ia-sync`, live zsh configs). Contract files: registry schema (seat id · pane id · bed · host · ts), record layout (per-writer file naming, line shape, segment rule, head/index), settings file shape + resolver. No code yet. Houston consult if the contract crosses a seam you did not expect. | `raw/contract.registry.md` · `raw/contract.record.md` · `raw/contract.settings.md` · sweep file (eagle) |
| P2 | **Registry writer + reader** (trajectory): ovitmugen writes on pane creation via the resolver; reader shows the registry. Run E1, E2 locally (not yet the witness). | code diff (shown to majkee before commit) · local E1/E2 output |
| P3 | **Record layout + producer** (trajectory/delta): per-writer files; one hook, own file per pane; serialization proven (E3 mechanical check). Coordinate with Package Q if it exists. | code diff · E3 output |
| P4 | **View** (trajectory): derived state per seat from the record. Local E4. Majkee uses it; skin-note lines harvested. | code diff · E4 output · `raw/skin-requirements.majkee.md` growing |
| P5 | **Witness** (assay, fresh, yardstick only): E1–E6 against the bytes; head writes its own expected list **before** reading the witness (handoff rule 7). Houston `card: consult` → E7. Defects → reiterate P2–P4, resume the same witness. | assay VERDICT · Houston text landed verbatim |
| P6 | **Majkee GO/STOP** on the gate. Then closure: observations promote before prune · agol once · skin note → handoff for `instarmux-X0-sitting-brief` · **muticula-01-qualify pulse row alignment is majkee's at this point** (said: majkee 11:45 "muticula can wait to be aligned, when spine will be finished") · U-steward re-asked · successor handoff for `stridulatrix-X0-hello`. | closure manifest · promoted observations · harvest |

## 4. Acceptance evidence — frozen before build; assay reads the yardstick, never the transcript

- E1 `grep` over the slice's scripts finds no literal registry/record path; the resolved path (`<project>/.nablarva/…` or `~/.nablarva/…`) comes from the settings file (command + output).
- E2 `ov-up <slug>` → registry gains N seat entries; `ov-down` + `ov-up` → same seat ids, new pane ids (diff of two registry snapshots).
- E3 record directory: one file per writer; a mechanical check shows no two writers share a file (writer id in filename and in every line).
- E4 reader output shows a state per seat derived from the record; killing the producer changes the state without touching tmux state.
- E5 witness: tmux `pipe-pane`/hook audit shows zero `send-keys`/`paste-buffer`/`load-buffer` into any session pane for the slice's lifetime (L4, L17).
- E6 head/index of the record readable with `head -80`.
- E7 Houston closure consult: fits or stretches with constraints carried to flag/dock; no breaks.

## 5. Known constraints and holds at authoring (fixed → RUNBOOK; discovered mid-bed → STATUS holds)

- **Locks that bind the slice:** L3 S1 (the room journal is stridulatrix's single-writer truth — the record is NOT it and never becomes it) · L4 (recorded deaths incl. send-keys injection — not reopened by qualification) · L14 D1 (PTY/tmux base layer; no vendor devices where avoidable → a CLI-hook producer is optional, own file) · L17 (discovery ≠ delivery authority; ovitmugen performs panes) · L18 (organ-body homes — the component gets its own thin folder) · L20 (observations authorize nothing) · L21 (one body; shared layer = own release) · L22 (sealed vaults `.hlm/` `.majkee/` — never read).
- **Houston's five constraints (consult 2026-10-24, `inferred:` strength, carried whole):** one serialized writing process per file · name the owner or admit the gap (admitted: interim steward) · timestamp merge is a reader-side view, stage 1 only · never room truth or delivery authority · CLI-hook producers optional, own file, hook→bus parked.
- **Working split (said: majkee; r8 after X1):** termbrana composes/submits, ends at a packet file in the bus; stridulatrix sends (journal, cursors, adapters, receipts, API boundary); termbrana never writes into a session; stridulatrix never composes; stridulatrix requests panes, ovitmugen performs. The slice touches neither sender nor composer.
- **Cross-head:** Package Q belongs to the termpanum line (Cartan). Coordinate the producer through majkee with paths; do not edit their bed. Foreign dirt in the tree is never absorbed, staged or reverted (ask whose it is).
- **Config rule is law from day one:** a literal path in any slice script fails E1 and the bed.
- **No commit without majkee's word; canon-touching files shown first.** Carrier Bash is a whitelist (handoff §3 rule 1): spawn delta for anything blocked; never route around a denial.
- **ARCHITECTURE §2.5/§4.7/§9 are stale against L21 until r8** — cite L21.

## 6. Falsifiers / stop rules (r1 §3 lens 11, carried)

- Registry cannot be written by ovitmugen without a hardcoded path → the config rule is harder than assumed: **stop, design config first**, re-POINT.
- No producer can write per-writer files without a serializer → Houston c1 bites: **narrow to one producer**, record the limit.
- The derived state in the view needs tmux polling rather than the record → the record is not yet useful: **stop**, back to P3.
- Any step wants to type into a pane to "make it work" → that is delivery (L4/L17): **stop, STATUS hold, majkee**. U-send-keys is his, on evidence, later.

## 7. U-rows to carry into the RUNBOOK (name them; do not resolve them here)

| row | item | owner / when |
|---|---|---|
| U-send-keys | is a contentless nudge over the PTY "injection" in L4's sense | majkee, on slice evidence — surfaced at X5 closure, decided in stridulatrix-X0 |
| U-steward | real owner of the shared-substrate component (interim: x5-head) | majkee; re-asked at X5 closure |
| U-continuity | journaling, rotation of long canon files, planning across sessions; requirement carried: records segment-able, ≤80-line head | majkee, no fixation yet |
| U-vendor-spawn | Claude Code / Codex / Gemini CLI spawn & message internals | bounded @Epoch pass, only when a stridulatrix design needs it |
| docket 8 | envelope — four candidates (ARCHITECTURE §4.5); working default: bounded comparison first | termpanum line |
| Package Q coordination | whether the producer is the hook or Q's collector | X5 P1/P3 with Cartan via majkee |
| Agol U8 | clock from `date` in the same turn; record a relay/commit/send only after it happened | x5-head, every turn |
| Agol U9 | dark measurement: a missing usage/`ctx` line is logged `unmeasured` before the next large ask; counts re-derived from files | x5-head |
| Agol U10 | operator decisions ship as a costed deck, never blank fields | x5-head (§8 below) |
| Agol U11 | head writes its own expected list before reading a drafter's/witness's output; every `@<sha>:<path>` cite checked with `git cat-file -e` before commit | x5-head |
| Agol U5 | if any drafter runs on a long-lived Claude child: name the fresh-child trigger and handoff set at authoring | x5-head, only if applicable |

## 8. Method carried: the costed deck + Houston by phase

**Costed deck** (said: majkee 2026-10-24 "looking fine like methodologic substrate for next cSharp"; full text + example: `.dev/session/nablarva-X4-vist/raw/handoff.csharp-method.oraculum.2026-10-24.md` §6; proven again in arch-X0: seven blocks, seven answers, ~4 hours incl. landing). Shape:

```
GAVEL <source-qualified id> · <the question, one sentence?>
  options:  a) … b) … c) …      context: <enough to decide without opening a file>
  buys: … cost: … can be lost: … consequence: …
  lean: <seat> → <option> — <one reason>     source: <path[:line]>     answer: ___
```
One block at a time in chat; the deck also in a file; his answer lands verbatim in `raw/answers.majkee.<topic>.<date>.md` **before** anything acts on it; "own"/mixed answers → placement table, then the few questions only he can answer.

**Houston by phase** (handoff §7, compressed): build/organ work → `card: consult` from the head or majkee when a move crosses a seam, touches L17/L20/L21, changes ownership, or at closure — returns fits · stretches · breaks · unclear + ≤5 constraints, writes nothing. After a meaningful closure → `card: audit`, majkee invokes, give it an input file; it NAMES edits, a shell seat makes the diff. Reshaping the animal (UI vs terminal is this class) → `card: sitting`, majkee assigns — **not this bed**; the skin waits for the note. Name the card on the first line of every Houston assignment.

**Subagents and carrier rules:** handoff §2 (who for what, with the watch column) and §3 (ten technical rules) — read them once at P0; they are substrate, not law.

## 9. First hour for the X5 head (P0 checklist)

1. `date` · read order (AGENTS → flag L16–L23 → pulse → ARCHITECTURE r8 or L21) · this file · arch-X0 `raw/answers.majkee.deck` + `organs` (pinned) · observations (`ls .dev/observations/nablarva*`).
2. `git status`: list dirty paths and ask majkee **whose** they are before anything is staged.
3. Confirm ovitmugen.py path and `ov-selftest` / `rb-selftest` green (eagle, one file).
4. Confirm X1 state: ARCHITECTURE at r8? If not, pin r2 and add the dependency row.
5. Write STATUS (gate verbatim from the RUNBOOK; `steward: interim (U-steward)`; coordination row for Package Q; holds from §5).
6. Freeze `raw/yardstick.E1-E7.md`. Only then the first POINT (P1 sweep).
7. Ask majkee once: how many confirmations he wants for bookkeeping commits in this bed; and whether the head brand/seat list above is the team he wants.

## 10. Open for majkee at X5 opening (not decided by arch-X0)

- Brand of the X5 head (Claude / Codex) and the participant list in §1.
- Whether X5 may open before `architecture-X1-bookkeeping` closes (default from X0-5 = a: no).
- The component's disk name — **his GO on the sweep result**, not the head's pick alone (naming law).
- Whether to record `GLOSS.spine.md` (the driver ASKS; never assumes — AGENTS.md).

— oraculum(arch-X0), 2026-10-24
