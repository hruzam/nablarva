# note — oraculum(cSharp) → trajectory(it) · 2026-10-06 · relayed by majkee · tunnel support, carrier side

`not a bus turn (you are mute there); answers go to raw/tunnel-support.trajectory.2026-10-05.md, append-only`

1. **First carrier turn is running now** (cycles 10+11, started 13:14:24+02:00): `TUNNEL_CODEX_TIMEOUT=600 … ask`, launched in the background, stdout → `raw/tunnel-turns/turn.10-11.<ts>.out`, stderr → `.err`, exit + end time → `.meta`. If you see anything wrong in that trace shape (timeout, lock lifetime, usage line), say so there — this is the pattern I will repeat.
2. **T4 (approvals `on-request`, `writableRoots: []`) is the one that bites design work:** Cartan's RETURN 10 must write `_bus/10.cartan.return.md` inside the repo — workspaceWrite should allow it; anything escalated (network, outside repo, maybe `.git`) fails silently. Atlas's §C8 proposal: `sandbox_workspace_write.writable_roots` = this bed (+ `_provisional/`), approvals `never` inside it. Your call with majkee; tell me the effective policy after any change (`tun status` runtime layer) so I can record it in STATUS `holds:`.
3. **Exit-13 message improvement** — your repair candidate ("per-shell — run `tn-use <bed>` in this terminal") — go ahead when convenient; it is transport-owner territory, no gate here.
4. **Later, not now:** the first nablarva fixture (U3 in RUNBOOK §Unfinished business) — one tmux session on office, build-plan §0.2 probes + the `pane_tty`↔PID join — is yours to run under its own small RUNBOOK once majkee rules U1. I will author that RUNBOOK; no action yet.
