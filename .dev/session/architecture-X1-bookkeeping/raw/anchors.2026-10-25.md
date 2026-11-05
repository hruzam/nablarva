# Verified anchors — cartan-x1 — 2026-10-25

Clock: 2026-10-25 20:15:42 CET; baseline: `baseline.cartan.2026-10-25.json`.
Native roles available: implementer (gpt-5.6-terra/high), houston (gpt-6.1-sol/high), per current tool contracts and deployed role files. Main model/effort not independently exposed; operator-selected. Permission: workspace-write in Nablarva and /tmp; no staging. Presence beyond initial wake is unclear: UNMANNED until a live ruling.
All target diffs staged/unstaged empty. No execution bus existed. Protected foreign paths and index hash recorded in baseline. Four X0 copies equal pinned originals. Seven M4 payable blobs exist; v0 hashes match prior document. r7 equals f20dda5. No unresolved anchors.

## One row per edit ID

| ID | current anchors (original line numbers) | replacement / source |
|---|---|---|
| M3 | docs/ARCHITECTURE.md:3–3 | Exact quotations, replacements and verified sources below. |
| C1 | docs/ARCHITECTURE.md:92–104; docs/ARCHITECTURE.md:150–154; docs/ARCHITECTURE.md:159–160; docs/ARCHITECTURE.md:236–240; docs/ARCHITECTURE.md:343–343; docs/ARCHITECTURE.md:377–380; docs/ARCHITECTURE.md:439–439; docs/ARCHITECTURE.md:458–458 | Exact quotations, replacements and verified sources below. |
| M4 | docs/ARCHITECTURE.md:430–431; docs/ARCHITECTURE.md:473–481 | Exact quotations, replacements and verified sources below. |
| C4 | docs/ARCHITECTURE.md:381–382 | Exact quotations, replacements and verified sources below. |
| O1 | docs/ARCHITECTURE.md:366–366 | Exact quotations, replacements and verified sources below. |
| O2 | docs/ARCHITECTURE.md:367–367; docs/ARCHITECTURE.md:368–368 | Exact quotations, replacements and verified sources below. |
| O3 | docs/ARCHITECTURE.md:364–364; docs/ARCHITECTURE.md:463–463 | Exact quotations, replacements and verified sources below. |
| O4 | docs/ARCHITECTURE.md:370–372 | Exact quotations, replacements and verified sources below. |
| S1 | docs/ARCHITECTURE.md:138–138; docs/ARCHITECTURE.md:165–165; docs/ARCHITECTURE.md:189–189 | Exact quotations, replacements and verified sources below. |
| S2 | docs/ARCHITECTURE.md:136–136; docs/ARCHITECTURE.md:163–163; docs/ARCHITECTURE.md:374–374; docs/ARCHITECTURE.md:457–457 | Exact quotations, replacements and verified sources below. |
| S3 | docs/ARCHITECTURE.md:145–145; docs/ARCHITECTURE.md:247–248; docs/ARCHITECTURE.md:445–445; docs/ARCHITECTURE.md:462–462 | Exact quotations, replacements and verified sources below. |
| P1 | PROJECT-DESIGN.md:237–237 | Exact quotations, replacements and verified sources below. |
| P2 | PROJECT-DESIGN.md:282–282 | Exact quotations, replacements and verified sources below. |
| C2 | toolbox/termbrana/README.md:165–168 | Exact quotations, replacements and verified sources below. |

## M3

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:3–3`

Current:
```text
`checked: 2026-10-22` · `state: DRAFT r7 for majkee GO — not promoted; promotion target docs/ARCHITECTURE.md (L16.9)`
```
Replacement:
```text
`checked: 2026-10-25` · `state: r8 bookkeeping candidate · promoted r7 at f20dda5 · 2026-10-25 · awaiting majkee GO`
```
Source: M3; git show f20dda5:docs/ARCHITECTURE.md equals baseline; clock 2026-10-25 20:15:42 CET

## C1

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:92–104`

Current:
```text
5. **Clients are independent; shared mechanisms sit at a narrow edge.** locked: L17 — composition
   and ovitmugen are independently useful clients. Concrete shared-layer ownership/home/API remains
   open, and no common framework or transport is authorized by the Phase 0 build. Termbrana must
   work with nabLarva absent (said: toolbox/termbrana/README.md §Product direction).
   **Direction (said: majkee R9-1 N1):** "I will take in advance nablarva as body with
   architecture - bricks can share process|api|cli|subscription layers and call generic methods";
   "when particular tool is needed, than is no reason wake whole nablarva animal"; "UI should be
   coherent 'framework' not only group of worse findable bashes (-> aliases) and locked tmux-pane
   cages". On L17's phrase: "No common framework - I meaned to use little original angle of sight:
   floating yes, chaotic not" (said: majkee R9-1 A). **The tension is named and left unresolved
   here.** The direction allows shared process/API/CLI/subscription layers and a coherent UI
   framework. L17 places shared mechanisms at a narrow integration boundary. P5 in the lock
   proposals offers a reading (P5-a) or an amendment (P5-b). L17 holds unchanged until a GO names one of them.
```
Replacement:
```text
5. **One body; independently useful clients.** Composition and ovitmugen remain independently
   useful clients (locked: L17). See flag L21, adopted P5-b 2026-10-23: bricks may share
   process/API/CLI/subscription layers and generic methods, with a coherent UI framework —
   floating, not chaotic. The Phase 0 build authorizes no shared-layer, framework or transport
   implementation; designing them is architectural work, and implementation, activation,
   delivery or transport adoption needs its own separate release (locked: L21).
   Termbrana must work with nabLarva absent (said: toolbox/termbrana/README.md §Product direction).
```
Source: flag L17 retained clause; L21 exact two replacement clauses

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:150–154`

Current:
```text
- VIST is a shared observation principle and an intended protocol: conceptual boundaries come
  first, then a concrete contract is developed and qualified (said: majkee Q3).
- VIST names *observations*. Controller decisions and actuator actions stay separate components
  (said: majkee Q3; VIST brief §Where VIST sits).
- Antensor is an implementation candidate (said: majkee Q3). Its event envelope is proposed.
```
Replacement:
```text
- VIST is a shared observation principle and an intended protocol: conceptual boundaries come
  first, then a concrete contract is developed and qualified (locked: L20).
- VIST names *observations*. Controller decisions and actuator actions stay separate components
  with separate authority (locked: L20).
- Antensor is an implementation candidate; the event envelope is proposed, not adopted (locked: L20).
```
Source: flag L20

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:159–160`

Current:
```text
- The overlaps with termpanum (observe) and stridulatrix (deliver) stay visible here; no ownership
  is assigned (said: majkee Q3).
```
Replacement:
```text
- The overlaps with termpanum (observe) and stridulatrix (deliver) stay visible and unassigned
  (locked: L20).
```
Source: flag L20

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:236–240`

Current:
```text
- `inferred: houston`: there are two axes, run/use independence (L17) and build/install coherence
  (Q5), and both can hold. Whether build coherence implies any shared runtime mechanism is open. If
  it does, L17's narrow-edge rule applies.
- Majkee's later one-body direction (shared process/API/CLI/subscription layers, a coherent UI
  framework) and its tension with L17 are in §2 item 5 (said: majkee R9-1 N1; proposal P5).
```
Replacement:
```text
- `inferred: houston`: there are two axes, run/use independence (L17) and build/install coherence
  (Q5), and both can hold. Whether build coherence implies any shared runtime mechanism is open.
  The shared-layer direction and its separate implementation release are now governed by
  flag L21 (adopted P5-b, 2026-10-23); see §2 item 5.
```
Source: flag L21; existing inference retained with stale rule removed

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:343–343`

Current:
```text
One line per organ (said: majkee G2 a). The home rule (said: majkee, gavel deck STEP 4):
```
Replacement:
```text
One line per organ (said: majkee G2 a). The home rule (locked: L18):
```
Source: flag L18 enumerates next four bullets and folder-growth explanation

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:377–380`

Current:
```text
- **Where decisions live** (said: majkee, gavel deck STEP 5): locks in
  [flag.md](../.dev/session/flag.md); product-technical rationale in component ledgers, each entry
  citing its authorizing flag line **or session brief** (locked: L11 pattern, e.g.
  `../toolbox/termbrana/DECISIONS.md`). No root ADR series is opened.
```
Replacement:
```text
- **Where decisions live** (locked: L19): locks in
  [flag.md](../.dev/session/flag.md); product-technical rationale in component ledgers, each entry
  citing its authorizing flag line **or session brief** (L11 pattern, e.g.
  `../toolbox/termbrana/DECISIONS.md`). No root ADR series is opened.
```
Source: flag L19

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:439–439`

Current:
```text
| X5 | one `nabla <pipe> <verb>` router | L17 independent clients · majkee R9-1 N1 direction and proposal P5 (§2 item 5) |
```
Replacement:
```text
| X5 | one `nabla <pipe> <verb>` router | L17 independent clients · flag L21 (adopted P5-b, 2026-10-23); a concrete router remains open (§2 item 5) |
```
Source: flag L21 does not select router

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:458–458`

Current:
```text
- majkee's one-body direction against L17's narrow edge (R9-1 N1; proposal P5)
```
Replacement:
```text
- concrete shared-layer design under L21 (P5-b adopted 2026-10-23; §2 item 5)
```
Source: flag L21

## M4

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:430–431`

Current:
```text
is said: nablarva.v0 against the cited locks. Detail is in the X3 arc, `raw/arc.r2.md` §3 (pin owed at
promotion).
```
Replacement:
```text
is said: nablarva.v0 against the cited locks. Detail is in the X3 arc,
`nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/arc.r2.md` §3.
```
Source: baseline payable blob checks

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:473–481`

Current:
```text
**Pins owed before promotion.** These were uncommitted at drafting and are cited by sha256 or path only:
- Majkee's arc answers: `.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.pick-and-q1-q8.2026-10-22.md` (Message A = partial pick; Message B = shape B + Q1–Q8). It is absent from `78059da`.
- Majkee's R9-1 answers: `.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.r9-1-notes.2026-10-22.md` and `answers.majkee.r9-1-abc.2026-10-22.md`.
- nablarva.v0 (file Nabla-Tmux-Architecture-Draft-v0): .md `00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0`; zip `a7d28babe12277292f204fe6801d58b04087a3d3715068e1254b8683415e0ae7`.
- X2 `termpanum.build-plan.md`: `4e039f9f787c3224e8bb8c63342d3cdf68027339dd51ace682db89e430c83145`.
- X2 `disposition.x3-vectors.cartan.2026-10-22.md`: `efe7573d…68f7b`.
- X3 `arc.r2.md` and `arc.pick.2026-10-22.md`: Houston's own raw drafts.

A promoted document must not point into a prunable session folder without these pins.
```
Replacement:
```text
**Pins paid in r8.** These X3 sources, uncommitted at r7 drafting, are verified at `519a211`:
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.pick-and-q1-q8.2026-10-22.md` · sha256 `46ad7c56ea703e49738996954b8602f8f4f3079cc0a3319be84766aab7ad216d`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.r9-1-notes.2026-10-22.md` · sha256 `7ed5dd59be4c554a613ea4d5d29ecbe5c212da62390b7a0ae06e175e51902994`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.r9-1-abc.2026-10-22.md` · sha256 `2032f27e26b1730a3b0607ee6c485942a2281e866d1d42661130e86d2bb3336e`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/arc.r2.md` · sha256 `7ca22a3b5cc20239c66339acd386bba86ecb113c30746bca56356cd165d81eb5`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/arc.pick.2026-10-22.md` · sha256 `da40442fde7bb2726ced75f3b029655bf70ef2352919c2c0139ebb0d70dd2b22`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.md` · sha256 `00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.zip` · sha256 `a7d28babe12277292f204fe6801d58b04087a3d3715068e1254b8683415e0ae7`.

**X0 ruling sources.** Verified at `1ceceee`; X0-n means the deck block and X0 organs §n the organ walk:
- `nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md`.
- `nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/consult.d1-observation-record.houston.2026-10-24.md`.
- `nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.organs.2026-10-24.md`.
- `nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/decision-package.r2.oraculum.2026-10-24.md`.

**Pins owed — X2 head.** These remain path/hash citations pending that head's preservation commit:
- X2 `termpanum.build-plan.md`: `4e039f9f787c3224e8bb8c63342d3cdf68027339dd51ace682db89e430c83145`.
- X2 `disposition.x3-vectors.cartan.2026-10-22.md`: `efe7573d…68f7b`.

The two X2 pins remain an explicit preservation debt; no pin is inferred from file presence.
```
Source: seven payable blobs checked with git cat-file -e/show; four X0 copies byte-compared; X2 debt retained

## C4

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:381–382`

Current:
```text
- **The root stub** `decisions/README.md` still promises that gaveled items land there, which
  contradicts the line above. Its correction versus retirement is `unknown:` and not decided here.
```
Replacement:
```text
- **The stub under docs/** `decisions/README.md` still promises that gaveled items land there,
  which contradicts the line above. Its correction versus retirement is `unknown:` and not decided here.
```
Source: actual docs/decisions/README.md; L19 leaves disposition open

## O1

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:366–366`

Current:
```text
| **instarmux** | `unknown:` organ or placeholder (PROJECT-DESIGN §3.3 empty) | `unknown:` |
```
Replacement:
```text
| **instarmux** | the skin — UI only if zsh + tmux + the simplified way are not enough; Slint a candidate under it (said: majkee, 2026-10-24, X0 organs §7; deck X0-6) | `unknown:` |
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.organs.2026-10-24.md §7–8; nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-6

## O2

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:367–367`

Current:
```text
| **reposoma (tool)** | `unknown:` organ or placeholder (PROJECT-DESIGN §3.4 empty) | `unknown:` |
```
Replacement:
```text
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.organs.2026-10-24.md §7–8

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:368–368`

Current:
```text

```
Replacement:
```text

reposoma is an older RAG project; `~/reposoma/` is the pre-RAG common store, not an organ (said: majkee, 2026-10-24, X0 organs §8).

```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.organs.2026-10-24.md §7–8

## O3

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:364–364`

Current:
```text
| **stridularium** | the phone app, the human's door (locked: L13) | body [`organs/stridularium.md`](organs/stridularium.md) · code home proposed `stridularium/{android,host}` (said: same) |
```
Replacement:
```text
| **stridularium** | the phone app, the human's door (locked: L13); cultural retirement requested (said: majkee, 2026-10-24, X0 organs §5–6); body and lock L13 unchanged; new name pending | body [`organs/stridularium.md`](organs/stridularium.md) · code home proposed `stridularium/{android,host}` (said: same) |
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.organs.2026-10-24.md §5–6; flag L13

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:463–463`

Current:
```text
- stridularium's name: "if we will use **stridulatrix** as broker, stridularium as phone app needs new name" (said: majkee R9-1 N4). L13 is a lock; this document renames nothing.
```
Replacement:
```text
- stridularium: cultural retirement requested (said: majkee, 2026-10-24, X0 organs §5–6); body and lock L13 unchanged; new name pending. This document renames nothing.
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.organs.2026-10-24.md §5–6

## O4

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:370–372`

Current:
```text
- **VIST** — observation principle and intended protocol (said: majkee Q3).
- **Antensor** — implementation candidate.
- **Nablarva Boost** — open reader concept.
```
Replacement:
```text
- **VIST** — observation principle and intended protocol (locked: L20); protocol name only,
  not an organ (said: majkee, 2026-10-24, X0 organs §9).
- **Antensor** — implementation candidate: translator of important termpanum outputs to the body
  (said: majkee, 2026-10-24, X0 organs §9).
- **Nablarva Boost** — open reader concept; working name, rename pending (Laravel Boost collision;
  said: majkee, 2026-10-24, X0 organs §9).
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.organs.2026-10-24.md §9; flag L20

## S1

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:138–138`

Current:
```text
| **deliver / write into a session** | `unknown:` — proposed: stridulatrix (said: PROJECT-DESIGN §3.7) | agents · humans | L3 S5 · L4 · L14 D1/D4/D7 · L17 | rejected mechanisms stay dead: send-keys injection, git-as-wire (locked: L4) | regulated adapter-owned PTY delivery (locked: L3 S5, unbuilt), after the relay research verdict (locked: L14 D4) | relay architecture, locked only after blind triangulation (locked: L14 D7) · doorbell mechanism, alternatives welcome (said: majkee R9-1 N3) · classifier · VIST actuator · human tmux/editor/pipe push qualification (4.3) |
```
Replacement:
```text
| **deliver / write into a session** | stridulatrix — working split (said: majkee, 2026-10-24, architecture-X0 deck X0-2) | agents · humans | L3 S5 · L4 · L14 D1/D4/D7 · L17 | rejected mechanisms stay dead: send-keys injection, git-as-wire (locked: L4) | regulated adapter-owned PTY delivery (locked: L3 S5, unbuilt), after the relay research verdict (locked: L14 D4) | relay architecture, locked only after blind triangulation (locked: L14 D7) · doorbell mechanism, alternatives welcome (said: majkee R9-1 N3) · classifier · VIST actuator · human tmux/editor/pipe push qualification (4.3) |
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-2

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:165–165`

Current:
```text
**4.2 Compose.**
```
Replacement:
```text
**4.2 Compose.**
- Working split (said: majkee, 2026-10-24, architecture-X0 deck X0-2): termbrana composes
  and submits, ending at a packet file in the bus; stridulatrix sends. Termbrana never writes
  into a session, and stridulatrix never composes. This is planned, not a delivery release.
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-2; organs §4–5

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:189–189`

Current:
```text
**4.3 Deliver.**
```
Replacement:
```text
**4.3 Deliver.**
- Working split (said: majkee, 2026-10-24, architecture-X0 deck X0-2): stridulatrix owns sending,
  the room journal, cursors, adapters, receipts and the process/API boundary; the traffic view
  is a journal projection. L3 supplies the single-writer journal and adapter constraints.
  Stridulatrix requests a pane; ovitmugen performs the lifetime action under L17. These planned
  responsibilities release no delivery or spawning mechanism.
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-2; organs §4–5; L3/L17 constraints

## S2

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:136–136`

Current:
```text
| **observe** | `unknown:` — termpanum is the observation **lab** by name (locked: L13, name only) | VIST candidates · views · humans | L13 · L14 D1 · L17 · said: majkee Q3 | read-only stance: never types or injects (said: PROJECT-DESIGN §3.6) | termpanum build plan, documentary first (said: X2 plan, uncommitted) · VIST contract | producer topology (said: cartan-x2 X2-1, "unspecified") · VIST ↔ termpanum overlap (4.1) |
```
Replacement:
```text
| **observe** | seam owner `unknown:`; shared-substrate component has interim steward X5 head (§4.1); termpanum is the observation **lab** by name (locked: L13, name only) | VIST candidates · views · humans | L13 · L14 D1 · L17 · L20 · said: majkee, 2026-10-24, architecture-X0 deck X0-3 | read-only stance: never types or injects (said: PROJECT-DESIGN §3.6) | termpanum build plan, documentary first (said: X2 plan, uncommitted) · VIST contract · shared-substrate component (§4.1) | producer topology (said: cartan-x2 X2-1, "unspecified") · VIST ↔ termpanum overlap (4.1) |
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-3; consult constraints

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:163–163`

Current:
```text
- Organ-local records are allowed without animal-level compatibility (said: cartan-x2 X2-2).
```
Replacement:
```text
- Organ-local records are allowed without animal-level compatibility (said: cartan-x2 X2-2).
- The address registry and shared observation record form a planned shared-substrate component,
  independent of any organ's liveness; lab records remain separate. Its interim steward is the
  X5 head (U-steward); the permanent owner is open (said: majkee, 2026-10-24, architecture-X0
  deck X0-3). It is not owned by ovitmugen, termpanum or stridulatrix.
- Five constraints accompany that design (`inferred: houston`, consult 2026-10-24):
  1. Each file has one serialized writing process; split per instance or serialize the writes.
  2. Admit the cross-organ owner gap: X5's steward is interim; shared-layer implementation needs
     its own release under L21 (2), and L20's overlaps stay unassigned.
  3. Timestamp merging is a reader-side stage-1 view, not truth or total order; no envelope is
     adopted, docket 8 stays open, and the rule does not extend across hosts.
  4. The observation record never becomes room truth or delivery authority; a room fact enters
     through the journal's single writer. No reader acts on it to deliver, close a pane or admit.
  5. CLI hooks are optional vendor-feature producers writing their own observation files; hook
     → bus stays parked. Building or running a producer needs a separate release.
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-3; nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/consult.d1-observation-record.houston.2026-10-24.md five constraints

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:374–374`

Current:
```text

```
Replacement:
```text

Planned shared-substrate component: address registry + shared observation record (§4.1), own thin
folder per L18; disk name after the X5 P1 duplicate/cross-interference sweep. Interim steward:
X5 head (U-steward), permanent owner open (said: majkee, 2026-10-24, architecture-X0 deck X0-3).

```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-3; flag L18; RUNBOOK S2

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:457–457`

Current:
```text
- the shared layer's owner/home/API (L17)
```
Replacement:
```text
- the shared layer's permanent owner and API; interim steward = X5 head (U-steward, §4.1), config-resolved home in §4.8
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-3/4; existing open item narrowed

## S3

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:145–145`

Current:
```text
| **configuration · roles** | `unknown:` | the operator · projects · agents | said: majkee R9-1 N2 (direction) | — | a registry/config/settings layer (routes, project-local settings, key bindings) and a manageable app with admin/user/super-admin + agentive layer (said: majkee R9-1 N2) | design, role model, schema, home and owner (4.8) |
```
Replacement:
```text
| **configuration · roles** | `unknown:` | the operator · projects · agents | said: majkee R9-1 N2; 2026-10-24, architecture-X0 deck X0-4 | — | a registry/config/settings layer (routes, project-local settings, key bindings) and a manageable app with admin/user/super-admin + agentive layer (said: majkee R9-1 N2); substrate homes and config rule (§4.8) | design, role model, schema and owner (4.8) |
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-4

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:247–248`

Current:
```text
- This is recorded as direction only. This document chooses no role model, configuration schema,
  home or owner.
```
Replacement:
```text
- Substrate home (said: majkee, 2026-10-24, architecture-X0 deck X0-4; X0 organs §1):
  `<project>/.nablarva/` for project-scoped state (address registry, observation-record segments,
  bed-local settings), plus `~/.nablarva/` for machine defaults. Layout and config rule travel
  together: no path in a script; resolve paths from nabLarva settings.
- The configuration mechanism, role model, schema and owner remain open. This home direction
  neither chooses the room store/topology nor releases implementation.
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-4; organs §1

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:445–445`

Current:
```text
| X11 | substrate at XDG paths | L3 S8 · O3 · docket 5 · said: majkee R9-1 N10 lean: a CLI tree `~/.nablarva` OR `<project>/.nablarva`; both open |
```
Replacement:
```text
| X11 | substrate at XDG paths | superseded working direction: project state `<project>/.nablarva/` + machine defaults `~/.nablarva/`, via settings (said: majkee, 2026-10-24, architecture-X0 deck X0-4; §4.8); L3 S8, O3 and docket 5 remain |
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-4

`/home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md:462–462`

Current:
```text
- the per-project process vault home, `~/.nablarva` or `<project>/.nablarva` (said: majkee R9-1 N10, lean; both open)
```
Replacement:
```text
- the configuration mechanism for the selected substrate homes (§4.8; said: majkee, 2026-10-24, architecture-X0 deck X0-4)
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.deck.2026-10-24.md X0-4

## P1

`/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md:237–237`

Current:
```text
## 3.4. reposoma *(tool, not `~/reposoma` - this is substrate)*
```
Replacement:
```text
3.4. reposoma — removed from the organ list; see [ARCHITECTURE §7](docs/ARCHITECTURE.md#7-organs-and-their-homes).
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.organs.2026-10-24.md §7–8; tombstone keeps section numbering without organ heading

## P2

`/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md:282–282`

Current:
```text
## 3.8. stridularium *(phone app)*
```
Replacement:
```text
## 3.8. stridularium *(phone app — cultural retirement requested by majkee 2026-10-24; new name pending)*
```
Source: nablarva@1ceceee:.dev/session/architecture-X0-spine-and-skin/raw/answers.majkee.organs.2026-10-24.md §5–6

## C2

`/home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/README.md:165–168`

Current:
```text
**Layering B — L17:** Termbrana composition and ovitmugen are independently useful
clients. Any common mechanism is prospective and belongs at a narrow integration
edge with demonstrated consumers, not a framework built by this phase. Composition
works without ovitmugen, a RUNBOOK bed, tmux, editor or interactive shell. Ovitmugen
```
Replacement:
```text
**Layering B — L17, amended by L21:** Termbrana composition and ovitmugen are independently useful
clients. See [flag L21](../../.dev/session/flag.md), adopted P5-b 2026-10-23, for shared layers
and a coherent UI framework; implementing, activating, delivering through or adopting a transport
for them needs its own separate release. Composition
works without ovitmugen, a RUNBOOK bed, tmux, editor or interactive shell. Ovitmugen
```
Source: flag L21 replaces narrow edge/framework phrases; retained L17 independent clients

## M4 verification inventory

- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.pick-and-q1-q8.2026-10-22.md` · sha256 `46ad7c56ea703e49738996954b8602f8f4f3079cc0a3319be84766aab7ad216d`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.r9-1-notes.2026-10-22.md` · sha256 `7ed5dd59be4c554a613ea4d5d29ecbe5c212da62390b7a0ae06e175e51902994`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.r9-1-abc.2026-10-22.md` · sha256 `2032f27e26b1730a3b0607ee6c485942a2281e866d1d42661130e86d2bb3336e`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/arc.r2.md` · sha256 `7ca22a3b5cc20239c66339acd386bba86ecb113c30746bca56356cd165d81eb5`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/arc.pick.2026-10-22.md` · sha256 `da40442fde7bb2726ced75f3b029655bf70ef2352919c2c0139ebb0d70dd2b22`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.md` · sha256 `00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0`.
- `nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.zip` · sha256 `a7d28babe12277292f204fe6801d58b04087a3d3715068e1254b8683415e0ae7`.

Each git cat-file -e and git show succeeded. See baseline JSON for full X0 SHA-256 evidence and target before-hashes. X2 pins intentionally owed.
