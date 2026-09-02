# handoff — toolbox-termbrana · session 02 (M0 truth spike)
`NOTE 2026-09-02: paths below pre-date flag L12 — termbrana now lives at ~/unikuklatrix/nablarva/toolbox/termbrana/; Part 1 bootstrap commands are historical record, do not re-run.`

`authorized-by: flag L11 (majkee gavel 2026-08-15) · designed-by: Houston (office 2026-08-15)`
`read first: nablarva AGENTS.md → flag L11 → ../toolbox-termbrana-01-brief/brief.md →`
`~/.remote/harvest/termbrana.execution-plan.md (§1 authority order · §3 M0 · §12 assignment)`
`gate: M0 deliverables complete → host contract FROZEN. No parallel coding before that.`

## Part 1 — repo bootstrap (operator or @Delta; commands EMITTED, never auto-run)

```bash
# === termbrana — toolbox bootstrap (A2 mechanics, flag L11) ===
mkdir -p ~/unikuklatrix/termbrana
cd ~/unikuklatrix/termbrana
git init --initial-branch=core
gh repo create termbrana --private --source=. --remote=origin
# first commit happens AFTER Part-1 files land (below), then:
#   git add -A && git commit -m "founding: substrate + governance (flag L11, session 01)" && git push -u origin core
```

**Founding files (@Delta task — surgical, no judgment):**
1. Copy the 5 harvest files `~/.remote/harvest/{termbrana.project-definition.md,
   termbrana.execution-plan.md,termbrana.addendum-to-foil-theory.md,foil_theory.md,
   foil_plugin.rs}` → `termbrana/research/`, each gaining a provenance header
   (`source: ~/.remote/harvest · author: Wave r0 2026-08-15 | nabla (foil pair) ·`
   `adopted: flag L11 2026-08-15 · role: founding canon | research history`).
2. Move `../toolbox-termbrana-01-brief/evidence.host-versions.md` →
   `termbrana/research/evidence/host-versions.md` (leave a one-line "moved, safe to
   delete" stub behind — pad-builder orphan rule).
3. `termbrana/README.md` — short product line + **Governance section (A3, verbatim
   intent):** "Structural/topology/ownership decisions live in nablarva
   `.dev/session/flag.md` (L11). `DECISIONS.md` here holds product-technical ADRs only;
   every entry cites the flag line or session brief that authorized it. Sessions run in
   nablarva `.dev/session/toolbox-termbrana-*`."
4. `termbrana/DECISIONS.md` — ADR-0000: adoption record (cites flag L11 + session-01
   brief; pins zellij 0.44.3 · rustc 1.95.0 · wasm32-wasip1 · zellij-tile 0.44.3).
5. NO other pre-created architecture (execution-plan §2: "do not pre-create empty
   architecture"). Cargo workspace is born by the spike itself.

**Machine layer:** `[termbrana]="/home/hruzam/unikuklatrix/termbrana"` into
temple-project-map — **via the surgical table batch already staged** (pulse item E,
`~/ia-sync/zsh/`, @Delta fresh-read + `zsh -n`; one deploy covers nablarva + termbrana;
activation gate: deploy.sh + shell reload — awaits majkee).

## Part 2 — the truth spike (coding team)

**Integration owner: @Trajectory** (sole owner of shared conclusions; A4). Bounded probe
tasks may be dispatched to **@Astrobley** (report usage numbers) or @Delta/@Vector.
@Field melts bulky probe output into the evidence reports. Verification of "done" claims:
@Assay-class fresh eyes, not the writer.

Assignment = execution-plan **§12 verbatim**, with the pins already established:

- Host is LOCKED (PAD-01 green): zellij **0.44.3** · rustc **1.95.0** · target
  **wasm32-wasip1** · `zellij-tile = 0.44.3`. T0.1 = *verify and record*, not choose.
- Build the smallest compiling plugin for that exact host; commit exact build+load
  commands.
- Run probes T0.2–T0.5 (pane-content semantics · input behavior · geometry/rendering ·
  performance). Fixtures per plan §3. Epoch's open item folds into T0.2: diff the actual
  0.44.3 plugin-API surface (PaneRenderReportWithAnsi availability, permission names)
  against the docs — evidence, not docs-trust.
- Deliverables → `termbrana/research/evidence/`: five probe reports +
  `pane-content-matrix.md` + ADR-0001 (view/capture path choice, in DECISIONS.md,
  citing this handoff) + corrected M1/M2 backlog.

**Constraints (plan §12):** no NablaRava coupling · no global interception for observer
mode · no raw-capture/sanitization claims · no full VT parser · no production rewrite of
the foil skeleton.

**Return format (each coder):** files changed · exact commands + outcomes · evidence
paths · discovered API mismatches · recommended next task · remaining uncertainty.

## Gate (session 02 exit)

M0 deliverables on disk + @Assay-class pass → **host contract FROZEN** → session 03
(m1-core) may open parallel lanes (@Flight branch group per flag deferral threshold).
Anything blocked lands here + pulse; gates route to Houston, locks to majkee.
