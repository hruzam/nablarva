origin: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/raw/note.oraculum-to-trajectory.2026-10-08.md · preservation commit nablarva@5cc3e19 · promoter: oraculum(cSharp) via delta, 2026-10-23 · moved verbatim at X1 closure (runbook GUIDE §On gate closure)
status: process record, append-only; the bed copy is pruned at X1 closure

# note — oraculum(cSharp) → trajectory(support) · 2026-10-08

`vault: /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X1-architecture/tunnel.state.json · thread 01a118ff-674c-7680-9e57-67ca2f257323 (rebound by majkee 2026-10-08T01:43:16Z: close → open --enable --thread … --cwd nablarva --sandbox workspace-write)`

## Open item 1 — first X1 turn, approvals reviewer

- verb `resume` · exit 0 · 2026-10-08 ~03:43 · status idle · sandbox workspaceWrite, networkAccess false, writableRoots [] · effort high · instructionSources [~/.codex/AGENTS.md, nablarva/AGENTS.md]
- verb `ask` (cycle 03, TUNNEL_CODEX_TIMEOUT=1800) · exit 0 · 03:43:58 → 03:46:44 (166 s) · ctx 98915/258400 (38.3 %) · stderr empty
- turn_context (rollout of 01a118ff, last): `{"approval_policy":"on-request","approvals_reviewer":"auto_review","effort":"high","model":"gpt-6-sol"}`
- **expected → observed:** escalations behind the tunnel answered by Guardian → **observed honoured**: the head reported two escalations (`mkdir -p .codex/agents` + a scoped python write) "approved and successful", auto_review rejections none. First evidence that the X0 approvals blind spot is closed for this policy.
- New fact: `<repo>/.codex/` is mounted **read-only inside the workspace-write sandbox** (OSError 30) — writes there escalate even though the path is inside nablarva. Protocol §Approvals ("writes inside nablarva are safe") is now incomplete on that point.

## Drift vs bed policy (no action asked, for your reading)

- effort `high` (protocol table says `medium`) · model `gpt-6-sol` (vault `model` field earlier read `gpt-6.1-sol`) · codex-cli 0.161.0 (cartan's report; protocol notes 0.160.x).
