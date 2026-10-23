witness: R8d re-witness of ARCHITECTURE.draft.r5.md + lock-proposals.r3.md · writer of the text: assay (same witness as R8/R8c, resumed; returned as text) · landed verbatim on disk by oraculum(cSharp) X3 head, 2026-10-22 ~23:5x CEST
NOT an assay-authored file: assay writes no files. This is the head's verbatim record of assay's returned verdict.

---

VERDICT: PASS for ARCHITECTURE.draft.r5.md and lock-proposals.r3.md (checks 1–5). I found no undeclared hunk and no blocking claim-type defect. Two small wording notes are non-blocking.

Task: R8 re-witness, R9-1 revision
Bed: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/

Ran:
- `sha256sum` on r5, proposals r3, log r4, card r2 and the wrapper diff
- `git rev-parse HEAD HEAD:PROJECT-DESIGN.md`
- `git diff --no-index -U0` for r3→r5 and for proposals r2→r3, read in full
- a `python3 -I` substring check of 12 quoted majkee phrases against the two answers files
- grep for `L14 D5`, `L17`, `rename` and `vault` in r5
- `diff` of the KEYS CODE chapter, r3 against r5

1. Hashes and base — PASS
- r5 = 25d1b589…, proposals r3 = a121b66d…, log r4 = 1895a0f5…, card r2 = 2a6baf3f…, wrapper-thinning.diff = ff03ee66…. All match your values.
- HEAD = 78059da137f2b6d17192c251220d80b148aa1ac6 and the blob = 74e94d55…, both unchanged.
- I did not hash r4 and did not read it.

2. Hunk mapping — PASS
- The r3→r5 diff has 36 hunks. The log declares 34 edits. The difference is merge and split, not undeclared change.
- Merged hunks:
  - E2+E3 are one hunk at line 28.
  - E29+E30 are one hunk at lines 439–440.
  - E33+E34 are one hunk at line 475.
- Split edits: E16 (2 hunks), E21 (2), E25 (intro and table), E32 (3), and E5/E6 per line.
- Every hunk maps to an E-number. No undeclared hunk found. Unchanged lines:
  - `## 5. KEYS CODE` and its chapter are identical to r3 apart from the E21 v0 → nablarva.v0 renames in the reading aid.
- The proposals r2→r3 diff has 7 hunks. All map to log §3:
  - doc line and heading
  - the rules-line exception
  - the P5 block plus the leans heading
  - the c1 labels, the nablarva.v0 renames and the O1/O2 additions
  - the ad hoc sentence
  - the two "Not proposed here" lines (N8 and N6)
- P1–P4 are unchanged.

3. Claim types in the changed hunks — PASS
- All 12 phrases I checked are verbatim in the answers files. They cover N1, A, N2, N3, N4, N5, N10 "keep terminology", N9 O1/O2 and C "c1".
- AGENTS.md naming-law quote: the "Naming law" bullet exists at AGENTS.md:66–68. The r5 text uses an ellipsis.
- L14 D5 is limited to "detaching never closes a bed" at r5 lines 64, 88 and 139.
  - "Closing a view ends/doesn't end a session" is `inferred: houston`, with "no lock says it" (E4, E7).
  - L14 D5 at lines 60 and 333 is "sessions live on the workstation", as before.
- L17 is not cited as amended. r5 lines 104 and 240 say "L17 holds unchanged until a GO names P5" and call P5 a proposal.
  - P5 (placeholder L22) says "adopted only if majkee's GO names this proposal; L17 is unchanged until then".
  - Its two quoted L17 clauses match flag L17 verbatim.
  - The P5 sources are quoted `said: majkee`. The head's reading of A as a2 is tagged `inferred: oraculum`.
- No new `locked:` reaches past its text. The nablarva.v0 rename is claim-neutral. Source tags changed from `said: v0` to `said: nablarva.v0` only.

4. No manufactured decision — PASS
- Roles/config: the new row and §4.8 are direction only. Owner is `unknown:`, and "design, role model, schema, home and owner" are open.
- Vault: both options are open, and the entry sits in open items.
- Stridularium: the name is an open item. The text says "L13 is a lock; this document renames nothing".
- Ovitmugen code home: open (N11).
- Packaging, shared layer owner/home/API and docket 2: untouched. P5 lists "which shared layers exist, their owner/home/API, and carrier qualification" as OPEN. Docket 2 is "excluded" in both the draft table and the proposals.
- Working defaults (c1) in §9 and the proposals are labelled "working default (inferred: houston, per R9-1 c1)", "not gavels", "overridable without ceremony", and "every item stays open".
  - The default text matches the r2 leans: docket 5 NDJSON/SQLite, docket 8 comparison first, docket 4 no pick, and "none" for 3, 6 and O3/O4.
  - The O1/O2 cells carry majkee's quotes.
  - c1 authorizes these in the body.
  - The docket 5 default is the nearest thing to a store/history choice, and it is labelled.
- L4: send-keys injection remains a recorded death. "Alternatives welcome" is said: majkee N3 and leaves the mechanism open. No exception is granted.

5. KEYS CODE anchor — PASS
- `## 5. KEYS CODE` is at line 250 of r5. The unchanged wrapper-thinning.diff pointer `#5-keys-code` resolves.

Non-blocking notes:
- r5 line ~31 says "Nabla.Tmux is the name of the chatbot that wrote it (said: majkee R9-1 N7)". N7 says only "Nabla.Tmux is chatbot name - same as her project". "That wrote it" is the author's inference inside a said: tag.
- Lock-proposals rules line still says leans appear "here only and never in the draft body", then adds the c1 exception. The two sentences are consistent only because of the exception.
- Checks 6–9 (diff apply, route evidence, scope, STATUS YAML): no rerun needed. The diff and base are unchanged. I did not verify the new raw files against Houston's transcript writes, so scope for r4/r5/proposals r3/log r4 is unverified, and the transcript was not read.

Reproduce:
- `cd <bed>/raw && sha256sum ARCHITECTURE.draft.r5.md lock-proposals.r3.md revision-log.r4.md`
- `git diff --no-index -U0 ARCHITECTURE.draft.r3.md ARCHITECTURE.draft.r5.md | grep -c '^@@'`
- `git diff --no-index -U0 lock-proposals.r2.md lock-proposals.r3.md`
- `grep -n '^## 5. KEYS CODE' ARCHITECTURE.draft.r5.md`
