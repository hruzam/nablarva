---
brief: nablarva-token-economy (file bus vs UI/PTY relay)
date: 2026-09-14
thread: symmetry.agentive-collaboration
author: symmetry
regime: informative — NOT design; ground later in the Nablarva practical project
status: released after buffer · sources: vendor docs + community reports (Sept 2026)
sovereignty: HIGH — cost model is vendor-invariant; only the multipliers are weather
---

# Nablarva — token economy of a file-mediated bus between two heads

## 0. Axioms (strike any that misread you)

1. Nablarva = two heads (Claude Code, Codex CLI) exchanging via markdown files; human moves from **wire** to **gate**.
2. The heads spawn their own workers for routine work; workers are out of scope for this brief.
3. A handoff message is short (~100–300 tokens): "done my part, continue" / "you code, I release testers".
4. The question was: is file-relay meaningfully more expensive than human copy-paste or PTY scraping? Not: how to design the protocol.
5. Vendors differ → no shared cache between heads. Each head pays its own freight.
6. Markdown preferred over JSON for bus files.
7. Loop budgets ("ten loops then report") are a later mechanism, not this brief.
8. Costs quoted are API-layer; Max subscription hides them but the ratios still govern context health.

## 1. Cost model — one ratio

At the API layer there is **no separate rate** for "output to UI" vs "write to file" vs "read a file". Output is output tokens; a file read is input tokens. What differs is *residency*: UI content stays in context for the session; file content leaves and returns only when read — and every re-read is a fresh input charge.

The only real curve is **cache**:

| event | multiplier vs base input |
|---|---|
| cache write | ~1.25× |
| cache read (most models) | ~0.10× |
| cache read (Fable/Mythos 5.1) | ~0.025× |
| **miss vs hit** | **~12.5×** |

Sources: Anthropic pricing/prompt-caching docs; tokencalculator.ai break-even write-up. Write premium is repaid after ~2 reads.

Corollary you already reached yourself: **repeating text in a prompt and re-reading a file are the same cost event.** Partial reads (last N lines) are cheap only because they are *short* repetitions. Reading *different* slices each time rewrites the middle of context and breaks cache downstream.

## 2. Scaling — 10k → 1M

Assume one handoff ≈ 200 tokens, read once by the receiving head.

| head context | one handoff as % of context | 10 handoffs |
|---|---|---|
| 10k | 2.0 % | 20 % |
| 50k | 0.4 % | 4 % |
| 100k | 0.2 % | 2 % |
| 500k | 0.04 % | 0.4 % |
| 1M | 0.02 % | 0.2 % |

Bus cost is **flat**; head context **grows**. The ratio only improves with scale. At 1M the spend is the head's own accumulation, not the messages.

→ **Brake belongs on context growth, not on exchange count.** (Loop budget is still worth having — for runaway *behaviour*, not for cost.)

## 3. File bus vs alternatives — verdict

| relay | token cost | hidden cost |
|---|---|---|
| human copy-paste | zero API | your time; but it was a natural rate limiter |
| PTY scraping | pay to ingest prompt decoration, ANSI, spinner frames, then pay again to filter | filter maintenance hell; brittle across CLIs |
| file bus (md) | ~200 tok/handoff | none structural; needs notification + read discipline |

**File bus wins; not close.** PTY ruled out: you would be paying tokens for garbage twice.

## 4. Edge cases — community-reported, re-filtered for Nablarva

Generic list first (single long session), then what each *means* for two heads on a bus.

- **TTL mismatch** — agent fires less often than cache lifetime → pays write premium every call, never collects a read; ~25 % *worse* than no caching. (technspire, alejandro-ao)
  → Nablarva: a head that idles waiting on the other head will cold-start. Notification latency is a cache cost.

- **Pruning costs more than it saves** — deleting old tool results from mid-context changes the prefix at that point; everything after may reprocess. (earendil)
  → Nablarva: **this flips.** Harbour *is* pruning done right — evidence survives on disk, so rebuild-from-files is the correct move, not a loss. Don't prune in-context; harbour instead.

- **Live data inside cached prefix** — reasoning over stale tool output. (unscriptedcoding)
  → Nablarva: bus files are live by definition. Read fresh every time; never pin them into the system block.

- **Model-specific cache** — entries don't cross models or vendors. (unscriptedcoding)
  → Nablarva: baseline doubles; each head builds its own. Not a bug, a floor.

- **Non-deterministic serialization** — unordered JSON keys, float formatting, hash-order sets → prompt not byte-stable → cache not stable. (alejandro-ao)
  → Nablarva: **markdown with stable header + append-only body** keeps the reader's prefix intact. Vindicates md over JSON.

- **System-prompt-only caching beat full-context caching** — naive full caching writes cache for tool results nobody reuses, raising latency. (arXiv 2601.06007)
  → Nablarva: cache the head's doctrine/canon; leave bus reads and tool results uncached.

- **Compaction = one full-price call** at the start of the compacted session. (alejandro-ao)
  → Nablarva: budget one cold call per harbour; it's the price of sleep.

## 5. Protective mechanisms (from the above, not invented)

- Append-only bus files; stable header; no in-place rewrites.
- Handoff must carry a **state change**, not acknowledgement. "Continue" is fine; "let's discuss how" is the burn.
- Bus outside cached region; canon inside it.
- Harbour on cadence, not exhaustion (#harbour-is-sleep).
- Loop budget as a later, separate mechanism: N exchanges → report to gate → buy more.

## 6. Underlined — not resolved

- **Auditor sub-agent** ("did we forget something?"): reads the *bus* or the heads' own *state*? Unsettled. Reading the bus is cheap and append-only; reading head state re-enters the cache-break problem.
- Notification transport (hooks vs polling) — out of scope here; affects TTL edge case only.
- Whether a third/fourth head fits the same bus or needs a hub file — parked.

---
Created by Symmetry claude.ai, Ostrava 2026-09-14.
