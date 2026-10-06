---
doc: project-documentation
seat: Symmetry (claude.ai · Opus) — final fold, side-quest research
date: 2026-10-06
version: final (supersedes this file's earlier draft of the same day)
status: FINAL · gaveled in conversation (majkee, 2026-10-06) · becomes a lock when L16 lands in flag
read_at: nablarva@3547e3c (PROJECT.yaml as read @6dbe97b)
research: web, 2026-10-06; sources at the end
triad: architecture-process · project-documentation · houston (.symmetry.2026-10-06)
---

# Project documentation: the animal's index

This file is about the shelf. It says where each kind of truth lives, how the docs grow along with the animal, and which rules keep an index cheap. The workflow is in `architecture-process`, and the seat that keeps the shelf honest is in `houston`.

## Axioms

| id | axiom | decided in |
|---|---|---|
| K1 | At nablarva's size, documentation is a map, not a retrieval system: an index, key files and grep. There's no vector index for dev-time navigation. | L16.7 |
| K2 | Each kind of truth has one home. PROJECT.yaml maps, PROJECT-DESIGN indexes, docs/ARCHITECTURE.md holds what crosses organs, organ bodies hold local detail, flag locks, and pulse routes. | L16.9 |
| K3 | PROJECT-DESIGN.md is a thin wrapper: a few lines on the animal, a line or two per organ, and pointers outward. | L16.10 |
| K4 | Each fact has one home. The index points to it and never copies it. | L16.10 |
| K5 | Born thin, promoted on need: a line first, then a sub-chapter, then a folder. | L16.10 |
| K6 | Staleness is declared, never hidden. Age makes something a candidate, not a finding. | L16.10 |
| K7 | Claims are tested by type. Mechanical claims get tested, architectural claims get cited, and unknowns stay unknown. | L16.10 |
| K8 | Move up a tier only when a measurement shows the current tier failing. | L16.7 |

In the contrast, wave bent K7: architecture is not grep compliance. Wave also voted GO on `docs/ARCHITECTURE.md` as the whole-animal body and withdrew its own `.dev/architecture/`.

## The map

```text
PROJECT.yaml ────────── machine skeleton · pointers
   │
   ▼
PROJECT-DESIGN.md ───── the wrapper: silhouette · organ one-liners · checked: stamps
   │
   ├──► docs/ARCHITECTURE.md ─── whole-animal body: layer model · dependency direction ·
   │                             shared grammars · cross-organ ownership
   │
   └──► organ bodies ─────────── contract · key files · decisions in force · trajectory

beside the map:
   flag.md ──── locks
   pulse.md ─── live-session router
   sessions ─── temporary work: briefs · raw · RUNBOOK · STATUS · evidence
```

| surface | role | holds | never becomes |
|---|---|---|---|
| `PROJECT.yaml` | machine map | skeleton facts, canonical pointers | a prose encyclopedia |
| `PROJECT-DESIGN.md` | the wrapper: the animal's index | the animal in a few lines, organ one-liners, pointers, `checked:` stamps | organ detail, a progress register |
| `docs/ARCHITECTURE.md` | whole-animal body | layer model, dependency direction, shared grammars, cross-organ ownership, system-wide boundaries | one organ's detail |
| organ body | local detail | contract, key files, decisions in force, trajectory notes | another organ's truth |
| `flag.md` | locks | L-ids, docket, deferral thresholds | a descriptive duplicate |
| `pulse.md` | live router | one line per live session | next actions, narrative |
| session folders | temporary work | briefs, raw, RUNBOOK, STATUS, evidence | durable truth (promoted out at closure, then pruned) |

Most of this is already law. PROJECT-DESIGN's own *Document role* sends locks to flag, the machine contract to PROJECT.yaml, and live work to STATUS via pulse. It also says the wrapper carries description and pointers, not a second progress register. The runbook GUIDE says to point at canon and never reproduce it. What this fold adds is the thinness rule, the growth law, the whole-animal body, and a keeper.

## Growth law

```text
new organ
  │  one or two wrapper lines: what it is, where its body lives
  ▼
sub-chapter
  │  its contracts and decisions grow in its own body; the wrapper line stays put
  ▼
folder
  │  outgrows a page: a folder with its own small index, same shape one level down
  ▼
archive
     retired: its line moves under ## Archived index, naming its replacement (L15)
```

However large the animal gets, the wrapper stays at a few lines per organ. That keeps both reading it and auditing it cheap.

## Ten rules

1. **Map, not encyclopedia.** The entry file routes and never dumps; in a long entry file, pointers get lost.
2. **One home per fact.** A fact that lives in two places has forked. This is the trap L9′ names for state, applied to docs.
3. **Durable high-level docs prefer capability and domain words over brittle paths and line numbers.** A stale path sends an agent confidently to the wrong place. RUNBOOKs can keep absolute paths, because they die with the gate before the paths rot.
4. **Every organ body names its key files.** If docs reach the right directory but not the files, every agent ends up grepping for the same entry points.
5. **Declare staleness.** Each organ line carries a `checked:` date. The wrapper's floor is the oldest of them.
6. **Age is a candidate, not a finding.** Old means "check me." Report verified-wrong separately from flagged-by-age.
7. **Test claims by type.** See *Claim types* below.
8. **Born thin, promoted on need.** See the growth law above.
9. **Recipes become tools once repeated use earns automation.** The paragraph then shrinks to a pointer.
10. **Measure before you upgrade the machinery.** Track time to the first relevant file, tokens per task, and staleness incidents.

Rules 3 and 4 pull against each other in the sources. My reconciliation (`inferred: symmetry`): stable words go in the wrapper, key files go in organ bodies, and rule 7 keeps both honest.

### Claim types

```text
a doc claim
  ├── mechanical ────► test it  file exists · pointer resolves · symbol · script
  ├── architectural ─► cite it  lock · code boundary · evidence · runtime observation
  └── unknown ───────► say so   never upgraded to fact

architecture is not grep compliance
```

## Tiers

```text
tier 2 ┐ semantic / vector retrieval
       │ a product question: only a large unstructured corpus with measured
       │ retrieval failure earns it; code navigation never does
tier 1 ┤ a checker / regenerator script; output stays markdown
       │ earned at ≥2 stale-pointer findings in one audit
tier 0 ┘ wrapper · docs/ARCHITECTURE.md · organ bodies with key files ·
         grep · checked: stamps; now, with no new dependencies
```

At nablarva's size, nothing I found argues for leaving tier 0.

## Measuring

The project already has a measurement shape: L11's pre-registered M2 benchmark for termbrana (frozen sessions, retrieval tasks, median time-to-locate against native, success ≥ native). Reuse it for the index instead of inventing a new one. The cheapest probe is to give a fresh agent intent-only change requests and count how many reach the right files without falling back to grep.

## Migration notes (@3547e3c)

- **docs/ARCHITECTURE.md** is a "pointer (no build yet)" today, and it becomes the whole-animal body.
  - Its *shape of record* pointer stays on as the first section.
  - Its promised `decisions/` folder stays unbuilt until it's earned. Any ADR that does land there is product-technical and cites the flag line that authorizes it, the pattern L11 set for termbrana.
- **KEYS CODE** is a cross-organ grammar: the same key means the same thing in every organ. It moves to docs/ARCHITECTURE.md, and the wrapper keeps one line and a pointer to it. Its DRY rule is already one home per fact.
- **The KEYS CODE acceptance cite** points into `ovitmugen-01-basement/raw/`, so it dies when that session is pruned. Pin it (`nablarva@<sha>:path`), or carry D3's text across with its acceptance date before the prune.
- **@Trajectory notes** (§3.2.x) belong to ovitmugen, so they go to ovitmugen's body.
- **VOLATILE** (the delivery route) stays as a short section in the wrapper. It covers the whole animal and is already pointer-shaped.
- **Status.** The wrapper's own rule already makes authority per statement: everything is a proposal unless a cited decision backs it. PROJECT.yaml's "draft, not canon" comment could read `index; authority lives where it points`.
- **Keeper.** When convergence retires (it's currently seated by Cartan), the wrapper's `maintainer:` frontmatter and PROJECT.yaml's `docs.project-design-maintainer` both point at Houston's audit card (L16.14, proposed).

## Open (gavel: Majkee)

**Where organ bodies live before the structure earns them.** My proposal (`inferred: symmetry`):

- An organ that already has a home keeps its body there. For example, termbrana lives at `toolbox/termbrana/` with its own `DECISIONS.md` under L11.
- Otherwise, the body starts as one file, `docs/organs/<organ>.md`, and becomes a folder, `docs/organs/<organ>/`, once it outgrows a page.
- The wrapper points at whichever applies.

## Sources

Web, 2026-10-06. These are practitioner reports and vendor-adjacent posts, not benchmarks. They all point the same way, but none of them measures how much.

- Coding agents dropping vector indexes for on-demand search with lightweight references: https://buzzgrewal.medium.com/ai-agents-dont-need-vector-search-anymore-inside-the-agentic-search-stack-replacing-rag-in-2026-58efcabe4f6f
- RAG as a product feature rather than a dev tool, and standing instructions kept short: https://aliteq.com/agentic-search-vs-rag
- The infrastructure any index drags in (chunking, sync, invalidation, ranking): https://dev.to/nimay_04/rag-is-not-always-the-answer-anymore-how-ai-agents-search-code-in-2026-43m3
- Agentic search as the backbone, a semantic index only where needed, and three KPIs: https://smartscope.blog/en/ai-development/practices/rag-debate-agentic-search-code-exploration/
- One fact per file, and grepping docs against code: https://dev.to/hash01/how-to-structure-claudemd-skills-and-agents-2p7a
- Declared staleness, with the floor visible in the index: https://www.fmind.dev/articles/agent-docs-answer-locally-before-the-web-a-shared-reference-for-every-coding-agent/
- A blind audit where docs reached the module but not the files, fixed with key-files blocks: https://github.com/hjung3113/FeedbackOps/issues/598
- Stale paths mislead agents, so document capabilities and domain concepts: https://www.aihero.dev/a-complete-guide-to-agents-md
- Entry files that route versus ones that dump, and verified-wrong versus flagged-by-age: https://github.com/jonhill90/agent-estate/issues/1397
- Oversized entry files lose pointers, and recipes get turned into tools: https://github.com/mattiasbrandt/protoArtoo/issues/465
