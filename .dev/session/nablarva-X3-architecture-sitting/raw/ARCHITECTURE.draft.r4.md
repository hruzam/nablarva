# ARCHITECTURE — nabLarva, the whole animal

`checked: 2026-10-22` · `state: DRAFT r4 for majkee GO — not promoted; promotion target docs/ARCHITECTURE.md (L16.9)`
`authored: houston (card: sitting), X3 architecture sitting · links are relative to docs/`

This document holds what crosses organs: the layer model, dependency direction, the seams between
organs with their owners, shared grammars, system-wide boundaries and the ladder. It never holds
one organ's detail; that lives in the organ's own body (L16.9). Locks live in
[flag.md](../.dev/session/flag.md), the machine contract in [PROJECT.yaml](../PROJECT.yaml), the
animal's index in [PROJECT-DESIGN.md](../PROJECT-DESIGN.md), and live work in the `STATUS.md`
files routed by [pulse.md](../.dev/session/pulse.md).

**How to read a statement here.** Every claim carries its type (L16.11):
- `locked: L<n>` is a gaveled flag line, and covers only what that line enumerates.
- `said: <source>` is that source's words or ruling.
- `inferred: houston` is this document's interpretation.
- `unknown:` is open, with its docket item when one owns it.

Seam rows mark each capability:
- **accepted**: qualified, or a locked design constraint. This does not necessarily mean a working implementation.
- **planned**: directed, not built or not qualified.
- **open**: undecided.

A statement without a lock or a cited decision is a proposal. Majkee's sitting rulings have no
flag L-id and are cited as `said: majkee`. They are:
- the gavel deck G1–G9 (`gavels.X4.2026-10-17.md`);
- the arc answers (`answers.majkee.pick-and-q1-q8.2026-10-22.md`): Message A is the partial pick, and Message B is shape B plus Q1–Q8. "Q<n>" below means Message B;
- the R9-1 notes N1–N11 and the answers A/B/C (`answers.majkee.r9-1-notes.2026-10-22.md`, `answers.majkee.r9-1-abc.2026-10-22.md`), cited as "R9-1 N<n>" and "R9-1 A/B/C".

**nablarva.v0** is the candidate draft in the file `Nabla-Tmux-Architecture-Draft-v0.md`. The
file keeps its name. Nabla.Tmux is the name of the chatbot that wrote it (said: majkee R9-1 N7).

## 0. Shape of record

The proto-architecture is the settled triangulation in
`../raw.nablarva/oraculum-basic-triangulation/triad.comparison.2026-07-31.md`.
- Its settled points **S1–S8 are locked** (locked: L3).
- The same source also records Z's five adopted organs: consultation leases · four-phase blind
  protocol · versioned goal revisions · human-accepted checkpoints · at-least-once delivery with
  replay markers. These are a **source claim, not locked commitments** (said: triad comparison,
  as summarised by the pre-architecture pointer this document replaces).
- Position Y: `../raw.nablarva/oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md`.

The generation-X direction holds where older narratives conflict. Majkee's words (said: majkee,
gavel deck report 1): "I even folded  animal body (bricks) and reconfigure focus on tmux|PTY
(event  zellij where we can touch ceilings)" and "in contradictive narative wining tmux|PTY
solution", with "I want not go that cycle again when main intents were introduced". `inferred:
houston`: tmux/PTY is the preferred direction, and Zellij is used where its ceilings can be
reached. This document grounds that direction; it does not restart intent discovery.

## 1. Layer model

The animal is a set of planes. Each plane allows certain effects and forbids others. `inferred:
houston`, assembled from the locks cited per row.

| plane | what lives there | allowed effect | forbidden effect | grounds |
|---|---|---|---|---|
| **sessions** | living CLI agent sessions on the workstation, in tmux | the agents' own work | — | locked: L14 D5 (sessions live on the workstation) · said: majkee G1 |
| **observation** | termpanum (observation lab) · VIST principle and candidates · Termbrana's Zellij observer | read, record, report with provenance | typing into sessions, injecting context, granting acceptance | locked: L13 (name) · said: PROJECT-DESIGN §3.6 · locked: L11/L17 (observer) · said: majkee Q3 |
| **composition** | Termbrana's composition family | validate and (planned) prepare text | transmission without checked target binding and explicit authority; autonomous sending from assistant drafts | locked: L17 |
| **room / delivery** | stridulatrix broker and CLI · single-writer room journal · adapter-owned PTY delivery | regulated writes into sessions | tmux as protocol, send-keys injection | locked: L3 S1/S5 · L4 · L13 · L14 D1/D2/D4/D7 |
| **view** | ovitmugen (frame, view/layout) · stridularium (phone lens) · observer views | show, attach, switch views | closing a bed by detaching (locked); ending a session by closing a view (`inferred: houston`) | locked: L14 D5 ("detaching never closes a bed") · closing a view: consistent with ovitmugen's protected process lifetime (locked: L17) and said: PROJECT-DESIGN §3.2.x "A viewer never owns lifetime" — no lock says it |
| **coordination** | muticula (checkout claims) · session surfaces (flag · pulse · STATUS) | claim, hand over, record state | a second authority for the same fact | said: PROJECT-DESIGN §3.5 · locked: L9/L9′/L16 |
| **build · install** (cross-cutting) | ia-sync source → reviewed deploy / installer → live host | ship organs as installable packages | auto-deploy from this repo | locked: L6 · L8′ · said: majkee Q5 |

**Brick-layer sub-model (candidate).** Inside the zsh brick layer, nablarva.v0 proposes six
layers: boot · living tissue · gates · bricks · services · substrate. This is said: nablarva.v0,
a candidate frame "for collecting bricks" per majkee (sha256 `00251ebf…66a0`, §Layers).
`inferred: houston`: it describes how bricks are organised, not the whole animal. The Rust/WASM
observer, the Android app and a future broker sit outside it. Exact packaging and runtime sharing
are left for later (said: majkee Q5).

## 2. Dependency direction

1. **Content travels in files; the PTY carries only the impulse.** locked: L14 D1/D2 — the file
   plane is the spine; PTY as impulse layer (plan, not lock); "full PTY orchestration" stays dead.
   nablarva.v0's rule "content lives in files; tmux only rings the doorbell" is the same direction
   (said: nablarva.v0, candidate). The doorbell's *mechanism* is open (§4, row deliver).
2. **Relay work is research-gated.** Research precedes build: the canon mapping is
   `relay-00-research` (verdict gate) → `relay-01-pty` · `relay-02-tracker` (locked: L14 D4).
   Blind triangulation precedes locking the relay architecture (locked: L14 D7). These are
   relay-work constraints, not prerequisites for this document.
3. **Observation never depends on, or grants, delivery.** Discovery is not delivery authority.
   Future transmission requires checked target binding and explicit authority (locked: L17).
   Observations are evidence, never acceptance (said: PROJECT-DESIGN §3.7; VIST brief §Limits).
4. **Detaching never closes a bed** (locked: L14 D5). Process lifetime is ovitmugen's protected
   ownership, not any view's (locked: L17). `inferred: houston`: closing a view does not end a
   session either. That follows from L17's lifetime ownership and from the candidate principle "A
   viewer never owns lifetime" (said: PROJECT-DESIGN §3.2.x). It is not locked.
5. **Clients are independent; shared mechanisms sit at a narrow edge.**
   - locked: L17 — composition and ovitmugen are independently useful clients. Concrete
     shared-layer ownership/home/API remains open, and no common framework or transport is
     authorized by the Phase 0 build.
   - Termbrana must work with nabLarva absent (said: toolbox/termbrana/README.md §Product
     direction).
   - **Direction (said: majkee R9-1 N1):**
     - "I will take in advance nablarva as body with architecture - bricks can share
       process|api|cli|subscription layers and call generic methods".
     - "when particular tool is needed, than is no reason wake whole nablarva animal".
     - "UI should be coherent 'framework' not only group of worse findable bashes (-> aliases)
       and locked tmux-pane cages".
     - On L17's phrase: "No common framework - I meaned to use little original angle of sight:
       floating yes, chaotic not" (said: majkee R9-1 A).
   - **Tension, named and not resolved here:** the direction allows shared
     process/API/CLI/subscription layers and a coherent UI framework. L17 says shared mechanisms
     belong at a narrow integration boundary. A proposed L17 amendment is P5 in the lock
     proposals. **L17 holds unchanged** until a GO names P5.
6. **Room truth flows one way: journal → projections.** locked: L3 S1/S2 — the append-only
   single-writer journal is the sole room truth, and participant cursors are projections.
7. **Within the brick layer (candidate): control flows down a tree, information flows sideways
   through shared files, never brick to brick.** said: nablarva.v0 rules 1–2. Whether the tree is
   one animal-wide router or a pattern each organ repeats is open (§9, X5).

## 3. Principles carried as candidates

These come from nablarva.v0 (said: nablarva.v0, candidate). Majkee: "not insisting on exact
details where is a lot against philosophy" (said: majkee). Each principle holds only as far as the
cited locks allow. The middle column is a consistency reading (`inferred: houston`) against the
quoted lock text, not a claim that the lock states the principle.

| principle | consistent with (`inferred: houston`) | limit |
|---|---|---|
| Every state file has exactly one writer | L3 S1 "append-only single-writer journal" | nablarva.v0's own event log has many appenders (§9, X4) |
| Commands are imperative, events past tense | — | a naming grammar, not an event format (docket 8) |
| Optional parts fail soft | L17 "independently useful clients" · said: termbrana README "standalone operation with nabLarva completely absent" | — |
| Load cost follows use; edges are executables, insides load on first call | — | brick-layer only |
| Python computes, zsh acts | L17 (composition family: `composer.zsh` and adjacent Python stdlib; Python acceptance conditional on measured responsiveness) | does not decide docket 2 |

## 4. Seam ledger

One row per cross-organ seam. Cells point to their owning source, and the notes 4.x carry what a
cell cannot.
- **accepted** = qualified, or a locked design constraint
- **planned** = directed, not built or not qualified
- **open** = undecided

| seam | owner | consumers | governing | accepted | planned | open |
|---|---|---|---|---|---|---|
| **observe** | `unknown:` — termpanum is the observation **lab** by name (locked: L13, name only) | VIST candidates · views · humans | L13 · L14 D1 · L17 · said: majkee Q3 | read-only stance: never types or injects (said: PROJECT-DESIGN §3.6) | termpanum build plan, documentary first (said: X2 plan, uncommitted) · VIST contract | producer topology (said: cartan-x2 X2-1, "unspecified") · VIST ↔ termpanum overlap (4.1) |
| **compose** | Termbrana composition family (locked: L17) | humans · editors · pipes · assistant drafts | L17 · L8′ · L8/L13 (OUTPUT(A) boundary) | Phase 0: packet validation with opaque byte preservation incl. body EOL; grammar v4 (locked: L17; said: composer handoff) | generation-X sourcing — common programs/controllers, germline, vendor shapes/rosters, SPECIAL incl. germline/pipes — and preparation (said: termbrana README §Future adjustable sources) | loader, picker, renderer, native activation, editor target · OUTPUT(A) ↔ stridularium boundary note (4.2) |
| **deliver / write into a session** | `unknown:` — proposed: stridulatrix (said: PROJECT-DESIGN §3.7) | agents · humans | L3 S5 · L4 · L14 D1/D4/D7 · L17 | rejected mechanisms stay dead: send-keys injection, git-as-wire (locked: L4) | regulated adapter-owned PTY delivery (locked: L3 S5, unbuilt), after the relay research verdict (locked: L14 D4) | relay architecture, locked only after blind triangulation (locked: L14 D7) · doorbell mechanism, alternatives welcome (said: majkee R9-1 N3) · classifier · VIST actuator · human tmux/editor/pipe push qualification (4.3) |
| **view · layout · process lifetime** | ovitmugen for view/layout and protected process lifetime (locked: L17) | humans · phone · observer views | L17 · L14 D5 | detaching never closes a bed (locked: L14 D5) | — | collector process lifetime (said: cartan-x2 X2-3, "unspecified") · brick spawn/close vs ovitmugen (4.4) |
| **room truth** | the journal's single writer — the broker, named stridulatrix (name locked: L13; "L3 supplies the single-writer room journal" under stridulatrix, said: PROJECT-DESIGN §3.7) | all participants via cursors | L3 S1–S3, S8 | design constraints settled (locked: L3): single-writer journal · per-participant cursor projections · **private = in-ledger visibility boundary** (S3) · **room state on neutral ground** (S8) | journal, cursors | lifecycle `unknown: docket #4` · store `unknown: docket #5` · room topology `unknown: O3` · event vocabulary `unknown: docket #8` (4.5) |
| **human door** | stridularium (locked: L13) | the human | L14 D5/D6 · L8/L8′/L13 (OUTPUT(A) boundary) | thin lens; app-scoped reach; host-side engine (locked: L14 D5/D6) | `stridularium-00-design` (said: docs/organs/stridularium.md) | native terminal vs rendered cards (said: same) · OUTPUT(A) ↔ stridularium feed (4.2) |
| **cross-host** | — | stage 2 | L3 S7 · O2 | same protocol over SSH to one central broker (locked: L3 S7) | — | transport `unknown: O2` (lean recorded in flag Archived index; current practice tailnet + SSH, alternatives open — said: majkee R9-1 N9) |
| **checkout coordination** | muticula | cooperating teams | — | — | claim · work · hand over (said: PROJECT-DESIGN §3.5) | enforcement coverage (said: muticula-01 gate, pulse.md) |
| **context sourcing · reading** | `unknown:` — a controller/function under the eventual sourcing program (said: majkee G5, direction) | builders · verifiers · planners · Houston · Termbrana/IDE clients | L16 · said: majkee G4/G5 | reading schedule: preparation before RUNBOOK, recipient reading at entry, refresh on change (said: majkee, gavel deck STEP 5 "gaveled") | Nablarva Boost reader concept, typed source descriptors (said: boost brief, open design) | reader schema · program home/API · navigation surface (4.6) |
| **configuration · roles** | `unknown:` | the operator · projects · agents | said: majkee R9-1 N2 (direction) | — | a registry/config/settings layer (routes, project-local settings, key bindings) and a manageable app with admin/user/super-admin + agentive layer (said: majkee R9-1 N2) | the design, role model, schema, home and owner (4.8) |
| **key meanings** | this document, §5 | every organ's TUI | L16.9 · said: majkee G3 | KEYS CODE (accepted by majkee 2026-09-29) | — | keyboard / command-discovery design; palette ownership (said: keys brief) |
| **build · install · publication** | `unknown:` | the operator's hosts | L6 · L8′ · L12 · L17 | route as described: ia-sync source → reviewed `deploy.sh` → `~/.config/zsh/`, plus `install-pkgs` (said: PROJECT-DESIGN VOLATILE) | coherent build/install packages for nabLarva and its toolboxes (said: majkee Q5) | package shape; one vs several; any shared runtime mechanism (4.7) |

**4.1 Observe.**
- VIST is a shared observation principle and an intended protocol: conceptual boundaries first,
  then a concrete contract developed and qualified (said: majkee Q3).
- VIST names *observations*. Controller decisions and actuator actions stay separate components
  (said: majkee Q3; VIST brief §Where VIST sits).
- Antensor is an implementation candidate (said: majkee Q3). Its event envelope is proposed.
- Termpanum and VIST are siblings: termpanum reports inform VIST and can qualify candidate VIST
  updates, and producing evidence grants no admission (said: X2 RUNBOOK, as Majkee's direction).
- Majkee holds canon and gavel (locked: L16.1). The operational admission receiver is not
  appointed (said: X2 plan §5).
- The overlaps with termpanum (observe) and stridulatrix (deliver) stay visible here. No ownership
  is assigned (said: majkee Q3).
- nablarva.v0's "living tissue" (tmux and CLI hooks writing events) is a third candidate producer
  (said: nablarva.v0 §Layers).
- Organ-local records are allowed without animal-level compatibility (said: cartan-x2 X2-2).

**4.2 Compose.**
- Termbrana composition and ovitmugen are independently useful clients (locked: L17).
  Composition "does not require a session bed, editor, tmux or ovitmugen" (said: composer handoff,
  incorporation text; also termbrana README §Layering B).
- An architectural verb must not promote a planned capability into a dependency. Consumers depend
  only on the accepted column (said: composer handoff, cycle37 correction).
- Each generation-X sourcing category keeps its owner, consumer contract and acceptance, and a
  split needs named remaining gates (said: composer handoff). Adjustable sources do not imply
  generic YAML/TOML loading or instruction execution (said: same).
- Composer's architecture-owner proposal is attributed input to this row (said: majkee Q4). Its
  text is reproduced in the composer handoff at
  `nablarva@78059da:.dev/session/nablarva-X3-architecture-sitting/raw/handoff.composer-boundaries.cartan.2026-10-22.md`.
- **Retained boundary.**
  - L8′ moved the composer work's location and publication to or through ia-sync.
  - The OUTPUT(A) ↔ stridularium interface boundary remains as in L8/L13 (locked: L8′).
  - That interface is owned by one boundary note when both threads run (locked: L8). The note is
    pending, and this document defines no API for it.
  - L8 placed Cluster A mechanism (clipper/processor/composer) in `applications-in-common`
    (locked: L8), and L8′ supersedes that location "for this work", the composer work (locked:
    L8′). `inferred: houston`: the clipper and processor therefore keep L8's placement, because
    nothing supersedes it for them.
- Current editor target: Sublime, intended app-neutral (said: majkee G2). This is not an editor
  decision (`unknown: O4`).

**4.3 Deliver.**
- Editor/pipe/tmux push is a human-operated carrier outside L3/L4's regulated protocol until
  separately qualified. Assistant draft contribution grants no autonomous sending authority
  (locked: L17).
- Regulated delivery waits on the relay research verdict (locked: L14 D4). The relay
  architecture is locked only after blind triangulation (locked: L14 D7).
- Three candidates touch this seam, and none is accepted:
  - nablarva.v0's doorbell, typed with `tmux send-keys -l` and rung by a watcher (said:
    nablarva.v0 §Messages);
  - nablarva.v0's classifier, which routes output (said: nablarva.v0);
  - VIST's actuator (said: VIST brief).
- Majkee: "do not insist on exact solution by `tmux send-keys -l` if can be more alternatives"
  (said: majkee R9-1 N3). Alternatives are welcome, and the mechanism stays open.
- **Send-keys injection is a recorded death (locked: L4).** Qualification work alone cannot
  reopen it. Any claimed exception, for example a pointer-only nudge that carries no content,
  returns to Majkee with its evidence. No future gate may presume that exception.
- Tmux is never the protocol (locked: L3 S5). Open (§9, X1/X10).

**4.4 Lifetime.**
- Ovitmugen's protection is a constraint. It is neither extended to nor transferred to a newly
  appointed owner (said: cartan-x2 X2-3).
- A brick that spawns or closes panes (said: nablarva.v0 `pane-spawn`/`pane-close`) acts on this
  seam. Who may do so is open (§9, X8).

**4.5 Room truth.**
- Private is an in-ledger visibility boundary (locked: L3 S3). Room state lives on neutral ground
  (locked: L3 S8). This document chooses no roles, access-control scheme, schema or room topology
  for either (`unknown: O3`).
- Four candidate event envelopes exist, and none is chosen:
  - the nablarva.v0 record;
  - the VIST event model v0;
  - the termpanum EVENTS map v0.3;
  - the proposed `jev.event/v1` convergence.

  Source: `../.dev/research/termpanum-events/events-map.v0.2026-10-02.md`, "OPEN → majkee"
  (said). `unknown: docket #8`.

**4.6 Context sourcing.**
- One owned source should serve human/file readers and the intended deterministic engine. Pins
  are derived at acquisition, not handwritten (said: boost brief, proposal).
- A required prerequisite that exceeds a budget stays visible, never silently shortened (said: G5
  brief).
- A pin proves read bytes, not continued applicability (said: G5 brief).
- The existing any-seat read order (AGENTS → flag → pulse → PROJECT.yaml) is not waived by a
  selected profile (said: G5 brief, gaveled schedule).

**4.7 Build · install.**
- The direction is coherent build/install packages for nabLarva and its toolboxes, **while the
  independent client boundaries hold** (said: majkee Q5). Coherent packaging does not itself
  select one global router or a common runtime framework (said: majkee Q5).
- `inferred: houston`: there are two axes, run/use independence (L17) and build/install coherence
  (Q5), and both can hold. Whether build coherence implies any shared runtime mechanism is open. If
  it does, L17's narrow-edge rule applies.
- Majkee's later direction toward shared process/API/CLI/subscription layers and a coherent UI
  framework, and its tension with L17, are in §2 item 5 (said: majkee R9-1 N1; proposal P5).
- Promotion out of this repo is a reviewed merge, never auto-deploy (locked: L6).

**4.8 Configuration · roles.**
- Majkee: "need registry |config |setting layer to f.e. adjust routes, speciffic local project
  settings, key bindings... although started with this detil, in fact expecting managable app with
  admin|user|super admin| + agentive layer" (said: majkee R9-1 N2).
- This is recorded as direction only. This document chooses no role model, configuration schema,
  home or owner.
- Key *meanings* stay in §5. Configurable bindings would be a separate layer over them
  (`inferred: houston`).

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

**Beyond the grammar (open).** Relocating the accepted grammar does not settle the larger keyboard
and command-discovery design (said: keys brief, research and proposed directions). That design
covers tool-owned command truth, a derived catalogue, toolbox-attached palettes, and the effect
distinctions explain · insert · prepare · execute · request delivery. "An attached palette is not a
new sending authority" (said: keys brief). This is consistent with L17's
discovery-is-not-delivery rule.

### Reading aid — same word, different things

A reading aid, not an adopted glossary or a renaming (said: majkee Q6).

- **session gate** — the one acceptance condition of a session (`gate:` in its RUNBOOK and STATUS;
  locked: L16.2).
  **command gate** — in nablarva.v0's brick layer, a pipe's executable entry that checks input,
  resolves context and dispatches (said: nablarva.v0 §Glossary, candidate).
- **RUNBOOK document** — a session's stable intent, assignments and rules, read at entry. Current
  position lives in STATUS (said: G5 brief, gaveled schedule).
  **proposed executable step runner** — nablarva.v0's "runbook": a command file whose steps run in
  order and stop on failure (said: nablarva.v0, candidate).
- **program controller document** — a CONTROLLER.md indexing a program's functions. It is the
  candidate home for the context-sourcing procedure (said: G5 brief).
  **VIST controller** — the decision component between VIST observations and actuator actions
  (said: VIST brief; majkee Q3).

## 6. The ladder (L2)

Framing locked, stage content evolves (locked: L2).

- **Stage 1 — same host.** Every row of §4 is a stage-1 seam today, and the sessions plane is the
  workstation (locked: L14 D5). Relay work within stage 1 follows the research and triangulation
  constraints (locked: L14 D4/D7).
- **Stage 2 — different host.** Same protocol over SSH to one central broker (locked: L3 S7).
  Transport `unknown: O2`. Depends on rows room truth and deliver.
- **Stage 3 — stridularium.** The human's door (locked: L13), on the human-door row. Its
  room-dependent organ layer needs room truth and deliver (said: docs/organs/stridularium.md). Its
  feed carries the retained OUTPUT(A) boundary (4.2).

## 7. Organs and their homes

One line per organ (said: majkee G2 a). The home rule (said: majkee, gavel deck STEP 4):
- An organ that already has a home keeps it.
- A new body starts as a component folder with a thin `README.md` entry and grows chapters on
  need.
- The organ/toolbox taxonomy is under review.
- The parent directory for new folders is not chosen.

Reconciliation with the growth law (`inferred: houston`): a README-only folder is K5's folder
stage entered early, and K5's line → chapter growth continues inside it. Existing single-file
bodies are not migrated for symmetry.

Naming (said: majkee R9-1 N5): "biological terms are only descriptive organ, but inside code must
be held standard factory standard naming". This matches the naming law: "disk contract terse and
grep-able … the life-stage metaphor (larva · pupa · stridulation) is culture — keep it rich, keep
it off the machine surface" (said: AGENTS.md, Standing rules).

| organ | one line | home |
|---|---|---|
| **termbrana** | the terminal membrane: Zellij observer + composition family (locked: L17); composer work is its composition family (said: majkee G2) | observer `toolbox/termbrana/` with `DECISIONS.md` (locked: L11/L12) · composition `~/ia-sync/zsh/termbrana/` (locked: L17) |
| **ovitmugen** | tmux frame and session view manager (said: PROJECT-DESIGN §3.2); view/layout + protected process lifetime (locked: L17) | code `~/ia-sync/zsh/session/ovitmugen.*` (observed); whether `zsh/session/` stays its code home is open (said: majkee R9-1 N11) · body: interim in PROJECT-DESIGN §3.2 (said: majkee Q2); body home `unknown:` |
| **termpanum** | observation lab (locked: L13, name); the read-only ear (said: PROJECT-DESIGN §3.6) | proposed `toolbox/termpanum/` (said: PROJECT-DESIGN §3.6) — not created |
| **stridulatrix** | broker and CLI (locked: L13) | `unknown:` (said: PROJECT-DESIGN §3.7) · design `../meshup/room.brokered-journal.2026-07-31/` |
| **stridularium** | the phone app, the human's door (locked: L13) | body [`organs/stridularium.md`](organs/stridularium.md) · code home proposed `stridularium/{android,host}` (said: same) |
| **muticula** | file-backed concurrency coordination in one checkout (said: PROJECT-DESIGN §3.5) | `unknown:` |
| **instarmux** | `unknown:` organ or placeholder (PROJECT-DESIGN §3.3 empty) | `unknown:` |
| **reposoma (tool)** | `unknown:` organ or placeholder (PROJECT-DESIGN §3.4 empty) | `unknown:` |

Not organs; cited only:
- **VIST** — observation principle and intended protocol (said: majkee Q3).
- **Antensor** — implementation candidate.
- **Nablarva Boost** — open reader concept.
- **nablarva.v0** — candidate brick frame.

## 8. Decisions and reading

- **Where decisions live** (said: majkee, gavel deck STEP 5): locks in
  [flag.md](../.dev/session/flag.md); product-technical rationale in component ledgers, each entry
  citing its authorizing flag line **or session brief** (locked: L11 pattern, e.g.
  `../toolbox/termbrana/DECISIONS.md`). No root ADR series is opened.
- **The root stub** `decisions/README.md` still promises that gaveled items land there, which
  contradicts the line above. Its correction versus retirement is `unknown:` and not decided here.
- **Who reads what, when** (said: majkee, gavel deck STEP 5, "gaveled"):
  - Context is prepared before RUNBOOK authorship.
  - Each recipient reads again at entry.
  - The affected selection is refreshed on reassignment, scope or interface change, a changed
    governing source, a new constraint or a conflict.
  - Missing, ambiguous or oversized required context holds the affected action.
  - The procedure's survival as a controller/function is a promotion obligation. Its schema,
    program home and API are open.

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

**Docket and O-items** (flag §Pending gavel / §Open). The table shows where this document depends
on each item and its working default.
- **Working defaults** are Houston's leans, made labelled working defaults by majkee's R9-1 C
  answer "c1" (said: majkee).
- They are not gavels and can be overridden without ceremony.
- Docket 2 is excluded.
- O1 and O2 carry majkee's own words instead (said: majkee R9-1 N9). Every item stays open.

| item | depends here | working default (`inferred: houston`, per R9-1 c1) |
|---|---|---|
| docket 2 — v1 language | everywhere a language is named | **excluded** ("only majkee weighs") |
| docket 3 — git residual seat | — | none; stays open |
| docket 4 — broker lifecycle | room truth | no choice between pane and service. Either way the broker's lifetime is independent of every viewer, so it never runs as a pane inside the ovitmugen frame |
| docket 5 — journal store | room truth | NDJSON now, SQLite import path later, under L3 S1's single writer |
| docket 6 — V1 cut | all rows | none; stays open |
| docket 8 — discrete-state vocabulary | observe, room truth | not confirmed; first a bounded comparison of the four candidate envelopes (4.5) |
| O1 — hosting machine | — | said: majkee R9-1 N9: "office\|in case home" |
| O2 — cross-host transport | cross-host | said: majkee R9-1 N9: "now using tailnet with SSH but openned to alternatives, like pseudo\|local-server (later I can try to buy some virtual machine)" |
| O3 — room repo topology | room truth | none; stays open |
| O4 — monitor brick-set | — | none; Sublime is the current working target (said: majkee G2), not an editor choice |

**Relay research.** The `relay-00-research` verdict (locked: L14 D4) and the blind triangulation
before a relay-architecture lock (locked: L14 D7) are outstanding for relay work. They are not
prerequisites for this document.

**Collisions between nablarva.v0 and locked or newer state**, named and unresolved. Each row is
said: nablarva.v0, set against the cited locks. Detail is in the X3 arc, `raw/arc.r2.md` §3 (pin
owed at promotion).

| id | nablarva.v0 | meets |
|---|---|---|
| X1 | doorbell typed with `tmux send-keys -l` | L4 (recorded death) · L3 S5 · L17 — any exception returns to Majkee; alternatives welcome (§4.3) |
| X2 | compiled broker binary later | L4 (C++/Go clause) · docket 2 |
| X3 | watcher as a user service | docket 4 (lean: pane) |
| X4 | one event record, many appenders | docket 8 · four envelopes · one-writer rule |
| X5 | one `nabla <pipe> <verb>` router | L17 independent clients · majkee R9-1 N1 direction and proposal P5 (§2 item 5) |
| X6 | command `nabla`, `NABLA_*`, `~/nabla` | L13 (commands stay ASCII `nablarva`) · said: majkee R9-1 N10 "we should keep terminology" |
| X7 | Termbrana as a popup inside the tree | L17 (newer) |
| X8 | bricks spawn and close panes | L17 (ovitmugen lifetime) |
| X9 | CLI hook writes agent output into the bus | L14 D1 (vendor doors parked) |
| X10 | classifier routes output | L3 S4 · VIST controller |
| X11 | substrate at XDG paths | L3 S8 · O3 · docket 5 · said: majkee R9-1 N10 lean: a CLI tree `~/.nablarva` OR `<project>/.nablarva`; both open |
| X12–X13 | gate · runbook · status · pipe · controller | §5 reading aid |

**Cross-head items** (said: cartan-x2, confirmed):
- The observation producer topology is unspecified (X2-1).
- The collector lifetime owner is unspecified (X2-3).

**Other open items:**
- the root for new organ folders (G4)
- the reader schema, program home/API and root stub (G5)
- ovitmugen's body home (said: majkee Q2) and code home (said: majkee R9-1 N11)
- the build/install package shape (Q5)
- the shared layer's owner/home/API (L17), and majkee's one-body direction against it (R9-1 N1; P5)
- the configuration · roles design (R9-1 N2)
- the operational VIST admission receiver
- the OUTPUT(A) ↔ stridularium boundary note (L8)
- the per-project process vault home: `~/.nablarva` or `<project>/.nablarva` (said: majkee R9-1 N10, lean; both open)
- stridularium's name: "if we will use **stridulatrix** as broker, stridularium as phone app needs new name" (said: majkee R9-1 N4). L13 is a lock, and this document renames nothing.

## Sources and pins

Durable cites follow the commit-pin rule. These pins were verified at drafting:
- KEYS CODE acceptance: `nablarva@c630f0e8b1490e34458a52988342d679b24f2f5b:.dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md` :120.
- Sitting record and rulings: `nablarva@78059da:.dev/session/nablarva-X3-architecture-sitting/raw/{gavels.X4.2026-10-17.md,prompt.sitting.2026-10-17.md,brief.component-docs-and-nablarva-boost.2026-10-21.md,brief.nablarva-boost-reader-concept.2026-10-21.md,brief.adr-task-context.2026-10-21.md,brief.keys-command-discovery.2026-10-21.md,handoff.composer-boundaries.cartan.2026-10-22.md}`.
- VIST brief: `nablarva@78059da:.dev/session/nablarva-X4-vist/raw/vist-01-principle-and-applications.md`.
- Shelf law: `nablarva@2ae8636:.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md`.

**Pins owed before promotion.** These were uncommitted at drafting, so they are cited by sha256 or path only:
- Majkee's arc answers: `.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.pick-and-q1-q8.2026-10-22.md` (Message A = partial pick; Message B = shape B + Q1–Q8). It is absent from `78059da`.
- Majkee's R9-1 answers: `.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.r9-1-notes.2026-10-22.md` and `answers.majkee.r9-1-abc.2026-10-22.md`.
- nablarva.v0 (file Nabla-Tmux-Architecture-Draft-v0): .md `00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0`; zip `a7d28babe12277292f204fe6801d58b04087a3d3715068e1254b8683415e0ae7`.
- X2 `termpanum.build-plan.md`: `4e039f9f787c3224e8bb8c63342d3cdf68027339dd51ace682db89e430c83145`.
- X2 `disposition.x3-vectors.cartan.2026-10-22.md`: `efe7573d…68f7b`.
- X3 `arc.r2.md` and `arc.pick.2026-10-22.md`: Houston's own raw drafts.

A promoted document must not point into a prunable session folder without these pins.
