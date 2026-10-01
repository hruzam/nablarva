# Seam Probe — report

_Run 2026-08-01 by Atlas (atlas-ui, over Delta for bash) for @majkee / Nabla._
_Read-only. Stage 6 (write-back) NOT run — gated, awaiting explicit clearance._

## env
- host / reachable: **home reachable over Tailscale** (`100.110.27.60`, active/direct) — but home is **not a usable target** (see Stage 2). Probe **redesigned to a local OFFICE target**.
- target: office tmux session `seam` → `claude --agent atlas-ui --model claude-sonnet-4-6` in `~/reposoma`.
- braid log present: no.

## per stage

### Stage 1 — Reachability — PASS
- `[SEEN]` `100.110.27.60  hruzam  ...  active; direct 94.112.47.33:41641`; ssh returned `reachable` / `hruzam`.
- `[INFERRED]` home is up and directly reachable over Tailscale (rests on `active; direct` + the ssh echo).

### Stage 2 — See the session — FAIL on home → REDESIGNED
- `[SEEN]` on home: `zsh:1: command not found: tmux` (×2). `ps` on home: `3460 claude --agent atlas-ui --model claude-opus-4-8`, `7115 claude --agent epoch --model claude-sonnet-4-6`.
- `[INFERRED]` home runs live Claude TUIs but has **no multiplexer** → `tmux capture-pane` is blind to them.
- `[BLIND]` the **live screens** of the two home Claude sessions — no tmux, no tee log, nothing to capture. I can see *that* they run and their launch args, not what they render.
- **Redesign (honest, not a fake pass):** only OFFICE has tmux (3.7b; home has none of tmux/screen/zellij/abduco/dtach). Target moved to a controllable office-local tmux session.

### Stage 3 — Capture the live screen — PARTIAL
- `[SEEN]` header: `Claude Code v2.1.220` · `Sonnet 4.6 with high effort · Claude Max` · `@atlas-ui · ~/reposoma`. Input line: `❯` (empty). Footer: `⏸ manual mode on · ? for shortcuts · ← 1 agent`. A status banner reading `atlas.office.building`. A large band of repeated `renderQueue: [object Object] …` where the transcript region should be.
- `[INFERRED]` the TUI booted to an **idle, empty, manual-mode prompt awaiting first input** (rests on the empty `❯`, the `⏸ manual mode` footer, and the absence of any response text).
- `[BLIND]` clean transcript **content** — the transcript band rendered as `renderQueue: [object Object]` noise, not readable text. The provenance of the `atlas.office.building` banner is also `[BLIND]` — I saw the string; I will not claim what produces it.

### Stage 4 — Motion — PASS (reads as idle)
- `[SEEN]` three consecutive frame hashes: `cc895c17…` / `cc895c17…` / `e4fbc72e…` (first two identical, third differs).
- `[INFERRED]` screen is essentially **static → idle/waiting**; the single late hash change is a cursor/render tick, not content generation.
- `[BLIND]` a lone idle frame cannot by itself separate *waiting-for-input* from *finished* — both look idle. Launch context (fresh boot, empty prompt) points to *waiting-for-input*, stated as inference not observation.

### Stage 5 — braid vs river — SKIPPED
- No `BRAID_LOG` / tee exists. Not run.

## headline answer
"What is the [target] agent doing right now?"
- `[SEEN]` empty `❯`, `⏸ manual mode on`, `← 1 agent`, no response text.
- `[INFERRED]` a freshly-booted atlas-ui / Sonnet 4.6 session sitting **idle, waiting for its first input**.

## sectors — the read/write map (@majkee's ask)
- **WRITE sector** = the `❯` input line, between the two horizontal rules, just above the status footer. Write via `tmux send-keys -t <session> '<text>' [Enter]`.
- **READ sector** = the transcript band **above** the input rule (obscured by render noise in this idle capture). Header band = context (version/model/agent/cwd); footer band = mode + agent count.

## honest failures
1. **The over-Tailscale read of home is not possible with the current method** — no tmux, no tee on home. I did not fake it; I said so and redesigned to a local target.
2. **The transcript sector was not cleanly readable** — this Claude version's Ink TUI screen-scrapes as `renderQueue: [object Object]` noise under `tmux capture-pane`. I could read the **chrome** (header / input / footer / status) but **not clean transcript content**. The clean channel for content is almost certainly headless `claude -p` output or the session **JSONL transcript**, not screen capture.
3. `atlas.office.building` banner meaning — unresolved, marked `[BLIND]`.

## verdict
- **Can I read a live remote TUI over Tailscale, keeping seen/inferred separate?**
  **PARTIAL.** Remote (home): **NO** — nothing capturable there. Local (office, tmux): **YES for the chrome/state, PARTIAL for transcript** (render-noise).
- **One line, what surprised me:** the seam itself is fine — the limiter is that this Claude TUI screen-scrapes noisily; the reliable read is headless/JSONL, not `capture-pane`.

## Stage 6 — GATED, prepared but NOT run
A clean write-sector test that spends no model tokens: type into the input **without** submitting, confirm it lands, then clear.
```
tmux new-session -d -s seam -x 210 -y 50
tmux send-keys -t seam 'cd ~/reposoma && claude --agent atlas-ui --model claude-sonnet-4-6' Enter
sleep 16
tmux send-keys -t seam 'nabla-probe-marker'      # NO Enter → text should appear at ❯, unsent
tmux capture-pane -p -t seam                      # [SEEN] the marker in the input sector = write proven
tmux send-keys -t seam C-u                         # clear the line, submit nothing
tmux kill-session -t seam
```
Awaiting @majkee's "go" before this runs.
