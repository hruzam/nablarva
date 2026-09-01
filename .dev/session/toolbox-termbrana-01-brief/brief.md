# brief — toolbox-termbrana · session 01 (founding brief)

`name: termbrana · status: DRAFT — challenge FOLDED, awaiting majkee gavel`
`source: ~/.remote/harvest/ (Wave r0 2026-08-15: definition + execution-plan + addendum ·`
`nabla pair: foil_theory.md + foil_plugin.rs = research history) · author: Houston (office) 2026-08-15`
`challenge: @Mirror first (majkee rule) — relay graceful-fail, no verdict → @Janus fallback:`
`REVISE (narrow) — A2/A4/phase structure sound; two folds absorbed: A5 pre-registered benchmark`
`(stop-rule teeth) + A3 governance precedence. Folded below.`
`session law: flag L9 — this dir dies with the task; canon lands in flag/pulse + the toolbox repo.`

## 1 · Scope

**Termbrana** = independent semantic observation, navigation, and replay layer for terminal
sessions. Zellij-first: `termbrana-core` (pure Rust) + `termbrana-zellij` (WASM observer
plugin). Read-only MVP; append-only JSONL with explicit source grades; NablaRava = one
*optional* consumer via a later adapter. Success criterion (definition §10): user returns to a
meaningful terminal event faster and more reliably than raw scrollback search — visual novelty
alone is not success. Stop-rule carried from execution-plan §11 and given TEETH by A5 below:
the M2 verdict fires on a number pre-registered at founding, not on a feeling next to a
working plugin.

## 2 · Adoptions for gavel (A1–A5)

- **A1 — substrate adoption.** `termbrana.project-definition.md` + `termbrana.execution-plan.md`
  + `termbrana.addendum-to-foil-theory.md` adopted as the toolbox's founding canon;
  `foil_theory.md` + `foil_plugin.rs` preserved as research history (never promoted by rename).
  All five copied from `~/.remote/harvest/` (volatile surface) into `termbrana/research/` at
  repo creation, provenance headers attached (@Delta task). **Guard:** termbrana's Rust is
  forced by the Zellij WASM boundary — it does NOT pre-decide docket item 2 (nabLarva v1
  language).
- **A2 — placement + classification (aligned to `/new-project` skill · canon.project-topology,
  checked 2026-08-15 per majkee's direction).** Own repo `~/unikuklatrix/termbrana/` —
  scope-group sibling of nablarva; git + gh PRIVATE, branch `core`. **Termbrana is a TOOLBOX
  repo, NOT a temple project** — the anti-parallel-system reading:
  - reuses the skill's mechanics: scope-group placement (canon MANDATE satisfied —
    `~/unikuklatrix/`), `git init --initial-branch=core`, `gh repo create --private`,
    `temple-project-map.zsh` entry (fresh-read rule + ia-sync/reload activation gate);
  - takes NO harness of its own: no AGENTS/CLAUDE/flag/pulse in termbrana — nablarva's
    harness governs; all dev sessions in nablarva `.dev/session/toolbox-termbrana-NN-<slug>/`;
  - NO `.devenv` twin (majkee confirmed 2026-08-15 — "solve from central spot"): a pure
    product repo has no gitignored harness, so there is nothing for a devenv to transport —
    the twin's *reason* is absent, canon intact, not violated;
  - NO own registry beacon: one `toolbox:` line appended to nablarva's beacon
    (`registry.nablarva.beacon.md`) pointing at the repo.
  Rationale for own-repo over subtree: standalone-first product law, own release lifecycle,
  Rust build churn out of the animal's git history, clean later promotion.
- **A3 — docs canon + governance precedence (Janus fold).** Technical documentation lives WITH
  the product: `termbrana/{README,ARCHITECTURE,DECISIONS}.md` + `docs/` + `research/evidence/`
  — all COMMITTED (product docs, not harness). Precedence, explicit:
  - **nablarva `flag.md` holds SOLE authority** over structural / topology / ownership /
    scope locks concerning termbrana;
  - **`termbrana/DECISIONS.md`** = append-only ADR ledger scoped STRICTLY to
    product-technical calls (view path, capture mechanism, JSONL schema, API pins);
  - every `DECISIONS.md` entry MUST cite the nablarva flag line or session brief that
    authorized its work — an entry with no citation is invalid;
  - enforcement without a harness: a one-line **Governance** section in the committed
    `termbrana/README.md` states the above (topology gives a sibling repo no nablarva
    context — the committed README closes that gap).
  Session dirs = process only, point-never-copy. Backtrack chain: nablarva flag line →
  session brief → `DECISIONS.md` → evidence file.
- **A4 — team topology.** Integration ownership = ONE seat (@Trajectory) per execution-plan §9.
  @Astrobley = bounded probe/implementation tasks (Codex composite, reports usage). @Delta =
  surgical; @Vector = mid-size specified code; @Field = melt probe corpora into evidence
  reports; @Eagle = orientation scout. **Challenge turn: @Mirror first, @Janus fallback**
  (exercised this session — see header). @Epoch before any version-sensitive pick. @Flight as
  branch-coding group only at ≥2 concurrent lanes (flag deferral threshold — M1 is the first
  candidate). Parallel agents never change shared domain types — propose through the owner or
  an ADR.
- **A5 — pre-registered M2 benchmark (Janus fold — the stop-rule's teeth).** Registered NOW,
  at founding, before any UI exists:
  - **Corpus:** 5 real saved sessions (mixed: agent runs + ordinary shell work), frozen as
    fixtures during M1;
  - **Tasks:** 15 pre-written "return to event X" retrieval tasks over that corpus (errors,
    approvals, specific tool runs, specific outputs);
  - **Axes:** median time-to-locate + success rate; termbrana vs native Zellij scrollback
    search / scrollback editor, same operator, same tasks;
  - **Bar:** median time-to-locate **≥30% lower** AND success rate **≥ native** — else the
    stop-rule FIRES: stop at M2, preserve probe + core work, no M3 hardening;
  - **Procedure:** run as an operator PAD at M2 acceptance; raw timings land in the pad;
    verdict distilled by a fresh-eyes seat (@Assay class), not by the builder and not
    mid-run by the operator.
  The bar may be re-gaveled only BEFORE M2 begins — never while the measured MVP is on screen.

## 3 · Phase plan (sessions on this toolbox)

| session | scope | gate |
|---|---|---|
| **01-brief** (this) | adoptions A1–A5 · @Epoch version calibration ✅ · PAD-01 authored ✅ · challenge folded ✅ | majkee gavels A1–A5 · PAD-01 run green (zellij + rust installed, versions LOCKED in `evidence.host-versions.md`) |
| **02-m0-truthspike** | execution-plan §12 verbatim: smallest compiling plugin on the pinned host + the five M0 probes (T0.1–T0.5) · repo bootstrap (A2 mechanics) + harvest copy-in | M0 deliverables: compiling plugin + build instructions + 5 probe reports + `pane-content-matrix.md` + view/capture ADR → **host contract FROZEN** |
| **03-m1-core** | pure core (T1.1–T1.5), no host dependency · benchmark corpus frozen (A5) · parallel lanes open → @Flight branch group | all core tests green under ordinary host tests, no Zellij/WASM · corpus + 15 tasks on disk |
| **04-m2-mvp** | read-only Zellij MVP (T2.1–T2.5) | M2 acceptance 1–6 (incl. "NablaRava completely absent") **+ A5 benchmark pad: bar met or stop-rule fires** |
| **05-m3-hardening** | beta hardening list — only if A5 bar met | beta release gate (no swallowed input · no writes · deterministic replay · grades preserved · lifecycle recovery · resource docs · clean install/uninstall) |
| later | M4 nablarava adapter — only after the nablarva boundary contract exists (docket-dependent) · M5 PTY experiment — parked behind its ADR | per execution plan |

Authority order (execution-plan §1): current definition/decisions → probe evidence → compiling
code+tests → foil history → agent recollection. No parallel work before M0 freezes the contract.

## 4 · PAD-01 — host bring-up (operator) ✅ AUTHORED

`pad.1-host-bringup.md` in this dir. Pins from `research.epoch.host-versions.2026-08-15.md`
(@Epoch, live-verified): zellij **0.44.3** (Arch extra, in sync) · rustc **1.95.0** via rustup
(matches Zellij CI) · target **wasm32-wasip1** (`wasm32-wasi` REMOVED since rustc 1.84) ·
crate pin at M0: `zellij-tile = 0.44.3`. NOT an install-pkgs recipe (majkee ruling: pkgs =
finalized own-produced bricks only). Home bring-up = later pad if ever needed.

## 5 · Open to majkee

1. **Gavel A1–A5** (challenge folded — ready).
2. ~~Confirm no devenv twin~~ — CONFIRMED 2026-08-15 ("solve from central spot").
3. PAD-01 sitting: this session or next?
4. A5 numbers (5 sessions / 15 tasks / ≥30% / ≥ native success): confirm or re-set — yours to
   tune, but only NOW, never at M2.

## parked

- Epoch open item: exact plugin-API symbol diff 0.44.0→0.44.3 (PaneRenderReportWithAnsi,
  permissions) — belongs to M0 T0.2, not to this brief.
- @Mirror relay graceful-fail on first live outing — worth one maintenance look at the
  codex-line relay plumbing (temple lane, not this project).
