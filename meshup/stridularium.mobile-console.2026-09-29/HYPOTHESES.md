# HYPOTHESES — stridularium.mobile-console.2026-09-29

```yaml
updated: "2026-10-02"
writer: oraculum · Claude (loop 1.3; from IDEA.k0k0nV3R, note.phone-lens, note.stridularium, design-chapters §3.8)
design: stridularium.mobile-console.2026-09-29
phases: [phone-lens-note, k0k0nV3R-idea, stridularium-note, L13-L14-locks, console-core-first]
open:
  - h1: "Terminal on the phone (Cartan: native terminal, selection, key row) vs no terminal emulator on the phone (Symmetry: host renders text, phone shows cards)"
    src: raw/IDEA.k0k0nV3R.2026-09-29.md (§First experience 3) · raw/note.stridularium.2026-10-01.md (§Navigation)
  - h2: "Build order — notifier first (majkee) · buffer first (Symmetry) · console core first (oraculum): which slice proves the loop earliest?"
    src: raw/note.stridularium.2026-10-01.md (§Open) · AGENTS.stridularium-design.md
  - h3: "Engine contract — on-demand host helper over SSH vs authenticated service behind Tailscale Serve; today's device key forces interactive tmux and exposes no command API"
    src: raw/IDEA.k0k0nV3R.2026-09-29.md (§How to approach · §Design choices)
  - h4: "Companion over Termux (RUN_COMMAND intent) vs purpose-built shell with terminal component + SSH lib vs Termux fork"
    src: raw/IDEA.k0k0nV3R.2026-09-29.md (§Design choices to test)
  - h5: "Rule for secrets spoken aloud (inherited gap from Ptyra; urgent on a phone in public)"
    src: raw/note.stridularium.2026-10-01.md (§Voice mode)
  - h6: "voice-relay-00-probe in nablarva — unread; does it change the voice pipe shape?"
    src: raw/note.stridularium.2026-10-01.md (§Open)
  - h7: "Zellij web client (0.43+ token login, 0.44 read-only follow) as a one-test alternative bridge — weather, re-verify"
    src: raw/note.stridularium.2026-10-01.md (§Bridge)
  - h8: "Notifications via private ntfy — locked-screen delivery on Galaxy (Android 8.1) and Redmi (Android 15) untested"
    src: raw/IDEA.k0k0nV3R.2026-09-29.md (§Services table)
  - h9: "Cross-device tray sync — separate future decision; export is enough for the first design"
    src: raw/IDEA.k0k0nV3R.2026-09-29.md (§Make collection deliberate and durable)
  - h10: "Delivery uncertainty — a paste over a raw terminal channel cannot promise exactly-once; mark uncertain, never auto-replay"
    src: raw/IDEA.k0k0nV3R.2026-09-29.md (§Persistence is part of the product)
confirmed:
  - claim: "Galaxy baseline 2026-09-29 — device key unlocks; create/type/execute/detach/reconnect passed against office and home"
    src: raw/IDEA.k0k0nV3R.2026-09-29.md (§Planning gates 1 · §What exists now)
  - claim: "Redmi interactive proof — create/type/execute/detach/reconnect and Unicode byte delivery passed against both hosts"
    src: raw/IDEA.k0k0nV3R.2026-09-29.md (§What exists now)
  - claim: "Sessions live on the host; the phone never hosts (L14 D5, gaveled)"
    src: /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md (L14 D5)
refuted:
  - claim: "device-scoped access — a CLI reaching Android functions outside the app"
    src: /home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md (L14 D6) · raw/note.stridularium.2026-10-01.md (§Shape, Rejected)
next_probe: none here — majkee drafts the app in stridularium-00-design; h1 and h2 are its first decisions
expected: a stridularium-00-design RUNBOOK whose gate names the first slice; this file updated with its verdicts
```
