---
doc: revision log r5 — review cycle 03 (P5) and assay R8d notes
seat: houston · card: sitting · 2026-10-22
inputs: _bus/03.cartan.return.md · _bus/03.oraculum.verdict.md · raw/witness.r8d.assay.2026-10-22.md (non-blocking notes)
---

# Revision log r5

## ARCHITECTURE.draft.r6.md — a byte copy of r5, changed on exactly these lines

| r5 line | old | new | cause |
|---|---|---|---|
| 3 | `state: DRAFT r5 for majkee GO …` | `state: DRAFT r6 for majkee GO …` | revision |
| 33 | `file keeps its name. Nabla.Tmux is the name of the chatbot that wrote it (said: majkee R9-1 N7).` | `file keeps its name. "Nabla.Tmux is chatbot name - same as her project" (said: majkee R9-1 N7).` | assay R8d note: "that wrote it" went past N7, so N7 is now quoted verbatim |
| §2 item 5, last two lines (~103–104) | `framework. L17 places shared mechanisms at a narrow integration boundary. A proposed L17` / `amendment is P5 in the lock proposals. L17 holds unchanged until a GO names P5.` | `framework. L17 places shared mechanisms at a narrow integration boundary. P5 in the lock` / `proposals offers a reading (P5-a) or an amendment (P5-b). L17 holds unchanged until a GO names one of them.` | P5 is now two alternatives, and P5-a is not an amendment |

No other byte changed. The remaining "proposal P5" references (§4.7, X5, other open items) name the
P5 group and stay correct as written. `## 5. KEYS CODE` is unchanged.

Head check: `diff raw/ARCHITECTURE.draft.r5.md raw/ARCHITECTURE.draft.r6.md` should show exactly
these three hunks. Any other hunk is a defect of mine.

## lock-proposals.r4.md — a copy of r3, changed only here

| r3 location | old | new | cause |
|---|---|---|---|
| line 2 (doc) | `lock proposals r3 — … (supersedes raw/lock-proposals.r2.md after R9-1)` | `lock proposals r4 — … (supersedes raw/lock-proposals.r3.md after review cycle 03)` | revision |
| line 5 (rules) | `Leans per G7 b are inferred: houston, appear here only and never in the draft body, and exclude docket 2.` … `Exception (said: majkee R9-1 C "c1"): the leans … now also appear in the draft §9 …; docket 2 stays excluded.` | `Leans per G7 b are inferred: houston and exclude docket 2. They appear here, and in the draft body only as the labelled working defaults that majkee's R9-1 C "c1" allows: dockets 3/4/5/6/8 and O3/O4, which are not gavels and can be overridden without ceremony.` The separate "Exception …" sentence is removed, and the G7 option-b quote is kept | assay R8d note on the rules line |
| line 8 (heading) | `# Lock proposals (r3)` | `# Lock proposals (r4)` | revision |
| P5 section (r3 lines 77–108) | one P5 block that "amends" both L17 clauses and also applies the reading, with a note leaving reading versus replacement open | P5 with **two exact alternatives**. **P5-a (reading):** L17 text unchanged, plus a clarifying clause. **P5-b (replacement):** the two exact L17 phrases are named and superseded by exact new wording. Both alternatives: are sourced only in N1 and A, quoted verbatim; show the "No common framework" vs "coherent 'framework'" tension without resolving it; keep permission to design shared layers separate from any implementation, activation, delivery or transport release; and state "All other L17 provisions remain in force". A GO naming "P5" alone adopts neither | cycle-03 substantive and wording findings |

P1–P4, the leans table, the ad hoc paragraph and "Not proposed here" are r3 verbatim.

## Not changed

card.sitting.draft.r2.md and wrapper-thinning.diff are unchanged.
