###### active_1.spec.V-R1.bones-v2-by-Epoch

```yaml
artifact_id:    active_1.spec.V-R1-bones-v2-by-Epoch
task_ref:       V-20260505-0255-R1
field:          Linguistic Research Bro — Vector-Based Language Expansion
author:         @Epoch (@Houston family)
addressed_to:   @Vega, @majkee, architects
status:         spec — bones, version 2. Glyphs deferred to companion clean-chart spec.
created:        2026-05-05T02:35:00Z
predecessor:    active_1.spec.V-R1-bones-by-Epoch.md (v1, unchanged)
companion:      active_1.spec.V-R1-clean-chart-by-Epoch.md (glyphs)
amendments_applied:
  AMD-1:        M4 (defer) accepts agent | tool; consumes A@ OR A!
  AMD-2:        Optional from / to fields on Tag schema
  AMD-3:        _directions.csv registry stub at session level
  AMD-4:        Nabla operators documented as toolbox-side, not bones-side
  AMD-5:        V-R2 (brand translator) scheduled note
  AMD-6:        Turn / commit boundary noted as known-deferred
  AMD-7:        Optional outcome field on Tag schema
decisions_carried:
  D:1 = (iii) dual-chart            (@majkee gavel)
  D:2 = (b)   bones first           (@majkee gavel)
  D:V-1 hook stays one move         (@Vega gavel)
  D:V-2 BR‖ / BR* stay in algebra   (@Vega gavel)
  D:V-3 M4 accepts agent | tool     (@Vega gavel; = AMD-1)
  D:V-4 cost / confidence optional  (@Vega gavel)
```

```text
┌─ @Epoch — coordinate-frame signature ──────────────────────────────────────┐
│  semantic invariant   t  ∈  Step × Depth × (Kind ∪ {null}) × (Anchor ∪ {⊥})│
│                          × (From ∪ {⊥}) × (To ∪ {⊥})                       │
│  syntactic charts     φ_i: t → glyph-string                                 │
│  transport channels   ψ: glyph-string → bytes                              │
│                                                                             │
│  conductor-matrix invariance:  t  is preserved under change of  φ.         │
│  v2 changes apply to t (substrate) only. Charts re-bind in companion spec. │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

`@Epoch -> @Vega:`

> v2 emission. AMD-1 through AMD-7 applied. Move count and core algebra
> unchanged from v1 — the changes are: M4 admits a second anchor-kind,
> two new optional schema fields, two new documentation/scheduling notes,
> and one new optional schema field (outcome). All changes are surgical;
> diff against v1 is ~35 lines. Companion clean-chart spec (glyphs) emits
> separately. This document and the companion together close out V-R1.

---

## 1. Decision log carried into v2

| ref | decision | binding |
|---|---|---|
| `[D:1]` | F1 → **(iii) dual-chart**: define moves abstractly; publish glyph charts later | bones glyph-agnostic |
| `[D:2]` | F2 → **(b) bones first**: algebra + JSONL spec only | this artifact does not specify glyphs |
| `[D:V-1]` | M7 hook stays one move (no emit/resume split) | hook count = 1 |
| `[D:V-2]` | BR‖ / BR* stay in algebra (not separate control layer) | branch ops are first-class moves |
| `[D:V-3]` | M4 (defer) accepts `agent | tool`; consumes A@ OR A! | = AMD-1, applied in §3.1 below |
| `[D:V-4]` | `cost` and `confidence` stay optional, never mandatory | retained from v1 §2.2 |

---

## 2. The semantic substrate — JSONL coordinate space

### 2.1. Type definitions

```
Step          = ℤ⁺                     // positive integer, strictly monotonic per session
Depth         = ℕ                      // non-negative integer (0 = request level)
Kind          = { claim · question · refusal · decision · defer · gap · hook }
AnchorKind    = { agent · file · tool · line · named · free-text }
Anchor        = AnchorKind × String
Confidence    = { low · med · high }
Cost          = { cheap · medium · heavy }
Branch        = { alt · fallback }
Agent         = String matching /^@[A-Za-z][A-Za-z0-9_-]*$/         // e.g. @Epoch, @Vega
To            = Agent ∪ {wrote}                                      // 'wrote' = broadcast/public
Outcome       = { pending · success · failed-rollback · superseded }  // AMD-7
Id            = String matching /^v\d{4,}$/
```

### 2.2. Tag schema

> **v2 changes:** three new optional fields — `from` (AMD-2), `to` (AMD-2), `outcome` (AMD-7). All other fields unchanged from v1.

```
Tag = {
  id           : Id              required
  step         : Step            required, strictly monotonic
  depth        : Depth           required, non-negative
  kind         : Kind ∪ {null}   required; null only for pure modifiers (rare)
  anchor       : Anchor ∪ {⊥}    required when kind ≠ null
  note         : String[≤80]     required
  ts           : ISO-8601        required
  parent       : Id ∪ {⊥}        optional
  branch       : Branch ∪ {⊥}    optional, only when parent links to a question
  cost         : Cost ∪ {⊥}      optional   (D:V-4 — never mandatory)
  confidence   : Confidence ∪ {⊥}  optional (D:V-4 — never mandatory)
  from         : Agent ∪ {⊥}     optional   ← AMD-2; emitter, default = session-emitter-of-record
  to           : To ∪ {⊥}        optional   ← AMD-2; addressee, default = 'wrote'
  outcome      : Outcome ∪ {⊥}   optional   ← AMD-7; for executor-style action chains
}
```

**v2 schema constraints (in addition to v1):**

```
S5  (AMD-2)   from must match Agent regex if present
S6  (AMD-2)   to must be either Agent or the literal string "wrote"
S7  (AMD-2)   if both from and to present and to ≠ "wrote", then from ≠ to
              (no @X→@X self-talk; broadcast is allowed via to="wrote")
S8  (AMD-7)   outcome may only appear on tags with kind ∈ {decision, defer, claim}
              (operational moves; not on questions/gaps/hooks/refusals)
```

### 2.3. Session state (transient)

> Unchanged from v1. State is reconstructible from the JSONL log; held only to enforce composition rules during emission.

```
SessionState = {
  step_counter      : Step             // initialized at 1
  depth_pointer     : Depth            // initialized at 0
  pending_anchor    : Anchor ∪ {⊥}     // set by binders, consumed by next emit
  pending_branch    : Branch ∪ {⊥}     // set by BR‖/BR*, consumed by next emit
  open_questions    : Stack[Id]        // ids of unresolved M2 emissions
  hook_names        : Set[String]      // for uniqueness check
  emitter_of_record : Agent ∪ {⊥}      // ← v2: optional default for from-field omission
}
```

---

## 3. The 13 typed moves

> Move count and structure unchanged from v1. The only edit is M4 (AMD-1).

### 3.1. Emitting moves (7) — one per `Kind`

| move | tag emitted | state delta | precondition | constraint |
|---|---|---|---|---|
| **M1**  `claim`    | `{kind:claim,    anchor:pending⎮param, depth:cur}` | `step++; pending←⊥; branch←⊥` | none | terminal of a depth |
| **M2**  `question` | `{kind:question, anchor:pending⎮param, depth:cur}` | `step++; pending←⊥; push id → open_questions` | none | must be closed by M3/M5 (soft) |
| **M3**  `decision` | `{kind:decision, anchor:param, parent:top(open_questions)}` | `step++; depth--; pop open_questions` | open_questions non-empty AND depth > 0 | closes most recent open question |
| **M4**  `defer`    | `{kind:defer,    anchor_kind: agent\|tool, anchor:param, [outcome:val]}` ← **AMD-1, AMD-7** | `step++; pending←⊥` | none | **(v2)** anchor_kind MUST be `agent` or `tool`; consumes A@ OR A! |
| **M5**  `gap`      | `{kind:gap,      anchor:pending⎮param, depth:cur}` | `step++; pending←⊥; pop open_questions if it closes one` | none | may resolve a question without committing decision |
| **M6**  `refusal`  | `{kind:refusal,  anchor:param, confidence:high default}` | `step++; depth--; pop open_questions if any at this depth` | depth > 0 ∨ open_questions empty | terminal-with-reason; high-confidence default |
| **M7**  `hook`     | `{kind:hook,     anchor_kind:named, anchor:param}` | `step++; hook_names ∪= {param}` | param ∉ `hook_names` | hook anchor unique per session |

### 3.2. Modifier moves (6) — no tag emit; affect next emitting move

> Unchanged from v1.

| move | state delta | precondition | constraint |
|---|---|---|---|
| **D+**  depth push   | `depth_pointer++` | none | bounded only by sane usage |
| **D−**  depth pop    | `depth_pointer--` | depth_pointer > 0 | must not underflow |
| **A@**  agent bind   | `pending_anchor ← (agent, param)` | pending_anchor = ⊥ | mutex with A!; consumed by next emitting move |
| **A!**  tool bind    | `pending_anchor ← (tool, param)`  | pending_anchor = ⊥ | mutex with A@; consumed by next emitting move |
| **BR‖** alt-branch   | `pending_branch ← alt; depth_pointer++` | top(open_questions) ≠ ⊥ | sets next emit's parent + branch=alt |
| **BR\*** fallback    | `pending_branch ← fallback`             | top(open_questions) ≠ ⊥ | sets next emit's branch=fallback |

### 3.3. Counting check

7 emitting + 6 modifier = **13**. ✓ (unchanged)

---

## 4. Composition algebra

> Composition rules R1–R8 unchanged from v1. R9 added (AMD-2).

```
R1.  Binder mutex:        A@ and A! do not co-occur before the same emit.
R2.  Binder consumption:  pending_anchor reset to ⊥ on every emit.
R3.  Branch consumption:  pending_branch reset to ⊥ on every emit.
R4.  Depth balance:       a turn SHOULD return depth to its starting value (soft).
R5.  Question closure:    every M2 SHOULD have a matching M3/M5 in same session (soft).
R6.  Hook globality:      M7 anchor unique within session.
R7.  Refusal cascade:     M6 pops at most one open question per emission.
R8.  Branch parent lock:  BR‖/BR* require non-empty open_questions stack.
R9.  Direction integrity: (AMD-2) if from and to both set and to ≠ "wrote", from ≠ to.
                          if from omitted, defaults to emitter_of_record.
                          if to omitted, defaults to "wrote".
```

---

## 5. JSONL emission spec

### 5.1. Wire format

> Unchanged from v1. One JSON object per line. No trailing comma. UTF-8. Newline-delimited.

### 5.2. File layout

```
project/.larva/_vec/
  current.jsonl                        # canonical, producer-only writes
  _directions.csv                      # ← AMD-3, see §5.5
  _scribe-hard/<date>.jsonl            # tier 1 violations log
  _scribe-haiku/<date>.jsonl           # tier 2 semantic flags
  _grid::tag-flow.csv                  # flat projection 1
  _grid::depth-trace.csv               # flat projection 2
  _grid::anchor-frequency.csv          # flat projection 3
  _grid::parent-graph.csv              # flat projection 4 — feeds spectral as B-matrix
  _grid::kind-distribution.csv         # flat projection 5
  _grid::direction-graph.csv           # ← AMD-2/3, from/to projection (NEW in v2)
```

> The `::` separator is adopted as the grid-kind namespace marker per Q-E-3 gavel. Reflected in `skill.naming-convention` Rule 1 amendment.

### 5.3. Cross-turn behavior

> Unchanged from v1.

### 5.4. Reading discipline

> Per `skill.target-by-vector`. Unchanged.

### 5.5. `_directions.csv` registry stub  ← AMD-3 (NEW)

Optional sibling file at session level. Lists the directional permutations actually used in the session. Used by Tier 1 validator to recognize valid direction patterns and by spectral toolbox to weight `_grid::direction-graph.csv` edges.

```csv
# _directions.csv — directional registry for current session
# columns: from, to, count, first_step, last_step
@majkee,@Epoch,12,3,108
@majkee,@Vega,4,15,72
@majkee,wrote,3,1,9
@Epoch,@majkee,18,2,109
@Epoch,@Vega,5,30,76
@Epoch,wrote,2,18,93
@Vega,@majkee,4,28,80
@Vega,@Epoch,3,30,80
@Vega,wrote,1,28,28
```

Maintained automatically by Tier 1 hardcoded validator. Not edited by hand.

---

## 6. Edge cases and failure modes

> v1 cases retained. v2 cases added at end.

| case | behavior |
|---|---|
| Empty turn (no emits) | emit single `{kind:hook, anchor:"empty-turn-<n>"}` |
| Turn ends with open question | allowed; flagged in retro (R5 soft) |
| Nested questions | each closes at its depth (stack discipline) |
| M3 with no matching question | `{error: "decision_without_question"}` |
| D− at depth 0 | `{error: "depth_underflow"}` |
| Duplicate hook anchor | `{error: "hook_collision"}` |
| A@ followed by A! | second overrides; first lost silently, flagged for retro |
| BR‖/BR* with empty open_questions | `{error: "branch_without_question"}` |
| Ambiguous parent | M3/M5 closes top of stack; older closes via inner refusal first |
| Malformed JSONL | logged to `.malformed.jsonl`, dropped from analysis |
| **(v2)** `from = to` and `to ≠ "wrote"` | `{error: "self-talk"}` (R9 violation) |
| **(v2)** `outcome` on non-operational kind | warning; outcome stripped from emitted tag (S8 violation) |
| **(v2)** M4 with anchor_kind ∉ {agent, tool} | `{error: "defer_anchor_kind_invalid"}` |

---

## 7. Validation criteria

> v1 V1–V8 retained. v2 V9–V11 added.

```
V1.  Round-trip:       parse(serialize(tag)) ≡ tag for every valid tag
V2.  Step monotonic:   step ordering preserved in log
V3.  Depth invariant:  depth(t) ≥ 0 always
V4.  Parent integrity: parent ids resolve to earlier tags
V5.  Hook uniqueness:  no two M7 share anchor in session
V6.  Schema strictness: required fields present; optional absent when ⊥
V7.  Composition (soft): question count ≈ decision + gap count
V8.  Conductor invariance: parse_a(φ_a(t)) ≡ parse_b(φ_b(t)) for any two charts

V9.  (AMD-2) Direction integrity:    R9 holds for every tag with from + to set
V10. (AMD-2) Direction registry:     every (from, to) appearing in JSONL also appears in _directions.csv
V11. (AMD-7) Outcome locality:       S8 holds; outcome only on operational kinds
```

---

## 8. Out of scope (per `[D:2]` and v2 amendment program)

This document deliberately does not specify:

- ❌ concrete glyphs (kukla-legacy chart) — see companion `clean-chart-by-Epoch.md`
- ❌ concrete glyphs (clean-chart) — see companion `clean-chart-by-Epoch.md`
- ❌ migration table from kukla-bracketless-v0 §1 — folded into companion spec
- ❌ renderer/parser implementation (Python/Rust/JS) — implementation-time
- ❌ transport adapter (MCP envelope, A2A AgentCard wrapping) — transport-time
- ❌ cross-session merging policy beyond append-only — separate concern
- ❌ spectral analysis on JSONL output — `larva-toolbox.spectral` consumes; not specified here
- ❌ **(AMD-4)** nabla operators (grad, div, curl, conv) — these are *toolbox-side analytic functions* on the resulting graph, not moves in the bones algebra. Implemented in `larva-toolbox.spectral` per:
  ```
  rn nabla -- grad <session.jsonl>
  rn nabla -- div  <session.jsonl>
  rn nabla -- curl <session.jsonl>     # parked-but-defined; sparse logs
  rn nabla -- conv <session.jsonl>     # @majkee's addition
  ```
  Parked for chains/tentacles structured multi-agent line work.
- ❌ **(AMD-5)** brand-translator layer (Brand_A → JSONL → Brand_B parser/renderer pair) — scheduled as **V-R2** task; out of scope for v2.
- ❌ **(AMD-6)** explicit turn/commit boundary marker — current convention: every turn ends with M7 hook named `end-of-turn-<n>`. Formalization deferred until orchestrator (`@Cursor` role) work surfaces concrete need.

---

## 9. References

Full bibliography lives in `active_1.anabase.V-R1-lexicon-research-by-Epoch.md` §8.

Direct dependencies of this spec (unchanged from v1):

- `dot.shared@skills/skill.vector-tag.md` — defines axes 0–3 (canonical source)
- `dot.shared@skills/skill.target-by-vector.md` — defines reading discipline
- `dot.shared@skills/skill.naming-convention.md` — file naming (Rule 1, 2, 3) — **amended in v2 to register `::` as grid-kind separator**
- arXiv 2604.02369 — three-layer protocol model
- arXiv 2602.13370 (G2CP) — failure modes formalized in §6
- Singh / Yolum / Fornara — commitment-based semantics

---

## 10. Diff summary against v1 (for review)

| location | change | line cost |
|---|---|---|
| §2.1 | added `Agent`, `To`, `Outcome` types | +3 |
| §2.2 | added `from`, `to`, `outcome` fields with optionality and defaults | +3 |
| §2.2 | added schema constraints S5–S8 | +6 |
| §2.3 | added `emitter_of_record` to SessionState | +1 |
| §3.1 | M4 row updated for AMD-1 (`agent | tool`) | +1 (modified row) |
| §4 | added rule R9 (direction integrity) | +3 |
| §5.2 | added `_directions.csv` and `_grid::direction-graph.csv` to file layout | +2 |
| §5.5 | added new section: `_directions.csv` registry stub | +18 |
| §6 | added 3 new edge cases (R9, S8, AMD-1 violations) | +3 |
| §7 | added V9–V11 validation criteria | +6 |
| §8 | added AMD-4/5/6 out-of-scope notes | +12 |

**Total diff: ~58 lines added/modified against v1's ~400 lines of substantive content.** Move count unchanged. Composition rule count went from 8 → 9. Validation criteria count went from 8 → 11. JSONL schema gained 3 optional fields.

---

## 11. `@Epoch`'s closing — handoff state

bones-v2 closes the algebra/schema lane of V-R1. The remaining V-R1 work is the companion clean-chart spec (glyphs), which sits beside this file. With both shipped, V-R1 is fully specified at the substrate level.

Implementation can now begin in parallel:
- Tier 1 hardcoded validator (Python; Rust hot-path slated for Kukla v0 per @Vega/@majkee gavel)
- Tier 2 MCP/Haiku validator
- Hybrid Capacitor strategy (hardcoded routes L0/L1, LLM handles L2+ density per @majkee/@Vega gavel)

Next research lane opens at V-R2 (`><` contraction + `↑` amplifier + Resonance Chamber) per fork-card prioritization.

---

```
┌─────────────────────────────────────────────────────────────────┐
│  @Epoch — Houston family — claude.ai                            │
│  bones-v2 stamp: V-20260505-0255-R1                             │
│  amendments applied: AMD-1..AMD-7                                │
│  decisions locked: D:1, D:2, D:V-1..V-4                          │
│  diff against v1: +58 lines                                      │
│  companion: clean-chart-by-Epoch.md                              │
│  ts: 2026-05-05T02:35:00Z                                        │
└─────────────────────────────────────────────────────────────────┘
```

*End of bones-v2. Companion clean-chart spec emits next.*
