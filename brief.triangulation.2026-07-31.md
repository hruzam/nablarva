# Design brief — multi-participant room for humans and terminal AI agents

You are asked to propose a system architecture from scratch. No existing
design is being evaluated; there is no preferred solution hidden in this
brief. Propose what you would build, and argue for it.

## Problem

A small working group communicates and plans together. Participants are:

- one or more humans,
- two or more AI coding agents, each running as a **live interactive session
  of a terminal CLI tool** (Claude Code, Codex CLI, or similar).

Crucially, each agent session is **rooted in its own project directory** and
carries that project's context. The sessions are peers — none is a parent or
subprocess of another. The native "spawn a subagent" feature of these CLI
tools cannot produce this topology: a subagent is a child of one session, not
an independent peer rooted in a different project.

### Motivating scenario (pilot)

A company migrates an old OpenCart admin to a new Laravel application. One
agent session runs inside the OpenCart repo and knows it deeply; a second
agent session runs inside the Laravel repo. The human supervises. The two
agents must consult each other in near-real-time to produce a migration plan,
each answering from its own project's perspective, while the human steers.

## Requirements

1. **Peer sessions.** Two (later N) live CLI agent sessions, each in its own
   project directory, exchanging messages while remaining alive and
   interactive. Version 1 may assume all sessions run on the same machine.
   A later version must extend to sessions on different machines.
2. **Directed addressing.** Any participant (human or agent) can address a
   message to all participants, to a subset, or to exactly one participant.
3. **Private lines.** A participant can send a message intended only for one
   other participant — e.g., agent-to-agent technical traffic the human does
   not want surfaced, or a human side-question to one agent that should not
   enter the other agent's working context.
4. **Read economy.** A participant should be presented only with what it
   needs: not its own past output, not traffic addressed elsewhere. Agent
   context windows are a scarce resource; the mechanism must actively
   minimize what each agent re-reads. A participant rejoining after absence
   should be able to catch up cheaply.
5. **Goal stability / anti-drift.** Extended agent-to-agent exchanges are
   known to drift away from the original objective. The system must include
   a regulation mechanism that keeps the conversation anchored to a stated
   goal and gives the human effective control points.
6. **Auditability.** The group's communication should form a durable,
   inspectable record: who said what, to whom, in what order. A human must
   be able to review the full history, including traffic that was not
   surfaced to them live.
7. **Clean text.** Agent CLI sessions emit decorative/process noise
   (spinners, tool-call chatter, status lines). The system must extract the
   meaningful text I/O from a session and transport only that.
8. **Lightweight observation.** The human observes and participates using
   lightweight existing tools. Assume a user whose daily editor is Sublime
   Text and whose culture is Unix/Linux command-line composition. No
   Electron-style application, no heavyweight IDE, no browser requirement.
9. **Minimal moving parts.** Prefer mechanisms already present on a typical
   Linux/macOS developer machine over new long-running services. If you
   introduce a daemon or server, justify why nothing simpler suffices.

## Deliverables of your proposal

A. **Architecture** — the components, what state exists, where it lives, and
   how a message travels end-to-end from one participant to another
   (including into a live CLI agent session).
B. **Addressing and visibility model** — how directed and private messages
   are represented and enforced, and how it satisfies requirements 3, 4, 6
   simultaneously.
C. **Anti-drift regulation** — a concrete mechanism, not a principle.
D. **Failure and restart story** — what happens when a session dies or a
   participant rejoins.
E. **Version 1 cut** — the smallest same-machine implementation you would
   build first (name the technologies), and what you would defer.
F. **Trade-offs** — the two or three decisions in your design you consider
   most contestable, and the strongest argument against your own choice.

Answer in markdown. Be specific about mechanisms; avoid generic advice.
