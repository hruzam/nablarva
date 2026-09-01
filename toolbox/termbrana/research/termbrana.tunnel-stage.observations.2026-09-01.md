---
what: Tunnel-stage observations — synthesis of the two 2026-09-01 Epoch passes + the cross-runtime
      architecture context; the design input for session toolbox-termbrana-03-tunnel task t1
state: OBSERVATION + one recorded gavel (§4) — mechanics verdict still belongs to session t1
       (oraculum + cartan + majkee)
verified: 2026-09-01 (sources: research.epoch.tunnel-claude-side.2026-09-01.md ·
       research.epoch.tunnel-codex-side.2026-09-01.md · ~/ia-sync/HANDSHAKE.md r2 ·
       termbrana.project-definition.md laws 2.4/2.5)
by: oraculum (claude/opus, office, session fc-sync.oraculum.sella)
next:
  - "session 03-tunnel t1: per-leg MECHANICS verdict within the gaveled v0 shape (Cartan's live evidence outranks research on volatile CLI facts)"
  - "L11: no code until M0 freezes or exception recorded"
---

# Tunnel stage — what the evidence actually says

## 1 · The topology is three legs, not one tunnel

- **Claude ↔ Claude: SOLVED NATIVELY.** SendMessage/ListAgents (v2.1.224+) delivers
  peer-mail into a live peer session with built-in peer-framing. Build nothing here;
  law 2.5 (native outranks replica) applies verbatim.
- **Claude → Codex:** the contested leg. Candidates: (a) `codex app-server` JSON-RPC
  (`thread/start|resume`, `turn/start|steer|interrupt`) — official, robust, headless;
  (b) pane injection into a rendered Codex TUI — `zellij action paste --pane-id`
  preferred over `tmux send-keys` (bracketed-paste native; tmux carries the
  Claude-specific #31739 regression), WITH the ≥120ms text→Enter gap mitigation.
- **Codex → Claude:** pane injection into the Claude TUI (`zellij action paste`), or —
  if the Claude seat is reachable as a teammate — a bridge process that converts Codex
  output into a SendMessage. Injection mid-generation QUEUES on Claude (verified) —
  safe; permission-dialog behavior is an UNVERIFIED gap → pilot item.

## 2 · Substrate ranking (pre-t1, advisory)

| Mechanism | Strength | Weakness | Role |
|---|---|---|---|
| Claude native messaging | official, framed, live | Claude-only | Claude↔Claude leg, and the Claude-side terminus of any bridge |
| `codex app-server` | official JSON-RPC, steer/interrupt, resumable threads | headless — no rendered TUI; co-presence RFC (#21551) died unshipped | **v0 Codex leg (gaveled — §4)** |
| `zellij action paste` | bracketed-paste, pane-id addressing, termbrana's own host | needs enable + envelope discipline; 120ms gap on Codex TUI | **v1 visible mode (gaveled — §4)** |
| `tmux send-keys` | ubiquitous pattern | #31739 Claude regression; two-step Enter discipline | avoid unless zellij disqualifies itself in pilot |

## 3 · Hazards ledger (carry into the pilot checklist)

1. Codex TUI paste-burst/Enter-suppression — ≥120ms gap (issue-sourced constants 8ms/120ms
   are M-confidence; verify empirically, don't hardcode blindly). v1 concern.
2. tmux #31739 (Claude post-interrupt send-keys breakage) — M, direct fetch pending. Moot
   for v0; relevant only if zellij disqualifies in v1.
3. Claude permission-dialog under injection — unverified (L); v1 pilot must probe it.
4. Vendor-named PTY systemic hazards (draft-without-submit, injection racing human
   typing, no attribution/replay — Codex issue #15355) — exactly the provenance problem
   termbrana laws 2.1/2.6 exist for. Every tunnel message carries an envelope the
   observer can attribute.
5. Codex-native multi-agent (for v2 architect-with-crew): confirmed UNSTABLE via live
   open bugs — v2 stays gated on Cartan's verification, do not design against it yet.

## 4 · Living vs visible — DECIDED

> **GAVELED — majkee, 2026-09-01 (at desk, session fc-sync.oraculum.sella):**
> **v0 = app-server-first** — prove the round-trip via `codex app-server` (living,
> steerable, headless Cartan thread) + native Claude messaging on the Claude side.
> **v1 = visible mode** — render the Codex thread into a pane termbrana can observe
> (zellij-paste mechanics where injection is needed).
> The recommendation below stands as the decision; t1 retains only the per-leg
> mechanics verdict within this shape.

Original reasoning, kept for the record: app-server gives a *living* mind but not a
*visible* one; pane injection gives the twin-TUI picture on the flakier substrate. The
round-trip gate does not require visibility — and law 2.1 (truth vs projection) suggests
the rendered view IS a projection layer, which is termbrana's own job description. The
tunnel and the observer converge into one project.

## 5 · Effort re-estimate (supersedes the 2026-09-01 mobile estimate)

- **v0 (gaveled shape):** app-server client shim (`thread/start` + `turn/start|steer`,
  result read-back) + native Claude messaging terminus + round-trip proof: **4–6 h.**
- v1 (visible mode: render Codex thread into an observable pane + duplex discipline +
  HANDSHAKE TABLE shape r3): **+3–4 h.**
- v2 (architect-with-crew): **gated** on multi-agent stability — do not schedule.

## 6 · Governance unchanged

flag L11 holds until M0 freezes or majkee excepts. This file is design input plus one
recorded gavel (§4), not a start signal. Mechanics verdict = session t1 with @Cartan
seated; his live Codex evidence outranks both Epoch reports on volatile CLI facts
(HANDSHAKE precedence).
