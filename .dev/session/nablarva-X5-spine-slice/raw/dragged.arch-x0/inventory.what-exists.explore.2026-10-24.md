# inventory.what-exists — code vs document vs name, along observe → record → view (lens 4)

`collected: 2026-10-24 by an Explore subagent (read-only, no Write; report relayed verbatim by oraculum(arch-X0)) · scope: ~/unikuklatrix/nablarva (core) and ~/ia-sync (main) · nothing modified, staged or run · vaults .hlm/ .majkee/ not read · tags: CODE-RUNS (executable with usage text or tests) · CODE-DRAFT · DOC-PLAN · DOC-CONTRACT · NAME-ONLY · facts only; interpretation belongs to the synthesis`

## 1. ovitmugen (~/ia-sync, own repo)
| path | exists | type | lines | last commit | header line | tag |
|---|---|---|---|---|---|---|
| zsh/session/ovitmugen.py | y | Python, executable, 49479 B | 1089 | b435af5 2026-10-02 | "ovitmugen — tmux manager of the session layer (layout C: frame + agents)" | CODE-RUNS |
| zsh/session/ovitmugen.zsh | y | zsh, executable, 1676 B | 30 | 0b95adf 2026-09-25 | "ovitmugen engine (tmux manager: frame + agents, layout C)" | CODE-RUNS |
| zsh/session/ovitmugen.tmux.conf | y | tmux conf, 1539 B | 27 | d7d35e0 2026-09-29 | "FRAME server only (tmux -L ovitmugen -f <this file>)" | CODE-RUNS (config) |
| zsh/session/ovitmugen.presets.json | y | JSON, 498 B | 5 | 0b95adf 2026-09-25 | presets for `ov-up <slug> @<key>` (csharp, web) | CODE-RUNS (data) |
| zsh/session/runbook.py | y | Python, 103792 B | 2587 | 515eac5 2026-09-29 | runbook TUI backend for the rb-* commands | CODE-RUNS |
| zsh/session/keyboard.zsh | y | zsh, 3901 B | 56 | f2304d9 2026-10-08 | alias table for the rb-*, cs-* and ov-* commands | CODE-RUNS |
| zsh/session/runbook.zsh, board.zsh | y | zsh | n/c | n/c | `_rb_*` functions | CODE-RUNS |

The deployed copy is present at ~/.config/zsh/session/ovitmugen.py. Line counts and commits for runbook.zsh and board.zsh were not collected.

- **ov-* commands** (aliases in keyboard.zsh:36-41, functions in ovitmugen.zsh:25-30, argparse subcommands in ovitmugen.py:1041-1082): `ov-up`, `ov-tab`, `ov-ls`, `ov-down`, `ov-console`, `ov-selftest`.
- **rb-* commands** (keyboard.zsh:17-32): `rb-open`, `rb-pick`, `rb-help`, `rb-mark`, `rb-unmark`, `rb-board`, `rb-selftest`, `rb-keys`. The functions are `_rb_open`, `_rb_pick`, `_rb_help` in runbook.zsh and `_rb_mark`, `_rb_unmark`, `_rb_board` in board.zsh.
- **Selftests, named only and not run:**
  - `ov-selftest` runs `ovitmugen.py selftest` (py:788, "isolated servers, PASS/FAIL, zero side effects").
  - `rb-selftest` runs `python3 ~/.config/zsh/session/runbook.py selftest`.
- **Other files mentioning these commands:** zsh/AGENTS.md, zsh/session/help/commands/HELP.md, zsh/session/help/ovitmugen/HELP.md, zsh/session/help/board/HELP.md.
- ovitmugen.py contains no `pipe-pane`, `capture-pane` or `pane_tty`.

## 2. termpanum (nablarva)
- **toolbox/termpanum/** does not exist. toolbox/ contains only `termbrana/`.

**.dev/session/termpanum-X0-source-contract/** (committed at 78ff8b2 2026-10-23; only STATUS.md is modified)
| file | bytes |
|---|---|
| RUNBOOK.md | 6661 |
| STATUS.md | 3189 (41 lines) |
| raw/source-contract.md | 13149 |
| raw/research-disposition.md | 9813 |
| raw/entry.cartan.2026-10-22.json | 8998 |
| raw/review.packet.2026-10-22.md | 6888 |
| raw/review.packet.r2.2026-10-22.md | 5542 |
| raw/review.closure.2026-10-22.md | 5051 |
| raw/closure.manifest.cartan.2026-10-22.md | 2681 |
| raw/experience-transfer.cartan.2026-10-22.md | 2345 |
| raw/decision.majkee.packet-acceptance.2026-10-22.md | 1716 |
| _bus/ | 18 files, 01-06, each a cartan.point, implementer/verifier.return and cartan.verdict, 1.7–4.2 KB |

**.dev/session/toolbox-termpanum-00-brief/**: only raw/brief-substrate-for-RUNBOOK.termpanum.2026-10-01.md (11055 B).

**.dev/session/nablarva-X2-builder-narative/raw/**
| file | bytes | lines | git |
|---|---|---|---|
| termpanum.build-plan.md | 31999 | 120 | UNTRACKED |
| termpanum.baseline-and-research.md | 31344 | 160 | UNTRACKED |
| hello* | none | – | – |
| question.release-and-vist-boundary.cartan.2026-10-22.md | 2775 | – | UNTRACKED |
| question.tmux-source-fidelity.cartan.2026-10-22.md | 1794 | – | UNTRACKED |
| qualification* | none | – | – |

There is also review.termpanum-build-plan.2026-10-22.md (7845 B, UNTRACKED).

Tags: build-plan is DOC-PLAN, and X0 is DOC-CONTRACT (STATUS says "CLOSED … no runtime work opened").

**termpanum.build-plan.md, first 30 lines (summary; quote of the key line):**
- Line 1: "# Termpanum build plan and first assignment".
- Line 3: "2026-10-22 · Astrobley / Codex · cycle 02 · candidate for independent review and Majkee GO".
- Line 5, verbatim: "No fixture ran, successor bed was opened, code was built, architecture locked or execution release obtained by this plan."
- §1 lists five binding constraints: preparation is not release; the synthetic fixture needs a separate release (D4 verdict or an explicit Majkee exception); reports do not perform admission; comparisons stay independently inspectable; consequential holds stay with their packages.
- §2, scenario S1: a synthetic process in a private tmux pane. The first successor is documentary prep. Package Q is the first runnable observation slice; package L is a later htop-like view.
- Table: the proposed first choice is lab capture/replay/compare plus a prospective `pipe-pane -O` source. `capture-pane` and control mode are later alternatives.

**X0 STATUS.md, first 30 lines (summary):**
- updated "2026-10-23 23:34 CEST"; writer "Cartan · Codex"; observed HEAD 78ff8b2.
- gate: Majkee accepts the documentary packet as input for `relay-00-research`.
- checkpoint: "CLOSED, original gate MET … Accepted packet remains byte-identical; all 29 pre-maintenance files match existing commit 78ff8b2".
- in_flight: "none — original work complete … no runtime work opened".
- holds: "X2 approved evidence lacks a preservation commit".

**.dev/session/nablarva-X4-vist/raw/hello-01-contract.md** (361 lines, 78ff8b2 2026-10-23)
- Headings: What this is · The idea in one paragraph · Fit with what already exists · The bed · The mail file · nabla-send · nabla-read · nabla-bell · nabla-mail, the operator's command · The instruction block · Nabla mail (peer agents) · Per-CLI configuration · Token economy · Tests: fake seats first, then live · Out of scope for r0 · Work split for the evening · Prior art and fit · Open choices for Majkee.
- First 40 lines:
  - Line 3: "Contract draft r0 requested by Majkee · proposed, not implemented".
  - Two CLI seats (Claude Code and Codex) in tmux panes exchange one hello each, using only files, `nabla-send`, `nabla-read`, a `nabla-bell` watcher and tmux keystrokes.
  - No hooks, `claude -p`, MCP or tunnel ("decided").
  - Keystroke injection happens only inside the experiment bed.
- Tag: DOC-CONTRACT. No `nabla-send`, `nabla-bell` or `nabla-read` code exists in either repo; the only `nabla-*` filename is under raw.nablarva/ and is unrelated.

**hello-02-addendum-r1.md** (202 lines, 78ff8b2)
- Headings: .nablarva next to .germline · The layering · The tree · How a session binds · The session log · What r1 changes in r0 · New tests · Open choices added by r1.
- Tag: DOC-CONTRACT.

## 3. Capture/collector code
- **nablarva** (excluding .git, raw.nablarva, .hlm, .majkee): 33 files contain `pipe-pane`, `capture-pane`, `pane_tty`, `script -f` or `asciinema`. All 33 are `.md`; there are zero code hits. The 40 hits are file:line in:
  - .dev/research/termpanum-events/events-map.v0.2026-10-02.md:21,50,92
  - .dev/research/pty-community/pty-observation.prior-art.2026-10-02.md:12,13,20,34,57,71,80,82,91,92,95,106,115,116
  - .dev/observations/nablarva-X0-restarted.trajectory.2026-10-05.md:25
  - .dev/session/dock.md:23,53
  - .dev/session/composer-01-parse/evidence/research.ovitmugen-layer.2026-10-20.md:25
  - .dev/session/nablarva-X4-vist/raw/catalogue.hello-intake.cartan.2026-10-23.md:43
  - .dev/session/termpanum-X0-source-contract/raw/research-disposition.md:65,99
  - .dev/session/skill-report-test/raw.synth.phase1.6378.md:14
  - .dev/session/nablarva-X2-builder-narative/raw/brief.rosters-and-team.2026-10-22.md:120
  - .dev/session/nablarva-X2-builder-narative/raw/question.tmux-source-fidelity.cartan.2026-10-22.md:7,18
  - .dev/session/nablarva-X2-builder-narative/RUNBOOK.md:226
  - .dev/session/nablarva-X2-builder-narative/raw/termpanum.baseline-and-research.md:53,54,56,129
  - .dev/session/nablarva-X2-builder-narative/_bus/01.astrobley.return.md:90
  - .dev/session/muticula-01-qualify/raw/plan.step0.2026-09-29.reviewed-3b83620b.md:190
  - .dev/session/nablarva-X4-vist/raw/vist-01-principle-and-applications.md:121,129,207
  - .dev/session/nablarva-X2-builder-narative/raw/termpanum.build-plan.md:29,30
- **~/ia-sync code** (*.py, *.zsh, *.sh), the only code hits:
  - zsh/experimental/reincarnation-session.sh:3,24,25,26. Bash, 34 lines, 0427e10 2026-09-22. Header: "tmux bed: claude-0, claude-1, codex-0 — Adds a raw pipe-pane transcript per window". Lines 24-26 run `tmux pipe-pane -t "$SESSION:<win>" -o "cat >> '$LOGDIR/<win>.raw.log'"`. Tag: CODE-DRAFT (experimental, no tests).
  - zsh/experimental/base.zsh:43 is only a comment describing that script.

## 4. termbrana
**~/ia-sync/zsh/termbrana/** (last commit e290aee 2026-10-22)
| file | bytes | lines |
|---|---|---|
| composer.py | 13884 | 386 |
| composer.zsh | 372 | 8 |
| base.zsh | 233 | 5 |
| keyboard.zsh | 186 | 4 |
| GRAMMAR.md | 21311 | 377 |
| README.md | 6058 | 113 |
| tests/test_composer.py | 20647 | – |
| tests/test_startup.py | 4775 | – |
| tests/acceptance.py | 9540 | – |
| tests/benchmark.py | 3316 | – |

- composer.py header: "Termbrana request/0.1: inert bytes-in parser. Wire contract: GRAMMAR.md." composer.zsh defines `_tbc_python`, `_tbc_check`, `_tbc_parse`.
- Tests named in README:94-96, not run: `python3 -B -m unittest discover -s tests -v`, `tests/acceptance.py --bed … --out …`, `tests/benchmark.py …`.
- Tag: CODE-RUNS. It is a parser for composition packets, not a capture tool.

**toolbox/termbrana/** (last commit 32bd6f4 2026-10-22)
- Top level: Cargo.toml (9 lines), Cargo.lock, README.md (239 lines), DECISIONS.md (178 lines), .gitignore (`/target`), crates/, research/, target/.
- Code: crates/termbrana-zellij/src/main.rs (259 lines), plus research/foil_plugin.rs (289 lines). research/ also holds 14 md/log evidence files: t01-t06, the API surface for zellij 0.44.3, and zellij-session.log.
- README: "Status — pre-product, Milestone 0 truth spike … a compiling Zellij 0.44.3 probe harness, not an installable semantic-navigation MVP".
- Built .wasm on disk, untracked because target/ is gitignored:
  - target/wasm32-wasip1/release/termbrana-zellij.wasm (1577266 B, 2026-09-02 01:38)
  - deps/termbrana_zellij-42a7d3e2db5d9ed7.wasm
- `git ls-files` shows no tracked wasm.
- Tag: CODE-DRAFT (probe harness with a build artifact; no `#[test]` found in the sources).

## 5. events
- .dev/research/termpanum-events/ contains only events-map.v0.2026-10-02.md (11737 B, 97 lines, 3eb57a9 2026-10-02).
- First 25 lines (summary): frontmatter says "EVENTS map — the shared event vocabulary for session observation", version v0.3, "status: DRAFT for docket 8 … v1 after first fixture run". Vendors: Claude Code and Codex are first-class; Gemini and agy are second-level; `jev` is a model role. Rule: "an event earns a slot only if at least one real source emits it today". Title: "EVENTS map v0.3 — 20 events, 4 states". Event shape: `ts · session_id · event · phase? · source · certainty · grade? · anchor · payload`. Sources: hook, record, mux, pty, proc, kernel. "events are append-only facts; state is derived, never stored".
- Tag: DOC-PLAN.

## 6. muticula
- .dev/session/muticula-01-qualify/ (last commit f461b20 2026-10-02):
  - RUNBOOK.md (8123 B), STATUS.md (4859 B, 62 lines).
  - _bus/: 5 files — 01 and 02 cartan-muticula.verdict; 01, 02 and 03 trajectory-dashboard.point.
  - raw/: muticula.master.2026-09-26.md (38177), manifest.step0.claude.2026-10-02.md (20825), plan.step0.2026-09-29.md (21302), two reviewed plan copies (9930 and 16589), plan.step0.codex-lane (15800).
- STATUS first 20 lines (summary): updated 2026-10-02, writer "trajectory · anthropic". Gate: Majkee records GO or STOP on a witnessed step-0 package. That package would prove which raw git routes the native permission rules deny for Claude Code and Codex, show that a stub `muticula` command stays allowed, and check whether MUTICULA_ID/MUTICULA_KEY reach tools. Checkpoint: opened 2026-09-27; the r3 brief was copied byte-identically from adce981.
- Code: zero `muticula` hits in *.zsh, *.sh or *.py in either repo. The one non-.md hit is the JSON manifest .dev/session/nablarva-X2-builder-narative/raw/p0.tracked-preservation.cartan.2026-10-22.json.
- Tag: DOC-PLAN.

## 7. stridulatrix / broker
- 29 files in nablarva mention it and 0 in ~/ia-sync. All 29 are `.md` (docs) and none are code. Main locations:
  - Top level: PROJECT-DESIGN.md (§3.7 "stridulatrix (broker + CLI)"), AGENTS.md, docs/ARCHITECTURE.md, docs/organs/stridularium.md.
  - .dev/session: flag.md, GLOSS.nablarva.md, plus composer-01-parse, X2, X4, toolbox-termpanum and events-map docs.
  - meshup/: REGISTRY.md and the stridularium.mobile-console, lab.observability-probes, seam.cross-vendor-relay and room.brokered-journal DESIGN/HYPOTHESES files.
- No file or directory is named `*stridul*` other than the stridularium docs and meshup dir.
- Tag: NAME-ONLY (in design docs).

## 8. PROJECT.yaml (24 lines, 22cfa26 2026-10-17), verbatim
```yaml
# PROJECT.yaml v1 — GAVELED founding set 2026-08-02 (majkee); docket items stay pending
name: nablarva              # operational repo/dir name (lowercase disk contract)
official-name: nabLarva     # the animal — ∇larva (nabla larva), brand-car larva V3.
                            # Public naming avoids the t-word (larvaTnux 'n' rule).
                            # Claim no public namespace before majkee clears it.
stack: { lang: TBD, framework: none }   # v1 language = gavel docket item 2 (python-stdlib
                                        # vs C++ learning path) — do NOT assume before gavel
commands:                   # docs-only phase; verbs land when docket item 2 gavels
  test:  "TBD"
  lint:  "TBD"
  build: "none (strategy + substrate docs)"
  run:   "none yet"
docs:
  architecture: docs/ARCHITECTURE.md
  project-design: PROJECT-DESIGN.md # maintained working wrapper; draft, not canon
  project-design-maintainer: .germline/agents/houston/nablarva.md # Houston audit method; vendor bindings global at ~/.germline/agents/houston/
  decisions:    .dev/session/flag.md
agents: [ architect, challenger, researcher, implementer ]   # four base seats; domain seats earned
mcp_profile: none           # placeholder — Model-C sizing deferred (onboarding-kit O1)
# tools: none yet. First organs (stridularium naming = docket item 7) arrive as
# experimental builds under the naming law in AGENTS.md, each carrying a provenance
# header (name · status · schema · source · trust note) before it lands.
guidelines_channel: stable
# purpose · laws · ownership · constraints → .dev/session/flag.md
```

## 9. docs/organs and PROJECT-DESIGN
- docs/organs/ contains only stridularium.md (3115 B, 51 lines, 22cfa26 2026-10-17).
- PROJECT-DESIGN.md is 309 lines, last commit 3b4278c 2026-10-24. Headings:
  - Document role
  - 1. what is it / 1.1 nablarva
  - 2.process / 2.1 planning phase / 2.2 Architecture work
  - VOLATILE
  - 3. APP parts:
    - 3.1 termbrana
    - 3.2 ovitmugen (tool), with sub-headings "function ADD", "function create", "another managing options", "3.1.1 demanded tree" and "3.2.x @Trajectory notes"
    - 3.3 instarmux (tool)
    - 3.4 reposoma (tool)
    - 3.5 muticula (tool)
    - 3.6 termpanum (toolbox)
    - 3.7 stridulatrix (broker + CLI)
    - 3.8 stridularium (phone app)
  - KEYS CODE

## 10. git status (nablarva, core) — another head's files; reported, never staged
- `git status --short | wc -l` gives 43.
- **X2 (.dev/session/nablarva-X2-builder-narative/)**
  - Modified: RUNBOOK.md, STATUS.md, raw/brief.rosters-and-team.2026-10-22.md.
  - Untracked: the whole `_bus/` directory, plus these raw/ files:
    - checks.cycle01.cartan.2026-10-22.json, checks.cycle03.cartan.2026-10-22.json
    - closure.manifest.cartan.2026-10-22.md
    - consult.release-and-vist-boundary.2026-10-22.md
    - decision.majkee.plan-go.2026-10-22.md
    - disposition.x3-vectors.cartan.2026-10-22.md
    - experience-transfer.cartan.2026-10-22.md
    - handoff.termpanum-X0-source-contract.cartan.2026-10-22.md
    - p0.entry.cartan.2026-10-22.json, p0.tracked-preservation.cartan.2026-10-22.json
    - question.release-and-vist-boundary.cartan.2026-10-22.md, question.tmux-source-fidelity.cartan.2026-10-22.md
    - research.tmux-source-fidelity.2026-10-22.md
    - review.p5-handoff.2026-10-22.md, review.termpanum-build-plan.2026-10-22.md
    - termpanum.baseline-and-research.md, termpanum.build-plan.md
- **X0 (.dev/session/termpanum-X0-source-contract/)**: modified STATUS.md only.
- With `--untracked-files=all`, these two directories account for 33 dirty entries.

## Summary
| item | tag | evidence |
|---|---|---|
| 1 ovitmugen (ov-*) | CODE-RUNS | ovitmugen.py 1089 lines, 6 subcommands, `ov-selftest` (b435af5 2026-10-02) |
| 1 runbook (rb-*) | CODE-RUNS | runbook.py 2587 lines, `rb-selftest` alias |
| 2 toolbox/termpanum | NAME-ONLY | directory does not exist |
| 2 termpanum build-plan / baseline | DOC-PLAN | untracked md; the plan states "no … code was built" |
| 2 termpanum X0 source contract | DOC-CONTRACT | STATUS "CLOSED … no runtime work opened" (78ff8b2) |
| 2 HELLO r0/r1 (nabla-send/bell/read) | DOC-CONTRACT | "proposed, not implemented"; no code found |
| 3 capture/collector | CODE-DRAFT (ia-sync only) | only reincarnation-session.sh (pipe-pane → raw.log, 34 lines, experimental); nablarva has 0 code hits |
| 4 termbrana composer (ia-sync) | CODE-RUNS | composer.py 386 lines plus 4 test files and a unittest command |
| 4 toolbox/termbrana observer | CODE-DRAFT | M0 Zellij probe: main.rs 259 lines, untracked built wasm 1.58 MB from 2026-09-02 |
| 5 events map | DOC-PLAN | v0.3 "DRAFT for docket 8" |
| 6 muticula | DOC-PLAN | qualify bed docs only; 0 code files |
| 7 stridulatrix | NAME-ONLY | 29 md files, 0 code |
| 8 PROJECT.yaml | DOC-CONTRACT | lang TBD; test/lint TBD; run "none yet" |
| 9 docs/organs / PROJECT-DESIGN | DOC-PLAN | one organ doc (stridularium); design §3.1–3.8 names the parts |
| 10 git status | – | 43 dirty entries; X2 mostly untracked, X0 only STATUS.md modified |
