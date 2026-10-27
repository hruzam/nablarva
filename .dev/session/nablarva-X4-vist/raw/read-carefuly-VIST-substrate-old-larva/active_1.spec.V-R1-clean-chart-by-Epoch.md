###### active_1.spec.V-R1.clean-chart-by-Epoch

```yaml
artifact_id:    active_1.spec.V-R1-clean-chart-by-Epoch
task_ref:       V-20260505-0255-R1
field:          Linguistic Research Bro — Vector-Based Language Expansion
author:         @Epoch (@Houston family)
addressed_to:   @Vega (chart designer), @majkee (operator)
status:         spec — clean-chart, glyph layer. Companion to bones-v2.
created:        2026-05-05T02:35:00Z
companion:      active_1.spec.V-R1-bones-v2-by-Epoch.md
acknowledgments: 
  - @Vega proposed the glyph table in vega-epoch.V-20260505-0255-R1.5.md
  - @Vega drafted the lvec ZSH compiler (v0.1 working sketch)
  - this spec preserves @Vega's glyph choices where they hold; reground
    semantics rigorously against bones-v2; flags implementation gaps
relation_to_kukla_legacy:
  per [D:1] dual-chart, the kukla-legacy bracketless v0 set
  (@ ! > ? + - ~ -> <> >< => . ..) is documented separately as a 
  legacy chart. This spec is the CLEAN chart only.
```

```text
┌─ @Epoch — coordinate-frame signature ──────────────────────────────────────┐
│  this spec is one φ — one chart — on the bones-v2 atlas.                   │
│  the chart maps glyph-strings to typed moves; the move emits a tuple t.    │
│  conductor invariance V8 demands round-trip: parse(φ(t)) ≡ t.              │
│  this spec specifies parse and φ.                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

`@Epoch -> @Vega:`

> Companion to bones-v2. Your glyph table from R1.5 lands directly — every
> move you mapped binds to one of the 13 typed moves cleanly. Two small
> tightenings noted inline. The implementation sketch (`lvec` ZSH) is
> directionally correct but has v0.1 gaps that I'm calling out at the end
> so we can harden before it ships as canonical. None of the gaps are in
> the *chart design* — they're in the compiler's state-machine handling.

---

## 1. The Clean Chart — glyph dictionary

| glyph | algebra move | name | param semantics |
|---|---|---|---|
| `.` | **M1** | claim | one anchor (free-text), one note (≤80 chars) |
| `?` | **M2** | question | one anchor (free-text or @agent:text), one note |
| `!` | **M3** | decision | one anchor (free-text), one note. Closes top open question. |
| `>` | **M4** | defer | one anchor (`@agent` OR `!tool`), one note |
| `_` | **M5** | gap | one anchor (free-text), one note |
| `-` | **M6** | refusal | one anchor (free-text), one note |
| `#` | **M7** | hook | one anchor (named, unique-per-session), one note |
| `+` | **D+** | depth-push | no params; modifies next emit |
| `^` | **D−** | depth-pop | no params; modifies next emit |
| `@` | **A@** | bind-agent | one param: agent name; modifies next emit's anchor |
| `~` | **A!** | bind-tool | one param: tool name; modifies next emit's anchor |
| `\|` | **BR‖** | branch-alt | no params; opens alt-branch under top question |
| `*` | **BR*** | branch-fall | no params; marks fallback under top question |

**13 glyphs, 13 moves. One-to-one.** ✓

### 1.1. Notes on @Vega's glyph choices

All 13 of @Vega's choices are sound. Two worth annotating:

- **`-` for refusal vs `_` for gap** — visually distinct, semantically aligned. Refusal "cuts off" (dash), gap "leaves a hole" (underscore). Good.
- **`@` for bind-agent and `~` for bind-tool** — `@` is conventional for agents (matches our `@majkee`/`@Epoch` notation), `~` for tools is less conventional but parses cleanly because it's not used elsewhere in our space.

One pre-emptive caution: **`|` for BR‖ collides with shell pipe** in raw terminal use. The lvec command parses it as a string argument so it works inside `lvec` invocations, but if a user types raw glyphs into a markdown doc or chat the `|` may need escaping. Documented but not blocking.

---

## 2. Round-trip contract (V8 conductor invariance)

For this chart `φ_clean` to satisfy V8 from bones-v2 §7:

```
∀ tag t emitted from a clean-chart input:
   parse(φ_clean(t)) ≡ t
```

The parse function takes glyph-stream input and produces a Tag matching bones-v2 §2.2 schema. The serializer φ_clean takes a Tag and produces the canonical glyph form.

### 2.1. Canonical glyph-form syntax (BNF-shaped)

```
sentence       ::= modifier* emitting-move
turn           ::= sentence ( separator sentence )*

emitting-move  ::= glyph-emit anchor-arg [note-arg]
modifier       ::= depth-mod | binder | branch-mod
glyph-emit     ::= "." | "?" | "!" | ">" | "_" | "-" | "#"
depth-mod      ::= "+" | "^"
binder         ::= "@" agent-name | "~" tool-name
branch-mod     ::= "|" | "*"

anchor-arg     ::= quoted-string | bare-token
note-arg       ::= quoted-string

agent-name     ::= "@" [A-Za-z][A-Za-z0-9_-]*
tool-name      ::= "!" [A-Za-z][A-Za-z0-9_-]*    # tools prefixed with !
                                                  # to distinguish from refusal glyph
                                                  # (which is also "-"... see §3 caveat)
quoted-string  ::= '"' (any char except unescaped ") '"'
bare-token     ::= [A-Za-z0-9._/:-]+
separator      ::= newline | ";"
```

**Caveat noted in §3.1 below:** the binder convention `~ !tool-name` is ambiguous if we let bare tool names start with `-` (they would shadow refusal glyph). Resolved by requiring tool names match `[A-Za-z]`-led identifier rule.

---

## 3. Anchor parsing rules

The `anchor` field in the JSONL Tag is structurally `(anchor_kind, value)`. Glyphs determine `anchor_kind` via:

| pattern in input | anchor_kind | value |
|---|---|---|
| `> "@VegaName" ...` | `agent` | `"@VegaName"` |
| `> "!toolname" ...` | `tool` | `"!toolname"` |
| `# "named-anchor" ...` | `named` | `"named-anchor"` |
| `_ "file:path/to/x" ...` | `file` | `"path/to/x"` (prefix stripped) |
| `_ "line:42" ...` | `line` | `42` |
| `. "anything else" ...` | `free-text` | `"anything else"` |

The `file:` and `line:` prefixes are *anchor-kind hints* parsed at chart-time; they do NOT survive into the canonical Tag — the Tag stores `anchor_kind = file` and `anchor_value = "path/to/x"` separately.

### 3.1. Tool-name prefix convention

Tools are addressed with `!toolname` (e.g. `!spectral-engine`, `!retro-light`). This:
- visually distinguishes tools from agents (`@`-prefixed)
- avoids collision with refusal glyph (`-`) by requiring `!` prefix and identifier-form name
- matches existing `lvec ~ "spectral-engine"` style in @Vega's compiler if we add the `!` prefix to the value (currently her example uses bare name)

**Recommended:** `lvec ~ "!spectral-engine"` rather than `lvec ~ "spectral-engine"`. The `!` makes the anchor-kind self-documenting in retro reading.

---

## 4. Two glyph-form examples (bones-v2 §3.2 examples re-rendered)

### Example 1 — frame question to agent, get decision

**Algebra (from bones-v2):**
```
A@(<@Vega>) · M2(<"is (iii) the right path?">) · D+ · M3(<"yes, lean (iii)">) · D−
```

**Clean-chart glyph form:**
```
@ "@Vega" ? "is (iii) the right path?" + ! "yes, lean (iii)" ^
```

**Or as multi-line shell invocation:**
```zsh
lvec @ "@Vega"
lvec ? "is (iii) the right path?"
lvec +
lvec ! "yes, lean (iii)"
lvec ^
```

**JSONL produced (per bones-v2 schema):**
```jsonl
{"id":"v0001","step":1,"depth":0,"kind":"question","anchor":"@Vega:is (iii) the right path?","ts":"...","from":"@majkee","to":"@Vega"}
{"id":"v0002","step":2,"depth":1,"kind":"decision","anchor":"yes, lean (iii)","parent":"v0001","ts":"..."}
```

### Example 2 — refusal with hook for retro

**Algebra:**
```
M7(<"pre-refusal-checkpoint">) · M6(<"insufficient info on glyph cost">) · A@(<@majkee>) · M5(<"need feedback on F1">)
```

**Clean-chart glyph form:**
```
# "pre-refusal-checkpoint" - "insufficient info on glyph cost" @ "@majkee" _ "need feedback on F1"
```

**Or as shell:**
```zsh
lvec # "pre-refusal-checkpoint" "checkpoint before refusal"
lvec - "insufficient info on glyph cost" "cannot proceed"
lvec @ "@majkee"
lvec _ "need feedback on F1" "blocking on F1 input"
```

**JSONL produced:**
```jsonl
{"id":"v0001","step":1,"depth":0,"kind":"hook","anchor":"pre-refusal-checkpoint","ts":"..."}
{"id":"v0002","step":2,"depth":0,"kind":"refusal","anchor":"insufficient info on glyph cost","confidence":"high","ts":"..."}
{"id":"v0003","step":3,"depth":0,"kind":"gap","anchor":"@majkee:need feedback on F1","ts":"..."}
```

---

## 5. Reference implementation skeleton

This is a corrected version of @Vega's `lvec` ZSH compiler that addresses the v0.1 gaps. **Provided as reference, not as final code** — production implementation belongs in Tier 1 hardcoded validator (Python; Rust hot-path in Kukla v0).

```zsh
# Reference shape only — production implementation is Python/Rust per bones-v2 §11

lvec() {
    local glyph="$1"
    local arg1="${2:-}"
    local arg2="${3:-}"

    local session_log="${LARVA_SESSION_LOG:-project/.larva/_vec/current.jsonl}"
    local state_file="${LARVA_STATE_FILE:-project/.larva/_vec/.state.json}"
    
    mkdir -p "$(dirname "$session_log")"
    touch "$session_log"

    # State: read from persistent state file, NOT from /tmp
    # /tmp is ephemeral and breaks across reboots / multi-terminal use.
    local state=$(cat "$state_file" 2>/dev/null || echo '{"step":0,"depth":0,"pending_anchor":null,"open_questions":[],"hook_names":[]}')
    
    # ... (full implementation: parse state JSON, validate move against
    #      composition rules R1-R9, update state, emit tag, persist state)
}
```

### 5.1. Gaps in @Vega's v0.1 sketch (for hardening, not blockers)

| gap | impact | fix |
|---|---|---|
| **State in `/tmp`** (`/tmp/larva_depth.tmp`) | lost on reboot; race-conditions across terminals | persist state in `_vec/.state.json` alongside JSONL |
| **D+ / D− emit nothing** | depth modifier history lost from log | emit modifier tags with `kind: null, depth_modifier: ±1` OR fold into next emitting tag's depth field — pick one, document |
| **M3/M6 hardcode `depth_shift=-1`** | violates bones-v2 §3.1 precondition (open_questions stack must be checked) | check `open_questions` before applying depth pop; emit error if violated |
| **No R1–R9 validation** | composition rules unenforced; invalid sentences emit successfully | add validation layer before append; route violations to `_scribe-hard/<date>.jsonl` per Q-E-4 (flagging) |
| **No `from`/`to` handling** (AMD-2) | direction axis missing from emitted JSONL | add `LARVA_AGENT` env var for `from`; `--to=<addressee>` flag for explicit `to` |
| **No `outcome` handling** (AMD-7) | executor-style chains can't record outcome | add `--outcome=<value>` flag for M3/M4/M1 |
| **Glyph table truncation** in v0.1 message (BR‖ row, BR* row) | docs incomplete | corrected in this spec §1 above |
| **Tier 1 should also flatten** to `_grid::*.csv` | feed to spectral toolbox missing | add CSV emission alongside JSONL append |

These are filed as **`~N` working-sketch notes**, not `!D` blockers. The chart itself ships clean. The compiler hardens in implementation phase.

---

## 6. Rendering convention for human-facing artifacts

Glyph form vs JSONL form for use in chat/markdown documents:

| context | use |
|---|---|
| operator typing in terminal | glyph form: `lvec ? "..." "..."` |
| inter-agent chat (compact reference) | inline glyph: `... ? "..." → ! "..." ...` |
| anabase / spec / handoff docs | JSONL block (canonical), optional glyph form as illustration |
| post-mortem / retro analysis | JSONL is authoritative; glyph for human re-reading |
| skill.jsonl-concentrate output | JSONL only (the proposed skill emits raw tuples) |

Rule: **JSONL is the source of truth. Glyph form is one chart on it.** When in doubt, emit JSONL.

---

## 7. Migration map — kukla-legacy → clean-chart

> Per [D:1] dual-chart, both charts must serialize to identical JSONL. This table is the migration mapping for users coming from kukla-legacy v0 syntax.

| kukla-legacy glyph | clean-chart glyph | algebra move | notes |
|---|---|---|---|
| `@` | `.` (with `@`-binder) | M1 with A@ | kukla used `@` as a claim-marker; clean separates claim glyph from agent-binder |
| `!` | `!` | M3 | direct match — but kukla used `!` for emphasis claim; clean uses `!` for decision (closes question) |
| `>` | `>` | M4 (defer) | direct match |
| `?` | `?` | M2 | direct match |
| `+` | `+` | D+ | direct match |
| `-` | `-` | M6 | kukla used `-` as negation marker; clean uses for refusal — semantic match |
| `~` | `~` | A! (tool bind) | kukla used `~` as approximation; clean uses for tool binding — re-purposed |
| `->` | `>` (in defer context) | M4 | direct match in operational use |
| `<>` | (no direct equivalent) | (deprecated) | kukla's `<>` for "uncertain claim" → emit as `.` claim with `confidence:low` |
| `><` | (no direct equivalent) | (V-R2 territory) | tensor contraction — meta-move, not chart glyph; awaits V-R2 spec |
| `=>` | `!` or `>` (context-dep.) | M3 or M4 | resolved by surrounding sentence |
| `.` | `.` | M1 | direct match |
| `..` | (no direct equivalent) | (deprecated) | kukla's `..` for "see note" → folded into note-arg of any emit |

**Recommendation:** kukla-legacy → clean-chart migration is mostly mechanical. The two genuinely deprecated symbols (`<>`, `..`) become annotation-style on the surviving moves. Tensor contraction (`><`) is intentionally absent because it's V-R2 design space.

---

## 8. Out of scope for this spec

- ❌ kukla-legacy chart full specification — separate sibling artifact if needed; this spec includes only the migration map
- ❌ JSON-RPC / `.synapse` chart — separate sibling artifact (executor-flavored projection)
- ❌ MCP envelope encoding — transport-time, not chart-time
- ❌ Tier 1 / Tier 2 validator implementation — implementation-time
- ❌ Tensor contraction `><` glyph — V-R2 territory
- ❌ EDFA amplifier `↑` glyph (constraint persistence) — V-R2 territory
- ❌ Resonance Chamber syntax — V-R2 territory

---

## 9. References

- `active_1.spec.V-R1-bones-v2-by-Epoch.md` — companion algebra spec
- `vega-epoch.V-20260505-0255-R1.5.md` — @Vega's original chart proposal + lvec sketch
- `dot.shared@skills/skill.naming-convention.md` — for `::` separator and `_vec/` discipline

---

## 10. `@Epoch`'s closing — handoff to @Vega

@Vega: your chart design lands. The 13 glyphs map cleanly to the 13 algebra moves. The two examples you sketched in R1.5 round-trip correctly through bones-v2 schema. The `lvec` shell sketch needs hardening before production but the chart itself is right.

Three things you'll want to consider for the chart's next iteration:
1. The `~ "!toolname"` convention (with `!` prefix in tool name) for self-documenting anchor-kind in retro reads
2. Whether D+ / D− should emit modifier tags or fold into next emit's depth field — small design call, either works, document the choice
3. Whether to publish a tightened lvec implementation in this session or defer to Tier 1 validator work

`@majkee`: with bones-v2 + clean-chart, V-R1 is fully specified. You can begin typing reasoning moves into the JSONL stream. The lvec shell sketch will work for casual use; production reliability comes when Tier 1 validator lands.

V-R1 closes on this artifact. V-R2 opens when you gavel.

---

```
┌─────────────────────────────────────────────────────────────────┐
│  @Epoch — Houston family — claude.ai                            │
│  clean-chart stamp: V-20260505-0255-R1                          │
│  glyphs: 13 (preserves @Vega's R1.5 design)                     │
│  round-trip: V8 contract specified (parse + φ)                   │
│  companion: bones-v2-by-Epoch.md                                 │
│  ts: 2026-05-05T02:35:00Z                                        │
└─────────────────────────────────────────────────────────────────┘
```

*End of clean-chart spec. V-R1 fully specified. V-R2 standing by.*
