---
kind: historical-documentary-annotation
author: nablarva.cartan
date: 2026-11-14
sources: preparation.sources.2026-11-14.json
qualification: historical C04 only; no new runtime test, replay or universal classifier qualification
---

# C04 — successful queue acceptance with different observation accuracy

All event times below are UTC on **2026-11-13**. `cases` and `inventory` identify the immutable
Git inputs in the source-pin JSON. The local inputs were read/hash-checked on the packet's
observation date; this does not refresh their event time or establish durable/cross-host custody.
The selected receipt extracts are historical extracts, not a new audit of complete native histories.

## Meaning and oracle

| Layer | What the cited evidence can establish | Independent comparison and limit |
|---|---|---|
| Native activity | A setup turn's user/start and completed events bracket activity | Receiver receipt extract, independent of helper `@state`; time inside that interval is not proof of continuous CPU work or semantic progress |
| Reported observation | Exact sampled `ready`/`busy` value tied to an attempt | Compare with the native interval and sample time; metadata's prior `@state` may be stale, not a live native state or authenticated identity |
| Controller/carrier action | Helper selected the queue route and its invocation returned queue acceptance | Sender result and selected log, separate from receiver events; this was a prototype's branch, not an adopted VIST controller policy or proof of delivery |
| Receiver receipt | Later receiving user event, turn and nonce final correlate the requested work | Compare message ID and expected nonce with the separate selected receiver extract; receipt is not independent authentication or proof of artifact quality |

## r1 — observation failure survives successful carrier/work result

Message `c08r1-04-90c4f4e6`; receiver thread `01a1d496-8940-7941-9d4b-97564cb5fd22`, PID189655,
pane%19. Helper `06cc9b4` and signature set hashes are pinned in `inventory` P6/P9.

| UTC | Layer | Source and annotation |
|---|---|---|
| 12:07:57.070 | Native activity | R1 receipt case04-setup: setup user event; turn `01a1d4ce-ad52-7112-ac5b-1855b95db180` |
| 12:08:11.321060 | Prior observation | R1 `04-busy-before-queued.meta`: `ready` still belongs to the **setup** attempt at12:07:57Z |
| 12:08:11.326575–12:08:11.642815 | Carrier call/observation | R1 `results.jsonl`, case04: exit0, queue ID `01a1d4ce-e656-7980-8f85-cb409458eefc`; selected log has second precision12:08:11Z. `sample_meta` reports `ready` for the **new** attempt |
| 12:08:11.647154 | Post-call observation | R1 `04-after.meta`: `ready`, now correlated with the new message ID |
| 12:08:16.549 | Native activity | Setup turn completed according to R1 receipt extract; the entire queue invocation preceded it |
| 12:08:16.596 | Receiver event | R1 receipt case04: one receiving user event; turn `01a1d4ce-f9a8-7d52-8d67-26493cc3d097` |
| 12:08:22.194 | Worked receipt | Matching final `copy-dbf673b9ec`; completion12:08:22.248Z |

The source's r1 C04 expectation required truthful busy observation. Its result is **carrier/work
success and observation failure**, not an overall classifier PASS. A later nonce cannot repair the
earlier false-ready observation.

## r2 — scoped busy observation, queue acceptance, later receipt

Message `c08r2-04-19820a5b`; rebound receiver thread `01a1d4de-ecc1-75d1-ab32-03caf35f72a7`,
PID356560, same pane%19. These are **different native lifetimes**. Helper `22d5008` and signatures
are `inventory` P7/P10, not the r1 build.

| UTC | Layer | Source and annotation |
|---|---|---|
| 12:31:06.680 / 12:31:06.725 | Native activity | R2 receipt extract: setup turn start/user; turn `01a1d4e3-e1b0-76f0-9b02-5e1b7f70847e` |
| 12:31:23.431650 | Prior observation | R2 `04-busy-before.meta`: old `ready` still names the setup attempt; do not label this the corrected acceptance observation |
| 12:31:23.436264–12:31:23.777822 | Carrier call/observation | R2 results case04: exit0 in0.342s, queue ID `01a1d4e4-245b-79e3-85fd-874265461e9e`, `sample_meta=busy` for the new attempt; selected log precision12:31:23Z |
| 12:31:23.783450 | Post-call observation | R2 `04-after.meta`: `busy` correlated with the new message ID |
| 12:31:28.041 | Native activity | Setup turn completed; its interval still included the earlier queue call |
| 12:31:28.058 / 12:31:28.102 | Receiver event | Receiving turn start/user; turn `01a1d4e4-352b-7873-8765-cae739e4d91e` |
| 12:31:32.930 | Worked receipt | Matching final `copy-78e2150fb3`; completion12:31:32.956Z |

This supports the source's **one scoped r2 C04 correlation**. It does not qualify every busy frame,
make the window-activity heuristic authoritative, or prove a latency distribution. In particular,
`.777822` is the sender wrapper's return timestamp; the queue log itself has only second precision.

## Provenance and missingness

R1=`/tmp/vc08r1.tkz50zbf/`; R2=`/tmp/vc08r2.kk50sqqh/`. Exact source-input hashes and byte lengths
are in `preparation.sources.2026-11-14.json`, `local_c04_inputs`. This packet selects scalar metadata,
IDs, event times and test nonce finals, without importing raw screens, full transcripts or settings.
The annotation is derived by the packet author and requires non-author review against those sources.

The `cases` observed r1/r2 tables and `inventory` row1 corroborate the comparison. Installed
Codex0.169.0/Claude2.1.323 probes do not prove event-time executable versions for these running
processes. Earlier metadata lacks process start ticks; no complete lifetime bridge is inferred.
No portable redacted ANSI/cursor fixture or native classifier replay is produced by this timeline.
Historical data correlation and fresh runtime qualification remain separate.
