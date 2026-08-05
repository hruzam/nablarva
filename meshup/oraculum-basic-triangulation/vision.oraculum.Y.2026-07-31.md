# Vision Y (Oraculum) — the room is a process

> Triad seat: Y. Stands AGAINST vision X (majkee: the room is a file —
> roller + git-diff wire + composer + cooperative anchors). Sealed from the
> Z brief (blind triangulation); Z must never read this before answering.
> 2026-07-31, append-only.

## The bet

X bets on no living parts: ledger-mediated, regulation by convention.
Y bets on one living part: **bus-mediated, regulation by structure** —
a seat cannot read what the router never delivers, cannot drift on traffic
it never receives, and privacy is enforced physics, not etiquette.

## Shape

One small static binary — the **stridulator** (C++ or Go, no runtime deps):

1. **PTY adoption.** Each agent CLI session runs under a PTY owned by the
   stridulator. Noise-mining (spinners, harness chrome) happens at the
   terminal layer — clean utterance extraction, no pane scraping, and
   injection into a live session is a plain write to the same PTY.
2. **In-memory envelope routing.** from / to / visibility routed over Unix
   domain sockets. No polling anywhere; delivery is push, sub-second.
3. **Structural regulation.** Turn quotas, drift gates, goal re-anchoring
   are router-enforced: the stridulator withholds delivery until a gate
   passes, injects the pinned goal on schedule, and can hold agent<>agent
   free-run to N turns mechanically. Agents need no discipline; the wire
   has it.
4. **Journal as memory.** Every routed envelope appends to a per-room
   journal file (full ledger, including undelivered-to-you traffic).
   Sublime/Zed observe by tailing the journal — the monitor is still just
   a file. Git may archive journals; it is not the wire.
5. **Cross-host = same socket over a tunnel** (SSH/Tailscale). Topology
   unchanged; only the transport under the socket changes.
6. **Engine socket.** Hardcoded mathematical mechanisms (majkee's engine
   research) plug into the router as filters/compressors/schedulers —
   a natural home that vision X does not offer.

## Failure story (the honest cost)

- X fails soft: a file is always readable; the room survives every crash.
- Y fails hard: dead router = dead room. Mitigation: journal is the only
  state; the stridulator is stateless-restartable by replaying its own
  journal tail. PTY children survive via reattach (tmux-style) or are
  re-adopted on restart. This mitigation is the most contestable part of Y.

## Most contestable decisions (self-audit)

1. A daemon at all — against the lightness constraint. Defense: one static
   binary is lighter than a polling choreography of hooks, cron, and git
   plumbing; "light" should count moving parts at runtime, not processes.
2. Router-enforced regulation — risks rigidity; a gate wrongly tuned blocks
   good work. X's cooperative anchors degrade more gracefully.
3. PTY adoption — couples Y to terminal mechanics of each vendor CLI;
   a CLI that repaints aggressively fights the miner.

## Convergence forecast (for the comparison pass)

Likely hybrid if Y loses on lightness: X's ledger as the room truth +
a Y-style enforcement point ONLY at the injection leg (the one place where
structure beats convention cheaply). Recorded now so the forecast can be
scored honestly against Z's blind answer.
