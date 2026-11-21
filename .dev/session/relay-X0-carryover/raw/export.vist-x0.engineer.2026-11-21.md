---
kind: carry-over export (pointers and summary; the origin files stay where they are)
author: engineer (trajectory, claude d1ca16e9), host home
date: 2026-11-21
origin_bed: ~/unikuklatrix/nablarva/.dev/session/vist-X0-helloWorld   # short name in this file is O/
origin_revision: nablarva core 75227bc + three uncommitted origin edits that are not mine (see §2)
archive_of_trial: ~/ia-sync/.dev/records/vist/2026-11-14/vistMini-01-tests   # short name in this file is A/
read: all 45 files of O/ (root 3, _bus 3, raw 39) on 2026-11-21
status: UNVERIFIED by a non-author until cycle 01 closes (goal G2). A summary is a claim; the origin file wins.
---

# What the VIST X0 bed hands to the relay line

Use this as a map. When a line here matters to a decision, open the origin file it points to.
Nothing here releases an experiment, an implementation or a transport (L21).

## 1. One-paragraph story

vistMini (ia-sync, 2026-11-12/14) was an unplanned home-host trial: a Claude seat and a Codex seat exchanged bus pointers without
operator relay. Majkee accepted it on 2026-11-14 under a narrowed scope: "scope narrowed, unrun cases go to vist-X0, GO". VIST X0
(this origin bed) then did **paperwork only**: it re-read one old case (C04) to separate four meanings of "delivered", and it wrote a
plan for the six cases that were never run. That packet was reviewed (PASS) and the controller accepted the review. **Majkee's own
decision on the packet is still open.** No new experiment has run since 2026-11-14.

## 2. Position of the origin bed today (do not change it from here)

| Fact | Source |
|---|---|
| Gate OPEN: Majkee ACCEPT / REVISE / STOP on the reviewed documentary packet | O/STATUS.md `next` |
| Packet = RUNBOOK + 4 files, frozen by sha256 | O/raw/preparation.review-input.01.2026-11-14.json |
| Non-author review: PASS on 6 criteria | O/_bus/01.packet-review.return.md |
| Controller verdict on that review: ACCEPT (not operator acceptance) | O/_bus/01.nablarva-cartan.verdict.md |
| Pen: nablarva.cartan, Codex thread `01a1d582…`, moved to **office** 2026-11-19 | O/STATUS.md `pen`, O/raw/cache.controller-office.nablarva-cartan.2026-11-19.md |
| Operator desk: Trajectory `06352fda` (home), successor unbound | O/STATUS.md `operator_desk` |
| Outside witness: Claude `c266d10a…`, note-only, moved to office; no sweep ever called | O/raw/witness.host-move.2026-11-19.md |

Observed on home 2026-11-21 (mine, not in the origin files):
- O/RUNBOOK.md has an **uncommitted edit by Majkee** (the `goal:` line). The committed bytes still match the review hash `9081d353…`. If that edit is committed, the review no longer covers the file.
- O/majkee-personal-notes.md is untracked and his. `relay-X.ledger.md` and `vist-X.ledger.md` carry an uncommitted merge by myShell (Majkee's request, 2026-11-21).
- The X0 desk session `06352fda` is not running: its pane `%49` shows a shell. The `controller` window in today's tmux party is a **fresh** Codex thread `01a1ff5e…`, not the X0 pen.

## 3. What is established and what is not

| Claim | Class | Source |
|---|---|---|
| Three ordinary messages in each direction on one host, with independently checked reporting | **supported** (accepted scope) | ~/ia-sync/.dev/records/vist/2026-11-14/CLOSE.md |
| Codex→Claude 3/3 through the tmux keystroke adapter | supported, version-specific screen reading | O/raw/handoff.vistmini-01-evidence… §1,§3 |
| Claude→Codex through `codex queue --thread` (q01 first; three ordinary + scoped samples) | supported, **bounded** | O/raw/handoff.vistmini-01-evidence… §4; O/raw/handoff.vistmini-05-team.cartan… "Queue evidence has bounds" |
| Claude→Codex by tmux keystrokes | **failed 0/3** (29, 29, 27); cause is a hypothesis (paste window) | O/raw/handoff.vistmini-01-evidence… §2; O/raw/handoff.vistmini-cartan.cartan… |
| Codex→Codex native `send_message_to_thread` | stable on office; fails `-32600 active writer` when the thread is held elsewhere | O/raw/handoff.vistmini-01-evidence… §3 |
| Claude→Claude / Codex→Claude native messaging | **seen once**, mechanism not inspected; not a qualified route | O/raw/handoff.vistmini-04-longrun… fact 2; O/raw/handoff.vistmini-05-team.cartan… |
| Cross-vendor review found six overclaims (R1–R6) in the trial report | observed once; not a measured superiority result | handoff 04 fact 3; handoff 05 |
| Controller succession by read-back → acceptance → activation → uptake | observed once, **warm** successor | O/raw/readback.controller…, acceptance.controller…, activation.controller…, checkpoint.controller… |
| Six carried cases U01–U06 | **UNRUN / UNQUALIFIED** | O/raw/preregister.vistmini-carryover.cartan.2026-11-14.md |
| Cross-host anything · permission boundaries · reliability numbers · survival of a CLI upgrade | **not established** | handoff 01 §5 |

Three successes are a smoke test, not statistics. Queue acceptance, submission, a native turn, a file read, a worked receipt and
accepted work are six different observations (O/raw/cache.controller-office… "Review and coordination lessons").

## 4. The C04 lesson (why "delivered" needs four layers)

Source: O/raw/preparation.c04-timeline.2026-11-14.md. Same message type, two runs:
- **r1:** the carrier accepted the queued message and the work arrived, but the sensor said `ready` while the receiver was still busy. Carrier success, **observation failure**.
- **r2:** the sensor said `busy`, the queue accepted, the receiver took the turn later, the nonce matched.

Layers to keep apart: (1) native activity, (2) reported observation, (3) carrier acceptance, (4) receiver receipt. A later good receipt
does not repair an earlier wrong observation.

## 5. The six carried cases

Full rows, candidate bounds and proposed oracles: O/raw/preparation.qualification-matrix.2026-11-14.md (reviewed, frozen).
Original expectations: O/raw/preregister.vistmini-carryover.cartan.2026-11-14.md. Candidate reasoning for U03–U06:
O/raw/preparation.receiver-policy.2026-11-14.md (adopts nothing).

| ID | Case | Kind | Needs a live actuator? |
|---|---|---|---|
| U01 | Genuine unknown native view must stay "unknown" | observation / classification | no (fixture selection is read-only) |
| U02 | Receiver exits after the text, before Enter | actuator / lifetime | yes |
| U03 | Expired request is declined before work | receiver policy | controlled dispatch |
| U04 | Wrong recipient or unauthorised path does no work | receiver policy | controlled dispatch |
| U05 | Reading a pointer is not authority for its action | receiver policy | controlled dispatch |
| U06 | Hop and retry budgets end; no recursion, no duplicate work | receiver policy / controller | controlled dispatch |

The packet names its own first operation after acceptance: **one U01 fixture / missingness selection** — find whether a genuine
unsupported, redacted, lifetime-bound historical native view exists under a frozen signature set; report MISSING if not. It sends
nothing. Its exact file-access and redaction scope must be named in the assignment (matrix, last paragraph).

## 6. Doors per direction, and versions

| Direction | Door | Evidence class |
|---|---|---|
| Claude→Codex | `codex queue --thread <uuid> --message <one line>` (no `--resume`) | worked in the trial; queued ≠ read |
| Codex→Claude | tmux pane, look-first; adapter `bus-poke.sh` in A/scripts/ (archived, not live) | 3/3 in the trial; fails when the receiver is mid-work (exit 29) |
| Codex→Codex | native thread messaging | stable when the target has no other writer |
| Claude→Claude | native session messaging | seen once; untested here |
| state of a Claude seat | `claude agents --json` | documented, not qualified |
| state of a Codex seat | `read_thread` (Codex native) | used once for q01 |

Versions: trial ran codex-cli 0.167.2 / Claude Code 2.1.286 (handoff 01). The packet probed 0.169.0 / 2.1.323. **Home today:
codex-cli 0.171.0, Claude Code 2.1.330, tmux 3.7c.** No door has been re-checked on today's versions.

Lead from this session (untested): Claude Code session files `~/.claude/sessions/<pid>.json` carry `peerProtocol`, `peerFeatures`
(`notify_idle`, …) and a messaging socket field, plus live `name`, `status` (busy/idle) and the hosting `tmux` pane. That is a native
state probe and maybe a native door into Claude — the weak direction. Do not print the socket path or the `.key` files.

## 7. Rules that bind this line (pointer, never copy)

- **Locks:** `~/unikuklatrix/nablarva/.dev/session/flag.md` — L12 (core, plain pull/push, never rebase, serial owned-path Git), L14 (relay foundations), L20 (observation ≠ decision ≠ action), L21 (each implementation / activation / delivery / transport operation needs its own release), L22 (`.majkee/`, `.hlm/` sealed from agent reading).
- **Shared practice:** `~/reposoma/raw.guides/bus/GUIDE.md` (POINT / RETURN / VERDICT) and `~/reposoma/raw.guides/bus/res/file-poke.md` (provisional; write → poke → work → return → verify). The using session carries the retirement debt of file-poke.
- **Fallback poke "like sudo":** look first, label `[manual …]`, once, never after an uncertain send, record it — O/raw/decision.majkee.fallback-poke.2026-11-14.md.
- **Never retry or clear:** historical `t03` and `c08r1-05-ae3ee8e7` (home state file still present 2026-11-21).
- **No carrier switch after an uncertain submission** until the receipt is reconciled. One logical message id across carriers.
- **Author ≠ accepting reviewer.** Changed bytes after a review = a new review input.
- **Match role and output before dispatch:** a read-only seat cannot write a RETURN; plan its publisher, never impersonate (O/raw/plan.runbook-and-team… "Reviewer output contract").
- **Majkee's decisions go to disk verbatim** with the question he answered.
- **Disruptive cases run on disposable samples**, never on senior panes.

## 8. Scars → rule (short)

| Scar | Rule | Source |
|---|---|---|
| Three cycles on keystroke guards while `codex queue --help` existed | list every native door per direction before building | handoff 02 S1 |
| 40 stand-in fixtures passed, live failed | record live frames first, then write fixtures | handoff 02 S2 |
| Sensor matched the agent's own words in scrollback | anchor on bottom UI rows only | handoff 02 S3 |
| Head wrote a contradictory POINT | every POINT carries the bell rule explicitly | handoff 02 S4 |
| Agents under an interactive shell | start the agent as the pane's root: `exec <agent>` | handoff 02 S5; handoff 04 "rebuild broke the resolver" |
| A peer offered to execute for another seat | delivering pointers is fine; executing for another seat is permission laundering | handoff 02 S7 |
| Framework ate the task | seats keep task memory; keep helpers boring | handoff 02 S8 |
| Bell into a working seat woke nobody | a bell is a hint; the file is the truth; the waiting owner polls | handoff 04 §2 |
| A sample said "no prompt was needed"; the screen showed one | receipts come from observation, never from self-report | handoff 04 §2 |
| Read-only verifier asked to write a file (cycle 19) | check the seat's tools can produce the artifact | handoff 04 fact 6; handoff 05 |
| Context cliff at ~70% | write the cold-start card near 60%; hand over by read-back | handoff 04 §2 |
| One extra newline broke a frozen hash | hash the intended published bytes before freezing | handoff 05 |

## 9. Team shape that the two authors agreed on

O/raw/plan.runbook-and-team.cartan-trajectory.2026-11-14.md: one resident controller/integrator with the only STATUS pen; one resident
builder; a bounded non-author reviewer at acceptance edges; an outside witness that only writes notes; operator desk as a duty of the
seat Majkee reaches; samples only when a released case needs them; no idle spare successors; a finite timer only for an observed
wake-up need. Cartan's caution (handoff 05, last paragraph): do not build a generic resolver, launcher, envelope or permanent
orchestration layer merely because the trial used one.

## 10. Decisions still owed by Majkee (carried, not mine to make)

1. X0 packet: ACCEPT / REVISE / STOP. (O/STATUS.md)
2. `git push` runs without a prompt for every seat in ia-sync and nablarva; "only the controller pushes" is not enforced. Keep or restore the prompt. (O/raw/cache.operator-desk.trajectory.2026-11-20.md, owed #2)
3. Witness hook extras beyond the brief (`-L <name>`, short aliases). (same file, owed #3; O/raw/witness.host-move…)
4. Whether the fallback poke applies to the witness. (O/raw/witness.host-move…)

## 11. Tensions I see (engineer's view; not resolved anywhere in the origin bed)

- **T1 — L14 D1 against the trial's evidence.** L14 D1 says PTY is the base layer and vendor doors (`codex queue`, Claude channels) are "weather, parked". The trial found the opposite in practice: keystrokes into Codex failed 0/3 and the vendor door worked. Trajectory's kept disagreement is handoff 02 S9 ("PTY = sensor, receipts = truth, native doors = actuator where they exist"). Measuring doors adopts nothing; adopting one touches L14 and is Majkee's call.
- **T2 — two live beds on one line.** X0's gate is open while this bed starts. Rule I set for this bed: no U-case runs here until Majkee accepts the X0 packet or explicitly carries that case here.
- **T3 — today's party panes are shell-rooted** (`exec zsh -l`, then the CLI). If an agent exits, a typed poke lands in a shell. Look before every typed line.
- **T4 — evidence custody.** The eight local C04 inputs pinned by the packet live in `/tmp/vc08r1.tkz50zbf` and `/tmp/vc08r2.kk50sqqh` on home. Both exist today; a reboot loses them. The packet says hashes do not prove durable custody. Copying them needs Majkee's word (they are host-local, private material).
- **T5 — versions moved** since every recorded observation (§6).

## 12. Coverage map — every origin file

- **Live position:** STATUS.md · RUNBOOK.md (frozen; + Majkee's uncommitted goal edit) · majkee-personal-notes.md (his, untracked; I printed it once on 2026-11-21 before he said it was his; nothing from it is used here).
- **Reviewed packet (frozen by hash):** raw/preparation.sources.2026-11-14.json · raw/preparation.c04-timeline.2026-11-14.md · raw/preparation.qualification-matrix.2026-11-14.md · raw/preparation.receiver-policy.2026-11-14.md · raw/preparation.review-input.01.2026-11-14.json
- **Review cycle 01:** _bus/01.nablarva-cartan.point.md · _bus/01.packet-review.return.md · _bus/01.nablarva-cartan.verdict.md
- **Carried cases:** raw/preregister.vistmini-carryover.cartan.2026-11-14.md
- **Agreed plan and its consultation:** raw/plan.runbook-and-team.cartan-trajectory.2026-11-14.md · raw/consult.runbook-team.cartan.point… · raw/consult.runbook-team.trajectory.return… · raw/consult.runbook-team.cartan.followup… · raw/consult.runbook-team.trajectory.final…
- **Controller authority trail:** raw/readback.controller.nablarva-cartan… · raw/acceptance.controller.nablarva-cartan… · raw/activation.controller.nablarva-cartan… · raw/checkpoint.controller.nablarva-cartan…
- **Operator decisions:** raw/decision.majkee.fallback-poke.2026-11-14.md · raw/decision.majkee.witness.2026-11-14.md · raw/decision.shared-file-poke-relay.majkee.2026-11-19.md
- **Proposals and their disposition:** raw/proposal.runbook-amendments.trajectory… · raw/disposition.runbook-amendments.nablarva-cartan… · raw/feedback.controller.nablarva-cartan… · raw/check.stuck.nablarva-cartan.2026-11-14.json · raw/review.shared-file-poke.challenger.2026-11-19.md
- **Witness:** raw/brief.witness.trajectory… · raw/readback.witness… · raw/integration.witness.cartan… · raw/witness.host-move.2026-11-19.md
- **Trial experience (history, marked superseded where it names staffing):** raw/handoff.vistmini-00-index.trajectory… · -01-evidence · -02-scars · -03-runbook-substrate · -04-longrun · raw/handoff.vistmini-05-team.cartan… · raw/handoff.vistmini-cartan.cartan… · raw/request.cartan-handoff.trajectory… · raw/copy.h01.cartan.md · raw/roster.vist-x0.2026-11-13.md
- **Context caches (dated, not doing-state):** raw/cache.controller-office.nablarva-cartan.2026-11-19.md · raw/cache.operator-desk.trajectory.2026-11-20.md

## 13. Not exported, on purpose

- Raw pane captures, full transcripts, credentials, session tokens: host-local, never into Git.
- `~/reposoma/.majkee/` journal entries that the handoffs mention: sealed (L22).
- Office-only transfer evidence under `~/.codex/session-transfers/…`: not on this host.
- The archived prototype code in A/scripts/ (`vist-deliver.sh`, `bus-poke.sh`, `vist-heartbeat.py`): evidence, not a live tool. Do not reactivate it without a release.
