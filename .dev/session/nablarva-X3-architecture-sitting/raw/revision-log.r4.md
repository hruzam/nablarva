---
doc: revision log r4 — R9-1 placements (N1–N11, A/B/C) and the b-fix
seat: houston · card: sitting · 2026-10-22
inputs: raw/answers.majkee.r9-1-notes.2026-10-22.md · raw/answers.majkee.r9-1-abc.2026-10-22.md · the head's placement table (relayed)
base unchanged: HEAD 78059da · PROPOSED wrapper diff unchanged, because `## 5. KEYS CODE` is kept
---

# Revision log r4

## 0. File status — read this first

- **raw/ARCHITECTURE.draft.r4.md is WITHDRAWN. Do not witness it.** I wrote it, then compared it
  line by line with r3. Besides the intended placements, it contains about thirty undeclared
  wording and reflow changes, for example "PTY as the impulse layer (that part is plan, not lock)"
  → "PTY as impulse layer (plan, not lock)", "but producing evidence" → "and producing evidence",
  merged bullets in §4.2, §4.5 and §4.7, and a reworded stage 2/3 in §6. The pen forbids editing
  r4, so I replaced it.
- **raw/ARCHITECTURE.draft.r5.md is the candidate.** It is r3 copied verbatim, with only the edits
  E1–E34 below. A substitution such as v0 → nablarva.v0 lengthens a line, but no line was rewrapped.
- **Disclosure about r3.** r3 also reflowed parts of r2 without declaring it: list formatting in the
  reading guide, §0, §4 notes and §7, and the §9 docket list turned into a table. Its log
  (revision-log.r3.md) does not list those changes. They are wording-neutral, but they were
  undeclared, which is what cost the full re-witness.
- **Suggested mechanical check for the head:** `diff /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/ARCHITECTURE.draft.r3.md /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/ARCHITECTURE.draft.r5.md`. Every hunk should map to one entry in E1–E34.

## 1. Edits in ARCHITECTURE.draft.r5.md (line numbers are r3's)

| E | r3 line | change | cause |
|---|---|---|---|
| E1 | 3 | `DRAFT r3` → `DRAFT r5` | revision |
| E2 | 28 | after "…means Message B." one sentence appended on the same paragraph, citing the R9-1 notes and A/B/C files; the paragraph continues for two more lines | R9-1 citation |
| E3 | after 28 | new paragraph: **nablarva.v0** names the file `Nabla-Tmux-Architecture-Draft-v0.md`; the file keeps its name; Nabla.Tmux is the chatbot's name | N7 |
| E4 | 59 | view row, forbidden cell: "ending a session's life by detaching or closing a view" → "closing a bed by detaching a view (locked); ending a session by closing a view (`inferred: houston`)". Grounds cell: L14 D5 now quoted "detaching never closes a bed"; closing retagged as consistent with L17 and §3.2.x, "no lock says it" | b-fix |
| E5 | 63–64 | "Nabla-Tmux v0" → "nablarva.v0"; "said: v0" → "said: nablarva.v0" | N7 |
| E6 | 74–75 | "v0's rule" → "nablarva.v0's rule"; "said: v0" → "said: nablarva.v0" | N7 |
| E7 | 83–85 | item 4 replaced. Heading "Closing or detaching a view never ends a session." → "**Detaching never closes a bed** (locked: L14 D5)". L17 lifetime sentence kept. The closing claim is now `inferred: houston`, resting on L17 and the §3.2.x candidate, "No lock says it" | b-fix |
| E8 | after 89 | item 5: r3 lines 86–89 unchanged. Appended: majkee's N1 words (four quotes), answer A's words, and the named tension with L17's narrow integration boundary, with a pointer to P5. "L17 holds unchanged until a GO names P5" | N1 · A (a2) |
| E9 | 93 | "said: v0 rules" → "said: nablarva.v0 rules" | N7 |
| E10 | 98 | "From Nabla-Tmux v0 (said: v0," → "From nablarva.v0 (said: nablarva.v0," | N7 |
| E11 | 105 | "v0's own event log" → "nablarva.v0's own event log" | N7 |
| E12 | 123 | deliver row, open cell: "doorbell mechanism" → "doorbell mechanism, alternatives welcome (said: majkee R9-1 N3)" | N3 |
| E13 | 127 | cross-host row, open cell: appended "; current practice tailnet + SSH, alternatives open — said: majkee R9-1 N9" | N9 |
| E14 | after 129 | new seam row **configuration · roles**: owner `unknown:`; planned = majkee's N2 direction (registry/config/settings layer; admin/user/super-admin + agentive layer); open = design, role model, schema, home and owner | N2 |
| E15 | 145–146 | "v0's "living tissue"" / "said: v0" → nablarva.v0 | N7 |
| E16 | 180–182 | three "v0" → "nablarva.v0", and a new bullet after 182 quoting N3: "Alternatives are welcome, and the mechanism stays open." The L4 bullet is unchanged | N7 · N3 |
| E17 | 191 | "said: v0 `pane-spawn`" → "said: nablarva.v0 `pane-spawn`" | N7 |
| E18 | 199 | "Nabla-Tmux v0's record" → "the nablarva.v0 record" (VIST "v0" and EVENTS "v0.3" unchanged) | N7 |
| E19 | after 220 | new §4.7 bullet: a pointer to §2 item 5 for majkee's one-body direction and P5 | N1 |
| E20 | after 221 | new **§4.8 Configuration · roles**: N2 quoted verbatim; recorded as direction only; no role model, schema, home or owner chosen | N2 |
| E21 | 290–291, 294–295 | four "v0" → "nablarva.v0" in the reading aid | N7 |
| E22 | after 324 | new §7 paragraph: N5 quoted; it matches the AGENTS.md naming law (quoted, said: AGENTS.md, Standing rules) | N5 |
| E23 | 329 | ovitmugen home cell: inserted "; whether `zsh/session/` stays its code home is open (said: majkee R9-1 N11)" | N11 |
| E24 | 341 | "**Nabla-Tmux v0**" → "**nablarva.v0**" | N7 |
| E25 | 374–387 | docket intro rewritten to explain the working defaults (c1: Houston's leans, not gavels, overridable without ceremony, docket 2 excluded; O1/O2 carry majkee's N9 words). The table gains a third column "working default". The first two columns are unchanged | C (c1) · N9 |
| E26 | 393–394 | "Collisions between Nabla-Tmux v0" → "between nablarva.v0"; "said: v0" → "said: nablarva.v0" | N7 |
| E27 | 397 | table header "v0" → "nablarva.v0" | N7 |
| E28 | 399 | X1: appended "; alternatives welcome" | N3 |
| E29 | 403 | X5: appended "· majkee R9-1 N1 direction and proposal P5 (§2 item 5)" | N1 |
| E30 | 404 | X6: appended "· said: majkee R9-1 N10 "we should keep terminology"" | N10 |
| E31 | 409 | X11: appended N10's lean (`~/.nablarva` OR `<project>/.nablarva`; both open) | N10 |
| E32 | 419–423 | other open items: 419 gains "and code home (said: majkee R9-1 N11)". New items: majkee's one-body direction against L17 (N1/P5), the configuration · roles design (N2), the per-project process vault home (N10, both options open), and stridularium's name (N4 quoted; "L13 is a lock; this document renames nothing") | N1 · N2 · N4 · N10 · N11 |
| E33 | after 434 | new pins-owed bullet: the two R9-1 answer files | R9-1 citation |
| E34 | 435 | "Nabla-Tmux-Architecture-Draft-v0:" → "nablarva.v0 (file Nabla-Tmux-Architecture-Draft-v0):" | N7 |

No other byte of r3 changed. `## 5. KEYS CODE` and its whole chapter are unchanged, so
`wrapper-thinning.diff` (`#5-keys-code`) stays valid.

## 2. N1–N11, b-fix and A/B/C → where

| item | placement | where |
|---|---|---|
| b-fix (R9-1 option b) | L14 D5 now locks only "detaching never closes a bed". "Closing" is retagged `inferred: houston` in both places | r5 E4 (§1 view row), E7 (§2 item 4) |
| N1 + A | direction recorded as said: majkee, with the tension against L17 named and P5 proposed; L17 is unchanged | r5 E8, E19, E29, E32 · lock-proposals.r3 P5 |
| N2 | new seam row and §4.8; design left open | r5 E14, E20, E32 |
| N3 | "alternatives welcome"; the mechanism stays open; L4's death is unchanged | r5 E12, E16, E28 · lock-proposals.r3 ad hoc (last sentence) |
| N4 | open naming item; nothing is renamed (L13 holds) | r5 E32 |
| N5 | naming paragraph citing the AGENTS.md naming law | r5 E22 |
| N6 | **out of the doc, parked** (session naming / sub-organ numbering) | lock-proposals.r3 "Not proposed here" (one line, pointer only) |
| N7 | nablarva.v0 throughout the doc; the file name is kept | r5 E3, E5, E6, E9–E11, E15–E18, E21, E24, E26, E27, E34 · lock-proposals.r3 rows 5 and 8 |
| N8 + B (b1) | **out of the doc, parked** as its own governance question | lock-proposals.r3 "Not proposed here" (one line, pointer only) |
| N9 | O1/O2 carry majkee's words; both items stay open | r5 E13, E25 · lock-proposals.r3 rows O1, O2 |
| C (c1) | leans for 3/4/5/6/8 and O3/O4 become labelled working defaults in §9; docket 2 excluded | r5 E25 · lock-proposals.r3 frontmatter, leans heading and rows |
| N10 | the vault lean is recorded with both options open; terminology kept | r5 E30, E31, E32 |
| N11 | ovitmugen's code home is an open item | r5 E23, E32 |

## 3. Edits in lock-proposals.r3.md (line numbers are r2's)

| r2 line | change | cause |
|---|---|---|
| 2 | doc line: r2 → r3, "supersedes raw/lock-proposals.r2.md after R9-1" | revision |
| 5 | rules line: appended "Exception (said: majkee R9-1 C "c1"): …" for working defaults; docket 2 excluded | C (c1) |
| 8 | heading "(r2)" → "(r3)" | revision |
| after 75 | new **P5**: L17 amendment proposal text plus a source and open-points note. It uses majkee's words "No common framework" and "floating yes, chaotic not". Adopted only if majkee's GO names it | N1 · A (a2) |
| 77 | leans heading: "never in the draft body" → items marked working default (c1) also appear in draft §9 | C (c1) |
| 83, 84, 85, 86, 87, 90, 91 | prefixed "**working default (c1):**" (rows 3, 4, 5, 6, 8, O3, O4) | C (c1) |
| 85, 87 | "v0" → "nablarva.v0" | N7 |
| 88, 89 | O1 and O2 rows: appended majkee's N9 words | N9 |
| 99 | ad hoc paragraph: appended "Majkee welcomes alternatives to `tmux send-keys -l` (said: majkee R9-1 N3)." | N3 |
| after 105 | two "Not proposed here" lines: N8 (parked per b1) and N6 (parked by the head) | N8 · N6 |

Everything else in lock-proposals.r3 is r2 verbatim (P1–P4 unchanged).

## 4. Not changed

`card.sitting.draft.r2.md` and `wrapper-thinning.diff` are unchanged. The §8 defaults table is
unchanged.
