---
title: Phone console — fast build direction and retained native option
date: '2026-10-30'
author: Oraculum
status: uncanonical; operator-requested preservation and planning
runtime_validation: not performed
---

# Phone console — keep the fast path and the later option

Majkee requested a fast vendor-neutral remote-session interface whose useful parts
can later extend Nablarva. He accepted keeping its code inside Nablarva and asked
that the earlier native architecture not be lost. This backlog remains under his
control; these notes do not create a second project authority or active session.

## Current build direction

Qualify a small browser console around an existing terminal gateway such as
[ttyd](https://github.com/tsl0922/ttyd), reachable through authenticated tailnet
HTTPS. Sessions remain on the workstation. First prove one disposable session on
the Redmi: typing, Czech text, scrolling, special keys, app switching and reconnect.
Then add the durable composer and saved vault. This is a proposed integration,
not an installed application or a qualified transport.

Keep terminal transport, session operations, draft storage, vault export/import
and speech behind explicit small interfaces so a later frontend can reuse them.
Ovitmugen remains the owner of view/layout and protected process lifetime. The
phone adapter uses existing public operations; it does not become another manager.
Foreground human terminal input is distinct from future regulated room delivery.

Code stays in Nablarva; `apps/session-console/` is the proposed component location.
ttyd remains an external dependency. Deployment recipes and machine-specific wiring
belong in ia-sync through the reviewed publication path. Exact interfaces and
package layout remain implementation-design work.

## Earlier architecture — preserved verbatim as the later native option

This is the table Majkee explicitly requested to retain. It is not the stack
commitment for the fast browser build.

| Part | Recommendation |
|---|---|
| Android app | Kotlin, Compose UI, existing terminal component, SSH library, Room storage |
| Host integration | Small Python helper beside the existing tmux machinery |
| Sessions | Stay on the workstation; ovitmugen retains lifecycle protection |
| Vault | Dedicated host storage for shortcuts/prompts/files, plus persistent phone drafts |
| Speech | Replaceable recognition/playback adapters |
| Docker | Optional later packaging for vault/web or speech services |
| Kubernetes | Defer; keep service interfaces replaceable without making sessions depend on containers |

The Python helper is a candidate adapter language, not permission to duplicate
session management, composition or observation. A component language does not settle
the broker-language docket. Kubernetes readiness means replaceable service boundaries,
not a promise that workstation sessions migrate with containers.

## Behaviour that survives either frontend

- Vault holds shortcuts, prompts and files; terminal history is separate.
- Unsent drafts persist until deliberately handled. Temporary tray items support
  manual clearing or a 30-minute expiry; explicitly saved vault items persist.
- Show the target before sending. Paste and Enter are separate; uncertain input is
  never automatically replayed after reconnect.
- At most ten primary command buttons, with a separate terminal key palette.
- Native CLI permission interaction first; structured approval cards require a
  supported exact-request binding.
- Speech produces editable drafts or reads selected text. Contextual correction is
  explicit. English first, Czech next as available, Ukrainian later; device support
  remains unverified. Keyboard dictation is the initial fast-path candidate.
- Do not wait for unbuilt Termbrana preparation, VIST/spine or room-delivery APIs.
  Reuse accepted interfaces, keep gaps visible and qualify extensions with their owners.

## Required follow-through after implementation and verification

Majkee explicitly requested: call Houston again after the implementation/testing
process to help wire the result into project documentation. The executing head must
carry this as an open closure item. It is a task dependency, not a timed automation.

Give Houston the actual code and interface map, candidate/release hashes, independent
test evidence, runtime/install homes and known limitations. Request a bounded
`card: consult` on documentation integration. If wrapper-mechanics editing is needed,
assign the corresponding bounded audit scope explicitly.

Expected disposition:

1. Existing phone-organ body owns the actual product/engine/storage contract.
2. `docs/ARCHITECTURE.md` gets only changed cross-organ seams and owners.
3. `PROJECT-DESIGN.md` and, where warranted, `PROJECT.yaml` point to the actual
   implementation and build/run entry; stale closed-session pointers are reconciled.
4. Component README/decision ledger cover build/run and technical rationale.
5. ia-sync device cards, logs and install wiring reflect changes actually deployed.
6. Remaining native/container ideas stay here, visibly deferred; no untested proposal
   is promoted as working behaviour. The execution head retains integration/closure.

## Related evidence

- [V0 extension note](09_V0_PHONE_EXTENSION_2026-10-30.md)
- [Independent test schedule](../../../meshup/stridularium.mobile-console.2026-09-29/raw/test-schedule.oraculum.2026-10-30.md)
- [Existing phone body](../../../docs/organs/stridularium.md)
- [Current whole-animal architecture](../../../docs/ARCHITECTURE.md)
- [Earlier repository-fit review](07_NABLARVA_UI_FIT_REVIEW_2026-10-25.md)

The existing path uses the retired cultural name under L24; retaining the path does
not reinstate the name. This note records the conversation and inspected local
evidence, not implementation, deployment or a fresh independent acceptance result.
