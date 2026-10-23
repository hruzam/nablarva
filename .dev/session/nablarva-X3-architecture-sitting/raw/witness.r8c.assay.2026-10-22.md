witness: R8c re-witness of ARCHITECTURE.draft.r3.md · writer of the text: assay (same witness as R8, resumed; returned as text) · landed verbatim on disk by oraculum(cSharp) X3 head, 2026-10-22 ~11:45 CEST
NOT an assay-authored file: assay writes no files. This is the head's verbatim record of assay's returned verdict.
first pass: raw/witness.r8.assay.2026-10-22.md (FAIL on check 2, r2:139). This pass covers r3 sha256 88fe67e4a0657b8efd20e0623dd95038514469dbedfa0c08feb84037aa21eff0.

---

VERDICT: PASS for ARCHITECTURE.draft.r3.md (checks 1–5). Checks 6–9 need no rerun. One residual non-blocking stretch is noted under check 2.
Task: R8 re-witness, nablarva-X3-architecture-sitting, r3 correction
Bed: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/

Ran:
- `sha256sum` on r3, revision-log.r3, lock-proposals.r2, card r2, wrapper-thinning.diff and r2
- `git rev-parse HEAD HEAD:PROJECT-DESIGN.md`
- `git diff --no-index -U0 ARCHITECTURE.draft.r2.md ARCHITECTURE.draft.r3.md`, read in full
- `diff` of the KEYS CODE and Reading-aid sections and of the seam-row block
- grep of the flag.md, handoff, termbrana README, keys brief and PROJECT-DESIGN quotes that r3 cites

1. Hashes — PASS
- r3 = 88fe67e4a065…, revision-log.r3 = e859b2220393…, lock-proposals.r2 = a4ccf464…, card r2 = 2a6baf3f…, wrapper-thinning.diff = ff03ee66…. All match the values you gave.
- HEAD = 78059da137f2b6d17192c251220d80b148aa1ac6. The blob is 74e94d55…. Both unchanged.

2. Claim types across all of r3 — PASS, one residual stretch
- A1 confirmed, at §4.2 line 150. L17 is cited only for "independently useful clients". The "does not require a session bed, editor, tmux or ovitmugen" wording is now quoted `said: composer handoff`. That quote matches handoff:22 verbatim. The README §Layering B (README:165) backs it up.
- A2 confirmed. The §3 middle column is now "consistent with (inferred: houston)", with a note, and quotes L17 and the README. The README quote "standalone operation with nabLarva completely absent" exists at README:106.
- A3 confirmed. L8 (clipper/processor/composer placement) and L8′ ("for this work") are cited separately. The conclusion that clipper and processor keep L8's placement is tagged `inferred: houston`.
- S1–S8 confirmed in the text.
  - S1: the composition row's forbidden effect is now "transmission without checked target binding… autonomous sending from assistant drafts".
  - S2: dependency item 4 and the view row are restated, with L14 D5 for detaching and L17 for ovitmugen's lifetime.
  - S3: "by the Phase 0 build" is restored.
  - S4: the room-truth row now carries a quote that exists at PROJECT-DESIGN.md:262 (§3.7), tagged `said`.
  - S5: "Private is an in-ledger visibility boundary" has dropped "not a separate store".
  - S6: the palette sentence is a `said: keys brief` quote ("is not a new sending authority", keys brief:190), with a "consistent with L17" reading.
  - S7: the descriptions are split to `said: PROJECT-DESIGN §3.2/§3.6`.
  - S8: the X1 row reads "L4 (recorded death) · L3 S5 · L17 — any exception returns to Majkee (§4.3)".
- No locked/said/inferred/unknown merging was found in the other hunks. The count of `unknown:` tags is 18 in both r2 and r3. G4 and G5 are still `said: majkee`. L13 is still name-only.
- Residual stretch, non-blocking: §2 item 4 and the view row say "closing or detaching a view never ends a session". L14 D5 locks only "detaching never closes a bed". The word "closing" is not in the lock text. It was already in r2, and r3's sweep did not narrow it. Retag or trim if the author wants zero stretch.

3. Undeclared r2→r3 edits — none that change meaning, claim type, open/closed status or attribution
- There are 50 hunks. All are declared (A1–A3, S1–S8) or pure formatting or rewording:
  - prose to bullets (how-to-read, §0, §4.1, §4.2, §4.3, §4.5, §4.7)
  - the docket list to a table (the same ten items; the dependency notes are identical: docket 2, 4, 5, 6 and 8 keep theirs, and the rest show "—", as in r2)
  - small wording changes ("grounds that direction; it does not restart", "Framing locked", "neither extended to nor transferred", "A pin proves read bytes, not continued applicability", "survival as a controller/function")
  - dropped bold on the Sources labels
  - "This file is absent" to "It is absent"
  - the Defaults label reworded
- Undeclared but meaning-preserving or tightening:
  - §4.2: "owned by that note" became "owned by one boundary note", which is closer to L8.
  - §2 item 5: "shared layer's owner/home/API is open" became L17's own "Concrete… remains open… by the Phase 0 build".
  - §3: added a note that the middle column is a consistency reading.
  - The §4.1 sentence "Majkee holds canon (locked: L16.1)…" became its own bullet. The content is the same.
- Unchanged: the KEYS CODE section body, the Shared/Reserved/Conformity tables, the seam rows other than room truth, the Defaults table rows, and the open items. `## 5. KEYS CODE` now sits at line 223.

4. Manufactured decisions, L17 and L4 — PASS
- The same sweep as before found no lean words (the only hits are "lean: pane", a quote of flag docket 4, and "lean recorded in flag").
- The docket and O-item mentions match r2 exactly (identical counts).
- L17 holds in §2.5, §4.7 and row X5. L4 holds in §4.3: send-keys is a recorded death, and an exception returns to Majkee.
- The §8 Defaults table is unchanged. The caution from my first report still stands for Majkee.

5. KEYS CODE anchor — PASS
- `## 5. KEYS CODE` exists at line 223 of r3. The unchanged diff's `docs/ARCHITECTURE.md#5-keys-code` still resolves.
- The diff is the same bytes, so the earlier `git apply --check` (exit 0, shared tree and scratch) stands.

Checks 6–9: no rerun. The diff, base, STATUS YAML, route evidence and scope are unaffected by an r3 swap. The r3 file and revision-log.r3 are new Houston raw files. I did not re-verify that their writes were in the child's transcript, which has grown since my first pass.

Limits:
- I did not check that r3 and revision-log.r3 appear as Write events in the Houston transcript.
- Only quotes I could grep were verified.
- No jsonl was read this pass.

Reproduce: `cd <bed>/raw && sha256sum ARCHITECTURE.draft.r3.md; git diff --no-index -U0 ARCHITECTURE.draft.r2.md ARCHITECTURE.draft.r3.md; grep -n '^## 5. KEYS CODE' ARCHITECTURE.draft.r3.md`
