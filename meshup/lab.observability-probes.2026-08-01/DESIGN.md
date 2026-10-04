# DESIGN — lab.observability-probes.2026-08-01

`scope: the research laboratory → termpanum: controlled capture, extractor replay, cross-host read discipline, 7-gate promotion; since 2026-10-01 the read-only ear on living CLI sessions and the FIRST BUILD (L14 D1 plan).`
`status: live · name termpanum (L13) · toolbox at toolbox/termpanum/ (brief 10-01) · research gate relay-00-research precedes any RUNBOOK (L14 D4) · origin 2026-08-01`
`lineage: larva-lab (doc 04, 08-05) → onion study + unilarvatrix build plan (Nabla, 09-17/18) → termpanum brief (symmetry × majkee, 10-01) → EVENTS map (10-02)`
`sources: raw.nablarva/ (prefix rule) + raw/ (born inside this design, origin headers) + .dev/research/ (cited). Composed from cards A, D, E, G, H + Epoch 10-01/10-02.`

## Shape

**PTY is the base stone (L14 D1).** The lab taps every layer of the onion but owes nothing to any vendor: L0/L1 (liveness, death, exit codes — facts), L2/L3 (bytes moved, viewport changed, stalls), L5 (hooks and on-disk records — meaning, where the vendor offers it). Rule 1 of the study: tap high for meaning, low for liveness; never approximate one with the other (study:80). Toward the relay the lab says only `idle · working · waiting · exited` (L14 D3, docket 8), never what the screen means.

Laboratory separated from production; a rule leaves the lab only through doc 04 §4.12's seven gates. — `raw.nablarva/oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md:181,313`

**Struck 2026-10-02 (majkee):** the termpanum brief's `#gate` ("stop building the PTY tap if hooks cover all states") — it made the vendor-invariant floor conditional on vendor features. Replaced by L14 D1: the PTY tap is built; hooks enrich. Epoch 10-02 evidence that sealed it: Codex `SessionEnd` missed 3/10 clean exits (#49003); hooks never fire on `kill -9`; agy has no approval hook. The backstop is load-bearing, not belt-and-braces.

## Multiplexers (loop 1.4, majkee 2026-10-02)

One `mux` word in the event envelope, **one adapter per multiplexer** — the same rule as one adapter per vendor. tmux first (where the agents live: `agentive` sessions, ovitmugen); Zellij second through termbrana's knowledge (M0: plugins never see raw_pty; `zellij subscribe` since 0.44). A third backend is a slot, not a design. Cost recorded, not hidden: under tmux the pane↔PID join is a `pane_tty` string match; under Zellij the hook inherits `$ZELLIJ_PANE_ID` — the study's verified verdict "Zellij is the easier target" (study:583) stands as a fact; tmux-first is an operational choice → HYPOTHESES h4.

## Phases

| phase | origin | state | source |
|---|---|---|---|
| Seam probe over Tailscale (stages 1–5 run) | 2026-08-01 | live | `nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md` |
| Stage 6 write-back, closed-loop verification | 2026-08-01 | prepared, gated on majkee go | same |
| Laboratory + 7-gate promotion path | 2026-08-05 | live | `oraculum-basic-triangulation/04_LABORATORY…md` |
| Shadow extractor deployment | 2026-08-05 | fork C | `…/05_DECISION_LEDGER…md` |
| Epoch observability facts (hooks, PTY libs, OSC-133) | 2026-08-07/08 | 5 gaps → 3 closed | `_preflight/research.web.epoch*.md` |
| **Terminal onion study** — L0–L5 map, observability matrix, three rules, taps per multiplexer, lens rack, context bus (ch. 6 → stridulatrix) | 2026-09-17/18 | live, the formal PTY research | `raw/terminal-onion.study.2026-09-17.md` (origin ia-sync) |
| **unilarvatrix build plan** — phases 0–4; sh+jq v0, Rust only for picker/board; v0 buildable with zero compilation | 2026-09-18 | adopted with delta (name, home, tmux, format, context bus out) | `raw/build-plan.unilarvatrix.2026-09-18.md` (origin ia-sync) |
| **termpanum brief** — axioms #ax1–6, invariant EXPECT→TRIGGER→OBSERVE→COMPARE, taps, outputs, access, storage, PAPERS; `#gate` struck | 2026-10-01 | SUBSTRATE for RUNBOOK, waits on relay-00-research verdict | `.dev/session/toolbox-termpanum-00-brief/raw/brief-substrate-for-RUNBOOK.termpanum.2026-10-01.md` |
| **EVENTS map v0.3** — 20 events · 4 states · envelope; vendor tiers | 2026-10-02 | DRAFT, docket 8 | `.dev/research/termpanum-events/events-map.v0.2026-10-02.md` |
| Vendor event catalogue + PTY prior art + jev | 2026-10-01/02 | research, (S) rows capped M | `.dev/research/vendor-events/` · `.dev/research/pty-community/` |

## Boundaries

LAB/observability · stage 2 cross-host · Claude↔Codex seam (vendor-neutral read; hooks are sources, never words) · feeds room.brokered-journal / stridulatrix only through the 7 gates and only as discrete states · extraction.driller-onion is the meaning-from-PTY fallback this lab measures, not owns · context bus (study ch. 6) belongs to stridulatrix.

## Sources (5 archived + 4 own)

- raw.nablarva/oraculum-basic-triangulation/04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md
- raw.nablarva/nabla-buffer-brideAndBook/test.seam-probe.atlas-over-tailscale.2026-08-01.md
- raw.nablarva/nabla-buffer-brideAndBook/report.seam-probe.2026-08-01.md
- raw.nablarva/_preflight/research.web.epoch.2026-08-07.md
- raw.nablarva/_preflight/research.web.epoch.delta.2026-08-08.md
- raw/terminal-onion.study.2026-09-17.md — copied 2026-10-02 from ~/ia-sync/.dev/session/voice-meetings-01-threshold/meeting-themes/onion-terminal/ (origin header inside; ia-sync keeps its original)
- raw/build-plan.unilarvatrix.2026-09-18.md — copied 2026-10-02 from the same ia-sync folder (origin header inside)
- raw/card.G.onion-buildplan.md — Field card, 2026-10-01 (study × plan × brief delta check)
- raw/card.H.event-vocabularies.md — Field card, 2026-10-02 (doc 04 §4.13/§4.15 × hooks × taps)

Pointers (not copied): .dev/session/toolbox-termpanum-00-brief/raw/brief-substrate-for-RUNBOOK.termpanum.2026-10-01.md · .dev/research/termpanum-events/ · .dev/research/vendor-events/ · .dev/research/pty-community/ · raw.nablarva/old-but-good-onion/ (the June "old onion", 183 lines — a different, earlier document; owned by extraction)
