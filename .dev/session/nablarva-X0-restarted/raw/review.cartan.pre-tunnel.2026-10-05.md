# Cartan — pre-tunnel review and handover

`2026-10-05 · office hruzam-120922 · HEAD ce6063016b782bfec88a2bb2cca666ade2e27a64`
`Source: direct user request after blessing RUNBOOK; this is a review receipt, not STATUS or a new BUS cycle.`

## Verdict

Ownership is settled: Oraculum owns STATUS; Cartan coordinates design. Majkee's explicit
RUNBOOK blessing supersedes the historical DRAFT HOLD in RETURN 06. Trajectory's added
mute transport-support role is consistent with the design/transport separation.

The RUNBOOK still contains executable leftovers: prompt-0 says Cartan owns STATUS;
prompt-2 tells Cartan to rewrite it; Fixed facts refers to an active transcription
exception. Prompt-2 also repeats the consumed round-1 task. The
[exact patch](patch.cartan.runbook-pre-tunnel.2026-10-05.diff) reconciles those lines,
the gavel attribution and the protocol pin, without changing the gate or participants.
It is **prepared, not applied**: Oraculum owns this launcher and its STATUS.

Patch base RUNBOOK blob: `a25836c8257477ea645b5ebf83cef8f2b74bd4fc`.
Patch SHA-256: `b4063479394dbd79abf32cbca040e5ac82f90dc40de67257b8f4120eaba8c4a2`.
Oraculum can check it with `git apply --check` before applying; if the base changed,
reconcile the six intended corrections rather than overwrite another edit.

STATUS also needs Oraculum's refresh: it still says the RUNBOOK is unseen/uncommitted,
uses interim R2 hashes, and says to create the already-present POINT 07. POINT 07 needs
current source pins before Atlas reviews. Preserve the earlier RETURN/diff as historical
evidence at HEAD; the ownership question is no longer pending. This receipt does not
claim that Oraculum has applied these corrections or that the trial gate is accepted.

## Current sources to carry

| Artifact | Git blob |
|---|---|
| `_provisional/coordination.2026-10-05.md` | `c9725baab1d55c64956fadcee36fc9df581aeedd` |
| `raw/brief.cartan.houston-mediation.2026-10-05.md` | `78ff72d45f4333c1c8aa687346d9a41afb1dbf45` |
| [Compact Houston design](brief.cartan.houston-design.2026-10-05.md) | `84e7c32f4dcb96937b7e0961f138c1aa6419c163` |

R3 changes ownership/continuation wording and makes the candidate file layout concrete;
it does not claim Atlas has accepted the design. The older RETURN 06/delta remain unchanged.

## Model and context recommendation

Local user configuration declares `gpt-6-astra` with effort `max`; that is a configured
default, not a fresh report of this thread. For routine coordination I recommend Sol at
medium, raising effort for a difficult design decision. Prefer GPT-6.1 Sol if offered
in `/model`; the older GPT-6 Sol is also a reasonable bounded-work option. This is a
workload recommendation, not a measured latency guarantee. Official [Sol documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
describes its capability and supported effort choices.

Use `/compact` in the current TUI after reading this packet. It summarizes prior context;
I have prepared the durable input but have not run compaction or changed your model.
Keep the same thread and use the re-entry paragraph in the compact design. Short POINTs,
one outcome per turn and bounded evidence reads reduce avoidable work; compaction cannot
guarantee a sub-ten-minute answer. [Official CLI commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli).

## Unattended shell work inside this project

Recommended effective policy: workspace-write rooted at this Nablarva repository,
approval_policy=never. It suppresses prompts while retaining the workspace boundary;
out-of-scope operations fail instead of waiting for an invisible approval. Existing
rules/managed restrictions may still constrain commands. This is not blanket shell or
whole-home authority. [Official sandbox settings](https://learn.chatgpt.com/docs/sandboxing).

The installed CLI 0.160.0 `resume --help` confirms the following flags. To set them on
this existing thread, first note its exact ID using `/status`, exit the current TUI,
then resume **that ID** from an operator terminal (replace `THREAD_ID`):

```sh
codex resume THREAD_ID \
  -C /home/hruzam/unikuklatrix/nablarva \
  -m gpt-6.1-sol -c 'model_reasoning_effort="medium"' \
  --sandbox workspace-write --ask-for-approval never
```

If that Sol model is unavailable, select the offered Sol through `/model`. Confirm the
model/effort and permissions in the TUI; run `/compact` there if not already done. Exit
the TUI before Oraculum's tunnel resume. No permanent global/project configuration was
changed by Cartan. I cannot widen the currently running tool sandbox from within a turn.

After the operator-established binding, Oraculum must inspect the `runtime` block in
the one appointed vault after `tun resume`: exact thread, Nablarva cwd, model/effort,
workspaceWrite sandbox and approvalPolicy never. A bind's top-level `--sandbox` intent
does not change an existing thread. If runtime differs, Trajectory investigates while
write dispatch waits; do not treat the proposed command as a runtime proof.

Source checked: `/home/hruzam/ia-sync/zsh/ai/tunnel-codex.py`, `thread_start` sets never;
`thread_resume` sends only threadId; `_auto_decline` rejects requests it cannot display.
The [local handover guide](/home/hruzam/reposoma/raw.guides/tunnel/res/user-run.md)
agrees. No tunnel verb was run in this review.

The personal journal and global ia-sync sources are outside this project sandbox.
Carry a ready journal addition to an authorized writer if unattended; broaden exact
writable roots only when that scope is deliberately assigned. No broad shell-prefix
allow rule is necessary for normal in-project work.

## Verification and compact continuity

Patch applicability, unchanged gate/participants, YAML, local links and candidate pins
are checked before release. The compact design's proposed package remains absent.
RUNBOOK, STATUS, POINT 07, gitignore, runtime config and live bindings were not edited.
The next action remains in STATUS and must be refreshed by Oraculum; this note supplies
its evidence and corrections. The user still controls when the TUI releases to tunnel.
