# Shared task terminal — bounded consultation brief

2026-11-17 · Cartan · home/hruzam · nablarva core @3318b17.
Status: experimental preparation; no architecture lock.

## Outcome and competing hypotheses

A full terminal means a PTY-backed process session with continuing working directory,
environment, foreground jobs, interactive input and output. The operator wants agents and
human to work there together. Whether the human attaches to the same PTY, proxies it, or
hands over through another interface is open.

Compare native facilities, reuse of existing components, a minimal local adapter, and
CLI-authored request files consumed by a container worker. A request file may carry a
shell command, script or prompt; those are different payload types and must be identified.
A prompt to another agent is not equivalent to shell input. A container may persist a PTY
or start a fresh process per request; only the former directly addresses session state.

## Candidate regimes, not adopted policy

Observe-only; stage-for-human-approval; agent control of one disposable shell; explicit
human takeover. Compare this tentative list against native permission mechanisms and
against the actual component that can enforce it. Define effect boundaries, workspace,
network, mounts, secrets, long-running jobs, interrupts, stale/replayed requests and
identity. Do not assume shell text is safely classifiable by a command-name allowlist.

## Local sweep and adjacent evidence

Finite search: .dev/session/, .dev/observations/, docs/, toolbox/ and portable
~/ia-sync/codex/ and ~/ia-sync/zsh/, excluding operator vaults and .git. Exact proposed
slugs terminal-workspace/task-terminal/shared-terminal had no matches before this bed.
No .dev/observations/terminal-workspace* predecessor was found. This is a local collision
check, not public namespace clearance or a whole-host exhaustive search.

- flag L3/L4: adapter-owned PTY, tmux not the protocol; rejected input mechanisms stay rejected.
- flag L14 and docs/ARCHITECTURE.md §§1–2: relay research boundary and file spine; avoid silently
  turning task-shell execution into input delivery to the agent's conversation.
- flag L17/L20/L21: observation, composition, decision and actuation authority remain distinct;
  shared layers may be designed but implementation/adoption needs its separate release.
- PROJECT-DESIGN.md §§3.1–3.2: terminal/composition intent and ovitmugen view/lifetime ownership.
- PROJECT-DESIGN.md §§3.5–3.8: muticula, observation lab, broker/delivery and human-view boundaries.
- .dev/session/phone-console-01-browser/raw/terminal-trial.host-return.2026-10-30.md reports
  pinned ttyd + xterm and owned disposable shell fixtures, identity/auth/origin checks,
  no replay, detach preserving shell lifetime. Historical report, not requalified here.
- .dev/session/termpanum-X0-source-contract/ and termpanum-X1-source-qualification/ already
  distinguish source bytes, rendered terminal state and inferred task meaning. Reuse that
  distinction; do not claim this research qualifies their production collector.
- .dev/session/nablarva-02-pipe-qualification/ concerns assignment into a running agent;
  that is a different endpoint and acceptance question.
- .dev/session/sublime-observer-X.ledger.md supplies line naming and explicit sharing context;
  observation publication there does not supply terminal execution authority here.

Read current source for any reuse claim. Check historical report wording before citing it
as local evidence. No live service/session, editor, runtime directory or vault inspection.

## Outputs and ownership

Cartan owns the bed documents, saved reply transcripts, synthesis and STATUS. Delegates
return read-only findings; they do not write or delegate. Save actual route metadata and
reply bodies without manufacturing persistence or model observations. Houston's current
consult card is read-only even though the project's older addendum describes a write-capable
landing path: the controller preserves the finding instead.

Gate: Majkee records GO or STOP on an evidence-backed preparation packet for a human-and-agent shared task terminal: dated native/reuse alternatives, Oraculum technical consultation, Houston architecture and documentation review, a disposition of file-fed container requests and operator-selected input regimes, and the exact scope and proof obligations of one recommended next experiment.
