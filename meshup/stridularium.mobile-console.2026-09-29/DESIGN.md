# DESIGN — stridularium.mobile-console.2026-09-29

`scope: the human's door into the room (L2 stage 3) — a thin mobile lens over sessions living on the workstation; an organ with a toolbox-grade console core.`
`status: design input only · two origins kept whole · majkee drafts the app in stridularium-00-design (L14 D5) · origin 2026-09-29 (Cartan's IDEA, earliest file)`
`names: stridularium (L13) · k0k0nV3R / coconvergence (working name) — culture layer; disk ASCII.`
`living draft: .dev/session/AGENTS.stridularium-design.md — this file is the fixed registry entry; it points, never duplicates.`
`class: ORGAN of the animal (first with a client), not a toolbox. Code home proposed nablarva/stridularium/{android,host}; final home = nablarva-03-app-architecture.`

## Shape

Two layers, one test — *does it run with nablarva absent and meet it at a file boundary?*

| layer | content | nablarva-absent | origin |
|---|---|---|---|
| console core | host picker · host › session › window › pane tree · live terminal · text tray (select → collect → arrange → destination → release) · detach/reconnect · services menu (preview · files · status · notifications) | yes — any tmux host over SSH | Cartan IDEA 09-29 |
| organ layer | gavel feed (7 triggers) · per-target buffers on the host, release only through stridulatrix + adapter PTY (L3/L4) · host-side speech-to-text · carousel + breadcrumbs host › room › seat › session | no — needs stridulatrix's journal | Symmetry note 09-30/10-01 |

Host-side **engine** (L14 D6): hosts the processes; the app sends commands and prompts, receives output; never Android functions outside the app. Reach on the device = app + its files; operator-scoped vault as later extension.

Bridge (O2 lean, majkee): harden Tailscale + Termux (battery, autostart, always-on VPN, wake-lock) → mosh → phone attaches to its own view session `<slug>--phone`, `window-size latest`. Fallback not chosen: VPS relay. Rejected: vendor-hosted page.

## Phases

| phase | origin | state | source |
|---|---|---|---|
| Phone lens note — thin client, buffer, tmux wrapper | 2026-09-30 | superseded by stridularium note | `raw/note.phone-lens.2026-09-30.md` |
| k0k0nV3R IDEA — console, tray, services, persistence, feasibility gates 1–5 (Galaxy baseline done 09-29) | 2026-09-29 | live, planning only | `raw/IDEA.k0k0nV3R.2026-09-29.md` |
| stridularium note — door, DECIDED shape, bridge O2, carousel, voice, gavel feed, delta worth building | 2026-10-01 | live, input to 03 | `raw/note.stridularium.2026-10-01.md` |
| L13 naming · L14 D5/D6 locks | 2026-10-01/02 | locked | `.dev/session/flag.md` |
| Console core as first slice (toolbox-grade, usable before stridulatrix exists) | 2026-10-01 | proposed (oraculum) | `AGENTS.stridularium-design.md` |

## The tension (not resolved here)

Cartan: open the **actual terminal** on the phone, native selection, key row, copy mode. Symmetry: **no terminal emulator on the phone** — the host renders text, the phone shows cards. Both agree sessions live on the host and the tray/buffer is the delta no vendor app gives. → HYPOTHESES h1.

## Boundaries

stage 3 · Claude↔Codex seam (vendor-neutral console; agent identity never invented from process hints) · room (reads stridulatrix's journal; writes only through it) · naming (L13) · termpanum supplies states, never meaning.

## Sources (3 + 1 pointer)

- raw/IDEA.k0k0nV3R.2026-09-29.md — copied from ~/unikuklatrix/k0k0nV3R/IDEA.md 2026-10-02 (origin header inside); folder left as stub pointer
- raw/note.phone-lens.2026-09-30.md — materialized 2026-10-02 from the formerly untracked X0 input (never committed before → no git rename history; its frontmatter 'supersedes'/'home' lines are the origin record)
- raw/note.stridularium.2026-10-01.md — moved from .dev/session/nablarva-X0-restarted/raw/ (git history = origin)
- .dev/session/nablarva-X0-restarted/raw/design-chapters.for-cartan.2026-10-01.md §3.8 — stays with Cartan's input
