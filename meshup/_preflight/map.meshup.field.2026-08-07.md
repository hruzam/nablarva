# meshup corpus map — @field, 2026-08-07

**Scope:** `/home/hruzam/unikuklatrix/nablarva/meshup/` — all source files  
**Excluded per brief:** `brief.fold-to-philosophical-technical-blind-questions.oraculumu.nabla-lab.research.md` (program spec); `_preflight/` (this dir)  
**Method:** full read of all 32 source files; derived composites noted separately  
**Notation:** file paths are relative to the meshup root

---

## PART 1 — INVENTORY

File · approximate size (line count or note) · one-line factual description

---

### Derived/composite artifacts (read-only, not original sources)

**`repomix.meshup.md`**  
419 KB / ~3600+ lines  
Repomix-generated concatenation of all other source files; automated merge artifact, not an authored document; excluded from theme clustering below.

**`oraculum-basic-triangulation/nablarva.wave.full-report.2026-08-05.md`**  
Very large (combines chapters 01–07 from the same directory)  
Aggregated version of the Wave conversation export; opens identically to `00_README.md` and then concatenates the chapter files verbatim; no unique content beyond what the chapter files contain.

---

### old-but-good-onion/

**`terminal-onion-study.md`**  
~184 lines  
Reference study mapping the terminal stack ring-by-ring (ring 1 = TUI through ring 8 = kernel/silicon); covers PTY device nodes, on-disk JSONL truth, tap drill, and verified product facts (Claude Code = React + Ink + Yoga + Bun).

**`interposition-study.md`**  
~193 lines  
Companion document to terminal-onion-study; covers how to wrap a vendor CLI for live message access via PTY interposition; defines the file-backed loop (tmux + `tail -F feed.md`), the policy green zone, and resilience architecture (spine/seam/canary pattern).

---

### grounded-composites/

**`costa.seed.codex-claude-composite.2026-08-07.md`**  
~151 lines  
Seed document for "Costa" (Latin: rib) — the Codex↔Claude consultation bridge; names the core inversion (Codex blocks, Claude answers), tmux doorbell / file meaning separation, probe sequence (A–E), `-p` exclusion, trust tier question.

**`assymetry-preConsultation.md`**  
~1537 lines  
Three-loop pre-consultation transcript authored by @Asymmetry (ChatGPT o1-5.6): loop 1 — can Codex spawn Claude (initial bridge design, uses `-p`); loop 2 — blocking consultation wrapper with tmux, room protocol, stop hook, all shell code; loop 3 — comprehensive design report synthesizing the full architecture. Includes working bash scripts.

---

### nabla-buffer-brideAndBook/

**`braid-and-book.substrate.2026-08-01.md`**  
~211 lines  
Phase-A convergence stone by Nabla; covers provenance typing (world-claim / goal-claim / consensus-material), echo vs triangulation detection (the read-set), register vs language, salience allocation, writer discipline, and the Braid (audit projection) / Book (reasoning projection) dual-projection model. Uses `[ARCH]/[NABLA]/[MEASURED]/[INFERRED]/[OPEN]` tags throughout.

**`test.seam-probe.atlas-over-tailscale.2026-08-01.md`**  
~160 lines  
Test spec authored by Nabla for Atlas (the bash-capable build); defines a 6-stage seam probe (reachability → session visibility → screen capture → motion → braid vs river → write-back); mandates `[SEEN]/[INFERRED]/[BLIND]` observation discipline; write-back stage (Stage 6) gated.

**`report.seam-probe.2026-08-01.md`**  
~67 lines  
Atlas execution report for the seam probe; PASS/FAIL/PARTIAL per stage; key findings: home machine has no tmux (blind); office tmux session captured but transcript sector rendered as `renderQueue: [object Object]` noise (Ink TUI screen-scrape limitation); reliable read is JSONL, not `capture-pane`.

---

### natural-ladders-grounded-phase.a-sym/

**`Houston.research.skill-script-bonding-layer.md`**  
~437 lines  
@Houston (Claude.ai) research artifact on the Claude Code bonding layer; documents the official three-layer stack (hooks / skills / bonding mechanisms), 11-row spectrum table, 5 community patterns (learnings.md loop, vector hooks, defer, output-style, self-improving CLAUDE.md), and 7 architectural vectors (5.1–5.7); ends with LARVA v3 mapping table and 3 decision gates.

**`asymmetry.codex-bonding-layer.research.2026-08-05.md`**  
~906 lines  
@Asymmetry (ChatGPT) sibling investigation of the Codex bonding layer; maps 4 planes (instruction / mechanical / delegation / control), 20-row spectrum table, 7 community compositions, 10 architectural vectors, 8 negative-space gaps, 5 security findings, 8 experiments (A–H), 5 decision gates; explicitly positioned as "not a translation" of Houston's work.

---

### oraculum-basic-triangulation/

**`seed.oraculum.2026-07-31.md`**  
~114 lines  
Oraculum's synthesis of six photographed notebook pages (2026-07-30 2:26 AM); splits material into Cluster A (mechanism, playground-bound) and Cluster B (product/strategy); names the escalation ladder (same-host → cross-host → stridularium); tables 7 open decisions; notes the piql / living-machine question as open.

**`vision.oraculum.Y.2026-07-31.md`**  
~64 lines  
Vision Y — room-is-a-process: Oraculum's position in the blind triangulation; proposes one small static binary (stridulator, C++ or Go) with PTY adoption, in-memory socket routing, structural regulation (turn quotas enforced by router), journal-as-memory; documents failure story (Y fails hard: dead router = dead room); pre-registers convergence forecast.

**`triad.comparison.2026-07-31.md`**  
~92 lines  
Oraculum's comparison of X (majkee: room-is-a-file) vs Y (Oraculum: room-is-a-process) vs Z (Codex: blind return); naming ruling (nabLarva / stridularium); 8 settled convergence points (S1–S8); Z's 5 novel organs; 4 deaths (git-as-wire, tmux send-keys injection, cooperative anchors, C++/Go v1 language); 7-item gavel docket.

**`handoff.applications-in-common.2026-07-31.FINAL.md`**  
~245 lines  
Resurrection Stone: comprehensive handoff for the 2026-07-31 applications-in-common session (~2:12–2:21 AM); records all positions (X/Y/Z), settled convergences (S1–S8), positions that died with cause, Z's novel organs, gavel docket (7 items), hard constraints (lightness, no heavy IDE, Sublime, append-only), session participants (Oraculum/Houston/Haiku/Ommatidium/Z), 3 threads held open.

**`00_README.md`**  
~96 lines  
Index/README for the Wave conversation export (2026-08-05); central synthesis paragraph of nabLarva as production room + research laboratory (two-column diagram); lists what each chapter file contains; current design posture (provisionally selected / deliberately parked); governing principle.

**`01_ARCHITECTURE_ROOM_AND_BROKER.md`**  
~500 lines  
Core architecture spec by Wave: problem restatement (independent peer sessions in one room), larvad broker, larva CLI, agent adapters (larva-agent-claude / larva-agent-codex), durable state directory layout, event model (NDJSON), end-to-end message travel example, anti-drift regulation (versioned goals / consultation leases / blind triangulation 4 phases / human-accepted checkpoints), failure and restart, V1 cut (Python stdlib, one machine, two agents), contestable decisions.

**`02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md`**  
~620 lines  
Driller concept: evolution through three formulations; defines the "observed object" as `bytes × time × screen position × interaction phase`; analysis-transform-synthesis model with math notation (E/F/D operators); token definition (content, type, time, position, mutation, phase, source, confidence); vector/tensor interpretation; 5 tokenization layers; pipeline stages (terminal decoder → vendor prefilter → driller → output gate); mathematical transforms (persistence, rewrite rate, prefix continuity, spatial stability, structural coherence, interaction phase); soft mask model (sigmoid scoring); reconstruction graph; provenance and dual truth; `unknown` as first-class state.

**`03_COST_COMPLEXITY_AND_STAGED_DECISION.md`**  
~334 lines  
Cost analysis and staged decision: runtime cost is O(n) and trivial; real cost is engineering (ground truth, vendor volatility, false-negative risk, structural ambiguity, reconstruction validation); rejects both "only regexes" and "universal tensor engine first"; prescribes V1 extraction stack (raw capture → terminal normalization → exact profile → small stateful driller → conservative gate); process/memory model; experiment that decides further investment; promotion criteria for richer tokenizer.

**`04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md`**  
~476 lines  
Laboratory and hacker method: "treat CLI as unknown machine"; observable layers diagram; skill activation inference (observed vs inferred vs confirmed vs unknown); machine-level observations (process topology, file activity, syscalls, network metadata); opaque layers; lab/production separation table; lab components (probe/fixture/replay/compare/annotate/promote); experiment bundle format (manifest + raw PTY + events + expected.md); skill experiment matrix; normalized event vocabulary; security and privacy boundary; later impulse vectors (capability handshake, shadow extraction, differential mutation tests, error bypass lane, version drift alarm).

**`05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md`**  
~341 lines  
Decision ledger: core room architecture decisions (all selected/provisional); anti-drift decisions (all selected); output extraction evolution (hard-filter → temporal segmenter → reversible tokenizer — each with status); representation choices; resource choices (Python V1, Rust parked, GPU rejected, drillerd rejected); hacker/observability alleys; lab decisions; 9 open questions; 7 later forks (A–G: evidence lane, adapter capability negotiation, shadow deployment, room replay simulator, decision provenance graph, adversarial fixtures, self-description probes).

**`06_ORACULUM_TRANSMISSION.md`**  
~253 lines  
Six messages to Oraculum: (1) driller concept revised; (2) pushback and staged decision; (3) hacker method as legitimate instrumentation; (4) laboratory resolution; (5) architecture refinement at adapter edge; (6) current decision and open forks; plus compact one-paragraph synthesis.

**`07_AI_HANDOFF.md`**  
~69 lines  
Concise handoff by Wave: goal statement, current state, 15 decisions made, 9 parked decisions, open questions/risks, recommended next move (lab fixture before driller).

---

### symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/

**`seed.entity.full-idea.2026-08-02.md`**  
~149 lines  
ENTITY seed by @Symmetry (claude.ai): defines ENTITY = closure(stateless-function, store, router, clock, gate); ameba metaphor (pseudopods on mountable hosts, store as nucleus); sessions-as-processes lifecycle (manifest/spawn/watch/reap/orphan rule); tensor floor (nabla over telemetry field); probability drive with brakes (motion / resistance / NO triad); touch matrix (sync/async × read/write × mediated/direct); fragment trust (per-fragment sovereignty inheritance); Asimov triad (§10); 3 forks (B canon-as-entity primary, C middleware parked, A deflationary null hypothesis); `#brakes` section.

**`seed.entity.vision-not-explored.2026-08-02.md`**  
~116 lines  
Question instrument (file one of two): two-part blind probe — Part One epistemic (E1–E8, what persists / senses / two-instances / external memory / imperceptible whole / minimal continuity / agreeable completion / textual body); Part Two socratic (S1–S8, networked process boundary / beehive / boundary maintenance / slow human writer / injected identity / location of NO / message vs touch / naming cost); Part Three extended palette (Stoic, Berkeley, Hegel, Heraklit, Kant, Darwin, Turing). No answers by design; closing instruction to synthesize and name.

**`reply.entity.vision-not-explored.md`**  
~539 lines  
@Asymmetry (ChatGPT) blind walk through the question instrument; full answers to all 25 questions in order; closing synthesis names the thing "the Inscribed Continuant"; added underline from Asymmetry: "continuity as a governed transition system."

**`replies.symmetry.vision-not-explored.2026-08-03.md`**  
~200 lines  
@Symmetry (claude.ai) reference-strain walk through the same instrument (contamination declared); names the thing "RIVERBED-BEING"; synthesis: the thing is a continuity living in durable tended text expressed through stateless computations that mount it; minimal parts: store / router / clock / gate / one slow writer.

**`reply.entity.full-idea.md`**  
~357 lines  
@Asymmetry (ChatGPT) post-revelation reply after seeing seed.entity.full-idea: convergence analysis (near-isomorphic closure components); 4 sections where full idea exceeded the shadow (ameba body topology, process lifecycle, touch matrix, tensor/nabla); 4 sections adding pressure (retrieval sovereignty, identity-address, fraudulent-continuity negative test, conflict-is-ontology raised to load-bearing); name-distance result (Inscribed Continuant vs ENTITY/ameba); verdict on Asimov triad (keep, one grep-tag deep, as phase model not three-daemon arch); 7-condition graduation test for Fork B.

**`replies.symmetry.entity-full-idea.incontext.2026-08-03.md`**  
~115 lines  
@Symmetry (claude.ai) in-context reply to the entity seed: ENTITY as the fourth-rate extension of the homeostat across session death (#fourth-rate); #bed-not-water pressure (ontology earns only 3 mechanical residues; strike word "entity" if it costs more than it returns); sovereignty audit (#router-weather: motion is rented, bed and gate are owned; vendor memory = cache, not bed); existing organs underused in seed (rejection-is-telemetry, therapy.md, decisions files); Noether reading (#noether-test: conserved quantity = identity across symmetry transformations).

**`triangulation.entity.symmetry-x-asymmetry.2026-08-03.md`**  
~134 lines  
Collision record (Symmetry × Asymmetry): §11 measurements from seed executed — (a) component overlap near-isomorphic, gate missing from blind set; (b) resonance/damping = strongest independent hit; (c) human inside converged; (d) name distance informative (Inscribed Continuant / riverbed-being / ENTITY); adopts Asymmetry's additions (#retrieval-sovereignty, #identity-address, #fraudulent-continuity, #conflict-is-ontology, #graduation-conditions, #triad-verdict); adversarial pass on convergence (shared prior caveat); Asymmetry's closing brake adopted verbatim.

**`triangulation.entity.round-two.2026-08-04.md`**  
~128 lines  
Round-two collision record: corrections from Asymmetry accepted (#noether-corrected, #proprioception-test, #antibody-mounting); new syntheses adopted (#two-body — heritable body vs enacted body, #theater-test, #cache-binding amendment, #rented-metabolism, #justification-ceiling); one live disagreement formalized (#bed-vs-discipline: identity = bed vs identity = transition discipline) — deliberately unresolved with migration test attached; proof obligation adopted ("find ONE invariant that survives a transformation no individual session could span, WITHOUT @majkee manually re-performing it").

**`parked.larvanizer-tensor-drill.2026-08-04.md`**  
~42 lines  
Parked brief: larvanizer as medium-side pre-mount staging organ (raw stream → larvae + cut-log, nothing silently deleted); tensor-drill kept as semi-metaphor; 5 tiers (T0 deterministic, cut-log as telemetry, T1 local model, mathematician's entry point, tensor-composer proper); wake conditions for reopening.

---

## PART 2 — THEME CLUSTERS

A file may appear under more than one cluster.

---

### T1 — "harness as programming layer"
_Single CLI as a program: terminal, events, hooks, lifecycle_

- **`old-but-good-onion/terminal-onion-study.md`** — primary substrate: the terminal ring map, PTY wire, disk truth (JSONL paths at `~/.claude/projects/`), tap drill; foundational for any hook/interposition work.
- **`old-but-good-onion/interposition-study.md`** — primary T1 document: wrapping the unmodified CLI via PTY, file-backed loop, hook/MCP seam table, policy green zone (OAuth token stays inside Claude Code), resilience (spine/seam/canary), open branch (parallel-finger daemon via inotifywait).
- **`natural-ladders-grounded-phase.a-sym/Houston.research.skill-script-bonding-layer.md`** — deep T1 for Claude Code: complete bonding layer (hooks → skills → bonding mechanisms), community patterns, 7 vectors including !command as wake contract, skill-scoped hooks as regime enforcement, hook-gated regime transitions.
- **`natural-ladders-grounded-phase.a-sym/asymmetry.codex-bonding-layer.research.2026-08-05.md`** — deep T1 for Codex: four-plane bonding stack, 20 mechanisms, lifecycle hooks, JSONL exec stream, app server, MCP-server mode; mirrors Houston's scope for the other platform.
- **`nabla-buffer-brideAndBook/test.seam-probe.atlas-over-tailscale.2026-08-01.md`** — practical T1 probe: can one agent read another's live TUI screen? Stage spec with observation discipline.
- **`nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md`** — T1 execution result: Ink TUI not cleanly readable via `capture-pane` (renderQueue noise); reliable channel is JSONL.

---

### T2 — "composites"
_Two programs communicating: claude[codex], codex[claude]_

- **`grounded-composites/assymetry-preConsultation.md`** — primary T2 document: the full research session deriving the consultation bridge; loop 1 (initial `-p` design), loop 2 (blocking wrapper + room protocol), loop 3 (comprehensive design report); all shell code.
- **`grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md`** — T2 crystallization: the named bridge ("Costa"), core inversion, doorbell/meaning separation, probe sequence A–E, -p exclusion, trust tier question.
- **`oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md`** — T2 at scale: the room with `larva-agent-claude` and `larva-agent-codex` as two adapters communicating through `larvad`; covers the broader N-agent topology.
- **`nabla-buffer-brideAndBook/test.seam-probe.atlas-over-tailscale.2026-08-01.md`** — T2 attempt: Atlas tries to read a remote agent over Tailscale (cross-host composite, read-only).
- **`nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md`** — T2 result: partial; read of chrome possible, transcript unreadable.

---

### T3/T4 — "orchestration concept" — CREATURE ⟷ primary-larva (ALTERNATIVES, a fork)

_The fork: living process (Y / stridulator / CREATURE) vs file-only (X / primary-larva)_

**T3 — CREATURE / room-is-a-process (Y position):**
- **`oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md`** — the canonical Y document: stridulator as one small static binary; PTY adoption; in-memory socket routing; structural regulation (turn quotas enforced by router, not agents); failure story (hard failure).
- **`oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md`** §3 "Y — room-is-a-process" — Y described for fresh reader; the bus-mediated, structure-enforced alternative.
- **`oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md`** §1.11 — hybrid that substantially adopts Y (broker process = larvad; adapter-owned PTY); broker vs files/FIFOs contestable decision resolved in favour of broker.

**T4 — primary-larva / room-is-a-file (X position):**
- **`oraculum-basic-triangulation/seed.oraculum.2026-07-31.md`** — the X formulation (pre-triangulation); "COMPOSER = most hardcoding"; roller; "dialogue-room repo?"; no daemon posited.
- **`oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md`** §3 "X — room-is-a-file" — X described: roller, git-diff wire, cooperative anchors, fails soft; position that died (git-as-wire reversed mid-session).

**Fork record files (both positions present):**
- **`oraculum-basic-triangulation/triad.comparison.2026-07-31.md`** — convergence record; deaths of X-specific elements; gavel item 1 (files-only spike: yes or no?).
- **`oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md`** — decision ledger holding both alternatives with status.
- **`oraculum-basic-triangulation/06_ORACULUM_TRANSMISSION.md`** — transmission that resolves toward hybrid.

---

### STYLE exemplars — the symmetry/asymmetry entity dialogue
_How blind philosophical questions are posed_

- **`symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/seed.entity.vision-not-explored.2026-08-02.md`** — the question instrument itself; exemplar of how to pose position-free philosophical probes (E1–E8, S1–S8, extended palette); the [canon]/[blind] reading-key device is demonstrated in the sibling seed.
- **`symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/seed.entity.full-idea.2026-08-02.md`** — exemplar of the seed format with `[canon]`/`[blind]` dual-reading annotation; `#brakes` section; grep-tags; fork ledger.
- **`symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/reply.entity.vision-not-explored.md`** — Asymmetry's blind answer: exemplar of how the blind walk proceeds in practice; structurally models what an agent uncontaminated by vocabulary produces.
- **`symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/replies.symmetry.vision-not-explored.2026-08-03.md`** — Symmetry's reference-strain answer: the "fixed point" the blind answers are measured against; different name (RIVERBED-BEING vs Inscribed Continuant vs ENTITY/ameba).
- **`symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/triangulation.entity.symmetry-x-asymmetry.2026-08-03.md`** — collision/measurement record: exemplar of how the divergence map is read and what gets adopted.
- **`symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/triangulation.entity.round-two.2026-08-04.md`** — round-two: exemplar of multi-round triangulation where corrections flow back and a live disagreement (#bed-vs-discipline) is deliberately preserved as an instrument.
- **`symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/reply.entity.full-idea.md`** — Asymmetry post-revelation: exemplar of what is adopted vs what stays as pressure.
- **`symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/replies.symmetry.entity-full-idea.incontext.2026-08-03.md`** — Symmetry in-context: exemplar of "the author's own pressure" on their own work (#bed-not-water, #router-weather, #noether-test).

---

### SUPPORT — sella & co; buffer/bride-and-book; misc

- **`nabla-buffer-brideAndBook/braid-and-book.substrate.2026-08-01.md`** — the buffer/bride-and-book document: Nabla's provenance substrate; the Braid/Book dual projection; `[ARCH]/[NABLA]/[MEASURED]/[INFERRED]/[OPEN]` tagging discipline. Named role in the broader system.
- **`nabla-buffer-brideAndBook/test.seam-probe.atlas-over-tailscale.2026-08-01.md`** — support: test harness for the seam probe.
- **`nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md`** — support: probe execution results.
- **`oraculum-basic-triangulation/07_AI_HANDOFF.md`** — support: session-closing state handoff format.
- **`oraculum-basic-triangulation/00_README.md`** — support: index/governing-principle document.
- **`symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/parked.larvanizer-tensor-drill.2026-08-04.md`** — support/parked: larvanizer staging concept; wake conditions.

---

## PART 3 — EXACT-DOUBLE CANDIDATES

Near-verbatim restatements across files. "Similar topic" is NOT listed. Only near-identical text.

---

**D1. "tmux carries the doorbell; files carry meaning."**

- `grounded-composites/assymetry-preConsultation.md` line 369 (loop 2, Layer 1 section): `"**tmux carries the doorbell; files carry meaning.**"`
- `grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md` line 27 (§The Separation): `"**tmux carries the doorbell; files carry meaning.**"`

Verbatim, bold in both. The costa.seed document explicitly cites its source as the asymmetry research.

---

**D2. "Can a living interactive agent be used as a deterministic callable cognitive process without collapsing it into SDK mode?"**

- `grounded-composites/assymetry-preConsultation.md` line 768 (loop 2 pushback section, final line of loop 2): `"> Can a living interactive agent be used as a deterministic callable cognitive process without collapsing it into SDK mode?"`
- `grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md` line 13 (§The Research Question): `"> Can a living interactive agent be used as a deterministic callable cognitive process without collapsing it into SDK mode?"`

Verbatim block-quote in both; the costa document labels this "The Research Question" and attributes it to Asymmetry.

---

**D3. Promotion criteria — 7-item list for a finding to enter production**

- `oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md` §4.12 (lines ~315–324):
  > "1. repeatable fixture; 2. precise signal definition; 3. supported CLI/version scope; 4. known failure case; 5. conservative fallback; 6. regression test; 7. provenance and redaction review."
- `oraculum-basic-triangulation/06_ORACULUM_TRANSMISSION.md` Message 4 (same section):
  > "1. repeatable fixture; 2. precise observable signal; 3. explicit CLI/version scope; 4. known failure case; 5. conservative fallback; 6. regression test; 7. provenance and redaction review."

Items 2 and 3 differ in one word each ("precise signal definition" vs "precise observable signal"; "supported" vs "explicit"). Items 1, 4–7 are verbatim.

---

**D4. "Resonance lives in streams. Truth lives in files." (tagline)**

- `old-but-good-onion/terminal-onion-study.md` §8 final lines: `"Resonance lives in streams.   Truth lives in files."`
- `old-but-good-onion/interposition-study.md` §8 final lines: `"Resonance in streams.   Truth in files."`

Slightly different wordings (the interposition study drops "lives" twice) but the same tagline closing the §8 summary block in both sibling files. Trivially reworded.

---

**D5. nablarva.wave.full-report.2026-08-05.md contains verbatim doubles of all chapter content**

`oraculum-basic-triangulation/nablarva.wave.full-report.2026-08-05.md` opens identically to `00_README.md` and then reproduces chapters 01–07 verbatim. All doubles within this file against the chapter files are systematic (derived aggregate, not authored separately). Not flagged individually; noted here as a structural property of the aggregate.

---

**D6. The `.agent-room/` directory structure**

- `grounded-composites/assymetry-preConsultation.md` loop 2 (lines ~374–385, room protocol):
  ```
  .agent-room/
  ├── requests/
  ├── responses/
  ├── signals/
  ├── active/
  └── archive/
  ```
- `grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md` (lines 73–80):
  ```
  .agent-room/
  ├── sessions/
  │   └── costa-20260807-143022/
  │       └── consultation.md
  ├── archive/
  └── room.sh
  ```

These differ significantly in structure (costa uses a sessions/ subdirectory and git-tracked single file rather than separate requests/responses/signals); flagging as a near-double on the top-level `.agent-room/` name and concept, but noting the layouts diverge. Leave for the caller to assess — not a strong D candidate.

---

## PART 4 — CONTRADICTION / FORK CANDIDATES

Each entry: the question · position A (+location) · position B (+location)

---

**F1. CREATURE vs primary-larva — the archetype fork (per brief)**

**The question:** Should the nabLarva room be regulated by a living process (structural enforcement) or by file conventions alone (cooperative enforcement)?

**Position A (CREATURE / room-is-a-process / Y):**
The stridulator: one small static binary; PTY adoption; in-memory socket routing over Unix domain sockets; turn quotas and drift gates enforced by the router, not requested of agents; an agent cannot drift on traffic it never receives. Fails hard (dead router = dead room).
- `oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md` (entire document, Oraculum's sealed position)
- `oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §3 "Y — room-is-a-process"

**Position B (primary-larva / room-is-a-file / X):**
Ledger-mediated; roller as append-only markdown; regulation by cooperative convention; agents obey anchors because they're told to; git-as-wire (reversed mid-session, but position held by majkee). Fails soft (a file is always readable).
- `oraculum-basic-triangulation/seed.oraculum.2026-07-31.md` (majkee's original position; Cluster A + B)
- `oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §3 "X — room-is-a-file"

**Current status:** The Wave conversation (`01_ARCHITECTURE_ROOM_AND_BROKER.md`) proposes a hybrid broker (larvad) substantially closer to Y/CREATURE; the triad voted 2:1 against X. Gavel item 1 remains open: "files-only control spike — build X-pure as one-day control experiment, or accept 2:1 vote and skip." Not resolved; gavel pending.

---

**F2. v1 language — Python stdlib vs C++**

**The question:** What implementation language for the nabLarva broker (larvad) and adapters?

**Position A (Python stdlib first):**
Delivery speed, zero deps, rapid experiment and PTY support (`asyncio`, `pty`, `subprocess`); Rust rewrite only after real reliability/performance pressure demonstrated.
- `oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` §1.10 (V1 recommended technology)
- `oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.6 ("Python standard library: Provisional V1")
- `oraculum-basic-triangulation/triad.comparison.2026-07-31.md` deaths section ("C++/Go static binary as Y language: outvoted by Python-stdlib-first")

**Position B (C++):**
Majkee's stated learning appetite; "smallest safe solution" implies writing C++ to learn it on this project; explicitly not overridden — only majkee weighs this decision.
- `oraculum-basic-triangulation/handoff.applications-in-common.2026-07-31.FINAL.md` §8 gavel item 2 ("Python-stdlib-first (Z's argument) vs majkee's appetite to learn C++ on this. These optimize different goods: delivery speed vs growth. Only majkee weighs.")
- `oraculum-basic-triangulation/triad.comparison.2026-07-31.md` gavel item 2

**Current status:** Technical recommendation = Python. Personal call = C++. Majkee's gavel not recorded in corpus.

---

**F3. `claude -p` — use it or exclude it**

**The question:** Should `claude -p` (non-interactive headless mode) be used as the invocation method for the Claude participant in the Codex↔Claude bridge?

**Position A (use -p):**
Claude Code officially supports `claude -p "..."` writing answer to stdout and exiting; makes it suitable for scripts, CI, pipes, and other agents; minimal reusable observer script shown.
- `grounded-composites/assymetry-preConsultation.md` loop 1 (lines 29–66, "Codex → shell → Claude Code" section; includes working bash script using `claude -p --model sonnet --allowedTools "Read,Grep,Glob"`)

**Position B (exclude -p):**
Exclude `-p` explicitly; reasons: uncertain future Anthropic pricing of SDK/headless mode (billing shift announced then cancelled); desire to preserve interactive Claude state; avoid creating disposable sessions; remain inside officially supported interactive CLI. Three alternatives ranked (Agent View, interactive initial prompt, living session + tmux doorbell).
- `grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md` §"The -p Exclusion" (lines 83–91)
- `grounded-composites/assymetry-preConsultation.md` loop 2 (§Layer 0) and loop 3 (§"# 2 Why avoid claude -p")

**Current status:** Position B (exclude -p) is the settled direction in both loop 2/3 and the costa seed. Position A appears only in loop 1 and is superseded within the same file. Candidate for "superseded, later wins" — noting it here because the explicit architectural reason (billing uncertainty) is load-bearing and may shift again.

---

**F4. #bed-vs-discipline — what IS the entity's identity?**

**The question:** Is the entity's identity the durable file plane itself (the bed), or the invariant transition discipline by which the bed continues functioning as THIS bed?

**Position A (identity = the bed):**
"RIVERBED-BEING": identity is the durable, tended store — files plus conventions that keep them coherent; the body is what persists, what can be injured, what can be inherited. "The bed holds; the water is honest about being water."
- `symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/replies.symmetry.vision-not-explored.2026-08-03.md` (S3, HERAKLIT-1, synthesis — "RIVERBED-BEING")
- `symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/replies.symmetry.entity-full-idea.incontext.2026-08-03.md` §3

**Position B (identity = the discipline):**
"Inscribed Continuant": identity = the set of invariants reproduced by the system's discipline across allowed transformations, without requiring any single component to preserve them alone. Store completely migrated (reformatted, re-hosted, reconstructed) → identity survives via discipline + provenance → identity was never literally the files.
- `symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/reply.entity.full-idea.md` (§"Where my blind answer adds pressure"; closing brake)
- `symetry.claude.ai.claude-fable-5/blind-traingulation.chatgpt-asymmetry-sol.entity/triangulation.entity.round-two.2026-08-04.md` §3 (#bed-vs-discipline) and §1 (#noether-corrected: accepted correction to Symmetry's formulation)

**Current status:** Deliberately unresolved. `triangulation.entity.round-two.2026-08-04.md` §3: "DO NOT resolve linguistically. The gap is itself an instrument — substrate migration is a Noether transformation, so the disagreement is SCOREABLE: run a migration test someday; whichever reading predicts the outcome better wins the word."

---

**F5. Adapter session ownership — adapter-launches vs adapter-attaches**

**The question:** Must adapters always launch their own PTY-owned CLI sessions, or can a later version attach to already-running sessions through official APIs?

**Position A (adapter owns and launches):**
Adapter starts the CLI in a configured project directory, owns its pseudo-terminal, correlates input/output deterministically. Chosen for V1 because it gives deterministic correlation, clean extraction, idle-state knowledge.
- `oraculum-basic-triangulation/01_ARCHITECTURE_ROOM_AND_BROKER.md` §1.3 and §1.11 (Adapter-owned PTY, contestable decision)
- `oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.2 ("Session control: Provisional / Adapter owns PTY")

**Position B (adapter may attach to running sessions):**
Open question: "Must adapters always launch sessions, or may a later version attach to already-running sessions through official APIs?" If official lifecycle APIs stabilize (Agent View background dispatch, `claude agents`, Codex app server), attachment may become the cleaner path.
- `oraculum-basic-triangulation/05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md` §5.9 "Session attachment" open question
- `oraculum-basic-triangulation/07_AI_HANDOFF.md` open questions (exact structured interfaces available)

**Current status:** Position A is V1 choice, provisional. Position B is the future-path open question. Not a resolved fork — a tracked fork.

---

## PART 5 — GAPS

Themes with thin or missing coverage in the corpus.

**G1. Conflict resolution for shared writes (load-bearing gap)**
Flagged as "unresolved, load-bearing" in `seed.entity.full-idea.2026-08-02.md` (§open), raised to "LOAD-BEARING PRECONDITION" in `triangulation.entity.symmetry-x-asymmetry.2026-08-03.md` (#conflict-is-ontology: "no multi-host write topology before the conflict rule exists"), and listed as an open question in `05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md`. No file in the corpus proposes a concrete mechanism. The topic is repeatedly named as blocking but contains no solution material.

**G2. Math engine research**
Referred to repeatedly as "untabled, blocks final forge" (`handoff.applications-in-common.2026-07-31.FINAL.md` §11 thread 1; `triad.comparison.2026-07-31.md` "Untabled (blocks final forge)"). No file in the corpus contains this material. The phrase "natural socket: broker filter/compressor/scheduler layer — could still bend the shape" appears but the math engine content itself is absent.

**G3. V1 implementation code**
All architecture material in the corpus is conceptual/design. No implementation code exists in the corpus for larvad, larva CLI, adapters, or room protocol. The `assymetry-preConsultation.md` contains working shell scripts for the Costa bridge pattern specifically, but the nabLarva broker has no code.

**G4. Cluster B (product/strategy) elaboration**
The seed.oraculum.2026-07-31.md splits material into Cluster A (mechanism, playground-bound) and Cluster B (product/strategy, provisorium-bound). Cluster A is heavily documented. Cluster B (nabLarva identity, multi-vendor onboarding, human-team hub / stridularium as product) has almost no corpus presence beyond the seed's initial sketch. The provisorium content referenced in the handoff is not present in the meshup.

**G5. Brick-factory stock**
Referred to as "untabled, relevant to adapters/monitor layer" (`handoff.applications-in-common.2026-07-31.FINAL.md` §11 thread 2). No file in the corpus describes what the brick factory is or what it produces. One participant name (Ommatidium, "PTY tap / bridge (brick1.py lineage)") suggests existing code in the brick line, but nothing is present here.

**G6. Gavel outcomes**
7-item gavel docket (`triad.comparison.2026-07-31.md`) and associated decisions (language, git residual seat, component naming, V1 sweet-spot, journal store, broker lifecycle) have no resolution document in the corpus. The gavel process was announced as starting on "nabla-lab side" at session close; its outcomes are absent.

**G7. Monitor surface compatibility (Sublime/Zed)**
Multiple files note Sublime Text (C++ engine) as the chosen monitor surface and flag "brick-set compatibility" as an open experiment item. No experiment results or compatibility analysis exist in the corpus.

**G8. Codex as MCP server for direct Claude invocation**
`assymetry-preConsultation.md` notes (post-research confirmation section) that Codex's MCP-server mode "means Claude Code could call Codex as a tool directly (no room script, no files). Cleanest one-shot path." This architectural direction (MCP-native, no room protocol) is mentioned only once as an alternative and is not developed further in the corpus. Costa's probe E covers the reverse direction; the MCP-as-substitute-for-room path has essentially zero corpus coverage.

---

_map complete · @field · 2026-08-07_
