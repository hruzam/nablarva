# X1 — carrier observations (oraculum(cSharp), 2026-10-07 … 10-22)

`seat: oraculum(cSharp) — X1 head, carrier, STATUS owner · append-only, never pruned · bed: .dev/session/nablarva-X1-architecture/ (NOT closed — checks 4–6 continue in X3) · companion: nablarva-X1-to-X3-arc.agol.2026-10-22.md (the arc synthesis), germline-06 raw/feedback.houston-install.oraculum.2026-10-21.md (germline lessons)`

What running this session taught about running sessions. Faults are mine unless named.

## Carrier faults (mine)
1. **YAML parse failures in STATUS** — unquoted `: ` inside plain list items, repeatedly; caught only because a parse gate ran before commit. Rule kept: validate every STATUS write with `python3 -I` yaml (via a spawn — carrier python is hook-blocked).
2. **Lock check run in parallel with the send** (cycle 11) — the check must precede the turn, never share its tool batch. Happened to be clear; no harm, still a fault.
3. **Wrong commit trailer for spawns** — I copied my own `Co-Authored-By: Opus` into a Haiku delta's brief (reposoma 63a11a2). Name the model that actually commits.
4. **Instruction carried a stale line** — the X3 sitting prompt kept "reader spawns allowed" from the pre-loader prompt while the binding said "never spawns" (caught by Agol, fixed 7151611). Re-read inherited prompts against the latest gavel before handoff.
5. **Wrong status claim** — told majkee cartan was "on loan" to trajectory; it wasn't. Corrected in STATUS. Don't assert seat state from memory.
6. **Over-reach in a brief** — asked delta to make the tunnel preamble line 1 generic (my own extra, not in the approved change); the classifier denied it. Keep briefs to the approved scope.
7. **Wrong framing in a POINT** — POINT 03 conflated consult with the profile route; cartan corrected. A POINT is cheaper to get right than a RETURN is to fold.
8. **Echo into an ordered journal** — majkee: "logs have some order, spawn somebody". Ordered files are written by a spawn that reads the file's rules, never `echo >>`.

## Carriage that worked
- POINT file first, one line + absolute path on the wire, RETURN saved to `_bus/` before any claim (cycles 03–15).
- Fresh-eyes witness from RAW transcripts, not operator notes (assay on C1–X2, R1–R2, C-def.*, COEX) — it overturned two false fails (dropped stamps were relay loss, not Houston's).
- Verbatim relay between majkee and a seat; `to-<seat> from-<seat> --- … ---` human relay convention.
- Stop-on-unexpected in spawns (delta stopped on an extra dry-run file; it was expected, but stopping was right).
- Never routing around a denial (hook, classifier) — surface to majkee, let him decide.
- Context hygiene for the tunnel: preamble + targeted asks kept the fresh Cartan at 10–21 % over five cycles.

## Structural notes for the next head
- Carrier Bash is bookkeeping by hook; subagents are exempt (agent_id). Agent-config deploys may still need majkee's hands (permission classifier).
- `deploy.sh` ships the working tree, not commits — another seat's untracked files went live once (zsh/termbrana, majkee's own, harmless). Check `git status` of ia-sync before a full deploy.
- One-off exceptions granted in chat must be written to their law file the same turn (e.g. trajectory as tunnel driver, 2026-10-17) — otherwise they live only in the transcript.
- X1 is open: do not prune the bed before closure; its _bus/ and raw/ are evidence for X3 and the post-promotion audit.
