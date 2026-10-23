# nablarva-X3-architecture-sitting · oraculum(cSharp) · session-process observations

`origin: written by the X3 MAIN head during the session (2026-10-22 06:4x → 2026-10-23 22:06 CEST, office) · sources: .dev/session/nablarva-X3-architecture-sitting/{STATUS.md,_bus/,raw/} — preservation commit nablarva@519a211 (bed record) plus later bed commits · promoter: oraculum(cSharp) · append-only`
`what: how this sitting RAN, not what it decided (decisions: docs/ARCHITECTURE.md @f20dda5, flag L18–L21 @5e93688). Majkee asked for this explicitly: "your experiences please do not forget, wery important for later drafts handoff phase" (2026-10-23).`

## 1. Carriage facts

- Mode B, one Claude MAIN head plus ONE Houston child on `card: sitting` (first real child-sitting route), seven handbacks, 0 spawns, 22 writes, all new files in the bed's raw/ (raw/evidence.houston-route.final.eagle.2026-10-23.md). Child spend ≈539k subagent tokens.
- Revisions: arc → arc.r2 (after Majkee's late source) → drafts r1 → r2 (Cartan REVISE) → r3 (assay FAIL) → r4 WITHDRAWN → r5 (Majkee's R9-1 notes) → r6 WITHDRAWN → r7 (Cartan REVISE on P5). Final: r7 promoted byte-identical.
- External review: Cartan (Codex, X1 tunnel vault, thread 01a14731), 3 cycles: 01 REVISE (5 substantive + 4 wording), 02 PROCEED, 03 REVISE (P5 only). Context 35.7 % after cycle 01; **no usage line printed on cycles 02–03** (context unmeasured).
- Witness: assay, five passes (R8 FAIL → R8c → R8d → R8e PASS, + the flag-append witness), resumed as the same witness; it never loaded a transcript (route evidence by mechanical extraction with a fixed-prefix hash).
- Readers: eagle ×6 (mechanical crawls, zip isolation, route evidence ×4). delta ×2 (promotion copy + patch; flag append).
- Majkee decision traffic: G1–G9 pre-answered; arc pick; Q1–Q8; R9 deck of 7 items (R9-1…R9-5 + GO), each landed verbatim in raw/answers.majkee.* before any action.

## 2. Faults — mine first

| # | fault | caught by | cure that worked |
|---|---|---|---|
| H1 | STATUS said arc "relayed to Majkee 06:56" before the relay happened | myself, when Majkee's message arrived first | CORRECTION line; never write a state ahead of the act |
| H2 | three timestamps written from expectation, not the clock (VERDICT 03 "10-23 ~00:0x"; witness r8e "after 00:00"; earlier "07:2x" style) | myself, against `date` | every recorded time comes from `date` in the same turn |
| H3 | route-evidence spec defined "first answer" as first assistant text; on a Claude child the answer is a SubagentHandback tool call | the first eagle output (record 15 = narration, no Route line) | re-cut at first SubagentHandback; keep the wrong first cut as evidence |
| H4 | flag commit message pinned its source file "@519a211", where the file did not exist | myself, re-reading the message | amend (unpushed) to include the file in the same commit |
| H5 | vector to X2 copied Houston's over-wide "observe owner = termpanum (locked: L13)" | myShell's relay | correction file landed verbatim; L13 = name only |
| H6 | I proposed "tiny r4" (b) for R9-1 before Majkee's notes revealed new direction — the "tiny" frame was wrong | Majkee's own notes | buffer + placement table + explicit A/B/C before relaying |

Others' faults, each self-caught or caught by the next seat:
- Houston: lock tags cited wider than their text — **eleven** instances (Cartan cycle 01 ×5, assay R8 ×1, Houston's own sweep ×8 in r3, plus one residual stretch). The dominant defect class of the sitting.
- Houston: undeclared reflow in "narrow" revisions (r3 undeclared; r4 withdrawn by itself); a revision written **from memory** instead of from disk (r6 withdrawn by itself). Both late in its context budget.
- Houston: read order card-before-addendum against the loader's "in this order"; stamp lines printed in canonical order (assay: "minor procedural deviation … not a pass on order").
- eagle: reported 18 writes while its file listed 17 (the file is the record).
- Cartan: cycle-01 RETURN used non-guide headings (content present).

## 3. What worked — keep these

- **Land the operator's words verbatim in a file before acting** (raw/answers.majkee.*). Every relay then points at bytes; no paraphrase can drift. Non-objection is recorded as non-objection, never as his words.
- **The gavel deck with buys / costs / can-be-lost per option** (raw/gavels.R9.oraculum.2026-10-22.md). Majkee asked for it ("help me to see bigger context|costs| what selection buys me| what can be lost") and decided seven items in about an hour, one at a time, with no re-litigation.
- **A held-back collision list** (K1–K7) while the drafter worked, compared after: 7/7 covered, and the drafter found 6 more. This is an independence check that costs nothing.
- **A revision's change log is a claim; diff the bytes.** It caught 30 undeclared hunks (r2→r3) and confirmed clean ones (r5→r7: 3 hunks).
- **New-files-only pen + explicit publication release.** History is complete (two withdrawn drafts kept), and the head copies byte-identical (sha256 equal on both sides).
- **Mechanical route evidence:** fixed-prefix hash at the first handback, tool timeline restricted to name + path. Assay reproduced it without loading the transcript.
- **Split decisions into document GO vs lock adoption** (each lock named separately; an ambiguous proposal returned as explicit alternatives P5-a/P5-b).

## 4. For the later drafts-handoff phase (Majkee's emphasis)

1. A drafting child degrades late. Plan a **fresh child** after about 4–5 revision turns or ~400k tokens, by the operator's order, and give it the arc, the answers files and the last released revision. Do not stretch one child to exhaustion; the slips (reflow, from-memory writes) cluster at the end.
2. Every revision request says: **"revise from the bytes on disk; declare every changed line, formatting included."** Without that sentence, reflow drift appears.
3. Put the **lock-citation rule** at the top of every drafting brief: a `locked: L<n>` tag never reaches past the lock's text; name-locks are not ownership; deaths are not reopened by qualification.
4. **A source that arrives late is not a failure; a pin written ahead of it is.** When new material lands mid-sitting, stop, place it with the operator (placement table), then relay.
5. **Count before you relay.** Any reported number (writes, hunks, findings) is re-derived from the file before it enters STATUS.
6. **The reviewer's context goes dark silently.** If the tunnel stops printing usage, say so to the operator before the next large ask.
7. Keep one file per operator message (append-only), with the head's reading below it, tagged `inferred: oraculum`.

## 5. Open at the time of writing

- X1 (`nablarva-X1-architecture`) closure: check 5 (Houston audit, card: audit, a main session Majkee starts; input incl. 05 Q1 conventional names per seam), check 6 (L12 seal + qualifier lines, Majkee's), the closure inventory (assay, running), observations promotion, pulse rows for X1 and X3.
- Card draft r2 handed to germline-03 (ia-sync `.dev/session/germline-03-foundation-audit/raw/HANDOFF.oraculum.x3-sitting-card.2026-10-23.md`), not yet accepted.
- N6 / N8 parked in dock.md.
