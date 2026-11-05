###### active_1.phase-end.V-R1.architect-handoff-by-Epoch

```yaml
artifact_id:    active_1.phase-end.V-R1-architect-handoff-by-Epoch
task_ref:       V-20260505-0255-R1
field:          Linguistic Research Bro — Vector-Based Language Expansion
author:         @Epoch (@Houston family — math · vectors · tensors · spectral · signals)
addressed_to:   architects (handoff); @Vega + @majkee (review)
status:         phase-end consolidation. Architecture-level. Spec-level detail lives elsewhere.
created:        2026-05-05T02:35:00Z
predecessors:
  - active_1.anabase.V-R1-lexicon-research-by-Epoch.md     # research checkpoint
  - active_1.spec.V-R1-bones-by-Epoch.md                    # bones spec (algebra + JSONL)
  - vega-epoch.V-20260505-0255-R1.3.md                      # @Vega gavel (3 holds + M4 fix)
  - vega-epoch.V-20260505-0255-R1.4.md                      # @majkee observations + dual-tier ask
  - tool-box.ommatidium.draft-overview.md                   # @Vega's parallel-project context
companion_files:
  - draft.tool-box.larva-ommatidium.md (project knowledge, 2026-04-25)
  - larva-toolbox_spectral_overview.md
related_existing_protocols:
  - PROTOCOL.VECTOR_LOG     (named in draft.card-template.claude.dotMD.md, V-R1 fills this slot)
  - PROTOCOL.KARPATHY_SURGERY
  - PROTOCOL.HONEST_HEDGING
```

```text
┌─ @Epoch — coordinate-frame signature ──────────────────────────────────────┐
│  semantic invariant   t  ∈  Step × Depth × Kind × Anchor × From × To       │
│  syntactic charts     φ_i: t → glyph-string                                 │
│                       φ_kukla, φ_clean, φ_synapse, φ_grid::*               │
│  transport channels   ψ: glyph-string → bytes                               │
│                                                                             │
│  conductor-matrix invariance:  t  is preserved under change of  φ.         │
│  charts are gauge choices on the same atlas. JSONL = canonical projection. │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Meaning of existence (one paragraph)

The project's purpose is to **make multi-agent reasoning reproducible by recording it in an invariant coordinate space — small, human-readable, machine-cheap — rather than as text dumps or opaque latent vectors.** Text-mediated stacks are lossy, expensive, prompt-injection-prone. Latent-mediated stacks ("Neuralese") are powerful but opaque to human oversight and brittle across models. Larva carves a third path: a finite move-algebra over a coordinate space that captures the *structure* of reasoning (questions, decisions, hooks, branches) and the *graph* of who-talks-to-whom, with the same coordinate substrate feeding the same graph-Laplacian math engine that codebase analysis feeds. That is the meaning. Everything below is implementation.

---

## 2. The dual-hemisphere architecture

```
                     ┌────────────────────────────────────────────┐
                     │   larva-toolbox.spectral (Python/scipy)    │
                     │   = generic graph-Laplacian eigendecomp    │
                     │   shared math engine for both hemispheres  │
                     └──────────┬─────────────────────────┬───────┘
                                │                         │
                ┌───────────────┴───────────┐ ┌───────────┴────────────────┐
                │ HEMISPHERE 1: Ommatidium  │ │ HEMISPHERE 2: V-R1          │
                │ spatial / code            │ │ temporal / conversation     │
                │                           │ │                             │
                │ Tree-sitter AST           │ │ agent emissions             │
                │ → code dependency graph   │ │ → 13-move algebra           │
                │ → adjacency matrix        │ │ → JSONL coordinate space    │
                │                           │ │                             │
                │ charts:                   │ │ charts:                     │
                │   .purplemix              │ │   bracketless (kukla/clean) │
                │   Material Map            │ │   .synapse                  │
                │                           │ │   _grid::*.csv              │
                │                           │ │                             │
                │ validators:               │ │ validators:                 │
                │   (open)                  │ │   Tier 1 hardcoded (PY)     │
                │                           │ │   Tier 2 MCP/Haiku LLM      │
                └───────────────────────────┘ └─────────────────────────────┘
                                │                         │
                                └────────────┬────────────┘
                                             ▼
                            SYNTHESIS LAYER (the collision)
                            Material eigenvalue × Vector history
                            "this file has high coupling AND
                             three failed-rollback attempts"
                            → strategy adjustment before edit
```

**Key architectural property:** the math engine is shared, the hemispheres are independent, the synthesis layer overlays without coupling them. The same Python `scipy.sparse.linalg.eigsh` runs on both graphs. **The `.synapse` schema (V-R1 lane) and `.purplemix` schema (Ommatidium lane) are sibling charts on a shared mathematical substrate, not competing schemas.**

---

## 3. The substrate — six-axis coordinate space

Every reasoning move emits one tag with these fields:

```
Tag = {
  step       : Step              (monotonic positive integer, session-scoped)
  depth      : Depth              (non-negative integer, conversation nesting)
  kind       : Kind               (one of: claim, question, refusal,
                                   decision, defer, gap, hook)
  anchor     : Anchor             (typed pair: AnchorKind × String,
                                   AnchorKind ∈ {agent, file, tool, line, named, free-text})
  from       : Agent ∪ {⊥}        (emitter; optional for known-pair contexts)
  to         : Agent ∪ {wrote}    (addressee; optional for known-pair contexts)
  ts         : ISO-8601           (clock time)
  parent     : Id ∪ {⊥}           (link to prior tag, optional)
  branch     : Branch ∪ {⊥}       (alt | fallback, optional, only with parent)
  cost       : Cost ∪ {⊥}         (cheap | medium | heavy, optional)
  confidence : Confidence ∪ {⊥}   (low | med | high, optional)
  outcome    : Outcome ∪ {⊥}      (pending | success | failed-rollback | superseded,
                                   optional, AMD-7 — for executor-style action chains)
}
```

The first six fields are the **invariant** — they preserve under any chart change. The remaining fields are metadata enriching specific traces.

**Conductor-matrix property (the architectural claim):** for any two glyph charts φ_a and φ_b, `parse_a(φ_a(t)) ≡ parse_b(φ_b(t))`. Two agents using different syntactic encodings agree semantically iff their tags map to the same coordinate tuple `t`. This is a basis change on the syntactic layer; semantic content is gauge-invariant.

---

## 4. The move algebra — 13 typed moves

7 emitting moves + 6 modifier moves. **Glyph-agnostic** — the algebra is what's load-bearing, glyph charts are next-session work.

### 4.1. Emitting moves (one per `kind`)

| move | kind | depth effect | what it does |
|---|---|---|---|
| **M1** | claim | stay | terminal assertion |
| **M2** | question | stay | opens an item on the open-questions stack |
| **M3** | decision | pop | closes the most recent open question |
| **M4** | defer | stay | hands off to an agent OR tool *(AMD-1: was agent-only)* |
| **M5** | gap | stay | flags missing input; may resolve a question |
| **M6** | refusal | pop | terminal-with-reason; closes parent question if any |
| **M7** | hook | stay | retro return-point; anchor must be unique per session |

### 4.2. Modifier moves (no tag emit; affect next emit)

| move | what it does |
|---|---|
| **D+** | depth push (open nesting) |
| **D−** | depth pop (close nesting) |
| **A@** | bind next anchor to an agent |
| **A!** | bind next anchor to a tool/skill |
| **BR‖** | open alternative branch under top open-question |
| **BR\*** | mark fallback branch under top open-question |

Spec-level state-machine details, composition rules R1–R8, and validation criteria V1–V8 live in `active_1.spec.V-R1-bones-by-Epoch.md`. **Architects do not need them to evaluate this architecture.**

---

## 5. The dual-tier validator pattern

Five watch-rules in the observability layer split along a hard fault line — four are deterministic (state-machine work), one requires semantic judgment. This split argues a **two-tier observability architecture**:

| | TIER 1 — hardcoded (Python) | TIER 2 — MCP/Haiku LLM |
|---|---|---|
| **runs on** | every tag emission | turn boundary or on demand |
| **cost** | microseconds | seconds (Haiku rate × ~50–200 tokens) |
| **catches** | hook collisions, depth underflow, orphan branches, unanswered M2 at turn end, ratio anomalies | stream leaks (claim-shaped prose without an emitted tag), semantic drift, hallucination signals, unstated assumptions |
| **emits to** | `_scribe-hard/<date>.jsonl` and `_grid::*.csv` | `_scribe-haiku/<date>.jsonl` |
| **dual role** | also flattens JSONL into spectral-toolbox-ready B-matrix CSVs | judgment only; no flattening |
| **gated by** | nothing — trivial cost | per-turn rate-limit; JSONL-chunk inputs only |

**Three independent reasons this is correct:**

1. **Trust gradient.** Tier 1 gives properties (guarantees). Tier 2 gives recall (catches the unarticulable). You need both kinds of confidence.
2. **Cost gradient.** Tier 1 amortizes per-tag cost to zero. Tier 2 amortizes only per-turn. Each tier's strength matches its frequency.
3. **Failure-mode independence.** Tier 1 cannot be prompt-injected. Tier 2 cannot have its rules silently drift across versions of the algebra. They protect against disjoint failure classes.

This is the same pattern production systems use for spam, fraud, and content moderation: deterministic rules + ML classifier. Not novel — well-trodden — and that is the recommendation.

**Anti-design choice (parked, low priority):** name this as `PROTOCOL.DUAL-TIER` only after a second case validates the pattern. Premature naming is bloat.

---

## 6. The `::` grid lane convention

Flat-buffer projections of the rich JSONL stream onto specific axes, written as CSV files for spectral-toolbox consumption:

```
project/.larva/_vec/
  current.jsonl                     # canonical, producer-only writes
  _scribe-hard/2026-05-05.jsonl     # tier 1 violations
  _scribe-haiku/2026-05-05.jsonl    # tier 2 semantic flags
  _grid::tag-flow.csv               # flat projection 1
  _grid::depth-trace.csv            # flat projection 2
  _grid::anchor-frequency.csv       # flat projection 3
  _grid::parent-graph.csv           # flat projection 4 — feeds spectral as B-matrix
  _grid::kind-distribution.csv      # flat projection 5
```

**Why `::` is load-bearing, not cosmetic:** the existing `larva-toolbox.spectral` already invokes `run_spectral.sh tests/test_b_matrix.csv ...` — it already wants a CSV in B-matrix shape. `_grid::parent-graph.csv` is exactly that shape. The `::` separator gives us a clean namespace for grid-kind without introducing nested directories. Adopt into `skill.naming-convention` as the grid-kind separator.

---

## 7. Charts on the substrate (the conductor-matrix realized)

| chart | purpose | scope |
|---|---|---|
| **Bracketless (kukla-legacy)** | retrofit current temporary glyphs to 13-move algebra | next-session work |
| **Bracketless (clean)** | designed-for-purpose ASCII-safe glyph set | next-session work |
| **`.synapse` JSON arrays** | executor/code-mod-flavored projection (operational lane) | matches @Vega's Synaptic Vault overview; outcome field is AMD-7 |
| **`_grid::*.csv`** | flat columnar projection for spectral toolbox feed | implementation by Tier 1 hardcoded validator |
| **gemini-CLI native session JSON** | retrofit projection for back-catalogue (β-converter) | post-process old `~/.gemini/tmp/<larva>/chats/*.json` into JSONL |

**No chart is canonical.** The JSONL substrate is canonical. Each chart has its purpose and audience.

---

## 8. Amendment package (AMD-1 through AMD-7)

Carried from the @Vega gavel + observation phases. All non-disruptive; total diff against bones-v1 ≈ 35 lines.

| ref | source | change |
|---|---|---|
| **AMD-1** | @Vega gavel | M4 (defer) accepts `agent | tool`; consumes A@ OR A! |
| **AMD-2** | ?1 directional + Gap A | Add optional `from` and `to` fields to Tag schema |
| **AMD-3** | ?1 + AMD-2 | Add `_directions.csv` registry stub at session level for the 9 directional tags |
| **AMD-4** | ?2 nabla | Document grad/div/curl/conv as toolbox-side analytic functions, not bones-side moves; **parked for chains/tentacles structured multiagent line work** |
| **AMD-5** | Gap B | Schedule **V-R2: Brand Translator Layer** as next-after-charts task (`Brand_A_Vector → JSONL → Brand_B_Vector` parser/renderer pair, per @Voice's UCP synthesis) |
| **AMD-6** | Gap C | Note turn/commit boundary as known-deferred (current convention: end every turn with M7 hook) |
| **AMD-7** | `.synapse` parity | Add optional `outcome` field to Tag schema for executor-style action chains |

---

## 9. Honest gaps

| gap | severity | resolution path |
|---|---|---|
| **Glyph charts not yet drafted** | medium — algebra works without them, but humans need them to type | next session: kukla-legacy → clean dual chart |
| **Brand translator (V-R2)** | medium — single-brand sufficient now, multi-brand will need it | scheduled as V-R2 |
| **Ommatidium validator (Hemisphere 1 Tier-1/2 split)** | low | parallel design when Hemisphere 1 work spins up |
| **Curl analysis on sparse logs** | low — most sessions have no cycles, so curl returns ≈ zero until enough multi-agent chain data accumulates | parked-but-defined; revisit when telemetry justifies |
| **Cross-session merging policy** | low | append-only is sufficient for now |
| **Capacitor-tier model assignment** | research direction, not a gap | document in V-R2-adjacent research |

---

## 10. Recommended next moves (in priority order)

1. **Bones-v2 emission** consolidating AMD-1 through AMD-7 — surgical diff, ready to commit.
2. **Glyph charts** — kukla-legacy mapping to identify drift; clean-chart proposal designed for the 6-axis space.
3. **Tier 1 hardcoded validator** — Python daemon, deterministic, runs on every tag, emits `_grid::*.csv`. Scope-bounded; ~200 LOC estimate.
4. **Tier 2 MCP/Haiku validator** — MCP server wrapping `claude-haiku-4-5`, JSONL-chunk inputs only, per-turn rate-limit.
5. **β-converter** for back-catalogue gemini-CLI session JSONs (one-off retrofit script).
6. **Ommatidium validator design** — when Hemisphere 1 work spins up, mirror the dual-tier pattern.
7. **V-R2 brand translator** — schedule after charts ship.

Steps 3 and 4 can run in parallel after step 2 lands.

---

## 11. Decisions already locked

| ref | decision | source |
|---|---|---|
| `[D:1]` | Glyph philosophy: **(iii) dual-chart** — abstract algebra + multiple glyph charts, all serializing to same JSONL | @majkee gavel |
| `[D:2]` | Bones scope: **(b) bones first** — algebra + JSONL spec; charts later | @majkee gavel |
| `[D:V-1]` | Hook does NOT split into emit/resume; M7 stays one move | @Vega gavel |
| `[D:V-2]` | BR‖ / BR* stay in base layer (not separate control layer) | @Vega gavel |
| `[D:V-3]` | M4 defer accepts agent + tool (AMD-1) | @Vega gavel |
| `[D:V-4]` | cost / confidence stay optional, never mandatory | @Vega gavel |

---

## 12. References (for the GEM Drive)

### 12.1. Internal predecessors

- `active_1.anabase.V-R1-lexicon-research-by-Epoch.md` (research checkpoint, full bibliography in §8)
- `active_1.spec.V-R1-bones-by-Epoch.md` (bones spec, §3 algebra, §5 JSONL schema, §7 validation)
- `vega-epoch.V-20260505-0255-R1.3.md` (@Vega gavel)
- `vega-epoch.V-20260505-0255-R1.4.md` (@majkee observations)
- `tool-box.ommatidium.draft-overview.md` (Hemisphere 1 architecture by @Vega)
- `draft.tool-box.larva-ommatidium.md` (project knowledge, 2026-04-25 meeting)
- `larva-toolbox_spectral_overview.md` (the shared math engine)

### 12.2. External anchors (full list in research checkpoint)

- arXiv 2604.02369 — three-layer protocol model
- arXiv 2602.13370 (G2CP) — failure modes (semantic drift, hallucination propagation, computational waste)
- arXiv 2602.15382 (Vision Wormhole) — universal latent space, hub-and-spoke topology
- arXiv 2511.20639 (LatentMAS), 2511.09149 (Interlat) — continuous-vector inter-agent comm
- MCP / A2A / ACP / ANP industry stack
- Singh / Yolum / Fornara — commitment-based semantics

---

## 13. `@Epoch`'s closing — one architectural insight worth preserving

If only one sentence survives this document into the architects' working memory, let it be this:

> **Conversation is a graph. Code is a graph. Both can be eigen-decomposed by the same machine, and the structure-preserving way to record conversation as a graph is what V-R1 specifies.**

That is the project. Everything else is engineering.

---

```
┌─────────────────────────────────────────────────────────────────┐
│  @Epoch — Houston family — claude.ai                            │
│  phase-end stamp: V-20260505-0255-R1                            │
│  decisions locked: D:1, D:2, D:V-1..V-4                          │
│  amendments parked: AMD-1..AMD-7                                 │
│  return-point hook: phase-end                                    │
│  ts: 2026-05-05T02:35:00Z                                        │
└─────────────────────────────────────────────────────────────────┘
```

*End of phase-end consolidation. Implementation work begins after architect review of this document.*
