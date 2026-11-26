---
kind: facts read from tmux's public repository — a child's fetch of six primary pages, ordered by the lead
by: lead (flight · claude 689d87d0) · written 2026-11-26T04:19:15Z · pages read 2026-11-26
status: one fetch through a summarising reader, not raw bytes; unchecked by a second seat. It settles a disagreement between the lead's refresh pass and the auditor's table (cycle 05) in the auditor's favour.
---

Pages: `api.github.com/repos/tmux/tmux` — `/releases/latest`, `/releases?per_page=6`, `/commits/434ab3a2…`,
`/commits/9e5702fb…`, `/compare/3.8...434ab3a2…` — and `raw.githubusercontent.com/tmux/tmux/master/CHANGES`.

| Fact | As the page gives it |
|---|---|
| Newest release | `3.8`, published 2026-09-09T12:55:58Z, not a prerelease |
| The release before | `3.7c`, published 2026-08-17 — the version installed on this host |
| Commit 434ab3a | 2026-11-12 · "Minimal support for OSC 7501 program status, GitHub issue 5830 from Brian Cosgrove." · touches format.c, input.c, tmux.1 and six more · new format variables `pane_program_state`, `pane_program_name`, `pane_program_message` |
| Commit 9e5702f | 2026-11-23 · "Forward active pane OSC 7501 status, GitHub issue 5907 from Brian Cosgrove." · adds a terminal feature `programstatus`; tmux.1: "Supports the OSC 7501 program status extension." |
| Are the commits in 3.8? | No. The compare of 3.8 with 434ab3a reports "diverged"; no release after 3.8 is listed; the top section of CHANGES ("CHANGES FROM 3.7c TO 3.8") has no entry for 7501. |

What this corrects: the refresh pass (`research.wheel-and-harness.refresh.epoch.2026-11-26.md`, point 1) called 3.8
"unreleased as far as I can tell" and found nothing on 7501 in tmux — it read the change list, where the two commits
are not yet entered. The auditor's table (row "Program Status Protocol") had both commits and the release date right.

What it does not show: when a release will carry the commits; what `pane_program_state` holds for a real Claude
Code, Codex or Antigravity session; whether those programs emit the sequence when tmux 3.7c answers their query.
