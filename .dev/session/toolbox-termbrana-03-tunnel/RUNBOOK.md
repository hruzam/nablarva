# RUNBOOK: Termbrana 03 — the tunnel (law-2.4 operator capability)

```yaml
goal: Two living sessions — one Claude seat, one Codex seat — exchange work through a proven tunnel on office, as termbrana's deliberately-enabled write capability (project law 2.4).
gate: One full round-trip (Claude→Codex task, Codex→Claude result) through the v0 tunnel, live on office, receipts on disk in this session folder.
participant_1: [oraculum, {brand: "Claude Code", model: opus, effort: high}, host: "office"]
participant_2: [cartan, {brand: "Codex CLI", role: "Codex resident co-architect — owns Codex-side receive/send mechanics"}, host: "office"]
participant_3: [majkee, {role: "operator — pane/tab hands, tunnel enable gavel, L11 authority"}, host: "office"]
```

## Known constraints and destructive holds

- **⚠ nablarva flag L11 HOLDS:** *"no parallel coding before M0 freezes the host contract."*
  M0 was NOT confirmed frozen when this RUNBOOK was authored (2026-09-01; the m0-close
  runbook still sat on the bench `~/reposoma/_runbook/termbrana/m0-close/RUNBOOK.md`).
  **This session may be READ (research, design) but no tunnel code is written until
  either M0 freezes or majkee records an explicit L11 exception in
  `~/unikuklatrix/nablarva/.dev/session/flag.md`.** Do not resolve this silently.
- **v0 SHAPE IS GAVELED (majkee, 2026-09-01):** **v0 = app-server-first** — Codex leg
  via `codex app-server` JSON-RPC (living, steerable, headless thread) + native Claude
  messaging (SendMessage, v2.1.224+) on the Claude side. **v1 = visible mode** — the
  Codex thread rendered into a pane termbrana observes; zellij-paste mechanics where
  injection is needed. Decision record: `~/unikuklatrix/termbrana/research/`
  `termbrana.tunnel-stage.observations.2026-09-01.md` §4. Do not re-litigate the axis;
  t1 decides only per-leg mechanics inside this shape.
- **Office only.** Verify before anything: `ls /usr/bin/php74 && command -v valet` —
  both present = office. zellij and tmux are ABSENT on home; this work cannot run there.
- **termbrana law 2.4:** the default product is read-only; the tunnel is the *separately
  enabled operator capability*. It must be built as an explicit enable, never a default.
- **termbrana law 2.5:** native facilities outrank replicas — which is exactly why v0
  rides official surfaces (app-server + SendMessage) and no daemon is built.
- **Cross-runtime law:** `~/ia-sync/HANDSHAKE.md` governs the exchange semantics; the
  tunnel is the candidate TABLE shape — adopted into the HANDSHAKE only after this gate
  closes, co-signed by @Cartan.
- **Do not touch** `termbrana-core`, M1 lanes, or nablarva locks. One gate: the round-trip.

# prompt-0 (owner seat — oraculum)

```
Termbrana 03-tunnel — office session.

0 · SEAT + HOST. You are @Oraculum, tunnel-stage owner, running on office.
VERIFY HOST: ls /usr/bin/php74 && command -v valet  (both present = office; else STOP).
Do not trust any file's host: header.

1 · READ, IN THIS ORDER (absolute paths):
   ~/unikuklatrix/nablarva/AGENTS.md
   ~/unikuklatrix/nablarva/.dev/session/flag.md          — L6, L9, L11 (L11 gates this session)
   ~/unikuklatrix/nablarva/.dev/session/pulse.md         — top entry only
   ~/unikuklatrix/termbrana/research/termbrana.project-definition.md   — laws 2.4, 2.5
   ~/unikuklatrix/termbrana/research/research.epoch.tunnel-claude-side.2026-09-01.md
   ~/unikuklatrix/termbrana/research/research.epoch.tunnel-codex-side.2026-09-01.md
   ~/unikuklatrix/termbrana/research/termbrana.tunnel-stage.observations.2026-09-01.md  — §4 = gaveled v0 shape
   ~/ia-sync/HANDSHAKE.md                                — Delivery rule + TABLE candidate

2 · L11 CHECK — FIRST ACTION. If M0 is not frozen and no L11 exception is recorded in
flag.md: research/design tasks only; report the block to majkee; write no tunnel code.

3 · TASKS (in order, inside this one gate; v0 shape is gaveled — see constraints):
   t1 — per-leg mechanics verdict WITHIN the v0 shape: Codex leg = app-server client
        details (thread lifecycle, turn/steer usage, result read-back, auth frame) —
        Cartan's live evidence decides; Claude leg = SendMessage terminus + envelope
        convention. Record verdicts + evidence refs in STATUS.md. Conflicts → majkee.
   t2 — v0 build (L11-gated): the app-server client shim + Claude-side messaging
        terminus, authored in ~/ia-sync/zsh/ (machine layer, compose-first, deploy
        outward). Smallest native primitive; explicit enable per law 2.4; no daemon.
   t3 — live proof = THE GATE: majkee enables the tunnel; the Claude seat sends one
        scoped task; the living Codex thread (Cartan) receives, acts, returns the
        result through the tunnel; transcripts + the exchange land as receipts in this
        folder. Zero copy-paste by the human during the round-trip.
   t4 — close: promote evidence (mechanics verdict → termbrana/research/evidence/,
        tunnel shim → ia-sync commit), propose TABLE shape to HANDSHAKE r3 (Cartan
        co-signs), prune per the runbook guide. v1 (visible mode) opens as sibling
        session 04 — not inside this gate.

4 · SESSION FILES. Create STATUS.md in this folder at session start, per
~/reposoma/raw.guides/status/GUIDE.md — it carries the gate verbatim and is the sole
doing-state. dock.md / pads / _bus/ born on need only.

5 · GATES. majkee owns commit, push, flag locks, the L11 call, and the tunnel-enable
gavel. Cartan owns Codex-side mechanics and co-signs the TABLE shape. Behavior proof
before promotion — a tunnel that worked once in a pilot is piloted, not proven; record
the pilot date + models (Sella L8).
```

# prompt-1 (cartan — Codex resident)

```
Termbrana 03-tunnel, Codex side. You are @Cartan. Read (absolute paths):
~/ia-sync/HANDSHAKE.md ·
~/unikuklatrix/termbrana/research/research.epoch.tunnel-codex-side.2026-09-01.md ·
~/unikuklatrix/termbrana/research/termbrana.tunnel-stage.observations.2026-09-01.md (§4
= the gaveled v0 shape) · this folder's STATUS.md. Your scope: the Codex leg of v0 —
app-server mechanics (thread/start|resume lifecycle, turn/start|steer, result
read-back, auth/entitlement frame on the current CLI), verified against your live
runtime, which outranks the research on volatile CLI facts. Also: verify multi-agent
status for a later v2 (architect tasking own crew) — currently held unstable. Hold the
round-trip's Codex end at t3. Record verdicts to STATUS.md via the meeting-room flow if
you are not seated in this bed directly.
```

## References — point, do not copy

- Canon: `~/unikuklatrix/nablarva/.dev/session/flag.md` (L11 sole authority on structure)
  · `~/unikuklatrix/termbrana/research/termbrana.project-definition.md` (laws)
- Decision record: `~/unikuklatrix/termbrana/research/termbrana.tunnel-stage.observations.2026-09-01.md` §4
- Prior session: `~/unikuklatrix/nablarva/.dev/session/toolbox-termbrana-02-m0-truthspike/`
  (M0 — must freeze first or be excepted)
- Cross-runtime: `~/ia-sync/HANDSHAKE.md` · `~/ia-sync/session/rellays-calude-codex/`
- Machine layer: `~/ia-sync/journal.host-cleanup.md` · `~/ia-sync/AGENTS.md` §"Which host am I on?"
- This RUNBOOK's bench origin: authored live 2026-09-01 (majkee order, session
  fc-sync.oraculum.sella); no bench copy retained — the guide's bench is for drafts
  preceding a session folder, and this folder already existed.
