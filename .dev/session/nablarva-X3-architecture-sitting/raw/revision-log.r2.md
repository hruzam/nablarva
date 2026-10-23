---
doc: revision log r2 — dispositions of external review cycle 01
seat: houston · card: sitting · 2026-10-22
inputs: _bus/01.cartan.return.md (RETURN §4) · _bus/01.oraculum.verdict.md (all findings CONFIRMED by the head)
base unchanged: HEAD 78059da137f2b6d17192c251220d80b148aa1ac6 · PROJECT-DESIGN.md blob 74e94d5519be6a2de1565ad686ab16cdff6c64c2
---

# Revision log r2

Every finding in RETURN §4 is listed here. None was declined.

| # | finding (class) | what changed | where |
|---|---|---|---|
| S1 | One `locked: L3` covered S1–S8 **and** Z's five adopted organs. Flag L3 locks only S1–S8 (substantive) | Split the citation. S1–S8 are `locked: L3`. The five organs are a source claim, "not locked commitments" (said: triad comparison) | ARCHITECTURE.draft.r2.md §0 |
| S2 | The delivery model omitted the L14 D4 research-before-build sequence and the D7 blind-triangulation requirement (substantive) | Both are carried as relay-work constraints and stated explicitly as **not** prerequisites for this document. Added to the layer-model room/delivery grounds, to dependency direction item 2 (new), to the deliver row's governing / planned / open cells, to §4.3, to §6 stage 1 and to §9 "Relay research". lock-proposals notes that no proposal is needed because these are existing locks | draft r2 §1, §2.2, §4 deliver row, §4.3, §6, §9 · lock-proposals.r2 "Not proposed here" |
| S3 | The room-truth row cited S3 without stating its visibility boundary. S8 was named but not explained (substantive) | The row's accepted cell now states "private = in-ledger visibility boundary (S3)" and "room state on neutral ground (S8)". §4.5 says no roles, ACLs, schema or O3 topology are chosen | draft r2 §4 room truth row, §4.5 |
| S4 | The retained OUTPUT(A) ↔ stridularium interface boundary was omitted. L8′ retains it (substantive) | Named in the compose and human-door rows and in §4.2 "Retained boundary". The boundary note is pending (L8 "when both threads run"), no API is given, and clipper/processor are not moved, since L8′ covers composer work only. Added to §6 stage 3 and §9 other open items | draft r2 §4 compose + human door rows, §4.2, §6, §9 |
| S5 | "each entry citing its authorizing flag line" dropped L11's "or session brief" (substantive) | Restored "flag line **or session brief**" in both places. P2 adds "(the L11 pattern, unchanged)" | draft r2 §8 · lock-proposals.r2 P2 |
| W1 | Send-keys: the prose called the nudge "unqualified" and asked whether L4's death covers it. Qualification cannot reopen L4 (wording) | §4.3 now reads: a recorded death (locked: L4); qualification alone cannot reopen it; any claimed exception returns to Majkee with evidence; no future gate may presume it. The X1 row in §9 adds "an exception returns to Majkee". The lock-proposals ad hoc item is rewritten as a decision route to Majkee, no longer framed as a gate question | draft r2 §4.3, §9 X1 · lock-proposals.r2 ad hoc |
| W2 | G1 was paraphrased under `said: majkee` (wording; queued by me) | Majkee's report-1 words are quoted verbatim (double spaces kept). The synthesis "tmux/PTY preferred, Zellij where its ceilings can be reached" is tagged `inferred: houston` | draft r2 §0 |
| W3 | The Q answers lacked a path (wording; queued by me) | The how-to-read paragraph names `answers.majkee.pick-and-q1-q8.2026-10-22.md`, with Message A = partial pick and Message B = shape B + Q1–Q8, and says "Q<n>" means Message B. "Pins owed" lists the file as absent from `78059da` | draft r2 header paragraph, §Sources |
| W4 | "locked at GO of docs/ARCHITECTURE.md" conflated document GO with lock adoption (wording) | Each proposal now reads "adopted only if majkee's GO names this proposal". The frontmatter states that document GO does not append placeholder L-lines. The card r2 carries the same rule | lock-proposals.r2 frontmatter, P1–P4 · card.sitting.draft.r2 §Writes |
| scale | G4/K5 folder-first refinement (scale note, not a defect) | No change. The `inferred: houston` reconciliation and the `said: majkee` G4 attribution stay as they were | draft r2 §7 · lock-proposals.r2 P1 |
| G7 | The reviewer was uncertain about the G7 option mapping (RESOLVED by the head from STEP 7 option b) | Leans kept. The lock-proposals.r2 frontmatter now quotes option b's printed text, so the authorization is visible in the file | lock-proposals.r2 frontmatter |

**Directly implied corrections (no new content):** the how-to-read paragraph now says a `locked:`
tag covers only what the flag line enumerates (implied by S1), and that "accepted" can mean a locked
design constraint and not necessarily a working implementation (the reviewer's §2 reading, made
explicit).

**Not revised:** `wrapper-thinning.diff`. The draft r2 keeps the heading `## 5. KEYS CODE`, so the
anchor `docs/ARCHITECTURE.md#5-keys-code` still resolves. The base is unchanged, and the reviewer
reported `git apply --check` exit 0 (UNVERIFIED by the head; R8 reruns it).
