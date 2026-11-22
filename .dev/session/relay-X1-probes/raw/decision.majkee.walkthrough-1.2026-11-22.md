---
kind: operator decisions, verbatim with confirmed summaries under R1 where applicable
from: majkee, typed in the exec session (codex 01a1fefc-0356-7ea1-860c-783a66a91211)
recorded_by: exec
date: 2026-11-22
scope: relay-X1-probes, cycle 02 read-back and six release lines, S0–S7
---

## S0 — The plan before any releases

asked: **Is this the plan as you understand it, or is something different?**

majkee:
> Yes, we should go through some decission loop, lets strart.

status: decided

## S1 — Start and close `sample-codex`

asked: **Release the sample start and close with A, with B, with other values you name, or leave it unreleased?**

asked, follow-up: **Which setup should we record?**

Context presented: A uses `gpt-6.1-terra` with the current sandbox and approval defaults and no explicit sandbox or approval flags. Majkee starts and closes the sample and handles any trust dialog.

majkee:
> I''l pick A, usualy have full permission mode, but that will not happen each time, so catch variable is not error here but part of observations.

status: decided

## S2 — Who enters the receipt instruction?

asked: **Should the instruction go in by your hand, by the desk’s hand under a separate exception, or be left out?**

majkee:
> of course i'll provide, but `exec`, would need probably new tmux window, you may prepare via some `subagent, set on model luna` after whole decission loop.

status: decided

## S3 — What the auditor can see and keep

asked: **Approve the auditor’s access and private evidence storage as described, or change the scope?**

Context presented: Menu line 6 covers the sample pane, tmux metadata, the sample session record and receipts. The auditor records independently and keeps the captures and receipts in private host-local custody. The repository gets the result rows.

majkee:
> of course, that is one of `why` we have auditor, not because burecracy.

status: decided

## S4 — Observation A, one send by queue

asked: **Release observation A for one attempt?**

Context presented: Menu line 4 is one scoped `codex queue` call from the Claude lead to `sample-codex`, without `--resume`, with a fresh nonce and independent observation. If A ends UNCERTAIN, B is skipped.

majkee:
> yes

status: decided

## S5 — Observation B, one tmux paste and submit

asked: **Do you release observation B as one explicit exception to L4 for this one measurement?**

Context presented: Menu line 5 is one Claude lead to disposable Codex paste and separate submit, witnessed by the auditor, with a fresh nonce and the agreed stop conditions.

majkee:
> yes, if not closing any path.

asked, follow-up: **Is that what you meant by “not closing any path”?**

majkee:
> ok.

confirmed summary: Release B as a single L4 exception. Current manual fallback and future research options remain available under their existing rules. The agreed stop conditions apply, including skipping B if A ends UNCERTAIN.

status: decided

## S6 — Keep the sample’s session record through the gate

asked: **Keep the session record through the gate and decide whether to delete it then?**

majkee:
> of course

majkee, follow-up:
> home

status: decided

## S7 — Final read-back

asked: **Is this what you released, or is anything different?**

asked, follow-up: Before we prepare the window, **do you confirm the six releases in the S7 read-back?**

Context presented: The desk read back lines 2, 3, 6, 4, 5 and 7 as selected, none declined. Majkee starts and closes the sample, uses configuration A, handles any trust prompt and enters the receipt instruction. The auditor independently observes and holds the evidence on home. A and B are one attempt each, with B subject to the one-time L4 exception and the uncertainty stop. The sample record stays on home through the gate.

majkee:
> Ok, instead Luna, i'll make this session fork, with that fork set on luna|terra i will go throught, fork will say what I have to put to terminal and why. I need little bit lesson, than we can made even document helper for me. OK? But as remember `auditor` want to be witnes or who has|hold knowledge about what how would be tested?

asked, preparation follow-up: **Should your fork walk you through creating the scratch folder and tmux window too, or should I prepare those so the lesson starts with attaching to the window?**

majkee:
> yes please, as tutor

status: decided
