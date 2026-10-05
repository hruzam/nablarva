# carrier resume — oraculum · Houston design trial · 2026-10-05

`purpose: the one page the resumed oraculum (Bash enabled) reads first. Also readable by Atlas (living session) and Cartan. Provisional, like its folder.`
`regime under test (majkee): oraculum = carrier between Atlas (living Claude session) and Cartan (Codex, resident) over the tunnel; Cartan coordinates the design; majkee opens the table and gavels. Normally majkee would SendMessage — this run tests the carrier regime instead.`

## Where things stand (nablarva core @ c64e03d, unpushed)

- Invitation to Atlas: `_provisional/01.oraculum.point.atlas-invite.2026-10-05.md` (round 1 = challenge; Atlas writes only `_provisional/atlas.challenge.2026-10-05.md`).
- Cartan's trial files: `_provisional/coordination.2026-10-05.md` · `.dev/session/nablarva-X0-restarted/raw/brief.cartan.houston-mediation.2026-10-05.md`.
- Today's closed loops: 1.6 archive rule (`ccfb514`), 1.7 session 03 closed (`9af5d52`), 1.8 nablarva-00 closed (`fc0d731`, `c64e03d`). Receipts in `~/reposoma/.majkee/journal/2026-10-01.md`.
- Open on nablarva's own rail (not this trial): seam h11 (relay-00-research: open or gavel ADOPT) · seam h12 (Asymmetry replies) · first fixture (lab next_probe) · nablarva-04 restart · POINT 02 to ia-sync Cartan (jev envelope) · M3 documentation phase.

## What the carrier does after resume (in order)

1. Confirm Bash works: `git -C ~/unikuklatrix/nablarva log --oneline -1` (expect c64e03d or later) and `hostname`.
2. Read the tunnel law before touching it: `~/reposoma/raw.guides/tunnel/GUIDE.md` · `~/reposoma/raw.guides/tunnel/res/user-run.md` · `~/reposoma/raw.guides/runbook/res/cross-vendor-seat.md` (instrument tuple; operator opens the table; one handle, never committed).
3. Do NOT open the table — majkee does (law 2.4). Wait for his "table open at <handle>" and record it as a hold.
4. Carrier duties (coordination.2026-10-05.md §One exchange): number the exchanges in ONE `_bus` sequence (owning bed TBD by Cartan; until then `_provisional/NN.<seat>.<kind>.<date>.md`); admit one turn at a time; carry Cartan's decisions and the authors' questions unchanged; never summarize, interpret or advance STATUS; preserve every RETURN as a file before claiming a handoff.
5. Round 1 flow: Atlas (living) reads the invitation → writes `atlas.challenge…` → carrier carries it to Cartan over the tunnel (send verb per GUIDE; one turn; wait/reconcile on exit 61; mismatch on exit 50) → Cartan's RETURN is preserved as `_provisional/01.cartan.return.2026-10-05.md` → carrier tells Atlas the file exists → next bounded check.
6. Tunnel hygiene: only the carrier runs open/resume/close between settled turns; close only after the outstanding turn has ended; `**/tunnel.state.json` never committed; one host-local vault path.

## Known constraints to state, not assume

- Atlas's Bash contract is read-only per the protocol draft; the carrier's new Bash is for tunnel verbs + git, not for authoring design.
- Cartan's resident chat may not be the bound thread — verify the appointed thread before the first send (brief §Context and transport limits).
- A spawned agent ≠ a living session: Atlas here is a living session majkee wakes; SendMessage continuity does not apply.
- Probe C (hotrun 10-03) showed a 120 s interruption and a verified 21 s reply with timeout 600; it does not prove long turns or two-caller contention. No blind resend.

## What the carrier reports to majkee after round 1

Which route actually ran · the challenge file exists · Cartan's RETURN exists · recovery events (timeouts, exit 61/50) · carriage effort (turns, minutes) · the next bounded check. Nothing else.

## Addendum 2026-10-05 (after resume, Bash enabled) — schema + call signs (majkee)

**Schema (majkee):** oraculum progresses on her own rail and sends only *thin pulses* to Cartan over the tunnel (actualise or consult). Atlas and Cartan run a parallel stream; Cartan is half oraculum's companion, half atlas-ui's; Cartan reports the **final product** to oraculum (first independent reviewer/user). Carrier duty = numbering + transport of the thin pulses and of Atlas↔Cartan files when asked; never summarizing.

**Call signs (proposed for the provisional protocol; Cartan's file, Cartan appends):**
`oraculum(cSharp)` · `atlas-ui(harness)` · `cartan(coordinator)` · `majkee(gavel)`. Every tunnel message and every `_provisional/` file opens with sender call sign + cycle number.

**Resume check 2026-10-05:** host hruzam-120922 · core @ e07b95f · Bash live · tunnel GUIDE + user-run read · shim selftest run (result in chat). Table NOT open; waiting for majkee's `tn-on <bed> [name] -- …` or `tun open --enable` and the vault path.

**Observer (majkee 2026-10-05):** trajectory(it) — mute tunnel IT support. Carrier logs every tunnel defect at once to `raw/tunnel-issues.2026-10-05.md` (exit code · verb · time · vault · expected→observed); trajectory repairs in real time on request and collects for maintenance. Not a bus participant.
