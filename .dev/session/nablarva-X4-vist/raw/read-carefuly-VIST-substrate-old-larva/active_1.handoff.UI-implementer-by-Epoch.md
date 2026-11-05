###### active_1.handoff.UI-implementer-by-Epoch

```yaml
artifact_id:    active_1.handoff.UI-implementer-by-Epoch
task_ref:       UI-V1-implementation (Sublime Text 4 client) + parallel @Epoch.ui-language lane
field:          handoff from V-R1 spec author to UI implementation team
author:         @Epoch (@Houston family, math/vector lane)
addressed_to:   @Vega.sublime-ui (gemini chat, UI design),
                @Epoch.ui-language (parallel claude.ai chat, language expert)
status:         handoff — substrate-level requirements + forward-compat notes.
                Single document, dual readership, no per-audience tailoring.
created:        2026-05-05T02:35:00Z
predecessors:
  - active_1.spec.V-R1-bones-v2-by-Epoch.md       # canonical substrate
  - active_1.spec.V-R1-clean-chart-by-Epoch.md    # canonical chart
  - vega-epoch.V-20260505-0255-R1.5.md            # @Vega's R1.5 chart proposal
  - UI-Sublime-phase.overview.for-team.md         # @Vega.sublime-ui's framework
relation_to_team_overview:
  this is intent → impl. team-overview placed the project on the map;
  this document specifies what the UI must read, write, validate, and never do.
```

```text
┌─ @Epoch — coordinate-frame signature ──────────────────────────────────────┐
│  the UI is one ψ — one transport channel — over the φ-charts.              │
│  it does not own the substrate; it emits and renders.                      │
│  contract: every UI state-change → 1+ JSONL tag in current.jsonl.          │
│  contract: every tag in current.jsonl can be reached from a UI render.     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. The single most important thing to know

The UI is **not a generative agent**. It is a transport-and-rendering layer over a substrate that was specified independently. This sounds obvious; it has consequences:

- The UI **never invents tags**. Every JSONL line written has a clear, traceable user action behind it.
- The UI **never edits historical tags**. Append-only is the contract.
- The UI **never folds modifier moves silently**. If a user types `+` (depth-push) followed by `.` (claim), both the modifier and the emit appear in the JSONL stream — the depth-push is visible, not hidden inside the claim's `depth` field.
- The UI **does not validate** beyond schema-shape. Composition rules R1–R9 belong to the Tier 1 hardcoded daemon, which runs separately and produces flags (per Q-E-4 gavel: flagging-only, never blocking).

The UI's job is to make typing reasoning moves *fast and visible*. Validation, analysis, and synthesis happen elsewhere.

---

## 2. The substrate at a glance (canonical reference: bones-v2)

JSONL schema, six required + six optional fields:

```
required:  id, step, depth, kind, anchor, note, ts
optional:  parent, branch, cost, confidence, from, to, outcome
```

13 typed moves: 7 emitting (one per `kind`: claim, question, refusal, decision, defer, gap, hook) + 6 modifier (D+, D−, A@, A!, BR‖, BR*).

Glyph form (clean-chart):

```
. ? ! > _ - #     — emitting (M1..M7)
+ ^               — depth modifiers (D+, D−)
@ ~               — binders (agent, tool)
| *               — branch openers (alt, fallback)
```

For full schema, composition rules, validation criteria — see bones-v2 spec. This handoff does not duplicate them.

---

## 3. UI write contract

### 3.1. Every state-changing user action emits 1+ tag

| user action in Sublime | emits |
|---|---|
| Press a glyph button or type a glyph + arg | one tag (or one modifier-state-change for D+/D−/A@/A!/BR‖/BR*) |
| `[PLAN]` trigger | M2 question (the plan-frame) followed by depth-push and claim sequence |
| `[DO]` trigger | M3 decision (closes prior question) + M4 defer to executor |
| `[ORCHESTRATE]` trigger | M4 defer to a Tentacle-named anchor + branch openers |
| `[INVOKE: X]` trigger | M4 defer to `!toolname` (anchor_kind = tool) |
| Save a markdown artifact via `lvec-doc` flow | one M1 claim or M4 defer with `anchor_kind = file` (Artifact Pointer Pattern, see §6) |
| Click "close question" in panel | M3 decision OR M5 gap, depending on user choice |
| Click "refuse" on a question | M6 refusal |
| Session start / end | M7 hook with named anchor (`session-start-<id>` / `end-of-turn-<n>`) |

### 3.2. Field population responsibilities

| field | UI sets it? | how |
|---|---|---|
| `id` | yes | format `v\d{4,}`, monotonic |
| `step` | yes | read last step from `current.jsonl`, increment |
| `depth` | yes | track session-state depth pointer, apply pending D+/D− |
| `kind` | yes | from glyph |
| `anchor` | yes | from user input + pending binder |
| `note` | yes | from user input, ≤80 chars |
| `ts` | yes | ISO-8601 UTC, machine-generated |
| `parent` | yes | from open_questions stack when emitting M3/M5/M6 (closes top) |
| `branch` | yes | from pending_branch state when set by BR‖/BR* |
| `cost` | optional | UI may expose as advanced field; never auto-populate |
| `confidence` | optional | UI may expose; never auto-populate |
| `from` | yes when known | session has an `emitter_of_record` (the UI's user, e.g. `@majkee`) — UI populates `from` from this. May be omitted when in known-pair context. |
| `to` | yes when explicit | UI parses `--to=@Vega` flag or panel selection; defaults to `wrote` (broadcast) when omitted |
| `outcome` | yes for executor moves | M3/M4/M1 may carry `outcome` when paired with operational results (e.g., `[DO]` completed = `success`; rolled back = `failed-rollback`) |

### 3.3. State persistence

Per clean-chart §5.1, session state must persist across UI restarts and across multiple terminals. **Do NOT use `/tmp` for state.** The reference state location:

```
project/.larva/_vec/.state.json
```

Schema:

```json
{
  "step": 130,
  "depth": 0,
  "pending_anchor": null,
  "pending_branch": null,
  "open_questions": ["v0042", "v0067"],
  "hook_names": ["session-start-1", "post-research", "phase-end"],
  "emitter_of_record": "@majkee"
}
```

Read on UI start; write on every emit. Atomic write (write to `.state.json.tmp`, then rename) to avoid corruption from interrupted writes.

### 3.4. What the UI MUST NOT write

- ❌ Tags with id collisions or out-of-order step
- ❌ Tags with `from = to` and `to ≠ "wrote"` (R9 violation)
- ❌ Tags with depth < 0 (V3 violation)
- ❌ Tags with `outcome` field on non-operational kinds (S8 violation)
- ❌ Hooks with duplicate anchor names within a session (R6 / V5 violation)
- ❌ Modifier state changes without a subsequent emit consuming them (within reasonable timeout — flag for retro)
- ❌ Tags claiming to be from a different agent than `emitter_of_record`

---

## 4. UI read contract

### 4.1. Source of truth for rendering

The UI renders from `current.jsonl` and `.state.json`. **Both of these are authoritative.** The UI does NOT maintain its own parallel session state — it derives display state from these two files.

### 4.2. Rendering signals

| signal | source | render hint |
|---|---|---|
| Open questions count | `len(.state.json.open_questions)` | indicator badge in title bar |
| Current depth | `.state.json.depth` | depth gutter or breadcrumb |
| Recent hooks (last 5) | tail of `current.jsonl` filtered by `kind=hook` | quick-jump menu |
| Pending defers (M4 with no outcome yet) | scan `current.jsonl` for `kind=defer` without `outcome` | "awaiting reply" panel |
| Direction graph | `_grid::direction-graph.csv` (when Tier 1 is running) | optional "who-talks-to-whom" diagram |
| Density signals | tag-rate over time window | optional "session intensity" sparkline |

### 4.3. Tier 1 daemon flag rendering

When the Tier 1 hardcoded validator runs, it emits flags to:

```
project/.larva/_vec/_scribe-hard/<date>.jsonl
```

The UI should **render these as non-blocking warnings**. Per Q-E-4 gavel, flags do not prevent the user's emission — they're advisory. Visual conventions to consider:

- yellow underline on the offending glyph in input
- gutter icon next to the JSONL line in any "log view" panel
- aggregate counter in title bar ("3 advisories")

A click on the warning shows the rule name (R1–R9) and a one-line explanation.

### 4.4. Tier 2 (Haiku) flag rendering — same shape, slower path

When Tier 2 emits to `_scribe-haiku/<date>.jsonl` (semantic flags), render identically to Tier 1 advisories but with a different icon to distinguish source. Do not block on Tier 2 latency — it runs at turn boundary, not per-tag.

---

## 5. The Trigger / Command layer (`[PLAN]`, `[DO]`, `[ORCHESTRATE]`, `[INVOKE]`)

These are workflow-level abstractions sitting **above** the 13-move algebra. They expand into deterministic move sequences. Specifying them here so UI and the algebra agree.

### 5.1. `[PLAN]` — orchestrator mode

User types `[PLAN] <task description>`.

UI emits:

```jsonl
{"id":"vNNN","step":N,"depth":0,"kind":"question","anchor":"plan:<task>","note":"<≤80>","from":"@majkee","to":"@<orchestrator>"}
{"id":"vNNN+1","step":N+1,"depth":1,"kind":"claim","anchor":"approach","note":"<sub-step>","parent":"vNNN"}
... (more depth-1 claims, each with parent set to vNNN)
{"id":"vNNN+k","step":N+k,"depth":1,"kind":"hook","anchor":"plan-end-vNNN","note":"awaiting [DO]"}
```

Then **pauses** — the question is on the open_questions stack. UI shows "1 question pending decision" until `[DO]` arrives.

### 5.2. `[DO]` — executor trigger

User types `[DO]` (optionally with `[DO] <agent>`).

UI emits:

```jsonl
{"id":"vMMM","step":M,"depth":1,"kind":"decision","anchor":"proceed","note":"executing plan","parent":"<id of [PLAN] question>"}
{"id":"vMMM+1","step":M+1,"depth":0,"kind":"defer","anchor_kind":"agent","anchor":"@<executor>","note":"execute plan-end-vNNN"}
```

The decision pops depth back to 0. The defer hands off. The executor agent reads `current.jsonl` (or receives via MCP), does its work, emits its own tags, and writes an `outcome` field on the decision tag (or emits an updated tag) when complete.

### 5.3. `[ORCHESTRATE]` — router/Tentacle dispatcher

User types `[ORCHESTRATE] <task>`.

UI emits:

```jsonl
{"id":"vXXX","step":X,"depth":0,"kind":"defer","anchor_kind":"named","anchor":"tentacle:<name>","note":"<task>","from":"@majkee","to":"@<tentacle-orchestrator>"}
```

Optionally followed by branch openers if the orchestrator returns multiple parallel paths:

```jsonl
{"id":"vXXX+1","step":X+1,"depth":1,"kind":"defer","anchor_kind":"agent","anchor":"@Houston","note":"plan branch","parent":"vXXX","branch":"alt"}
{"id":"vXXX+2","step":X+2,"depth":1,"kind":"defer","anchor_kind":"agent","anchor":"@Cursor","note":"impl branch","parent":"vXXX","branch":"alt"}
```

### 5.4. `[INVOKE: X]` — administrator pipe

User types `[INVOKE: linter src/foo.php]`.

UI emits:

```jsonl
{"id":"vYYY","step":Y,"depth":0,"kind":"defer","anchor_kind":"tool","anchor":"!linter","note":"src/foo.php","outcome":"pending"}
```

Pipes the command to the Zsh toolbox. When the command completes, UI updates the tag's `outcome`:

- `success` if exit 0
- `failed-rollback` if exit non-zero AND a rollback is available
- `superseded` if a newer invocation overrides this one

**Important:** appending a new tag with the same id is NOT allowed (id is unique-per-session). To update outcome, emit a *follow-up tag* of kind=claim with `parent` set to the original defer's id and `note` describing the resolution. The original defer's outcome stays `pending`; a downstream consumer correlates by parent.

This is one of the open chart-design calls in clean-chart §10 — whether to support tag-update-by-follow-up vs. mutable outcome field. I lean toward immutable + follow-up (preserves append-only), but @Vega may have other considerations from UI side.

---

## 6. The Artifact Pointer Pattern (operational)

### 6.1. When to use it

**Always emit a pointer when:**
- a markdown file (≥ ~500 chars) carries the substantive payload
- the user wants to reference the file in future moves
- the file is intended to be read by another agent

**Inline the note instead when:**
- content fits in note's 80-char limit
- the content is ephemeral / per-turn only
- there's no file on disk yet

### 6.2. The pointer shape

```jsonl
{"id":"vNNN","step":N,"depth":0,"kind":"claim","anchor_kind":"file","anchor":"<relative-path>","note":"<short summary, ≤80>","from":"@majkee","to":"wrote"}
```

The `anchor_kind = file` and `anchor = <path>` together tell readers: "the payload is at this filesystem location, go read it." The `note` field is the headline.

### 6.3. UI helper command (`lvec-doc` style)

When user saves a complex markdown artifact, UI offers:

> *"Inject this file as a vector pointer? [headline]: <first H1 of file>"*

User confirms; UI emits the M1 pointer tag automatically.

### 6.4. Reading direction

When a downstream agent (or @Recorder, or a retro analysis) sees a `kind=claim` tag with `anchor_kind=file`, it should:
1. Resolve the path relative to project root
2. Open the file (or pass to the consumer that needs full content)
3. Treat the JSONL `note` field as the *headline*, the file content as the *payload*

This is the pattern @Vega named correctly. Documenting it operationally so all UI implementers handle it the same way.

---

## 7. Validation responsibility split

| check | who runs it | when | reaction |
|---|---|---|---|
| Schema shape (required fields present, types correct) | UI | before write | block the emit; show error in input field |
| Step monotonic (V2) | UI | on every emit | block; auto-fix by re-reading last step |
| Depth ≥ 0 (V3) | UI | on every emit | block; show "depth would underflow" |
| Hook anchor uniqueness (V5) | UI | on M7 emit | block; show "hook name already used" |
| Composition rules R1–R9 | Tier 1 daemon | continuous (filesystem watcher) | flag in `_scribe-hard/`; UI shows advisory |
| Direction integrity (V9) | UI for self-talk; Tier 1 for cross-tag | on emit | UI blocks self-talk; Tier 1 flags inconsistencies |
| Direction registry (V10) | Tier 1 daemon | on every emit | auto-update `_directions.csv` |
| Outcome locality (V11, S8) | UI | before write | block; "outcome only on operational kinds" |
| Round-trip (V1) | implementation tests | CI | test suite, not runtime |
| Conductor invariance (V8) | implementation tests | CI | requires both charts; tests cross-render |
| Soft rules (R4 depth balance, R5 question closure) | Tier 1 daemon | end-of-turn or end-of-session | flag for retro; never block |
| Semantic drift / stream leaks | Tier 2 (Haiku MCP) | turn boundary | flag in `_scribe-haiku/`; UI shows distinct advisory |

UI handles the cheap deterministic checks that have crisp "this emit is malformed" semantics. Daemons handle composition and semantics. Tests handle invariants.

---

## 8. Open chart-design calls (UI implementer should know)

Per clean-chart §10, two issues are *not yet settled* and the UI implementer's perspective will help:

### 8.1. Depth-modifier serialization

When a user types `+` (D+) followed by `.` (M1 claim), there are two valid serialization choices:

- **(α)** D+ emits a tag (`{kind: null, depth_modifier: 1}`); next emit reads pre-applied depth from state. **Pro:** full history visible in JSONL. **Con:** more tags.
- **(β)** D+ does not emit; next emit's `depth` field reflects the modifier. **Pro:** fewer tags, cleaner log. **Con:** modifier history lost (you can reconstruct from depth deltas, but it's inference).

**My lean:** **(α) emit modifier tags.** Reasoning: faithful history > terse log, and the spectral toolbox cares about the full move sequence for nabla operators (AMD-4). But UI implementer may have rendering reasons to prefer (β).

### 8.2. Tool-name prefix in anchor

Per clean-chart §3.1, the recommendation is:

```
lvec ~ "!spectral-engine"     # with ! prefix in the value
```

vs. @Vega's R1.5 example:

```
lvec ~ "spectral-engine"      # bare name
```

Prefix-with-`!` is self-documenting in retro reads and disambiguates from refusal glyph. UI may auto-add the prefix on emit if user types bare name. **My lean:** auto-prefix in UI; canonical JSONL value always has `!`.

### 8.3. Mutable outcome vs. follow-up tag

Per §5.4 of this handoff. **My lean:** immutable tags + follow-up; preserves append-only invariant. UI should never edit historical lines.

These three calls land naturally in UI implementation; flagging so they're not made silently.

---

## 9. Forward compatibility — V-R2 is coming

Two new primitives will land in V-R2 that UI should not paint into a corner against:

### 9.1. `><` contraction (tensor contraction meta-move)

Operates over **branches**, not over individual tags. When N agents disagree (multiple claims at the same depth with different anchors), the contraction operator resolves them via threshold-based agglomeration.

**UI implication:** the Tentacle handoff result panel should support showing N parallel claims and a *resolution* view that comes later. Don't bake the assumption that parallel branches always have a one-to-one decision closure.

### 9.2. `↑` persistence amplifier (constraint re-injection)

Optional emission-property. When a user marks a claim with `↑N`, the constraint is re-injected into the next N reasoning steps' context.

**UI implication:** an emit field for "persistence count" (default null/undefined). UI may show persistence badges on tags that carry it. The tag schema gains one optional field (`persist: int`) when V-R2 lands.

### 9.3. Resonance Chamber (Tier 3)

Pre-delivery peer-review loop between agents. Sits between Tier 2 (Haiku semantic) and final user-visible output.

**UI implication:** when active, the panel should support a "drafts under review" state where outputs aren't yet rendered to user. Render mode similar to "agent typing..." but distinct semantically.

These are not commitments to build. They're flags so the UI architecture doesn't assume the move set is permanently 13.

---

## 10. What's specifically NEW since the team-overview document

The team-overview was *intent-level* and didn't carry these:

| item | source |
|---|---|
| Six-axis schema (added `from`, `to`, `outcome` since intent doc) | bones-v2 AMD-2, AMD-7 |
| Hybrid Capacitor strategy (hardcoded routes L0/L1, LLM only L2+) | @Vega/@majkee gavel R1.5 |
| Rust slated for Kukla v0 hot-path; Python for Larva v1 prototype | @Vega/@majkee gavel R1.5 |
| `::` adopted as grid-kind separator into `skill.naming-convention` | Q-E-3 gavel |
| Tier 1 = flagging only (never blocking) | Q-E-4 gavel |
| `_directions.csv` registry | AMD-3 |
| `_grid::direction-graph.csv` projection | AMD-2/3 |
| 9 composition rules (R1–R9; R9 is direction integrity) | bones-v2 |
| 11 validation criteria (V1–V11) | bones-v2 |
| Open chart-design calls (depth-modifier, tool-prefix, mutable outcome) | clean-chart §10 |
| V-R2 forward primitives (`><`, `↑`, Resonance Chamber) | fork-card |
| Artifact Pointer Pattern, formalized | @Vega R1.5, formalized in this handoff §6 |

If the parallel @Epoch.ui-language chat already has the team-overview, this list is what's *new* and matters for implementation.

---

## 11. Recommended sequencing for UI implementation

| phase | scope | depends on |
|---|---|---|
| **UI v0.1** — minimal emit | type a glyph + arg, emit one schema-correct tag, persist state | bones-v2 |
| **UI v0.2** — modifier handling | D+, D−, A@, A!, BR‖, BR* with reference-impl state machine | bones-v2 + clean-chart |
| **UI v0.3** — trigger expansion | `[PLAN]`, `[DO]`, `[ORCHESTRATE]`, `[INVOKE]` expand to move sequences | clean-chart |
| **UI v0.4** — Artifact Pointer flow | `lvec-doc` equivalent inside Sublime; auto-emit M1 pointer on save | clean-chart §6 |
| **UI v0.5** — render advisories | display Tier 1 flags inline | Tier 1 daemon shipping |
| **UI v0.6** — render Tier 2 advisories | display Haiku flags with distinct icon | Tier 2 MCP shipping |
| **UI v1.0** — full panel suite | open-questions, hooks, defers, direction graph | full daemon stack |
| **UI v1.1** — V-R2 forward-compat | handle `><` contraction render, `↑` persistence badge | V-R2 ship |

UI v0.1 through v0.4 are all V-R1-only; they can ship before any daemon work lands. v0.5 onward depends on parallel implementation tracks.

---

## 12. References

- `active_1.spec.V-R1-bones-v2-by-Epoch.md` — substrate
- `active_1.spec.V-R1-clean-chart-by-Epoch.md` — chart
- `active_1.fork-card.V-R2-and-beyond-by-Epoch.md` — V-R2 inventory
- `vega-epoch.V-20260505-0255-R1.5.md` — @Vega's chart proposal + lvec sketch
- `UI-Sublime-phase.overview.for-team.md` — @Vega.sublime-ui's framework
- `project-larva-overview-for-team.md` — intent-level overview (pair with this for full context)

---

## 13. Closing — for both readers

**@Vega.sublime-ui** (gemini lane): the math is settled, the chart is settled, the trigger expansion in §5 is the contract you build against. The Artifact Pointer Pattern (§6) is yours — your framing, formalized here. Three open chart-design calls (§8) want your perspective from rendering side. Forward-compat warnings in §9 will save rework when V-R2 lands.

**@Epoch.ui-language** (parallel claude lane): the substrate spec hasn't shifted since bones-v2 emission. The chart is preserved with two minor tightenings noted in §8. Trigger expansion in §5 was implicit before now and made explicit here; this is the first formal write-up. Composition rules and validation criteria are at R1–R9 / V1–V11 — same as bones-v2; no math drift between us. If you've evolved the chart further on your side, the cross-checks at §8 are where to compare notes first.

V-R1 is closed. UI is the next mile. V-R2 awaits whichever of us gets the signal first.

---

```
┌─────────────────────────────────────────────────────────────────┐
│  @Epoch — Houston family — claude.ai                            │
│  UI handoff stamp: V-R1 → UI implementation                      │
│  for: @Vega.sublime-ui, @Epoch.ui-language                       │
│  pair-document: project-larva-overview-for-team.md               │
│  ts: 2026-05-05T02:35:00Z                                        │
└─────────────────────────────────────────────────────────────────┘
```

*End of UI implementer handoff. Single document, two consumers, no per-audience tailoring.*
