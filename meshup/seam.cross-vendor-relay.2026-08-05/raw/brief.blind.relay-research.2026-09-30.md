---
brief: blind · research
to: Asymmetry (ChatGPT)
from: majkee — drafted by Symmetry; problem and constraints only, no Symmetry findings or conclusions
date: 2026-09-30
mode: BLIND — answer before reading any other seat's take on this topic
use: wheel check + vendor-harness check for a big-scope research gate
---

# Research brief — tracking and relaying CLI agent sessions

## Situation

One operator runs interactive CLI coding agents from three vendors — Claude Code, Codex CLI and Antigravity CLI (`agy`, Google's successor to Gemini CLI) — in tmux on a workstation, reached from a phone over Tailscale. Sessions coordinate through markdown files: each session folder holds its state and a `_bus/` of message files between seats. Today the operator relays between sessions by hand. He wants routine relay automated; only strategic decisions should reach him.

His current choice: the PTY/terminal is the common layer to build on, because every CLI runs in one. The terminal should yield only the signal that something happened; content goes to files.

## Question

What is already published — open source, documentation, write-ups, issue threads — about:

1. detecting the state of an interactive CLI agent session from outside the process (working, idle, waiting for input or approval, compacting, crashed/exited);
2. delivering a message into a running or idle session;
3. relaying between sessions of different vendors;
4. the terminal layer itself, as it bears on (1): tmux capture and send-keys semantics, PTY and terminal-emulation libraries, bracketed paste, alternate screen, OSC/title signals, process and wait states.

And: which vendor-native changes, shipped or announced, would make a PTY-based tracker unnecessary?

## Objective function

Maximize reliable, dated evidence of what already exists and what the vendors are shipping. Novel design is out of scope.

## Evidence set

Primary sources first: vendor docs, changelogs and release notes, source repos, issue trackers. Secondary write-ups only when they point back to a primary source.

## Blind spots to watch

- Vendor behavior changes release to release; date everything.
- Marketing claims versus observed behavior.
- "Works in my demo" versus tested unattended runs.

## Deliverable

1. Source table: name · link · date · what it does · which layer it reads or writes (terminal/PTY · on-disk session records · hooks · vendor protocol or API) · states it detects · evidence type (documented / observed / claimed) · maintenance signal.
2. Per vendor: which session states are reliably detectable without interpreting screen content, and which require it.
3. Gaps: what nobody has solved.
4. Verdict on the operator's plan: REINVENT · ADOPT (name what, and the delta) · REFUSE — plus one falsifier, the observation that would overturn your verdict.

Your answer will be collided with an independent one; majkee gates the collision. Commit to an answer — consensus with anyone else is not a goal.
