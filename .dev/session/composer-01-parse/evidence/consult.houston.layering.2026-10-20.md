---
kind: consultation-capture
captured_by: Cartan · Codex
source: /root/houston_termbrana_consult · native houston · bounded follow-up
cycle: '22'
date: 2026-10-20
verbatim: true
---

Route: spawned child (canary: hc-9b3f0521).
/home/hruzam/.germline/agents/houston/identity.md · stamp: 99ae988e
/home/hruzam/.germline/agents/houston/binding.codex.md · stamp: 0c812f6c
/home/hruzam/unikuklatrix/nablarva/.germline/agents/houston/nablarva.md · stamp: d9ee9067
/home/hruzam/.germline/agents/houston/cards/consult.md · stamp: 5435b1c7
Effective cwd: /home/hruzam/unikuklatrix/nablarva

**card: consult · verdict: stretches**

## 1. Files changed

None. No helper, live probe or source execution.

## 2. Commands and outcomes

Read-only `cat`, `nl`, `sed`, `rg`, `sha256sum` and `git rev-parse` inspections succeeded.

Inspected ovitmugen source SHA256: `97dba115a36abf216ab6f5deabda601ce82e395cdd285a1b52aca7568f5a3125`. This consult establishes source facts and architectural compatibility, not functional acceptance.

## 3. Evidence paths

- `/home/hruzam/ia-sync/zsh/session/ovitmugen.py`: header laws, lines 10–23; `Tmux`/`servers`, 59–101; `tabs`, 147–165; `plan_up`, 222–292; `bed_report`/`cmd_ls`, 552–587; `plan_down`, 590–620; injection exclusion selftest, 817–827.
- `toolbox/termbrana/Cargo.toml`; `crates/termbrana-zellij/Cargo.toml` and `src/main.rs` under that workspace, especially lines 47–63, 112–137 and 204–219.
- `toolbox/termbrana/research/termbrana.project-definition.md` §§2.3/2.4; current README composition direction; `PROJECT-DESIGN.md` §§3.1/3.2.
- Composer `_bus/21.cartan.point.md` operator words, `_bus/22.cartan.point.md`, RUNBOOK and current STATUS; flag L3/L4/L11/L12/L14/L16/L8′; `docs/ARCHITECTURE.md`; native entry chain.

## 4. Mismatches discovered

**said: Majkee:** asks whether Termbrana uses ovitmugen resources/pipes or both share a layer. This is a question, not an A/B selection.

**inferred: houston:** Cartan’s provisional **B is coherent as a dependency direction**, with the constraints below. Ovitmugen supplies layout/control operations and computed discovery today. Its `Tmux` helper names servers explicitly but executes arbitrary tmux arguments; its viewer-only law is not an enforced restriction inside that helper. `bed_report` returns beds, windows, views and attachment counts, without complete host/socket/pane binding. `Tmux.run` captures decoded text; `lines` splits it. These are not byte-preserving packet interfaces.

Termbrana’s actual workspace contains only the Zellij probe crate. Its pipe dispatches probe commands and returns diagnostic logs; `ReadCliPipes` is explicitly harness-only. Neither source supplies the proposed common payload layer.

Thus **“both already share a pipe layer” would contradict the artifacts**. The proposal correctly remains prospective. Optional consumption of ovitmugen’s JSON discovery is compatible with B; it need not make reusable composition depend on the dashboard’s existence.

## 5. Recommended next task

Carry B as a proposed direction, subject to five constraints:

1. **Keep dependencies at integration edges.** Termbrana composition and its inert parser remain useful without ovitmugen, a RUNBOOK bed, tmux, an editor or an interactive shell. Share only mechanisms with demonstrated consumers; B does not require creating a framework now.
2. **Preserve resource and lifetime ownership.** Ovitmugen retains view/layout management and its protected agent-session boundary. Composition must not require its frame or views to remain open, or acquire process-lifetime control through helper reuse.
3. **Separate discovery from delivery authority.** Reading JSON or sharing command helpers grants no permission to submit input. Future transmission needs explicit operator authority and complete, checked target binding; current bed/window metadata alone is insufficient.
4. **Keep control text distinct from payload bytes.** Neither `Tmux.run` nor the probe pipe establishes packet fidelity, delivery semantics or raw-PTY provenance. Preserve Phase 0 bytes/EOLs and observer defaults; qualify any later carrier and reconcile applicable L3/L4/L14 conflicts before implementation or activation.
5. **Leave ownership and placement decisions explicit.** A lower boundary must not absorb composition policy, regulated room routing or room truth. Its eventual owner/source home and any structural change require the applicable Majkee gavel; L8′ alone does not settle them.

## 6. Remaining uncertainty

The actual shared mechanism, ownership, target-binding contract, payload semantics and qualification criteria remain undecided. No runtime behavior was tested. These gaps permit recommending B provisionally; they prevent describing a common service as existing or authorizing its build.
