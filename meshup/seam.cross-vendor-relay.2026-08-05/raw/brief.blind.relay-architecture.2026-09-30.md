---
brief: blind · architecture
to: Asymmetry (ChatGPT)
from: majkee — drafted by Symmetry; problem and constraints only, no Symmetry design
date: 2026-09-30
mode: BLIND — answer before reading any other seat's take on this topic
use: independent architecture + overengineering check for a big-scope research gate
---

# Architecture brief — automated relay between CLI agent sessions

## Situation

One operator runs interactive CLI coding agents from three vendors — Claude Code, Codex CLI and Antigravity CLI (`agy`, Google's successor to Gemini CLI) — in tmux on a workstation, reached from a phone over Tailscale. Today he relays between sessions by hand. He wants routine relay automated; only strategic decisions should reach him.

## Canon in force — fixed, not up for redesign

- Truth lives in files. A session has one gate, a RUNBOOK and a STATUS. Seats exchange `_bus/` message files of three kinds: POINT, RETURN, VERDICT.
- A head seat holds strategic decisions and rolls them up to the operator. He gavels anything that promotes, deploys or becomes canon.
- Kill test (from your side, earlier): stop if reliable unattended crossings require continuously parsing or emulating vendor UI semantics — UI parsers, command ontology, version-specific state machines. Then fall back to native orchestration per vendor plus manual cross-vendor gates.

## The operator's choices so far — constraints; challenge each at most once, with reasons

1. The PTY/terminal is the common layer, because every CLI runs in one. Vendor-specific wake mechanisms are parked until the vendors shift.
2. The terminal yields only the signal that something happened; message content goes to markdown files.
3. Every prompt, hand-written included, is structured: addressed blocks in markdown or a programmatic enclosure a parser can find.
4. Sending is always bound to a shell command or a hook.
5. Later, a cheap model may learn to read terminal windows.
6. The phone is a thin client; sessions live on the workstation.

## Question

Design the architecture that relays routine messages between sessions automatically, across all three vendors, with only strategic decisions reaching the operator.

## Objective function

Fewest moving parts that make routine relay unattended and survive a vendor changing its CLI. Vendor-neutrality and a sovereign file plane beat features.

## Blind spots to watch

- Designs that quietly make a server, queue or broker the source of truth.
- Parsers that drift from detecting state into interpreting content.
- The human leaking back in as the routine path.

## Deliverable

1. About ten numbered, falsifiable axioms.
2. Components: what each does, and where its state lives.
3. One crossing, step by step: seat A on one vendor → seat B on another, idle at the moment of sending.
4. Escalation: what reaches the operator, and how.
5. Failure modes, ordered by risk.
6. The first build slice, and what not to build yet.
7. Overengineering check: is this complexity earned, or does a smaller composition of existing parts serve?
8. Your committed answer, plus one falsifier.

Your answer will be collided with an independent one; majkee gates the collision. Commit to an answer — consensus with anyone else is not a goal.
