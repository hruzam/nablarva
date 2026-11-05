# nabLarva / VIST HELLO world — raw experiment

Operator scope, 2026-10-25: “small experiment in raw”; “In fact nablarva|VIST hello world”; selected “Two fresh disposable real CLI sessions”. X1 architecture preparation is committed at `cb08d6f`; X4 has no executable RUNBOOK. This is a bounded operator-requested raw demonstration, not X4 gate completion, Q qualification, a shared-layer release or a promoted protocol.

## What this demonstrates

Two fresh interactive CLI sessions receive one assignment at launch. The sender chooses an ordinary animal word and sends a HELLO through an immutable file. The receiver reads the actual message and composes one correlated reply repeating that word. The sender's bounded helper wait returns the reply; it confirms it read the reply, and both end their turns. The supervisor waits briefly for final screen output and destroys only its own disposable tmux server. Available pairs are `codex-codex` (default), `claude-codex`, and `codex-gemini`. Majkee authorized the alternatives after Claude refused subscription access. See `FINDING.md` for actual outcomes.

A separate observer reads their rendered screens and the protocol receipts. It records changed screen bytes as `state: unknown`, separately from receipt-file evidence. Paint is never promoted into collaborator identity, readiness, acceptance or completion. Event labels are `experiment.*`, not an adopted VIST envelope. This is VIST's observational separation demonstrated at minimum scale; it is not a qualified busy/idle detector or Antensor implementation.

## Deliberate reduction of HELLO r0+r1

- One opener, one reply, one sender confirmation. Replies never invite another reply; duplicate writes fail.
- No bell, `send-keys`, input injection, native queue, vendor hooks, MCP transport, headless CLI or resumed session. Startup assignments are operator-authorized initial prompts, not delivery into existing sessions.
- Unlike r0's proposed asynchronous wakeup, one helper may wait up to 240 seconds for its expected file. This small bootstrap experiment does not demonstrate waking an idle agent or qualify live delivery under L4/L14.
- No registry/shared-substrate implementation, settings install, `~/.nablarva` write, daemon deployment, adopted schema, publication or commit. Scripts and experiment evidence remain here. Native CLI authentication/history remains host-local in the CLI's normal state directories.
- Existing CLI models and authentication are inherited. Codex keeps workspace-write/on-request; Claude receives only a scoped allowance for this helper. Gemini uses default approval mode and a process-local `--policy` file allowing this run's helper prefix only. This is not an OS sandbox; ordinary native defaults still apply. Permission/trust dialogs are never auto-confirmed by the observer.
- Fresh tmux socket under `/tmp/nablarva-hello-<run-id>.sock`; no default or ovitmugen server access. Target bindings are recorded. Scripts never write terminal input; cleanup is scoped to the owned disposable server.
- Codex and Claude run from the established Nablarva root. Gemini runs from this directory, with the operator-requested `GEMINI.md` limiting it to the assigned HELLO. Native ancestor/global context loading remains in force; its UI reported three GEMINI.md files. Prompt write scope is only helper-generated files here; this is a cooperative assignment boundary, not an independent OS security boundary.
- Gemini's inherited startup behavior reported an automatic update from 0.56.0 to 0.65.0 during the attempted run. No update command was requested by the head. This is a real host-side effect, recorded in the run; the experiment is not host-state-neutral.

## Run and inspect

```sh
python3 .dev/session/nablarva-X4-vist/raw/hello-world/hello.py selftest
python3 .dev/session/nablarva-X4-vist/raw/hello-world/hello.py start --timeout 300 --pair codex-codex
```

The live command needs the host's normal CLI state/network access. Each run creates a new `runs/<timestamp>-<nonce>/`, never overwriting earlier evidence. A pass needs `hello.json`, `reply.json` and `confirmed.json` with exact parent IDs. `result.json` records the bounded outcome. `observations.jsonl`, `screens/`, version/cwd/socket records, bindings and exact startup prompts are retained. TIMEOUT is not PASS; inspect the captured screen for an actual approval, authentication or tool problem before any retry.

Mechanical preflight checks: immutable publication, wrong-parent refusal, duplicate opener/reply refusal, reply-to-reply refusal, and final confirmation. Real success additionally requires inspecting the actual receipt bodies and both CLI screen evidence; the supervisor's label alone is not the complete finding.

## Sources and limits

- `../hello-01-contract.md`, `../hello-02-addendum-r1.md`: source concepts, explicitly reduced above.
- `../vist-01-principle-and-applications.md`: observations separated from decisions/actions.
- `../consult.hello-grounding.2026-10-23.md`: screen evidence limits and unreleased automatic bell.
- Current `docs/ARCHITECTURE.md` and flag L3/L4/L14/L17/L20/L21/L24 remain governing; this test selects no transport exception.
- Interactive startup prompts/options checked against installed CLI help (Codex 0.164.0, Claude Code 2.1.310) and [OpenAI CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli), [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference). Runtime behavior still requires the recorded run.
- Gemini options checked against installed 0.56.0 help; [GEMINI.md context](https://geminicli.com/docs/cli/gemini-md/) and [policy engine](https://geminicli.com/docs/reference/policy-engine/) informed the local instruction file and temporary helper allowance. Neither was proven behaviorally: the provider refused the first model request.
