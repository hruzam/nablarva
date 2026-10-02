---
decisions: relay · PTY layer · phone lens
date: 2026-09-30
append-to: the project decisions file (append-only)
legend: DECIDED = majkee said it · PROPOSED = Symmetry, strike or keep
---

## 2026-09-30 · relay

- **D1 · PTY is the base layer for session relay — DECIDED**
  Every CLI runs in a terminal, and the terminal doesn't move with vendor features. Vendor doors (Claude channels, `codex queue`, ACP) parked until the vendors' bigger shifts.
  Boundary, PROPOSED: PTY as impulse layer is not "full PTY orchestration as architecture". Relay-seam v2 rejected that, and it stays rejected.

- **D2 · Finding: only bad solutions on the table — DECIDED**
  Every transport available today is bad somewhere: preview flags, per-vendor doors, a retired CLI, TUIs that shift under a parser. Consequence: the file plane stays the spine and no transport becomes truth ("files are more safe").

- **D3 · Discrete states, never comprehension — PROPOSED (passed under "everything is fine"; confirm)**
  The PTY parser, and any cheap model reading windows later, classifies (idle · working · waiting · exited). It never interprets screen content. Precedent: Ommatermia's description-not-pixels. Crossing it trips the kill test.

- **D4 · Research before build, in nablarva — three parts DECIDED · canon mapping PROPOSED**
  Parts: prior-art sweep → formal PTY research → tracker builder draft.
  Mapping per res/research.md: one `relay-00-research/` session (wheel · overengineering · vendor-harness → REINVENT / ADOPT / REFUSE); PTY research and tracker draft open after the verdict as `relay-01-pty` and `relay-02-tracker`.
  Rejected: three independent siblings before a verdict. Symmetry's first proposal; it duplicated the gaveled gate.

- **D5 · Phone is a thin lens; the session lives on the server — DECIDED**
  Compute, state and sessions stay on the workstation; the phone renders and types over Tailscale. Attaching is advisory (presence-board class); detaching never closes the bed.

- **D6 · Phone reach is app-scoped — vault DECIDED as a later extension · rejection PROPOSED**
  A session may ask the app to switch views inside an app-owned vault the operator scoped.
  Rejected: device-scoped access — a CLI reaching Android functions outside the app over Tailscale. Agent reach on a personal device; blast radius.

- **D7 · Blind triangulation before lock — DECIDED**
  Two blind briefs to Asymmetry: research and architecture. Neither carries Symmetry's conclusions. Termination per triangulation canon: a committed answer plus a falsifier, never consensus.
