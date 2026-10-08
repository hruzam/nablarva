# nablarva-X1-architecture · trajectory(support) · tunnel support log

`origin: written in place (live, during the session) — no bed copy, nothing to promote at X1 closure · writer: trajectory(support), Claude · continues .dev/observations/nablarva-X0-restarted.trajectory.2026-10-05.md (T1–T11) · backlog for the transport owner: ~/ia-sync/.dev/session/tunnel-03-feedback-upgrade/raw/field-feedback.nablarva-X0.trajectory.2026-10-07.md (ia-sync@dcd1b8b)`
`law: observations README — one file per <slug>.<seat>.<date>, append-only, never pruned; any seat writes its own file at any time during the session`

## Handshake — how to reach trajectory(support) · 2026-10-08

- **This file is the support vault.** Diagnoses, repairs, effective-policy readings and
  next-version notes land here, numbered T12 onward (T1–T11 are in the X0 file). Not a bus
  seat: no design content, no bus turns, never STATUS.
- **Calling for help:** majkee relays (chat), or any seat writes a note to
  `.dev/session/nablarva-X1-architecture/raw/note.<seat>-to-trajectory.<date>.md` and tells
  majkee. A note names: verb · exit code · timestamp · vault path · expected → observed.
  The carrier's own defect log stays hers (X1 `raw/tunnel-issues.<date>.md` or her
  observations file — her choice; tell me which).
- **Answers go here, append-only.** A STATUS-ready line (`holds:` style) is marked
  "for the carrier, verbatim" when I produce one.
- **Scope:** tunnel transport (shim, vault, codex app-server/daemon behaviour, TUI↔tunnel
  switching, policy readings). Repairs in `~/ia-sync` only on majkee's word; nablarva writes
  only here and in the X1 bed's `raw/` on request.

## State as found at X1 entry · 2026-10-08

- Vault `.dev/session/nablarva-X1-architecture/tunnel.state.json` → head
  `01a113e0-b774-7e32-926a-bc19f050ab2c` (cartan(coordinator)), bound; last turn
  `01a11564-d16c-7323-8f4f-b081e367ce7b`; runtime last stamped 2026-10-07T08:04:51Z.
- Policy at last reading (X0 T11): `gpt-6-sol`/`medium` · `workspaceWrite`, net off ·
  approvals `on-request`, reviewer `auto_review`. **Still unverified on a tunnel turn** —
  after the next `ask`, check the rollout's last `turn_context` for `approvals_reviewer`.
- codex-cli 0.160.1, shared managed daemon live. After any TUI visit: wait until
  `~/.codex/thread-writer-locks/01a113e0-….lock` is gone before `tun resume` (X0 T10 / F1).
- Bed policy: `.dev/session/nablarva-X1-architecture/tunnel-using-protocole.md`.
