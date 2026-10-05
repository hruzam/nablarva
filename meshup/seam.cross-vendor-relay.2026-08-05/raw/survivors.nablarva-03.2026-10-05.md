---
survivors: nablarva-03-app-architecture — what outlives the closed session
date: 2026-10-05 · oraculum (loop 1.7, majkee ruling M1 2026-10-05: session stale → CLOSE; keep external/operator inputs; purge the rest)
source bed: .dev/session/nablarva-03-app-architecture/ (opened 2026-09-29, Cartan head, Flight challenger) — preserved whole at commit fd66470; pruned 2026-10-05
restart: a numbered sibling (nablarva-04-app-architecture) when majkee opens it with oraculum; this file is its first input
quotes: verbatim from raw/architecture.working.md as committed in fd66470 (Cartan, §1 premises re-aimed 2026-10-04 per POINT 03)
---

# survivors — session 03

Three statements lived only in the head's working candidate and in no DESIGN file. They survive here, unchanged, as **input** — not as a lock, not as the restart's answer.

## 1 · The animal-ownership statement (architecture.working.md:37-40)

> nabLarva should own the continuity of an exchange: who addressed whom, what was released, what delivery evidence exists, which reply belongs to it, and what still needs attention. Its clients may be shell commands, a terminal panel, an editor or a phone. Choosing a GUI is independent of giving the application those boundaries.

And the first useful experience as the candidate named it (:42-46):

> collect a prompt, choose a living colleague, release it, see the reply beside it, continue. The recipient acts in its own session under its own permissions. Majkee can inspect the inter-session roller without becoming the routine courier. Visible pending work and honest uncertainty matter more than an impressive dashboard.

## 2 · The bounded exchange loop — five steps (architecture.working.md:60-84)

> The proposed animal is a **bounded exchange loop between independent living sessions**, with durable files carrying selected work and replaceable adapters handling the qualified PTY impulse under L3/L4 and L14 D1/D2. Native hooks/records may enrich observation; their availability cannot decide whether the PTY base exists. "Hardcoded attractor" means explicit routing, correlation, limits and stop conditions outside model prose. It does not mean hardcoding the agents' conclusions or forcing agreement.
>
> 1. Majkee starts a bounded task with named peers, allowed work and a completion condition. Those peers may be different vendors; responsibility is assigned by the task, not permanently attached to a vendor.
> 2. A sender publishes the selected assignment and exact expected reply destination. The exchange mechanism checks that it belongs to this task and recipient before requesting activation through a qualified adapter.
> 3. The recipient reads and works in its own native session and permission context. It may use permitted specialists from its runtime's roster; it remains responsible for their work and the outward reply. Helpers need not become bus participants.
> 4. A complete, correlated reply becomes available to the designated next peer. Its qualified activation/read completes the transport loop. The peer reviews the work and may publish the next permitted assignment; receipt and acceptance remain different facts.
> 5. The cycle continues only within its declared scope and finite limits, or finishes on its completion condition. A budget or round limit stops an unproductive loop; it cannot prove semantic agreement. Exact limit values remain to be chosen for the first trial. No unsolicited peer discovery, automatic retargeting or blind retry.

## 3 · Event → human role (architecture.working.md:93-99)

| Event | Proposed human role |
|---|---|
| In-scope assignment, correlated reply, ordinary review/revision within the delegated task | Inspect when useful; no human copying or approval merely to relay each message. |
| Native permission request or action outside granted scope | Decide through the proper approval surface; the bus preserves the pending exchange. |
| Ambiguous target, uncertain delivery, missing/invalid reply or exhausted loop limit | Receive one actionable attention item with the evidence and available recovery choices; no silent fallback. |
| Product choice, unresolved tradeoff, architectural lock, promotion or deployment beyond existing authority | Decide at the relevant boundary, with the peers' disagreement and evidence visible. |
| Task completion within delegated scope | Receive the result; perform final acceptance where that task requires it, without reopening each intermediate relay. |

Closing line of the candidate (:101-104): *"Files provide inspectable continuity; they do not wake agents, prove consumption, or confer write permissions. … The core must not repair it by interpreting terminal paint."*

## 4 · What the challenger concluded (Flight, MANNED by majkee, 2026-09-29)

- RETURN 00 — **REVISE (small):** the return/attention leg (~19 actions, ~16 min lag) dominates the recorded exchange, so the first slice should target that leg, not outbound send (~5 actions); the nablarva zsh scope is already wired on both hosts (not "unchecked"); manual recipes still run their `check` block on `update`.
- RETURN 01 — **CONFIRM** the consultation / living-peer split; **REVISE** the carrier map: consultation has two existing carriers — ephemeral `codex-run.zsh` relay for a fresh independent opinion, stored-thread `tunnel-codex.zsh` for continuity; earlier docs wrongly routed all second-opinion work to the tunnel.
- RETURN 02 — never arrived (POINT 02 re-aimed by Cartan 2026-10-04; gate closed before Flight answered).

## 5 · External challenge kept beside this file

`review.claude.2026-09-29.md` (one-off Claude Opus 5.5 CLI review, majkee-requested): two BLOCKING findings — product-vs-harness confusion; a wiring contradiction — plus a phase-0 proposal and the cheapest alternative. Kept whole as input for the restart.

## 6 · Operator substrate kept in `room`

The three notebook sheets of 2026-07-30 (SESSION/CLIPPER/ROLLER/COMPOSER · processor sheet · features sheet) with Cartan's SHA-256 + transcription receipt → `meshup/room.brokered-journal.2026-07-31/raw/notebook-2026-07-30/`.

## What did NOT survive (history only, fd66470)

RUNBOOK · STATUS · 7 bus files · `architecture.working.md` as a whole · `tunnel-consultation` · `workflow-reading`. Gate, verbatim, for the record: *"Majkee records GO or STOP on a source-backed, independently challenged architecture blueprint covering animal/toolbox boundaries, code/config/data/runtime homes, delivery/install/wiring/admin lifecycle, and the first prompt/reply slice, with unresolved choices explicit."* — closed STOP-by-ruling (stale), not GO.
