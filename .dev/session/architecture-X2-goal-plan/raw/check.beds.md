# check.beds — 13 open beds, enter / merge / stop (read 2026-11-27, read-only)

Method: each bed's RUNBOOK front matter + STATUS.md (checkpoint, in_flight, holds, next). Evidence folders not read.
Host: "office" = hruzam-120922. A bed marked office cannot be entered from home (this host).
Areas: (1) relay tests Claude<->Codex · (2) terminal observation + first consumer · (3) hcom review · (4) continuity / documentation routing.
"stop" = propose to Majkee that he closes the bed. Only he can do it (STOP/GO is his).

| Bed (idle days) | What it is for | Owner (seat, vendor, host) | Real state | Waits for | Areas | Rec. | Reason |
|---|---|---|---|---|---|---|---|
| muticula-01-qualify (56) | Test which raw git commands the native permission rules of Claude Code and Codex really block, before muticula (a git-guard tool) exists. | trajectory (Claude), cartan (Codex); office | Plan r3 and a 122-cell run manifest written; no run started. POINT 03 to Cartan open since 2026-10-02. | Cartan's answer (another seat) — then Majkee picks the runner session | none | stop | No product depends on it; 8 weeks silent; its question is about muticula, not about the plan's four areas. Reopen only if muticula returns. |
| nablarva-02-pipe-qualification (52) | Test whether one running Codex session can receive an operator-triggered task and return a matching answer (the first "pipe"). | oraculum (Claude), cartan (Codex); office | Cycle 03 closed (offline tests pass, 9). Sitting 1 never begun. STATUS last written 2026-09-14. | Majkee's one-line `open_approval` (STATUS `next`) | (1) strong: same question as relay tests | merge | Its gate is the relay delivery test the plan wants, but older than the relay-X2 verdict (REFUSE of the program). Move its offline code and findings into area (1) in the new worktree; close this bed. |
| ovitmugen-01-basement (41) | Extend ovitmugen (tmux session manager): remembered beds, tab jumps, swappable halves, a session map others can read. | trajectory (Claude); office | Authored only. "Nothing of 01 is built." Baseline selftest OK. | Majkee wakes a fresh Trajectory (prompt-0) | (2) partial: its "v1 map" is the address registry X5 needs | merge | X5 says ovitmugen writes the address registry on `ov-up`. Treat that piece as a step of X5; the rest (keys, presets) is UI, not in the plan — keep it unopened. |
| composer-01-parse (36) | Parser for a packet grammar (the "composer") with Phase 0 test corpus. | cartan (Codex); office | Phase 0 PASS, cycles 37/38 accepted, everything committed (745d732). PARKED by Majkee 2026-10-22. | Reviewed outcome of X3 AND Majkee's next word | none | stop | Its gate is met and preserved; nothing to do until X3. Close it as done-and-parked; open a new bed when X1 composer work resumes. |
| architecture-X1-bookkeeping (22) | Write the docs (ARCHITECTURE r8, 2 other docs, one flag line) so later beds build on canon. | cartan-x1 (Codex); office | GATE COMPLETE: Majkee GO, commit cb08d6f holds the 3 docs + flag. in_flight none. | Majkee's closure word only (and pulse-row removal / prune) | (4) a little | stop (close) | Work is finished. Only his closing word is missing. This also frees X5. |
| nablarva-X5-spine-slice (22) | Smallest build of the shared "observation record" (what each session shows) plus one reader — read-only, writes nothing into any session. | cartan-x5 (Codex); office | Authored 2026-10-24, "no seat has entered", no code, no folder. | Majkee: disk name GO; opening a fresh Cartan with prompt-0. Hold on X1 is now moot (see a) | (2) core: it IS the observation floor + first consumer | enter | This is area (2). Its only hold (X1 closes) is met in substance. Needs Majkee for the component name and the wake. Office only. |
| termpanum-X1-source-qualification (22) | Qualify capture of one synthetic tmux output source (bytes vs expected) — the "source" for any lab view. | cartan-termpanum-x1 (Codex); office | P1 accepted; P2 partial, BLOCKED: an interrupted host recovery command has unknown state; cleanup of one run unproven. | The working head (reconcile the half-run), then Majkee's runtime release | (2) partial: a capture source | merge | Fold into area (2) as the source test beside X5. First action is cleanup/reconcile, not new work. X5 says its consumer must not silently use it, so keep the line explicit. |
| phone-console-01-browser (22) | Use the tmux consoles from the phone browser (Redmi). | cartan (Codex); office | Live pilot working over USB loopback; many tests pass; native approval, Czech keyboard, remote route unqualified. | Majkee "resume" (explicit pause) | none (a consumer, not observation) | stop | Paused by him; not in the plan; route is USB-only. Close it as a working pilot, or leave paused — I judge it outside this plan. |
| termbrana-M0-markdown-test (14) | Turn Codex and Claude session transcripts into markdown views in Sublime, with bookmarks and cache. | Cartan (Codex); **home** | 70 tests pass; home synthetic walk done; native Claude follow-up (PAD step 28) pending. | Majkee: close Claude test views, send the follow-up | (4) strong: transcript routing = continuity | enter | Newest real work on the home host and nearest to a gate. Finish it; it is the base for continuity. |
| documentation-X1-organ-discovery (8) | Find which sessions and docs govern each organ, using Termbrana. | cartan-docs (Codex); host hruzam-120922 (= office) | Packet and independent repeat complete (83 inputs, PASS). | Majkee GO or STOP on the packet, then choose navigation owner | (4) core | enter | Waits only for his word. It is area (4). Office host — packet is files, readable from here. |
| sublime-observer-X1-file-publish (8) | Sublime publishes the open file text and state to a path, so Claude and Codex can read it. | oraculum (Claude), codex-auditor; **home** | Code frozen v1.1, 107 tests, audits done; smoke pending. | Majkee installs 1.1, walks SMOKE.md, says "smoke done" | (2) a first consumer of an observation record | enter | Closest to the gate, home host, a real consumer. Only Majkee's smoke is missing. |
| terminal-workspace-X0-approaches (3) | Preparation packet for a shared human+agent terminal (alternatives, one next experiment). | cartan (Codex); home, transferred to office | REVISE from Claude colleague; no VERDICT; X1 not released. | Cartan on office writes the VERDICT; then Majkee | (2) overlaps | merge | Same ground as area (2) and session-window. Fold its open choices into the observation plan; do not open a separate X1. |
| session-window-X1-surface (1) | Show status (model, usage) of Claude and Codex sessions: test 3 display routes on a separate tmux server. | lead.seswin (Claude), audit.seswin (Codex); **home** | Step 1 written; sheet draft 2 passed assay; parked, no run. | Majkee: how he reads the sheet; sandbox release (hold, STATUS lines 39-41) | (1)(2) both | enter | Live, newest, home. Its sandbox test server is the one area (1) needs. Needs his release first. |

Counts: enter 5 (X5, M0, documentation-X1, sublime-observer-X1, session-window-X1) · merge 4 (nablarva-02, ovitmugen-01, termpanum-X1, terminal-workspace-X0) · stop 4 (muticula-01, composer-01, architecture-X1, phone-console-01).

## (a) Dependency chains
- X5 waits for architecture-X1: `nablarva-X5-spine-slice/STATUS.md:29`; `RUNBOOK.md:39` says only to carry an X1 dependency row, "do not wait silently". The hold is met: `architecture-X1-bookkeeping/STATUS.md:7` GATE COMPLETE, cb08d6f; `docs/ARCHITECTURE.md:3` says r8. What remains is Majkee's closure word (X1 STATUS:64) — a formality, not a technical hold.
- X5 also waits for Majkee: disk name GO, fresh Cartan wake (`X5 STATUS:34-36`).
- X5 needs ovitmugen to write the address registry on `ov-up` (`X5` goal, pulse row 15) — ovitmugen-01 STATUS `next` is unbuilt.
- X5's consumer must not use termpanum silently: `termpanum-X1 STATUS:36` ("coordination goes through Majkee").
- composer-01 X1 waits for X3 outcome and Majkee: `composer-01-parse/STATUS.md:32`.
- sublime-observer-X1 must not touch termbrana-M0 or sublime-observer X0: `sublime-observer-X1/STATUS.md:54`.
- session-window-X1 shares the sandbox tmux server with a "group 2" (`sandbox-terwor`) — `session-window-X1/STATUS.md:43,53`; group 1's sole use is not yet in his words.

## (b) Beds waiting only for Majkee's word
- architecture-X1: "close the session" (+ pulse row removal; prune is separate).
- documentation-X1: GO or STOP on the packet; then name the navigation owner.
- sublime-observer-X1: install 1.1, walk SMOKE.md, say "smoke done".
- termbrana-M0: close the Claude test views, send PAD step 28 follow-up.
- nablarva-02: the `open_approval` line (but I recommend merge, so not needed).
- phone-console-01: "resume" (explicit pause).
- session-window-X1: how the sheet reaches him; then release of the sandbox.
- X5: disk-name GO and the wake. composer-01: his next instruction after X3.

## (c) pulse.md vs bed files
- pulse row 14 lists architecture-X1 as open; its STATUS says gate complete since 2026-10-25.
- pulse row 13 (composer-01) gives gate "Phase 0 exit finding, brief §3"; STATUS says PARKED, Phase 0 PASS. The router hides that it is parked.
- X5 STATUS says "No seat has entered", but `termpanum-X1/STATUS.md:11` names `nablarva-X5-spine-slice/raw/handoff.entry.cartan.2026-10-25.md` — a handoff file exists (not opened by me; existence taken from that line).
- nablarva-02: last folder commit 2026-10-06, but STATUS `updated` is 2026-09-14 — the folder was touched by an unrelated broad commit ("updates for nabla, symmetry, wave..."), so "52 days idle" is real, the date is not bed work. Same may hold for other beds.
- pulse says nothing of hosts. Host label is mixed: `hruzam-120922` = office, `home · hruzam` = home; terminal-workspace-X0 has both (STATUS:6).
- Pulse holds 13 rows + this bed; STATUS dirs on disk also include nablarva-X2-builder-narative, termpanum-X0, relay-X0/X1/X2, vist-X0, etc. not in pulse (closed or out of scope; not checked).

## (d) Not read
Evidence folders (raw/, _bus/, runs/), all RUNBOOK bodies beyond front matter/goal/participants, STATUS below the first lines of long files, `relay-X.ledger.md`, flag.md, the relay-X2 verdict, observations, `.hlm/`, `.majkee/`, CACHE files. No test or probe re-run. Chosen enter/merge/stop is my reading of STATUS text, not verified on the hosts.
