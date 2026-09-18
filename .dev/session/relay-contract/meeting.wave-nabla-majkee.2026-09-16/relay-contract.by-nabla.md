# CLI relay — coordinator behaviour (Nabla's half)

Status: draft from the 2026-09-16 meeting. Countersigned split with Wave:
- Wave owns envelope semantics and invariants (task exits, relay states, what evidence a declaration carries).
- Nabla owns coordinator behaviour, the wake adapter, the watcher boundary, and kill tests.
- Field names and exact schema are deferred until the existing runbook / state / bus guides are read. Cross-review before anything hardens. Nothing here may clobber what already works.

## Principle

Truth lives in files. The poke is electricity, not meaning. No vendor event is ever evidence of anything. Deadlines live outside the model.

## Seats

| Seat | What it is | Can it act on the bus? |
|---|---|---|
| Architect (C*/O*) | Thinking model. Writes/rewrites the runbook. Receives escalations. | Yes — only via runbook edits and escalation replies |
| Coordinator | Deterministic script. No model. | Yes — writes envelopes, pokes, advances state |
| Watcher | Small model, optional. Reads bus + state. | No — reports to chair only |
| Participants | CLI sessions (Claude Code, Codex, ...). Do the steps. | Yes — declare exits into the bus |
| Chair | Majkee. | Anything |

Only one seat can be wrong in a way that costs seven hours, and it is not the coordinator.

## Files (existing, to reconcile with guides)

- runbook — stable. Steps, roles, roster, master prompts, escalation targets by role, per-step retry budget, per-step done-condition.
- state — volatile. Current step, current relay state, deadline, retry count.
- bus/ — one file per message. Envelopes out, declarations in, escalations parked.

## Coordinator loop

```
loop:
  read state
  step = runbook[state.current]
  target = runbook.roles[step.role]          # role -> concrete session, never a live lookup
  write envelope to bus (step id, goal, done-condition, deadline)
  adapter.wake(target)                        # zero semantics
  state.relay = delivered; state.deadline = now + step.timeout
  wait until: declaration file for this step appears  OR  deadline passes
  if declaration:
      validate shape only (declared exit present, required evidence present)
      # meaning is never interpreted by the coordinator
      transition(declared exit)
  else:
      transition(timeout)
```

The coordinator never advances on silence, on a vendor Stop event, on transcript text, or on an agent saying "done" without evidence. Evidence is something the filesystem or a command can check: file exists, test exits 0, migration applied.

## Exits and transitions

Task exits (declared by the participant — Wave defines meaning):
- done → advance to next step.
- failed → same participant retries, up to runbook step.retries; then escalate as task failure.
- invalid → the world no longer matches the step's assumptions. Escalate to architect and notify chair. May mean a runbook rewrite; rare and now detectable.

Relay states (owned by the coordinator, never a task outcome):
- delivered → envelope written, wake sent.
- acked → participant has opened the envelope (optional, adapter-dependent; never required).
- timeout → no valid declaration by deadline. Re-wake once. If still nothing: escalate as relay failure, not task failure. A dead session is not a failed step.

Timeout is a protocol invariant, not an error handler. A missing event is indistinguishable from a slow agent.

## Escalation

- Steps escalate by role: `escalate: architect`. Runbook maps role → endpoint.
- If no session is live at that endpoint, the escalation sits in the bus in a named box until someone attaches. Chair can close the laptop and return tomorrow; context is in the file.
- Coordinator never has to find anyone. It writes to a named box and pokes if a session is present.
- Ambiguity is never a cue to interpret. It is a cue to stop and escalate.

## Wake adapter

Interface: `wake(session) -> void`. No payload, no meaning. The envelope on the bus is the message.

Implementations, swappable, none trusted:
- tmux send-keys — baseline for every vendor. Blunt, works everywhere.
- claude-hook — Claude Code hooks (TeammateIdle / TaskCompleted / SessionStart family) as a cleaner wake when available.
- codex-hook — Codex session/stop hooks when they fire.

Constraints learned 2026-09-16:
- Hooks must be configured at provisioning, before the session starts. Mid-session hook changes are not reliably active. The relay never installs its own doorbell into a running session.
- A Claude Code turn ending in rate limit or API error fires StopFailure, not Stop. Any adapter that listens for Stop as "turn finished" will see a dead pane as working forever. Hooks feed relay state at most; they never advance task state.
- Codex hooks exist but drop events across versions. Same rule.

Symmetric by discipline, not by capability: if one vendor's adapter is better, the relay must not grow a second shape around it.

## Watcher

- Reads bus and state. Writes nothing there.
- Reports to the chair (terminal pane, notification, whatever the chair prefers) when something smells wrong: step stuck near deadline, retry count climbing, escalation parked with nobody attached, agents chattering without evidence.
- Whispers, never moves a piece. Kill it and nothing stops.

## Loop safety

- Budget is per step, not per turn. Turn counts are arbitrary; step done-conditions are not.
- Done-conditions must be externally checkable. "The other agent said it's done" is not a done-condition.
- Chatter without evidence is harmless and times out.

## Kill tests

1. Remove the watcher → relay continues.
2. Remove the architect → deterministic steps continue until the first escalation, then park.
3. Remove the coordinator → everything stops. Nothing else claims its job.
4. Remove every vendor hook → relay continues over tmux send-keys.
5. Never build a transcript observer. Not "remove later" — never ship it, or dependencies grow on it.

## Deferred / open

- Envelope and declaration field names — Wave, after reading the guides.
- Whether ack is worth having at all, or is just a second place to lie.
- Codex wake: confirm tmux send-keys reaches the input reliably; hooks are optional on top.
- Chair notification channel for the watcher.
- Retry budget default (runbook-level, overridable per step).

Nabla, stop.
