# HYPOTHESES — lab.observability-probes.2026-08-01

```yaml
updated: "2026-10-01"
writer: oraculum · Claude (cleanup-00-meshup; from card.D, card.E)
design: lab.observability-probes.2026-08-01
phases: [seam-probe-tailscale, stage-6-writeback, lab-7-gates, shadow-extractor, epoch-facts]
open:
  - h1: "Stage 6 write-back over Tailscale — closed-loop verification; prepared, not run"
    src: raw.nablarva/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md
    gate: majkee go
  - h2: "Is the Codex CLI hooks framework currently labeled experimental, beta, or stable by OpenAI, and if so where exactly is that label stated?"
    src: raw.nablarva/_preflight/research.web.epoch.delta.2026-08-08.md:121
  - h3: "OSC-133 markers as standard PTY-structure primitive"
    src: raw.nablarva/_preflight/research.web.epoch.2026-08-07.md (Topic 2)
confirmed:
  - claim: "tmux capture-pane cannot read Claude TUI transcript content (renderQueue noise); headless/JSONL is the clean channel"
    src: raw.nablarva/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md:47,53
  - claim: "The over-Tailscale read of home is not possible with the current method — no tmux, no tee on home."
    src: raw.nablarva/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md:47
  - claim: "claude agents/attach/logs/respawn/stop as background-session surface"
    src: raw.nablarva/_preflight/research.web.epoch.delta.2026-08-08.md:96,143
refuted: none
next_probe: none scheduled — this registry lists, it does not run (cleanup-00-meshup)
expected: n/a until a study session names one of h1–h3 as its gate
```
