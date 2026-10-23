witness: R8e narrow re-witness of ARCHITECTURE.draft.r7.md + lock-proposals.r4.md · writer of the text: assay (same witness, resumed; returned as text) · landed verbatim on disk by oraculum(cSharp) X3 head, 2026-10-22 23:59 CEST (clock read after a first save that wrongly said "2026-10-23 after 00:00" from expectation)
NOT an assay-authored file: assay writes no files. This is the head's verbatim record of assay's returned verdict.

---

VERDICT: PASS (checks 1–5). No failures found. One non-blocking observation under check 4.

Task: narrow R8 re-witness, r7 and lock-proposals.r4
Bed: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/

Ran:
- `sha256sum` on the two candidates
- `git rev-parse HEAD`
- `git diff --no-index -U0` for r5→r7 and for proposals r3→r4
- `diff` of the P1–P4 block and of the "Leans…" to end tail between proposals r3 and r4
- a `python3 -I` check of 11 quotes, with whitespace normalised, against the two answers files and flag.md
- reads of the P5 section of lock-proposals.r4.md and of _bus/03.cartan.return.md §4 and _bus/03.oraculum.verdict.md

1. Hashes and diff scope — PASS
- r7 = 3330b99ad986…, proposals r4 = 12ed06692262…. Both match your values.
- HEAD is still 78059da137f2b6d17192c251220d80b148aa1ac6.
- The r5→r7 diff has 3 hunks: line 3 (r5 → r7), line 33 and lines 103–104. Nothing else changed.
- The proposals r3→r4 diff touches:
  - line 2 (the doc line)
  - line 5 (the rules line, which is outside the P5 section)
  - line 8 (the heading)
  - the P5 section (r3 lines 77–109)
- From the "## Leans…" heading to the end, r3 and r4 are identical. The P1–P4 block (from `## P1` up to the `## P5` heading) is byte-identical to r3.

2. P5-a and P5-b answer Cartan's findings — PASS
- Finding 1 (substantive, one exact operative meaning): P5 is now two alternatives.
  - The text says "A GO adopts P5 only if it names P5-a or P5-b. A GO that names 'P5' alone has no single meaning, so it adopts neither."
  - P5-a keeps L17's text unchanged and adds a reading of the "no common framework" clause.
  - P5-b supersedes exactly two named L17 phrases with stated replacement wording. The original L17 text stays in place, with the superseded phrases listed in the Archived index under L15.
- Finding 2 (blanket preservation): both operative blocks end "All other L17 provisions remain in force… this line releases no implementation, delivery, activation or transport."
- Design permission versus release:
  - P5-a says "Designing shared layers is architectural work and is permitted. Implementing, activating, delivering through or adopting a transport for any of them needs its own separate release."
  - P5-b(2) says the same in its replacement wording.

3. Quotes — PASS
- All 6 `said: majkee` quotes (N1 ×4, A, and the N7 line) are verbatim in the answers files. The N7 line is "Nabla.Tmux is chatbot name - same as her project".
- The L17 quotes in the "L17 text concerned" paragraph and in the operative blocks are verbatim in flag.md. The wrapped "Concrete shared-layer ownership/home/API… Phase 0 build." quote matches after whitespace normalisation.
- The partial quotes "floating yes, chaotic not", "coherent 'framework'" and "can share process|api|cli|subscription layers and call generic methods" are all found in the answers.

4. Tension and no manufactured owner/home/API — PASS
- The tension is shown and not resolved. A section titled "Tension in the sources, shown and not resolved" names the conflict between "No common framework" and "coherent 'framework'". It says the alternatives "differ exactly on this point".
- Choosing between P5-a and P5-b, or neither, is left to majkee.
- Both notes state that "Concrete shared-layer ownership/home/API and carrier qualification remain open" under both alternatives. No owner, home, API, process model or transport is named in either block.
- Observation, non-blocking: P5-a's operative text carries its own reading, "does not forbid architecting nabLarva as one body". It also keeps the narrow-integration-boundary sentence in force. The note says openly that this leaves tension with N1, so it is visible, not silent.

5. r7 lines 33 and 103–104 — PASS
- Line 33 quotes N7 verbatim, in quotation marks and tagged `said: majkee R9-1 N7`. The "that wrote it" inference is gone.
- Lines 103–104 say "P5 in the lock proposals offers a reading (P5-a) or an amendment (P5-b). L17 holds unchanged until a GO names one of them." L17 is not cited as amended.

Limits:
- I did not re-check the unchanged parts of r7 beyond the 3-hunk diff.
- Checks 6–9 from the first pass are not rerun. The diff, base and KEYS CODE chapter are unaffected.
- Scope for the new raw files (r4–r7, proposals r4, logs r5/r6) against Houston's transcript was not verified, and no jsonl was read.
- r6 was withdrawn and not read. I read revision-log.r5/r6 only to the extent of not needing them.

Reproduce:
- `cd <bed>/raw && sha256sum ARCHITECTURE.draft.r7.md lock-proposals.r4.md`
- `git diff --no-index -U0 ARCHITECTURE.draft.r5.md ARCHITECTURE.draft.r7.md`
- `git diff --no-index -U0 lock-proposals.r3.md lock-proposals.r4.md | grep '^@@'`
- `diff <(sed -n '/^## P1/,/^## P5/p' lock-proposals.r3.md | sed '$d') <(sed -n '/^## P1/,/^## P5/p' lock-proposals.r4.md | sed '$d')`
