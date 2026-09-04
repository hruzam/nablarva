---
brief: ommatermia — sensing / intervention boundary for living CLI agents
date: 2026-09-04
version: 1.0 (canonical · folded from asymmetry seed 2026-09-03 + symmetry counter-seed 2026-09-03 + symmetry pass 2026-09-04)
authors: asymmetry (chatgpt) × symmetry (claude.ai) · operator @majkee
status: M0 = EXPERIMENT, not foundation · actuator deferred · handoff-ready for practical research
regime: vendor-invariant local utility · conceptual layer closed, practical layer next
sovereignty: HIGH — core is a boring executable + local files; no vendor primitive in the protocol
etymology: ommatidia (clustered compound-eye sensing) + terminal
---

# ommatermia

Not "AI mouse control". A small local sensing organ attached to already-living CLI agents
(Claude Code, Codex, later others), whose first job is to discover WHERE those agents go blind
before anyone grows them hands.

## AXIOMS  (#grep · falsifiable · strike before reading further)
- #ax1-symptom-not-gap — a graphical intervention is a symptom of a missing programmatic interface,
    not a missing agent capability. Falsified if the log repeatedly names an app with no CLI/API/a11y path.
- #ax2-two-ladders — sensing and acting have different cost gradients; never one ladder.
- #ax3-text-is-interchange — text/structure is the agent interface; pixels are dispute evidence only.
    Falsified if a text-only consumer cannot state `target` + `expect` from the log's descriptions.
- #ax4-verify-is-authored — the sovereign, authored part is `verify()`; the actuator is a borrowed dumb tool.
- #ax5-numbers-decide — nothing graduates on possibility; only on counted, classified interventions.

## INVARIANT  (#invariant)
    OBSERVE → EXPECT → INTERVENE → OBSERVE → COMPARE
- `target` = where I think the intervention belongs.
- `expect` = what reality should look like afterward.
- Only `expect` gives `verify()` something independent to test. Therefore `--expect` is REQUIRED at flag time.
    A flag without expectation is a log line, not an experiment.

## TWO LADDERS  (#two-ladders)
SENSE — permissive. Read-only, cheap, reversible. Sources (later): window capture, terminal state,
    Zellij state, browser DOM/a11y, app-specific structured interfaces.
ACT — restrictive. 1 app CLI/API → 2 structured UI → 3 bounded graphical → 4 unrestricted coordinates (never).
    Actuation is NOT M0.

## OBSERVATION CONTRACT  (#observation)
    raw evidence (screenshot / structured state)
          ↓
    sovereign sensor layer
          ↓
    normalized observation { description · structured elements · ref → raw evidence }
          ↓
    living agent
- #pixels-optional — the raw reference is a path an agent MAY open to challenge a description.
    No adapter may REQUIRE it. Test: a text-only consumer (no vision) must pass the same tasks.
- #evidence-tier — pixels are generated + gitignored. Observations/events are generated + committed.

## M0 — THE BORING EXECUTABLE  (#m0)
One vendor-neutral binary/script. stdin/stdout, files, JSON/YAML. No agent framework.
    ommatermia flag --need <click|type|read> --target "<guess>" --expect "<state afterward>"
    ommatermia resolve [done|done-differently|could-not|not-needed]
    ommatermia latest
    ommatermia stats
- `flag` auto-captures BEFORE evidence + whatever cheap context exists (session, agent, focused app/window).
- `resolve` auto-captures AFTER evidence. Bare `resolve` = `done`. Zero keystrokes on the common path.
- #no-clerk — operator input is the resolution enum ONLY. No mandatory free-text. Anything not captured
    automatically is not captured. A field the operator must fill is how the instrument dies.
- Claude Code / Codex adapters (skill, subagent, hook) are disposable wrappers. Neither runtime knows
    screenshots exist.

## STORAGE  (#storage)
- Append-only EVENT STREAM + evidence directory. Not one-file-per-session (that is Costa's dialogue shape;
    this is telemetry, and `stats` wants flat events).
- Sovereignty gradient:
    1. schema  — authored / sovereign
    2. events  — generated + committed
    3. pixels  — generated + gitignored
Minimal event:
```yaml
ts: …
session: …
agent: …
app: …            # auto
window: …         # auto
need: click
target: "close modal"
expect: "modal closed, editor focused"
before: {evidence_ref: …, structured_state: …}
shadow: {sealed_ref: …}          # optional, see below
after:  {evidence_ref: …, structured_state: …}
resolution: done | done-differently | could-not | not-needed
```

## SHADOW VISION  (#shadow · allowed in M0 · controls nothing)
A vision model MAY run from day one as a shadow observer. Per flag it emits
description_before, predicted_action, predicted_after; at resolve, description_after, inferred_change.
- #sealed — the prediction is written at FLAG time and SEALED until human resolution. The operator never
    reads it before acting. (Otherwise the human label is anchored and the measurement is void.
    Held-out-set discipline, per the SkillOpt lesson.)
- #cost-bounded — days, not a second project. If shadow threatens to become the work, drop it; the flag
    instrument stands alone.
- Shadow-vs-human-action is the first SCOREABLE task class this ecosystem has produced. That is why it
    is admitted without loosening actuator restraint.

## FALSIFICATION GATE  (#gate · prominent · M0 is an experiment, not automatically M1's foundation)
Run ~2 weeks in real work, flag only (shadow optional).
STOP building ommatermia as a graphical-sensing system if:
- fewer than ~10 genuine flags occur, OR
- essentially all resolutions reduce to "native/programmatic path already existed".
The result is still valuable: we found a documentation / interface-discovery problem, not a missing sense.
Cheaper pre-test (no vision spend): hand Codex only the human one-line descriptions from the log and ask
for `target` + `expect`. If it cannot, #ax3 falls before any vision model is bought.

## ACTUATOR GRADUATION  (#graduation · later)
Only after ~20–30 real interventions, classified by app × need, with a REPEATED named class,
AND after checking native CLI/API/a11y does not already solve it. Expected sort:
    Zellij cases → native commands · browser → DOM/a11y · app shortcuts → programmatic adapter ·
    genuine pixel cases → bounded visual actuator.
Numbers decide architecture.

## GUARD DESIGN  (#guard · later · only if graphical action graduates)
Separate ENFORCEABLE `{action, region, point}` from COMMENTARY `{intent, reason, confidence, expected_result}`.
The guard never treats model prose or model-reported confidence as authority. Default deny.
`expected_result` here is the same `expect` field — `verify()` compares against it.

## BUILD BOUNDARY  (#boundary)
BUILD NOW: flag · before/after capture · event stream + evidence dir · stats/classification · optional sealed shadow.
NOT YET: autonomous mouse · unrestricted keyboard injection · generic desktop agent · streaming video ·
    phone-camera sensor · human teaching overlay · voice/TTS. Possible later branches; not this creature yet.

## HANDOFF → practical research (asymmetry, next layer)  (#handoff)
Owed by the practical layer, NOT resolved here:
- current Arch / Wayland vs X11 primitives for capture, focused-window identification, structured state;
- existing projects to steal primitives from (computer-use loops, a11y bridges, screenshot/portal tools);
- Claude Code + Codex adapter shape around the same binary;
- cheapest M0 implementation.
Constraint carried down: none of the above may leak a vendor primitive into the protocol (#ax3, #pixels-optional).

## CHANGELOG / LINEAGE  (#lineage)
- 2026-09-03 asymmetry seed: visual-servo loop + capability ladder + proposal object + safety boundary.
- 2026-09-03 symmetry counter-seed: count before hands (#nav-flag) · two ladders · pixels-bind-text-frees ·
    verify-is-the-product · prose-in-the-guard.
- 2026-09-03 asymmetry merge: name `ommatermia` · pixels-as-evidence modification · shadow vision · M0 verbs.
- 2026-09-04 symmetry pass, folded here:
    · WITHDRAWN #brake-no-vision-model — shadow admitted because SEALED prediction yields a falsifiable
      measurement without granting actuation. Actuator restraint unchanged.
    · CORRECTED #boring-binary storage — one-file-per-session was a reflex import from Costa; replaced by
      append-only event stream + evidence dir.
    · ADDED mandatory `--expect` (turns log into experiment).
    · ADDED resolution enum, no-clerk rule, three-tier sovereignty gradient, text-only-consumer test.
- Kept separate from: swarm/composition study · Costa protocol (shape borrowed, not merged).
