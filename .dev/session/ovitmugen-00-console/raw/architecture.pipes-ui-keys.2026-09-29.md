---
what: ovitmugen basement — pipes for other bricks, UI, keys (proposal for majkee's decisions)
created: 2026-09-29
author: trajectory
status: PROPOSAL · nothing built · decisions D1–D5 at the end
reads: raw/ui-operability.2026-09-29.md · ~/ia-sync/zsh/guides/claviature.global.spec.md ·
       toolbox/termbrana/{README,DECISIONS}.md · .dev/session/flag.md L3/L4, docket 4–5
---

# ovitmugen basement: pipes · UI · keys

## 0. What was found (the ground this stands on)

- **Keys doctrine is locked:** claviature spec, "Derive, don't register". No key registry;
  only FAMILIES are registered (one line each in `ai/keys.zsh`); unknown keys surface in
  UNSORTED. A keys registry file would be the second truth that doctrine forbids.
- **termbrana is Zellij-first** (ADR-0000/0002: host contract frozen on zellij 0.44.3,
  read-only observer). ovitmugen is tmux. Two multiplexers → the shared layer must be
  multiplexer-neutral data, not tmux ids.
- **nablarva settled points (L3):** append-only journal as truth · monitor = plain files ·
  room state on neutral ground · tmux never the protocol (L4: send-keys is a recorded death).
  Docket 4 leans "broker = a foreground process in a tmux pane"; docket 5 "NDJSON now".
- **Prior art for pane ↔ agent identity:** `install-pkgs/tmux-pin-bus.md` (BUS_PANE tokens →
  session ids via hooks, `~/.bus/hooks.jsonl`). Reference only; ovitmugen does not own identity.

## 1. Layers

```text
L4  UI        frame keys · console · runbook T · (mosaic later)
L3  control   narrow verbs: up · tab · close-idle · down · open   (never input to a pane)
L2  pipes     pull: ov-ls --json      push: events.jsonl      state: beds/<bed>.json
L1  map       neutral model: host → bed → tabs → process (pid, tty, cwd, fg program)
L0  adapter   tmux today (ovitmugen.py internals); a zellij adapter stays possible
```

Rule: bricks talk to **L2/L3 through the CLI and files**, never by importing ovitmugen's
Python (runbook is the one sibling allowed to import; it ships in the same folder).

## 2. L1 — the session map (schema `ovitmugen.map/v1`)

```json
{ "schema": "ovitmugen.map/v1", "host": "office", "at": "2026-09-29T08:10:00+02:00",
  "beds": [ { "bed": "nablarva-00", "root": "~/unikuklatrix/nablarva/.dev/session",
              "project": "~/unikuklatrix/nablarva",
              "frame": { "up": true, "attached": 1 }, "views": ["nablarva-00--left"],
              "tabs": [ { "name": "cSharp", "index": 0, "id": "@63", "left": true,
                          "busy": true, "fg": "claude",
                          "pane": { "pid": 12345, "tty": "/dev/pts/7", "cwd": "~/…" } } ] } ] }
```

- `id` is the tmux window id: an adapter detail, carried but never a key for other bricks.
  The neutral key is `(host, bed, tab name)`.
- `pid`/`tty`/`cwd` let nablarva or termbrana map an agent process to a tab with their own
  identity rules (hooks ledger, session ids). ovitmugen never claims *who* the agent is.
- `root`/`project` come from the bed's remembered state (L2 state file), not from tmux.

## 3. L2 — three pipes

| pipe | form | who writes | who reads | truth |
|---|---|---|---|---|
| **pull** | `ov-ls --json` (+ `--schema`) | computed live from tmux | runbook, termbrana, nablarva monitor | live |
| **push** | `~/.local/state/ovitmugen/events.jsonl` | ovitmugen only, own actions | anyone tailing (plain file, S6) | append-only |
| **state** | `~/.local/state/ovitmugen/beds/<bed>.json` + `last` | ovitmugen on up/down/b/x | ovitmugen (rebuild), others (which beds exist even after a reboot) | remembered |

- **Events** are ovitmugen's own verbs only: `bed.built · tab.added · tab.closed ·
  tab.switched · frame.opened · frame.closed`, one JSON line each (`ts, host, bed, tab, verb`).
  Never agent content, never keystrokes. Rotation: keep the file small (size cap → `.1`).
- **State** is machine-local (`~/.local/state`, never synced, like the presence board's own
  ids). It carries the tab list, root, project, split, and `last` bed → powers UI U3 + U4.

## 4. L3 — control verbs (what other bricks may ask for)

`ov-up [bed] [--root] [--no-attach]` · `ov-tab [bed] <tab>` · `ov-down [bed] [--views|--idle]`
· console `x x` (close idle) · `o` (open frame). All already exist or are one flag away.
**Never:** send-keys, paste-buffer, starting a program in a tab, closing a ● tab.
A future broker (nablarva docket 4) lives in its **own tab of the agents server**; the frame
only views it (a viewer never owns lifetime).

## 5. L4 — UI (from the backlog)

| id | what | needs |
|---|---|---|
| U1 | `C-a 1…9` tab N · `C-a n/p` next/prev tab (any frame pane) | frame conf only |
| U3 | `ov-up` with no name → last bed | L2 state `last` |
| U4 | rebuild recreates the bed's own tabs (not the preset) | L2 state `beds/<bed>.json` |
| U5 | mosaic: 2nd frame window of small read-only views, `C-a m` | L1 map; later |
| U6 | tab badges `●○!` in the tab bar | `!` needs a waiting-for-input signal: research |

## 6. Keys — derive, don't register (fits the locked claviature doctrine)

One source per surface; every overview is derived from it, never hand-kept:

| surface | the one source | derived view |
|---|---|---|
| shell aliases | `session/keyboard.zsh` | `keys` panel: register the **families** `ov-` and `rb-` (one line each in `ai/keys.zsh` + a row in `guides/keyboard.md`) |
| frame keys | `ovitmugen.tmux.conf` with `bind -N "<note>"` | native `C-a ?` (tmux lists keys with notes) |
| console keys | one `KEYMAP` table in `ovitmugen.py` (drives dispatch + hint line) | `ov-keys` |
| all ovitmugen keys | the three above | `ov-keys` prints frame (live `list-keys -N`) + console + runbook `T` |

HELP.md stays the curated prose layer above (claviature: "two layers, different jobs") and
points to `ov-keys` for the live truth. **No keys registry file.**

## 7. Build order (each shippable alone)

| step | scope | proves |
|---|---|---|
| B1 | L1 schema + versioned `ov-ls --json` · L2 state dir, `beds/<bed>.json`, `last` · events.jsonl | selftest: schema keys, state written on up/down, events appended |
| B2 | U1 tab jumps · U3 last bed · U4 remembered tabs | selftest + live: C-a 2 from the runbook pane moves the left pane |
| B3 | keys: `bind -N` notes, KEYMAP, `ov-keys`, families `ov-`/`rb-` in `ai/keys.zsh` | `keys` shows them outside UNSORTED; `C-a ?` lists notes |
| B4 | U5 mosaic | when 3+ agents run at once |

## 8. Decisions for majkee

- **D1 · events.jsonl — ANSWERED 2026-09-29 (majkee): YES.** JSONL (= NDJSON), one line per ovitmugen action, append-only, plain file per host; never agent content or keystrokes.
- **D2 · state in `~/.local/state/ovitmugen/`** (machine-local, never synced): yes / other.
- **D3 · keys: derive, don't register** — no registry file; register `ov-`/`rb-` families in
  `ai/keys.zsh` (outside zsh/session: one line, announced): yes / no.
- **D4 · termbrana:** tmux stays the frame; termbrana consumes only L1/L2 (neutral data);
  a zellij adapter is possible later but not planned: accept / want termbrana as the frame.
- **D5 · session shape:** this exceeds the 00 gate (v1 live). Close 00 after the home
  selftests; open sibling `ovitmugen-01-basement` with its own gate for B1–B3.

## 9. majkee input (2026-09-29, mobile, voice — recorded as heard)

- nablarva = the multi-session bridge / bus between brand CLIs (Codex, Claude, Gemini…);
  toolboxes = partly independent organs of nablarva, like building bricks. ovitmugen is
  converging into that picture — fine.
- Keys: "derive, don't register" was meant for shell commands. For the UIs of the
  toolboxes the wish is ONE normalized shortcut style across all of them (not lost between
  styles) — a shared key grammar, not a registry file.
- No heavier IDE: terminal / tmux, or zellij if needed, behind an app construction with a
  loader that can switch (= L0 adapter).
- Pseudo-buttons (trees, lists inside the animal) instead of real buttons are fine.
- Sooner or later all toolboxes / nablarva parts hosted in the LEFT half of the window.
  (Open: today agents are left and runbook right — confirm the side when we reach layout.)
- ovitmugen must design for horizontal AND vertical monitors (office: two, one can be a
  vertical 21"; home: one horizontal 21").
- Process: answer D1–D5 one question per turn, loop until answered, then the next.
