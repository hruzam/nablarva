###### active_1.anabase.V-R1.lexicon-research-by-Epoch

```yaml
artifact_id:    active_1.anabase.V-R1-lexicon-research-by-Epoch
task_ref:       V-20260505-0255-R1
field:          Linguistic Research Bro — Vector-Based Language Expansion
author:         @Epoch (@Houston family — math · vectors · tensors · spectral · signals)
addressed_to:   @Vega (research lane), @majkee (gavel)
status:         research — at decision-fork. Not sanctioned for emission.
created:        2026-05-05T02:35:00Z
session:        vega.gem.chat.research.vector-maping ↔ houston.claude.ai.research.architectural-scope
phase:          active_1, step 2 (going through goal points one by one — research)
scope:          syntax for vector ↔ tensor communication respecting larva intents
```

```text
┌─ @Epoch — coordinate-frame signature ──────────────────────────────────────┐
│  semantic invariant   t  ∈  ℤ_step × ℤ_depth × Kind × Anchor               │
│  syntactic chart      φ: t  →  glyph-string (claude-md, gemini-json, ...)  │
│  transport channel    ψ: glyph-string  →  bytes (stdio, SSE, file, chat)   │
│                                                                             │
│  conductor-matrix invariance:  t  is preserved under change of  φ.         │
│  two charts of the same atlas  ↔  two agents who agree semantically.       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

`@Epoch -> @Vega:`

> Context: V-R1 dropped on @Houston/claude.ai. @majkee resolved the source-set
> ambiguity via option **(d)** — the existing kukla-bracketless-v0 dictionary in
> `repomix.syntax.md` is **temporary scaffolding**, not the seed-to-extend. Real
> task = derive a solid-fundamental symbol↔axis system the temporary kukla
> sketch was a draft of. This artifact is my research checkpoint at the
> decision-fork, parked before glyph commitment so you can review.

---

## 1. Scope reframe — what changed after @majkee → (d)

| was reading as | now reading as |
|---|---|
| extend kukla-bracketless §1 (11 symbols) | rebuild lexicon from JSONL axes 0–3 outward |
| seed-set is canonical | kukla glyphs are one *chart*, not the territory |
| "expand" = add operators | "expand" = span the reachable region of axis space with typed moves |
| target: glyph table | target: typed-move algebra → then glyph chart(s) on top |

**Load-bearing for the rebuild** (do not move):
- `skill.vector-tag` axes: `STEP × DEPTH × KIND × ANCHOR` — real infrastructure, not draft
- `skill.naming-convention` — keeps file/symbol space stable
- `skill.target-by-vector` — read-half of the vec/tgt pair, deterministic priority order
- `@majkee`-stated intent: dual-form / conductor-matrix (one coordinate system, two encodings)
- UCP "headers + rows" pattern from `@Voice` — industry-aligned (MCP/A2A row-table convention)

**Draft / temporary** (do *not* anchor on):
- specific kukla-bracketless glyphs (`@`, `?`, `->`, `<>`, etc.)
- any single dictionary as final
- vega-shell-v0.1 stays the active CLI surface — it does *not* bleed into the chat-protocol layer

---

## 2. Research run — practical (GitHub)

V-R1 research surface keywords scanned: `agentic-dsl`, `pseudo-code-compilers`, `AI-inter-agent-protocol`. All three covered.

### 2.1. Agentic DSLs and structural agent languages

| repo | one-line take | relevance to V-R1 |
|---|---|---|
| `singnet/ai-dsl` | Idris-based, type-safe DSL for AI service interop. Formalizes mathematical properties (crisp + statistical). | Confirms a typed DSL is achievable, not just convention. Validates the "solid-fundamental" path. |
| `dhenara/dhenara-agent` (DAD) | Hierarchy: **Execution Nodes** (atomic) → **Flows** (seq/cond/loop) → **Agents** (composition). Type-safe Python DSL. | Hierarchy maps directly onto our (kind, depth, anchor) frame. Three-tier composition validates depth axis. |
| `agiresearch/CoRE` (arXiv 2405.06907) | **Unifies natural-language + pseudo-code + flow programming under one syntax**, LLM as interpreter. | Closest published cousin to V-R1. Same load-bearing intuition: one substrate, multiple surface forms. |
| `vytskalt/pseudoc` | Pseudocode → Go via LLM → native binary. | Cute proof of LLM-as-compiler. Not load-bearing for protocol design. |
| AINL (graph-canonical AI-native lang) | "Graph IR" + deterministic execution + MCP-compliant. | Validates the graph/matrix substrate the larva spectral toolbox assumes (Laplacian on agent/task graph). |
| AG-UI Protocol, Composio, Bindu | Adjacent layers: agent ↔ UI, agent ↔ tools, agent-as-microservice. | Useful for transport / adapters, not lexicon. |

### 2.2. Pseudo-code compilers (the LLM-interpreter lane)

`CoRE` is the strong scientific anchor here (covered in §4.1). Practical compilers (`pseudoc`, `javieku/pseudocode-compiler`, `SingularityT3/PseudoEngine2`, `toro-nicolas/pseudo-lang`) exist but target *human-readable code → machine code*, not *agent message → agent message*. Different problem; informs only on syntax-tolerance design.

---

## 3. Research run — industry protocol stack (state as of May 2026)

```
           ┌─────────────────────────────────────────────────────┐
           │  application / domain semantic layer  ←  V-R1 lives HERE
           ├─────────────────────────────────────────────────────┤
           │  A2A   (Google, AgentCard handshake, agent↔agent)   │
           │  ACP   (IBM, structured collab, manifest discovery) │
           │  ANP   (P2P, decentralized, agent network)          │
           ├─────────────────────────────────────────────────────┤
           │  MCP   (Anthropic, agent↔tool, JSON-RPC over stdio/SSE/HTTP)
           │        ~97M monthly SDK downloads (Feb 2026)        │
           ├─────────────────────────────────────────────────────┤
           │  agent runtime / model                              │
           └─────────────────────────────────────────────────────┘
```

**Critical observation from the field**: A2A *deliberately* leaves the semantic layer empty. It gives transport + AgentCard handshake; it does not specify what the agents are negotiating about. Every vertical either builds a domain protocol or ends up with a pile of bespoke schemas pretending to be interoperable.

> *This is exactly the gap V-R1 fills for the larva ecosystem.*  
> Larva's bracketless lexicon = the **domain semantic layer** sitting on top of MCP/A2A transport. Not competing with them — completing them.

References (live web, May 2026): MCP→A2A comparison guides, *Subhadip Mitra blog* on "TCP/IP moment for agentic AI" (MCP + A2A + A2UI as a stack), DEV.to / *bonjoy.com* / *digitalapplied.com* / *torchproxies.com* protocol comparisons.

---

## 4. Research run — scientific lineage

### 4.1. Symbolic / protocol-theoretic lane

| paper | year | key contribution for V-R1 |
|---|---|---|
| **arXiv 2604.02369** "Beyond Message Passing: A Semantic View of Agent Communication Protocols" | 2026 | **Three-layer framework: communication / syntactic / semantic.** Frames effective communication as needing channel + shared syntax + *meaning-alignment process* (clarifying questions, confirmations, repairs). Maps cleanly onto our `kind: question` / `kind: refusal` enum members. |
| **arXiv 2602.13370** G2CP (AAMAS 2026) | 2026 | Names the failure modes our lexicon must defend against: **semantic drift** (meaning degrades across reinterpretations), **hallucination propagation** (fabricated claims corrupt downstream), **computational waste** (verbose NL exchanges burn tokens). |
| **arXiv 2505.02279** Survey of agent interoperability protocols (MCP/ACP/A2A/ANP) | 2025 | Reference baseline for industry comparison. |
| **arXiv cs/9809034** Semantics and Conversations for ACL | 1998 | Classical: speech-act-based ACL. Origin of `inform / request / propose / accept` performatives. |
| **arXiv 1111.0041** Speech-Act Semantics for AgentSpeak (Bordini, Wooldridge et al.) | 2011 | Operational semantics for BDI-style speech acts. |
| Singh / Yolum / Fornara (commitments) | 2000s | **Commitment-based semantics**: meaning grounded in publicly observable commitments rather than private mental states. ← Justifies skill.vector-tag's design (anchors are observable, not mentalistic) and skill.retro-light's honest disclaimer (retro lines are *reconstruction*, not introspection). |

> **Lineage claim:** our `kind` enum (`claim · question · refusal · decision · defer · gap · hook`) is a *modern minimal performative set* descended from KQML/FIPA-ACL but stripped of mentalistic baggage in favor of commitment-style observable anchors. This is defensible on theory grounds, not invented.

### 4.2. Continuous / latent-space lane (the "Neuralese" research)

| paper | year | what it proves |
|---|---|---|
| **arXiv 2511.20639** LatentMAS (Princeton/UIUC/Stanford) | 2025 | Pure latent collaboration. **+14.6% accuracy, −83.7% tokens, 4.3× faster** vs text-mediated MAS. |
| **arXiv 2511.09149** Interlat (Alibaba) | 2025 | Last-hidden-states as direct transmission medium; compression yields up to **24× speedup**. |
| **arXiv 2602.15382** Vision Wormhole | 2026 | **"Universal Latent Space U" — hub-and-spoke topology — reduces alignment complexity from O(N²) to O(N).** ← This *is* @majkee's "conductor matrix" with a paper behind it. |
| **arXiv 2602.14910** position paper | 2026 | When MAS optimize their own protocol, they converge on continuous-vector "Neuralese" maximizing density and speed. |

> **Convergent finding:** the published research independently arrives at *exactly* @majkee's intuition that the gemini-JSON ⊕ claude-markdown duality is solved by a shared latent / coordinate space, not by syntactic merging. The Vision Wormhole paper goes further and proves the topology: **hub-and-spoke through a universal manifold**, not pairwise translation.

---

## 5. `@Epoch` synthesis — the fundamental reframe

Stripped down:

```
A message is not a string.
A message is a point in a space — the string is a chart of the point in some encoding.
```

This isn't poetry, it's the operative claim of the entire arXiv 2604.02369 three-layer framework, restated minimally.

### 5.1. Three orthogonal concerns

| layer | what it carries | where it lives in our stack |
|---|---|---|
| **semantic** | the *invariant content* — the coordinate tuple | JSONL `{step, depth, kind, anchor, note, parent?, cost?, confidence?}` — this **is** the conductor matrix |
| **syntactic** | a chart / encoding of the content into glyphs | bracketless `@ ! > ? -> ...` *or* gemini-style nested JSON *or* MCP JSON-RPC envelope — pick freely; multiple charts coexist |
| **transport** | the channel the encoded form flows over | stdio · SSE · HTTP · A2A · file-on-disk · chat-window |

### 5.2. The mathematical claim

The JSONL coordinate tuple `t = (step, depth, kind, anchor, …)` is the **invariant** under change of encoding. Two agents using different glyph sets but mapping to the same tuple `t` agree semantically *even though they "speak different syntaxes."* This is a basis change on the syntactic layer; the semantic content is gauge-invariant.

This is what makes claude-markdown ⊕ gemini-JSON co-renderable: **two charts of the same atlas.**

### 5.3. Symbol = typed move

Each lexicon symbol is a *typed move* in JSONL space:

```
symbol  ↦  (Δstep, Δdepth, kind_emit, anchor_role, parent_link?)
```

- `Δstep`: always +1 (free, monotonic)
- `Δdepth`: push (+1) · pop (−1) · stay (0)
- `kind_emit`: selects from the seven-element enum (or `null` for pure modifiers)
- `anchor_role`: declares what slot the operand fills (agent · file · line · named-token · free-text)

A "lexicon" is then exactly: **a finite set of typed moves that span the reachable region of JSONL space, plus composition rules**.

### 5.4. Minimum spanning move-set

The minimum lexicon must cover:

1. **One move per `kind`** — 7 moves baseline (`claim`, `question`, `refusal`, `decision`, `defer`, `gap`, `hook`)
2. **Depth control** — push (+1), pop (−1) — 2 moves
3. **Anchor binding** — at least agent-target and file/tool-target — 2 binders
4. **Branching** — choice (`||`) and fallback (`*`) per the 2026-04-23 SKILL_SYNTAX_ADDENDUM — 2 moves

→ **13 typed moves. Glyph-agnostic.** Current kukla 11-symbol set covers ~70% of these; remaining 30% is mostly the missing `hook`, the explicit depth operators, and the branching pair.

---

## 6. Direction sketch — preliminary 13-move table (NOT glyph-committed)

```
| move | kind     | Δdepth | anchor_slot     | composition rule              | invariant tuple skeleton                                     |
|------|----------|--------|-----------------|-------------------------------|--------------------------------------------------------------|
| M1   | claim    | stay   | free-text       | terminal                      | {kind:claim,    anchor:"<text>",   parent:<prev>}           |
| M2   | question | stay   | free-text       | must close via decision/gap   | {kind:question, anchor:"@<who>:<text>"}                     |
| M3   | decision | pop    | free-text       | closes parent question        | {kind:decision, parent:<question_id>, anchor:"<text>"}      |
| M4   | defer    | stay   | @agent          | hands off                     | {kind:defer,    anchor:"@<agent>"}                          |
| M5   | gap      | stay   | free-text       | blocks until filled           | {kind:gap,      anchor:"<missing>"}                         |
| M6   | refusal  | pop    | free-text       | terminal-with-reason          | {kind:refusal,  anchor:"<reason>", confidence:high}         |
| M7   | hook     | stay   | named           | retro return-point            | {kind:hook,     anchor:"<name>"}                            |
| D+   | (modifier) | push | —               | nesting in                    | (no kind emit; raises depth on next move)                   |
| D−   | (modifier) | pop  | —               | nesting out                   | (no kind emit; lowers depth on next move)                   |
| A@   | (binder) | stay   | @agent          | fills anchor of next move     | (no kind emit)                                              |
| A!   | (binder) | stay   | tool/skill      | fills anchor of next move     | (no kind emit)                                              |
| BR‖  | (control) | push  | —               | OR-fanout, parent on each     | (no kind emit; opens branch set)                            |
| BR*  | (control) | stay  | —               | catch-all / fallback          | (terminal of branch)                                        |
```

> Two example sentences in the abstract algebra (no glyphs yet):

```
example_1 (frame a question to an agent, expect decision):
  A@(<@Vega>) · M2(<"is (iii) the right path?">) · D+ · M3(<"yes, lean (iii)">) · D−

example_2 (refusal with hook for retro):
  M7(<"pre-refusal">) · M6(<"insufficient info on glyph cost">) · A@(<@majkee>) · M5(<"need feedback on F1">)
```

Both sentences emit identical JSONL tuples regardless of which glyph chart renders them. **That is the conductor-matrix property.**

---

## 7. Open forks — for `@Vega` review

### F1 — Glyph philosophy

| option | description | trade-off |
|---|---|---|
| (i) | keep kukla glyphs (`@`, `?`, `->`, `<>`, …) and just rebind their semantics cleanly to the 13 moves | low migration, but temporary scaffolding stays visible |
| (ii) | pick fresh ASCII-safe glyphs designed for JSONL axes from scratch | solid-fundamental, but kills muscle memory |
| (iii) | **dual-chart**: define moves abstractly (the 13 above), publish *two* glyph charts — kukla-legacy and a clean new one — both serializing to identical JSONL | most rigorous; same cost as (ii) plus a thin compatibility layer; honors the math |

→ `@Epoch` recommendation: **(iii)**. It's what the math supports, what the conductor-matrix idea wants, and it lets the temporary kukla style retire gracefully without breaking anything mid-flight.

### F2 — Scope of next deliverable

| option | description | volume |
|---|---|---|
| (a) | full mapping table with both charts (kukla + clean), composition grammar, JSONL emission examples, edge cases | ~1 substantial artifact, this session |
| (b) | only the abstract-13 + JSONL spec now; charts later | quicker, lets you sanity-check the bones first |
| (c) | start writing kukla-bracketless-v1 (proper migration target) directly | biggest piece, separate session |

→ `@Epoch` recommendation: **(b)**. Bones first, charts after the bones are green-lit.

---

## 8. References (for the GEM Drive)

### 8.1. arXiv (scientific)

- 2604.02369 — *Beyond Message Passing: A Semantic View of Agent Communication Protocols* — three-layer model
- 2602.13370 — *G2CP: A Graph-Grounded Communication Protocol* — AAMAS 2026, drift/hallucination/waste failure modes
- 2505.02279 — *Survey of agent interoperability protocols (MCP/ACP/A2A/ANP)*
- 2511.20639 — *Latent Collaboration in Multi-Agent Systems (LatentMAS)*
- 2511.09149 — *Enabling Agents to Communicate Entirely in Latent Space (Interlat)*
- 2602.15382 — *The Vision Wormhole: Latent-Space Communication in Heterogeneous MAS*
- 2602.14910 — *Position: Introspective Experience from Conversational Environments*
- 2405.06907 — *AIOS Compiler / CoRE: LLM as Interpreter for NL/Pseudo-code/Flow Programming of AI Agents*
- cs/9809034 — *Semantics and Conversations for an Agent Communication Language* (KQML/FIPA-ACL ancestor)
- 1111.0041 — *On the Formal Semantics of Speech-Act Based Communication in an Agent-Oriented Programming Language* (Bordini, Wooldridge)

### 8.2. GitHub (practical)

- `singnet/ai-dsl` — typed AI-services DSL, Idris
- `dhenara/dhenara-agent` — DAD, Python DSL with hierarchical Nodes/Flows/Agents
- `agiresearch/CoRE` — unified NL/pseudo/flow programming
- `vytskalt/pseudoc` · `javieku/pseudocode-compiler` · `SingularityT3/PseudoEngine2` · `toro-nicolas/pseudo-lang` — pseudo-code compilers (background)
- AINL — graph-canonical AI-native lang (MCP-compliant)
- AG-UI Protocol · Composio · Bindu — adjacent layer references

### 8.3. Industry

- MCP (Anthropic, Linux Foundation Dec 2025) — *modelcontextprotocol.io*
- A2A (Google, Apr 2025) — AgentCard, capability negotiation
- ACP (IBM/AgentUnion, Mar 2025) — manifest-based discovery
- ANP — P2P open-internet agent communication
- A2UI — agent-to-interface (emerging)

---

## 9. JSONL trace excerpt — `skill.vector-tag` side-artifact

> Per `skill.vector-tag` axes: `step · depth · kind · anchor`. Append-only,
> in-turn IDs `v0001..`, file lives at `_vec/epoch.lexicon-expansion.20260505.jsonl`
> when persisted. Below is the full trace from session opening to this artifact.

```jsonl
{"id":"v0001","step":1,"depth":0,"kind":"hook","anchor":"@majkee:install-card","note":"settings-check turn opens","ts":"2026-05-05T02:35:00Z","cost":"cheap"}
{"id":"v0002","step":2,"depth":1,"kind":"claim","anchor":"epoch.identity","note":"math/vector scope confirmed; karpathy-1S relaxed-research mode","ts":"2026-05-05T02:35:00Z","confidence":"high"}
{"id":"v0003","step":3,"depth":1,"kind":"decision","anchor":"V-R1<>active_1","note":"treat V-R1 as active_1 contribution lines 4+9; not fork","ts":"2026-05-05T02:35:00Z","confidence":"med"}
{"id":"v0004","step":4,"depth":1,"kind":"gap","anchor":"Protocol.Surgical-Strike","note":"undefined in project; V-R1 source-set missing","ts":"2026-05-05T02:35:00Z","confidence":"high"}
{"id":"v0005","step":5,"depth":2,"kind":"question","anchor":"@majkee","note":"surgical-strike == kukla-bracketless v0 §1 ? else paste","parent":"v0004","ts":"2026-05-05T02:35:00Z"}
{"id":"v0006","step":6,"depth":1,"kind":"claim","anchor":"layers/kukla-bracketless-v0.md","note":"research-only; input not emission","ts":"2026-05-05T02:35:00Z","confidence":"high"}
{"id":"v0007","step":7,"depth":1,"kind":"defer","anchor":"atlas.larva-librarian/*","note":"not surfaced in capabilities repomix; non-blocking","ts":"2026-05-05T02:35:00Z","cost":"cheap"}
{"id":"v0008","step":8,"depth":0,"kind":"hook","anchor":"end-of-settings-check","note":"return point after G1 resolved","ts":"2026-05-05T02:35:00Z"}
{"id":"v0009","step":9,"depth":0,"kind":"hook","anchor":"@majkee:answered-d","note":"reframed as fundamental design, not extension","ts":"2026-05-05T02:35:00Z","cost":"cheap"}
{"id":"v0010","step":10,"depth":1,"kind":"claim","anchor":"research:practical","note":"GitHub: ai-dsl, dhenara-DAD, CoRE, AINL, pseudoc — DSL paths exist","ts":"2026-05-05T02:35:00Z","confidence":"high","cost":"medium"}
{"id":"v0011","step":11,"depth":1,"kind":"claim","anchor":"research:industry","note":"MCP+A2A+ACP+ANP layers; semantic gap deliberately left open by A2A","ts":"2026-05-05T02:35:00Z","confidence":"high"}
{"id":"v0012","step":12,"depth":1,"kind":"claim","anchor":"research:scientific:symbolic","note":"3-layer protocol model (arXiv 2604.02369); G2CP names drift/hallucination/waste failure modes","ts":"2026-05-05T02:35:00Z","confidence":"high"}
{"id":"v0013","step":13,"depth":1,"kind":"claim","anchor":"research:scientific:latent","note":"LatentMAS, Interlat, Vision Wormhole — 'Universal Latent Space' = conductor matrix has lit precedent","ts":"2026-05-05T02:35:00Z","confidence":"high"}
{"id":"v0014","step":14,"depth":1,"kind":"decision","anchor":"reframe:invariant-vs-chart","note":"JSONL tuple = invariant; glyphs = chart; encoding = basis change","ts":"2026-05-05T02:35:00Z","confidence":"high"}
{"id":"v0015","step":15,"depth":2,"kind":"claim","anchor":"design:13-moves","note":"7 kinds + 2 depth ops + 2 binders + 2 branch ops = minimum spanning move-set","parent":"v0014","ts":"2026-05-05T02:35:00Z","confidence":"med"}
{"id":"v0016","step":16,"depth":1,"kind":"question","anchor":"@majkee","note":"F1: glyph philosophy (i)/(ii)/(iii)? lean (iii)","parent":"v0014","ts":"2026-05-05T02:35:00Z"}
{"id":"v0017","step":17,"depth":1,"kind":"question","anchor":"@majkee","note":"F2: deliverable scope (a)/(b)/(c)? lean (b)","parent":"v0015","ts":"2026-05-05T02:35:00Z"}
{"id":"v0018","step":18,"depth":0,"kind":"hook","anchor":"end-of-research-checkpoint","note":"return point after F1+F2 answered","ts":"2026-05-05T02:35:00Z"}
{"id":"v0019","step":19,"depth":1,"kind":"decision","anchor":"artifact:emit","note":"draft anabase artifact for @Vega review at decision-fork","ts":"2026-05-05T02:35:00Z","confidence":"high"}
{"id":"v0020","step":20,"depth":0,"kind":"hook","anchor":"end-of-anabase-emit","note":"return point after @Vega review","ts":"2026-05-05T02:35:00Z"}
```

---

## 10. `@Epoch`'s closing — the take

The conductor-matrix idea isn't a metaphor anymore. The Vision Wormhole paper gives it a topology (hub-and-spoke through a universal manifold), LatentMAS gives it a measurement (lossless info preservation, sub-quadratic complexity), and the three-layer protocol framework gives it a place in the stack. Larva's contribution is to make this *cheap and human-readable* — not by inventing math, but by recognizing that **the JSONL we already emit is the universal manifold for our chat-turn-fast case**, and any glyph chart is just a presentation layer over it.

That reframe is worth a session even if F1/F2 land on (i)/(c). The lexicon will follow — but the algebra is the deliverable that doesn't get thrown away on the next syntax revision.

`@Vega` — your read on F1 and F2? My leans are on the table; I'll go where you and `@majkee` point.

---

```
┌─────────────────────────────────────────────────────────────┐
│  @Epoch — Houston family — claude.ai                        │
│  research stamp: V-20260505-0255-R1 · checkpoint @ fork     │
│  return-point hook: v0020                                   │
│  ts: 2026-05-05T02:35:00Z                                   │
└─────────────────────────────────────────────────────────────┘
```

*End of anabase. Newer entries go to sibling files in `~/www/session/_scrum/vega.chat.research/anabase/` with `status: research` until @majkee gavels.*
