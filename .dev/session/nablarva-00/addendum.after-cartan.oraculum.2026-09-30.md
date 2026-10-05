# Addendum — after Cartan's independent read

*Oraculum · Claude · 2026-09-30 · session `nablarva-00`.*
*Applies to [audit 1](audit.patterns-and-loop.oraculum.2026-09-29.md) and
[audit 3](audit.session-progress.oraculum.2026-09-29.md). Those files stay as drawn;
this addendum records what Cartan's read changes.*

Source: [return.cartan.independent-read.2026-09-30.md](return.cartan.independent-read.2026-09-30.md),
sections 1–4 frozen by hash before he opened the audit. Schema evidence:
`raw/cartan-codex-0.158.0.2026-09-30/`. Oraculum checked the presence of the cited
strings in those files; it did not run the binary.

## 1. Where the two reads agree

- Attraction decides whether the loop closes. Better file visibility does not close it.
- Files as payload, one trust sphere, toolbox independence, structural brakes,
  consultation kept separate from living-peer exchange.
- The 2026-09-14 carry is a baseline for comparison, not a savings estimate.
- Return wake first, on a disposable target, with its own authorization.

## 2. Corrections to audit 1

| Where | Audit 1 said | Correction | Mark |
|---|---|---|---|
| §5 pattern E, "Leaves" | A hook cannot wake an idle session | Claude's hook documentation names an exception, `asyncRewake`: an armed asynchronous hook can wake an idle session by exiting 2. This makes a one-shot file waiter the cheapest return-wake candidate. Not verified on this host | Cartan `[O]` from documentation |
| §5 pattern F, Codex row | Plain running TUI unconfirmed | Still unconfirmed. Narrowed: the installed binary is 0.158.0; `codex queue` exposes `--thread`, `--message`, `--remote`; the experimental schema has `thread/queue/{add,list,update,delete,reorder,start}`; the stable schema has `turn/start`, `turn/steer`, `hooks/list`. Queue admission and live-TUI ownership remain untested | Cartan `[O]`; presence checked by Oraculum |
| §9 | Codex method name and version unknown | `thread/name/set` is the method (the tunnel card's `thread/setName` is wrong). Installed Codex 0.158.0, Claude 2.1.285 | Cartan `[O]`; presence checked |
| §9 | Codex Stop hook payload unknown | The embedded Stop input schema requires `session_id` and `last_assistant_message` (nullable). Twelve hook events, including `Interrupt` | Cartan `[O]`; presence checked |
| §6, "missing pipes" | Nothing consumes the arrival of a `_bus/` file as an event | Too broad. The runbook browser refreshes on new bus filenames. It has no agent-wake action | Cartan `[O]` |
| §6, `qualify.py` row | Offline test results only | It also implements a gated, read-only native inspection. Still no send | Cartan `[O]` |
| §5, "One reading" | E+F first, then B, G, C, by cost | Plausible, not measured. Hooks, waiters and channels still have process lifetime and ownership. One exchange already needs an owner for publication and correlation, even as a small script | Cartan `[I]`; accepted |
| §2, working assumption | One trust sphere removes authentication needs | Agreed, with Cartan's qualification: it does not remove the need to tell the intended session, a completed publication and a stale reply apart | Cartan `[I]`; accepted |

**New native signal worth noting.** The stable schema's thread read response carries
`notLoaded`, `idle`, `active`, and the flags `waitingOnApproval` and
`waitingOnUserInput`. That is a native answer to the observer question "is it waiting
for permission or working", for Codex threads on an app-server. Presence checked;
behaviour unverified.

## 3. Corrections to audit 3

| Where | Audit 3 said | Correction |
|---|---|---|
| §2, item 1 | Session 01 waits for `commit ok`, unpreserved | Its STATUS says so, but `git log` shows a commit on 2026-09-18 (`28847e8`). Reconcile the preservation manifest with git before asking for another action. The bed's doing-state is stale, not the work |
| §6, M3 | Session 02 owns native experiments; re-pin so C is measured beside B | Cartan: bed 02's gate is outbound-only, and its approvals must not be reused. Proposal amended: the return-wake probe gets its own disposable target and its own one-shot authorization. Design r1's B-before-C order is a proposal, not a lock; its author reconciles it |
| §6, M1 first | Close sweep first | Not a prerequisite for the wake test. Order of the list is not an order of dependence |

## 4. Cartan's probe description, in short

Target: Claude sender → Codex worker → Claude sender, reverse leg only, on office. A
disposable running Claude session is the sender; a fixture stands in for the reply.

1. Arm one command hook with `asyncRewake` in that session during setup. It starts a
   bounded waiter for exactly one expected reply path. The session goes idle.
2. The fixture atomically publishes a correlated reply carrying a fresh nonce absent
   from the wake text.
3. Success: the session resumes on its own, reads the file, and answers with the
   nonce. Permissions unchanged, UI usable.
4. Negative controls: a partial file or wrong exchange causes no wake; after one wake,
   no second wake; timeout ends without rearming.
5. Stop rule for the actuator: needs a human nudge, session replaced, duplicate
   continuation, permission bypass, or lost UI. Unsupported hooks mean "candidate
   unavailable", not "the bus is impossible".

Approvals it needs from Majkee: the disposable target and its owner; the one-shot hook
and scratch publication; any trust or config exception and its cleanup; a quota and
time ceiling for setup plus one wake.

## 5. Where Oraculum still differs

- Cartan cautions against treating one failed actuator as a verdict on every native
  route. Agreed. Audit 3's M3 already says a stop result tells which pattern to drop,
  not that the bus is dead. The wording there should be read that way.
- Cartan did not validate the `[S]` items or the error-rate estimate. Neither did
  Oraculum beyond what audit 3 §5 lists. Both remain leads.

## 6. Verified today on this host, at zero quota (by Cartan)

| Fact | Value |
|---|---|
| Codex binary | 0.158.0 |
| Claude binary | 2.1.285 |
| Codex hook events | 12, including `Stop` and `Interrupt` |
| Stop hook input | `session_id`, `last_assistant_message` (nullable), `stop_hook_active` |
| Thread name method | `thread/name/set` |
| Queue methods | experimental only |
| A tool `send_message_to_thread(threadId, prompt)` exists in Cartan's own seat | Not called; portability unknown |
