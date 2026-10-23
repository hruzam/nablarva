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

## 2026-10-23 · parked from the X3 architecture sitting (majkee R9-1 N6 and N8; homed here by majkee: "N6/N8 to dock.md")

- **N6 · session naming and sub-organ numbering.** Verbatim (said: majkee R9-1): "if sessions has shape <organ>-<generation><order_number>-<slug*>, if slug means growing specific sub-organ Q should have second injected numbering, like `termbrana-X8-sublimeIDE-05-pins` so slug line can describe development of separate suborgan, or should we have flat numbering?" Open; not architecture. Matures into a naming/process proposal when a sub-organ bed series actually needs it.
- **N8 · agents approving low-key things.** Verbatim (said: majkee R9-1): "agents (folding architecture, managing session) can have competence to approve at least low key things, I do need gavel loop for solving chasing bureocracy." Parked as its own governance question (said: majkee R9-1 B "b1"). It touches the gavel itself (flag L16.1 / L16.12), so any proposal needs a list of what counts as low-key and which seat may approve it, and returns to majkee for a lock.
- Source: nablarva@519a211:.dev/session/nablarva-X3-architecture-sitting/raw/answers.majkee.r9-1-notes.2026-10-22.md and …r9-1-abc.2026-10-22.md.

## 2026-10-23 · carried out of nablarva-X1-architecture at its closure (said: majkee "dragging to next session property which has no shelf is good idea")

Each line keeps X1's own wording and owner. None of them blocks X1's gate. A future head picks one up and gives it a bed, a pulse line or a flag proposal, or deletes it when it is stale. The X1 originals are in git history at X1's prune commit (X1 RUNBOOK U-table, STATUS next:, raw/pad.1-tunnel-support.md). Harness/germline items went to ia-sync germline-03 raw/HANDOFF.oraculum.x1-carried-items.2026-10-23.md, not here.

- **N6 lean added** (said: majkee 2026-10-23): "I'll try manage sessions to have continuous shape by line, that was my question before if we should have flat session numbering or by worktree, organs can develop in subchapters different organ sub-organs in sub loop".
- **U1** relay-00-research: open, or gavel ADOPT-on-own-work · owner majkee.
- **U2** Asymmetry's two blind replies (D7): do they exist, and where? · owner majkee. Relates to L14 D7 (triangulation before locking the relay architecture).
- **U3** first fixture (one tmux session, build-plan §0.2 probes, pane_tty↔PID join; feeds docket 8) · owner: the termpanum line (X2's successor bed termpanum-X0-source-contract and its followers).
- **U4** nablarva-04 app-architecture restart from survivors.nablarva-03; "may fold INTO this bed after check 4" · owner majkee + oraculum · **UNVERIFIED** (said: myShell relay 2026-10-23: "Do not mark either completed merely from the new architecture").
- **U5** POINT 02 → ia-sync jev Cartan (event envelope) · majkee carries · **UNVERIFIED** (same relay). Relates to docket 8 and the four envelopes named in docs/ARCHITECTURE.md §4.5.
- **U6** docket 8 EVENTS map ≤20: confirm after U3 · owner majkee.
- **U7** M3 documentation phase: Cartan placement proposal; oraculum review owed · owner majkee · oraculum.
- **U8** ovitmugen-01 citations of the old nablarva-00 path · owner: the ovitmugen-01 head (its own bed).
- **U9** stridularium UI pass → stridularium-00-design · majkee opens.
- **U12** cartan re-audit of RETURN 04 repairs (ccfb514) · owner cartan. Note: the X1 tunnel table closed 2026-10-23 22:18; any re-audit needs a re-opened or new route.
- **U13** bus GUIDE: slice/suffix rule for per-seat RETURNs under one cycle (Atlas obs §A.3) · majkee → guide keeper.
- **U14** PROJECT.yaml `docs:` line for the stridularium wrapper · one writer, later.
- **U15** reposoma commit of the three cold-start cards · owner majkee (commit state not verified at X1 closure).
- **U21** louder review channel (notify-send from the reposoma cron): the first deferred item to return if the cron reminder alone goes unread · owner majkee.
- **J2** AGENTS.md still describes the architect as owning gates/pulse; PROJECT.yaml keeps the older seat list · a separately owned saddle reconciliation (said: myShell relay, D); not wrapper maintenance.
- **pad.1 F** journal §1.1.4 correction ("your file, your hand") · owner majkee. The other pad.1 items at closure: A, B, C, E, K tested or tuned the released tunnel thread / closed table (obsolete since 2026-10-23 22:18); D and J resolved; H done (all pushed); I resolved by T23 (preamble now ~/.germline/tunnel/tunnel.preamble.md); G moot (the bed protocol file is pruned with X1; the canonical tunnel guide is reposoma raw.guides/tunnel/). The full pad is promoted at .dev/observations/nablarva-X1-architecture.tunnel-support-pad.trajectory.2026-10-23.md.

## 2026-10-24 · carried from X1 check 5 (Houston post-promotion audit, classified "useful" by majkee; dragged by majkee "drag yes")

Source: nablarva-X1-architecture raw/houston-audit.2026-10-23.post-promotion.md (git history at X1's prune commit). One small next session can do all of the docs/ARCHITECTURE.md items together, as an r8 promotion.

- **docs/ARCHITECTURE.md · M3** the promoted doc's `:3` state line still reads "DRAFT r7 for majkee GO — not promoted" (r7 was promoted byte-identical) · owner: the doc's next session.
- **docs/ARCHITECTURE.md · C1** §2 item 5 (`:102–104`) still says "L17 holds unchanged until a GO names one of them"; L21 has superseded it, and L21 itself points readers at this doc. Three `said:` tags now have locks behind them (L18–L20). The audit's options were (a) a short note under the header now, (b) an r8 folding C1+M3+M4+C4; Houston's lean: (a) now, (b) at the next architecture-touching sitting · owner: the doc's next session.
- **docs/ARCHITECTURE.md · M4** source pins owed at promotion were not added. The ones at 519a211 are payable now; the X2 ones (termpanum.build-plan.md, disposition.x3-vectors…) wait until the X2 head commits those files · owner: the doc's next session + the X2 head.
- **docs/ARCHITECTURE.md · C4** §8 calls `docs/decisions/README.md` "the root stub"; it sits under docs/ · fold into the C1 edit.
- **docs/ARCHITECTURE.md · conventional names (05 Q1, majkee "yes")** the audit ranks room truth, deliver, checkout coordination and view/lifetime as gaining most; a bounded research pass on ranks 1–4 first · owner: the doc's next session.
- **C2 · toolbox/termbrana/README.md** §"Layering B — L17" and §Composition still carry the L17 phrase that L21 superseded ("narrow integration edge … not a framework") · owner: the termbrana organ owner.
- **J1b · PROJECT-DESIGN.md §2.2 / §3.6 / §3.8** still describe a pre-architecture state and name the closed session 03 as owner · owner: a wrapper sitting (majkee).
- **X1 tunnel.preamble.md** — two live ia-sync vaults (`tunnel-03-feedback-upgrade/tunnel.state.json` and `tunnel.fork.state.json`) take their preamble from `nablarva/.dev/session/nablarva-X1-architecture/tunnel.preamble.md` (sha256 c2153598…), which differs from `~/.germline/tunnel/tunnel.preamble.md` (f84e51eb…). It is kept out of X1's prune until tunnel-03's owner repoints the vaults or moves the file · owner: tunnel-03 head / majkee.
- **Audit stamps diff did not apply** — raw/houston-audit.2026-10-23.post-promotion.diff (4 hunks, `checked:` stamps in PROJECT-DESIGN.md; majkee "stamps yes") fails `git apply --check` at `PROJECT-DESIGN.md:96` against the current file (59cdcdac…). Houston wrote it by hand without a shell. Regenerate it from the current bytes, in the J1b wrapper sitting or a short Houston audit-mechanics turn, then apply after `--check` · owner: majkee (invokes) / Houston (writes).
