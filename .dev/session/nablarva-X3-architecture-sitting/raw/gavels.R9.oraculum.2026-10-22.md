# R9 gavel deck — GO on the X3 architecture package

`author: oraculum(cSharp), X3 head · 2026-10-22 · for: majkee · shape: raw/shape.gavel-line.2026-10-22.md (candidate), plus two fields majkee asked for: buys · can be lost · ids R9-<n>, so G1–G9 numbering is not restarted · leans are oraculum's, attributed, never decisions`

Driving: one block at a time. Majkee answers; the head records his words verbatim under `answer:`, then the next block.
Silence is not an answer. Every block is readable without opening its sources; `source:` is for verification only.

What has already happened, so no block needs to repeat it: Houston drafted the package. Cartan reviewed it (REVISE →
fixed → PROCEED). Assay witnessed it (FAIL on one over-wide lock tag → fixed in r3 → PASS). Nothing is promoted,
committed, locked or pushed yet.

---

```
GAVEL R9-1 · Do you approve the architecture document r3 as the content of docs/ARCHITECTURE.md?
  options:      a) GO on r3 as it is
                b) GO after one tiny r4: trim "closing" from "closing or detaching a view never ends a session"
                c) revise: name what to change
  context:      r3 is the first whole-animal architecture body: a seam ledger (11 rows: who owns each meeting point
                between organs, what is accepted / planned / open), KEYS CODE moved in whole, the ladder, the organ list
                with homes, decisions and reading, and open questions (dockets, O-items, v0 collisions X1–X13). Every
                claim carries its source type. Assay's last pass found one leftover stretch. In two places the text says
                "closing or detaching a view never ends a session" and cites L14 D5. L14 D5 locks only "detaching never
                closes a bed". "Closing" is consistent with ovitmugen's protected lifetime (L17) and the wrapper's
                candidate "a viewer never owns lifetime", but no lock says it. GO approves the CONTENT only. It does not
                create locks (R9-2), does not promote by itself (R9-4), and does not adopt Houston's defaults table (R9-3).
  buys:         a) the gate closes now; promotion can start
                b) a document with zero known over-wide lock tags — the same class this sitting fixed ten times
                c) whatever you name, before it becomes canon
  cost:         a) none now
                b) one Houston turn plus one narrow assay check (≈10 min, no hands of yours). Houston has used ≈387k
                   tokens, so a degraded reply is possible; if it degrades I tell you and do not replace it silently
                c) one or more review cycles, depending on scope
  can be lost:  a) the canonical doc carries one sentence that cites a lock wider than its text. A later reader could cite
                   "closing a view never ends a session" as locked. It is small, but it is the exact habit the doc teaches
                   against
                b) nothing of substance; only time
                c) momentum, if the change is broad
  consequence:  a) R9 closed; R10 (promotion) waits on R9-4
                b) R9 closes on r4's hash after assay; then R10
                c) back to R7/R8 for the named change
  lean:         oraculum → b) — consistency: leaving the last instance of a defect class knowingly weakens the rule the
                document exists to carry; the cost is minutes
  source:       raw/ARCHITECTURE.draft.r3.md (sha256 88fe67e4…eff0) · raw/witness.r8c.assay.2026-10-22.md check 2 ·
                flag.md L14 D5
  answer:       ___
```

---

Lock proposals. Adopting one makes it a flag line: durable, citable as `locked:`, it outlives this bed, and reopening
it later needs new evidence (flag law). Not adopting leaves the same content in the architecture doc as `said: majkee`.
That is still citable, but softer, and changeable in an ordinary document update. You can adopt, decline, or adopt
with your own amended wording. The L-numbers in the proposals are placeholders; the head assigns real ones.

```
GAVEL R9-2a · Do you adopt P1 (organ-body homes) as a flag line?
  options:      a) adopt as written   b) adopt with your amendment   c) do not adopt — keep it as document text
  context:      P1 says an organ that has a documentation home keeps it (termbrana's toolbox folder, stridularium's
                docs/organs page). A NEW body starts as a component folder with a thin README entry and grows chapters
                only on need. This is the growth law's "folder" stage entered early. Nothing is migrated for symmetry.
                OPEN in P1: the parent directory for new folders, the taxonomy, any frontmatter schema, any reader/MCP.
                Today the Houston addendum still calls this rule "proposed, not locked", while practice already follows
                it (stridularium moved there 10-10). Your G4 answer was "Taking your team RESULT as GAVELED".
  buys:         a/b) the contradiction between practice and the addendum ends; the next organ (e.g. termpanum) has a
                     locked place to land; Houston audits can check it
                c) nothing new
  cost:         a/b) one flag line; a later change of the home rule needs new evidence
                c) none
  can be lost:  a/b) some freedom to pick a different home shape for a future organ without ceremony
                c) the addendum keeps saying "proposed", and each new organ re-asks the home question
  consequence:  a/b) the head appends the line; the addendum row is updated later in the germline forge
                c) the doc text alone carries it (said: majkee G4)
  lean:         oraculum → a) — it records what is already true and what you already gaveled; the open parts stay open
  source:       raw/lock-proposals.r2.md P1 · gavels.X4 STEP 4 report
  answer:       ___
```

```
GAVEL R9-2b · Do you adopt P2 (decision homes and task-bound reading) as a flag line?
  options:      a) adopt as written   b) adopt only the decision-homes half   c) do not adopt — keep it as document text
  context:      P2 has two halves.
                (1) Decision homes: locks stay in flag.md; product rationale lives in component ledgers, each entry
                    citing its flag line or session brief (the termbrana pattern); no root ADR series.
                (2) Task-bound reading: context for a task is prepared before the RUNBOOK is written, re-read by each
                    recipient at entry, and refreshed on reassignment or change; "missing, ambiguous or oversized
                    required context holds the affected action".
                Your G5 answer asked for "fixed way of who in process needs read what" and said "gaveled". OPEN in P2:
                the reader schema, the program home/API, and what happens to the docs/decisions stub.
  buys:         a) every future session gets one locked reading rule: builders, planners and verifiers know when to
                   read what; a head can stop an action for missing context and cite a lock
                b) the decision-home rule is locked; the reading procedure stays flexible until its program home exists
                c) nothing new
  cost:         a) the "holds the affected action" clause binds EVERY head in every session. Without a program that
                   prepares context, heads enforce it by hand, which adds ceremony and can stall work. It is the "too
                   tight cage" risk you named in G7
                b) the reading rule stays soft for now
                c) none
  can be lost:  a) speed in small sessions, until the controller/function exists
                b) the reading discipline can drift until it is locked later
                c) the decision-home rule stays doc-only, and the stub contradiction stays visible
  consequence:  a) one line, effective immediately for all beds
                b) one shorter line; the reading half is re-proposed when its program has a home
                c) doc text only
  lean:         oraculum → b) — lock what is settled and cheap (where decisions live); lock the reading procedure once a
                program carries it, so the rule has a tool and not only a duty
  source:       raw/lock-proposals.r2.md P2 · gavels.X4 STEP 5 report · raw/brief.adr-task-context.2026-10-21.md
  answer:       ___
```

```
GAVEL R9-2c · Do you adopt P3 (VIST as observation principle) as a flag line?
  options:      a) adopt as written   b) adopt with your amendment   c) do not adopt — keep it as document text
  context:      P3 records your Q3 answer as a line. VIST is a shared observation principle and an intended protocol,
                with boundaries first and the concrete contract later. VIST NAMES observations; controller decisions
                and actuator actions are separate components with separate authority. Antensor is an implementation
                candidate. The event envelope is proposed, not adopted. Overlaps with termpanum (observe) and
                stridulatrix (deliver) stay visible and unassigned. Observations authorize nothing. This touches a trust
                boundary: the line between seeing and acting. X2's termpanum plan already treats VIST as a sibling and
                keeps admission separate.
  buys:         a/b) the observation ≠ action split becomes a lock that X2, VIST and future actuator work must cite. An
                     actuator cannot creep in through a VIST implementation without reopening a lock
                c) VIST stays flexible while its design is young
  cost:         a/b) one flag line; if VIST's concept shifts early, the line needs a new-evidence amendment
                c) the split depends on a raw brief plus the doc
  can be lost:  a/b) some early design freedom for VIST
                c) the protection is softer: a future session could blur observation and action and cite only doc text
  consequence:  a/b) the head appends the line; X2/VIST cite it
                c) the doc carries it as said: majkee Q3
  lean:         oraculum → a) — it guards a trust boundary (seeing vs acting), the kind of decision that should not depend
                on a raw brief; everything still unsettled is marked as open inside it
  source:       raw/lock-proposals.r2.md P3 · raw/answers.majkee.pick-and-q1-q8.2026-10-22.md Q3
  answer:       ___
```

```
GAVEL R9-2d · Do you adopt P4 (coherent packages, independent clients) as a flag line?
  options:      a) adopt as written   b) adopt with your amendment   c) do not adopt — keep it as document text
  context:      P4 records your Q5 direction: aim at coherent build/install packages for nabLarva and its toolboxes
                while L17's independent clients hold. Coherent packaging does not select one global router or common
                runtime. OPEN: exact packaging, one vs several packages, any shared runtime mechanism. You said "Record
                that direction now". The doc records it. Houston itself notes that the flag line is "offered, not
                required".
  buys:         a/b) the direction outlives the doc and binds packaging work later
                c) the direction is recorded, without a lock that is mostly OPEN content
  cost:         a/b) a flag line whose substance is mostly "open"; locks that mostly say "later" add flag weight and
                     little constraint
                c) none
  can be lost:  a/b) little
                c) little: the doc keeps it as said: majkee Q5, and a packaging session can lock it when it decides
                   something concrete
  consequence:  a/b) the head appends the line
                c) doc text only; it is re-proposed when packaging is designed
  lean:         oraculum → c) — record it in the doc now and lock it when there is a concrete packaging decision to protect
  source:       raw/lock-proposals.r2.md P4 · answers file Q5
  answer:       ___
```

---

```
GAVEL R9-3 · Do you keep Houston's "defaults and their revisit signals" table in the document?
  options:      a) keep it, labelled as Houston's reading   b) drop it   c) keep it and adopt it as yours (said: majkee)
  context:      In the draft's decisions section, Houston added a six-row table: each current default, its reason, and
                the signal that should reopen it. Examples: "checked: stamp only — revisit when the earned-mechanism
                condition is met"; "organ-local event records, no shared envelope — revisit when docket 8 is gaveled".
                The idea is borrowed from v0's "decision · reason · revisit when" table. It is tagged inferred: houston;
                you never ruled on it. Assay does not count it as a lean, but notes that a strict reader could, mainly
                the event-records row.
  buys:         a) readers see when each default should be revisited, without it pretending to be your ruling
                b) the cleanest separation: the doc carries only rulings and locks
                c) the table carries your authority and becomes a real review schedule
  cost:         a) none
                b) the revisit signals are lost, and the next review must rediscover them
                c) you take ownership of six revisit triggers now. The docket-8 row then reads as your position on
                   event records
  can be lost:  a) little; a reader might over-weight Houston's reading
                b) useful navigation
                c) flexibility on docket 8 framing
  consequence:  a) no change to r3/r4
                b) one more revision (remove the table)
                c) a relabel revision (inferred: houston → said: majkee)
  lean:         oraculum → a) — it is honest about its authority and gives the doc a built-in reason to stay alive; the
                "too tight cage" risk is lowest when defaults name their own exit
  source:       raw/ARCHITECTURE.draft.r3.md §8 · raw/witness.r8.assay.2026-10-22.md check 3
  answer:       ___
```

---

```
GAVEL R9-4 · In what order should promotion (R10) run, and who commits your v0 folder?
  options:      a) head's order below, and the head commits v0 in the bed commit
                b) head's order, but you commit v0 yourself (or leave it untracked)
                c) your own order
  context:      Head's order:
                (1) commit this bed's files, so the doc's citations can pin to a commit; today the answers file,
                    arc.r2, arc.pick and the X2 files are cited only by hash;
                (2) copy the approved revision byte-identical to docs/ARCHITECTURE.md, with both hashes recorded;
                (3) apply the wrapper diff in the same commit as (2) or after it, never before, because the wrapper's
                    KEYS pointer must not point at a missing body;
                (4) write the flag lines you adopted in R9-2;
                (5) send the card draft to the germline-01 forge;
                (6) X1 check 5 (Houston audit of the promoted doc).
                You push; nothing is pushed by the head. v0 is your folder, uncommitted. The doc cites it by sha256.
                If it stays untracked and the bed is pruned later, the citation points at nothing.
  buys:         a) one clean sequence, and every citation resolvable by commit
                b) v0 stays fully under your hand
                c) your own sequencing
  cost:         a) the head commits a folder you created (your explicit word needed — this answer)
                b) one more step for you; if you leave v0 untracked, the doc's v0 citation is hash-only and can break at prune
                c) the head re-plans R10
  can be lost:  a) nothing, if you are content for v0 to be in history as is
                b) v0's durable citation, if it stays untracked
                c) nothing in particular
  consequence:  R10 opens as its own row in STATUS; each step is recorded with hashes; the session's gate closes on your GO
                (R9), not on R10
  lean:         oraculum → a) — the doc depends on v0 as a cited candidate source; committing it keeps that citation honest
  source:       RUNBOOK §Sequence R10 · raw/wrapper-thinning.diff header (order rule) · Houston's pins-owed list (r3 §Sources)
  answer:       ___
```
