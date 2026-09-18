---
artifact: relay-contract
project: NabLarva
author: Wave
counterparty: Nabla
date: 2026-09-16
status: draft-before-guide-reconciliation
scope: envelope-and-state-semantics
schema: deliberately-unfrozen
---

# NabLarva relay — Wave contract draft

## 0. Scope

This document defines semantics and invariants for exchanges between
participants.

It does NOT yet define:

- exact filenames;
- exact YAML/JSON/frontmatter fields;
- directory layout;
- coordinator implementation;
- vendor-specific hooks;
- tmux commands;
- PTY parsing;
- final timeout values.

Existing runbook, bus, and state guides must be read before those details are
frozen.

## 1. Fundamental separation

The relay has two distinct state planes.

### Task plane

Describes what happened to the assigned work.

A participant terminates a task attempt with exactly one of:

    DONE
    FAILED
    INVALID

### Relay plane

Describes what happened to transport/activation.

Examples include:

    DELIVERED
    ACKED
    TIMEOUT

The vocabulary may change after reconciliation with existing files.

The semantic separation may not.

A dead receiver is not a failed task.
A failed delivery is not an invalid runbook step.

## 2. DONE

Meaning:

> The participant claims the requested step has been completed and supplies
> the evidence required by that step.

DONE is not established merely because an agent writes "done."

The runbook determines the expected evidence class.

Examples:

- expected file exists;
- expected diff exists;
- test command reports the required result;
- migration produced the required state;
- requested artifact was written.

The coordinator may verify deterministic evidence.

It must not interpret prose to manufacture completion.

## 3. FAILED

Meaning:

> The task remains valid, but this attempt could not complete it.

Examples:

- implementation fails tests;
- command exits unsuccessfully;
- required operation cannot presently be completed;
- participant reaches a defined execution failure.

FAILED does not imply that the runbook itself is wrong.

A retry, alternate executor, or escalation may therefore remain meaningful.

## 4. INVALID

Meaning:

> The assumptions under which the current runbook step was written no longer
> describe reality sufficiently for the step to be executed as specified.

Examples:

- required API no longer exists;
- repository architecture materially differs from the assumed architecture;
- prerequisite was invalidated by another change;
- evidence discovered during execution contradicts the runbook's premise;
- continuing would require changing the goal rather than merely retrying the
  implementation.

INVALID is deliberately different from FAILED.

FAILED says:

    I could not do the requested operation.

INVALID says:

    The requested operation is no longer the right operation under the
    discovered state.

INVALID therefore escalates toward architectural/judgment authority rather
than silently producing another execution retry.

## 5. Participants declare; coordinator does not interpret

The participant explicitly declares its task exit.

The deterministic coordinator does not read natural language and infer:

    "this sounds like INVALID"

or:

    "this probably means DONE."

Its job is structural:

    declaration present?
    declaration allowed?
    required evidence references present?
    evidence mechanically checkable?
    next transition defined?

If interpretation is necessary, execution stops at the deterministic boundary
and an escalation artifact is produced.

## 6. Evidence is separate from assertion

An exit declaration carries or references evidence.

Conceptually:

    outcome
        |
        +-- declaration
        |
        +-- evidence pointer(s)
        |
        +-- source participant
        |
        +-- runbook step identity

Exact representation remains unfrozen.

The important invariant is:

> assertion and evidence are not the same object.

## 7. Silence has no task meaning

No task outcome may be inferred from silence.

Silence does NOT mean:

    FAILED
    DONE
    INVALID
    BUSY
    DEAD

It means only:

    no qualifying response has been observed yet

Liveness is bounded externally by a deadline.

## 8. Deadline is a protocol invariant

Every delivered exchange requiring a response eventually reaches an externally
controlled deadline.

The model does not own that deadline.

Vendor hooks do not own that deadline.

PTY appearance does not own that deadline.

Transcript activity does not own that deadline.

When the deadline expires without the required acknowledgement/result, the
relay records a relay-plane timeout.

That timeout is not converted into FAILED.

This preserves the distinction:

    task failed

versus

    task executor did not return a valid result

## 9. Vendor events are hints, not truth

Hooks, notifications, transcript changes, PTY activity, tmux observations, and
other vendor/session signals may accelerate activation and observation.

They are adapter capabilities.

They are not authoritative task state.

Therefore:

    hook event -> may wake / observe
    file artifact -> durable record
    deadline -> bounds silence

Loss of a hook must degrade responsiveness, not corrupt project truth.

## 10. The poke carries no semantics

Activation should conceptually be equivalent to:

    WAKE: inspect your named inbox/request

The poke must not contain the actual task semantics when avoidable.

Meaning lives in the durable artifact.

Therefore vendor-specific activation can be replaced:

    tmux send-keys
    vendor hook
    native notification
    future API
    other adapter

without changing the task protocol.

In short:

> File means truth.
> Poke means electricity.

## 11. Escalation target belongs to the runbook

A step names a reasoning role when escalation is possible.

Conceptually:

    executor -> role: implementation
    invalid -> role: architect

The runbook maps roles to concrete endpoints.

The relay does not discover an appropriate intelligence dynamically.

If the target endpoint is absent, the escalation remains durable and pending.

No live session is required for the judgment request to remain valid.

## 12. Coordinator intelligence boundary

The coordinator is deterministic code.

It may:

- read structured state;
- advance defined transitions;
- write bus artifacts;
- invoke activation adapters;
- verify explicitly defined mechanical evidence;
- enforce deadlines;
- perform predefined retry transitions;
- create escalation artifacts.

It may not:

- reinterpret goals;
- repair ambiguous runbook instructions;
- decide that prose "probably means done";
- rewrite architecture;
- silently substitute participants;
- invent a new task when reality changes.

Ambiguity terminates deterministic progress.

It does not summon hidden intelligence inside the relay.

## 13. Optional watcher boundary

A small-model watcher may exist beside the relay.

It has observational authority only.

It may:

    inspect
    correlate
    flag
    report

It may not:

    deliver
    retry
    advance state
    rewrite
    escalate on its own authority
    change runbook state

Its death must not stop deterministic relay operation.

This yields a useful kill test:

    kill watcher
        -> relay continues

    kill architect
        -> deterministic work continues until judgment is required

    kill coordinator
        -> relay stops

These failure boundaries are intentional.

## 14. State-machine sketch

                    request
                       |
                       v
                  DELIVERED
                       |
                 acknowledgement
                       |
                       v
                    ACKED
                       |
                  participant
                    works
                       |
          +------------+------------+
          |            |            |
          v            v            v
        DONE         FAILED       INVALID
          |            |            |
      evidence       defined      architect /
       check       retry/fail     judgment
          |           policy       escalation
          v
      next step


At any response-waiting transition:

                       |
                    deadline
                       |
                       v
                    TIMEOUT

TIMEOUT belongs to the relay plane, not the three task exits.

## 15. Completion invariant

Conversation does not advance project state.

Evidence does.

A useful shorthand is:

    message sent        != progress
    agent replied       != progress
    agent says "done"   != progress
    required evidence   -> permits progress

The runbook/state machinery remains the authority for what constitutes progress.

## 16. Required reconciliation before implementation

Before freezing a schema:

1. read the existing runbook guide;
2. read the existing bus guide;
3. read the existing state-file guide;
4. map these semantics onto existing vocabulary;
5. preserve existing valid conventions;
6. identify actual conflicts rather than renaming everything;
7. Wave reviews Nabla's coordinator draft;
8. Nabla reviews this contract;
9. only then freeze the wire/file schema.

No new `_bus/` architecture should be invented merely because this document
uses conceptual names.

## Countersign status

Wave accepts the division established during the 2026-09-16 meeting:

**Wave owns**
- task exit semantics;
- relay/task state separation;
- evidence invariants;
- deadline/liveness invariants;
- semantic boundary of the envelope.

**Nabla owns**
- deterministic coordinator walk;
- activation/poke behavior;
- retry/escalation transitions;
- deadline execution behavior;
- read-only watcher boundary.

**Joint**
- reconciliation with existing guides;
- cross-review;
- final schema freeze.

The two artifacts should converge into one implementation brief only after that
reconciliation.