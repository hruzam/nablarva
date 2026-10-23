witness: R8 · writer of the text: assay (fresh Claude witness, returned as text) · landed verbatim on disk by oraculum(cSharp) X3 head, 2026-10-22 ~11:45 CEST
NOT an assay-authored file: assay writes no files. This is the head's verbatim record of assay's returned verdict.
candidates witnessed: raw/ARCHITECTURE.draft.r2.md 1b2468bc… · raw/lock-proposals.r2.md a4ccf464… · raw/card.sitting.draft.r2.md 2a6baf3f… · raw/wrapper-thinning.diff ff03ee66… · base HEAD 78059da + blob 74e94d55…
head check of the FAIL (11:45): ARCHITECTURE.draft.r2.md:139 reads "- Composition does not require a session bed, editor, tmux or ovitmugen (locked: L17)."; handoff.composer-boundaries.cartan.2026-10-22.md:22 carries that wording; flag.md:204 (L17) reads "Termbrana composition and ovitmugen are independently useful clients". CONFIRMED.

---

VERDICT: FAIL (one narrow defect in check 2; checks 1, 3–9 PASS)
Task: R8 witness, nablarva-X3-architecture-sitting, selected r2 candidates
Bed: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/

Ran (all read-only except the scratch dir):
- sha256sum on the four candidates and revision-log.r2.md
- git rev-parse HEAD
- git rev-parse HEAD:PROJECT-DESIGN.md
- sha256sum PROJECT-DESIGN.md
- git apply --check against the shared tree
- scratch apply and verify under /tmp/claude-1000/-home-hruzam-unikuklatrix-nablarva/46c2dcf6-0264-4d06-8316-77fe12e0fa0f/scratchpad/assay-r8/
- grep and git cat-file for pins, citations and claim types
- the evidence-file jq/awk/sha256 commands against the child JSONL (filtered to metadata only; the transcript was never Read)
- python3 -I with yaml.safe_load on STATUS.md

Evidence by check

1. Hashes — PASS
- ARCHITECTURE.draft.r2.md is 1b2468bc…bbc… as given (full value matches 1b2468bc8dff15d8d3bab5b34655f84942dc77f702cedb400ad6ac46aeeb267e).
- lock-proposals.r2.md is a4ccf464…, card.sitting.draft.r2.md is 2a6baf3f…, wrapper-thinning.diff is ff03ee66…, revision-log.r2.md is f7d1e374…. All full values match your list.
- Base holds: HEAD = 78059da137f2b6d17192c251220d80b148aa1ac6. The PROJECT-DESIGN.md blob is 74e94d55…, and its sha256 is 6ee10aa1…2c78f. The working file is unmodified (git diff against HEAD is empty for it).

2. Claim types — FAIL (narrow)
- Passes:
  - G4/G5 are cited as `said: majkee`. No `locked: G…` exists in the draft or the lock proposals.
  - L13 is cited for names only. The observe row says "locked: L13, name only" and the owner cell is `unknown:`.
  - Every `locked: L<n>` cited exists in flag.md. These are L2, L3, L4, L6, L8, L8′, L9/L9′, L11, L12, L13, L14, L15, L16.1/.2/.7/.12 and L17.
  - Spot-checks of L3 (S1–S8 split from Z's organs), L11 ("flag line or session brief" restored), L14 (D1/D2/D4/D5/D6/D7 carried with the research and triangulation prerequisites) and L8/L8′ (retained OUTPUT(A) boundary) stay inside their text.
  - Pins resolve. Commit c630f0e8 exists and line 120 is the D3 keys entry. Seven raw files exist at 78059da. The VIST brief exists at 78059da. The shelf-law pin 2ae8636 exists. The answers file is correctly flagged absent from 78059da.
  - The G1 quote matches gavels.X4 line 133.
- Defect:
  - raw/ARCHITECTURE.draft.r2.md:139, "Composition does not require a session bed, editor, tmux or ovitmugen (locked: L17)". L17 only says composition and ovitmugen are "independently useful clients". The "session bed, editor, tmux" wording comes from the composer handoff (handoff.composer-boundaries.cartan.2026-10-22.md:22), so the tag should be `said:`. This is the same class of defect as cycle 01's S1, a lock cited wider than its text.
  - This breaks criterion 2 ("claim stays inside that lock's text").
- Lesser items, non-blocking:
  - Line 99, "Optional parts fail soft | locked: L17". L17 does not enumerate it, but the cell sits in a "consistent with" column.
  - Line 153, "clipper and processor not moved by L8′", is an inference tagged `locked`. L8′ says "for this work".

3. No manufactured decisions — PASS, with one caution
- grep of the draft body for lean/ndjson/jsonl/sqlite/recommend finds only quotes of existing flag text: "lean recorded in flag" and "docket 4 (lean: pane)".
- Leans appear only in lock-proposals.r2. They are tagged `inferred: houston`, docket 2 is explicitly excluded, and O4 gets "No lean".
- The draft leaves each of these `unknown:` or open: event envelope (four candidates, docket 8), program home/API, root stub correction versus retirement, editor, JSONL home, parent directory for new folders, packaging shape, shared runtime, VIST ownership, producer and collector-lifetime owners.
- Caution for the head and Majkee: §8 "Defaults and their revisit signals" is Houston's own table, labelled `inferred: houston`, and Majkee has not ruled on it. Rows such as "organ-local event records, no shared envelope" sit in the body. They describe the current state with a revisit signal, and no schema is adopted. I read this as not a lean, but a stricter reading would call it one.

4. L17 and L4 — PASS
- L17 holds in §2.5, §4.7, the compose and view rows, and collision row X5. The shared layer's home and API are open, discovery is not delivery, and no common framework is authorized.
- L4 deaths are not reopened. §4.3 says send-keys is a recorded death and qualification cannot reopen it. Any claimed exception goes to Majkee with evidence.

5. G4/K5 reconciliation — PASS
- ARCHITECTURE.draft.r2.md §7 ("Reconciliation with the growth law, inferred: houston") and lock-proposals P1 both state it: a README-only folder is K5's folder stage entered early, and growth continues inside it.
- The parent directory and taxonomy are left open. The reconciliation is grounded in brief.component-docs…:127 and :251–252.

6. Wrapper diff — PASS
- `git -C /home/hruzam/unikuklatrix/nablarva apply --check raw/wrapper-thinning.diff` on the shared tree exited 0. The shared PROJECT-DESIGN.md is unchanged.
- In the scratch repo, the blob was extracted by `git show 74e94d55…`, and `git hash-object` returned 74e94d55…. `git apply --check` exited 0, then the diff was applied.
- After apply:
  - `# KEYS CODE` survives at line 294.
  - The pointer is `docs/ARCHITECTURE.md#5-keys-code`, and the candidate has `## 5. KEYS CODE` at line 205.
  - The file ends with `\n` (`tail -c 1 | od -c` shows `\n`, both before and after apply).
- Live citations to "PROJECT-DESIGN.md § KEYS CODE":
  - pulse.md:10 is the ovitmugen-01 gate line.
  - ovitmugen-01-basement/STATUS.md:17 and :21, and RUNBOOK.md:14, :42, :68 and :95, cite it.
  - Other pulse-routed STATUS files have no citation.
  - The X3 STATUS cite is a mention.
  - GLOSS.nablarva.md:661 links `#keys-code`.
  - All of these resolve to the surviving heading.
- Semantic note: the key table itself moves to docs/ARCHITECTURE.md. The ovitmugen gate says keys "match § KEYS CODE", so the order dependency (apply with or after promotion) matters. The diff header states it.

7. Houston route evidence — PASS, with one classified deviation
- Reproduced:
  - H = 179, the first SubagentHandback.
  - `head -n 179 | sha256sum` = 4f19e0567ba384c0e8343686a1c2da049fe62bc3d2cf763d4f298d514f3c14a6, and 1531193 bytes.
  - Handbacks at 179, 242, 263, 336 and a new one at 383.
  - Reads before 179 match the evidence file: lines 16 identity, 17 binding.claude, 21 cards/sitting, 32 nablarva addendum, then the bed files.
  - Non-Read tools before 179 are only Glob, Grep and one Write (arc.md).
  - Agent/Task spawns: none.
  - Write events: 11 in the whole file, all in raw/ and all on the permitted list. The four r2 files and the revision log are at lines 359–376. None are Edits.
  - Route line with canary cl-e1a94c37 and the stamps 3702b18f / 6181ad36 / d9ee9067 / 630f58c3 open the first handback. They match the stamps in the files' current frontmatter.
  - Observed model is claude-opus-5-5, and the wrapper declares opus.
- Classification of the head's observation:
  - The wrapper says "read each file, in this order", with the addendum before the card. The child read the card (record 21) before the addendum (record 32).
  - This is a minor procedural deviation from the wrapper's order text. It does not affect the RUNBOOK criteria (reads before the first answer, Route and stamps, no spawn, write scope).
  - The stamps are printed in the canonical order. Non-blocking, but it is a real deviation and not a pass on order.
- Limits:
  - The transcript has grown from 337 to 384 lines. The sha256 of the whole file therefore differs from the evidence file's; the fixed-prefix hash is the check.
  - The evidence artifact ends at 337 lines. The r2 writes are covered only by my rerun.
  - Record 15 is an assistant text block of 98 characters before the first Read. It is not a Route line, and I did not read its content because the transcript is off limits. I could not classify it.
  - Only the first 6 lines of each handback were printed, filtered to Route and stamp lines.

8. Scope vs before-state — PASS
- Houston's Write events cover only: arc.md, arc.r2.md, arc.pick.2026-10-22.md, ARCHITECTURE.draft.md, wrapper-thinning.diff, lock-proposals.md, card.sitting.draft.md, ARCHITECTURE.draft.r2.md, lock-proposals.r2.md, card.sitting.draft.r2.md and revision-log.r2.md. All are on the permitted list.
- The other dirt in the bed is not Houston's:
  - M RUNBOOK.md and STATUS.md
  - _bus/
  - raw-additional-my-appology/
  - raw/crawl.*, evidence.*, vector.*, relay.*, answers.*, brief.preflight…
- `git status` outside the X2 and X3 beds is clean. PROJECT-DESIGN.md, flag.md, pulse.md, docs/ and PROJECT.yaml show no diff against HEAD.

9. STATUS.md YAML — PASS
- `python3 -I` with `yaml.safe_load` found 1 yaml block, which parsed to a dict with keys updated, writer, host, worktree, gate, checkpoint, in_flight, recovery_probe, holds, next, expected.

Failures
- /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/ARCHITECTURE.draft.r2.md:139 breaks criterion 2 (claim type). `locked: L17` is cited for "does not require a session bed, editor, tmux". That text is from the composer handoff and belongs under `said:`. Wording-class, but a lock cited wider than its text.
- Not failures, flagged for the head: the §8 defaults table caution (check 3), the line 99 and line 153 tags (check 2), the card-before-addendum read order and the unread record-15 text (check 7).
- Any change to ARCHITECTURE.draft.r2.md means a new revision file and a new hash. Per the base-moves rule, the diff and base are unaffected.

Reproduce
- Hashes: `cd <bed>/raw && sha256sum ARCHITECTURE.draft.r2.md lock-proposals.r2.md card.sitting.draft.r2.md wrapper-thinning.diff`
- Diff check: `git -C /home/hruzam/unikuklatrix/nablarva apply --check <bed>/raw/wrapper-thinning.diff`. For the scratch check, `git init` a fresh dir, run `git show 74e94d5519be6a2de1565ad686ab16cdff6c64c2 > PROJECT-DESIGN.md`, then `git apply`.
- Route evidence: run the commands in raw/evidence.houston-route.r2.eagle.2026-10-22.md with F set to the agent-a0618d796fbb697ce.jsonl path. Check `head -n 179 "$F" | sha256sum`.
- Claim defect: `sed -n 139p <bed>/raw/ARCHITECTURE.draft.r2.md`, and compare with `sed -n 22p <bed>/raw/handoff.composer-boundaries.cartan.2026-10-22.md`.
- STATUS YAML: `python3 -I -c 'import re,yaml;print(type(yaml.safe_load(re.findall(r"```yaml\n(.*?)\n```",open("<bed>/STATUS.md").read(),re.S)[0])))'`
