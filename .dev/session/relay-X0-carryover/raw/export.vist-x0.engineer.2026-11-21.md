---
kind: carry-over export (pointers and summary; the origin files stay where they are)
author: engineer (trajectory, claude d1ca16e9), host home
date: 2026-11-21
origin_bed: ~/unikuklatrix/nablarva/.dev/session/vist-X0-helloWorld   # short name in this file is O/
origin_revision: nablarva core 75227bc + three uncommitted origin edits that are not mine (see §2)
archive_of_trial: ~/ia-sync/.dev/records/vist/2026-11-14/vistMini-01-tests   # short name in this file is A/
read: all 45 files of O/ (root 3, _bus 3, raw 39) on 2026-11-21
rev: 4 (2026-11-21) — rev 1 was checked by cartan (cycle 01 — 43 confirmed, 7 refuted, 7 missing-source). rev 2 was my repair; cartan re-checked it (cycle 06 — 9 repaired, 5 repaired wrong, 3 statements stale). rev 3 repaired those eight; cartan re-checked it (cycle 08 — 7 repaired, 1 repaired wrong). rev 4 narrows that one sentence in §2.
status: rev 3 was re-checked by a non-author. rev 4 changes one bullet of §2 and this header, and that bullet is NOT yet re-checked (asked in cycle 09). Trail — ../_bus/01.cartan.return.md, ../_bus/06.cartan.return.md, ../_bus/08.cartan.return.md and their VERDICTs. A summary is still a claim; the origin file wins.
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

Observed on home 2026-11-21 (mine, not in the origin files; each with its source):
- O/RUNBOOK.md has an **uncommitted edit** of the `goal:` line. Disk differs from the review hash; `git show HEAD:` still matches `9081d353…` (cartan re-checked: HEAD 5/5, disk 4/5). If that edit is committed, the review no longer covers the file. *Whose edit:* Majkee said so in the engineer session on 2026-11-21 ("these are mine, now I am studying runbook"), about this edit and about O/majkee-personal-notes.md. Git itself shows no author for uncommitted work.
- `relay-X.ledger.md` and `vist-X.ledger.md` carried an uncommitted merge. *Whose:* the ledger's own `by:` line and ../_bus/02.myshell.return.md (myShell, on Majkee's request, 2026-11-21).
- The X0 desk session `06352fda`: two observations only. Its old pane `%49` showed a shell (my `tmux list-windows -a` on 2026-11-21; cartan again in cycle 06), and none of the files I listed under `~/.claude/sessions/` on home on 2026-11-21 carried that id. Neither shows that the session is gone — the listing was not shown to be complete, and other hosts were not looked at. O/STATUS still names it as desk; that binding is a dated record, not a live fact.
- The `controller` window in today's tmux party is a **fresh** Codex thread `01a1ff5e…` (its own footer; confirmed by that thread in ../_bus/01.cartan.return.md), not the X0 pen.

## 3. What is established and what is not

| Claim | Class | Source |
|---|---|---|
| Three ordinary messages in each direction on one host, with independently checked reporting | **supported** (accepted scope) | ~/ia-sync/.dev/records/vist/2026-11-14/CLOSE.md |
| Codex→Claude 3/3 through the tmux keystroke adapter | supported, version-specific screen reading | O/raw/handoff.vistmini-01-evidence… §1,§3 |
| Claude→Codex through `codex queue --thread` (q01 first; three ordinary + scoped samples) | supported, **bounded** | O/raw/handoff.vistmini-01-evidence… §4; O/raw/handoff.vistmini-05-team.cartan… "Queue evidence has bounds" |
| Claude→Codex by tmux keystrokes | **failed 0/3** (29, 29, 27); cause is a hypothesis (paste window) | O/raw/handoff.vistmini-01-evidence… §2; O/raw/handoff.vistmini-cartan.cartan… |
| Codex→Codex native `send_message_to_thread` | worked on office (cycles 09–11); one `-32600 active writer` failure on home. The cause is a clue, not an established rule | O/raw/handoff.vistmini-01-evidence… §3; O/raw/handoff.vistmini-cartan.cartan… ("a clue, not a causal fix") |
| Codex→Claude through Claude cross-session messaging, via a "Codex delivery worker" | **reported once** (2026-11-12, an Oraculum on Codex, marker VIST-READING-20261112-01); mechanism not inspected, how the worker reached the session is unknown; not a qualified route. A different event from the row below | O/raw/handoff.vistmini-01-evidence… lines 24–25 and 45; O/raw/handoff.vistmini-05-team.cartan… |
| Claude→Claude `SendMessage` / `ListAgents` | **documented, untested** in the evidence file. One event on 2026-11-13 (cycle 09): the trial report says the oraculum seat sent a Claude SendMessage at the operator's request and trajectory received it — reported from the receiver's side only, no sender-side record, "not counted, not reliable-by-evidence". Handoff 04 fact 2 repeats that account. It proves no route in this direction | archived trial report lines 37 and 103–104; O/raw/handoff.vistmini-01-evidence… line 49; handoff 04 fact 2; handoff 05 |
| Cross-vendor review found six overclaims (R1–R6) in the trial report | observed once; not a measured superiority result | handoff 04 fact 3; handoff 05 |
| Controller succession by read-back → acceptance → activation → uptake | observed once, **warm** successor | O/raw/readback.controller…, acceptance.controller…, activation.controller…, checkpoint.controller… |
| Six carried cases U01–U06 | **UNRUN / UNQUALIFIED** | O/raw/preregister.vistmini-carryover.cartan.2026-11-14.md |
| Cross-host anything · permission boundaries · reliability numbers · survival of a CLI upgrade | **not established** | handoff 01 §5 |
| The accepted trial report and the readable archived report are **different bytes** | accepted experimental report = ia-sync@3584a02, sha `dc219b62…`; the readable archive copy adds the later operator disposition, sha `fd1b1e20…` | O/raw/preparation.sources.2026-11-14.json (`accepted-report`); ~/ia-sync/.dev/records/vist/2026-11-14/MANIFEST.json maps every original path |

Three successes are a smoke test, not statistics. Queue acceptance, submission, a native turn, a file read, a worked receipt and
accepted work are six different observations (O/raw/cache.controller-office… "Review and coordination lessons").

## 4. The C04 lesson (why "delivered" needs four layers)

Source: O/raw/preparation.c04-timeline.2026-11-14.md. Same message type, two runs:
- **r1:** the carrier accepted the queued message and the work arrived, but the sample taken **for the new attempt** said `ready` while the receiver's setup turn was still running. Carrier success, **observation failure**.
- **r2:** the sample for the new attempt said `busy`, the queue accepted, the receiver took the turn later, the nonce matched. One scoped correlation, not a qualified classifier.
- In **both** runs the `ready` read *before* the call was stale data from the earlier setup attempt. Do not mix it with the new attempt's observation.
- r1 and r2 are **different native receiver lifetimes** (different thread and PID, same pane) and different helper builds. The sender's wrapper timestamp is finer than the queue log (seconds only).

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
| Codex→Claude | tmux pane, look-first; adapter `bus-poke.sh` in A/scripts/ (archived, not live) | 3/3 in the trial. Adapter codes: `24` busy, `29` unrecognised composer (handoff 01 §2). Handoff 04 reports that rings into a working Claude seat came back 29 |
| Codex→Claude | Claude cross-session messaging via a delivery worker | reported once (2026-11-12); mechanism not inspected |
| Codex→Codex | native thread messaging | worked on office; one active-writer failure on home; no rule established |
| Claude→Claude | `SendMessage` / `ListAgents` | documented; untested in the evidence file; one receiver-side account (2026-11-13), no sender-side record |
| state of a Claude seat | `claude agents --json` | documented, not qualified |
| state of a Codex seat | `read_thread` (Codex native) | used once for q01 |

Versions: handoff 01 records codex-cli 0.167.2 / Claude Code 2.1.286 for its early snapshot (2026-11-12). The archived trial report names CLI 0.169.0 for the queue results (line 35) and ties the screen signatures to Claude 2.1.323 and Codex 0.169.0 (line 83). The C04 timeline says installed-version probes do **not** prove which binary ran at event time. **Home today: codex-cli 0.171.0, Claude Code 2.1.330, tmux 3.7c** (re-checked by cartan). No door has been qualified on today's versions.

Today's coordination, as observations only (../raw/pokes.log.md): `codex queue` calls were accepted and native turns started; look-first tmux pastes into Claude panes were submitted, and once (bell r06) the text was staged in the composer and never submitted, cause unknown. In cycle 01 Cartan's Codex sandbox could not reach tmux (`Operation not permitted`, his RETURN field 2); after Majkee set his seat to Full Access it could (cycle 03). What a door reaches depends on the sender's permission mode.

Lead from this session (my own observation of the files on 2026-11-13 and 2026-11-21; **field meanings are not verified** against any documentation, and nobody else has checked it): Claude Code session files `~/.claude/sessions/<pid>.json` carry `peerProtocol`, `peerFeatures`
(`notify_idle`, …) and a messaging socket field, plus live `name`, `status` (busy/idle) and the hosting `tmux` pane. That may be a native
state probe and maybe a native door into Claude — the weak direction. Do not print the socket path or the `.key` files.

## 7. Rules that bind this line (pointer, never copy)

- **Locks:** `~/unikuklatrix/nablarva/.dev/session/flag.md` — L12 (one repo, plain `git pull`/`push` on `core`, never `pull --rebase`, parallel work via `git worktree`), L14 (relay foundations; reserved names `relay-00-research` → `relay-01-pty` / `relay-02-tracker`), L20 (observation ≠ decision ≠ action), L21 (no **shared** layer, framework or transport implementation is authorised; implementing, activating, delivering through or adopting a transport for one needs its own separate release), L22 (`.majkee/`, `.hlm/` sealed from agent reading).
- **Working holds, not locks:** serial, owned-path Git windows with foreign work left alone (O/STATUS `holds`); operation-specific authority per case — each proposed run names its action, owner, permission and side effects (O/raw/preparation.qualification-matrix…, O/raw/plan.runbook-and-team… "Release is action-specific").
- **Operative decision for this line:** O/raw/decision.shared-file-poke-relay.majkee.2026-11-19.md — file-poke is shared and development-limited; future coordination work runs on **relay**; VIST X0 keeps its identity, gate and frozen packet; the L14 names and gates stay; launched RUNBOOKs are never rewritten and a retired chapter keeps a tombstone.
- **Shared practice:** `~/reposoma/raw.guides/bus/GUIDE.md` (POINT / RETURN / VERDICT) and `~/reposoma/raw.guides/bus/res/file-poke.md` (provisional; write → poke → work → return → verify). The using session carries the retirement debt of file-poke.
- **Fallback poke "like sudo":** look first, label `[manual …]`, once, never after an uncertain send, record it — O/raw/decision.majkee.fallback-poke.2026-11-14.md.
- **Never retry or clear:** historical `t03` and `c08r1-05-ae3ee8e7` (home state file still present 2026-11-21).
- **No carrier switch after an uncertain submission** until the receipt is reconciled. One logical message id across carriers.
- **Author ≠ accepting reviewer.** Changed bytes after a review = a new review input.
- **Match role and output before dispatch:** a read-only seat cannot write a RETURN; plan its publisher, never impersonate (O/raw/plan.runbook-and-team… "Reviewer output contract"). The read-only route was used once: a hard read-only challenger's final was published verbatim, attributed, outside the BUS RETURN path (O/raw/review.shared-file-poke.challenger.2026-11-19.md).
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
2. `git push` without a prompt: the desk cache **reports** that it is allowed for every seat in ia-sync and nablarva on all three hosts, and concludes that "only the controller pushes" is not enforced. What is seen here is narrower: on home, `.claude/settings.local.json` in nablarva and in ia-sync each carry allow entries for `Bash(git push)` and `Bash(git push -q)` (seen by me in both; by cartan in nablarva, cycle 06). Allow entries in two files do not establish what other seats, other hosts or a policy do. Keeping or restoring the prompt is his call. Since 2026-11-21 he routes this bed's pushes through the controller. (O/raw/cache.operator-desk.trajectory.2026-11-20.md, owed #2)
3. Witness hook extras beyond the brief (`-L <name>`, short aliases). (same file, owed #3; O/raw/witness.host-move…)
4. Whether the fallback poke applies to the witness. (O/raw/witness.host-move…)

## 11. Tensions I see (engineer's view; not resolved anywhere in the origin bed)

- **T1 — L14 D1 and the trial's directional asymmetry.** L14 D1 keeps PTY as the base layer and parks vendor doors (`codex queue`, Claude channels) as "weather". The trial does **not** contradict that; it shows an asymmetry: PTY keystrokes delivered 3/3 **into Claude** and 0/3 **into Codex**, where the vendor door worked. Trajectory's kept disagreement is handoff 02 S9 ("PTY = sensor, receipts = truth, native doors = actuator where they exist"). The evidence supports comparing actuators under a release. It gives no ruling on the base layer; that stays Majkee's.
- **T2 — two live beds on one line.** X0's gate is open while this bed starts. Rule for this bed since cycle 04: no U-case runs here until Majkee names this bed as the one executing bed for that case; acceptance of the X0 packet alone carries nothing here.
- **T3 — today's party panes are shell-rooted.** My read-only tmux query on 2026-11-21 showed `pane_start_command` = `exec zsh -l` with `claude` / `codex` as the current command in all four windows (../raw/roster.2026-11-21.md). Cartan confirmed the four original start commands in cycle 06; the auditor window was opened later and its start command was not checked. If an agent exits, a typed poke lands in a shell. Look before every typed line.
- **T4 — evidence custody is unresolved.** The eight local C04 inputs pinned by the packet live in `/tmp/vc08r1.tkz50zbf` and `/tmp/vc08r2.kk50sqqh` on home. Both directories exist today (seen by me and by cartan); their bytes were not re-hashed. `/tmp` on home is `tmpfs` (`findmnt /tmp`), so its contents do not survive a reboot. The packet says hashes do not prove durable custody. Copying them needs Majkee's word (host-local, private material). Carried as goal G9.
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
