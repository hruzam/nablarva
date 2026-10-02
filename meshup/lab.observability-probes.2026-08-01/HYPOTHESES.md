# HYPOTHESES — lab.observability-probes.2026-08-01

```yaml
updated: "2026-10-02"
writer: oraculum · Claude (registry fold; from cards D, E, G, H · Epoch 10-01/10-02 · majkee loops 1.1–1.4)
design: lab.observability-probes.2026-08-01
phases: [seam-probe-tailscale, stage-6-writeback, lab-7-gates, shadow-extractor, epoch-facts, onion-study, build-plan, termpanum-brief, events-map, vendor-catalogue]
open:
  - h1: "Stage 6 write-back over Tailscale — closed-loop verification; prepared, not run"
    src: raw.nablarva/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md
    gate: majkee go
  - h2: "OSC-133 semantic-prompt marks as a PTY-structure primitive — does any agent CLI emit them itself? tmux 3.8 hook events still rc"
    src: .dev/research/pty-community/pty-observation.prior-art.2026-10-02.md
  - h3: "EVENTS map ≤20 — are the 20 words sufficient for the 4 states across Claude Code · Codex · Gemini CLI (agy optional)? (docket 8)"
    src: .dev/research/termpanum-events/events-map.v0.2026-10-02.md
    gate: majkee confirms after first fixture
  - h4: "tmux pane↔PID join on pane_tty string is reliable enough for the anchor (vs Zellij's inherited $ZELLIJ_PANE_ID — study's verified 'easier target')"
    src: raw/terminal-onion.study.2026-09-17.md (§2.6, L583) · raw/card.G.onion-buildplan.md (§6 delta 2)
    fixture: hook $PPID → /proc/<pid>/stat tty_nr → tmux list-panes -F '#{pane_tty} #{pane_id}'; pass = unambiguous join on all live panes
  - h5: "Who writes the PreCompact checkpoint — cheap facts copy vs model self-summary ('Last Standing Man' anti-pattern)? Belongs to stridulatrix's context bus; must travel with it"
    src: raw/terminal-onion.study.2026-09-17.md (§6, L922)
  - h6: "Claude Code: does Esc-interrupt fire Stop? Is ~/.claude/sessions/<pid>.json (status busy|idle|waiting|shell) schema-stable?"
    src: .dev/research/vendor-events/vendor-events.catalogue.2026-10-02.md
  - h7: "Codex: do rollout JSONL files record approvals? can an interactive TUI attach to app-server (waitingOnApproval)?"
    src: .dev/research/vendor-events/vendor-events.catalogue.2026-10-02.md
  - h8: "Gemini CLI: when did hooks ship; Notification(ToolPermission) as the only waiting signal — fixture never run"
    src: .dev/research/vendor-events/vendor-events.catalogue.2026-10-02.md
  - h9: "agy: approval gap — waiting only by stall; cannot distinguish approval from slow tool. Fixture: trigger an approval, inspect transcript status + hook order"
    src: .dev/research/vendor-events/research.epoch.hooks-vs-pty-meaning.2026-10-01.md
  - h10: "Event envelope convergence with jev's jev.event/v1 (schema · event_id · sequence · at · session_id · kind · actor · data) — before jev implementation"
    src: .dev/research/termpanum-events/events-map.v0.2026-10-02.md (§0, §3) · POINT .dev/session/nablarva-X0-restarted/_bus/02.oraculum.point.md
    gate: majkee carries the POINT
  - h11: "Build plan §0.2 probes (hop count, tool-child wiring, command-pane env) rerun under tmux instead of Zellij — do the [INFERRED] flags close?"
    src: raw/build-plan.unilarvatrix.2026-09-18.md (§0.2)
confirmed:
  - claim: "tmux capture-pane cannot read Claude TUI transcript content (renderQueue noise); headless/JSONL is the clean channel"
    src: raw.nablarva/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md:47,53
  - claim: "The over-Tailscale read of home is not possible with the current method — no tmux, no tee on home."
    src: raw.nablarva/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md:47
  - claim: "Claude Code SessionEnd hook exists (33 events); on SIGTERM of `claude -p` it is the only hook that runs"
    src: .dev/research/vendor-events/vendor-events.catalogue.2026-10-02.md (H)
  - claim: "Codex SessionEnd missed 3/10 codex exec runs (#49003) — L0 backstop is load-bearing for exited"
    src: .dev/research/vendor-events/vendor-events.catalogue.2026-10-02.md
  - claim: "PermissionDenied (CC) fires only when auto mode denies — not on a human no"
    src: .dev/research/vendor-events/vendor-events.catalogue.2026-10-02.md
  - claim: "Scraping the PTY for semantics is strictly worse than subscribing; PTY yields bytes and liveness, never meaning (L2 merges stdout/stderr, OPOST rewrites, echo)"
    src: raw/terminal-onion.study.2026-09-17.md:205,435 · raw/card.G.onion-buildplan.md (§2)
  - claim: "Field pattern across nine public tools: hooks first, on-disk records second, screen last; none reads state off the screen"
    src: .dev/research/pty-community/pty-observation.prior-art.2026-10-02.md
refuted:
  - claim: "agy has no known hook surface (termpanum brief #gate wording)"
    src: .dev/research/vendor-events/research.epoch.hooks-vs-pty-meaning.2026-10-01.md — 5 hooks exist (PreInvocation, PostInvocation, PreToolUse, PostToolUse, Stop)
  - claim: "Stop building the PTY tap if hooks cover all states (termpanum brief #gate)"
    src: flag.md L14 D1 (majkee 2026-10-02) — struck; the PTY tap is the base, hooks enrich
next_probe: "h4 + h11 together — one fixture session under tmux on office: build-plan §0.2 probes + pane_tty join; result → raw/report.<date>.probe-results.md (study's own convention)"
expected: "[INFERRED] flags in the study close to [MEASURED] or [REFUTED]; h4 answered; EVENTS map v0.3 → v1 candidate; docket 8 ready for majkee"
```
