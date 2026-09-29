---
what: UI / operability backlog for ovitmugen — proposals + majkee's friction log
created: 2026-09-29
author: trajectory (proposals) · majkee (friction entries)
status: open list; nothing here is built until majkee picks it
---

# Friction log (majkee — append: what I tried · where it hurt · how often)

- 2026-09-29 · switching agent tabs: focus right pane → navigate runbook → T → choose.
  "select subwindow is hell". C-a q only numbers the 2 frame panes, not agent tabs.
  Need fast jumps between agent cards; must not rebuild the basic screen from scratch.
  Later: small-panes dashboard; the pipes (nablarva) will need this surface.

# Proposals (trajectory)

| # | proposal | keys | cost | value |
|---|---|---|---|---|
| 1 | direct tab jump anywhere in the frame: C-a 1..9 = tab N, C-a n / p = next / prev tab (frame has one window, those keys are idle) | C-a 2 | tiny, frame conf | must-have |
| 2 | same without prefix: Alt-1..9 (steals zsh digit-argument; Claude Alt use unchecked) | Alt-2 | tiny | high — needs OK on stolen keys |
| 3 | `ov-up` with no name reopens the last bed (per host state) | ov-up | small | must-have |
| 4 | bed remembers its tabs (saved on up/down); rebuild = those tabs, not the preset | — | small | high |
| 5 | mosaic: 2nd frame window, N small read-only panes each watching one tab; C-a m toggles | C-a m | medium | high at 3+ agents |
| 6 | agent badges in the tab bar: cSharp● bus○ audit! (! = waiting for input; signal needs research) | glance | medium | medium |
| 7 | Konsole profile / shortcut starting straight into ov-up | click | tiny (operator side) | medium |
| 8 | ov-ls --json as the pipe for nablarva's dashboard / bus | — | none now | future |

Recommendation: 1 + 3 + 4 now · 5 when 3+ agents run at once · 2 after the stolen-keys OK ·
6's "!" after a reliable waiting-for-input signal exists.
