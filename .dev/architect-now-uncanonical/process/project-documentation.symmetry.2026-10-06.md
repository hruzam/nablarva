---
doc: project-documentation
seat: Symmetry (claude.ai · Opus) — fold author, side-quest research
date: 2026-10-06
status: DRAFT · un-gaveled · contrast-signature pending (wave)
read_at: nablarva@3547e3c (PROJECT.yaml as read @6dbe97b)
research: web, 2026-10-06; sources at the end
siblings: architecture-process.symmetry.2026-10-06.md · houston.symmetry.2026-10-06.md
---

# Project documentation: the animal's index

This file owns the shelf: where each kind of truth lives, how the docs grow with the animal, and the rules that keep an index cheap. The workflow is in `architecture-process`. The seat that keeps the shelf honest is in `houston`.

## Axioms

| id | axiom | wave |
|---|---|---|
| K1 | At nablarva's size, documentation is a map, not a retrieval system: an index, key files and grep. No vector index for dev-time navigation. | |
| K2 | PROJECT.yaml maps, PROJECT-DESIGN describes, flag locks, pulse routes. Content never crosses those lines. | |
| K3 | PROJECT-DESIGN.md is a thin wrapper: a few lines on the animal, a line or two per organ, pointers out. | |
| K4 | One home per fact. The index points; it never copies. | |
| K5 | Born thin, promoted on need: a line, then a sub-chapter, then an organ folder. | |
| K6 | Staleness is declared, never hidden. Age is a candidate, not a finding. | |
| K7 | Doc claims are testable. Grep before you trust. | |
| K8 | Move up a tier only when a measurement indicts the current one. | |

## The stack, one home each

| surface | is | holds | never holds |
|---|---|---|---|
| `PROJECT.yaml` | machine map | skeleton facts, pointers | prose; invariants as text |
| `PROJECT-DESIGN.md` | the wrapper | the animal in a few lines, one line per organ, pointers, `checked:` stamps | organ detail, tables, dated notes |
| organ body | the detail | contract, key files, decisions in force, trajectory notes | another organ's facts |
| whole-animal body | cross-organ detail | layer model, dependency direction, shared grammars (KEYS CODE) | one organ's detail |
| `flag.md` | locks | L-ids, docket, deferral thresholds | descriptions |
| `pulse.md` | router | one line per live session | next actions, narrative |
| session folder | the work | briefs, raw, RUNBOOK, STATUS | durable truth (promoted out at closure, then pruned) |

Most of this is already law. PROJECT-DESIGN's own *Document role* sends locks to flag, the machine contract to PROJECT.yaml, and live work to STATUS via pulse. It also says the wrapper carries description and pointers, not a second progress register. The runbook GUIDE says to point at canon and never reproduce it. This fold adds only three things: the thinness rule, the growth law, and a keeper once convergence retires.

## Growth law

1. **Born thin.** A new organ is one or two lines in the wrapper: what it is and where its body lives.
2. **Sub-chapter.** Once an organ has its own contracts or decisions, they go in its body under their own headings. Its wrapper line doesn't grow.
3. **Folder.** When the body outgrows a page, it becomes a folder with its own small index, the same shape one level down.
4. **Archive.** A retired organ's line moves under `## Archived index` with what replaced it, as L15 does for flag. Nothing goes to an archive dir.

The wrapper stays a few lines per organ however large the animal gets. That keeps both reading it and auditing it cheap.

## Ten rules

1. **Map, not encyclopedia.** The entry file routes and never dumps. In a long entry file, pointers get lost.
2. **One home per fact.** A fact in two places has forked. This is the trap L9′ names for state, applied to docs.
3. **Durable docs use capability and domain words, not line numbers.** Paths rot, and a stale path sends an agent confidently to the wrong place. RUNBOOKs can keep absolute paths, because they die with the gate before paths rot.
4. **Every organ body names its key files.** Docs that reach the right directory but not the files make every agent grep for the same entry points.
5. **Declare staleness.** Each organ line carries a `checked:` date. The wrapper's floor is the oldest one.
6. **Age is a candidate, not a finding.** Old means "check me." Report verified-wrong separately from flagged-by-age.
7. **Grep before you trust.** Every key file and example a doc names must exist in the code. A one-line check catches the dead ones.
8. **Born thin, promoted on need.** This is the growth law above.
9. **Recipes become tools.** A procedure agents keep re-reading becomes a script, and its paragraph shrinks to one line.
10. **Measure before you upgrade.** Track time to the first relevant file, tokens per task, and staleness incidents. Upgrade only the layer the numbers indict.

Rules 3 and 4 pull against each other in the sources. The reconciliation (`inferred: symmetry`) is to keep stable words in the wrapper and key files in organ bodies, with rule 7 keeping both honest.

## Tiers

- **Tier 0, now.** The wrapper, organ bodies with key-files blocks, grep, and staleness stamps. No new dependencies. The better the index, the cheaper the audit.
- **Tier 1, earned.** A script that checks or regenerates the index: it lists organs, resolves pointers, computes the staleness floor and greps key files. Its output is still markdown. Earned at ≥2 stale-pointer findings in one audit.
- **Tier 2, a different question.** Semantic or vector retrieval is a product feature for a large unstructured corpus, if nablarva one day has to answer from one. It isn't a dev-time doc tool, because coding agents already search the repo themselves. A corpus can earn it; code navigation never does.

At nablarva's size, nothing found argues for leaving tier 0.

## Measuring

The project already has a measurement shape: L11's pre-registered M2 benchmark for termbrana (frozen sessions, retrieval tasks, median time-to-locate vs native, success ≥ native). Reuse it for the index rather than inventing a new one. The cheapest probe is to give a fresh agent intent-only change requests and count how many reach the right files without falling back to grep.

## Migration notes (@3547e3c)

- **KEYS CODE** is a cross-organ grammar, not one organ's detail; its own text says the same key means the same thing in every organ. It moves to the whole-animal body, and the wrapper keeps one line and a pointer. Its DRY rule is already one home per fact.
- **KEYS CODE's acceptance cite** points into `ovitmugen-01-basement/raw/` and dies when that session is pruned. Pin it (`nablarva@<sha>:path`), or carry D3's text across with its acceptance date before the prune.
- **@Trajectory notes** (§3.2.x) belong to ovitmugen, so they go to ovitmugen's body.
- **VOLATILE** (the delivery route) stays as a short wrapper section. It covers the whole animal and is already pointer-shaped.
- **Status.** The doc's own rule already makes authority per statement: proposals unless a cited decision backs them. Once thin, the wrapper asserts almost nothing itself. PROJECT.yaml's "draft, not canon" comment could read `index; authority lives where it points`.
- **Keeper.** When convergence retires (currently seated by Cartan), PROJECT.yaml's `docs.project-design-maintainer` and the wrapper's `maintainer:` frontmatter both point at Houston's audit card.

## Open (gavel: Majkee)

**Is `docs/ARCHITECTURE.md` the whole-animal body?** Today it's a pointer that promises "the first real architecture doc" after the docket closes. Giving it this one job avoids two wrappers. PROJECT-DESIGN would index, and docs/ARCHITECTURE.md would hold what crosses organs, which is also where sittings land. The alternative is folding it into the wrapper. Lean: the first.

## Sources

Web, 2026-10-06. These are practitioner reports and vendor-adjacent posts, not benchmarks. The direction is unanimous; the magnitudes are unmeasured.

- Coding agents dropping vector indexes for on-demand search with lightweight references: https://buzzgrewal.medium.com/ai-agents-dont-need-vector-search-anymore-inside-the-agentic-search-stack-replacing-rag-in-2026-58efcabe4f6f
- RAG as a product feature rather than a dev tool; keep standing instructions short: https://aliteq.com/agentic-search-vs-rag
- The infrastructure any index drags in (chunking, sync, invalidation, ranking): https://dev.to/nimay_04/rag-is-not-always-the-answer-anymore-how-ai-agents-search-code-in-2026-43m3
- Agentic search as the backbone, a semantic index only where needed, three KPIs: https://smartscope.blog/en/ai-development/practices/rag-debate-agentic-search-code-exploration/
- One fact per file; grep docs against code: https://dev.to/hash01/how-to-structure-claudemd-skills-and-agents-2p7a
- Declared staleness, with the floor visible in the index: https://www.fmind.dev/articles/agent-docs-answer-locally-before-the-web-a-shared-reference-for-every-coding-agent/
- A blind audit where docs reached the module but not the files, fixed with key-files blocks: https://github.com/hjung3113/FeedbackOps/issues/598
- Stale paths mislead agents; document capabilities and domain concepts instead: https://www.aihero.dev/a-complete-guide-to-agents-md
- Entry files that route vs dump; verified-wrong vs flagged-by-age: https://github.com/jonhill90/agent-estate/issues/1397
- Oversized entry files lose pointers; recipes turned into tools: https://github.com/mattiasbrandt/protoArtoo/issues/465
