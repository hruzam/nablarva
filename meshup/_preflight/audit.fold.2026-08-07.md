# audit.fold.2026-08-07 — @Assay verification of corpus-fold

**Verdict: FAIL** (completeness gate — two source files silently dropped from the entire navigation layer)

## 1. Synthesis-creep
No sentence found that explains what an idea MEANS rather than pointing to it. All per-file descriptors trace to near-verbatim text in `map.meshup.field.2026-08-07.md` or `map.reposoma.epoch.2026-08-07.md` (spot-checked several against source maps — exact or trivially-reworded matches). The "What tyler does with it" bullets (one per doc) are borderline: they aggregate keywords already present in individual descriptors into a scope-framing sentence ("enters the corpus of how one CLI behaves as a programmable substrate…"). This is navigational scope-setting, not new interpretation of content meaning — judged compliant, but flagged as the closest-to-the-line material in all four docs.

## 2. Fork fidelity — PASS
F1–F5 all present, both branches, none collapsed:
- F1 (CREATURE vs primary-larva) — task.T3-T4, both branches + gavel-pending status preserved.
- F2 (Python vs C++) — task.T3-T4, both branches, "only majkee weighs" preserved.
- F3 (`-p` use vs exclude) — task.T2, both branches, billing-uncertainty caveat preserved, routed to DECISIONS not auto-resolved.
- F4 (#bed-vs-discipline) — task.STYLE-SUPPORT, both branches, deliberately-unresolved status preserved verbatim.
- F5 (adapter launch vs attach) — task.T1 (primary) + cross-ref in task.T3-T4, both branches.

## 3. Dedup correctness — PASS
D1–D6 all flagged as references only ("Raw preserved, not merged" appended to each). No merge/deletion of raw text found in any doc.

## 4. Provenance — PASS (5/5 spot-checks resolved)
- `old-but-good-onion/terminal-onion-study.md` §8 tail — tagline confirmed on disk.
- `old-but-good-onion/interposition-study.md` §8 tail — tagline confirmed on disk.
- `grounded-composites/assymetry-preConsultation.md:369` — "tmux carries the doorbell…" confirmed.
- `grounded-composites/assymetry-preConsultation.md:768` — D2 quote confirmed.
- `grounded-composites/costa.seed.codex-claude-composite.2026-08-07.md:13,27` — D1/D2 quotes confirmed.
- `oraculum-basic-triangulation/vision.oraculum.Y.2026-07-31.md` — exists, F1 branch A source.
- `symetry.../replies.symmetry.vision-not-explored.2026-08-03.md` — HERAKLIT-1/RIVERBED-BEING confirmed at line 147/180.

## 5. Completeness — FAIL
Field's map states "full read of all 32 source files" (map.meshup.field.2026-08-07.md:5). Two of those 32 original source files never receive a single pointer anywhere across the four navigation docs:
- `oraculum-basic-triangulation/02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md` (~620 lines — the Driller/tokenization concept, one of the largest and most technically load-bearing documents in the corpus)
- `oraculum-basic-triangulation/03_COST_COMPLEXITY_AND_STAGED_DECISION.md` (~334 lines — cost/staged-decision model)

Root cause: Field's own map (Part 2, THEME CLUSTERS) never assigned these two files to any T1/T2/T3/T4/STYLE/SUPPORT cluster — they appear only in Part 1 (Inventory) and 04_LABORATORY is the only sibling chapter that gets a pointer (via the D3 double). This gap already existed in the source-of-truth map, but the fold (task.T1/T2/T3-T4/STYLE-SUPPORT) reproduced the omission silently instead of surfacing it as a flagged gap ("Field's map left 02_DRILLER and 03_COST_COMPLEXITY uncategorized — no pointer exists to them in this nav layer"). For a corpus explicitly built as tyler's navigation entry point, two substantial architecture chapters are currently unreachable through any of the four docs. Confirmed via `grep -rn "02_DRILLER\|03_COST" task.*.md` → zero hits in all four docs.

All other clusters, doubles, forks, and gaps (D1–D6, F1–F5, G1–G8, and all remaining 30/32 files) are accounted for and traceable.

## Fix-list
1. Add pointers for `02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md` and `03_COST_COMPLEXITY_AND_STAGED_DECISION.md` to an appropriate doc (most natural home: task.T2.composites.md, alongside 01_ARCHITECTURE and 04_LABORATORY — Driller is part of the room/broker pipeline's output-extraction stage) — or at minimum add an explicit GAPS entry noting these two files are present in Field's inventory but uncategorized/unclustered, so a reader knows they exist and must go to Field's map directly.
2. (Non-blocking, borderline) Consider trimming the "What tyler does with it" scope sentences slightly further toward pure enumeration if the fold discipline is meant to be read strictly — currently compliant but closest to the line.

> **ADDENDUM (2026-08-07) — RESOLVED.** The FAIL above (02_DRILLER / 03_COST orphaned) was closed in `task.T2.composites.md`: both files now carry reachability pointers ("⚠ audit-fix reachability pointer"), inherited into MAJKEE.md SCOPE 2. This verdict is historical; the gap is fixed.
