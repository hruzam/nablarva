# RUNBOOK: Termbrana M0 — host contract freeze

```yaml
goal: Close termbrana M0 — sit pad.1, fold evidence into t02–t05, @Assay fresh-eyes pass, freeze the host contract.
gate: M0 deliverables on disk + an @Assay-class fresh-eyes pass → host contract FROZEN.
participant_1: [oraculum, {brand: "Claude Code", model: opus, effort: high}, host: "office"]
participant_2: [majkee, {role: "operator — pad.1 requires real hands at a real terminal"}, host: "office"]
```

## Status of this file

**Promoted from the bench 2026-09-01** (majkee blessing, session fc-sync.oraculum.sella) —
this file is now the session's `RUNBOOK.md`, completing the runbook-GUIDE file set for this
bed. `handoff.md` keeps its name (its gate is still open — never rename inside an open bed).
The bench copy at `~/reposoma/_runbook/termbrana/m0-close/` is pruned; reposoma git history
holds it. The superseded `termbrana-readme` draft (Proxima, 2026-08-24) was pruned with it —
its live content is item 4a below; its cold-start card now sits IN THIS FOLDER.

## Scope

- **Governance:** nablarva `flag.md` **L11** — sole authority on structural/topology/ownership.
- **Office only.** `zellij` is ABSENT on home; `research/evidence/host-versions.md` is stamped
  `host: office`.
- **Run from `~/ia-sync`.** The deliverable is a *host contract* — a machine-layer artefact
  wearing a project badge. Dual-harness precedence is declared in prompt-0.
- flag L11 holds until the gate closes: *"no parallel coding before M0 freezes the host
  contract."* M1 is governance-blocked, not merely pad-blocked. (Session 03-tunnel exists as
  an authored RUNBOOK but is L11-gated on THIS session's freeze — or majkee's exception.)

# prompt-0

```
Termbrana M0 closure — office session.

0 · SEAT, HARNESS, PRECEDENCE.
You are @Oraculum working termbrana M0, running from ~/ia-sync for machine-layer
overview — NOT as @Kelvin, and this is not maintenance work. Do not apply Kelvin's
"mail piql Houston after any meaningful session" rule to this task.

Two harnesses are in play. PRECEDENCE: nablarva flag.md wins on structure, topology,
ownership and gates (L11 is sole authority). ia-sync wins on host facts, deploy
mechanics and machine state. When they disagree, SAY SO rather than picking silently —
the disagreement is the artifact.

VERIFY HOST BEFORE ANYTHING ELSE:
    ls /usr/bin/php74 && command -v valet
Both present = office, proceed. Absent = you are on home, where zellij is ABSENT and
termbrana cannot build — stop and say so. Do not trust any file's `host:` header:
zsh/AGENTS.md, zsh/CLAUDE.md and the ai/temple-*.zsh headers all declare "office"
regardless of where you stand. See ~/ia-sync/AGENTS.md §"Which host am I on?".

1 · READ, IN THIS ORDER.
    ~/unikuklatrix/nablarva/AGENTS.md
    .dev/session/flag.md            — L6, L9, and especially L11
    .dev/session/pulse.md           — top entry only
    .dev/session/toolbox-termbrana-02-m0-truthspike/status.md
    .dev/session/toolbox-termbrana-02-m0-truthspike/pad.1-m0-runtime-confirm.md

2 · THE ONLY LEGAL PATH.
flag L11: "One integration owner; no parallel coding before M0 freezes the host
contract." Do not open M1 work, do not touch termbrana-core, do not plan lanes.
Close M0 or do nothing.

3 · FIRST ACTION — check pad.1's `>MAJKEE report` fences.
STEP 0 was sat 2026-08-16 (<MATCH>). STEPS 1–5 were still empty as of 2026-08-25.
  - EMPTY  → hand majkee the pad. One step, one concept, wait for his report, then the
    next. You drive, he is the hands. Never run ahead. Steps 2–3 are `zellij action
    pipe` probes; step 4 judges resize/flicker; step 5 is the largest evidence gap.
  - FILLED → fold results into the PENDING-OPERATOR rows of research/evidence/t02–t05
    and pane-content-matrix.md, then @Assay fresh-eyes over the full evidence set
    (handoff gate law — the writer does not verify their own work), then freeze.

4 · RESOLVE BEFORE FREEZING.
 a) toolbox/termbrana/README.md carries an uncommitted +153/−3 expansion by @Cartan. It is NOT
    stashed. Review against CS.termbrana-readme.2026-08-24.md (IN THIS FOLDER).
    DO NOT `git checkout` it away.
 b) The machines are MANJARO (/etc/os-release → ID=manjaro, ID_LIKE=arch), not Arch.
    research.epoch.host-versions.2026-08-15.md justified the M0 pins on "Arch extra in
    sync with upstream" — wrong repo; Manjaro holds packages behind Arch on staged
    branches. PAD-01 confirmed the pins empirically so they probably hold, but decide
    EXPLICITLY whether to accept or re-verify, rather than freezing a contract whose
    stated reasoning cites the wrong distro.
 c) Re-verify the pins on office and record the distro. The host contract is a
    machine-layer commitment:
        zellij --version && rustc --version && cargo --version
    Compare against research/evidence/host-versions.md and add `ID=manjaro` to that
    file, so the frozen contract states which repos the pins came from.

5 · GATES.
majkee owns commit, push, flag locks, and the M0 freeze itself. No termbrana-local
agent, harness, devenv twin, pulse or beacon (L11). DECISIONS.md = product-technical
ADRs only, each citing its authorizing flag line.

6 · AFTER FREEZE.
Session 03 opens — NOTE (2026-09-01): majkee re-scoped 03 from "m1-core" to
03-tunnel (RUNBOOK already authored at
.dev/session/toolbox-termbrana-03-tunnel/RUNBOOK.md, L11-gated on this freeze).
Parallel lanes become legal, @Flight branch group eligible. The A5 benchmark corpus
(5 frozen sessions / 15 retrieval tasks) freezes during M1 — do not forget it when
M1-core opens (as a later numbered sibling).

7 · MACHINE-LAYER CARRY.
Read the HOME 2026-08-25 and HOME 2026-08-27 entries in
~/ia-sync/journal.host-cleanup.md. NOTE (2026-09-01): office's zsh tree HAS now been
drift-audited — 18 orphans quarantined to /tmp/zsh-prune-2026-09-01 (see the ORACULUM
2026-09-01 journal entries); the zsh-orphans.zsh run in this step is a re-check, not
a first audit.
```

## References

Point, do not copy — canon lives with the project.

- Session bed: `nablarva/.dev/session/toolbox-termbrana-02-m0-truthspike/` (this folder)
- README review card: `CS.termbrana-readme.2026-08-24.md` (this folder — moved from the
  bench 2026-09-01)
- Evidence: `toolbox/termbrana/research/evidence/` — `host-versions.md` is the pin record
- Canon: nablarva `flag.md` L6 · L9 · L11 · `toolbox/termbrana/DECISIONS.md`
- Re-entry: `~/reposoma/_mail/monkey/inbox/CS.termbrana-m0.2026-08-15.md`
- Machine layer: `~/ia-sync/journal.host-cleanup.md` · `AGENTS.md` §"Which host am I on?"
- Next session (authored, L11-gated): `.dev/session/toolbox-termbrana-03-tunnel/RUNBOOK.md`
