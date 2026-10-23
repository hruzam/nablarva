# ARCHITECTURE — nabLarva, the whole animal

`checked: 2026-10-22` · `state: DRAFT for majkee GO — not promoted; promotion target docs/ARCHITECTURE.md (L16.9)`
`authored: houston (card: sitting), X3 architecture sitting · links are relative to docs/`

This document holds what crosses organs: the layer model, dependency direction, the seams between
organs with their owners, shared grammars, system-wide boundaries and the ladder. It never holds
one organ's detail; that lives in the organ's own body (L16.9). Locks live in
[flag.md](../.dev/session/flag.md), the machine contract in [PROJECT.yaml](../PROJECT.yaml), the
animal's index in [PROJECT-DESIGN.md](../PROJECT-DESIGN.md), and live work in the `STATUS.md`
files routed by [pulse.md](../.dev/session/pulse.md).

**How to read a statement here.** Every claim carries its type (L16.11):
`locked: L<n>` is a gaveled flag line · `said: <source>` is that source's words or ruling ·
`inferred: houston` is this document's interpretation · `unknown:` is open, with its docket item
when one owns it. Seam rows mark each capability **accepted** (qualified or locked), **planned**
(directed, not built or not qualified) or **open** (undecided). A statement without a lock or a
cited decision is a proposal. Majkee's sitting rulings (gavel deck G1–G9, arc picks Q1–Q8) have no
flag L-id; they are cited as `said: majkee`.

## 0. Shape of record

The proto-architecture is the settled triangulation: S1–S8 and Z's five adopted organs
(consultation leases · four-phase blind protocol · versioned goal revisions · human-accepted
checkpoints · at-least-once delivery with replay markers), in
`../raw.nablarva/oraculum-basic-triangulation/triad.comparison.2026-07-31.md` (locked: L3).
Position Y: `../raw.nablarva/oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md`.

The generation-X direction holds where older narratives conflict: tmux with clean PTY sourcing is
preferred, Zellij where its ceilings can be reached (said: majkee, gavel deck G1). This document
grounds that direction; it does not reopen intent discovery.

## 1. Layer model

The animal is a set of planes. Each plane allows certain effects and forbids others. `inferred:
houston`, assembled from the locks cited per row.

| plane | what lives there | allowed effect | forbidden effect | grounds |
|---|---|---|---|---|
| **sessions** | living CLI agent sessions on the workstation, in tmux | the agents' own work | — | locked: L14 D5 (sessions live on the workstation) · said: majkee G1 |
| **observation** | termpanum (observation lab) · VIST principle and candidates · Termbrana's Zellij observer | read, record, report with provenance | typing into sessions, injecting context, granting acceptance | locked: L13 (name) · said: PROJECT-DESIGN §3.6 · locked: L11/L17 (observer) · said: majkee Q3 |
| **composition** | Termbrana's composition family | validate and (planned) prepare text | sending | locked: L17 |
| **room / delivery** | stridulatrix broker and CLI · single-writer room journal · adapter-owned PTY delivery | regulated writes into sessions | tmux as protocol, send-keys injection | locked: L3 S1/S5 · L4 · L13 · L14 D1/D2 |
| **view** | ovitmugen (frame, view/layout) · stridularium (phone lens) · observer views | show, attach, switch views | owning or ending a session's life by closing a view | locked: L17 (ovitmugen) · L14 D5 (detaching never closes a bed) |
| **coordination** | muticula (checkout claims) · session surfaces (flag · pulse · STATUS) | claim, hand over, record state | a second authority for the same fact | said: PROJECT-DESIGN §3.5 · locked: L9/L9′/L16 |
| **build · install** (cross-cutting) | ia-sync source → reviewed deploy / installer → live host | ship organs as installable packages | auto-deploy from this repo | locked: L6 · L8′ · said: majkee Q5 |

**Brick-layer sub-model (candidate).** Inside the zsh brick layer, Nabla-Tmux v0 proposes six
layers: boot · living tissue · gates · bricks · services · substrate (said: v0, a candidate frame
"for collecting bricks" per majkee; sha256 `00251ebf…66a0`, §Layers). It describes how bricks are
organised, not the whole animal: the Rust/WASM observer, the Android app and a future broker sit
outside it (`inferred: houston`; said: majkee Q5 keeps exact packaging and runtime sharing for
later).

## 2. Dependency direction

1. **Content travels in files; the PTY carries only the impulse.** locked: L14 D1/D2 (file plane
   is the spine; PTY as impulse layer — plan, not lock — "full PTY orchestration" stays dead). v0's
   rule "content lives in files; tmux only rings the doorbell" is the same direction (said: v0,
   candidate). The doorbell's *mechanism* is open (§4, row deliver).
2. **Observation never depends on, or grants, delivery.** Discovery is not delivery authority;
   future transmission requires checked target binding and explicit authority (locked: L17).
   Observations are evidence, never acceptance (said: PROJECT-DESIGN §3.7; VIST brief §Limits).
3. **Viewers depend on sessions and never own their lifetime.** locked: L17 (ovitmugen keeps
   protected process lifetime) · L14 D5 · said: PROJECT-DESIGN §3.2.x "A viewer never owns
   lifetime" (candidate principle).
4. **Clients are independent; shared mechanisms sit at a narrow edge.** locked: L17 — composition
   and ovitmugen are independently useful clients; the shared layer's owner/home/API is open; no
   common framework or transport is authorized. Termbrana must work with nabLarva absent (said:
   toolbox/termbrana/README.md §Product direction).
5. **Room truth flows one way: journal → projections.** locked: L3 S1/S2 — the append-only
   single-writer journal is the sole room truth; participant cursors are projections.
6. **Within the brick layer (candidate): control down a tree, information sideways through
   shared files, never brick to brick.** said: v0 rules 1–2. Whether the tree is one animal-wide
   router or a pattern each organ repeats is open (§9, X5).

## 3. Principles carried as candidates

From Nabla-Tmux v0 (said: v0, candidate; "not insisting on exact details where is a lot against
philosophy", said: majkee). Each holds only as far as the cited locks allow.

| principle | consistent with | limit |
|---|---|---|
| Every state file has exactly one writer | locked: L3 S1 | v0's own event log has many appenders (§9, X4) |
| Commands are imperative, events past tense | — | a naming grammar, not an event format (docket 8) |
| Optional parts fail soft | locked: L17 · said: termbrana README | — |
| Load cost follows use; edges are executables, insides load on first call | — | brick-layer only |
| Python computes, zsh acts | locked: L17 (composition family: zsh entry + Python stdlib, conditional on responsiveness) | does not decide docket 2 |

## 4. Seam ledger

One row per cross-organ seam. Cells point to their owning source; notes 4.x carry what a cell
cannot. **accepted** = qualified or locked · **planned** = directed, not built or not qualified ·
**open** = undecided.

| seam | owner | consumers | governing | accepted | planned | open |
|---|---|---|---|---|---|---|
| **observe** | `unknown:` — termpanum is the observation **lab** by name (locked: L13, name only) | VIST candidates · views · humans | L13 · L14 D1 · L17 · said: majkee Q3 | read-only stance: never types or injects (said: PROJECT-DESIGN §3.6) | termpanum build plan, documentary first (said: X2 plan, uncommitted) · VIST contract | producer topology (said: cartan-x2 X2-1, "unspecified") · VIST ↔ termpanum overlap (4.1) |
| **compose** | Termbrana composition family (locked: L17) | humans · editors · pipes · assistant drafts | L17 · L8′ | Phase 0: packet validation with opaque byte preservation incl. body EOL; grammar v4 (locked: L17; said: composer handoff) | generation-X sourcing — common programs/controllers, germline, vendor shapes/rosters, SPECIAL incl. germline/pipes — and preparation (said: termbrana README §Future adjustable sources) | loader, picker, renderer, native activation, editor target (4.2) |
| **deliver / write into a session** | `unknown:` — proposed: stridulatrix (said: PROJECT-DESIGN §3.7) | agents · humans | L3 S5 · L4 · L14 D1 · L17 | rejected mechanisms stay dead: send-keys injection, git-as-wire (locked: L4) | regulated adapter-owned PTY delivery (locked: L3 S5, unbuilt) | doorbell mechanism · classifier · VIST actuator · human tmux/editor/pipe push qualification (4.3) |
| **view · layout · process lifetime** | ovitmugen for view/layout and protected process lifetime (locked: L17) | humans · phone · observer views | L17 · L14 D5 | detaching never closes a bed (locked: L14 D5) | — | collector process lifetime (said: cartan-x2 X2-3, "unspecified") · brick spawn/close vs ovitmugen (4.4) |
| **room truth** | stridulatrix journal (locked: L3 S1; name L13) | all participants via cursors | L3 S1–S3, S8 | design settled (L3) | single-writer journal, cursors | lifecycle `unknown: docket #4` · store `unknown: docket #5` · room topology `unknown: O3` · event vocabulary `unknown: docket #8` (4.5) |
| **human door** | stridularium (locked: L13) | the human | L14 D5/D6 | thin lens; app-scoped reach; host-side engine (locked: L14 D5/D6) | `stridularium-00-design` (said: docs/organs/stridularium.md) | native terminal vs rendered cards (said: same) |
| **cross-host** | — | stage 2 | L3 S7 · O2 | same protocol over SSH to one central broker (locked: L3 S7) | — | transport `unknown: O2` (lean recorded in flag Archived index) |
| **checkout coordination** | muticula | cooperating teams | — | — | claim · work · hand over (said: PROJECT-DESIGN §3.5) | enforcement coverage (said: muticula-01 gate, pulse.md) |
| **context sourcing · reading** | `unknown:` — a controller/function under the eventual sourcing program (said: majkee G5, direction) | builders · verifiers · planners · Houston · Termbrana/IDE clients | L16 · said: majkee G4/G5 | reading schedule: preparation before RUNBOOK, recipient reading at entry, refresh on change (said: majkee, gavel deck STEP 5 "gaveled") | Nablarva Boost reader concept, typed source descriptors (said: boost brief, open design) | reader schema · program home/API · navigation surface (4.6) |
| **key meanings** | this document, §5 | every organ's TUI | L16.9 · said: majkee G3 | KEYS CODE (accepted by majkee 2026-09-29) | — | keyboard / command-discovery design; palette ownership (said: keys brief) |
| **build · install · publication** | `unknown:` | the operator's hosts | L6 · L8′ · L12 · L17 | route as described: ia-sync source → reviewed `deploy.sh` → `~/.config/zsh/`, plus `install-pkgs` (said: PROJECT-DESIGN VOLATILE) | coherent build/install packages for nabLarva and its toolboxes (said: majkee Q5) | package shape; one vs several; any shared runtime mechanism (4.7) |

**4.1 Observe.** VIST is a shared observation principle and an intended protocol: conceptual
boundaries first, then a concrete contract developed and qualified (said: majkee Q3). VIST names
*observations*; controller decisions and actuator actions stay separate components (said: majkee
Q3; VIST brief §Where VIST sits). Antensor is an implementation candidate (said: majkee Q3). Its
event envelope is proposed. Termpanum and VIST are siblings: termpanum reports inform VIST and can
qualify candidate VIST updates; producing evidence grants no admission (said: X2 RUNBOOK, as
Majkee's direction). Majkee holds canon and gavel (locked: L16.1); the operational admission
receiver is not appointed (said: X2 plan §5). The overlaps with termpanum (observe) and
stridulatrix (deliver) stay visible here; no ownership is assigned (said: majkee Q3). v0's "living
tissue" (tmux and CLI hooks writing events) is a third candidate producer (said: v0 §Layers).
Organ-local records are allowed without animal-level compatibility (said: cartan-x2 X2-2).

**4.2 Compose.** Composition does not require a session bed, editor, tmux or ovitmugen (locked:
L17). An architectural verb must not promote a planned capability into a dependency: consumers
depend only on the accepted column (said: composer handoff, cycle37 correction). Each
generation-X sourcing category keeps its owner, consumer contract and acceptance; a split needs
named remaining gates (said: composer handoff). Adjustable sources do not imply generic YAML/TOML
loading or instruction execution (said: same). Composer's architecture-owner proposal is
attributed input to this row (said: majkee Q4; its text is reproduced in the composer handoff at
`nablarva@78059da:.dev/session/nablarva-X3-architecture-sitting/raw/handoff.composer-boundaries.cartan.2026-10-22.md`).
Current editor target: Sublime, intended app-neutral (said: majkee G2) — not an editor decision
(`unknown: O4`).

**4.3 Deliver.** Editor/pipe/tmux push is a human-operated carrier outside L3/L4's regulated
protocol until separately qualified; assistant draft contribution grants no autonomous sending
authority (locked: L17). Three candidates touch this seam and none is accepted: v0's doorbell typed
with `tmux send-keys -l` and rung by a watcher (said: v0 §Messages), v0's classifier routing output
(said: v0), and VIST's actuator (said: VIST brief). Each meets locked: L4 (send-keys injection is a
recorded death) and L3 S5 (tmux never the protocol). A pointer-only nudge is closer to L14 D1's
impulse layer than to content injection (`inferred: houston`) — but the automated mechanism is
unqualified. Open (§9, X1/X10).

**4.4 Lifetime.** Ovitmugen's protection is a constraint; it is neither extended nor transferred
to a newly appointed owner (said: cartan-x2 X2-3). A brick that spawns or closes panes (said: v0
`pane-spawn`/`pane-close`) acts on this seam; who may do so is open (§9, X8).

**4.5 Room truth.** Four candidate event envelopes exist and none is chosen: Nabla-Tmux v0's
record, the VIST event model v0, the termpanum EVENTS map v0.3, and the proposed `jev.event/v1`
convergence (said: `../.dev/research/termpanum-events/events-map.v0.2026-10-02.md`, "OPEN →
majkee"). `unknown: docket #8`.

**4.6 Context sourcing.** One owned source should serve human/file readers and the intended
deterministic engine; pins are derived at acquisition, not handwritten (said: boost brief,
proposal). A required prerequisite that exceeds a budget stays visible, never silently shortened
(said: G5 brief). A pin proves read bytes, not continued applicability (said: G5 brief). The
existing any-seat read order (AGENTS → flag → pulse → PROJECT.yaml) is not waived by a selected
profile (said: G5 brief, gaveled schedule).

**4.7 Build · install.** The direction is coherent build/install packages for nabLarva and its
toolboxes **while the independent client boundaries hold** (said: majkee Q5). Coherent packaging
does not itself select one global router or a common runtime framework (said: majkee Q5).
`inferred: houston`: two axes — run/use independence (L17) and build/install coherence (Q5) — can
both hold; whether build coherence implies any shared runtime mechanism is open, and if it does,
L17's narrow-edge rule applies. Promotion out of this repo is a reviewed merge, never auto-deploy
(locked: L6).

## 5. KEYS CODE

*Added 2026-09-29 by Trajectory (ovitmugen-00-console) at majkee's request · **ACCEPTED by
majkee 2026-09-29** (D3 in
`nablarva@c630f0e8b1490e34458a52988342d679b24f2f5b:.dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md`).
Moved here from PROJECT-DESIGN.md at this document's promotion (said: majkee G3 a); the wrapper
keeps its `# KEYS CODE` heading as a pointer.*

**DRY:** the meanings live only here. An organ's help points to this chapter and lists only
its own extra keys — it never copies this table.

One shortcut style for every organ's TUI: **the same key means the same thing everywhere**,
so moving between toolboxes never means relearning. This is a grammar, not a registry:
each organ keeps its keys in its own code; this chapter only fixes their meaning.

Shell commands stay under the claviature rule (`~/ia-sync/zsh/guides/claviature.global.spec.md`,
"derive, don't register"): families only (`ov-`, `rb-` …), the `keys` panel derives the rest.

### Shared meanings (all organs)

| key | meaning |
|---|---|
| ↑↓ · j k | move |
| Enter | act / open the selected item |
| q · Esc | back (close the view, never quit something running) |
| ? | help for this view |
| / | search |
| a | add |
| x x | remove — **always two presses** (first arms, second acts, any other key disarms) |
| b | build (create what is missing) |
| o | open / attach |
| r | refresh |
| T | tabs (agent tabs of the bed) |
| 1-9 | jump to item / part N |

### Reserved (never bound by an organ)

- `C-a` — the ovitmugen frame prefix (frame keys: focus, split, popup, restart, tabs).
- `C-b` — the agents' own tmux.
- Keys a running agent needs (anything typed into an agent pane) — organs act only in
  their own views.
- `Alt-…` — open: may become prefix-less tab jumps (`Alt-1…9`); decide before any organ uses Alt.

### Conformity today (honest check, 2026-09-29)

| organ · view | follows | deviates |
|---|---|---|
| ovitmugen console | ↑↓ j k · Enter · q Esc · a · x x · b · o · r | ? and / not yet |
| runbook tree | ↑↓ · Enter · q Esc · ? · r · T · 1-5 · A A (two-press) | no j k; `h` also opens help; no / (search only inside help: Ctrl-F / F) |
| runbook buffer view (P) | q · ↑↓ | `x` removes a line with ONE press |
| ovitmugen frame (C-a …) | reserved prefix | — |

Deviations are listed, not fixed here: each fix belongs to its organ's own session.

**Beyond the grammar (open).** Relocating the accepted grammar does not settle the larger
keyboard and command-discovery design: tool-owned command truth, a derived catalogue,
toolbox-attached palettes, and the effect distinctions explain · insert · prepare · execute ·
request delivery (said: keys brief, research and proposed directions). An attached palette is not
a sending authority (locked: L17).

### Reading aid — same word, different things

A reading aid, not an adopted glossary or a renaming (said: majkee Q6).

- **session gate** — the one acceptance condition of a session (`gate:` in its RUNBOOK and STATUS;
  locked: L16.2) · **command gate** — in v0's brick layer, a pipe's executable entry that checks
  input, resolves context and dispatches (said: v0 §Glossary, candidate).
- **RUNBOOK document** — a session's stable intent, assignments and rules, read at entry; current
  position lives in STATUS (said: G5 brief, gaveled schedule) · **proposed executable step runner**
  — v0's "runbook": a command file whose steps run in order and stop on failure (said: v0, candidate).
- **program controller document** — a CONTROLLER.md indexing a program's functions, the candidate
  home for the context-sourcing procedure (said: G5 brief) · **VIST controller** — the decision
  component between VIST observations and actuator actions (said: VIST brief; majkee Q3).

## 6. The ladder (L2)

Framing locked, stage content evolves (locked: L2).

- **Stage 1 — same host.** Every row of §4 is a stage-1 seam today; the sessions plane is the
  workstation (locked: L14 D5).
- **Stage 2 — different host.** Same protocol over SSH to one central broker (locked: L3 S7);
  transport `unknown: O2`. Depends on rows room truth and deliver.
- **Stage 3 — stridularium.** The human's door (locked: L13); row human door; the room-dependent
  organ layer needs room truth and deliver (said: docs/organs/stridularium.md).

## 7. Organs and their homes

One line per organ (said: majkee G2 a). Home rule: an organ that already has a home keeps it; a new
body starts as a component folder with a thin `README.md` entry and grows chapters on need; the
organ/toolbox taxonomy is under review; the parent directory for new folders is not chosen (said:
majkee, gavel deck STEP 4). Reconciliation with the growth law (`inferred: houston`): a README-only
folder is K5's folder stage entered early, and K5's line → chapter growth continues inside it;
existing single-file bodies are not migrated for symmetry.

| organ | one line | home |
|---|---|---|
| **termbrana** | the terminal membrane: Zellij observer + composition family (locked: L17); composer work is its composition family (said: majkee G2) | observer `toolbox/termbrana/` with `DECISIONS.md` (locked: L11/L12) · composition `~/ia-sync/zsh/termbrana/` (locked: L17) |
| **ovitmugen** | tmux frame and session view manager; view/layout + protected process lifetime (locked: L17) | code `~/ia-sync/zsh/session/ovitmugen.*` (observed) · body: interim in PROJECT-DESIGN §3.2 (said: majkee Q2); body home `unknown:` |
| **termpanum** | observation lab, the read-only ear (locked: L13 name) | proposed `toolbox/termpanum/` (said: PROJECT-DESIGN §3.6) — not created |
| **stridulatrix** | broker and CLI (locked: L13) | `unknown:` (said: PROJECT-DESIGN §3.7) · design `../meshup/room.brokered-journal.2026-07-31/` |
| **stridularium** | the phone app, the human's door (locked: L13) | body [`organs/stridularium.md`](organs/stridularium.md) · code home proposed `stridularium/{android,host}` (said: same) |
| **muticula** | file-backed concurrency coordination in one checkout (said: PROJECT-DESIGN §3.5) | `unknown:` |
| **instarmux** | `unknown:` organ or placeholder (PROJECT-DESIGN §3.3 empty) | `unknown:` |
| **reposoma (tool)** | `unknown:` organ or placeholder (PROJECT-DESIGN §3.4 empty) | `unknown:` |

Not organs, cited only: **VIST** (observation principle and intended protocol; said: majkee Q3) ·
**Antensor** (implementation candidate) · **Nablarva Boost** (open reader concept) · **Nabla-Tmux
v0** (candidate brick frame).

## 8. Decisions and reading

- **Where decisions live** (said: majkee, gavel deck STEP 5): locks in
  [flag.md](../.dev/session/flag.md); product-technical rationale in component ledgers, each entry
  citing its authorizing flag line (locked: L11 pattern, e.g. `../toolbox/termbrana/DECISIONS.md`).
  No root ADR series is opened.
- **The root stub** `decisions/README.md` still promises that gaveled items land there, which
  contradicts the line above. Its correction versus retirement is `unknown:` and not decided here.
- **Who reads what, when** (said: majkee, gavel deck STEP 5, "gaveled"): context is prepared before
  RUNBOOK authorship; each recipient reads again at entry; the affected selection is refreshed on
  reassignment, scope or interface change, a changed governing source, a new constraint or a
  conflict. Missing, ambiguous or oversized required context holds the affected action. The
  procedure's survival as a controller/function is a promotion obligation; its schema, program home
  and API are open.

**Defaults and their revisit signals** (`inferred: houston` — the seam-ledger shape's defaults
table, as recorded in the arc pick; not separately ruled by majkee):

| default | reason | revisit when |
|---|---|---|
| one whole-animal document, tier 0 | K1/K8 (record) | ≥2 stale-pointer findings in one audit (record §Tiers) |
| `checked:` stamp only | said: majkee G6 a · locked: L16.7 | the earned-mechanism condition in `architecture-process` §9 is met |
| decisions in flag + component ledgers | said: majkee STEP 5 | a genuinely cross-component decision needs a shared rationale home (said: G5 brief) |
| existing organ homes; new bodies as folder + README | said: majkee STEP 4 | a root is chosen, or a navigation probe shows wrong-source selection |
| KEYS CODE meanings only in §5 | said: majkee G3 a | the command-discovery design yields an owned catalogue |
| organ-local event records, no shared envelope | `unknown: docket #8` | docket 8 is gaveled |

## 9. Open questions

Docket and O-items (flag §Pending gavel / §Open), each marked where this document depends on it:
docket 2 v1 language (everywhere a language is named) · 3 git residual seat · 4 broker lifecycle
(room truth) · 5 journal store (room truth) · 6 V1 cut (all rows) · 8 discrete-state vocabulary
(observe, room truth) · O1 hosting machine · O2 cross-host transport · O3 room repo topology · O4
monitor brick-set.

Collisions between Nabla-Tmux v0 and locked or newer state, named and unresolved (said: v0 against
the cited locks; detail in the X3 arc,
`raw/arc.r2.md` §3 — pin owed at promotion):

| id | v0 | meets |
|---|---|---|
| X1 | doorbell typed with `tmux send-keys -l` | L4 · L3 S5 · L17 |
| X2 | compiled broker binary later | L4 (C++/Go clause) · docket 2 |
| X3 | watcher as a user service | docket 4 (lean: pane) |
| X4 | one event record, many appenders | docket 8 · four envelopes · one-writer rule |
| X5 | one `nabla <pipe> <verb>` router | L17 independent clients |
| X6 | command `nabla`, `NABLA_*`, `~/nabla` | L13 (commands stay ASCII `nablarva`) |
| X7 | Termbrana as a popup inside the tree | L17 (newer) |
| X8 | bricks spawn and close panes | L17 (ovitmugen lifetime) |
| X9 | CLI hook writes agent output into the bus | L14 D1 (vendor doors parked) |
| X10 | classifier routes output | L3 S4 · VIST controller |
| X11 | substrate at XDG paths | L3 S8 · O3 · docket 5 |
| X12–X13 | gate · runbook · status · pipe · controller | §5 reading aid |

Cross-head items (said: cartan-x2, confirmed): observation producer topology unspecified (X2-1);
collector lifetime owner unspecified (X2-3).

Other open items: the root for new organ folders (G4) · reader schema, program home/API, root stub
(G5) · ovitmugen's body home (said: majkee Q2) · the build/install package shape (Q5) · the shared
layer's owner/home/API (L17) · the operational VIST admission receiver.

## Sources and pins

Durable cites follow the commit-pin rule. The pins below were verified at drafting:
- KEYS CODE acceptance: `nablarva@c630f0e8b1490e34458a52988342d679b24f2f5b:.dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md` :120.
- Sitting record and rulings: `nablarva@78059da:.dev/session/nablarva-X3-architecture-sitting/raw/{gavels.X4.2026-10-17.md,prompt.sitting.2026-10-17.md,brief.component-docs-and-nablarva-boost.2026-10-21.md,brief.nablarva-boost-reader-concept.2026-10-21.md,brief.adr-task-context.2026-10-21.md,brief.keys-command-discovery.2026-10-21.md,handoff.composer-boundaries.cartan.2026-10-22.md}`.
- VIST brief: `nablarva@78059da:.dev/session/nablarva-X4-vist/raw/vist-01-principle-and-applications.md`.
- Shelf law: `nablarva@2ae8636:.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md`.

**Pins owed before promotion** (uncommitted at drafting, cited by sha256 only):
Nabla-Tmux-Architecture-Draft-v0 (.md `00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0`; zip `a7d28babe12277292f204fe6801d58b04087a3d3715068e1254b8683415e0ae7`) ·
X2 `termpanum.build-plan.md` (`4e039f9f787c3224e8bb8c63342d3cdf68027339dd51ace682db89e430c83145`) ·
X2 `disposition.x3-vectors.cartan.2026-10-22.md` (`efe7573d…68f7b`) · X3 `arc.r2.md` and
`arc.pick.2026-10-22.md` (Houston's own raw drafts). Majkee's Q1–Q8 answers live in the head's
record. A promoted document must not point into a prunable session folder without these pins.
