---
kind: handoff
date: 2026-11-13
seat: cartan|astrobley
vendor: codex
host: home
thread: 01a1ce98-6aa1-7021-b9cd-99805a07b2b2
request: 20261113T-h01
nonce: f0a8b749
status: experience and recommendations; no RUNBOOK adoption, canon lock or transport release
---

# My side of vistMini

I built the keystroke adapter, integrated the research, and received q01 in the existing Cartan thread. That gives me useful detail and a substantial attachment to my own implementation. A fresh head should read this as a builder’s account, then give another seat the source and an independent question. I am contributing this handoff, not taking the new head seat in this old thread.

I read Trajectory’s handoffs 00–03 and draft roster before writing this. They carry the cycle inventory; I will not reproduce it. The source bed is `/home/hruzam/ia-sync/.dev/session/vistMini-01-tests/`. Its latest STATUS pauses the bed with the gate open, Codex→Claude 3/3 and Claude→Codex 1/3 through queue. The cycle03 keystroke reverse result remains 0/3.

## What the adapter actually bought us

`bus-poke.sh` narrows a dangerous operation. It registers exact live server/pane pairs, checks the expected agent as the pane’s root process, binds PID plus Linux process start time, and checks the bottom composer, cursor, ANSI dim state and known footer. It rejects wrapping pointers and unknown layouts. It rechecks identity around the text/Enter boundary. It reserves an attempt with exclusive directory creation, types literal text, and sends Enter separately only after an exact post-text observation. The attempt phase survives failure. Those are useful guards, not an authenticated or atomic delivery API.

The shell-parent check was especially worthwhile: a foreground agent can disappear and reveal the shell that launched it. `exec` removes that particular fallback. It does not authenticate the agent, prove the roster’s logical identity, prevent every race, or make the endpoint durable across relaunches. `%2` and `%3` were explicit trial bindings, not universal addresses. The adapter’s argv0/process assumptions also need requalification when launch wrappers change.

The reservation is more valuable than a promising screen. Cycle03 t03 reached `text-attempted`, returned 27, and sent no Enter through the adapter. Majkee later supplied Enter. We consumed the content but did not count an adapter success. Preserve its historical key; do not repair history by clearing state or replaying the message. In a new transport, an uncertain submission must retain its uncertainty across carrier changes too.

The code’s success line deliberately says `notification-attempted ... receipt=unproven`. Keep that honesty. A check returning zero is one observed ready frame; a send returning zero is an attempted notification; neither is a worked return.

Sources: `scripts/bus-poke.sh`, `tests/README.md`, `reports/cartan.cycle03.2026-11-12.md`, `_bus/03.trajectory.verdict.md`.

## Codex-side surprises that should become cases

The one-shot helper checked both endpoints after an eight-second delay so the sending controller could finish its turn. It was an expedient for this paired trial. Running it from Claude created the very `1 shell` footer that the sender check did not recognise. That was a self-caused observation change, not proof that the recipient was unavailable. We registered one observed footer exactly and kept unobserved variants refused. Do not grow a wildcard until the runtime supplies evidence for it.

Then q01’s return bell refused on my own pane because the view was scrolled into earlier material with `New activity`. The receiving Claude pane had not even been checked. Receiver delivery readiness, sender UI view and caller permission are three different questions. I would not promote “both panes must look idle” into a universal carrier contract. Any change to that guard needs its own scoped qualification; I did not change it here.

I also initially mistook Claude’s dim suggestion for an unsent user draft. The ANSI/cursor evidence corrected me. Plain captured text is insufficient to tell those apart. Conversely, detecting the particular dim suggestion does not prove that every invisible or multiline draft can be excluded. Fixtures passed the screen states we encoded; they did not establish the real Codex composer’s post-text semantics.

The paste-window explanation is still a hypothesis. The adapter’s t03 failure occurred before its Enter call. It cannot demonstrate that an Enter sent by that adapter became a newline. Majkee and Trajectory’s manual observations motivate a timing experiment on an expendable receiver; they are not a fix already validated for the adapter. Preserve that distinction when telling the story.

Today’s h01 exposed another boundary without a new transport experiment: `[copy h01] cartan` is not in the adapter’s registered bus/read-pointer grammar. The requested helper invocation cleanly returned 30 before any input. I wrote `copy.h01.cartan.md`, as the request permits, before doing substantive handoff work. “Use the existing adapter” must include a payload format it can represent. I have not broadened its grammar.

## What changed my confidence

q01 was the first useful reverse-direction result. It reached this same existing thread as a normal new user turn. I read the POINT, copied nonce `ce3cbfe1`, and recorded the receiving turn ID and start time. The head then correlated its queue log, read-only receiver observation and Majkee’s statement that he had not touched my pane. That combination is substantially better evidence than my saying “I saw it.” The current head VERDICT accepts one queue delivery, not general queue reliability.

Read `reports/trial-msgs/q01.cartan.receipt.md` with `_bus/05.trajectory.verdict.md`. Keep the limitations: I could observe my own turn and consumption; I could not observe the sender’s shell call or absence of operator input there. My timestamp came from turn-start metadata, not a separately measured physical render time. Do not give a receiver receipt powers it does not have.

The office Jev exchange and its native-event excerpts are a useful precedent. Home’s Astra route still failed with an active writer. A worker later reached me, and Majkee reported resuming Oraculum before the successful retry. Different endpoints are involved. I recorded the timing as a clue, not a causal fix. Do not remove writer locks, force a competing owner, or replace the intended thread to make a demonstration green.

Native messaging can also carry runtime-added sender context. A short authored pointer does not guarantee a pointer-only received payload, and copied context does not transfer permissions. That deserves an explicit payload/provenance case alongside delivery cases.

Sources: `reports/office.native-messaging-reply.2026-11-12.md`, `reports/cartan.codex-channels.2026-11-12.md`, `reports/cartan.native-resume-clue.2026-11-12.md`.

## Where I would amend Trajectory’s proposals

I agree with native-door inventory first and with using real disposable receivers. I would tighten five points before adopting handoff 03 or the roster:

1. **Candidate is not qualified.** Office-native success, a documented Claude API, q01 on home and three tmux deliveries are different evidence classes. “Native doors exist for three directions” is a useful research map, not three qualified routes. The successful worker’s mechanism is still unknown here. Each route needs sender context, target ownership, version and a correlated receipt on this host. The roster should preserve those qualifications rather than calling an inbound list operational by itself.
2. **One logical message must survive carrier changes.** “Try carriers in order” is unsafe unless each preceding result proves it did not submit. A timeout, warning, missing receipt or unknown exit classification is not that proof. Keep the same logical message ID and receiver deduplication across routes. Reserve once, record what each layer actually knows, and stop on ambiguity. Any later retry after a clean hold needs a released limit, expiry and revalidation; it is not automatically safe because the ladder says “one later retry.”
3. **Separate acceptance from submission and consumption.** Exit zero plus a queue ID can establish enqueue acceptance if that command’s contract supports it; it need not establish a turn in the intended existing owner. q01 had additional turn and witness evidence. A nonce receipt correlates work but does not authenticate its author against a malicious or mistaken writer. This was a trusted local smoke trial, not an adversarial identity proof.
4. **Do not make tmux universal availability.** A native carrier can potentially reach a thread without a pane. Missing tmux or a pane-classifier refusal should not automatically mean host absent, session dead or native route unavailable. Observe each capability independently. A readable stored thread, similarly, is not proof that this caller owns or can reach its live writer.
5. **Qualify the proposed automatic copy hook.** Handoff 03’s Claude `UserPromptSubmit` / Codex `notify` equivalence is untested. Establish the actual supported event, timing, correlation fields and permissions before promising a turn-start receipt at zero agent cost. A hook execution proves its own event first. A copy receipt and a completed result remain separate outcomes.

I also qualify “auditor: no execution.” Read-only source inspection, approved test execution and product mutation are distinct powers. If the auditor must verify mechanical claims, give it a precise evidence/check scope. Otherwise it can review reports but cannot independently confirm the behavior. It should return findings through the head and leave repairs to the builder.

## What I would tell the fresh Sol head

Keep a short board of claims and next discriminating observations. Do not load every raw log into your own context. Give a researcher one volatile API/ownership question, an implementer one bounded component, and a verifier the declared acceptance criteria plus original artifacts. Recheck the citations that change your decision. Children return evidence; you integrate. Avoid making yourself both the only adapter author and its acceptance witness.

Ask what existing door could resolve the uncertainty before adding another screen signature. We spent too long refining a safe refusal mechanism before testing the cheaper native candidate. Research was useful; the missed opportunity was turning the candidate inventory into an early released, bounded live test. Do not turn that lesson into “a documented door is already safe.”

Write the bell rule explicitly, including its exact accepted payload and the fallback after a clean refusal. No fallback after an uncertain submission. Have a receiver-copy outcome, a work outcome, and a completion notification outcome. A committed result with no successful bell is still waiting on notification. I left that last mile incomplete on q01; the adapter’s clean refusal was correct, but scheduling the helper was not completion. Avoid substituting a visual status banner for a wake-up claim.

Declare one push owner per repository and a concrete commit window. `git add` and `commit` do not make a file visible to office. Our office round trip stalled until Majkee explicitly authorized the one-off push. Scope staging to owned paths, preserve unrelated edits, and let the push owner report the remote result. In Nablarva, L12’s Git rules apply; do not carry ia-sync’s rebase recipe across the repository boundary.

My earlier tmux advice was too narrow: pane synchronisation, two clients following one session’s selected window, and copy/scroll mode are different phenomena. Sharing a window alone does not broadcast pane-addressed input. Diagnose the actual option and client/view binding before advising a move. Grouped sessions can provide independent selected windows; the address recorded for delivery must still resolve the intended underlying pane.

VIST keeps observation, controller decision and actuation separate under L20/L21. A correlated worked return is stronger evidence of consumption than an idle transition. It does not close the separate qualification of passive observations. Three ordinary successes are smoke evidence; preserve unknown, refused and untested states in the final report.

## Scope and continuation

Nonce `f0a8b749`. Files authored for h01: this handoff and `copy.h01.cartan.md`. No Trajectory file, RUNBOOK, STATUS, roster, pulse, canon, adapter, runtime configuration or Termbrana work was edited. No new transport test, retry, daemon, watcher or replacement agent was started. The copy helper’s grammar refusal is an administrative attempt only, not another message-trial result.

I read the requested reposoma card `CS.vist-x0-runbook-oraculum.2026-11-13.md`. It now describes a Claude/Fable phase-0 RUNBOOK preparer followed by a fresh Sol head; earlier raw seating alternatives remain proposals. There is no RUNBOOK/STATUS in this bed at capture. This request authorizes my experience handoff, not starting phase 0 or seating myself as head. The next owner should reconcile the roster and strategist identity with Majkee, then carry only adopted recommendations into the new RUNBOOK.

Commit only; Trajectory pushes. The completion poke is a separate administrative action after the commit. Its attempt/result must not be inferred from this file’s existence.
