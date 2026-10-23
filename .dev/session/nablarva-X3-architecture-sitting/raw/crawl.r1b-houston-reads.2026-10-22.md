crawl: r1b-houston-reads · writer: eagle · for: oraculum(cSharp) X3, answering Houston arc.md §5 · run at: 2026-10-22 06:56:55 CEST

## R-1

```zsh
git -C /home/hruzam/unikuklatrix/nablarva log -1 --format='%H %cs' -- .dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md
git -C /home/hruzam/unikuklatrix/nablarva ls-files --error-unmatch .dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md
grep -n 'D3' /home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md
git -C /home/hruzam/unikuklatrix/nablarva log --diff-filter=A --format='%H %cs %s' -- .dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md
```

```text
c630f0e8b1490e34458a52988342d679b24f2f5b 2026-10-02
.dev/session/ovitmugen-01-basement/raw/architecture.pipes-ui-keys.2026-09-29.md
120:- **D3 · keys — ANSWERED 2026-09-29 (majkee): shared TUI key grammar ACCEPTED, DRY.** Lives once
c630f0e8b1490e34458a52988342d679b24f2f5b 2026-10-02 ovitmugen-00-console: pruned after preservation c2882bd0fe1e10acd1beffa0c473d6b64bff8f80; router row removed
```

## R-2

```zsh
git -C /home/hruzam/unikuklatrix/nablarva log --format='%h %cs %s' -S 'L17 · Termbrana composition' -- .dev/session/flag.md
```

```text
32bd6f4 2026-10-22 2026-10-17 . nablarva-X1
```

## R-3

```zsh
git -C /home/hruzam/unikuklatrix/nablarva diff fe32a2951d11ca1004155b08090fabb6f5827fad HEAD -- .dev/session/pulse.md AGENTS.md PROJECT.yaml
```

```text
diff --git a/.dev/session/pulse.md b/.dev/session/pulse.md
index 735dbc9..232f6cb 100644
--- a/.dev/session/pulse.md
+++ b/.dev/session/pulse.md
@@ -7,5 +7,7 @@
 |---|---|---|
 | `nablarva-X1-architecture` | Majkee records GO on the first real whole-animal architecture doc (`docs/ARCHITECTURE.md`, L16.9 homes) written with Houston operating from its canonical homes — promotion + keeper migration + Codex runtime artifacts done, one Houston audit from the canonical card classified by majkee. | `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/STATUS.md` |
 | `nablarva-02-pipe-qualification` | Majkee records GO or STOP on Oraculum's evidence-backed qualification VERDICT: can one explicitly bound, already-running, disposable Codex session receive a native operator-triggered assignment and produce its exact correlated RETURN, while preserving identity, permissions, native UI and subscriber usage? | `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/STATUS.md` |
-| `ovitmugen-01-basement` | Majkee records GO or STOP after walking it live on office — ov-up with no name restores the last bed with its own tabs and root after its frame was closed; C-a 1-9 and C-a n/p jump agent tabs from either half; the halves swap left/right and up/down by key, and a preset is saved, applied and deleted from the console; ov-ls --json is unchanged while the new v1 map, events.jsonl and beds/<bed>.json appear; every ovitmugen key matches AGENTS.PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home. | `/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md` |
+| `ovitmugen-01-basement` | Majkee records GO or STOP after walking it live on office — ov-up with no name restores the last bed with its own tabs and root after its frame was closed; C-a 1-9 and C-a n/p jump agent tabs from either half; the halves swap left/right and up/down by key, and a preset is saved, applied and deleted from the console; ov-ls --json is unchanged while the new v1 map, events.jsonl and beds/<bed>.json appear; every ovitmugen key matches PROJECT-DESIGN.md § KEYS CODE — with ov-selftest and rb-selftest green on office and home. | `/home/hruzam/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md` |
 | `muticula-01-qualify` | Majkee records GO or STOP on an independently witnessed step-0 package. For Claude Code and Codex, in the interactive modes muticula will run in, it shows which raw Git routes the native permission rules really deny (stage, commit, whole-tree and HEAD-moving commands, including aliases, sh -c, command git, compound commands and bypass modes), that a stub muticula command stays allowed, and whether MUTICULA_ID/MUTICULA_KEY reach tools and child agents. Every route it does not prove is declared a cooperative rule, and B0's fail-open results carry over as limits. | `/home/hruzam/unikuklatrix/nablarva/.dev/session/muticula-01-qualify/STATUS.md` |
+| `composer-01-parse` | Phase 0 exit finding, brief §3 | `/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/STATUS.md` |
+| `nablarva-X3-architecture-sitting` | majkee GO on raw/ARCHITECTURE.draft.md, ready to promote to docs/ARCHITECTURE.md. | `/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X3-architecture-sitting/STATUS.md` |
diff --git a/AGENTS.md b/AGENTS.md
index 5400527..8525fcd 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -29,15 +29,15 @@
 
 Session surfaces (flag L9 + L9′): `flag.md` owns locks; `pulse.md` routes to each
 session's sole doing-state, `STATUS.md`. The working project wrapper is
-`.dev/session/AGENTS.PROJECT-DESIGN.md`, linked from `PROJECT.yaml`; it carries
+`PROJECT-DESIGN.md` (repo root), linked from `PROJECT.yaml`; it carries
 design intent and open questions. `.dev/session/dock.md` is the
 UNCANONICAL scratch — side quests land there without a blessing; never cite it as
 truth. Task-scoped work gets `.dev/session/<topic>/` dirs that die with the task. No
-standing plan.md (abolished — survey receipt, 2026-08-02). `.dev/session/GLOSS.<part>.md` = the operator's learning file for one part (uncanonical like dock.md; one per part; every RUNBOOK of the part points to it). Not every work needs one — the driver ASKS "record GLOSS.<slug>.md?" when a sitting looks like it needs explaining, never assumes. Guide: reposoma `raw.guides/gloss/GUIDE.md`.
+standing plan.md (abolished — survey receipt, 2026-08-02). `.dev/session/GLOSS.<part>.md` = the operator's learning file for one part (uncanonical like dock.md; one per part; every RUNBOOK of the part points to it). Not every work needs one — the driver ASKS "record GLOSS.<slug>.md?" when a sitting looks like it needs explaining, never assumes. Guide: reposoma `raw.guides/gloss/GUIDE.md`. `.dev/observations/<slug>.<seat>.<date>.md` = the session-PROCESS record (what a session taught about running sessions — faults, carriage, support logs); outside every bed, append-only, never pruned; beds promote theirs there before prune (runbook GUIDE §On gate closure, gaveled 2026-10-07; first instance X0).
 
 ## Route by seat
 
-**Convergence — app-scheme maintainer (any runtime, agent or subagent):** at session entry, unless already settled, ask @majkee "Am I the master app-scheme maintainer?"; if yes, read `.germline/agents/convergence.md` and maintain its named target; `flag.md` retains authority over locks.
+**Houston — project-design keeper (audit card):** Majkee invokes the audit. Its project method lives at `.germline/agents/houston/nablarva.md`, with the vendor bindings `~/.germline/agents/houston/binding.claude.md` and `binding.codex.md` and the shared identity at `~/.germline/agents/houston/identity.md`; the audit card is `~/.germline/agents/houston/cards/audit.md`. The audit returns wrapper-mechanics changes for Majkee to commit; `flag.md` retains authority over locks.
 
 Four base seats, global roster — no domain seat pre-granted (earned, not assumed):
 - **architect** (@Houston-family) — plan + gates; owns `.dev/session/pulse.md`
@@ -71,4 +71,7 @@ only through the reviewed-merge boundary.
 - **Boundary:** Cluster A mechanism (session clipper / processor / composer) stays in
   `applications-in-common`. The clipper `OUTPUT (A)` ↔ stridularium feed interface gets
   one boundary note when both threads run (L13).
+  Composer destination exception, majkee 2026-10-17: flag L8′ supersedes that location
+  for composer work; publication passes to or through `~/ia-sync/`, with deploy or
+  installer/agent-assisted procedure as suitable. Read L8′ before applying the older location.
 - Canon is gaveled by majkee. Agents draft; he locks.
diff --git a/PROJECT.yaml b/PROJECT.yaml
index e555c1f..9d46d32 100644
--- a/PROJECT.yaml
+++ b/PROJECT.yaml
@@ -12,8 +12,8 @@ commands:                   # docs-only phase; verbs land when docket item 2 gav
   run:   "none yet"
 docs:
   architecture: docs/ARCHITECTURE.md
-  project-design: .dev/session/AGENTS.PROJECT-DESIGN.md # maintained working wrapper; draft, not canon
-  project-design-maintainer: .germline/agents/convergence.md # shared role for any runtime
+  project-design: PROJECT-DESIGN.md # maintained working wrapper; draft, not canon
+  project-design-maintainer: .germline/agents/houston/nablarva.md # Houston audit method; vendor bindings global at ~/.germline/agents/houston/
   decisions:    .dev/session/flag.md
 agents: [ architect, challenger, researcher, implementer ]   # four base seats; domain seats earned
 mcp_profile: none           # placeholder — Model-C sizing deferred (onboarding-kit O1)
```

## R-4

```zsh
git -C /home/hruzam/unikuklatrix/nablarva ls-files .dev/session/nablarva-X4-vist .dev/session/termbrana-X1-composer-sourcing .dev/session/termbrana-X2-composer-sublime-ide
```

```text
.dev/session/nablarva-X4-vist/raw/vist-01-principle-and-applications.md
.dev/session/termbrana-X1-composer-sourcing/raw/handoff.cartan.runbook-preparation.2026-10-21.md
.dev/session/termbrana-X2-composer-sublime-ide/raw/termbrana-X3-sublime-ide.md
```
