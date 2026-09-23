---
what is it: ovitmugen architecture — Trajectory's grounding + build proposal
created: 2026-09-23
author: @Trajectory (session ff-sync.trajectory.ovitmugen-planning)
status: DRAFT · layout C gaveled by majkee 2026-09-23 · everything else = proposal
answers: ~/ia-sync/.dev/session/runbook-upgrade-02-app/raw/draft.majkee.app-scheme.2026-09-23.md §3.2 (ovitmugen) + hand sketch "SCREEN: volatile | fixed"
moved: 2026-09-23 from ia-sync runbook-upgrade-02-app/raw/ → here (majkee: docs live in nablarva)
placement: docs = nablarva (this bed) · build + deploy = ~/ia-sync/zsh/session/ → `bash deploy.sh` (majkee gavel 2026-09-23)
---

# ovitmugen — tmux manager, architecture from the implementer's side

## 0. One-paragraph version

ovitmugen puts **your app fixed on the right** and **agents switchable like tabs on the
left**, in one terminal, rebuildable from a JSON preset. It is a **view/layout manager
only**: it creates sessions, windows and views, and switches which window the left pane
shows. It never talks to agents (no `send-keys`), never owns them, and killing it never
kills an agent.

---

## 1. Locked: layout C (majkee gavel 2026-09-23)

```
┌─ your terminal (Konsole, phone over ssh, anything) ────────────────────────┐
│ FRAME = tmux server "ovitmugen" (own socket, own config)                    │
│ ┌─ left pane: VOLATILE ────────────────┬─ right pane: FIXED ──────────────┐ │
│ │ a tmux *client* showing view         │ runbook.py (the app)             │ │
│ │ <slug>--left of the AGENTS server    │  NABLARVA                        │ │
│ │                                      │   ├ termbrana                    │ │
│ │  [agent in the current tab]          │   ├ instarmux                    │ │
│ │                                      │   └ ovitmugen ──┐                │ │
│ │ [0:cSharp 1:bus 2:implement* 3:audit]│                 │ select-window  │ │
│ └──────────────────▲───────────────────┴─────────────────┼────────────────┘ │
└────────────────────┼─────────────────────────────────────┼──────────────────┘
                     │ shows                                │ switches
AGENTS = tmux server "default" (where agents live today)    ▼
  base  <slug>          windows: cSharp | bus | implement | audit   (1 agent each)
  view  <slug>--left    ← left pane's view (own current window)
  view  <slug>--<win>   ← optional extra columns / phone (t41-compatible naming)
```

**Prototype evidence (2026-09-23, isolated servers, blank config, killed after):**
the right pane stayed `MY-APP-FIXED` through three `select-window` calls while the left
pane went cSharp → bus → implement; left pane status bar showed the tabs.

---

## 2. Grounding — what exists today (verified, not assumed)

| Thing | Fact | Consequence for ovitmugen |
|---|---|---|
| `zsh/session/runbook.py` v0.3 | 2440 lines, stdlib, one file of top-level functions, curses. `palette()` ~400 lines of closure state; `draw()` fixed 13-arg signature | Do **not** grow a permanent third pane inside runbook. Add a **modal** (pattern: `board_view` L1133) + a sibling module |
| runbook tmux usage | **none** (only the ESCDELAY=250 multiplexer fix, L49-51) | ovitmugen is a clean addition, no legacy to untangle |
| runbook tick | 1 s `screen.timeout`; mtime-gated reloads | tmux queries must be on-keypress or slow-polled, with `timeout=` (like `copy_to_clipboard` L749) |
| runbook selftest | `runbook.py selftest`, sandboxed env, fake curses windows | ovitmugen gets the same: selftest on an **isolated socket** (`-L ovit-test -f /dev/null`) |
| zsh wiring | `session/base.zsh`: P1 keyboard (aliases only) · P2 runbook · P3 board · **P4+ free** | ovitmugen engine = P4; aliases in `keyboard.zsh` |
| `experimental/t41` | builds `<slug>` + N windows; join mode = `<slug>--<win>` grouped view; `registry.json` presets (`csharp`, `web`) | Same naming, same idea. ovitmugen absorbs it (§8 P3) |
| `help/tmux-session/HELP.md` | "Build a bed by hand" (uncommitted) | Manual twin of `ovitmugen up`; keep as the no-tool fallback |
| tmux | 3.7c on both hosts; `~/.tmux.conf` only sets `window-size largest` | See risk R1 |
| `=` exact-match on **pane** targets | `=frame:0.1` → `can't find pane` (3.7c, blank config); `frame:0.1` works | Use **IDs** (`$N @N %N`) from `-P -F`, never names, for anything after creation |
| nablarva flag **L3** | "adapter-owned PTY, tmux never the protocol" | ovitmugen = view layer. Not a transport, not a bus |
| nablarva flag **L4** | `tmux send-keys` injection = recorded death | ovitmugen **never** calls `send-keys` / `paste-buffer` into agent panes |
| rc.sh gavel 2026-08-15 | "minimize the tmux layer" (RC launching is tmux-free) | Agents must not *depend* on ovitmugen. Opt-in view; agents launch as today |
| live incident today | two windows named `bus` in one session | IDs, plus a duplicate-name check at `up` |

---

## 3. Boundaries

**ovitmugen does:**
- build a bed: base session + named windows (tabs) + left view + frame, from a preset or args
- switch the left pane's tab
- list what exists, including which tabs are hosting an agent
- tear down layers: frame, then views, then idle base, and only if no agent is running

**ovitmugen does not:**
- start agents inside tabs (v1: empty shells, same contract as t41 — Q3)
- type, paste or message into any pane (L4)
- own agent lifetime (agents live in the `default` server; the frame is disposable)
- replace runbook (runbook *is* the fixed pane; ovitmugen is a module it calls)

---

## 4. Names (one rule each, t41-compatible)

| Object | Name | Server |
|---|---|---|
| bed / slug | `<slug>` (e.g. `tunnel-upgrade-01`) | — |
| base session | `<slug>` | `default` |
| tab | window name from preset (`cSharp`, `bus`, …) | `default` |
| left view | `<slug>--left` | `default` |
| extra column / phone view | `<slug>--<win>` / `<slug>--phone` | `default` |
| frame session | `<slug>` | `ovitmugen` (`tmux -L ovitmugen`) |

**Socket rule (critical):** every call names its server explicitly: `tmux -L default …`
for agents, `tmux -L ovitmugen …` for the frame. runbook runs *inside* the frame, so
`$TMUX` points at the ovitmugen server. A bare `tmux select-window` from runbook would hit
the frame, not the agents.

---

## 5. Components

All paths below are in the **ia-sync deploy layer** (`~/ia-sync/zsh/session/`), built
there and spread with `bash deploy.sh`. Nothing below is built inside nablarva.

```
~/ia-sync/zsh/session/
  runbook.py            + modal tmux_view (key T) · overview line · calls ovitmugen.py
  ovitmugen.py          NEW  stdlib · CLI + importable · plan/apply split · selftest
  ovitmugen.tmux.conf   NEW  frame-only config (no status bar, own prefix, focus keys)
  ovitmugen.presets.json NEW presets (absorbs t41/registry.json)
  base.zsh              + P4 source ovitmugen engine (define-only)
  keyboard.zsh          + aliases ov-up / ov-tab / ov-ls / ov-down
  help/ovitmugen/HELP.md NEW  (runbook help scope, auto-discovered)
```

### 5.1 `ovitmugen.py`: plan / apply split

- `plan(slug, preset) -> [op]`: pure. It reads current tmux state and returns the
  *missing* steps only (idempotent: re-running `up` on a complete bed = empty plan).
  Fully testable without touching tmux.
- `apply(ops)`: runs each op via `subprocess.run([...], timeout=3)`, captures the new IDs
  with `-P -F '#{window_id}'` and similar, and stops at the first failure with a clear message.
- `--dry-run` prints the plan as literal tmux commands. That output is also the
  "by hand" recipe, so HELP.md and the tool can't drift apart.

### 5.2 CLI

```
ovitmugen.py up   <slug> [@preset | tab tab …]   build missing parts, attach frame
ovitmugen.py tab  <slug> <tab>                   left pane → that tab
ovitmugen.py ls   [<slug>]                       beds · tabs · agent? · clients · frame?
ovitmugen.py down <slug> [--frame|--views|--idle] peel layers; never kills a live agent
ovitmugen.py selftest
```

`up` sequence (each step skipped if already present):
1. `-L default new-session -d -s <slug> -n <tab1>`, then `new-window -d -n <tabN>` for each other tab
2. `-L default new-session -d -t <slug> -s <slug>--left`
3. `-L ovitmugen -f ovitmugen.tmux.conf new-session -d -s <slug> 'env -u TMUX tmux -L default attach -t <slug>--left'`
4. `-L ovitmugen split-window -h -l <split> -t <frame-window-id> '<fixed cmd>'` (default fixed cmd: `runbook.py --root <bed root>`)
5. attach the frame: `tmux -L ovitmugen attach -t <slug>`; if already inside the ovitmugen server, `switch-client`

### 5.3 Agent detection (the "is it safe to kill" rule)
A pane hosts an agent if its foreground command isn't a bare shell **or** its shell has
child processes. This is the same rule that was used live today (2026-09-23 cleanup). `down`
refuses any layer that would take the last reference to such a pane.

### 5.4 runbook integration (P2, small by design)
- **Modal `tmux_view`**, key `T`: lists the tabs of the bed under the cursor
  (`●` = agent running, `○` = empty shell). `Enter` runs `ovitmugen.tab`. Same loop shape as
  `board_view`.
- **Overview line** on the bed node: `tmux: 4 tabs · 2 agents · frame up`. Read on
  bed selection, not every tick.
- runbook already knows the bed root, so it passes `<slug>` = bed dir name by default.

### 5.5 Frame config `ovitmugen.tmux.conf`
- `status off` (the left pane already shows the inner tab bar)
- own prefix (proposal `C-a`) so `C-b` passes through to the agents server
- `C-a h` / `C-a l`: focus left / right pane; `C-a <` / `C-a >`: resize split
- `mouse on`: click a pane to focus it

### 5.6 Presets `ovitmugen.presets.json`

```json
{
  "csharp": { "tabs": ["cSharp", "bus", "implement", "audit"], "fixed": "runbook", "split": "40%" },
  "web":    { "tabs": ["front", "api", "db"],                   "fixed": "runbook", "split": "40%" }
}
```

`fixed` is a named command (`runbook` = `runbook.py --root <bed>`). The preset file never
holds a raw shell string, which keeps it declarative.

---

## 6. Risks

- **R1 · `window-size largest` (global, `~/.tmux.conf`).** A tab seen in the narrow left pane
  and also full-width (phone, second column) gets sized to the *largest* client, so the left
  pane crops. Fix: at creation, set `window-size latest` per ovitmugen window (a window
  option, so the global setting for other sessions stays). Needs a live check.
- **R2 · Pane targets.** `=` + pane fails, and names can duplicate. Use IDs everywhere
  after creation.
- **R3 · Socket confusion.** See §4. A selftest case must assert that `tab` from inside
  the frame moves the *agents* view.
- **R4 · UI stall.** tmux calls inside the 1 s tick. Keypress-driven plus `timeout=3`,
  never a per-tick poll.
- **R5 · Nested keys.** Solved by a separate server and prefix. Ask your agents whether
  anything uses `C-a` (readline start-of-line in the shell!). Q4.
- **R6 · Doctrine drift.** If anyone later adds "ovitmugen sends a prompt to tab X", that's
  the L4 death coming back. Put the rule in the module header and HELP.md.

---

## 7. What stays manual / out of scope

- Launching agents (you, or `rc.sh` / `claude --agent …`, in a tab)
- Cross-host frames (home viewing office agents): Stage 2 in nablarva terms. The design
  allows it (`ssh -t office tmux -L ovitmugen attach`) but it isn't built.
- A real GUI app (draft §2.1 Q1): if runbook outgrows curses, the plan/apply core stays
  and only the front end changes. That's the reason for the split.

---

## 8. Build order (each phase shippable alone)

| Phase | Scope | Gate |
|---|---|---|
| **P0** | HELP.md: commit "by hand" section, fix "don't switch windows" → left switches, right fixed | majkee read-through |
| **P1** | `ovitmugen.py` (plan/apply, up/tab/ls/down, dry-run) + presets + frame conf + selftest on an isolated socket. No runbook change | selftest green on office **and** home; `up` → `tab` → `down --idle` live on a scratch slug |
| **P2** | runbook modal `T` + overview line; fixed pane = runbook | `runbook.py selftest` still green + new cases; live walk |
| **P3** | t41 converges: `t41` becomes a thin alias over `ovitmugen up` (or retires); `t41/registry.json` → presets | no behavior lost from t41 `--help` |
| **P4** | nablarva: termbrana reads `ovitmugen ls --json` as its dashboard source | nablarva's own gate |

P1 is the real core. P2 is maybe 150 lines in runbook.

---

## 9. Open questions for majkee

1. ~~Placement~~ **ANSWERED 2026-09-23 (majkee):** documentation lives in nablarva (this
   bed). The implementation is zsh/py bricks, built in `~/ia-sync/zsh/` and deployed with
   `bash deploy.sh`. ia-sync = deploy layer.
2. **Split default:** left 60 / right 40?
3. **Tabs with agents:** v1 = empty shells (t41 contract). Later, a preset `cmd` per tab
   (e.g. `claude --agent trajectory`)? That's launching via `new-window <cmd>`, not
   `send-keys`, so L4 is intact. Your call.
4. **Frame prefix:** `C-a` (conflicts with shell start-of-line inside panes), or `C-]`, or no
   prefix and only mouse + `M-h/M-l`?
5. **Existing bed** `~/unikuklatrix/nablarva/.dev/session/ovitmugen-00-console/` holds
   only `brief.ovitmugen-sentinel.2026-09-04.md`, which is the **@kukla sentinel** brief
   (agent-file sorting keys), not a tmux manager. Misfiled, or was "ovitmugen" once a
   different organ? Not touched.
