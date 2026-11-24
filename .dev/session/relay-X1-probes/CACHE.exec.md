---
kind: exec desk working note — approval observation and proposed test-plan change
by: exec(codex)|astrobley
date: 2026-11-23
scope: Context for Flight to consider when revising the released probe plan. Noncanonical; RUNBOOK and STATUS remain authoritative.
---

# Approval mode observation

## What is currently released

The S7 decision record releases one disposable `sample-codex`, started by Majkee with the current Codex defaults, plus two one-shot Claude → Codex delivery probes into that same sample: A by `codex queue`, B by tmux paste and separate Enter. Flight sends. The auditor independently observes the sample and checks its turn and nonce receipt. B is one explicit L4 exception, subject to the agreed stops. The sample's Codex session record remains on `home` through the gate.

The current choice was intended to expose the actual permission behavior as an observation. The user later identified the `/permissions` choice shown as “Ask for approval” / “Approve for me” and asked whether it can be set at startup. The sample has not yet been reported as started, so its actual mode is not established here.

## Saved CLI help and interpretation

The saved help is for codex-cli 0.171.0 (`raw/help.codex-0.171.0.2026-11-22.txt`). It lists sandbox modes `read-only`, `workspace-write`, and `danger-full-access`; approval policies `on-request` and `never`; and `--approve-for-me`, described as routing approval requests through automatic review using the `workspace-write` sandbox.

The desk inferred that UI “Ask for approval” corresponds to `-s workspace-write -a on-request`. The saved help does not state that UI-to-CLI mapping, so treat it as an inference pending a live, version-matched check. Do not equate “Approve for me” with a human approval prompt. It routes requests through automatic review per the saved help.

## Proposed comparison, not yet released

The proposed comparison pair is:

1. **Current defaults** — the S1 setup already released. Record the actual sandbox and approval behavior shown by the sample; do not assume it from the invoking session.
2. **“Ask for approval”** — the UI choice Majkee pointed out, described as workspace reads/edits and command execution with approval required for internet access or workspace edits. The tentative CLI equivalent is `-s workspace-write -a on-request`; this UI-to-CLI mapping is not verified by the saved help and must be checked against the live CLI before use. Do not substitute `--approve-for-me`: that routes approval requests through automatic review.

If Majkee wants to compare these two setups, preserve the two delivery methods as the other factor: queue and tmux paste/submit under each setup. That is four one-shot observations across two separately configured disposable Codex samples. Keep sender, model, receiver instruction, observation window, nonce method, and evidence handling consistent where possible. Record each sample's actual startup configuration and every approval event or absence of one. This comparison remains proposed, not released.

Before any run, Flight should define which safe, in-scope action is expected to request approval, how the auditor can observe the request and disposition, and how a prompt affects the receipt result. The current NONCE instruction writes a receipt inside the sample workspace; whether that triggers an approval depends on the selected mode and actual policy. Do not invent an unsafe action solely to force a prompt. A denied or unresolved operation remains evidence and follows the stop rules.

## Ownership and next edge

The released RUNBOOK currently describes one sample under one setup and two delivery probes. A two-mode comparison changes the plan and needs Flight to revise the RUNBOOK and its release/read-back surface before additional sessions or sends. The auditor remains the independent observer. The exec desk can teach Majkee the terminal preparation one step at a time, while Majkee types the commands. No sample, hook, recorder, or additional probe was started or configured for this note.

Useful source paths:
- `RUNBOOK.md` — released probe plan
- `STATUS.md` — current releases and session state
- `raw/decision.majkee.walkthrough-1.2026-11-22.md` — S1–S7 decisions
- `raw/sheet.readback-1.2026-11-22.md` — approval choices, probe steps, and stop conditions
- `raw/help.codex-0.171.0.2026-11-22.txt` — saved CLI help
