---
wrapper: stridularium — design intent + open questions (working wrapper, draft · NOT canon)
sibling: AGENTS.PROJECT-DESIGN.md (same species: maintained working wrapper, linked from PROJECT.yaml)
maintainer: TBD — assigned when `stridularium-00-design` opens (majkee drafts the app there; L14 D5)
owner: majkee
registry: meshup/stridularium.mobile-console.2026-09-29/DESIGN.md (fixed entry; this wrapper is the living draft — one points to the other, neither duplicates)
created: 2026-10-02 · oraculum (journal 2026-10-01 §1 item 7 · TASK 2) · skeleton only, by majkee's lean
---

# stridularium — design wrapper

## What it is (one paragraph)

The human's door into the room — L2 stage 3, named by L13. An **organ** of the animal, not a toolbox: a
thin mobile lens (Android first; Galaxy + Redmi are the measured devices) over sessions that live on the
workstation in tmux (L14 D5). Two layers: a **console core** that works against any tmux host with the
animal absent (host picker · session tree · live terminal · text tray · detach/reconnect · services), and an
**organ layer** that needs the room (gavel feed · per-target buffers released only through stridulatrix and
the adapter's PTY, L3/L4 · host-side speech-to-text · room/seat navigation). Toward hosts the app controls
sessions only through a **host-side engine** that hosts the processes; the app sends commands and prompts
and receives output — nothing more by design; never Android functions outside the app (L14 D6).

## Names

stridularium (L13, the organ) · k0k0nV3R / coconvergence (working name, Cartan's seat, 2026-09-29) — culture
layer. Disk stays ASCII: slug `stridularium.mobile-console.2026-09-29`; code home proposed
`nablarva/stridularium/{android,host}` — final home is `nablarva-03-app-architecture`'s to fix.

## Canon it rides on

flag.md L2 · L3 · L4 · L13 · L14 (D5 thin lens · D6 reach · D7 triangulation) · O2 lean (hardened
Tailscale + Termux, then mosh) · session-bed · presence-board · KEYS CODE.

## Origins (kept whole, not merged)

- Cartan (Codex), 2026-09-29 — `meshup/stridularium.mobile-console.2026-09-29/raw/IDEA.k0k0nV3R.2026-09-29.md`
  (console · tray · services · persistence · Termux companion vs native shell vs fork)
- Symmetry (claude.ai), 2026-09-30 → 10-01 — `…/raw/note.phone-lens.2026-09-30.md` →
  `…/raw/note.stridularium.2026-10-01.md` (door · gavel feed · voice · carousel · bridge O2)
- design-chapters §3.8 — `.dev/session/nablarva-X0-restarted/raw/design-chapters.for-cartan.2026-10-01.md`

## Open questions

Live list: `meshup/stridularium.mobile-console.2026-09-29/HYPOTHESES.md`. The one real tension between the
two origins: Cartan's *native terminal on the phone* vs Symmetry's *host renders text, phone shows cards, no
terminal emulator*. Not resolved here.

## To be filled in `stridularium-00-design` (majkee)

shape of the first slice · console-first vs notifier-first vs buffer-first · engine contract (host helper
over SSH vs service behind Tailscale Serve) · persistence contract · which device is the measure.
