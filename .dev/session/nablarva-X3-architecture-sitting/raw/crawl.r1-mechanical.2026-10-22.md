crawl: r1-mechanical · writer: eagle · for: oraculum(cSharp) X3 · run at: 2026-10-22 06:50:18 CEST

## 1a

```zsh
git -C /home/hruzam/unikuklatrix/nablarva rev-parse HEAD
```

```text
32bd6f4b8a2be8ab65d2b5bd523f8e8f8c08956d
```

## 1b

```zsh
git -C /home/hruzam/unikuklatrix/nablarva hash-object PROJECT-DESIGN.md
```

```text
74e94d5519be6a2de1565ad686ab16cdff6c64c2
```

## 1c

```zsh
sha256sum /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md
```

```text
6ee10aa1c40a853cc6c1e6ff5dfa191999f38314058064b5543ac1392fe2c78f  /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md
```

## 1d

```zsh
git -C /home/hruzam/unikuklatrix/nablarva status --short
```

```text
 M .dev/session/composer-01-parse/RUNBOOK.md
 M .dev/session/composer-01-parse/STATUS.md
 M .dev/session/nablarva-X2-builder-narative/RUNBOOK.md
 M .dev/session/nablarva-X2-builder-narative/STATUS.md
 M .dev/session/nablarva-X2-builder-narative/raw/brief.rosters-and-team.2026-10-22.md
 M .dev/session/nablarva-X3-architecture-sitting/RUNBOOK.md
 M .dev/session/nablarva-X3-architecture-sitting/STATUS.md
?? .dev/session/composer-01-parse/_bus/11.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/12.builder.return.md
?? .dev/session/composer-01-parse/_bus/12.cartan.point.md
?? .dev/session/composer-01-parse/_bus/12.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/13.cartan.point.md
?? .dev/session/composer-01-parse/_bus/13.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/14.builder.return.md
?? .dev/session/composer-01-parse/_bus/14.cartan.point.md
?? .dev/session/composer-01-parse/_bus/14.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/15.cartan.point.md
?? .dev/session/composer-01-parse/_bus/15.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/16.builder.return.md
?? .dev/session/composer-01-parse/_bus/16.cartan.point.md
?? .dev/session/composer-01-parse/_bus/16.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/17.cartan.point.md
?? .dev/session/composer-01-parse/_bus/17.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/18.cartan.point.md
?? .dev/session/composer-01-parse/_bus/18.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/19.builder.return.md
?? .dev/session/composer-01-parse/_bus/19.cartan.point.md
?? .dev/session/composer-01-parse/_bus/19.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/20.cartan.point.md
?? .dev/session/composer-01-parse/_bus/20.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/21.cartan.point.md
?? .dev/session/composer-01-parse/_bus/21.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/22.cartan.point.md
?? .dev/session/composer-01-parse/_bus/22.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/23.builder.return.md
?? .dev/session/composer-01-parse/_bus/23.cartan.point.md
?? .dev/session/composer-01-parse/_bus/23.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/24.builder.return.md
?? .dev/session/composer-01-parse/_bus/24.cartan.point.md
?? .dev/session/composer-01-parse/_bus/24.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/25.builder.return.md
?? .dev/session/composer-01-parse/_bus/25.cartan.point.md
?? .dev/session/composer-01-parse/_bus/25.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/26.cartan.point.md
?? .dev/session/composer-01-parse/_bus/26.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/27.builder.return.md
?? .dev/session/composer-01-parse/_bus/27.cartan.point.md
?? .dev/session/composer-01-parse/_bus/27.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/28.cartan.point.md
?? .dev/session/composer-01-parse/_bus/28.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/28.luna.return.md
?? .dev/session/composer-01-parse/_bus/29.builder.return.md
?? .dev/session/composer-01-parse/_bus/29.cartan.point.md
?? .dev/session/composer-01-parse/_bus/29.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/30.builder.return.md
?? .dev/session/composer-01-parse/_bus/30.cartan.point.md
?? .dev/session/composer-01-parse/_bus/30.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/31.cartan.point.md
?? .dev/session/composer-01-parse/_bus/31.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/32.cartan.point.md
?? .dev/session/composer-01-parse/_bus/32.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/33.builder.return.md
?? .dev/session/composer-01-parse/_bus/33.cartan.point.md
?? .dev/session/composer-01-parse/_bus/33.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/34.cartan.point.md
?? .dev/session/composer-01-parse/_bus/34.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/35.cartan.point.md
?? .dev/session/composer-01-parse/_bus/35.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/36.builder.return.md
?? .dev/session/composer-01-parse/_bus/36.cartan.point.md
?? .dev/session/composer-01-parse/_bus/36.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/37.builder.return.md
?? .dev/session/composer-01-parse/_bus/37.cartan.point.md
?? .dev/session/composer-01-parse/_bus/37.cartan.verdict.md
?? .dev/session/composer-01-parse/_bus/38.builder.return.md
?? .dev/session/composer-01-parse/_bus/38.cartan.point.md
?? .dev/session/composer-01-parse/_bus/38.cartan.verdict.md
?? .dev/session/composer-01-parse/evidence/audit.houston.termbrana-shape.2026-10-21.diff
?? .dev/session/composer-01-parse/evidence/audit.houston.termbrana-shape.2026-10-21.md
?? .dev/session/composer-01-parse/evidence/baseline.phase0-go.2026-10-20.json
?? .dev/session/composer-01-parse/evidence/brief.germline-contract-testing.md
?? .dev/session/composer-01-parse/evidence/brief.sella-germline-audit.2026-10-19.md
?? .dev/session/composer-01-parse/evidence/challenge.janus.2026-10-19.md
?? .dev/session/composer-01-parse/evidence/challenge.janus.home-stack.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/challenge.native-resolve-r2.2026-10-21.md
?? .dev/session/composer-01-parse/evidence/challenge.native-resolve.2026-10-21.md
?? .dev/session/composer-01-parse/evidence/challenge.native-v3.2026-10-19.md
?? .dev/session/composer-01-parse/evidence/challenge.native-v4.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/challenge.termbrana.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/cleanup.termbrana.2026-10-21/
?? .dev/session/composer-01-parse/evidence/consult.houston.layering.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/consult.houston.resolve.2026-10-21.md
?? .dev/session/composer-01-parse/evidence/consult.houston.termbrana.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/correction.phase0/
?? .dev/session/composer-01-parse/evidence/decision-options.home-verifier.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/decision.majkee.c1.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/decision.majkee.phase0-go.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/direction.majkee.termbrana-generation-x.2026-10-21.md
?? .dev/session/composer-01-parse/evidence/direction.majkee.termbrana.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/experience-transfer.cartan.2026-10-21.md
?? .dev/session/composer-01-parse/evidence/fixtures/
?? .dev/session/composer-01-parse/evidence/grammar.builder.v3.md
?? .dev/session/composer-01-parse/evidence/grammar.builder.v3.sha256
?? .dev/session/composer-01-parse/evidence/grammar.builder.v4.md
?? .dev/session/composer-01-parse/evidence/grammar.builder.v4.sha256
?? .dev/session/composer-01-parse/evidence/handoff.termbrana-generation-x.2026-10-21.md
?? .dev/session/composer-01-parse/evidence/head.audit-checks.termbrana.2026-10-21.json
?? .dev/session/composer-01-parse/evidence/head.cleanup-checks.termbrana.2026-10-21.json
?? .dev/session/composer-01-parse/evidence/head.final-checks.phase0.json
?? .dev/session/composer-01-parse/evidence/head.output-failure.source-check.json
?? .dev/session/composer-01-parse/evidence/head.pre-return-checks.phase0.md
?? .dev/session/composer-01-parse/evidence/head.startup-diagnostic.phase0.json
?? .dev/session/composer-01-parse/evidence/head.startup-flags.phase0.json
?? .dev/session/composer-01-parse/evidence/implementation.phase0/
?? .dev/session/composer-01-parse/evidence/next-phase.resolve/
?? .dev/session/composer-01-parse/evidence/phase0.exit.cartan.2026-10-21.md
?? .dev/session/composer-01-parse/evidence/point.flight.c1.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/point.flight.c1.after-direction.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/preparation.handoff.cartan.2026-10-21.md
?? .dev/session/composer-01-parse/evidence/presence-detach.cartan.2026-10-21.json
?? .dev/session/composer-01-parse/evidence/preservation.cleanup.reconciliation.cartan.2026-10-21.json
?? .dev/session/composer-01-parse/evidence/preservation.phase0.cleanup/
?? .dev/session/composer-01-parse/evidence/prompt.janus.home-stack.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/publication.phase0/
?? .dev/session/composer-01-parse/evidence/publication.reconciliation.cartan.2026-10-21.json
?? .dev/session/composer-01-parse/evidence/report.to-myshell.cleanup.2026-10-21.md
?? .dev/session/composer-01-parse/evidence/research.ovitmugen-layer.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/response.flight.c1.2026-10-20.sha256
?? .dev/session/composer-01-parse/evidence/review-packet.janus.home-stack.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/review-packet.janus.home-stack.2026-10-20.sha256
?? .dev/session/composer-01-parse/evidence/review.janus-layering.2026-10-20.sha256
?? .dev/session/composer-01-parse/evidence/reviewed-project-design.pre-go.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/reviewed-readme.termbrana.pre-go.2026-10-20.md
?? .dev/session/composer-01-parse/evidence/source-copy.correction.phase0.json
?? .dev/session/composer-01-parse/evidence/source-copy.phase0.json
?? .dev/session/composer-01-parse/evidence/source-copy.startup.phase0.json
?? .dev/session/composer-01-parse/evidence/startup.builder-v3.2026-10-19.md
?? .dev/session/composer-01-parse/evidence/startup.phase0/
?? .dev/session/composer-01-parse/evidence/verification.phase0/
?? .dev/session/nablarva-X2-builder-narative/_bus/
?? .dev/session/nablarva-X2-builder-narative/raw/handoff.composer-experience.cartan.2026-10-22.md
?? .dev/session/nablarva-X2-builder-narative/raw/p0.entry.cartan.2026-10-22.json
?? .dev/session/nablarva-X2-builder-narative/raw/p0.tracked-preservation.cartan.2026-10-22.json
?? .dev/session/nablarva-X2-builder-narative/raw/question.tmux-source-fidelity.cartan.2026-10-22.md
?? .dev/session/nablarva-X2-builder-narative/raw/research.tmux-source-fidelity.2026-10-22.md
?? .dev/session/nablarva-X2-builder-narative/raw/termpanum.baseline-and-research.md
?? .dev/session/nablarva-X3-architecture-sitting/raw/brief.preflight-and-operator-asks.2026-10-22.md
?? .dev/session/nablarva-X3-architecture-sitting/raw/crawl.r1-mechanical.2026-10-22.md
?? .dev/session/nablarva-X3-architecture-sitting/raw/handoff.composer-boundaries.cartan.2026-10-22.md
```

## 2

```zsh
git -C /home/hruzam/unikuklatrix/nablarva log --diff-filter=A --format='%H %cs %s' -- .dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md
```

```text
fe32a2951d11ca1004155b08090fabb6f5827fad 2026-10-07 X0 pruned to stub (preserved at d1c4b1e); X1 nablarva-X1-architecture opened: RUNBOOK + STATUS + router row; houston package, audit, witness, tunnel protocol moved into X1 raw/
```

## 3a

```zsh
git -C /home/hruzam/unikuklatrix/nablarva log --format='%h %cs %s' fe32a2951d11ca1004155b08090fabb6f5827fad..HEAD -- PROJECT-DESIGN.md AGENTS.PROJECT-DESIGN.md AGENTS.md PROJECT.yaml docs/ .dev/session/flag.md .dev/session/pulse.md .germline/ toolbox/termbrana/README.md toolbox/termbrana/DECISIONS.md
```

```text
32bd6f4 2026-10-22 2026-10-17 . nablarva-X1
39c61ec 2026-10-21 sitting bed renamed X4 -> X3 (majkee); deck complete (G1–G9 answered via polyp) + four bounded briefs; prompt: X3 path, L17, VIST substrate, briefs, full G9 delta, no-cage/no-manufacture line; RUNBOOK/STATUS reconciled; launch mode pending gavel; pulse + X1 pointer
fff20b8 2026-10-17 composer-01-parse: bus cycles 03–11, evidence packets (grammar v1/v2, Janus review, Houston consult, ia-sync ruling); flag L8′ composer publication via ia-sync (majkee 2026-10-17); AGENTS pointer; RUNBOOK/STATUS
b4fdb8f 2026-10-17 X4 bed opened (check 4, Houston sitting): RUNBOOK, STATUS, polyp gavel deck G1–G9 (leans confirmed by oraculum), sitting prompt, arc file; pulse route; X1 STATUS pointer
33613c4 2026-10-17 flag L14 D5: append-only 2026-10-17 pointer to docs/organs/stridularium.md (majkee approved); X1 STATUS: name sweep + wrapper to root done
22cfa26 2026-10-17 wrapper move: AGENTS.PROJECT-DESIGN.md -> /PROJECT-DESIGN.md, AGENTS.stridularium-design.md -> docs/organs/stridularium.md (majkee ruling 2026-10-10); live pointers, stubs, addendum stamp d9ee9067; X1 bus cycle 15 (cartan REVISE folded, assay PASS)
d1d443f 2026-10-17 2026-10-17 . nablarva architecture nablarva-X1
6f3204d 2026-10-13 2026-10-13 . houston finished
b57e199 2026-10-12 Houston final fold (majkee gavel 2026-10-10): project wrappers retired to X1 raw/archive.x0-renders (+ pre-fold sources); project bindings removed (now global in ~/.germline); addendum stamped + runtime-load; pointers in AGENTS.md, PROJECT.yaml, AGENTS.PROJECT-DESIGN.md repointed to ~/.germline
cdd1d09 2026-10-07 observations law gaveled: README + saddle line + X1 U16 flipped to gaveled/folded
936c58a 2026-10-07 saddle: .dev/observations/ named among session surfaces (one line); observations README: newcomer opener
31bd51e 2026-10-07 houston: migrate project-design keeper to canonical audit route
7562091 2026-10-07 X1 check 1: Houston promoted to gaveled homes (.germline/agents/houston/{nablarva,binding.claude,binding.codex}.md, .claude/agents/houston.md — bytes = third freeze); Atlas RETURN 01; POINT 02 keeper migration
```

## 3b

```zsh
git -C /home/hruzam/unikuklatrix/nablarva diff --stat fe32a2951d11ca1004155b08090fabb6f5827fad HEAD -- PROJECT-DESIGN.md AGENTS.PROJECT-DESIGN.md AGENTS.md PROJECT.yaml docs/ .dev/session/flag.md .dev/session/pulse.md .germline/ toolbox/termbrana/README.md toolbox/termbrana/DECISIONS.md
```

```text
 .dev/session/flag.md                 |  38 ++++
 .dev/session/pulse.md                |   4 +-
 .germline/agents/convergence.md      |   4 +-
 .germline/agents/houston/nablarva.md | 132 ++++++++++++++
 AGENTS.md                            |   9 +-
 PROJECT-DESIGN.md                    | 342 +++++++++++++++++++++++++++++++++++
 PROJECT.yaml                         |   4 +-
 docs/organs/stridularium.md          |  51 ++++++
 toolbox/termbrana/README.md          | 100 +++++++++-
 9 files changed, 667 insertions(+), 17 deletions(-)
```

## 4a

```zsh
git -C /home/hruzam/ia-sync log --format='%h %cs %s' --since=2026-10-07 -- germline/agents/houston claude/agents/houston.md codex/agents/houston.toml codex/profiles/houston.config.toml
```

```text
5e5cc3b 2026-10-21 houston: child may run card: sitting under explicit operator assignment (majkee gavel 2026-10-21)
946cdce 2026-10-17 germline-01: remove inert sandbox_mode from Codex houston child (witnessed ignored for spawned children, C-def.2 2026-10-17); binding.codex 0c812f6c records the card as the only write fence; child canary hc-9b3f0521; witness addendum P1 / C-def / C-def.2 / C-def.claude (majkee GO 2026-10-17)
bfeb2eb 2026-10-15 2026-10-15 . houston adjust
e3231c3 2026-10-14 germline: commit Houston runtime-load set already deployed (ISS.germline-deploy-before-commit)
1fc2044 2026-10-13 2026-10-13 . all about ia-sync
5bf1df2 2026-10-08 2026-10-08 . updates on cluade side + hooks
```

## 4b

```zsh
git -C /home/hruzam/ia-sync log --format='%h %cs %s' --since=2026-10-07 -- zsh/termbrana | head -40
```

```text
e290aee 2026-10-22 2026-10-22 . flight update . termbrana push
```

## 4c

```zsh
ls -la /home/hruzam/ia-sync/zsh/termbrana/
```

```text
total 72
drwxr-xr-x  3 hruzam hruzam  4096 20. říj 23.30 .
drwxr-xr-x 19 hruzam hruzam  4096 20. říj 23.31 ..
-rw-r--r--  1 hruzam hruzam   233 20. říj 23.23 base.zsh
-rw-r--r--  1 hruzam hruzam 13884 20. říj 23.42 composer.py
-rw-r--r--  1 hruzam hruzam   372 20. říj 23.53 composer.zsh
-rw-r--r--  1 hruzam hruzam 21311 20. říj 23.36 GRAMMAR.md
-rw-r--r--  1 hruzam hruzam   186 20. říj 23.23 keyboard.zsh
-rw-r--r--  1 hruzam hruzam  6058 20. říj 23.53 README.md
drwxr-xr-x  2 hruzam hruzam  4096 20. říj 23.53 tests
```

## 5

```zsh
grep -n '^#' /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md
```

```text
16:## Document role
31:# 1. what is it
36:## 1.1. nablarva *(itself)*
45:# 2.process
50:## 2.1. planning phase
56:## 2.2. Architecture work
95:# VOLATILE
118:# 3. APP parts
120:## 3.1. termbrana
143:## 3.2. ovitmugen *(tool)*
149:###### function ADD
152:## function create
155:## another managing options
160:### 3.1.1. demanded tree
178:### 3.2.x. @Trajectory notes — tips, observations, upgrade ideas *(append-only, dated)*
231:## 3.3. instarmux *(tool)*
233:## 3.4. reposoma *(tool, not `~/reposoma` - this is substrate)*
235:## 3.5. muticula *(tool)*
245:## 3.6. termpanum *(toolbox)*
259:## 3.7. stridulatrix *(broker + CLI)*
274:## 3.8. stridularium *(phone app)*
293:# KEYS CODE
308:## Shared meanings (all organs)
325:## Reserved (never bound by an organ)
333:## Conformity today (honest check, 2026-09-29)
```

## 6a

```zsh
grep -rn --exclude-dir=.git --exclude-dir=.hlm --exclude-dir=.majkee --exclude='*.jsonl' 'KEYS CODE' /home/hruzam/unikuklatrix/nablarva
```

```text
/home/hruzam/unikuklatrix/nablarva/raw.nablarva/ovitmugen-00-console/experience-transfer.trajectory.2026-10-02.md:24:   uncommitted, tell majkee (AGENTS.PROJECT-DESIGN.md § KEYS CODE went in via another writer).
/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md:293:# KEYS CODE
/home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md:129:- **KEYS CODE** is a cross-organ grammar: the same key means the same thing in every organ. It moves to docs/ARCHITECTURE.md, and the wrapper keeps one line and a pointer to it. Its DRY rule is already one home per fact.
/home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md:130:- **The KEYS CODE acceptance cite** points into `ovitmugen-01-basement/raw/`, so it dies when that session is pruned. Pin it (`nablarva@<sha>:path`), or carry D3's text across with its acceptance date before the prune.
/home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/process/project-documentation.symmetry.2026-10-06.md:35:| whole-animal body | cross-organ detail | layer model, dependency direction, shared grammars (KEYS CODE) | one organ's detail |
/home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/process/project-documentation.symmetry.2026-10-06.md:80:- **KEYS CODE** is a cross-organ grammar, not one organ's detail; its own text says the same key means the same thing in every organ. It moves to the whole-animal body, and the wrapper keeps one line and a pointer. Its DRY rule is already one home per fact.
/home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/process/project-documentation.symmetry.2026-10-06.md:81:- **KEYS CODE's acceptance cite** points into `ovitmugen-01-basement/raw/` and dies when that session is pruned. Pin it (`nablarva@<sha>:path`), or carry D3's text across with its acceptance date before the prune.
/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/reviewed-project-design.pre-go.2026-10-20.md:285:# KEYS CODE
/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/report.to-myshell.cleanup.2026-10-21.md:38:pointers. Product intent, L17, the ovitmugen section and KEYS CODE remain intact.
/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/cleanup.termbrana.2026-10-21/PROJECT-DESIGN.before.md:287:# KEYS CODE
/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/_bus/21.cartan.point.md:39:Relevant current boundary sources: Nablarva PROJECT-DESIGN §3.1/§3.2 and KEYS CODE,
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/RUNBOOK.md:25:4. **Architecture doc v1** — Houston (card: architecture, living session, majkee-invoked) writes `docs/ARCHITECTURE.md` from L16.9: whole-animal shape, organ list with homes, KEYS CODE grammar moved out of the wrapper (J1 thinning as a *proposed* diff, wrapper keeper commits).
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.cartan.return.md:13:d3: KEEP the extra live-pointer repairs: convergence target/link, registry DESIGN/HYPOTHESES, STATUS path labels and KEYS CODE provenance; they follow the move without changing the organ or gate meaning.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:11:-  AGENTS.PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:12:+  PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:20:-  `/home/hruzam/unikuklatrix/nablarva/.dev/session/AGENTS.PROJECT-DESIGN.md` § KEYS CODE; helps point, never copy ·
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:21:+  `/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md` § KEYS CODE; helps point, never copy ·
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:28: then the design file named in Fixed facts (§8–§12 first) and § KEYS CODE in
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:39:+  `/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md` (majkee ruling 2026-10-10); § KEYS CODE moved with it.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:51:-  AGENTS.PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:52:+  PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:56:-  § KEYS CODE is in AGENTS.PROJECT-DESIGN.md (committed by another writer in addbe07).
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:57:+  § KEYS CODE is in PROJECT-DESIGN.md at repo root, moved 2026-10-17 (committed by another writer in addbe07).
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:78:-| `ovitmugen-01-basement` | Majkee records GO or STOP after walking it live on office — ov-up with no name restores the last bed with its own tabs and root after its frame was closed; C-a 1-9 and C-a n/p jump agent tabs from either half; the halves swap left/right and up/down by key, and a preset is saved, applied and deleted from the console; ov-ls --json is unchanged while the new v1 map, events.jsonl and beds/<bed>.json appear; every ovitmugen key matches AGENTS.PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home. | `/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md` |
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:79:+| `ovitmugen-01-basement` | Majkee records GO or STOP after walking it live on office — ov-up with no name restores the last bed with its own tabs and root after its frame was closed; C-a 1-9 and C-a n/p jump agent tabs from either half; the halves swap left/right and up/down by key, and a preset is saved, applied and deleted from the console; ov-ls --json is unchanged while the new v1 map, events.jsonl and beds/<bed>.json appear; every ovitmugen key matches PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home. | `/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md` |
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.diff:289: # KEYS CODE
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.point.md:12:- B — majkee ruling 2026-10-10: `.dev/session/AGENTS.PROJECT-DESIGN.md` → `/PROJECT-DESIGN.md`; `.dev/session/AGENTS.stridularium-design.md` → `docs/organs/stridularium.md`. Houston consult constraints (TEST-INSTALL C.2/C.3/X.1): every live pointer moves in the same change; pointer-only stub at old paths; rebase relative links in moved files; `](~/…)` links → code paths; repair inbound refs (ovitmugen § KEYS CODE); ovitmugen RUNBOOK:92 append-only (append a dated pointer, do not rewrite); keep frontmatter + draft status; `git mv`; no edits to raw/, archive*, _bus/, observations; flag.md not edited (locked lines listed for majkee).
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/_bus/15.trajectory.point.md:17:- d3 Also moved (beyond the named list, as live pointers): `.germline/agents/convergence.md` target + link; meshup REGISTRY/DESIGN/HYPOTHESES pointers to the stridularium wrapper; ovitmugen STATUS checkpoint/holds lines; KEYS CODE provenance code path prefixed `.dev/session/`.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md:66:  Observed: the wrapper carries (a) the full **KEYS CODE** shared grammar (lines 277–327,
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-prompts.2026-10-09.md:78:- wrapper: .dev/session/AGENTS.PROJECT-DESIGN.md (KEYS CODE grammar → moves to the doc; J1 thinning as a PROPOSED diff)
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-prompts.2026-10-09.md:83:1. <bed>/raw/ARCHITECTURE.draft.md — whole-animal shape · organ list with homes · cross-organ grammars (KEYS CODE
/home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md:10:| `ovitmugen-01-basement` | Majkee records GO or STOP after walking it live on office — ov-up with no name restores the last bed with its own tabs and root after its frame was closed; C-a 1-9 and C-a n/p jump agent tabs from either half; the halves swap left/right and up/down by key, and a preset is saved, applied and deleted from the console; ov-ls --json is unchanged while the new v1 map, events.jsonl and beds/<bed>.json appear; every ovitmugen key matches PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home. | `/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md` |
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/note.stridularium.2026-10-01.md:5:canon: flag.md L2 · L3 · L4 · L13 · O2 · session-bed · presence-board · KEYS CODE
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/note.stridularium.2026-10-01.md:51:- Proposal: gestures carry KEYS CODE meanings (swipe = move, tap = Enter, back = q), so the phone
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/design-chapters.for-cartan.2026-10-01.md:4:cites: flag.md L13 (gaveled 2026-10-01) · L2 · L3 · L4 · L11 · L12 · KEYS CODE
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md:17:  PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md:21:  § KEYS CODE is in PROJECT-DESIGN.md at repo root, moved 2026-10-17 (committed by another writer in addbe07).
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md:14:  PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md:42:  `/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md` § KEYS CODE; helps point, never copy ·
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md:68:then the design file named in Fixed facts (§8–§12 first) and § KEYS CODE in
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md:95:  `/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md` (majkee ruling 2026-10-10); § KEYS CODE moved with it.
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md:121:  in `.dev/session/AGENTS.PROJECT-DESIGN.md` § KEYS CODE; organ helps point there, never copy.
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md:186:Keys follow § KEYS CODE: `a` save as preset · `x x` delete preset · `Enter` apply.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/STATUS.md:52:  - "Pin wrapper diff base with HEAD and PROJECT-DESIGN.md working-file hash; name Composer's edits and its architecture-owner.proposal.md. Majkee decides commit order. Live KEYS CODE citation must resolve."
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/STATUS.md:63:  G9 delta commits and current-tree state, KEYS CODE inbound references, VIST raw listing, organ-home
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/RUNBOOK.md:68:| R1 | Oraculum runs bounded field/eagle/zenith readers as needed. | Cited quotes for G9 delta, G2 organ one-liners, G3 KEYS CODE, G4/K5, G5 and the relevant current source changes. Separate quotations from inference. |
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/RUNBOOK.md:106:Majkee determines commit order. Assay checks the exact pinned base, preserves KEYS CODE's
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/RUNBOOK.md:230:post-apply KEYS CODE/live-pointer checks; never apply it to the shared worktree.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/crawl.r1-mechanical.2026-10-22.md:314:293:# KEYS CODE
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/crawl.r1-mechanical.2026-10-22.md:323:grep -rn --exclude-dir=.git --exclude-dir=.hlm --exclude-dir=.majkee --exclude='*.jsonl' 'KEYS CODE' /home/hruzam/unikuklatrix/nablarva
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/project-documentation.symmetry.2026-10-06.md:129:- **KEYS CODE** is a cross-organ grammar: the same key means the same thing in every organ. It moves to docs/ARCHITECTURE.md, and the wrapper keeps one line and a pointer to it. Its DRY rule is already one home per fact.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/project-documentation.symmetry.2026-10-06.md:130:- **The KEYS CODE acceptance cite** points into `ovitmugen-01-basement/raw/`, so it dies when that session is pruned. Pin it (`nablarva@<sha>:path`), or carry D3's text across with its acceptance date before the prune.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/prompt.sitting.2026-10-17.md:11:G3 KEYS CODE (move into the draft now, or later): a
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/prompt.sitting.2026-10-17.md:35:- live citations into the wrapper: /home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md (the ovitmugen-01 gate cites PROJECT-DESIGN.md § KEYS CODE).
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/prompt.sitting.2026-10-17.md:42:1. ARCHITECTURE.draft.md — the whole-animal body per L16.9: layer model · dependency direction · shared cross-organ grammars · cross-organ ownership · system-wide boundaries · the ladder stages 1–3 (L2) · organ list with homes, at G2's depth and with G4's home rule · KEYS CODE per G3 · decisions per G5 · header per G6 · open questions per G1/G7. Never one organ's detail.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/brief.keys-command-discovery.2026-10-21.md:11:Majkee's problem is broader than relocating KEYS CODE: the animal needs coherent action
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/brief.keys-command-discovery.2026-10-21.md:73:| [KEYS CODE](/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md:287) | Accepted TUI meanings, reserved host keys, organ-owned code and listed deviations. | Prose conformity is not proof of current runtime conformity; Ovitmugen basement normalization remains unfinished. |
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/brief.keys-command-discovery.2026-10-21.md:219:G3 still asks whether the existing accepted KEYS CODE is moved into the architecture
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:159:sed -n '/^# 3. APP parts/,/^# KEYS CODE/p' /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md | grep -n '^## '
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:225:### STEP 3 — G3 · KEYS CODE: move the grammar now or later
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:227:**Question.** Does this sitting move the KEYS CODE grammar from `PROJECT-DESIGN.md` into the draft
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:230:**Why it matters for the sitting.** KEYS CODE is the only accepted cross-organ grammar today, and
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:232:`pulse.md`) cites "PROJECT-DESIGN.md § KEYS CODE", and the grammar's acceptance cite points into
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:235:**Claims.** `said: PROJECT-DESIGN.md # KEYS CODE` — "ACCEPTED by majkee 2026-09-29 (D3 …)" and "the
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:238:(`nablarva@<sha>:path`)" · `said: audit J1` · `said: pulse.md` ovitmugen-01 gate cites § KEYS CODE ·
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:244:sed -n '/^# KEYS CODE/,/^## Shared meanings/p' /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:245:grep -n 'KEYS CODE' /home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:250:Expected: the KEYS CODE header with "ACCEPTED by majkee 2026-09-29" · the ovitmugen-01 pulse row ·
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:251:migration notes on KEYS CODE and the pin · J1 · X1 check 4 ("KEYS CODE grammar moved out of the
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:255:- `a` · Move it now. The draft carries KEYS CODE with its acceptance (majkee 2026-09-29, D3 cited
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:256:  commit-pinned). The thinning diff leaves one line plus a pointer under the same `# KEYS CODE`
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:259:- `b` · Move it later. The draft points at the wrapper's KEYS CODE and lists the move as open, with
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/gavels.X4.2026-10-17.md:564:| 3 | G3 KEYS CODE | a | SUPPORTED | yes |
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/preprint.runbook-status.mode-B.2026-10-21.md:24:| R1 | oraculum → crawlers | pre-read packets for Houston: G9 delta (re-read: fold/install, wrapper + stridularium moves, L8′, L17, generation-X incl. `nablarva-X4-vist/raw/`, current working tree), organ one-liners (G2), KEYS CODE + its inbound refs (G3) | gavels report text; briefs; flag; `meshup/REGISTRY.md`; organ homes | `raw/crawl.*.md` (cited, claim-typed) |
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/raw/preprint.runbook-status.mode-B.2026-10-21.md:31:| R8 | oraculum → assay | witness: claim types kept apart; no manufactured decisions (schemas, program home/API, ADR stub, Sublime/LiteXL, jsonl home); KEYS CODE pointer resolves; diff applies (`git apply --check`); L17 respected | drafts | PASS / findings |
/home/hruzam/unikuklatrix/nablarva/.dev/session/GLOSS.nablarva.md:661:**What is being moved.** [KEYS CODE](../../PROJECT-DESIGN.md#keys-code) is the shared
/home/hruzam/unikuklatrix/nablarva/.dev/session/GLOSS.nablarva.md:678:and [pulse route](pulse.md) cite PROJECT-DESIGN.md section KEYS CODE. A safe migration
/home/hruzam/unikuklatrix/nablarva/docs/organs/stridularium.md:32:Tailscale + Termux, then mosh) · session-bed · presence-board · KEYS CODE.
/home/hruzam/unikuklatrix/nablarva/meshup/stridularium.mobile-console.2026-09-29/raw/note.stridularium.2026-10-01.md:5:canon: flag.md L2 · L3 · L4 · L13 · O2 · session-bed · presence-board · KEYS CODE
/home/hruzam/unikuklatrix/nablarva/meshup/stridularium.mobile-console.2026-09-29/raw/note.stridularium.2026-10-01.md:51:- Proposal: gestures carry KEYS CODE meanings (swipe = move, tap = Enter, back = q), so the phone
```

## 6b

```zsh
grep -n 'PROJECT-DESIGN.md' /home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md /home/hruzam/unikuklatrix/nablarva/.dev/session/*/STATUS.md /home/hruzam/unikuklatrix/nablarva/.dev/session/*/RUNBOOK.md /home/hruzam/unikuklatrix/nablarva/AGENTS.md /home/hruzam/unikuklatrix/nablarva/PROJECT.yaml /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/*.md; grep -rn --exclude-dir=.git 'PROJECT-DESIGN.md' /home/hruzam/unikuklatrix/nablarva/docs /home/hruzam/unikuklatrix/nablarva/.germline
```

```text
/home/hruzam/unikuklatrix/nablarva/.dev/session/pulse.md:10:| `ovitmugen-01-basement` | Majkee records GO or STOP after walking it live on office — ov-up with no name restores the last bed with its own tabs and root after its frame was closed; C-a 1-9 and C-a n/p jump agent tabs from either half; the halves swap left/right and up/down by key, and a preset is saved, applied and deleted from the console; ov-ls --json is unchanged while the new v1 map, events.jsonl and beds/<bed>.json appear; every ovitmugen key matches PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home. | `/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md` |
/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/STATUS.md:10:  composer bed, flag L17, PROJECT-DESIGN.md, toolbox/termbrana/README.md and exact
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/STATUS.md:14:  PROJECT-DESIGN.md, flag.md, pulse.md, docs/, PROJECT.yaml, AGENTS.md, .germline/, toolbox/termbrana/README.md clean against HEAD.
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/STATUS.md:28:  matched by prompt-1. Wrapper base: PROJECT-DESIGN.md clean vs HEAD, blob 74e94d5519be6a2de1565ad686ab16cdff6c64c2,
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/STATUS.md:39:  PROJECT-DESIGN.md .dev/session/flag.md .dev/session/composer-01-parse;
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/STATUS.md:52:  - "Pin wrapper diff base with HEAD and PROJECT-DESIGN.md working-file hash; name Composer's edits and its architecture-owner.proposal.md. Majkee decides commit order. Live KEYS CODE citation must resolve."
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md:17:  PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md:21:  § KEYS CODE is in PROJECT-DESIGN.md at repo root, moved 2026-10-17 (committed by another writer in addbe07).
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md:35:  - No deploy by this session; ia-sync journal is another writer's; PROJECT-DESIGN.md append-only.
/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/RUNBOOK.md:34:`PROJECT-DESIGN.md` §3.1; a RUNBOOK bed is an optional attachment to that surface.
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md:14:  PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home.
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md:42:  `/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md` § KEYS CODE; helps point, never copy ·
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md:69:/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md.
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md:92:- `AGENTS.PROJECT-DESIGN.md` is maintained by the convergence seat (Cartan): append-only, never
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md:95:  `/home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md` (majkee ruling 2026-10-10); § KEYS CODE moved with it.
/home/hruzam/unikuklatrix/nablarva/AGENTS.md:32:`PROJECT-DESIGN.md` (repo root), linked from `PROJECT.yaml`; it carries
/home/hruzam/unikuklatrix/nablarva/PROJECT.yaml:15:  project-design: PROJECT-DESIGN.md # maintained working wrapper; draft, not canon
/home/hruzam/unikuklatrix/nablarva/docs/organs/stridularium.md:3:sibling: PROJECT-DESIGN.md (repo root; same species: maintained working wrapper, linked from PROJECT.yaml)
/home/hruzam/unikuklatrix/nablarva/.germline/agents/convergence.md:4:target: PROJECT-DESIGN.md
/home/hruzam/unikuklatrix/nablarva/.germline/agents/convergence.md:11:`target` above is repository-relative: [the project-design wrapper](../../PROJECT-DESIGN.md).
/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md:23:| **the wrapper** (project index) | `PROJECT-DESIGN.md` | the animal in a few lines, organ one-liners, `checked:` stamps · organ detail, a progress register |
```

## 7a

```zsh
for p in docs/ARCHITECTURE.md docs/decisions/README.md docs/organs/stridularium.md toolbox/termbrana/README.md toolbox/termbrana/DECISIONS.md meshup/REGISTRY.md .dev/session/ovitmugen-01-basement/STATUS.md .dev/session/muticula-01-qualify/STATUS.md .dev/session/composer-01-parse/RUNBOOK.md .dev/session/composer-01-parse/evidence/cleanup.termbrana.2026-10-21/architecture-owner.proposal.md .dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md .dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md; do if [ -e /home/hruzam/unikuklatrix/nablarva/$p ]; then echo "ok /home/hruzam/unikuklatrix/nablarva/$p"; else echo "MISSING /home/hruzam/unikuklatrix/nablarva/$p"; fi; done
```

```text
ok /home/hruzam/unikuklatrix/nablarva/docs/ARCHITECTURE.md
ok /home/hruzam/unikuklatrix/nablarva/docs/decisions/README.md
ok /home/hruzam/unikuklatrix/nablarva/docs/organs/stridularium.md
ok /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/README.md
ok /home/hruzam/unikuklatrix/nablarva/toolbox/termbrana/DECISIONS.md
ok /home/hruzam/unikuklatrix/nablarva/meshup/REGISTRY.md
ok /home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md
ok /home/hruzam/unikuklatrix/nablarva/.dev/session/muticula-01-qualify/STATUS.md
ok /home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/RUNBOOK.md
ok /home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/cleanup.termbrana.2026-10-21/architecture-owner.proposal.md
ok /home/hruzam/unikuklatrix/nablarva/.dev/architect-now-uncanonical/project-documentation.symmetry.2026-10-06.md
ok /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/houston-audit.2026-10-07.md
```

## 7b

```zsh
ls -la /home/hruzam/unikuklatrix/nablarva/docs /home/hruzam/unikuklatrix/nablarva/docs/organs /home/hruzam/unikuklatrix/nablarva/toolbox /home/hruzam/unikuklatrix/nablarva/meshup
```

```text
/home/hruzam/unikuklatrix/nablarva/docs:
total 24
drwxr-xr-x  4 hruzam hruzam 4096 17. říj 06.14 .
drwxr-xr-x 16 hruzam hruzam 4096 22. říj 06.50 ..
-rw-r--r--  1 hruzam hruzam  801  1. říj 06.02 ARCHITECTURE.md
drwxr-xr-x  2 hruzam hruzam 4096 24. srp 09.36 decisions
drwxr-xr-x  2 hruzam hruzam 4096 17. říj 06.14 organs
-rw-r--r--  1 hruzam hruzam 3335  3. zář 15.36 repo-unification.2026-09-02.md

/home/hruzam/unikuklatrix/nablarva/docs/organs:
total 12
drwxr-xr-x 2 hruzam hruzam 4096 17. říj 06.14 .
drwxr-xr-x 4 hruzam hruzam 4096 17. říj 06.14 ..
-rw-r--r-- 1 hruzam hruzam 3115 17. říj 06.15 stridularium.md

/home/hruzam/unikuklatrix/nablarva/meshup:
total 40
drwxr-xr-x  8 hruzam hruzam 4096  5. říj 08.04 .
drwxr-xr-x 16 hruzam hruzam 4096 22. říj 06.50 ..
drwxr-xr-x  2 hruzam hruzam 4096  1. říj 09.21 entity.polysession-continuant.2026-08-02
drwxr-xr-x  2 hruzam hruzam 4096  5. říj 00.04 extraction.driller-onion.2026-06
drwxr-xr-x  3 hruzam hruzam 4096  5. říj 00.04 lab.observability-probes.2026-08-01
-rw-r--r--  1 hruzam hruzam 7758 17. říj 06.15 REGISTRY.md
drwxr-xr-x  3 hruzam hruzam 4096  5. říj 08.04 room.brokered-journal.2026-07-31
drwxr-xr-x  3 hruzam hruzam 4096  5. říj 08.03 seam.cross-vendor-relay.2026-08-05
drwxr-xr-x  3 hruzam hruzam 4096  5. říj 00.04 stridularium.mobile-console.2026-09-29

/home/hruzam/unikuklatrix/nablarva/toolbox:
total 12
drwxr-xr-x  3 hruzam hruzam 4096  2. zář 00.20 .
drwxr-xr-x 16 hruzam hruzam 4096 22. říj 06.50 ..
drwxr-xr-x  5 hruzam hruzam 4096  2. zář 11.24 termbrana
```

## 8a

```zsh
ls -la /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-vist/raw/
```

```text
total 24
drwxr-xr-x 2 hruzam hruzam  4096 19. říj 17.12 .
drwxr-xr-x 3 hruzam hruzam  4096 14. říj 03.49 ..
-rw-r--r-- 1 hruzam hruzam 16154 19. říj 17.11 vist-01-principle-and-applications.md
```

## 8b /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-vist/raw/vist-01-principle-and-applications.md

```zsh
grep -n '^#' /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-vist/raw/vist-01-principle-and-applications.md
```

```text
6:# VIST — vendor-invariant session telemetry: principle and possible applications
12:## The recommendation
22:## Names
35:## The principle: MCP turned inside out
58:## Where VIST sits: sensor, controller, actuator
97:## What VIST can and cannot establish
115:## Antensor: sources and pipeline
148:## Event model v0
177:## Registries: the programmatic part and the source part
191:## Canary
201:## Prior art and fit
216:## Possible applications
232:## Limits and non-goals
240:## Open choices for Majkee
```

## 9

```zsh
ls -d /home/hruzam/unikuklatrix/nablarva/.dev/session/*/
```

```text
/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/
/home/hruzam/unikuklatrix/nablarva/.dev/session/harvest/
/home/hruzam/unikuklatrix/nablarva/.dev/session/muticula-01-qualify/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-00-/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-00/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-00-main-design-signpost/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-03-app-architecture/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-communication-protocole/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X0-restarted/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/
/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X4-vist/
/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/
/home/hruzam/unikuklatrix/nablarva/.dev/session/promptbook-coder-foil/
/home/hruzam/unikuklatrix/nablarva/.dev/session/recovery/
/home/hruzam/unikuklatrix/nablarva/.dev/session/relay-contract/
/home/hruzam/unikuklatrix/nablarva/.dev/session/skill-report-test/
/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-X1-composer-sourcing/
/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-X2-composer-sublime-ide/
/home/hruzam/unikuklatrix/nablarva/.dev/session/test/
/home/hruzam/unikuklatrix/nablarva/.dev/session/toolbox-ommatermia-00-brief/
/home/hruzam/unikuklatrix/nablarva/.dev/session/toolbox-termbrana-01-brief/
/home/hruzam/unikuklatrix/nablarva/.dev/session/toolbox-termbrana-02-m0-truthspike/
/home/hruzam/unikuklatrix/nablarva/.dev/session/toolbox-termpanum-00-brief/
/home/hruzam/unikuklatrix/nablarva/.dev/session/voice-relay-00-probe/
```
