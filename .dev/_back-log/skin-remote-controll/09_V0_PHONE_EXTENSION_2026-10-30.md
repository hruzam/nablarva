---
title: Nablarva v0 — phone-client extension candidate
date: '2026-10-30'
author: Oraculum
status: uncanonical addendum; not merged into historical v0 or project canon
---

# V0 extension candidate — a replaceable phone client

Majkee asked that useful parts of the phone discussion pass toward v0 rather than
be lost. The referenced draft is preserved at:

`nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.md`

Its recorded SHA-256 is
`00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0`.
`docs/ARCHITECTURE.md` identifies it as a candidate. It is absent from the current
working tree. This forward addendum preserves that historical source; it does not
reconstruct a new authoritative copy or adopt all of its older mechanisms.

## Additions to carry into a future v0 revision

| V0 area | Proposed addition | Boundary |
|---|---|---|
| UI / gates | A browser or Android client calls explicit public operations for session navigation and user interaction. | Ovitmugen retains lifecycle/view ownership; no parallel phone session manager. |
| Services | Replaceable vault gateway and STT/TTS adapters can serve several frontends. | Service language and deployment are component choices; the host-local tmux owner remains explicit. |
| Substrate lifetimes | Distinguish phone draft/cache, deliberately saved prompts/files, and shared observations. | Each has an authoritative writer/home and retention; a saved prompt is not room truth. |
| Composition and relay | Foreground human terminal input is one path; structured preparation/submission and regulated delivery are separate owned paths. | Termbrana composes/submits; stridulatrix sends when that path is qualified. No phone-specific room sender. |
| Build/install | Keep the client independently buildable inside Nablarva; deploy through ia-sync's reviewed wiring. | Runtime independence does not require a new repository. |
| Later deployment | Containerize a replaceable gateway or speech worker if operational need appears. | Sessions remain on identified workstations; no Kubernetes dependency for the first client. |

The exact retained Kotlin/Compose/Room and Python recommendations have one home in
the [phone-direction note](08_PHONE_CONSOLE_DIRECTION_2026-10-30.md#earlier-architecture--preserved-verbatim-as-the-later-native-option).
The fast build tries a browser terminal first; these native choices remain available
if measured keyboard, lifecycle or storage requirements justify them.

## Reconciliation needed when v0 is next edited

The historical v0 proposes fixed XDG homes, a common event format, a send-keys
doorbell and a strict pure-Python-service split. Those statements are not authority
for the new client. Current flag and architecture take precedence:

- Shared paths follow the settings-resolved direction in architecture §4.8;
  configuration mechanism/ownership remains open.
- VIST and the shared spine do not yet provide an adopted general event API.
- Regulated delivery retains L3/L4/L17/L21 boundaries. Direct human terminal input
  is a distinct carrier, not a general bypass.
- Existing ovitmugen is Python; the proposed phone adapter does not authorize a
  rewrite of that organ or settle the whole project's language.

At the requested post-build Houston check, classify these additions as implemented,
still proposed, deferred or contradicted by evidence. Promote only the surviving
facts to their existing documentation homes; the executing head owns that fold.
