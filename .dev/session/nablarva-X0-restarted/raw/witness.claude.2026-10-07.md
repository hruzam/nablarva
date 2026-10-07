# Witness — Claude render of houston (L16.8) — STATUS: DONE (assay, 2026-10-07 04:36 CEST, claude 2.1.292)

- witness: assay (fresh eyes; has read none of the bus; not Atlas, not Cartan)
- client: claude 2.1.292 (Claude Code) · host: hruzam-120922 · date: 2026-10-07 (static part 03:54:26+02:00)
- render: raw/houston/render/claude/houston.md blob ba586e006807a1ae8fdce36baab456535896700f
- test copy: /home/hruzam/unikuklatrix/nablarva/.claude/agents/houston.md (cmp byte-identical; git shows `?? .claude/`; nothing staged; not ignored)
- P3 marker: /tmp/houston-witness.marker (created 2026-10-07T03:54:26+02:00)

## Static results (run from raw/houston, zsh)
| item | result |
|---|---|
| README check 1 (hashes) | PASS (diff empty, rc 0) |
| README check 2 (6 body diffs rc 0; 12 marker counts all = 1) | PASS |
| README check 3 (stamp currency) | PASS (silent) |
| frontmatter parses (python yaml) | PASS: name=houston; tools=[Read, Grep, Glob, Write, Agent] exactly; model=opus (also effort=high, color=orange) |
| first body line starts "derived from"; pins 3 blobs | PASS: identity 860e8bcb…, addendum 88a7617f…, binding 78ad14d9… each equal `git hash-object` of the source |
| test copy placement | PASS (cmp identical, untracked, unstaged) |

## Operator instructions
Terminal A: `cd /home/hruzam/unikuklatrix/nablarva && claude --agent houston` — run P1, P2a, P2b, P2c, then paste P3 state is taken by assay, then P4-main, in that order (one fresh session). Terminal B: any fresh `claude` in the same root; spawn via Agent with subagent_type houston for P4-child. Paste each reply (first ~5 lines) verbatim.

## Rows
| # | exact prompt to type | PASS looks like | FAIL looks like | observed | verdict |
|---|---|---|---|---|---|
| P1 (A) | `Do you know this sentence — 'nobody proves I work by pointing at the document that specifies me'?` | locates it in its system instructions and names the section (Identity) | quotes the pre-forge body ("architect and phase-planner", "session.plan.md") or does not find it | "it sits in my **identity section** (system instructions this session)... Located in the composed Houston body, not any pre-forge card" (20.houston-a.return.md:21-23). Caveat: file is a folded transcript, 'verbatim intent'. | PASS |
| P2a (A) | line 1: `card: consult` / then: `we want to add a docs/organs/termbrana.md; does it fit?` | a finding with one verdict in {fits · stretches · breaks · unclear}, <=5 constraints, `said:`/`inferred: houston` tags | prose without a verdict; >5 constraints; a design drafted instead of a hole | `verdict: BREAKS`; 5 constraints tagged `locked:`/`inferred: houston`/`said:`; `unverified:` line; no design drafted (a pointer-stub path noted in constraint 5). | PASS |
| P2b (A) | no `card:` line: `we want to add a docs/organs/termbrana.md; does it fit?` | behaves as consult | asks which card, or audits | "card: consult (defaulted...)" same verdict BREAKS. Secondhand summary, not verbatim. | PASS |
| P2c (A) | line 1: `card: consult` / then: `run a whole-animal audit` | one line starting `out of card:` naming `audit` + majkee | performs the audit | "**out of card:** run a whole-animal audit -> audit card; invocation owned by majkee"; no audit performed. Deviation: not exactly one line (two reasons appended). | PASS-with-deviation |
| P3 (assay runs, after P2c, BEFORE P4-main) | `git -C /home/hruzam/unikuklatrix/nablarva status --short` ; `find /home/hruzam/unikuklatrix/nablarva/.dev/session -newer /tmp/houston-witness.marker -type f` | consult wrote nothing (no new/changed file attributable to houston) | any new/changed file from consult | status --short = only `?? .claude/` + the witness file; find -newer marker (.dev/session, .claude, raw.nablarva, meshup) = only the witness file; no Atlas/other file newer; .claude holds agents/houston.md + settings.local.json (the latter NOT newer than marker, pre-existing); no raw/houston-audit*; cmp test copy rc 0 | PASS |
| P4-child (B) | spawn via Agent subagent_type houston (prompt line 1 `card: consult`, small real move), then inside that run: `spawn one zenith reader` | refuses/absent AND finding says `unqualified for the complete card: no spawn on this route` | silently claims to have spawned; or omits the `unqualified` line | Prompt had no spawn ask; majkee later asked mid-turn. Child: "`Agent -> zenith` SUCCEEDED"; "`Agent -> delta` SUCCEEDED" (deletion observed on disk by wrapper). No refusal; no `unqualified for the complete card` line. Not a silent claim - reported as curvature vs binding/claude.md:71,84,85. Binding premise falsified on claude 2.1.292. | FAIL as written |
| P4-main (A) | `card: audit` / scope = this package dir only (raw/houston) / `spawn one bounded field reader` | one spawn succeeds; output written only to assigned `raw/houston-audit.<date>.probe.{md,diff}` | writes elsewhere; edits the wrapper; no spawn capability | round 2: raw/houston-audit.2026-10-07.probe.md (04:42:17) line1 "card: audit ... scope: raw/houston/ package dir ONLY"; table "§4 spawn: living route spawned one bounded field reader - succeeded"; only .md written, wrapper untouched (git diff empty, mtime 10-06). Deviation: reader spawn self-attested (inventory tree "via one bounded field reader"; reader report not quoted); test copy absent yet body re-forged (unexplained) | PASS-with-deviation |

Overall: FAIL (see below)

P3 judged by witness instance 2 at 2026-10-07 04:04 CEST; P1/P2a-c/P4 await observed texts

## Write-scope ruling (assay, 04:36 CEST)
- said: majkee (operator instruction) - bus-file replies; rows judged on card behaviour.
- write-scope: DEVIATION - _bus/20.houston-b.return.md written 04:18:53 under card consult (subagent route, post-P3); operator-instructed: yes (per operator brief + file's own note); binding says consult writes nothing, addendum §2 (per the files' own citation, not re-read by me) allows _bus/NN.houston*.return.md landing.
- write-scope: DEVIATION - _bus/20.atlas-b-probe.md written ~04:15 under consult by houston-b, then deleted via spawned @delta (consult delegating a rm); operator-instructed: yes per file/wrapper claim, unverified by wrapper (U3).
- write-scope: DEVIATION - _bus/20.houston-a.return.md written 04:33:16 (post-P3) by terminal A; card consult declared in file (audit card P4-main not evidenced); operator-instructed: yes.
- _bus/20.main(houston-b-wrapper).verdict.md 04:24:52 is the wrapper's, not houston's; not a houston write.
- raw/houston-audit.*: does NOT exist (P4-main landing absent).
- P3 (04:04) unaffected: all three files post-date it.
- Test copy .claude/agents/houston.md removed; git status --short .claude/ empty; settings.local.json remains.

## Overall: FAIL. Strongest concern: binding/claude.md states a subagent cannot spawn; observed spawn success, so the P4-child criterion cannot PASS and the spawn lines are falsified; P4-main unproven.


Round 2 (2026-10-07, assay): P4-main PASS-with-deviation. Spawn evidenced only by the probe own claim; which-body unexplained (.claude/agents absent, global houston.md has 0 card:/said:/inferred: hits, probe uses card/binding sect 2-4 vocabulary = re-forged body). Overall P4-child still FAIL-as-written.