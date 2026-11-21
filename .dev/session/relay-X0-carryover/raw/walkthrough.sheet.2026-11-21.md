---
kind: decision walkthrough sheet — what to put to Majkee, one theme at a time
by: engineer (pen of relay-X0-carryover) · 2026-11-21 · host home
for: the exec desk (cycle 10) and Majkee
rule: every line here is a pointer or a summary of a file in this bed. Where it matters, open the file named under "Files". This sheet decides nothing and releases nothing.
order: as numbered. T1 and T2 first because they can be lost or leak. T3 before T7 because the umbrella is part of what the gate accepts. T4 before T5 because U01 belongs to the X0 packet.
base: ~/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/   (all relative paths below start here)
---

# Decisions owed by Majkee — eleven themes

## T1 — The transcript of the accidental Claude session
- **Context:** in cycle 07 a mistyped help command started a Claude session for 16 seconds. It read working files, among them the first 40 lines of `majkee-personal-notes.md` and your uncommitted RUNBOOK edit. The process is gone; its transcript is still on disk.
- **Buys:** *keep* — the raw evidence of the incident stays. *Delete* — the copy of your notes leaves the host's Claude history.
- **Cost:** none either way. The incident note keeps the facts without the content.
- **Consequences:** kept, it shows up in the session list of that folder and any session resumed from it would carry the content. Deleted, nothing in this bed depends on it. What was sent to the model during those 16 seconds cannot be recalled either way.
- **Ask:** keep or delete? If delete — by your own hand, or which seat?
- **Files:** `raw/incident.stray-claude-session.2026-11-21.md`

## T2 — The C04 inputs in /tmp (goal G9, part a)
- **Context:** eight local inputs that the VIST X0 packet pins by hash sit in `/tmp/vc08r1.tkz50zbf` and `/tmp/vc08r2.kk50sqqh` on home. `/tmp` is memory-backed; the host has been up since 2026-09-29.
- **Buys:** *copy* — the C04 reading can be repeated and the hashes re-checked later. *Let go* — nothing to keep safe.
- **Cost:** copy takes minutes, but it copies private screen captures: a durable host-local folder, mode 0600, never Git.
- **Consequences:** if a reboot comes first, the packet's hashes can never be re-checked. The packet itself says hashes do not prove custody.
- **Ask:** copy or let go? If copy — into which folder, and may the controller do it by assignment?
- **Files:** `goals/G9.custody-and-handoff.md` · `raw/export.vist-x0.engineer.2026-11-21.md` §11 T4

## T3 — The umbrella sentence (goal G0)
- **Context:** you wrote "Establish what the accepted home trial can support for RELAY organ, based on VIST aproach and list into observation qualification before selecting a new implementation or transport." as an edit of the X0 RUNBOOK's goal line. The engineer proposed it as the umbrella of this bed. You have not said yes to that.
- **Buys:** one yardstick — every goal must serve it or be dropped.
- **Cost:** none.
- **Consequences:** *yes* — the bed ends only when you say the question is answered. *No* — give another sentence, or the bed runs without an umbrella. Side matter: your edit in the X0 RUNBOOK is uncommitted; if committed there, that file no longer matches its review hash.
- **Ask:** is this sentence the umbrella of `relay-X0-carryover` — yes, no, or other words? And the edit in the X0 RUNBOOK: leave it, or take it back there?
- **Files:** `goals/G0.umbrella.md` · `raw/decision.majkee.open-bed.2026-11-21.md` (D3.5 and "My reading")

## T4 — Your decision on the VIST X0 packet
- **Context:** the X0 packet is paperwork: a re-reading of one old case and a plan for six cases that never ran. It was reviewed (PASS) and its controller accepted the review. Your own ACCEPT / REVISE / STOP has been open since 2026-11-14. That bed's pen is recorded on office.
- **Buys:** *ACCEPT* closes X0's paper gate. *REVISE* sends it back. *STOP* ends that line; carried cases then move only when you carry them.
- **Cost:** none now.
- **Consequences:** the packet names U01 as its own first operation. ACCEPT without naming a bed lets two beds claim U01 (see T5). "Not yet" is a valid answer; then nothing with a release runs.
- **Ask (two parts):** (a) who writes your decision into that bed — the engineer from home, the office pen, or you? (b) ACCEPT, REVISE, STOP, or not yet?
- **Files:** `../vist-X0-helloWorld/STATUS.md` · `raw/export.vist-x0.engineer.2026-11-21.md` §2 and §10

## T5 — U01: one real unknown screen, or "missing" (goal G4)
- **Context:** the trial never met a genuinely unknown native screen, so "unknown stays unknown" was never tested. The first step is a read-only search of old captures for one real fixture.
- **Buys:** U01 becomes testable, or an honest "none exists", which means a new capture under a different release.
- **Cost:** opening old captures that hold private screen content; two seats, because the labeller must not be the selector.
- **Consequences:** this is the first released work of the whole line. Run in two beds it would produce two results for one case.
- **Ask (four parts):** (a) run it now, or not yet? (b) which one bed executes it — `relay-X0-carryover` or `vist-X0-helloWorld`? (c) which capture folders may be opened, and how is the result redacted? (d) is cartan as selector and the auditor as independent labeller acceptable?
- **Files:** `goals/G4.u01-unknown-view-fixture.md` · `goals/OVERVIEW.md` (G4)

## T6 — The friendly reminder (goal G10, your question)
- **Context:** you asked for a vendor-neutral reminder with a timer. The shared file-poke chapter already describes a finite check-in; stage 1 turns it into a small script that reads one cycle's files and prints: closed, a return waits for review, or still outstanding. Stage 2 would send one reminder to the silent seat.
- **Buys:** stage 1 — the one who waits is told. tmux can also flag a silent window by itself (`monitor-silence`), no script.
- **Cost:** stage 1 is about 60 lines. Stage 2 is a second send, so it needs its own release and is forbidden after an uncertain first send.
- **Consequences:** it would be the first small product of the relay line. A timeout says only "outstanding when checked", never "the seat is dead".
- **Ask (five parts):** (a) go or no-go on stage 1? (b) where does the script live — in this bed, or in ia-sync beside the session-window helper? (c) output: a printed line and a file note only, or also a desktop notification? (d) do you want the tmux `monitor-silence` one-liner to set yourself? (e) stage 2 — not now, or a release later?
- **Files:** `goals/G10.friendly-reminder.md` · `raw/answer.majkee.reminder-and-leftovers.2026-11-21.md`

## T7 — The gate of this bed
- **Context:** the gate text was drafted by the engineer and reworded after two outside reads. It asks: will you accept export rev 4 and the listed goal revisions as the relay planning baseline, on paper only?
- **Buys:** a fixed baseline. Later changes to a goal become a new revision, visible as such.
- **Cost:** none.
- **Consequences:** accepting releases nothing — the X0 decision, the bed for each U-case, custody and every operational release stay separate. Rewriting replaces the engineer's words with yours. The export was read four times by a non-author; the goal files were read once by the auditor and repaired, and the repaired goal texts were not read again.
- **Ask:** accept as written, rewrite, or not yet?
- **Files:** `STATUS.md` (`gate:` and `goals:`) · `_bus/04.engineer.verdict.md` · `_bus/05.engineer.verdict.md`

## T8 — Live work behind releases (goals G8, G6, G7) and lock L14
- **Context:** the door inventory is done on paper (G3). G8 would try each door once on disposable sample sessions. G6 is the exit-race case and needs a two-step actuator. G7 retires the provisional file-poke once a replacement exists. The relay ledger says experimental routing must not bypass the L14 sequence (`relay-00-research` first) where the work falls under it.
- **Buys:** G8 turns a list of candidates into evidence on today's versions; today one of four pastes into a Claude pane failed to submit, cause unknown.
- **Cost:** G8 — starting sample sessions (trust dialogs are your hand), real sends, an independent observer. G6 — the highest of all goals.
- **Consequences:** G8 is the first goal that activates and delivers in the sense of L21. It adopts no door, but its results feed your later choice and touch L14 D1, which parks vendor doors.
- **Ask (three parts):** (a) does G8 belong in this bed, or under `relay-00-research`? (b) release G8 now, later, or not — and if now: which samples, who sends, who observes? (c) G6 stays parked and G7 stays blocked — agreed?
- **Files:** `goals/G8.door-probes-live.md` · `goals/G6.u02-exit-race.md` · `goals/G7.retire-file-poke.md` · `raw/doors.inventory.2026-11-21.md` · `../relay-X.ledger.md` · `../flag.md` (L14, L21)

## T9 — Three older open decisions from the X0 desk
- **Context:** carried in the export §10, items 2–4. (2) `git push` is allowed without a prompt in the Claude settings of nablarva and ia-sync on home; since today this bed's pushes go through the controller. (3) the witness hook has extras beyond its brief (`-L <name>`, short aliases). (4) whether the fallback poke applies to the witness.
- **Buys:** closing them removes three loose ends from the X0 desk.
- **Cost:** none to decide; (2) may mean editing settings through ia-sync.
- **Consequences:** left open, they stay listed and nobody acts on them.
- **Ask:** for each — decide now, or defer? (2) keep the allow entries, or restore the prompt for Claude seats? (3) keep or remove the extras? (4) yes or no?
- **Files:** `raw/export.vist-x0.engineer.2026-11-21.md` §10

## T10 — The team and the shape, after one evening
- **Context:** two at work (engineer, cartan as controller), two on call (oraculum, auditor), and this exec desk. Oraculum's identity file rules out code review, pushing and operating transports, so she cannot be a senior dev partner. Goals as small files were tried for one evening: goals changed several times mid-run without breaking a running assignment; two outside reads found seven real faults in the pen holder's work; every closing commit cost a push round.
- **Buys:** a settled team and a yes or no on the shape before the next work starts.
- **Cost:** each kept window is an idle seat.
- **Consequences:** if a build is released later, somebody must be the second coder; today nobody holds that role.
- **Ask (five parts):** (a) keep the auditor window as the independent observer for G8, or close it? (b) who is the senior dev partner if a build is released — this exec seat, a new one, nobody yet? (c) reply bells stay as a hint only — agreed? (d) goals as small files — keep trying, or return to a RUNBOOK? (e) does this exec desk stay as your decision desk for this bed?
- **Files:** `raw/roster.2026-11-21.md` · `STATUS.md` (`open_costs_of_this_shape`) · `goals/README.md`

## T11 — Outside this bed (pointer only, may be skipped)
- **Context:** the bed `session-window-X0-substrate` (the tmux status helper, moved from ia-sync on 2026-11-19) still has a provisional gate that waits for you, and its first probe was never run.
- **Ask:** now, later, or drop?
- **Files:** `../session-window-X0-substrate/STATUS.md` · `../session-window-X.ledger.md`
