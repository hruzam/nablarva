---
kind: handoff
from: trajectory (claude, vistMini-01-tests builder; report author)
to: vist-X0 team + whoever writes its RUNBOOK
date: 2026-11-14
extends: handoff.vistmini-00..03 (2026-11-13). Read those first; this adds the long-run shift (cycles 09–22) and a team proposal.
outcome: majkee GO 2026-11-14, verbatim "scope narrowed, unrun cases go to vist-X0, GO". Transport prototype NOT released (L21).
companion: cartan's angle in handoff.vistmini-05-*.cartan.* (requested)
---

# vistMini → vist-X0, part 04: the long run, scars, and the team I would seat

## 1. Core: what we actually learned (one line each)

1. **Doors beat keystrokes.** `codex queue` into a Codex thread worked every time, busy or idle. Typing into a Claude pane needed version-specific screen reading and still failed whenever the receiver was mid-work (exit 29).
2. **The weak direction is into Claude.** Codex→Claude had only the tmux adapter. Claude `SendMessage` (cross-session) was seen once working (oraculum → trajectory, cycle 09). **First RUNBOOK task: qualify a native door into Claude.** Until then, ringing a working Claude seat is unreliable by design.
3. **Cross-vendor review is the best quality gate we had.** Cartan's review of my report found six overclaims (R1–R6) I could not see: wrong gate verdict, a guessed cause stated as fact, a missing operator intervention, a one-session observation generalised to the whole trial. Author and verifier must be different seats, preferably different vendors.
4. **Successor handover with read-back works.** Old Cartan → fresh Cartan: POINT → read-back file → verdict ACCEPT → activation → old seat goes read-only (cycles 16–18). Nothing lost, no double controller.
> **CORRECTION 2026-11-14 (trajectory), after cartan's handoff 05:** fact 5 below is wrong where it says the keeper recorded nothing.
> Keeper RETURN12 exists (`~/ia-sync/.dev/records/vist/2026-11-14/vistMini-01-tests/_bus/12.oraculum.return.md`): a per-seat context
> table and a card-due cadence. I missed it because I listed only bus files from 16 on. Also read 05's qualifications of facts 2, 3, 4
> and of the "Claude files, Codex shell" rule in §2/§3; 05 is the better-evidenced reference on those. The merged view is in majkee's
> journal (`~/reposoma/.majkee/journal/raw.2026-11-13.md` §1.2).

5. **A finite self-wake beats an external keeper.** Cartan's `scripts/vist-heartbeat.py` (one bounded check-in on a timer, lease file, stops itself) kept the controller moving. The Claude oraculum keeper did not produce any recorded advice I can find in the bus. Its rules blocked the transport (Bash hook), and it had no way to read others' context. Context % is visible in each pane's footer (Codex: "Context 57% left"; Claude statusline: "ctx 97% left"). Seats said they cannot see their own meter, but the screen shows it.
6. **Role ≠ tool permissions is a real failure.** Cycle 19 STOPPED: a read-only verifier was assigned to write a RETURN file. Check that each seat's tools can produce the artifact its POINT asks for, before dispatch.

## 2. Scars (therapy style: what hurt, what it taught)

| scar | what happened | rule now |
|---|---|---|
| **approval storm** | trajectory (Claude, auto mode) got operator prompts on compound shell commands (queue + pane paste + push in one call). Majkee on the other end had to click repeatedly | Claude seats get an allow-list **before** start; one step per call; Claude does files, Codex does shell and git push |
| **rebuild broke the resolver** | majkee rebuilt the tmux umbrella; agents now ran under `zsh`, window labels (`@seat @vendor @id @carrier`) were gone. Delivery refused 22 for every rebuilt seat | one launch script per seat: `tmux new-window … 'exec <agent>'` + set labels from the roster in the same script. Never by hand |
| **bell into a working seat** | both cycle-09 acks rang trajectory while it worked: 29, then the notice to the sender failed 22. Nobody woke | a bell is a hint, never the delivery. Head polls with its heartbeat; files are the truth |
| **writer's blindness** | my report said "MET" where the gate was PARTIAL, and "observed repeatedly" where I had no receipt | every claim names a file; uncited = "operator/author account, unverified" |
| **the sample lied politely** | permission sample said "no prompt was needed"; the screen showed one | receipts come from observation (screen, transcript, logs), never from self-report |
| **phone operator** | majkee on mobile saw only one session (mine) and relayed decisions through it | name one **operator desk** seat (the one with remote-control). It relays decisions verbatim into a `_bus/*.decision.md` file to the head |
| **context cliff** | trajectory ran at ~70% through the whole shift; Cartan compacted once with a cache file and survived | write the cold-start card at ~60%, not at 90%. Hand over by read-back (fact 4) |

## 3. Team I would seat for vist-X0 (my angle; cartan adds his)

| seat | vendor/model | job | must have |
|---|---|---|---|
| **head / controller** | Codex Sol (fresh thread) | POINT/VERDICT, STATUS, git push, heartbeat, /clear + re-entry of others | the only pen on STATUS and push; heartbeat armed |
| **builder** | Claude Opus (trajectory) | code and documents; report author | allow-list set before start; **no shell transport duties**; writes files, head rings |
| **verifier** | the other vendor from the author of the artifact | independent check, PASS/NOK per claim | can write its RETURN (scar: cycle 19) |
| **operator desk** | whichever seat has remote-control (today: a Claude seat) | majkee's mobile entry; relays decisions verbatim | nothing else; it is not the head |
| **sample-claude / sample-codex** | haiku / Luna, default permission mode | all disruptive and permission cases | launched by script as pane root; disposable |
| **strategist** | optional, outside the build | consulted by brief at gates only | no pointers per cycle |

What I would drop: a dedicated keeper seat. Fold it into the head's heartbeat plus a footer read. Keep it only if majkee wants a second pair of eyes on context, and then let it **write notes only**. Majkee already decided that on 2026-11-13.

Two seats fewer than today's 11 windows. Today we had a hot line (nablarva.cartan) and two successors idle most of the time. Spawn successors when the card is written, not in advance.

## 4. Tips for the first cycles of vist-X0

1. **Cycle 0: launch and label by script.** Then a read-only inventory: each seat's pane root, id, vendor, permission mode, context %. Commit it as the roster's filled version.
2. **Cycle 1: native-door inventory per direction**, on samples only: `codex queue`, Claude `SendMessage`, the tmux adapter as fallback. One message each, receipt by nonce.
3. **Carry-over cases (majkee 2026-11-14):** C10 unknown native view, agent exit/crash between text and Enter, expired or misaddressed requests, receiver semantic and hop limits. Register them **before** any run with expected values, as vistMini did in `reports/cartan.cases-08.2026-11-13.md`.
4. **Keep the POINT discipline Cartan used late in the run:** each POINT names the only files the worker owns, a word limit on the RETURN, "no stage/commit/push", one optional bell. That kept many seats in one checkout from colliding.
5. **Decisions from majkee go into a file verbatim** with the question he answered, then the head records them in STATUS.
6. **Don't build what a `--help` already gives.** vistMini lost three cycles on a door that `codex queue --help` would have shown on day one (handoff 02).

## 5. Pointers
- Trial report (accepted): `~/ia-sync/.dev/session/vistMini-01-tests/reports/trial-report.vistmini-01.md` (3584a02)
- Case table: `…/reports/cartan.cases-08.2026-11-13.md`; offline fixture inventory: `…/reports/vist.offline-fixture-inventory.2026-11-13.md`
- Controller tools: `…/scripts/vist-deliver.sh` v3.1 (prototype), `…/scripts/vist-heartbeat.py`
- Handover pattern: `…/_bus/16..18.*`; decision relay: `…/_bus/22.trajectory.majkee-decision.md`
