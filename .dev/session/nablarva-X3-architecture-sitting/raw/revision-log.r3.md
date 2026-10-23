---
doc: revision log r3 — R8 assay correction (lock-scope class)
seat: houston · card: sitting · 2026-10-22
input: raw/witness.r8.assay.2026-10-22.md (FAIL on check 2; checks 1, 3–9 PASS), head-confirmed against flag.md:204 and handoff:22
base unchanged: HEAD 78059da · PROJECT-DESIGN.md blob 74e94d55…; `## 5. KEYS CODE` kept, so wrapper-thinning.diff stays valid
---

# Revision log r3

Line numbers refer to ARCHITECTURE.draft.r2.md. Every change is in ARCHITECTURE.draft.r3.md.

| # | item | r2 line | change in r3 |
|---|---|---|---|
| A1 | **Blocking (assay check 2).** "Composition does not require a session bed, editor, tmux or ovitmugen (locked: L17)". L17 only says "independently useful clients". | 139 | Split the claim. "Termbrana composition and ovitmugen are independently useful clients (locked: L17)". The full sentence is now a quote with the source `said: composer handoff, incorporation text; also termbrana README §Layering B`. (§4.2, first bullet) |
| A2 | Lesser: "Optional parts fail soft \| locked: L17". | 99 | Changed. The column now reads "consistent with (`inferred: houston`)", with a note that it is a consistency reading, not a lock statement. The cell quotes the lock text it rests on: L17 "independently useful clients" and the termbrana README quote. (§3) |
| A3 | Lesser: "clipper and processor not moved by L8′ … (locked: L8 · L8′)" is an inference tagged as locked. | 151–153 | Changed. The lock text is cited separately: L8 places Cluster A (clipper/processor/composer); L8′ supersedes it "for this work". The conclusion is now tagged `inferred: houston`. (§4.2, Retained boundary) |

**Sweep: same class (`locked:` cited past the lock's text).** I checked every `locked:` tag in r2
against flag.md. The tags below were wider than their lock and are fixed. Every other tag stays
inside its text.

| # | r2 line | finding | change in r3 |
|---|---|---|---|
| S1 | 50 | Composition row, forbidden effect "sending" under `locked: L17`. L17 forbids neither all sending nor human-operated push. It requires checked target binding and explicit authority, and it grants no autonomous sending from assistant drafts. | The cell now reads "transmission without checked target binding and explicit authority; autonomous sending from assistant drafts". |
| S2 | 52, 77–79 | View row and dependency item 4: "never own their lifetime", grounded in `locked: L17`. But L17 *gives* ovitmugen, which also sits in the view plane, protected process-lifetime ownership. Citing L17 for "viewers never own lifetime" contradicted its text. | Restated. Detaching or closing a view never ends a session (locked: L14 D5). Process lifetime is ovitmugen's protected ownership, not any view's (locked: L17). "A viewer never owns lifetime" stays as said: PROJECT-DESIGN §3.2.x (candidate). |
| S3 | 81–82 | "no common framework or transport is authorized" dropped L17's qualifier "by the Phase 0 build". | Qualifier restored, and the "concrete shared-layer ownership/home/API remains open" wording follows L17. (§2 item 5) |
| S4 | 115 | Room-truth owner "stridulatrix journal (locked: L3 S1; name L13)". L3 does not name stridulatrix; joining the two is a reading. | Changed to: the journal's single writer is the broker, named stridulatrix. The name is locked by L13. The journal's attribution to stridulatrix is said: PROJECT-DESIGN §3.7 ("L3 supplies the single-writer room journal"). |
| S5 | 179 | "Private visibility is a boundary inside the ledger, not a separate store (locked: L3 S3)". "not a separate store" goes past L3's "private = in-ledger visibility boundary". | Changed to "Private is an in-ledger visibility boundary (locked: L3 S3)". |
| S6 | 263 | "An attached palette is not a sending authority (locked: L17)". L17 does not mention palettes. | The sentence is now quoted from its source, said: keys brief, and marked "consistent with" L17's discovery-is-not-delivery rule. |
| S7 | 310–311 | Organ lines put descriptive words under `locked:`. "tmux frame and session view manager" and "the read-only ear" are not in L17 or L13. | Split. The descriptions are now said: PROJECT-DESIGN §3.2 / §3.6. The locked parts are view/layout + protected process lifetime (L17) and the observation-lab name (L13). |
| S8 | 378 | Collision X1, "L4 (recorded death; an exception returns to Majkee)". The exception route is this document's rule, not L4's text. | Moved outside the lock parenthetical: "L4 (recorded death) · L3 S5 · L17 — any exception returns to Majkee (§4.3)". |

**Sweep of the other candidates.** lock-proposals.r2.md: its L-references sit inside proposed text
or notes and stay within the cited locks (L11 "flag line or session brief", L17 lifetime and
independent clients, L16.12). card.sitting.draft.r2.md has no lock-scope claims of this class.
**No r3 for either.**

**Not changed.** §8 "Defaults and their revisit signals" stays as in r2. The assay's caution about it
is for Majkee, not a change request (head instruction).
