# Proposed next experiment — terminal-workspace X1

2026-11-18 · inferred: Cartan · proposed execution scope, not a release.
Provisional sibling: `terminal-workspace-X1-file-roundtrip`; finite name sweep found no
existing matching session. No successor bed is opened by this proposal.

## Why this is next

X0 has approaches research, Oraculum technical advice, Houston's constrained architecture
review and basic owned-PTY feasibility evidence. Majkee then explored collection/history,
caching and usage regimes and said “Sounds fair. Whats is next?” This is agreement to the
discussion's direction, not an inferred final mechanism or implementation gavel.

The smallest new evidence is an end-to-end file round trip against the already-demonstrated
synthetic persistent shell. Native/shared human attachment remains a separate qualification
question. This narrows the first experiment; it does not replace X0's wider six-row matrix
or select a custom manager over native/reusable facilities for the eventual product.

## Proposed single gate

Majkee records GO or STOP on an independently checked synthetic file-to-task-terminal
round trip: an explicitly submitted command file reaches one newly owned persistent
shell exactly as intended, correlated output and truthful outcome are readable, incomplete,
changed, duplicate and stale-target requests do not cause unintended execution, and the
owned processes and temporary runtime are cleaned up with retained evidence.

## Concrete demonstration

1. Start a disposable executor and one clean-start Bash shell in an owned PTY. Record the
   runtime namespace, target incarnation and fixed synthetic execution scope.
2. The agent-side fixture writes a command file. Preparation alone performs no execution.
3. A separate explicit submit operation adopts that exact content. Choose the submission
   mechanism in the X1 launcher; ordinary file close/save is not implicitly submit.
4. The executor executes the approved synthetic request in the same shell. A later request
   confirms retained cwd and an exported variable, with shell identity recorded.
5. A reader receives the corresponding output reference and completion/exit evidence.
   Capture pending, rejection, failure and uncertain termination truthfully.
6. A separate verifier checks both the effects and the records against frozen expectations.

Illustrative run-local artifacts: submitted request files, output chunks, a small serialized
`events.jsonl` and a current-state snapshot. They are an experimental format, not an adopted
shared schema. A Markdown history may be a disposable generated view; it is not needed to
prove the first round trip. Native agent conversation logs stay outside this fixture.

## Scope and effect proposal

- Standard-library Python 3 fixture helpers plus installed Bash, as used in X0. This is an
  experiment-local choice, not the animal's language or product stack.
- Source and retained evidence only in the proposed successor bed if released. Each run
  uses a newly allocated private `/tmp/terminal-workspace-<unique>/` directory and its own
  child PTY/processes, clean startup, controlled nonsecret environment and bounded timeouts.
- Start-up authority is limited to the frozen harmless synthetic command corpus. Record
  actual grant and exact approved content before execution. This proves fixture behavior,
  not protection from arbitrary shell code or enforcement of a vendor permission mode.
- Only the executor writes execution events; participant labels reflect the actual ingress
  route. Do not infer who typed from terminal echo. PTY output need not separate stderr.
- Cleanup addresses only owned processes in the recorded namespace and exact temporary
  paths. Retain requests, outputs, expectations and reports as evidence.
- Native Claude/Codex facility qualification, actual human attach/takeover, existing tmux or
  ovitmugen panes, containers, network services, arbitrary jobs, durable daemon installation,
  product permissions and whole-history collection are outside this first experiment.

## Required evidence

- Positive: exact submitted payload and target binding; output correlation; persistent shell
  state across two requests; meaningful nonzero command result; bounded job interruption;
  actual shell/child exit and exact-path cleanup.
- Negative: a draft is never executed; changed content cannot reuse an earlier approval;
  duplicate submit cannot repeat a harmless counted effect; an old target reference cannot
  operate a replacement process; receipt loss produces uncertainty without automatic replay.
- Oracle: freeze expected outputs and independent effect markers before running the executor.
  A matching log alone does not prove that the shell performed an effect.
- Completion evidence is qualified for these controlled fixtures. Do not generalize a printed
  sentinel to arbitrary shell/TUI command completion, nor claim exactly-once execution across
  every crash interleaving.

## After this gate

Use its result to choose the smallest qualified process-owner/attachment path. Then qualify
actual human attachment, input takeover and native CLI access, preserving ovitmugen lifetime
and the distinction between task-program input and conversation delivery. Only after that
should collection/retention policy, usage regimes and a durable component home be selected.

X0 acceptance and X1 execution are distinct decisions. An operator may explicitly give both
in one instruction; neither is manufactured from “Sounds fair.” Exact release belongs in
its actual receipt and later launcher, preserving flag L17/L21 and X0 RUNBOOK constraints.
