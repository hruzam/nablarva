---
for: Cartan (convergence) — fold into .dev/session/AGENTS.PROJECT-DESIGN.md
from: symmetry · relay-design thread 2026-09-30/10-01 · operator @majkee
cites: flag.md L13 (gaveled 2026-10-01) · L2 · L3 · L4 · L11 · L12 · KEYS CODE
note: per the doc's Document role, these stay proposals unless a cited decision supports them. Naming is L13's.
---

### into § 1.1 nablarva *(itself)*

- display form **nab∫ar∇a** — ∫ U+222B INTEGRAL, ∇ U+2207 NABLA; display only. Slugs, paths,
  commands and grep stay ASCII `nablarva` (L13). Voice input and phone keyboards don't produce ∫
  reliably, and lookalikes (ʃ U+0283, ▽ U+25BD, 𝛁 U+1D6C1) would silently split the name.

---

## 3.6. termpanum *(toolbox)*

- origin `terminal` × Latin `tympanum` (the insect ear) — it hears the sessions; stridularium calls you
- observation lab: records what living CLI sessions do (hooks, process tree, PTY liveness) as
  normalized events with source and certainty (doc 04 §4.13 + termbrana's provenance grade)
- read-only by construction: never types into a session (L4), never injects context; the onion
  study's context bus (ch. 6) belongs to stridulatrix
- toward the relay: discrete states only (idle · working · waiting · exited), never meaning read
  off the screen
- home `toolbox/termpanum/` (L12), its own tmux window, never the window it observes
- access: scripts and plain files first, every command returns a path; an optional thin read-only
  MCP for seats without a shell
- adopts the onion study (PTY research), the unilarvatrix build plan (builder draft) and doc 04's
  lab (`larva-lab` → termpanum)
- source: [brief substrate](toolbox-termpanum-00-brief/raw/brief-substrate-for-RUNBOOK.termpanum.2026-10-01.md)

## 3.7. stridulatrix *(broker + CLI)*

- origin: Latin-style agent noun from `stridulate`, `-trix` = she who does it (the -trix of
  unikuklatrix) — the organ that makes the call. Chosen over larvad/larva and stridulator to
  survive voice input (L13); voice test passed 2026-10-01
- the room's broker and its CLI: single writer of the journal (S1), per-participant cursors (S2),
  delivery through each adapter's own PTY (L3), never send-keys (L4)
- owns everything that writes into sessions, including the onion study's context bus (ch. 6)
- reads termpanum's state events from its own cursor; no pipe to name
- lifecycle (docket 4) and journal store (docket 5) stay open. The full design belongs to the
  architecture session (`nablarva-03-app-architecture`); this entry fixes only the name and the
  boundary
- commands: one family under the claviature rule; prefix open (`sx` is an X-session starter in
  Arch's repos)

## 3.8. stridularium *(phone app)*

- origin: Latin-style `stridularium`, the insect's chirping organ — the part that calls you.
  L2 stage 3, the human's door into the room (L13)
- thin lens: sessions live on the host; the phone renders and sends input; attaching is advisory
  (presence-board), detaching never closes a bed
- app-scoped reach: an app-owned vault the operator scopes; a session may switch the view inside
  it, never reach past it
- navigation: carousel cards + breadcrumbs; the host renders text, the phone shows cards; no
  terminal emulator on the phone
- voice: Ptyra's voice-to-CLI pipeline moved to the phone; one buffer per target on the host;
  release is the only way into a CLI
- bridge (O2, majkee's pick): hardened Tailscale + Termux, then mosh; a VPS relay as fallback
- source: [stridularium note](nablarva-X0-restarted/raw/note.stridularium.2026-10-01.md)
