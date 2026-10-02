# STATUS: muticula-01-qualify

```yaml
updated: 2026-10-02 (Cartan's verdict 02 folded into plan r3 + run manifest; POINT 03 out)
writer: trajectory · anthropic
host: office
worktree: >-
  /home/hruzam/unikuklatrix/nablarva · core · b35979e (before this bed's commit). Other writers'
  uncommitted changes in the checkout are not ours; they are never staged from here.
gate: >-
  Majkee records GO or STOP on an independently witnessed step-0 package. For Claude Code and
  Codex, in the interactive modes muticula will run in, it shows which raw Git routes the
  native permission rules really deny (stage, commit, whole-tree and HEAD-moving commands,
  including aliases, sh -c, command git, compound commands and bypass modes), that a stub
  muticula command stays allowed, and whether MUTICULA_ID/MUTICULA_KEY reach tools and child
  agents. Every route it does not prove is declared a cooperative rule, and B0's fail-open
  results carry over as limits.
checkpoint: >-
  Opened on 2026-09-27 with majkee's blessing of the drafted gate. The brief r3 was copied into
  raw/ byte-identically from nablarva adce981 (sha256 eca37781…). The RUNBOOK names the lanes:
  the Claude lane is Trajectory's, witnessed by Cartan; the Codex lane is Cartan's, witnessed
  by a fresh assay. On 2026-09-29, prompt-0 wrote raw/plan.step0.2026-09-29.md (sha256 d76a1802…),
  built on Claude Code 2.1.284's documented permission semantics: deny rules are checked per
  subcommand, hold in bypassPermissions, and miss git -C / git -c. It has tier A (print
  instrument, breadth) and tier B (interactive confirmation), with outcome classes DENIED /
  PROMPTED / RAN / INVALID. The Codex lane is framed for Cartan. Two open questions for majkee:
  his interactive modes (Q1) and a sandbox row (Q2). He answered the same day: default + acceptEdits,
  and no sandbox row. Both are folded (plan sha256 054bc2ac…), and the POINT was re-pinned before
  any reply. No run has started.
  Cartan answered on 2026-09-29: verdict 01 REVISE (_bus/01.cartan-muticula.verdict.md), plus his
  Codex-lane companion (raw/plan.step0.codex-lane.2026-09-29.md), whose native mapping is complete
  but blocked on persistence-free trust. The head folded the verdict into plan r2 (sha256
  3b83620b…): interactive-first, 34 cells per mode, the rest not_run. A Sonnet spawn drafted it and
  the head applied 8 corrections. r1 is kept as reviewed-054bc2ac. The RUNBOOK's fixed facts were
  corrected: three B0 Codex reasons, and the modes row.
  On 2026-10-02 Cartan returned verdict 02 REVISE (bounded: M1–M4) and fixed the Claude-lane budget:
  122 cell attempts, 8 parent launches, 3.5 h, haiku. It is folded into plan r3 (sha256 8b484e6d…) and
  the run manifest raw/manifest.step0.claude.2026-10-02.md (sha256 b661adc7…). The manifest has 8
  launches and 122 frozen rows, and its frozen settings list bare + wildcard denies. A Sonnet spawn
  applied the fold; the head made 4 corrections (the E cells run the stub, key-only absence, frozen
  settings, the title). r2 is kept as reviewed-3b83620b.
in_flight: >-
  _bus/03.trajectory-dashboard.point.md → cartan: a fold check of r3 and a review of the manifest's
  frozen settings (§1b).
recovery_probe: >-
  ls raw/ — if only the brief is there, prompt-0 has not started. A raw/plan.step0.*.md file
  means the plan exists: check _bus/ for its POINT to cartan and the CHALLENGE path it names.
  The brief must still hash to eca37781….
holds:
  - No product code; the stub muticula is a logging fixture.
  - No global settings or trust change (~/.claude*, ~/.codex/) without majkee's explicit word recorded here.
  - Recorded 2026-09-29, majkee "ok, try" — one temporary trust entry for the throwaway fixture folder, Claude lane only. It is added right before the interactive runs and removed right after. Only ~/.claude.json's before/after hashes are kept; the file itself never enters evidence.
  - Recorded 2026-10-02, majkee "(a)" — one temporary trust entry for the throwaway Codex fixture folder, Codex lane only. Added right before the Codex interactive runs and removed right after. Whole-file hashes of ~/.codex/config.toml and the other inventoried layers are taken before and after, plus a semantic check that only that one entry came and went. No other config change; this is not a precedent for any other folder.
  - No run before Cartan's CHALLENGE of the plan is answered and folded.
  - claude -p is a measurement instrument only, never in anything built.
next: >-
  Cartan answers POINT 03. On PROCEED the Claude lane launches within the 122 / 8 / 3.5 h ceiling,
  in a session majkee chooses (this one or a fresh runner). The Codex lane follows Cartan's companion
  with majkee's (a) trust entry.
expected: >-
  _bus/03.cartan-muticula.verdict.md (PROCEED → the Claude lane runs; REVISE → r4).
```
