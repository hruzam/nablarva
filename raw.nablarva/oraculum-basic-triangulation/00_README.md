# nabLarva — Wave conversation export

**Date:** 2026-08-05  
**Status:** architecture and research synthesis; not an implementation specification  
**Source basis:** the shared triangulation brief and the subsequent Wave–majkee discussion  
**Purpose:** preserve the full conceptual current, including pushback, parked branches, and later-testable forks

## What this export contains

This report set preserves the evolution of the design rather than presenting only the last answer.

1. `01_ARCHITECTURE_ROOM_AND_BROKER.md`  
   The original clean-room architecture: peer sessions, brokered room, append-only journal, directed projections, private lines, anti-drift control, failure recovery, and V1 cut.

2. `02_DRILLER_TOKENIZATION_AND_RECONSTRUCTION.md`  
   The output-cleaning discussion: hard prefilters, reversible tokenization, sparse vector/tensor representation, synchronization, transforms, and mathematical reconstruction.

3. `03_COST_COMPLEXITY_AND_STAGED_DECISION.md`  
   Practical resource cost, where the real complexity lies, and why the full generalized tokenizer engine is parked rather than discarded.

4. `04_LABORATORY_OBSERVABILITY_AND_EXPERIMENTS.md`  
   The “hacker” current: legitimate instrumentation, observable layers, skill/tool activation signals, controlled experiments, replay, and promotion of proven findings into production.

5. `05_DECISION_LEDGER_PARKED_BRANCHES_AND_FORKS.md`  
   A durable ledger of decisions, objections, rejected shortcuts, parked ideas, unresolved questions, and possible later branches.

6. `06_ORACULUM_TRANSMISSION.md`  
   Message-ready text intended for transmission to Oraculum after the initial architecture proposal already sent.

7. `07_AI_HANDOFF.md`  
   A concise state handoff for another agent or a later development thread.

8. `nablarva.wave.full-report.2026-08-05.md`  
   A combined report containing all substantive chapters.

## Central synthesis

nabLarva should be understood as two related but distinct systems:

```text
PRODUCTION ROOM
    Independent agent sessions
          ↓
    thin session adapters
          ↓
    clean normalized events
          ↓
    brokered append-only room journal
          ↓
    sparse participant-specific views

RESEARCH LABORATORY
    controlled CLI scenarios
          ↓
    native events + PTY + OS observations
          ↓
    synchronized evidence bundle
          ↓
    replay and extractor comparison
          ↓
    proven versioned adapter rules
```

The production system should remain conservative and lightweight. The laboratory is where broad observation, experimental tokenization, statistical transforms, and alternative reconstruction strategies can be explored safely.

## Current design posture

The following are provisionally selected for V1:

- one central room broker per active room or host;
- independent live CLI sessions rooted in their own repositories;
- adapter-owned PTYs;
- append-only room journal;
- explicit addressing and recipient-filtered delivery;
- versioned goal and bounded consultation leases;
- immutable raw terminal capture;
- terminal-state normalization;
- narrow vendor profiles;
- a small stateful extraction layer;
- an experimental laboratory kept outside the production path.

The following are deliberately parked:

- dense tensor infrastructure;
- neural or embedding-based token classification;
- LLM-based output cleaning;
- a central `drillerd` service;
- a universal transformation language;
- full machine-level tracing during ordinary production use;
- automatic inference presented as certainty;
- interception of encrypted provider traffic.

## Governing principle

> Observe first. Preserve raw truth. Prefer declared semantic events. Infer conservatively. Promote only repeatable findings. Keep production smaller than the laboratory.
