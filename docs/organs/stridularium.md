---
wrapper: stridularium — design intent + open questions (working wrapper, draft · NOT canon)
sibling: PROJECT-DESIGN.md (repo root; same species: maintained working wrapper, linked from PROJECT.yaml)
maintainer: TBD — assigned when `stridularium-00-design` opens (majkee drafts the app there; L14 D5)
owner: majkee
registry: meshup/stridularium.mobile-console.2026-09-29/DESIGN.md (fixed entry; this wrapper is the living draft — one points to the other, neither duplicates)
created: 2026-10-02 · oraculum (journal 2026-10-01 §1 item 7 · TASK 2) · skeleton only, by majkee's lean
---

# Phone organ — design wrapper

The cultural name “stridularium” is retired under L24; this existing path remains.

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

Historical names: stridularium (L13; cultural name retired by L24) and k0k0nV3R /
coconvergence (Cartan's working name, 2026-09-29). Existing registry paths remain.
The earlier `stridularium/{android,host}` placement was a native-app proposal, not
an implemented tree; the closed session 03 does not own the current browser pilot.

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

## Experimental browser console

An experimental browser-console core exists at [apps/session-console](../../apps/session-console/README.md).
It supports disposable fixtures and an explicitly configured live ovitmugen
adapter through the reviewed owner interface. The office loopback/USB pilot can
select and attach existing single-pane sessions; full physical qualification remains
open. Native Android remains a retained later option. The historical
`stridularium-00-design` plan is not the current implementation route.

Sessions stay on the workstation. Paste and Enter are explicit separate actions;
uncertain input is never replayed, and detach preserves underlying process lifetime.
Unsent drafts are browser-local; the temporary tray expires, while saved prompts
and files use a dedicated workstation vault with explicit revisions and verified
uploads. Gallery batches and camera capture use browser file selection. Verified
uploads may be followed by manual Gallery cleanup; the browser cannot erase phone
originals. Camera behaviour and the full pilot still require qualification.

Build/run instructions live in the component README; its [console contract](../../apps/session-console/contracts/console.md)
[live amendment](../../apps/session-console/contracts/live.md) and
[storage contract](../../apps/session-console/contracts/storage.md) own the exact
interfaces. This is a loopback/USB qualification candidate, not an installed
tailnet HTTPS service or a room-delivery implementation.
