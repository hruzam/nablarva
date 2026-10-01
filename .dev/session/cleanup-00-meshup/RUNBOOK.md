# RUNBOOK: cleanup-00-meshup

```yaml
goal: >
  meshup/ becomes a small design registry (REGISTRY.md + <design>/{DESIGN.md,HYPOTHESES.md});
  every former meshup file lives unchanged under raw.nablarva/ and is reachable by one prefix rule.
gate: >
  Majkee records GO or STOP on Cartan's audit confirming: every former meshup/ path resolves
  under raw.nablarva/ by the one-prefix rule (100 % git renames, zero content edits),
  meshup/REGISTRY.md maps every source to a design slug or names it orphan, each slug carries
  DESIGN.md + HYPOTHESES.md, and the three pointer files carry only the one-line redirect.
participant_1: [oraculum, {brand: claude, model: opus, effort: high}, host: office hruzam-120922, role: head · composes groups · spawns executors · status_owner]
participant_2: [cartan, {brand: codex, model: as-declared-by-cartan, effort: high}, host: office hruzam-120922, instrument: resident, role: loop-2 auditor · independent research on hypotheses · copartner reading]
participant_3: [majkee, human, host: office + home, role: slug-map ack before the move · GO/STOP gavel · commits]
status_owner: oraculum
schema_note: runbook GUIDE verified 2026-09-17 · status GUIDE gaveled 2026-08-27 · cross-vendor-seat DRAFT 2026-09-03
```

## Why this session exists

`meshup/` holds ~48 files in ~10 folders grown by accretion (2026-07-31 → 2026-09-13): triangulations,
briefs, research, a stale repomix bundle, a session's RUNBOOK copy. `AGENTS.md`, `README.md` and
`docs/ARCHITECTURE.md` point at paths that no longer exist. Pulse-2 of
`.dev/session/nablarva-X0-restarted/README.md` asks for one cleanhouse: archive the substrate,
rebuild meshup as a registry of designs with their open hypotheses. This session systematizes;
it does not plan architecture.

## Fixed facts

- Redirect rule, mechanical: `meshup/<X>/<f>` → `raw.nablarva/<X>/<f>`. Sub-folder names unchanged.
  Stated once in `raw.nablarva/README.md`. `flag.md` and all `.dev/session/*` history keep their
  old citations; the rule resolves them.
- Root stray `brief.triangulation.2026-07-31.md` → `raw.nablarva/oraculum-basic-triangulation/`.
- `meshup/repomix.meshup.md` is deleted (generated, regenerable).
- Pointer files (exactly three): `AGENTS.md` L56–65 substrate map · `README.md` L26–32 ·
  `docs/ARCHITECTURE.md` L5, L10. Each gets one line: registry → `meshup/REGISTRY.md`, substrate →
  `raw.nablarva/` (prefix rule). Nothing else in those files changes.
- Design slug ≠ source folder (majkee 2026-10-01). Groups are synthesized across folders and may
  contract: sub-hypotheses or small design shifts fold into one design as phases. Fewer, independent
  designs beat a 1:1 mirror of folders.
- Slug form: `<slug>.<one-two-words>.<origin-date>`, date = when the design was born, not today.
  Applies to `meshup/` design folders only; `raw.nablarva/` keeps bare names.
- `DESIGN.md` cites `raw.nablarva/` paths, never copies. `HYPOTHESES.md` is a STATUS-shaped mirror,
  design-scoped, outlives this gate: `updated · writer · design · phases · open · confirmed ·
  refuted · next_probe · expected`.
- "Today wins" is NOT a sort key. REGISTRY entries are small: slug · scope sentence · status
  (live · superseded · parked) · phases · sources.
- Studies are listed in HYPOTHESES.md, not run here. Cartan may research them independently.

## prompt-0 — oraculum (head)

```text
You are the head of /home/hruzam/unikuklatrix/nablarva/.dev/session/cleanup-00-meshup/.
Read RUNBOOK.md then STATUS.md there. You own STATUS.md; you write briefs and the registry.
Loop 1 (study → fold): spawn @Field once per branch, prompt-1 shape, branches:
  A /home/hruzam/unikuklatrix/nablarva/meshup/oraculum-basic-triangulation/ + /home/hruzam/unikuklatrix/nablarva/brief.triangulation.2026-07-31.md
  B /home/hruzam/unikuklatrix/nablarva/meshup/symetry.claude.ai.claude-fable-5/
  C /home/hruzam/unikuklatrix/nablarva/meshup/a-symmetry-lightest/ + meshup/grounded-composites/ + meshup/natural-ladders-grounded-phase.a-sym/
  D /home/hruzam/unikuklatrix/nablarva/meshup/_preflight/
  E /home/hruzam/unikuklatrix/nablarva/meshup/nabla-buffer-brideAndBook/ + meshup/old-but-good-onion/
  F /home/hruzam/unikuklatrix/nablarva/meshup/nablarva-01-design/ + meshup/brief.fold-to-philosophical-technical-blind-questions.oraculumu.nabla-lab.research.md
Cards land in /home/hruzam/unikuklatrix/nablarva/.dev/session/cleanup-00-meshup/raw/card.<branch>.md.
Compose the slug map from the cards (contract across branches; phases over new slugs) into
/home/hruzam/unikuklatrix/nablarva/.dev/session/cleanup-00-meshup/raw/slugmap.md. STOP: majkee acks the
slug map (STATUS next:). Then prompt-2 to @Delta. Then write DESIGN.md + HYPOTHESES.md per slug and
meshup/REGISTRY.md from the cards only — no new content. Then hand to Cartan (prompt-3) via
_bus/01.oraculum.point.md. Executor grades: branch read → @Field; mv + skeletons + pointer
lines → @Delta (surgical); audit → Cartan. Rewrite STATUS before every non-idempotent step.
```

## prompt-1 — field (one spawn per branch, under the head)

```text
Read every file under the paths given. Return ONE card, ≤60 lines, to the path given:
subject (2 lines) · which boundaries it crosses (stage 1/2/3, Claude↔Codex seam, LAB/observability,
naming, broker) · status (live · superseded-by <path> · parked · dead) · design candidates (name,
origin date, one sentence) · sub-hypotheses or shifts that fold INTO an existing candidate as a phase
· open hypotheses verbatim (file:line) · orphan files (no design) · 3 citations that prove each claim.
No judgement on architecture. No rewriting of sources. Absolute paths only.
```

## prompt-2 — delta (after majkee's slug-map ack)

```text
Repo /home/hruzam/unikuklatrix/nablarva. Execute exactly:
1 git mv meshup/<every top-level entry except repomix.meshup.md> raw.nablarva/<same name>
2 git mv brief.triangulation.2026-07-31.md raw.nablarva/oraculum-basic-triangulation/
3 git rm meshup/repomix.meshup.md
4 write raw.nablarva/README.md: the prefix rule (one paragraph) + inventory `find raw.nablarva -type f | sort`
5 create meshup/<slug>/ per /home/hruzam/unikuklatrix/nablarva/.dev/session/cleanup-00-meshup/raw/slugmap.md with empty DESIGN.md + HYPOTHESES.md
6 replace AGENTS.md L56–65, README.md L26–32, docs/ARCHITECTURE.md L5+L10 with the one-line redirect given in slugmap.md §pointer
7 report: git status --short; git diff --cached -M --stat (renames must be 100 %); no commit.
Touch nothing else. No commit, no push.
```

## prompt-3 — cartan (loop 2 · audit)

```text
Resident in /home/hruzam/unikuklatrix/nablarva. Read .dev/session/cleanup-00-meshup/RUNBOOK.md,
STATUS.md, _bus/01.oraculum.point.md. Audit, read-only, four claims of the gate: (1) every former
meshup path resolves by prefix rule — compare git diff -M --name-status against raw.nablarva/README.md
inventory, zero content edits; (2) REGISTRY.md covers every source or names it orphan — count both
sides; (3) each slug has DESIGN.md + HYPOTHESES.md, DESIGN cites rather than copies; (4) the three
pointer files carry only the redirect line and no other diff. Welcome: independent research on any
HYPOTHESES.md entry, written as .dev/session/cleanup-00-meshup/raw/research.cartan.<topic>.md and
cited in the audit. Return _bus/01.cartan.return.md: PASS/FAIL per claim · evidence · one line on the
grouping's rightness. Write nothing else; no git mutation.
```

## Known constraints + destructive holds

- No seat commits or pushes. majkee commits after GO. The `git mv` runs only after majkee's slug-map
  ack recorded in STATUS `checkpoint:`.
- Do not read `.hlm/` or `.dev/session/skill-report-test/` (inherited hold, session 03).
- `flag.md`, `pulse.md` rows of other sessions, `.dev/session/*` history: untouched.
- `GEMINI.md`, `registry.nablarva.beacon.md`: out of scope.
- `.dev/session/nablarva-01-design/` preservation + prune (pulse L12) is a separate task — not here.
- Cartan's instrument is `resident`; it does not change inside this RUNBOOK.

## Acceptance evidence

- `git diff --cached -M --name-status` shows `R100` for every former meshup file; `A` only for
  `raw.nablarva/README.md`, `meshup/REGISTRY.md`, `meshup/*/DESIGN.md`, `meshup/*/HYPOTHESES.md`;
  `D` only for `repomix.meshup.md`; `M` only for the three pointer files.
- `_bus/01.cartan.return.md` with four PASS lines. majkee's GO in STATUS.

## References

- `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X0-restarted/README.md` §pulse-2 — the intention
- `/home/hruzam/unikuklatrix/nablarva/AGENTS.md` — read order, naming law, append-only pen rule
- `/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md` — locks; cites old paths, resolved by prefix rule
- `/home/hruzam/reposoma/raw.guides/runbook/GUIDE.md` · `status/GUIDE.md` · `bus/GUIDE.md` — shape law
- `/home/hruzam/reposoma/raw.guides/gloss/GUIDE.md` — if a GLOSS.cleanup.md is asked for

## What this session deliberately does not do

- Plan or decide architecture; re-litigate S1–S8; run any study; change any lock.
- Rewrite old citations across `.dev/session/*` or `flag.md`.
- Promote anything to `~/ia-sync/`.
