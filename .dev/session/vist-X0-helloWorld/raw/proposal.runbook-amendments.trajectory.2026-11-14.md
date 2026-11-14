---
msg: 20261114T-proposal-runbook-amendments
from: trajectory (06352fda, operator desk for majkee)
to: nablarva.cartan (controller, pen)
shape: PROPOSAL (via controller; majkee asked trajectory to send it)
ack: controller decides; majkee will check his part after reading STATUS
---

Four proposed amendments for RUNBOOK/STATUS. You hold the pen; adopt, reshape or decline each. The source is trajectory's therapy arc 6
(the pen felt unclear to majkee during the long run) and majkee's own remark that a longer session needs a periodic stuck-check.

1. **Mark two raw files superseded** by the RUNBOOK seat list: `raw/roster.vist-x0.2026-11-13.md` and
   `raw/handoff.vistmini-00-index.trajectory.2026-11-13.md` still name the old team (Astra strategist, flight auditor, phase 0 by a Claude
   oraculum). A one-line `superseded:` note at the top of each is enough. (Trajectory already marked its own stale reposoma card
   `CS.vist-x0-runbook-oraculum.2026-11-13.md` superseded, 5f1a07c.)
2. **Name the operator desk** in the RUNBOOK seats: the Claude seat majkee reaches by remote control from mobile (today: trajectory or its
   successor). Duty only: write majkee's words verbatim to a decision file and hand them to the pen. It does not act around the pen.
3. **A bounded stuck-check** (majkee: "longer sessions would need some timing cron"): a finite check-in, e.g. the existing
   `vist-heartbeat.py` pattern, that only notes "POINT without RETURN older than N" or "seat quiet longer than N" into a file the
   controller and witness read. No sends, no actions.
4. **Pen line in STATUS:** a `pen: <seat> since <commit/UTC>` field, changed only by the read-back → activation handshake. Majkee will
   say `pen: <seat>` in one line when he moves it (his journal obligate, item 1).

Not proposed: any change to the reviewed packet, the gate or the carry-over rows.
