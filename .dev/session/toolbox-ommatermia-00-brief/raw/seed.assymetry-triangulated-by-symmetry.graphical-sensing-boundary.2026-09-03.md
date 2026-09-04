Yes. I’d fold it like this—compact enough for Symmetry to attack, but with the new creature already named.

````markdown
# SEED — `ommatermia`
working-name: ommatermia
etymology: ommatidia (compound insect eyes / clustered sensing) + terminal (CLI)
status: pre-build · telemetry-first · actuator deferred
regime: vendor-invariant local agent utility
origin: asymmetry × symmetry triangulation

## PURPOSE

`ommatermia` is not “AI mouse control”.

It is a small local sensing / intervention boundary for already-living CLI agents
(Claude Code, Codex, later others).

Primary question:

> where does a capable CLI agent actually become blind and require a human hand?

V0 should discover that boundary before automating it.

---

## CORE POSITION

Symmetry’s strongest correction is accepted:

**do not build the actuator before counting graphical interventions.**

The first executable is therefore a telemetry instrument.

Agent reaches graphical wall:

    living CLI agent
        ↓
    ommatermia flag
        ↓
    capture BEFORE state
        ↓
    human performs intervention
        ↓
    capture AFTER state
        ↓
    append observation / outcome
        ↓
    dataset tells us what deserves automation

The interruptions themselves become the specification.

---

## TWO LADDERS

Do not use one capability ladder.

### SENSE — permissive

Read-only observation is cheap and reversible.

Possible sources later:

- screenshot / window capture
- terminal state
- Zellij state
- browser DOM / accessibility
- application-specific structured interfaces

### ACT — restrictive

Order remains roughly:

1. application CLI / API
2. structured UI interface
3. bounded graphical action
4. unrestricted coordinate control — preferably never

Actuation is NOT V0.

---

## IMPORTANT DISAGREEMENT / SYNTHESIS

Symmetry proposes:

> pixels bind, text frees.

Asymmetry modifies this to:

> **pixels are evidence; text/structure is the interchange format.**

Do not force Claude/Codex to depend on raw pixels as the protocol.

But do not discard the screenshot after converting it to text either.

Proposed observation shape:

    raw evidence
      screenshot / structured state
            ↓
    sovereign sensor layer
            ↓
    normalized observation
      - textual description
      - structured elements
      - reference to raw evidence
            ↓
       living agent

Reason:

If the first vision model misreads the screen and raw evidence was discarded,
the downstream agent cannot challenge that interpretation.

---

## `verify()` MAY BE THE REAL PRODUCT

The emerging primitive is not fundamentally “eyes + mouse”.

It is:

    OBSERVE
    EXPECT
    INTERVENE
    OBSERVE
    COMPARE

Symmetry’s `#verify-is-the-product` is retained.

When automated hands eventually exist,
success is defined by observed state change matching expectation,
not by “the click command executed”.

---

## M0 — BORING EXECUTABLE

One vendor-neutral binary/script:

    ommatermia flag
    ommatermia resolve
    ommatermia latest
    ommatermia stats

stdin/stdout/files/JSON or YAML.
No agent framework required.

Claude Code / Codex adapters should be disposable wrappers around this primitive.

Example:

    ommatermia flag \
      --need click \
      --target "close modal"

Automatically records cheap available context and BEFORE evidence.

Human performs the action.

Then:

    ommatermia resolve

captures AFTER evidence and outcome.

Possible record:

```yaml
ts: ...
session: ...
agent: ...
app: ...
window: ...

need: click
target_guess: close modal

before:
  screenshot: ...
  terminal_context: ...
  structured_state: ...

human_action:
  class: ...
  note: ...

after:
  screenshot: ...
  structured_state: ...

outcome:
  resolved: true
````

Keep operator annotation tiny.
The instrument should collect whatever it can automatically.

---

## SHADOW VISION — ALLOWED EARLY

One difference from Symmetry’s brake:

A vision model MAY run from the beginning as a **shadow observer**.

It controls nothing.

For each BEFORE / AFTER pair it may emit:

* description_before
* description_after
* inferred change
* predicted needed action

Later compare this against the human intervention.

This tests whether graphical perception is actually reliable for our task class
without granting the model hands.

Raw evidence remains available.

---

## ACTUATOR GRADUATION

Do not automate merely because automation is technically possible.

Graduate only after the log exposes a repeated named task class.

Initial heuristic:

* ~20–30 real graphical interventions
* classify by application + need
* identify repeated classes
* check whether native CLI/API/a11y already solves them
* only then choose an actuator primitive

Possible result:

```
many Zellij cases      → native commands
browser cases          → DOM/a11y
application shortcuts  → programmatic adapter
genuine pixel cases    → bounded visual actuator
```

Numbers decide architecture.

---

## GUARD DESIGN — LATER

If graphical action graduates, separate:

### enforceable capability

```json
{
  "action": "click",
  "region": [100, 200, 600, 500],
  "point": [341, 287]
}
```

from:

### model commentary

```json
{
  "intent": "...",
  "reason": "...",
  "confidence": 0.91,
  "expected_result": "..."
}
```

The guard must never treat model prose or model-reported confidence as authority.

Default deny.

---

## SOVEREIGNTY

Core must remain independent of:

* Anthropic
* OpenAI
* Gemini
* any specific vision model
* any specific agent SDK

The stable thing is the local protocol and accumulated intervention evidence.

Vendor adapters are replaceable.

---

## CURRENT BUILD BOUNDARY

BUILD NOW:

* intervention flagging
* before/after capture
* session-local records
* append-only dataset
* minimal stats/classification
* optional shadow-description pipeline

DO NOT BUILD YET:

* autonomous mouse
* unrestricted keyboard injection
* generic desktop agent
* streaming video
* phone-camera sensor
* human teaching overlay
* voice/TTS

Those remain possible later branches.

---

## QUESTION FOR SYMMETRY

Please attack this merged form.

Especially:

1. Is keeping raw pixels while exposing text/structure enough to resolve your
   `#pixels-bind-text-frees` objection, or does the dependency leak remain?

2. Does shadow vision before actuator graduation create useful evidence,
   or merely contaminate the experiment?

3. What should the absolutely minimal `ommatermia` record contain so the
   operator does not become its data-entry clerk?

4. Should records be one-file-per-session, one-file-per-intervention,
   or append-only event stream + evidence directory?

5. Is `OBSERVE → EXPECT → INTERVENE → OBSERVE → COMPARE`
   the correct invariant to design around?

6. Find the cheapest falsification test for the whole creature.

No implementation yet unless a tiny executable is needed to test the ontology.

```

This now feels like the right embryo for **`ommatermia`**: not a desktop-control system, but a clustered sensory organ attached to terminal agents, learning where they actually lack senses before we grow them hands. Symmetry’s telemetry-first argument and `verify()` framing are preserved from the counter-seed. :contentReference[oaicite:0]{index=0}
```
