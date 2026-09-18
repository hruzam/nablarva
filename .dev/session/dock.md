# dock.md — UNCANONICAL scratch pad (the side-quest dock)

`no canon weight · any seat writes · prunable without ceremony · NEVER cite as truth`
`exists so side quests don't wait for a blessing (majkee gavel 2026-08-02, flag L9)`
`anything here that matures → propose for pulse/flag; anything stale → delete, no ledger`

---

## 2026-09-14 · majkee fork (voice) — "do we need the vendor's socket/server? could a ghost local server / old laptop on the tailnet / small cloud host be the reachable place for all sessions?"

- Correction first: `codex app-server` is a **local process on the host** (same binary as the TUI), listening on a local Unix socket; nothing external. The only cloud is the model API every session uses anyway. The "pocket-test" naming made it look like a remote service; it is not.
- Layer check: the bus (files + git) is already vendor-independent. What is vendor-specific — and disposable *by design* (a-symmetry: adapters rot) — is the **last inch**: how a living CLI is made to notice a file. Codex: `queue`/app-server; Claude: SendMessage/hooks; else PTY (L4). A relay host on the tailnet cannot type into a session; it can only hold files and notify. If vendors ship cross-vendor messaging, the door swaps; the bus stays.
- The fork maps onto existing open items: flag **O1** (living/hosting machine — blind pros/against pending), **O2** (cross-host transport: Tailscale), docket **4** (broker lifecycle), S7 (same protocol over SSH to one central broker). Old laptop on the tailnet = a Stage-2 broker/board host candidate. GitHub as wire = recorded death (L4); git as sync/archive = fine.
- "Short message at the end of output: something happened, please re-read" = pointer-only doorbell + nudge — exactly what bed 02 qualifies on the Codex side. Its last inch is never vendor-independent unless PTY, which is worse.
- Disposition: **parked, not contra** — Stage 2 substrate after the Stage-1 pipe qualifies. Nothing changes in bed 02 / sitting 1.
- Measurement side-note: the stenograph `?` lines already map the process; derive a workflow-map view after 2–3 logs; segment arcs with `special tab arc <name>`.

## 2026-09-14 · majkee fork (voice) — "agents emit a fixed marker block; a PTY reader spots it, else replies 'format not good, try again'"

- The correct form of this idea is already law: the marker is **the file at `return_to:`**, six headings, validated by the receiver's validator — no ANSI, no spinner, no scrollback. Absence → ATTENTION (human), never auto-"try again"; malformed → REVISE cycle, never a terminal loop.
- The PTY-scrape form of the same idea was measured (seam probe 2026-08-01: Claude TUI = `renderQueue` noise; JSONL is the read) and priced (token-economy brief: pay for garbage twice); v2 kill test: if crossings need UI parsing → stop.
- Braid-and-book's real finding stands: models follow file-writing instructions natively (Sonnet did) — that is *why* the file is the sentinel and the seam needs no cleverness.
- A read-only "spot a sentinel in capture-pane" sip is cheap but low-value given the above; not in bed 02; if native fails → STOP → L4 gavel decides, and such a sip would be a sibling with its own gate.
- Disposition: **already covered by law; PTY variant parked**.
- Sampling plan (majkee, back at PC): 2–3 sessions of ~1 h each with the stenograph (voice regime + fatigue), `special tab arc <name>` per arc, `?` narration on; deliver each to raw/human-relay-time-logs/. Head derives a workflow-map view after ≥3 logs → build-bed priorities.

## 2026-09-14 · majkee fork (voice) — "eyes" agent (screenshots, understand UI, bounded mouse/scroll/click) · flat Haiku/Luna PTY prefilter

- Both are OBSERVATION-plane sensors (v2 three planes): evidence, never truth; at most an ATTENTION source ("an approval dialog is visible"), never a delivery path. Kill test applies: if routine crossings need screen understanding → stop.
- Later phase of nablarva by majkee's own words; graphic capabilities are weather that improves — fine to revisit when Stage 1 is qualified. Local model (piql) as host: parked (noise/heat/cost, his call).
- Disposition: **parked**; no bed, no gate.

## 2026-09-14 · working agreements (majkee ↔ oraculum, chat)

- First word of a message: `mobile` or `pc` → the head sizes the answer and puts any copyable line first.
- Gavels are one line each, exact, transcribed verbatim (open_approval · armed_approval · GO/STOP · commit ok · count).
- Recording vocabulary may exceed the skill: unknown words land as `?` verbatim and the head maps them; three optional spoken markers help segmentation: `special tab arc <name>`, `special tab session <name>`, `special tab read start|end`.
- Two recorders (phone ptyra + tablet Claude Code/Sonnet as a second stenograph) are welcome; each flush is its own file in raw/human-relay-time-logs/; the head reconciles, never merges by hand into one.
