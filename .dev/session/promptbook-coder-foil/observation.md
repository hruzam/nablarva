# Promptbook Coder foil — harvest note

`status: OBSERVATION — task-scoped, not canon, not a plan, no implementation authorized`
`observed: 2026-08-26 · source: ~/projects/ext-sources/promptbook @ baf10bfd`

## Why keep this foil

Promptbook Coder has a useful operator shape: agent/run trees, readable queued and
finished work, explicit lifecycle, runner adapters, evidence sidecars, and direct actions
such as retry, cancel, or revert a project commit. Its architecture is not nabLarva's:
Promptbook coordinates per-agent repositories and parent→teammate calls, while nabLarva's
locked center is a neutral append-only room journal with participant projections.

Harvest the affordances, not the topology.

## Candidate harvest — session tree as task ladder

A future session tree could be a disposable, on-request projection of file truth into a
task ladder, for example:

```text
goal revision
└─ task
   └─ attempt
      ├─ evidence / artifact
      └─ checkpoint / outcome
```

- The journal, `flag.md`, and `pulse.md` remain authoritative; the tree is never a second
  truth surface.
- Ladder state is derived from explicit events and receipts, not inferred from prose or
  maintained as another hand-written plan.
- A requested "orchestration stream" may render only the active path plus its next safe
  actions, while the full event history remains inspectable.
- Buttons emit bounded commands or compensating events and then record receipts. They do
  not rewrite history. A project commit revert is an operator-scoped project action, not a
  rollback of room truth.
- Vendor-specific execution remains behind adapters; task identity, provenance, goal
  revision, delivery state, and checkpoint meaning remain vendor-neutral.

`orchestration stream` is a working phrase only. Run the naming and interference sweep
before landing any machine-surface name.

## Smart pieces worth re-reading

- Small harness adapter port: `scripts/run-codex-prompts/runners/types/PromptRunner.ts`
- Multi-repository queue supervisor and bounded scheduler:
  `scripts/run-agent-messages/main/runMultipleAgentMessages.ts` and
  `RunMultipleAgentMessageTaskScheduler.ts`
- Durable job states, attempts, leases, and one-running-job-per-chat:
  `apps/agents-server/src/utils/userChat/claimNextQueuedUserChatJob.ts` and migration
  `2026-03-0180-user-chat-jobs.sql`
- Human-readable `.book` queue, finished/failed transitions, run reports, and TEAM
  transcript sidecars under `scripts/run-agent-messages/`

## Boundary and harvest trigger

Do not fold this into Termbrana before its M0 host contract is frozen. Reopen the foil when
either nabLarva's journal/task event schema is on the gavel table or Termbrana reaches the
post-M0 operator-view lane. First experiment should be read-only: render one existing task's
events as a ladder and measure whether the next safe action is easier to locate.
