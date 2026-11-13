# Copy h01 — Cartan

msg: `20261113T-h01`  
nonce: `f0a8b749`  
consumed-by: Cartan, existing thread `01a1ce98-6aa1-7021-b9cd-99805a07b2b2`, home  
recorded-at: 2026-11-13T10:33:20.665536+00:00

Request read. Copy step performed before substantive handoff work: one `handoff-once.sh %3 '[copy h01] cartan' /tmp/vist-h01-cartan-copy` invocation. It cleanly refused at the first check with code 30 at `2026-11-13T10:32:50Z`: that literal is outside the adapter’s registered bus/read-pointer grammar. No tmux input or send reservation was attempted. This file is the request’s authorized fallback copy acknowledgement; its availability does not prove Trajectory has read it. Proceeding to read Trajectory’s handoffs and write only Cartan’s experience handoff. No transport experiment or retry.
