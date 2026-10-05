# card.J — nablarva-00 bed inventory · 2026-10-05

`@Field · majkee request 2026-10-05 · read-only distillation · uncanonical`
Scope: all files under `.dev/session/nablarva-00/`; cross-ref: pulse.md, meshup/REGISTRY.md.

## File table

Paths relative to `.dev/session/nablarva-00/`. JSON dir = `raw/cartan-codex-0.158.0.2026-09-30/` (754 files, text/JSON not binary).

| path | author/seat | date | class | one-line content | unique elsewhere? | disposition | evidence |
|---|---|---|---|---|---|---|---|
| `audit.patterns-and-loop.oraculum.2026-09-29.md` | Oraculum (Claude) | 2026-09-29 | audit | Loop 6-step table; 10-philosophy map; 9-pattern scoring; pipes table | Cited within bed by addendum L1 and build-description §0; not cited externally | HISTORY-ONLY | STATUS.md:24 |
| `audit.wrapper-rewrites.oraculum.2026-09-29.md` | Oraculum (Claude) | 2026-09-29 | audit | Proposed rewrite chapters 1–4 for AGENTS.PROJECT-DESIGN.md; dangling-ref findings | Candidate text target is AGENTS.PROJECT-DESIGN.md; commit fd66470 folded some changes | HISTORY-ONLY | STATUS.md:25 |
| `audit.session-progress.oraculum.2026-09-29.md` | Oraculum (Claude) | 2026-09-29 | audit | 13 open gates; orphan directory list; 8 contradictions; proposals M1–M8 | Corrected by addendum §3; items partially addressed in later sessions | HISTORY-ONLY | STATUS.md:26 |
| `return.cartan.independent-read.2026-09-30.md` | Cartan (Codex) | 2026-09-30 | raw input | Independent loop read; Codex 0.158.0 schema facts; probe design; session-progress notes | Key facts summarized in addendum §2/§6; probe in addendum §4 | HISTORY-ONLY | STATUS.md:28 |
| `addendum.after-cartan.oraculum.2026-09-30.md` | Oraculum (Claude) | 2026-09-30 | audit | Correction tables for audits 1+3; agreed points; "verified today" fact table | Standalone correction record; not cited externally | HISTORY-ONLY | STATUS.md:27 |
| `STATUS.md` | Oraculum (Claude) | 2026-09-30 | STATUS/RUNBOOK | Session gate, checkpoint, 5 Majkee decisions (2026-09-29), holds, open items | Majkee decisions not recorded elsewhere; no pulse.md row (STATUS.md:46) | HISTORY-ONLY | STATUS.md:1–54 |
| `build-description.draft.oraculum.2026-09-30.md` | Oraculum (Claude) | 2026-09-30 | brief | Relay pieces R1–R5; stones S0–S5; `ov ls --json` consumer contract; scope decisions | LIVE CITATION: ovitmugen-01-basement/RUNBOOK.md:87 and STATUS.md:30 name it as the consumer contract | KEEP → cite from ovitmugen-01 or promote to .dev/research/seam-cross-vendor-relay/ | build-description §6; ovitmugen-01/RUNBOOK.md:87 |
| `raw/cartan-codex-0.158.0.2026-09-30/` (754 JSON) | Cartan (Codex) | 2026-09-30 | raw input | Codex 0.158.0 app-server protocol schemas: stable (314) + experimental (440); zero-quota | Unique primary source; no other copy found; cited by return.cartan:30 | KEEP → .dev/research/vendor-events/ alongside existing catalogue | return.cartan.independent-read:30 |

## pulse.md and DESIGN.md cross-reference

**pulse.md:** nablarva-00 is absent (4 active sessions listed; none matches nablarva-00*).
STATUS.md:46 explicitly records this: "This session has no line in pulse.md."
**DESIGN.md files (meshup/):** no reference to nablarva-00* found.
**Other live references found:** nablarva-03/STATUS.md:13 (pre-existing untracked note);
ovitmugen-01-basement/RUNBOOK.md:87 and STATUS.md:30 (build-description named as consumer contract).

## git tracking

`git status` snapshot shows `?? .dev/session/nablarva-00/` — the entire directory is **untracked**.
No file in this bed has been committed. Delta to verify: `git log -- .dev/session/nablarva-00/`.

## What these beds were for

STATUS.md:8–9 (Oraculum): *"Full audit requested by Majkee: read everything, find patterns,
stratify the building philosophies and ideas, propose wrapper rewrites, analyse session progress.
Not an architecture build and not a plan."* The session ran 2026-09-29 with thirteen sub-reader
agents and a Janus challenge; Cartan delivered an independent read 2026-09-30, generating the
Codex 0.158.0 schemas at zero quota. STATUS.md:18–19: *"The two reads agree on the diagnosis:
attraction is the unresolved step."* The build-description.draft then named the first transport
protocol, relay pieces R1–R5, and stones S0–S5 — the framing Majkee identifies as the point
at which the playground was found.
