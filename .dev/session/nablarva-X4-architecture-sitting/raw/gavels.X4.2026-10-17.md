# pad.1-x4-gavels — the gavel deck for the X4 Houston sitting: nine decisions, answered before the sitting prompt runs

> Operator decision surface. Sequential — one unit, majkee answers, then the next unit.
> Driver: polyp (majkee's Codex shell, `$polyp`, human-driven mode). Authored 2026-10-17 by
> trajectory(bed) on oraculum's dispatch. Reusable shape: copy this file for a later sitting's deck.

## Driver rules (read before STEP 0, every sitting)

1. Human-driven mode only. Reveal ONE unit, wait for majkee's answer, then the next. Never run ahead.
2. The context commands are read-only. Run them, or show them, when majkee wants the source in front
   of him. A fresh shell needs nothing else: every path is absolute.
3. Never answer, rank or nudge past the printed `lean: oraculum`. A lean is a recommendation, never
   a decision. A lean marked `(drafted by trajectory — oraculum to confirm)` is shown with that mark
   until oraculum confirms or strikes it.
4. Paste majkee's answer verbatim into the unit's `>MAJKEE report` block: line 1 = the letter
   (`a` · `b` · `c` · `own`), then his words unchanged. Never paraphrase.
5. Branch per unit:
   - answered with a listed option → `SUPPORTED` → next unit
   - answered with an own option or an amended one → `RESHAPED` → record verbatim, continue
   - majkee wants more context, defers, or asks someone else first → `BLOCKED` → STOP, return the
     deck to the head (oraculum)
   - majkee says the question itself is wrong → `REFUTED` → STOP, return the deck to the head
6. Sink (the one approved distilled home): after the last unit, or at a STOP, go to the GAVELS
   block of
   `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-architecture-sitting/raw/prompt.sitting.2026-10-17.md`.
   On each answered `G<n> … : UNANSWERED` line, replace only the word `UNANSWERED` with
   `<letter> — <majkee's words verbatim>`. If his words run past three lines, write
   `<letter> — full answer: raw/gavels.X4.2026-10-17.md STEP <n>` instead. Unanswered units keep
   `UNANSWERED`. Touch nothing else in that file.
7. STATUS belongs to oraculum (status_owner). Do not edit it; return the result to oraculum.
8. Off-deck questions: answer briefly, return to the unit; park big ones under `## parked`.
9. If majkee seems to need the why behind a unit, ask once: "record it in GLOSS.nablarva.md?"
   Never assume. Explanations never go into this PAD.

Claim marks used in every unit (flag L16.11, never merged): `locked: L<n>` = gaveled in flag ·
`said: <source>` = the source's own words · `inferred: <seat>` = interpretation · `unknown:` = not
established.

Paths used in all commands:
```
REPO /home/hruzam/unikuklatrix/nablarva
BED  /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-architecture-sitting
```

Precondition: the repo is at `core` HEAD `33613c4` or later. `flag.md` is live (L8′ was appended
2026-10-17 in the working tree), so flag cites are anchored by heading text, not by line number.
Other line ranges are as of 2026-10-17; if a printed range misses its `Expected:` anchor, grep the
anchor.

---

### STEP 0 — state check (read-only)

```bash
git -C /home/hruzam/unikuklatrix/nablarva log -1 --format='%h %cs %s'; for f in docs/ARCHITECTURE.md docs/decisions/README.md docs/organs/stridularium.md PROJECT-DESIGN.md PROJECT.yaml meshup/REGISTRY.md .dev/session/flag.md .dev/session/pulse.md .germline/agents/houston/nablarva.md .dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md .dev/architect-now-uncanonical/architecture-process.symmetry.2026-10-06.md .dev/session/nablarva-X1-architecture/RUNBOOK.md .dev/session/nablarva-X1-architecture/STATUS.md .dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md .dev/session/nablarva-X1-architecture/raw/houston-prompts.2026-10-09.md .dev/session/composer-01-parse/RUNBOOK.md toolbox/termbrana/DECISIONS.md; do [ -e "/home/hruzam/unikuklatrix/nablarva/$f" ] && echo "ok      $f" || echo "MISSING $f"; done; for f in /home/hruzam/.germline/agents/houston/cards/sitting.md /home/hruzam/reposoma/raw.settings/README.md; do [ -e "$f" ] && echo "ok      $f" || echo "MISSING $f"; done; grep -c ': UNANSWERED$' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-architecture-sitting/raw/prompt.sitting.2026-10-17.md
```

Expected: a commit line (`33613c4` or newer), 19 `ok` lines, then `9` (the sink is empty).

- all `ok` and `9` → `SUPPORTED` → STEP 1
- any `MISSING`, or a count other than `9` → `BLOCKED` → STOP, paste the output, return to oraculum

>MAJKEE report 0
```zsh

```

---

### STEP 1 — G1 · precondition: may the first doc be drafted before the docket closes?

**Question.** Does L16.9 supersede the ARCHITECTURE stub's "first real architecture doc lands after
the gavel docket closes (v1 language + V1 cut)"?

**Why it matters for the sitting.** If the stub still binds, nothing can be drafted: docket 2 (v1
language) and docket 6 (V1 cut) are open. If L16.9 supersedes it, the sitting drafts now and still
decides no docket item.

**Claims.** `said: docs/ARCHITECTURE.md:12-13` — "lands after the gavel docket closes (v1 language +
V1 cut)" (a pre-L16 pointer) · `locked: L16.9` — `docs/ARCHITECTURE.md` = whole-animal cross-organ
architecture · `locked: flag header` — "Pending items block their dependents until majkee gavels" ·
`said: X1 RUNBOOK check 4` — Houston writes the doc · `unknown:` which parts of the whole-animal shape
actually depend on docket 2/4/5/6/8. The draft has to find that out.

**Where to take context.**
```bash
sed -n '12,13p' /home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md
sed -n '3,6p' /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
sed -n '/· 9 Documentation homes/,/· 11 Epistemic/p' /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
sed -n '/^## Pending gavel/,/^## Open/p' /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
sed -n '56,60p' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-prompts.2026-10-09.md
sed -n '25p' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/RUNBOOK.md
```
Expected: the stub line "after the gavel docket closes" · flag's "Pending items block their
dependents" · L16.9 and L16.10 · docket items 1–8 · the old prompt naming this exact open question ·
X1 check 4.

**Options.**
- `a` · The stub still binds. No draft until docket 2 and 6 are gaveled. → the bed parks, and X1
  check 4 waits on the docket.
- `b` · L16.9 supersedes the timing. The draft proceeds and marks every docket-dependent part
  `unknown: docket #N` without deciding it. → the draft lands now, the stub line becomes history at
  promotion, and the docket stays majkee's.
- `c` · L16.9 supersedes it, and majkee gavels docket 2 and 6 inside the sitting first. → firmer
  draft, but the sitting becomes a docket venue (see G7).

`lean: oraculum` — `b` — L16.9 (2026-10-06) is newer than the pre-architecture stub, and `unknown:`
marking honours "pending blocks dependents" without waiting.

>MAJKEE report 1
```zsh

```

---

### STEP 2 — G2 · draft scope: which organs, at what depth

**Question.** Which organs enter the first draft, and at what depth (a wrapper-style line, or a
sub-chapter per the K5 growth law)?

**Why it matters for the sitting.** The doc holds what crosses organs, never one organ's detail
(L16.9). Depth decides how much the draft says per organ and how much it leaves to organ bodies.

**Claims.** `locked: L16.9` / `L16.10` (organs born thin) · `said: record K5` — "Born thin, promoted
on need: a line first, then a sub-chapter, then a folder" · `said: PROJECT-DESIGN.md §3` — termbrana ·
ovitmugen · instarmux (empty) · reposoma-tool (empty) · muticula · termpanum · stridulatrix ·
stridularium · `locked: L13` (stridularium · stridulatrix · termpanum) · `locked: L11` (termbrana has
its own home and `DECISIONS.md`) · `locked: L8′` (composer publishes via ia-sync; appended
2026-10-17, uncommitted at authoring) · `inferred: trajectory` — composer (`composer-01-parse`) is a
candidate organ the wrapper does not list yet · `unknown:` whether instarmux and reposoma-tool are
organs or placeholders.

**Where to take context.**
```bash
sed -n '/^# 3. APP parts/,/^# KEYS CODE/p' /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md | grep -n '^## '
sed -n '13,20p' /home/hruzam/unikuklatrix/nablarva/meshup/REGISTRY.md
sed -n '16,27p;62,79p' /home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md
sed -n '18,29p' /home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md
sed -n '/L8′ · Composer/,/^## Named/p' /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
sed -n '1,3p' /home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/RUNBOOK.md
```
Expected: wrapper sub-sections 3.1–3.8 · six registry designs · axioms K1–K8 and the growth-law
ladder · the addendum's home map · the L8′ text · composer's goal "A readable packet grammar…".

**Options.**
- `a` · Every named organ gets one line with its home, or `home: unknown`. The substance sits in
  the cross-organ sections (layer model, dependency direction, grammars, ownership). → thinnest
  version. Organ bodies grow later per K5, and the empty ones show as `unknown`.
- `b` · Organs that cross another organ's boundary (stridulatrix, termpanum, stridularium,
  ovitmugen, termbrana) each get a sub-chapter. The rest get one line. → a richer cross-organ
  picture and a bigger review. It risks pulling organ detail into the doc.
- `c` · Only organs with a live bed or a locked name enter (termbrana, ovitmugen, muticula,
  termpanum, stridulatrix, stridularium). Composer, instarmux and reposoma-tool go under open
  questions. → a bounded draft, and a later sitting adds the rest.

With any option, majkee also says whether composer (L8′) enters.

`lean: oraculum` (lean: oraculum, confirmed 2026-10-17) — `a` — L16.9 and K5 put the
substance in cross-organ sections, so one line per organ is enough for a first doc.

>MAJKEE report 2
```zsh

```

---

### STEP 3 — G3 · KEYS CODE: move the grammar now or later

**Question.** Does this sitting move the KEYS CODE grammar from `PROJECT-DESIGN.md` into the draft
(J1 wrapper thinning), or later?

**Why it matters for the sitting.** KEYS CODE is the only accepted cross-organ grammar today, and
L16.9 homes it in the architecture doc. However, a live gate (`ovitmugen-01-basement`, in
`pulse.md`) cites "PROJECT-DESIGN.md § KEYS CODE", and the grammar's acceptance cite points into
that bed's `raw/`, which dies at its prune.

**Claims.** `said: PROJECT-DESIGN.md # KEYS CODE` — "ACCEPTED by majkee 2026-09-29 (D3 …)" and "the
meanings live only here" · `locked: L16.9` (shared grammars → the doc) · `said: record §Migration
notes` — "moves to docs/ARCHITECTURE.md, and the wrapper keeps one line and a pointer" and "Pin it
(`nablarva@<sha>:path`)" · `said: audit J1` · `said: pulse.md` ovitmugen-01 gate cites § KEYS CODE ·
`inferred: trajectory` — moving it while ovitmugen-01 is live means the wrapper pointer under the same
heading has to keep resolving.

**Where to take context.**
```bash
sed -n '/^# KEYS CODE/,/^## Shared meanings/p' /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md
grep -n 'KEYS CODE' /home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md
sed -n '124,130p' /home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md
sed -n '60,77p' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md
sed -n '25p' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/RUNBOOK.md
```
Expected: the KEYS CODE header with "ACCEPTED by majkee 2026-09-29" · the ovitmugen-01 pulse row ·
migration notes on KEYS CODE and the pin · J1 · X1 check 4 ("KEYS CODE grammar moved out of the
wrapper").

**Options.**
- `a` · Move it now. The draft carries KEYS CODE with its acceptance (majkee 2026-09-29, D3 cited
  commit-pinned). The thinning diff leaves one line plus a pointer under the same `# KEYS CODE`
  heading. → J1 closes for the grammar and it has one home after promotion. The ovitmugen-01 cite
  still resolves.
- `b` · Move it later. The draft points at the wrapper's KEYS CODE and lists the move as open, with
  no KEYS hunk in the diff. → no risk to ovitmugen-01, but the first doc lacks its one shared
  grammar and J1 stays open.
- `c` · Copy it into the draft now and cut it from the wrapper after ovitmugen-01 closes. → two
  copies in the window, against one home per fact (L16.10). Listed for completeness.

`lean: oraculum` (lean: oraculum, confirmed 2026-10-17) — `a` — it is X1 check 4's scope as
written, and the pointer under the same heading protects the live gate.

>MAJKEE report 3
```zsh

```

---

### STEP 4 — G4 · organ-body home: lock `docs/organs/<organ>.md`

**Question.** Is `docs/organs/<organ>.md` (a folder once it outgrows a page) locked as the
organ-body home for organs that have no home of their own?

**Why it matters for the sitting.** The draft's organ list needs a home column. The addendum calls
this rule "proposed, not locked", yet stridularium has lived there since `22cfa26`.

**Claims.** `said: addendum §1` — "proposed, not locked (`inferred: symmetry`, open for gavel)" ·
`said: record §Open (gavel: Majkee)` · `locked: L11` (termbrana keeps `toolbox/termbrana/` +
`DECISIONS.md`) · `locked: L14 D5` 2026-10-17 pointer to `docs/organs/stridularium.md` · `said:
commit 22cfa26` (majkee ruling 2026-10-10, wrapper move) · `locked: L16.12` — only majkee's GO creates
a lock; the head writes the flag line.

**Where to take context.**
```bash
sed -n '25p' /home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md
sed -n '136,142p' /home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md
sed -n '1,8p' /home/hruzam/unikuklatrix/nablarva/docs/organs/stridularium.md
grep -n '2026-10-17 pointer' /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
ls /home/hruzam/unikuklatrix/nablarva/docs/organs /home/hruzam/unikuklatrix/nablarva/toolbox
git -C /home/hruzam/unikuklatrix/nablarva log -1 --format='%h %s' 22cfa26
```
Expected: the addendum's "proposed, not locked" row · symmetry's three-line proposal · the
stridularium wrapper header · the D5 pointer · `stridularium.md` and `termbrana` · the move commit.

**Options.**
- `a` · Lock it now. majkee's answer here is the GO, and oraculum writes the flag line: an organ
  with a home keeps it, otherwise `docs/organs/<organ>.md`, then `docs/organs/<organ>/`. → the
  draft's home column is firm, and flag gains one L-line through the head.
- `b` · The sitting drafts the lock text in `raw/lock-proposals.md`, and the draft uses the rule as
  `inferred: houston` until majkee gavels it at GO. → one more gavel at the end; homes stay
  provisional in the draft.
- `c` · Leave it unlocked. The draft lists homes as `unknown` except termbrana and stridularium.
  → minimal change; most organ lines read `home: unknown`.

`lean: oraculum` (lean: oraculum, confirmed 2026-10-17) — `a` — the rule is already practice
(majkee's 2026-10-10 ruling moved stridularium there), so the lock records what is true.

>MAJKEE report 4
```zsh

```

---

### STEP 5 — G5 · `docs/decisions/` (ADRs): open now or stay unbuilt

**Question.** Does the draft open `docs/decisions/` for ADRs now, or does it stay unbuilt until a
decision earns it?

**Why it matters for the sitting.** The stub promises "ADRs then accrue in `decisions/`", while the
record says the folder stays unbuilt until earned. `PROJECT.yaml` already routes `decisions:` to
`flag.md`. The draft has to say where decisions live.

**Claims.** `said: docs/ARCHITECTURE.md:12-13` · `said: docs/decisions/README.md` — "Empty until the
first post-gavel decision" · `said: record §Migration notes` — "stays unbuilt until it's earned. Any
ADR … cites the flag line" · `locked: L16.7` (earned ceremony) · `said: record K8` — "Move up a tier
only when a measurement shows the current tier failing" · `locked: L11` (termbrana's `DECISIONS.md`
pattern) · `said: PROJECT.yaml` `decisions: .dev/session/flag.md`.

**Where to take context.**
```bash
sed -n '12,13p' /home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md
cat /home/hruzam/unikuklatrix/nablarva/docs/decisions/README.md
sed -n '27p;124,128p' /home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md
sed -n '/· 7 Earned ceremony/,/· 8 No autonomous/p' /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
sed -n '1,12p' /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/DECISIONS.md
sed -n '13,17p' /home/hruzam/unikuklatrix/nablarva/PROJECT.yaml
```
Expected: "ADRs then accrue in `decisions/`" · the README stub · K8 and the migration note · L16.7 ·
termbrana's ADR-0000 citing L11 · `decisions: .dev/session/flag.md`.

**Options.**
- `a` · Stay unbuilt. The draft says decisions live in `flag.md`, with product-technical ADRs in
  organ homes (the termbrana pattern). The README stub is untouched. → no new surface; the first
  decision that needs an ADR earns the folder.
- `b` · Open it now with an ADR-0000 that adopts the architecture doc. → a new surface without a
  measured need (K8 tension).
- `c` · Retire the `docs/decisions/` stub in the thinning, leaving flag plus organ ledgers. → removes
  a dangling promise, but a deletion needs its own GO.

`lean: oraculum` (lean: oraculum, confirmed 2026-10-17) — `a` — K8/L16.7: nothing measured
shows flag plus organ ledgers failing.

>MAJKEE report 5
```zsh

```

---

### STEP 6 — G6 · rhythm: a freshness nudge for ARCHITECTURE.md

**Question.** Does `docs/ARCHITECTURE.md` get a freshness rhythm now (a `half_life_days` field plus a
harness-stale-style cron nudge) as a named exception to earned ceremony, or not yet?

**Why it matters for the sitting.** It decides the draft's header. L16.7 adds cadence-type machinery
only once evidence earns it. Reposoma already runs a working `half_life_days` + `harness-stale` loop
for cards that could be borrowed.

**Claims.** `locked: L16.7` · `locked: L16.10` — "Staleness is declared; age is not a finding" ·
`said: architecture-process §9` — "audit cadence | ad hoc audits keep arriving after the drift they
should have caught" (a proposed threshold, not locked) · `said: record rule 5` — each organ line
carries a `checked:` date · `said: reposoma raw.settings/README.md` (`half_life_days`, read by
`harness-stale`) · `said: X1 RUNBOOK U21` (a louder review channel, deferred) · `unknown:` any
measured drift on the doc, which has no body yet.

**Where to take context.**
```bash
sed -n '/· 7 Earned ceremony/,/· 8 No autonomous/p' /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
sed -n '/· 10 Documentation law/,/· 11 Epistemic/p' /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
sed -n '220,232p' /home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/architecture-process.symmetry.2026-10-06.md
sed -n '86,86p' /home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md
sed -n '25,37p' /home/hruzam/reposoma/raw.settings/README.md
sed -n '75p' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/RUNBOOK.md
```
Expected: L16.7 · L16.10 · the §9 earned-mechanisms table · rule 5 "Declare staleness" · the two
freshness fields and the stale rule · U21.

**Options.**
- `a` · Not yet. The draft carries a `checked:` stamp only (L16.10), and the rhythm is revisited when
  §9's condition is met. → no machinery, and staleness is visible from the stamp.
- `b` · Stamp plus a declared `half_life_days` field, with no nudge. → a field nothing reads yet
  (§9: "something parses them").
- `c` · Stamp, field and a cron nudge now, as a named exception to L16.7. → ceremony before
  evidence, and the exception needs its own flag line.

`lean: oraculum` (lean: oraculum, confirmed 2026-10-17) — `a` — the doc has never had a body,
so no drift can have been measured.

>MAJKEE report 6
```zsh

```

---

### STEP 7 — G7 · docket handling: leans, or open questions only

**Question.** May the sitting propose leans for open docket items (and O1–O4) in
`raw/lock-proposals.md`, or only list them as open questions?

**Why it matters for the sitting.** Architecture choices touch docket 2/4/5/6/8 and O1–O4. The
sitting card writes "proposed lock text", but locks and docket weights are majkee's (docket 2 reads
"only majkee weighs").

**Claims.** `said: flag docket` — "2. v1 language … — only majkee weighs" · `locked: flag header` —
pending items block their dependents · `locked: L16.12` — only majkee's GO creates a lock ·
`said: addendum §2` — sitting lock text "is drafted in the sitting's bed; the head carries it" ·
`said: sitting card` — "Writes: … proposed lock text" · `said: PROJECT-DESIGN.md §2.1` — the UI vs
terminal question (open, outside the docket; the sitting card lists "UI vs terminal" as a firing
class).

**Where to take context.**
```bash
sed -n '/^## Pending gavel/,/^## Untabled/p' /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
sed -n '/· 12 Promotion/,/· 13 Houston/p' /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md
sed -n '37p' /home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md
sed -n '14,24p' /home/hruzam/.germline/agents/houston/cards/sitting.md
sed -n '50,54p' /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md
```
Expected: docket 1–8 and O1–O4 · L16.12 · the addendum's sitting row · the stub card's "Fires when"
and "Writes" · wrapper §2.1 question 1.

**Options.**
- `a` · List only. The draft and `lock-proposals.md` list each open item with what in the
  architecture depends on it. No leans. → cleanest separation; majkee gets a dependency map, not
  advice.
- `b` · Leans allowed, but only in `lock-proposals.md`, never in the draft body. Each is marked
  `inferred: houston` with the constraint that drives it. Docket 2 is excluded ("only majkee
  weighs"). → useful counsel, with some risk that a lean reads as a decision downstream.
- `c` · Leans allowed for every item, docket 2 included. → conflicts with docket 2's own wording.

`lean: oraculum` (lean: oraculum, confirmed 2026-10-17) — `b` — L16.15 asks every seat for
useful work with pending checks named, and docket 2's own words carve itself out.

>MAJKEE report 7
```zsh

```

---

### STEP 8 — G8 · the sitting card: write the full card in this sitting

**Question.** Does Houston write `raw/card.sitting.draft.md` (the full sitting card) in this
sitting?

**Why it matters for the sitting.** The stub card says the full card is written at the first real
sitting, and this is it. Card edits are accepted in the germline-01 forge bed, not here.

**Claims.** `said: cards/sitting.md` — "the full card is written at the first real sitting" ·
`said: architecture-process §9` — "the sitting card's full body | the first real sitting" ·
`said: X1 STATUS holds` — "Houston edits happen in the germline-01 forge bed (majkee 2026-10-10)" ·
`said: houston-prompts §5` item 4.

**Where to take context.**
```bash
sed -n '9,24p' /home/hruzam/.germline/agents/houston/cards/sitting.md
sed -n '231p' /home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/architecture-process.symmetry.2026-10-06.md
grep -n 'germline-01 forge bed' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/STATUS.md
sed -n '68,71p;83,87p' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-prompts.2026-10-09.md
```
Expected: the stub card · the §9 row · the forge-bed hold · the old prompt's card-draft lines.

**Options.**
- `a` · Yes. Houston drafts it in `raw/` from what this sitting actually did, and it goes to the
  germline-01 forge bed after GO. → the card is written from a real run, and the forge bed owns
  acceptance.
- `b` · No. The sitting notes card lessons in `raw/arc.md` only, and the card is written in
  germline-01 later. → a smaller sitting, at the risk that the lessons go cold.
- `c` · Yes, but in a second explicit Houston invocation after the review rows (L16.8), so the card
  describes a sitting that has been reviewed. → the card sees the whole run, at the cost of one more
  invocation.

`lean: oraculum` (lean: oraculum, confirmed 2026-10-17) — `a` — this is the earning event
named in §9, and the forge bed still gates acceptance.

>MAJKEE report 8
```zsh

```

---

### STEP 9 — G9 · audit input: cite the 2026-10-07 audit, or run a fresh one

*Added beyond the dispatched eight because the sitting card demands it: its inputs include "a fresh
audit (required unless equivalent current whole-animal evidence is cited)".*

**Question.** Does the sitting cite the 2026-10-07 audit as current whole-animal evidence, or does a
fresh audit run first?

**Why it matters for the sitting.** The 10-07 audit walked the old wrapper
(`AGENTS.PROJECT-DESIGN.md`), before the 10-10 fold, the 10-17 move and L8′. Its J1 and J2 are this
sitting's subject. X1 check 5 is a separate audit that runs after the doc.

**Claims.** `said: cards/sitting.md` inputs line · `said: houston-audit.2026-10-07.md` — walked
`AGENTS.PROJECT-DESIGN.md`, classification "is majkee's to assign" · `said: houston-prompts §5` —
"classified USEFUL" (oraculum's note) · `unknown:` majkee's classification of that audit on record ·
`said: X1 RUNBOOK check 5` · `said: commit 22cfa26` (wrapper move).

**Where to take context.**
```bash
sed -n '18,20p' /home/hruzam/.germline/agents/houston/cards/sitting.md
sed -n '1,16p' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md
sed -n '75,77p' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-prompts.2026-10-09.md
sed -n '26p' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/RUNBOOK.md
git -C /home/hruzam/unikuklatrix/nablarva log --oneline 2ae8636..HEAD -- PROJECT-DESIGN.md docs/ .dev/session/flag.md .germline/
```
Expected: the card's inputs line · the audit header and walk order · "classified USEFUL" · X1 check
5 · the commits that changed the wrapper, docs, flag and addendum since the L16 record.

**Options.**
- `a` · Cite 10-07 as equivalent, with a stated delta (fold 10-10, move 10-17, L8′) that the sitting
  re-reads itself. → no extra run, and Houston names what changed since.
- `b` · Run a fresh Houston audit (`card: audit`) before the sitting, with output in this bed's
  `raw/`. → current evidence, at the cost of one more living session. X1 check 5 then audits the
  promoted doc.
- `c` · Count X1 check 5 (after the doc) as the audit and run none before. → fails the card's
  "required unless … cited" unless (a)'s citation is made, so it collapses into `a`.

`lean: oraculum` (lean: oraculum, confirmed 2026-10-17) — `a` — the walk is ten days old,
its findings are the sitting's subject, and the deltas since are known and nameable. — condition: the sitting's raw/arc.md opens with the stated delta since 2026-10-07 (wrapper fold, wrapper move to /PROJECT-DESIGN.md + docs/organs/stridularium.md, Houston germline install); if Houston finds the delta material, it says so and majkee may order a fresh audit first.

>MAJKEE report 9
```zsh

```

---

## Verdict mapping (the driver fills this after the last unit)

| step | unit | answer | branch | landed in sink |
|---|---|---|---|---|
| 0 | state check | — | | — |
| 1 | G1 precondition | | | |
| 2 | G2 scope | | | |
| 3 | G3 KEYS CODE | | | |
| 4 | G4 organ-body home | | | |
| 5 | G5 decisions/ | | | |
| 6 | G6 rhythm | | | |
| 7 | G7 docket handling | | | |
| 8 | G8 sitting card | | | |
| 9 | G9 audit input | | | |

## parked
