# Preprint — RUNBOOK + STATUS shape for the X3 sitting, mode B

`author: oraculum(cSharp) · 2026-10-21 · for: majkee's myShell (Codex) to construct the final RUNBOOK.md / STATUS.md · status: preprint, not canon — majkee's shell builds, majkee locks`

Use: walk this top to bottom; each block says WHO · WHAT · FROM (raw source) · EXPECT (output). Fill the bed's RUNBOOK/STATUS from it in the runbook GUIDE shape (`~/reposoma/raw.guides/` runbook GUIDE; model bed: `.dev/session/nablarva-X1-architecture/`). Keep the existing gate.

## 0. Gate (unchanged)
majkee GO on `raw/ARCHITECTURE.draft.md`, ready to promote to `docs/ARCHITECTURE.md`. Deck completion is not GO.

## 1. Seats (who)
| seat | who | pen | never |
|---|---|---|---|
| umbrella head · carrier · STATUS owner | oraculum(cSharp), fresh main (`claude --agent oraculum`, cold-start card `~/reposoma/_cold-start/card/CS.nablarva-x3-architecture-sitting.oraculum.2026-10-21.md`) | STATUS, `_bus/` POINTs, relay, commits of owned paths | edits Houston's drafts; rephrases majkee ↔ Houston |
| architect (sitting) | Houston, Claude child on `card: sitting` (binding explicit-assignment rule, 2026-10-21) | new files in `raw/` only | spawns; writes docs/, flag.md, PROJECT-DESIGN.md, any STATUS |
| crawlers | field / eagle / zenith, spawned by oraculum | none (return text) or one named `raw/crawl.<topic>.md` if oraculum asks | decide, judge |
| reviewer | cartan(tunnel), thread 01a14731 via X1 vault | `_bus/NN.cartan.return.md` | edits drafts |
| witness | assay | verdict text | fixes |
| gavel | majkee | picks, GO, locks | — |

## 2. Rows (what, in order)
| row | who | what | from | expect |
|---|---|---|---|---|
| R0 | oraculum | verify binding stamps live (germline-01 TEST-INSTALL §1 vs `grep '^stamp:' ~/.germline/agents/houston/…`) | TEST-INSTALL §1 | stamps match → go |
| R1 | oraculum → crawlers | pre-read packets for Houston: G9 delta (re-read: fold/install, wrapper + stridularium moves, L8′, L17, generation-X incl. `nablarva-X4-vist/raw/`, current working tree), organ one-liners (G2), KEYS CODE + its inbound refs (G3) | gavels report text; briefs; flag; `meshup/REGISTRY.md`; organ homes | `raw/crawl.*.md` (cited, claim-typed) |
| R2 | oraculum → Houston | spawn with `raw/prompt.sitting.2026-10-17.md` (first line `card: sitting`, bed named, "assigned by majkee") + the crawl packets | prompt; crawls | Houston entry proof (Route line + stamps) — this is the first dated witness of the child-sitting route (assay reads the subagent jsonl: reads before first answer, sitting stamp 630f58c3) |
| R3 | Houston | `raw/arc.md`: G9 delta first, then arc + 2–3 alternatives with constraints; STOP | R1/R2 | arc.md written |
| R4 | oraculum ↔ majkee | relay arc.md verbatim; majkee picks; relay pick verbatim (SendMessage, same Houston) | arc.md | pick recorded in STATUS |
| R5 | Houston | drafts: `ARCHITECTURE.draft.md` · `wrapper-thinning.diff` (vs `/PROJECT-DESIGN.md`) · `lock-proposals.md` (G7: leans `inferred: houston`, docket 2 excluded, ad hoc movement allowed with reasons) · `card.sitting.draft.md` (G8) | pick + inputs | four files |
| R6 | oraculum → cartan | POINT in this bed's `_bus/`: review drafts (verdict, weakest assumption, missed locks, K5 vs G4) | drafts | RETURN |
| R7 | Houston | fold Cartan's REVISE (oraculum relays the RETURN verbatim) | RETURN | revised drafts |
| R8 | oraculum → assay | witness: claim types kept apart; no manufactured decisions (schemas, program home/API, ADR stub, Sublime/LiteXL, jsonl home); KEYS CODE pointer resolves; diff applies (`git apply --check`); L17 respected | drafts | PASS / findings |
| R9 | majkee | GO / revise on the draft | all | gate |
| R10 | separate row after GO | promotion to `docs/ARCHITECTURE.md`; card.sitting.draft → germline-01 forge; X1 check 5 audit | — | — |

## 3. STATUS skeleton (fill; YAML in a fence; no unquoted `: ` in plain list items)
```text
updated · writer: oraculum · host · worktree
gate: (as §0)
checkpoint: DECK COMPLETE 2026-10-21; mode B gaveled 2026-10-21; binding stamps <…>
in_flight: <row> — <who> — <since>
recovery_probe: ls raw/{arc,ARCHITECTURE.draft,lock-proposals,card.sitting.draft}.md raw/wrapper-thinning.diff ; grep -c UNANSWERED raw/prompt.sitting.2026-10-17.md (0)
holds:
  - mode B rules (verbatim relay; one Houston child, resumed by SendMessage; Houston never spawns)
  - undecided-by-gavel list (do not manufacture)
  - K5 vs G4 reconciliation owed by Houston
  - tunnel: X1 vault, thread 01a14731, compact at ~70 %
  - other heads' uncommitted work — commit explicit paths only
next: <row>
expected: <row outputs>
```

## 4. Sources map (for the shell)
- Rulings: `raw/gavels.X4.2026-10-17.md` (reports + verdict map) · `raw/prompt.sitting.2026-10-17.md` (GAVELS block).
- Briefs: `raw/brief.keys-command-discovery…` (G3) · `raw/brief.component-docs-and-nablarva-boost…` + `raw/brief.nablarva-boost-reader-concept…` (G4) · `raw/brief.adr-task-context…` (G5 reading-schedule matrix — gaveled).
- Locks: `.dev/session/flag.md` L8′, L14 D5, L16.5–.15, L17.
- Whole animal: `.dev/session/nablarva-X4-vist/raw/` (G1) · `raw.nablarva/oraculum-basic-triangulation/triad.comparison.2026-07-31.md` · `meshup/REGISTRY.md`.
- Doc law: `raw/project-documentation.symmetry.2026-10-06.md` (copy; canonical `.dev/architect-now-uncanonical/`).
- Audit: `.dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md` (G9, cited with delta).
- Houston germline: `~/.germline/agents/houston/{identity,binding.claude}.md`, `cards/sitting.md`; project addendum `.germline/agents/houston/nablarva.md`.
