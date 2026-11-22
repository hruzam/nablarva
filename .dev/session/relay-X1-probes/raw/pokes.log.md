---
kind: poke log of relay-X1-probes — every coordination poke, with what it proves and what it does not
by: lead · started 2026-11-22
rule: one entry per poke. UTC before and after, the exact line, the exit code, what was looked at first, what it proves. Queued is not read. A probe try of the handoff is not a poke and is not logged here.
pattern: /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/pokes.log.md
---

# Pokes

## p01 — lead → oraculum · `codex queue`
- file first: `_bus/01.lead.point.md`, committed in 3ae987c
- looked first (2026-11-22T05:48:48Z): pane %60 — codex in the foreground, not dead, input row empty (placeholder only), no dialog; footer thread id 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1, idle
- call: `codex queue --thread 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1 --message "<line>"`, without `--resume`
- line: `[poke p01] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/01.lead.point.md — opposing read of the read-back sheet; return by file, no bell`
- before: 2026-11-22T05:48:59Z · after: 2026-11-22T05:49:00Z · exit code: 0
- output (first line): `Queued message 01a201cc-f95b-7d32-9dcb-d57fa794d1ba for thread 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1.`
- proves: the queue accepted the call, if the exit code is 0. It does not prove that the line was read.
- read is shown by: `_bus/01.oraculum.return.md`, or by work in pane %60

- p01 outcome: read — her RETURN was on disk by 2026-11-22T05:50:07Z (file time 05:49Z); REVISE, eight points; checked in `_bus/01.lead.verdict.md`.

