---
doc: arc — X3 architecture sitting (G9 delta + documentation alternatives)
seat: houston · card: sitting · route: child of the Claude Oraculum MAIN head (Mode B), operator-assigned
written: 2026-10-22 · office
state: AWAITING MAJKEE'S PICK — nothing below is drafted architecture; no ARCHITECTURE.draft.md, diff, lock text or card draft exists yet
pen: new files in this bed's raw/ only; no spawn; head supplies reads
base-pin (said: crawl.r1-mechanical §1a–1c, 06:50): HEAD 32bd6f4b8a2be8ab65d2b5bd523f8e8f8c08956d · PROJECT-DESIGN.md blob 74e94d5519be6a2de1565ad686ab16cdff6c64c2 · sha256 6ee10aa1c40a853cc6c1e6ff5dfa191999f38314058064b5543ac1392fe2c78f — re-pinned at drafting time, not reused
---

# Arc — X3 architecture sitting

Tags follow L16.11: `said: <source>` · `inferred: houston` · `locked: L<n>` · `unknown: <what>`.
G4 and G5 are cited as `said: majkee (gavel deck STEP 4 / STEP 5)`. Neither has a flag L-id.

**Pen note (a finding, not a workaround).** The prompt says "After majkee picks, record the pick in
it [arc.md]". The child-sitting pen in the binding is *new files only*, and RUNBOOK §Sequence says
the same ("use a new raw revision file"). Where they conflict the binding wins, so the relayed pick
goes into a **new** file, `raw/arc.pick.2026-10-22.md`. This file is not edited after it is written.

---

## 1. G9 delta since the 2026-10-07 audit

The 10-07 audit walked `AGENTS.PROJECT-DESIGN.md` (said: houston-audit.2026-10-07 §Scope). I
re-read the current sources below myself. Commit facts come from the mechanical packet.

| # | change since 10-07 | evidence | effect on the audit's findings |
|---|---|---|---|
| D1 | **Houston fold + germline install, 10-10 → 10-21.** The project wrappers were retired, the bindings went global and the addendum was stamped. Keeper = audit card. The child-sitting rule was added 10-21. | said: crawl §3a `b57e199` (10-12), `6f3204d` (10-13); §4a ia-sync `e3231c3` (10-14), `bfeb2eb` (10-15), `946cdce` (10-17), `5e5cc3b` (10-21). said: PROJECT-DESIGN.md frontmatter `maintainer: role: houston · card: audit`. | The keeper prerequisite named in the audit's diff note is **discharged**. The audit's own C1 wrapper hunk is in effect: VOLATILE now says the ia-sync scripts "are distinct from the … retired by L12 — those lived in `nablarva.devenv`". |
| D2 | **Wrapper move** to `/PROJECT-DESIGN.md`. The stridularium wrapper moved to `docs/organs/stridularium.md`. A flag L14 D5 pointer was appended. | said: crawl §3a `22cfa26`, `33613c4` (10-17). | The audit's **line cites into the wrapper are stale**: KEYS CODE is now at :293–343, not 277–327, and the §3.2.x notes are at :178–229. J1's *substance* still holds (see D7). |
| D3 | **L8′.** Composer publication goes to or through ia-sync and supersedes L8's location. | locked: L8′ · said: crawl §3a `fff20b8`. | This is new since the audit. The composer is no longer an `applications-in-common` matter. |
| D4 | **L17.** Termbrana = the Zellij observer at `toolbox/termbrana/` plus the composition family at `~/ia-sync/zsh/termbrana/`. Composition and ovitmugen are independent clients. Ovitmugen keeps view/layout and process lifetime. Discovery ≠ delivery. Grammar v4 is approved. | locked: L17 · said: crawl §4b/§4c (source exists, `e290aee` 10-22) · said: toolbox/termbrana/README.md §Composition and explicit input direction (+100 lines, crawl §3b). | **This is the first organ home outside this repo that a lock establishes.** The 10-07 audit could not see it. The architecture doc must carry cross-repo homes. `unknown:` which commit brought L17 into flag.md (request R-2). |
| D5 | **Generation-X.** (a) VIST principle brief (10-18/19). (b) Two beds, `termbrana-X1-composer-sourcing/` and `termbrana-X2-composer-sublime-ide/`, raw only, with no RUNBOOK/STATUS and no pulse row. (c) composer-01-parse Phase 0 exit (10-21), uncommitted evidence. (d) X2 builder bed: gate = a termpanum build plan "using … the parallel X3 architecture work". | said: crawl §8a/§8b, §9 · said: termbrana-X1 handoff §1 · said: composer handoff §Capability wording · said: X2 RUNBOOK `goal:`. | VIST brings in **sensor → controller → actuator**, with Antensor as a read-only sensor and an actuator that sends a "short nudge into a pane". `inferred: houston` — this **overlaps L13's termpanum** ("observation lab = termpanum", the read-only ear). The actuator overlaps **stridulatrix's proposed write ownership** (wrapper §3.7) and the **L3/L4/L17 seams** (tmux never the protocol; send-keys injection is a recorded death; human-operated tmux push sits outside the protocol until qualified). The X2 termpanum plan depends on how this overlap is described. VIST's own marks: names and the passive approach are "decided", meaning *chosen in conversation*. No flag line exists, so the right tag is `said:`, not `locked:`. |
| D6 | **Current working tree.** PROJECT-DESIGN.md is clean against HEAD. No Composer wrapper edits are pending. Composer's architecture-owner text exists and is **unapplied**. Foreign changes sit only in the composer-01 and X2 beds. | said: crawl §1d, §7a · said: composer handoff ("remains unapplied to the current architecture pointer"). | There is no competing wrapper edit to sequence *today*. There are still **two architecture-owner texts in flight**: Composer's proposal and this sitting's draft. |
| D7 | **What still holds from the audit.** | said: current files, read 2026-10-22 | **J1 open (partly):** the KEYS CODE body is still whole in the wrapper, and the §3.2.x ovitmugen notes are still there. Termbrana §3.1 is now pointer-shaped (`checked: 2026-10-21`), so J1(b) is resolved for termbrana. **J2 open:** AGENTS.md still says "architect (@Houston-family) — plan + gates; owns `.dev/session/pulse.md`" and PROJECT.yaml still has `agents: [architect, …]`. That is a saddle edit outside this pen. **M3 / C1 lock side open:** L12's text is unchanged (said: flag.md L12), and X1 check 6 has not been appended. |

**Materiality.** `inferred: houston`. The delta is **material to what the draft must say**: D4 is a
cross-repo home under a lock, and D5 introduces a sensor/controller/actuator vocabulary that
overlaps locked and proposed owners. It is **not material to the audit's verdicts**: every
10-07 finding still holds in substance, and only the line cites have gone stale. A fresh
audit now would mostly re-walk what this sitting has to walk anyway. My proposal is that **G9 a
stands**: no fresh audit before drafting, and X1 check 5 is the fresh audit after promotion. This
is Majkee's call (G9's condition), so Q1 below asks it. If Majkee orders the audit, the
`to-oraculum` prompt in §6 is ready.

---

## 2. What every alternative holds fixed

These are the constraints that apply to all shapes. Alternatives vary only the *document's* shape and
never the animal's direction (said: prompt; G1 b: the tmux/PTY + Zellij direction wins, and intent discovery is not restarted).

1. **One file.** The doc is `docs/ARCHITECTURE.md` (locked: L16.9), drafted at `raw/ARCHITECTURE.draft.md`. It is tier 0 and
   creates no new surface (said: record K1/K8). Its first section keeps the "shape of record"
   pointer to the triad (said: record §Migration notes).
2. **Header = `checked:` stamp only.** No `half_life_days`, no nudge (said: majkee G6 a) and no
   source-engine frontmatter. Frontmatter is a design candidate in the Boost concept, not an adopted
   format (said: majkee STEP 4 + boost concept "no implementation or schema approved").
3. **KEYS CODE moves whole, now** (said: majkee G3 a). The D3 acceptance cite is commit-pinned (pin
   requested, R-1). The wrapper keeps one line and a pointer **under the same `# KEYS CODE` heading**, so the
   pulse / ovitmugen-01 cite "PROJECT-DESIGN.md § KEYS CODE" still resolves. Moving the accepted grammar does **not**
   settle the larger keyboard / command-discovery design (said: brief.keys-command-discovery
   §Subsequent disposition). That design stays an open item.
   - **Commit-order dependency** (`inferred: houston`): the KEYS hunk of the wrapper diff must
     land **with or after** promotion of `docs/ARCHITECTURE.md`. If it lands before, the wrapper points at
     a body that does not exist. Majkee sets the order (said: RUNBOOK).
   - ovitmugen-01 STATUS holds "PROJECT-DESIGN.md append-only" (said: its STATUS :35). `inferred:
     houston`: that rule binds that bed's own writers, not the keeper's commit. The ovitmugen head
     should still see the move before its gate walk, because its acceptance sentence then reads
     through a pointer.
4. **Organs = one line each, with a home or `home: unknown`** (said: majkee G2 a). The substance sits
   in cross-organ sections. Composer enters **as Termbrana's composition family**, not as a separate
   organ (said: majkee G2 "termbrana now starting from `composer-01-parse`"; locked: L17).
   Instarmux and reposoma-tool get `unknown:` lines, organ or placeholder. VIST/Antensor gets **no organ line**.
   It is a substrate pointer and an open overlap question (G1 says to point at VIST, and no lock places it).
5. **Homes per G4** (said: majkee STEP 4, own: "Taking your team RESULT as GAVELED"). Existing
   homes stay. For *new* bodies the direction is a component folder with a thin `README.md` entry and chapters on need.
   The organ/toolbox taxonomy stays under architectural review. Metadata and adapters wait for their
   consumers. **The parent directory for new folders is not specified, and I will not invent one.**
   - **G4 ↔ K5 reconciliation** (`inferred: houston`, to be carried into the draft and lock-proposals).
     K5's ladder is line → sub-chapter → folder (said: record K5). G4's direction is folder-plus-README for a *new*
     body. I read these as compatible if "folder with only README.md" is understood as K5's folder stage
     entered early, and the line → chapter growth then continues *inside* the README (README section → `res/`
     chapter). Existing single-file bodies (`docs/organs/stridularium.md`) are not migrated just for
     symmetry (said: component-docs brief §2 "Existing homes should not migrate solely to make a
     drawing symmetrical"). This is the reconciliation the RUNBOOK assigns to me, and it stays a proposal
     until GO.
6. **Decisions per G5** (said: majkee STEP 5, own + "gaveled" on the reading schedule). Locks are
   in flag. Product-technical rationale goes in component ledgers (the termbrana `DECISIONS.md` pattern, locked:
   L11). The team/controller direction for task-bound context and the who-reads-what-when schedule
   are accepted. **Not decided:** the reader schema, the program home/API, and whether the root
   `docs/decisions/README.md` stub is corrected or retired. The draft names that stub's ambiguity
   and does not touch the stub.
7. **Docket and open items.** Every docket-dependent part is marked `unknown: docket #N` (said: majkee G1 b).
   Leans go **only** in `lock-proposals.md`, as `inferred: houston`, with docket 2 excluded (said: majkee G7
   b). Majkee's qualification also applies: "ad hoc can shift behind boundary … not … too tight cage". So each
   shape below may carry a reasoned ad hoc section where the material does not fit. Such a section is named
   and justified, and it does not silently replace a lock.
8. **Accepted vs planned, everywhere a consumer depends on it** (said: composer handoff
   §Capability wording, cycle37). Phase 0 *validates* packets and preserves opaque bytes. Sourcing,
   preparation, loader, renderer, activation and delivery are *planned*. Every generation-X sourcing
   category survives with its owner (said: termbrana README §Future adjustable sources; locked: L17).
9. **Composer's architecture-owner text** (said: handoff, proposal file) is input to the Termbrana
   seam, re-derived from L17 and attributed by path. It is not pasted as an organ paragraph, because that
   would break G2 a's one-line depth. I checked its claims against L17 and found no contradiction.

---

## 3. Alternatives — the document's shape

### A — Spine (the L16.9 list, in order)

```text
0 shape of record (triad pointer) · checked: stamp
1 layer model            2 dependency direction        3 shared grammars (KEYS CODE)
4 cross-organ ownership (prose, one bullet per responsibility)
5 system-wide boundaries (prose)                       6 the ladder, stages 1–3 (L2)
7 organ list (one line + home)    8 decisions & reading schedule (G5)    9 open questions (G1/G7)
```

- **Strength.** It matches L16.9 and the prompt's list item by item, so it is the easiest for assay and Cartan to check
  against the gavels and the most familiar to a fresh reader.
- **Cost / risk.** Ownership (§4) and boundaries (§5) get written separately about the *same* seams,
  for example "discovery ≠ delivery" under both. That tends to fork one fact into two places (L16.10). Accepted vs
  planned has no fixed column, so whether it gets marked depends on prose discipline.
- **Where VIST lands.** In §9 as an open overlap with termpanum and stridulatrix, plus one sentence in §1.

### B — Seam ledger (L16.9 content, with ownership + boundaries keyed by seam)

```text
0 shape of record · checked:          1 layer model (short)        2 dependency direction (short)
3 SEAM LEDGER — one row per cross-organ seam:
    seam · owner · consumers · governing lock · accepted · planned · open (docket/unknown)
    e.g. observe · compose · deliver/write-into-session · view-layout & process lifetime ·
         room truth · human door · cross-host · checkout coordination · context sourcing/reading ·
         key meanings
  3.x short notes, only where a row needs more than a cell (each points to its owning source)
4 shared grammars (KEYS CODE, moved whole)   5 the ladder — which seams each stage needs (by reference)
6 organ list (one line + home)    7 decisions & reading schedule (G5)    8 open questions
```

- **Strength.** Every coherence risk the generation-X evidence names is a seam property:
  accepted vs planned (cycle37), discovery ≠ delivery (L17), observation ≠ acceptance (wrapper
  §3.7, VIST limits), viewer ≠ lifetime owner (L17). A row with fixed *accepted / planned / open*
  columns makes manufacture visible cell by cell, and assay can check each cell's tag. The VIST overlap shows up as
  **two candidate owners on the "observe" and "deliver" rows**, which is honest and is not a decision. Ownership and
  boundary are stated once per seam, which fits L16.10.
- **Cost / risk.** Table cells compress. Nuance can only survive in 3.x notes that point outward, so the
  table must never become the only home of a qualification. It departs from L16.9's *listing order*, but not
  its content. L16.9 names contents, not order (`inferred: houston`). It is a slightly larger first
  review.
- **Where VIST lands.** As candidate cells (`said: VIST brief`, unplaced) on the observe and deliver rows,
  plus an open question. Termpanum keeps the locked name for the observe row (locked: L13).

### C — Ladder-staged (organized by L2 stage)

```text
0 shape of record · checked:   1 layer model   2 shared grammars (KEYS CODE)
3 stage 1 — same host: organs present, their seams, what is accepted/planned
4 stage 2 — cross-host: S7 protocol, O2 transport open
5 stage 3 — stridularium: the human door, L14 D5/D6
6 organ list · 7 decisions & reading schedule · 8 open questions
```

- **Strength.** It shows at a glance what exists (almost all stage 1) against what is aspirational, and it follows the locked
  framing (L2).
- **Cost / risk.** Organs and seams cross stages. Termbrana, ovitmugen and termpanum all reappear in stages 2 and 3, so
  ownership gets restated per stage (against L16.10) or crammed into stage 1. Stages 2 and 3 are mostly
  `unknown: docket 4/5/6 · O1/O2/O3`, so two of three chapters would be lists of unknowns.
  `inferred: houston`: this shape is the most likely to read as a roadmap, which is a progress register the
  architecture doc must not become (said: record map "never becomes … a progress register" for the wrapper,
  by analogy).

### Lean — `inferred: houston`

**B.** The draft is the first body of the whole-animal doc, and the failure this project has actually
recorded is a planned capability silently read as an accepted dependency (cycle37), together with seams that
change owner without anyone noticing (L17's layering B; the VIST actuator vs stridulatrix). B is the only
shape that gives "accepted / planned / open" a fixed place. A is the safe literal reading and a
reasonable pick if Majkee prefers L16.9's order over the ledger. C is listed for completeness, and I
would not pick it. Any shape may take G7's ad hoc section where the material refuses the frame.

---

## 4. Questions for Majkee with the pick

Each one has a default that decides nothing new. A silent answer means the default applies.

- **Q1 — G9 condition.** Is a fresh audit needed before drafting? *Default: no* (see §1 materiality).
- **Q2 — ovitmugen §3.2.x notes (J1 remainder).** G4 leaves the root for a new body unspecified, so
  those notes have no home to move to. *Default:* they stay in the wrapper, the thinning diff touches only
  KEYS CODE (plus pointer lines), and J1's ovitmugen part stays open and listed. The alternative is that Majkee names
  ovitmugen's body home now. That would be his decision and not something I would infer.
- **Q3 — VIST placement.** *Default:* a substrate pointer plus an open overlap question (termpanum ↔ Antensor
  on observe; actuator ↔ stridulatrix ↔ L3/L4/L17 on deliver). No organ line, and no lean in the
  body. A lean can appear in lock-proposals.md under G7 b.
- **Q4 — the two architecture-owner texts.** *Default:* Composer's proposal is consumed as cited
  input to the Termbrana seam. This sitting's draft is the single architecture-owner text, and
  Composer's file stays its own evidence. Commit order is Majkee's.

---

## 5. Reads I need from the head (exact commands; I have no shell)

- **R-1 (G3 pin).** `git -C /home/hruzam/unikuklatrix/nablarva log -1 --format='%H %cs' -- .dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md` and `git -C /home/hruzam/unikuklatrix/nablarva ls-files --error-unmatch .dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md`, plus `grep -n 'D3' <that file>` (quote the D3 lines).
- **R-2 (D4).** `git -C /home/hruzam/unikuklatrix/nablarva log --format='%h %cs %s' -S 'L17 · Termbrana composition' -- .dev/session/flag.md`
- **R-3 (pulse delta).** `git -C /home/hruzam/unikuklatrix/nablarva diff fe32a2951d11ca1004155b08090fabb6f5827fad HEAD -- .dev/session/pulse.md AGENTS.md PROJECT.yaml`
- **R-4 (generation-X tracking).** `git -C /home/hruzam/unikuklatrix/nablarva ls-files .dev/session/nablarva-X4-vist .dev/session/termbrana-X1-composer-sourcing .dev/session/termbrana-X2-composer-sublime-ide`
- **R-5 (at drafting time, re-pin).** `git -C /home/hruzam/unikuklatrix/nablarva rev-parse HEAD; git -C /home/hruzam/unikuklatrix/nablarva hash-object PROJECT-DESIGN.md; sha256sum /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md; git -C /home/hruzam/unikuklatrix/nablarva status --short -- PROJECT-DESIGN.md docs/ .dev/session/flag.md .dev/session/pulse.md`

R-1 and R-5 block the diff. R-2 to R-4 only sharpen the delta's provenance, so the pick can come first.

---

## 6. `to-oraculum` (only if Majkee answers Q1 = fresh audit)

```text
to-oraculum ---
card: audit
Assigned by majkee: fresh whole-animal audit before the X3 sitting drafts (G9 condition).
Walk: /PROJECT-DESIGN.md → docs/organs/stridularium.md → toolbox/termbrana/{README,DECISIONS}.md →
~/ia-sync/zsh/termbrana/README.md → docs/ARCHITECTURE.md → flag (L8′, L16, L17) → pulse → AGENTS.md → PROJECT.yaml.
Output: .dev/session/nablarva-X3-architecture-sitting/raw/houston-audit.2026-10-22.md (+ .diff only if mechanics).
Do not reuse the X3 sitting child for this; the audit is a separate Houston invocation.
 ---
```

---

## 7. Unknown after this arc

- `unknown:` the commit that introduced L17 into flag.md (R-2), and the D3 acceptance commit pin (R-1).
- `unknown:` whether instarmux and reposoma-tool are organs or placeholders (wrapper §3.3/§3.4 are empty).
- `unknown:` the root directory for new component-folder bodies (G4 left open).
- `unknown:` the reader schema, program home/API and root ADR stub disposition (G5 left open), plus the editor target beyond
  "Sublime as the current target, app-neutral intended" (said: majkee G2) and the JSONL / `.nablarva` history home (said:
  majkee G2 "Just FYI"). None of these will be decided in the draft.
- `unknown:` docket 2, 4, 5, 6, 8 and O1–O4, all as in flag.
- I did not rerun the audit's M1 pointer check across the whole wrapper. I checked by Read only the pointers
  the delta touches. A full M1 re-check belongs to X1 check 5.

## Pick

*(awaiting — the head relays Majkee's words verbatim; they will be recorded as `said: majkee` in the
new file `raw/arc.pick.2026-10-22.md`, per the pen note above)*
