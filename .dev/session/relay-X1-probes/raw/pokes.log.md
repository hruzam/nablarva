---
kind: poke log of relay-X1-probes — every coordination poke, with what it proves and what it does not
by: lead · started 2026-11-22
rule: one entry per poke. UTC before and after, the exact line, the exit code, what was looked at first, what it proves. Queued is not read. A probe try of the handoff is not a poke and is not logged here.
pattern: /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/raw/pokes.log.md
---

# Pokes

## p01 — lead → oraculum · `codex queue`
- file first: `_bus/01.lead.point.md`, committed in 3ae987c
- looked first (2026-11-22T05:48:48Z): pane %60 — codex in the foreground, not dead, input row empty (placeholder only), no dialog; footer thread id 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1, idle
- call: `codex queue --thread 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1 --message "<line>"`, without `--resume`
- line: `[poke p01] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/01.lead.point.md — opposing read of the read-back sheet; return by file, no bell`
- before: 2026-11-22T05:48:59Z · after: 2026-11-22T05:49:00Z · exit code: 0
- output (first line): `Queued message 01a201cc-f95b-7d32-9dcb-d57fa794d1ba for thread 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1.`
- proves: the queue accepted the call, if the exit code is 0. It does not prove that the line was read.
- read is shown by: `_bus/01.oraculum.return.md`, or by work in pane %60

- p01 outcome: read — her RETURN was on disk by 2026-11-22T05:50:07Z (file time 05:49Z); REVISE, eight points; checked in `_bus/01.lead.verdict.md`.

## p02 — lead → exec · `codex queue`
- looked first (2026-11-22T05:54:53Z): pane %68 — codex in the foreground, not dead, input row empty (placeholder only), no dialog; footer thread id as in the roster; idle. File first: `_bus/02.lead.point.md`, committed in d49da40. Read is shown by `_bus/02.exec.return.md` or by work in the pane.
- call: `codex queue --thread 01a1fefc-0356-7ea1-860c-783a66a91211 --message "<line>"`, without `--resume`
- line: `[poke p02] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/02.lead.point.md — a walkthrough for Majkee: the read-back and six release lines; follow its return and bell instructions`
- before: 2026-11-22T05:55:06Z · after: 2026-11-22T05:55:06Z · exit code: 0
- output (first line): `Queued message 01a201d2-91dc-7d52-92ac-500eb1e7ac9d for thread 01a1fefc-0356-7ea1-860c-783a66a91211.`
- proves: the queue accepted the call, if the exit code is 0. It does not prove that the line was read.

## p03 — lead → controller · `codex queue`
- looked first (2026-11-22T05:54:53Z): pane %59 — codex in the foreground, not dead, input row empty (placeholder only), no dialog; footer thread id as in the roster; idle. No POINT: the duty is prompt-1 of the RUNBOOK and Majkee's push decision of 2026-11-22. Done is shown by origin/core = d49da40.
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke p03] push duty — prompt-1 in /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/RUNBOOK.md: nablarva core — fetch; only if ahead and not behind, one plain git push; never rebase, never force; write no file, type into no pane; I verify the remote ref`
- before: 2026-11-22T05:55:06Z · after: 2026-11-22T05:55:07Z · exit code: 0
- output (first line): `Queued message 01a201d2-92be-7b92-9467-e0ff2d51db28 for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`
- proves: the queue accepted the call, if the exit code is 0. It does not prove that the line was read.

- p03 outcome: done — `git ls-remote origin refs/heads/core` = `d49da40` at 2026-11-22T05:55:40Z, equal to local HEAD; checked by the lead.

- p02 outcome: read — the desk ran one turn from the queue, ended 2026-11-22T05:55:26Z, and put theme S0 to Majkee. Seen by the lead at 2026-11-22T06:54Z in the desk's own session record (entry types, times and the desk's last message only; nothing of Majkee's read). At that time: no record file, no RETURN, no answer. The first watch on the RETURN path ended empty at 06:53:38Z after 58 minutes; nothing was sent again. The desk's pane showed Codex's selection hint row at 06:53Z, so its newest text may be off screen in that window until a key is pressed there by Majkee's hand; the lead did not touch the pane.

## p04 — lead → myShell · look-first paste (a Claude pane)
- authority: Majkee, typed in the lead session shortly before 13:38Z — "you may poke `myShell` for that" (raw/decision.majkee.cache-and-commits.2026-11-22.md, second part)
- file first: `_bus/03.lead.point.md`
- looked first (2026-11-22T13:39:13Z): pane %61 — claude in the foreground, not dead, not in a tmux mode, no dialog. The input row showed words, all of them dim in the styled capture, with the cursor at the start of the row (`cursor_x` 2): a suggestion, not text. Only the bottom rows of the pane were read; nothing of them is kept.
- staged: `tmux set-buffer -b p04 '<line>'`, then `tmux paste-buffer -p -b p04 -t %61` — 2026-11-22T13:39:28Z, both exit code 0
- line: `[poke p04] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/03.lead.point.md — from the lead of relay-X1-probes, on Majkee's word: three questions about orphans and CACHE.md; return by file`
- looked again: the line sat on the input row as plain text, on two rows, `cursor_x` 95, nothing else on the row
- submit: `tmux send-keys -t %61 Enter` — 2026-11-22T13:39:41Z, exit code 0
- looked once more (13:39:46Z): the input row was empty, the line stood above it as a submitted prompt, and the pane showed a working turn
- proves: the line was submitted and a turn started. It does not prove that the POINT was read to the end.
- read is shown by: `_bus/03.myshell.return.md`

- p04 outcome: read — her RETURN was on disk by 2026-11-22T13:40:42Z; checked in `_bus/03.lead.verdict.md`. Her reply bell `[bell r03]` arrived in pane %70 afterwards, submitted.

## p05 — lead → controller · `codex queue`
- looked first (2026-11-22T13:44:31Z): pane %59 — codex in the foreground, not dead, input row empty (placeholder only, cursor at the start), no dialog; footer thread id as in the roster; idle. No POINT: the duty is prompt-1 of the RUNBOOK. Done is shown by origin/core = `59878f9`.
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke p05] push duty — prompt-1 in /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/RUNBOOK.md: nablarva core — fetch; only if ahead and not behind, one plain git push; never rebase, never force; write no file, type into no pane; I verify the remote ref`
- before: 2026-11-22T13:44:41Z · after: 2026-11-22T13:44:41Z · exit code: 0
- output (first line): `Queued message 01a20380-7c50-70b3-855a-6544be1efd8a for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`
- proves: the queue accepted the call. It does not prove that the line was read.

- p05 outcome: done — `git ls-remote origin refs/heads/core` = `59878f9` at 2026-11-22T13:45:06Z, equal to local HEAD; checked by the lead.

## p06 — lead → oraculum · `codex queue`
- authority: Majkee names her as the countersignature (raw/decision.majkee.countersignature.2026-11-22.md)
- file first: `_bus/04.lead.point.md`, committed in ce3807c
- looked first (2026-11-22T13:46:52Z): pane %60 — codex in the foreground, not dead, input row empty (placeholder only, cursor at the start), no dialog; footer thread id 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1. The pane showed the text-selection hint of Codex and a warning marker; the queue door does not type into the pane.
- call: `codex queue --thread 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1 --message "<line>"`, without `--resume`
- line: `[poke p06] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/04.lead.point.md — the countersignature, on Majkee's word: oppose the handoff's unread additions and sheet draft 2; return by file, no bell`
- before: 2026-11-22T13:46:52Z · after: 2026-11-22T13:46:52Z · exit code: 0
- output (first line): `Queued message 01a20382-7ad8-7853-9b8d-7bbfbb36e06a for thread 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1.`
- proves: the queue accepted the call. It does not prove that the line was read.
- read is shown by: `_bus/04.oraculum.return.md`, or by work in pane %60

- p06 outcome: read — her RETURN was on disk by 2026-11-22T13:48:45Z; REVISE, two points; checked in `_bus/04.lead.verdict.md`. Her footer went from 50% to 39% of context left over that cycle.

## p07 — lead → oraculum · `codex queue`
- file first: `_bus/05.lead.point.md`, committed in b533679
- looked first (2026-11-22T13:54:27Z): pane %60 — codex in the foreground, not dead, input row empty (placeholder only, cursor at the start), no dialog; footer thread id 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1; idle, 39% of context left; a warning marker in the footer row.
- call: `codex queue --thread 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1 --message "<line>"`, without `--resume`
- line: `[poke p07] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/05.lead.point.md — your REVISE is taken; sign sheet draft 3 or send it back; return by file and one reply bell`
- before: 2026-11-22T13:54:27Z · after: 2026-11-22T13:54:28Z · exit code: 0
- output (first line): `Queued message 01a20389-6e99-7b32-82a1-9e7fb56cdf6e for thread 01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1.`
- proves: the queue accepted the call. It does not prove that the line was read.
- read is shown by: `_bus/05.oraculum.return.md`, by her reply bell `[bell r05]` in pane %70, or by work in pane %60

- p07 outcome: read — her RETURN was on disk by 2026-11-22T13:55:41Z; COUNTERSIGNED; checked in `_bus/05.lead.verdict.md`. No bell: withheld under a limit of her own seat, said in her field 6; the watch picked the file up.

## p08 — lead → exec · `codex queue`
- file first: `_bus/02.lead.note-1.md`, committed in 21df208
- looked first (2026-11-22T13:56:51Z): pane %68 — codex in the foreground, not dead, input row empty (placeholder only), no dialog; footer thread id 01a1fefc-0356-7ea1-860c-783a66a91211, 62% of context left. The pane still showed the selection hint row of Codex; the queue door does not type into the pane, and p02 was read through the same state.
- call: `codex queue --thread 01a1fefc-0356-7ea1-860c-783a66a91211 --message "<line>"`, without `--resume`
- line: `[poke p08] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/02.lead.note-1.md — the sheet is now draft 3, countersigned; S0 stands as you asked it; end your turn with the S0 question`
- before: 2026-11-22T13:56:51Z · after: 2026-11-22T13:56:51Z · exit code: 0
- output (first line): `Queued message 01a2038b-a038-7263-8a47-dfe758dd02bb for thread 01a1fefc-0356-7ea1-860c-783a66a91211.`
- proves: the queue accepted the call. It does not prove that the line was read.
- read is shown by: a new turn in the desk's session record after 13:56:51Z; no RETURN is asked for this note

## p09 — lead → controller · `codex queue`
- looked first (2026-11-22T13:56:51Z): pane %59 — codex in the foreground, not dead, input row empty (cursor at the start), no dialog; footer thread id as in the roster. No POINT: the duty is prompt-1 of the RUNBOOK. Done is shown by origin/core = `21df208`.
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke p09] push duty — prompt-1 in /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/RUNBOOK.md: nablarva core — fetch; only if ahead and not behind, one plain git push; never rebase, never force; write no file, type into no pane; I verify the remote ref`
- before: 2026-11-22T13:56:51Z · after: 2026-11-22T13:56:52Z · exit code: 0
- output (first line): `Queued message 01a2038b-a10e-7b61-b630-f75a48e63eb1 for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`
- proves: the queue accepted the call. It does not prove that the line was read.

- p08 outcome: read — the desk ran one turn that ended 2026-11-22T13:57:07Z; its closing lines say it picked up p08 and repeat the S0 question to Majkee. Seen by the lead in the desk's own session record (entry types, times and the end of the desk's last message only).
- p09 outcome: done — `git ls-remote origin refs/heads/core` = `21df208` at 2026-11-22T13:57:11Z, equal to local HEAD; checked by the lead.

## p10 — lead → exec · `codex queue`
- authority: Majkee, typed in the lead session shortly before 14:04Z — "please poke `exec`" (raw/decision.majkee.seats-and-notice.2026-11-22.md, fifth part)
- file first: none new — the line points at the running `_bus/02.lead.point.md`
- looked first (2026-11-22T14:04:33Z): pane %68 — codex in the foreground, not dead, input row empty (placeholder only), no dialog. The transcript region still showed the desk's reply of 05:15Z as its last text and the selection hint row of Codex below the footer, although the desk's session record held two later turns (05:55Z, 13:57Z): the view was pinned by an old text selection, so Majkee at that window saw none of them.
- call: `codex queue --thread 01a1fefc-0356-7ea1-860c-783a66a91211 --message "<line>"`, without `--resume`
- line: `[poke p10] Majkee is at your window now for the walkthrough of /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/02.lead.point.md (sheet draft 3). Your screen there is pinned by an old text selection, so he may not see your last turns: put the S0 question to him again as the last line of this turn, then go on theme by theme as he answers`
- before: 2026-11-22T14:05:25Z · after: 2026-11-22T14:05:25Z · exit code: 0
- output (first line): `Queued message 01a20393-77ea-7e72-9874-5d9420a09270 for thread 01a1fefc-0356-7ea1-860c-783a66a91211.`
- proves: the queue accepted the call.

- p10 outcome: read and shown — the desk's turn ended 2026-11-22T14:05:29Z; the pane then showed the S0 question as its last line and the ordinary footer row, the selection hint gone. Whether a key of Majkee's or the new turn released the view is not known. The lead typed nothing into the pane.
- observation for the stage (not a probe result): a queued message can run a whole turn in a Codex main that its own window does not show, while a text selection pins the view. "The seat was poked and answered" and "the human at that window saw it" are two facts.

## p11 — lead → controller · `codex queue`
- looked first (2026-11-22T14:41:37Z): pane %59 — codex in the foreground, not dead, input row empty (cursor at the start), no dialog; footer thread id as in the roster. No POINT: the duty is prompt-1 of the RUNBOOK. Done is shown by origin/core = `22d3906`.
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke p11] push duty — prompt-1 in /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/RUNBOOK.md: nablarva core — fetch; only if ahead and not behind, one plain git push; never rebase, never force; write no file, type into no pane; I verify the remote ref. The stack carries one commit of the engineer session (824dfe9, two eSharp files) beside the lead's`
- before: 2026-11-22T14:41:37Z · after: 2026-11-22T14:41:37Z · exit code: 0
- output (first line): `Queued message 01a203b4-9c51-7c12-b18d-e256f24b2777 for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`
- proves: the queue accepted the call.

- p11 outcome: done — `git ls-remote origin refs/heads/core` = `22d3906` at 2026-11-22T14:41:59Z, equal to local HEAD; checked by the lead. The push carried the engineer session's commit 824dfe9, on the note n03 she left in pane %70 at about 14:40Z.

- bell r02 (exec → lead): arrived in pane %70 at about 2026-11-22T21:42Z, after the lead's file watch had picked up `_bus/02.exec.return.md` at 21:42:15Z. A seat's hint; the RETURN and the record were read from the files.
- pre-return look (no poke): at 2026-11-22T15:52:00Z a timed look at the bottom rows of the desk's pane %68 showed the S1 question as its last line, so no poke was sent. Nothing of the look is kept but that.

## p12 — lead → controller · `codex queue`
- looked first (2026-11-22T21:50:38Z): pane %59 — codex in the foreground, not dead, input row empty (placeholder only), no dialog. No POINT: the duty is prompt-1 of the RUNBOOK. Done is shown by origin/core = `a5275ed`.
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke p12] push duty — prompt-1 in /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/RUNBOOK.md: nablarva core — fetch; only if ahead and not behind, one plain git push; never rebase, never force; write no file, type into no pane; I verify the remote ref. The stack carries two commits of the engineer session (c22c060, 37f5e79, eSharp files) beside three of the lead`
- before: 2026-11-22T21:50:47Z · after: 2026-11-22T21:50:48Z · exit code: 0
- output (first line): `Queued message 01a2053d-876b-7d71-b3a3-35cda382be49 for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`
- proves: the queue accepted the call.

- p12 outcome: done — `git ls-remote origin refs/heads/core` = `a5275ed` at 2026-11-22T21:51:13Z, equal to local HEAD; checked by the lead. The push carried c572881, c22c060, 37f5e79, b3f33fc and a5275ed.

## p13 — lead → auditor · `codex queue`
- authority: line 6 of the release menu, given by Majkee on 2026-11-22 (raw/decision.majkee.walkthrough-1.2026-11-22.md, S3); the sample is up by his word of 2026-11-23 (raw/decision.majkee.sample-up.2026-11-23.md)
- file first: `_bus/06.lead.point.md` (committed in a5275ed)
- looked first (2026-11-23T11:16:14Z and again at 11:16:50Z): pane %66 — codex in the foreground, not dead, input row empty (placeholder only), no dialog; footer thread id as in the roster; 77% of context left
- call: `codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<line>"`, without `--resume`
- line: `[poke p13] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/06.lead.point.md — you are released as observer; the sample is up: private folder, first look, a 60-second dry watch; RETURN and one bell`
- before: 2026-11-23T11:16:52Z · after: 2026-11-23T11:16:53Z · exit code: 0
- output (first line): `Queued message 01a2081f-857b-7200-b0b0-c36119fbb268 for thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7.`
- proves: the queue accepted the call. Read is shown by `_bus/06.auditor.return.md`.

- p13 outcome: read and answered — `_bus/06.auditor.return.md` was picked up by the lead's file watch at 2026-11-23T11:19:04Z; the reply bell r06 arrived in pane %70 some minutes later. Checked in `_bus/06.lead.verdict.md`.

## p14 — lead → auditor · `codex queue`
- authority: lines 4 and 6 of the release menu (raw/decision.majkee.walkthrough-1.2026-11-22.md, S4, S3); Majkee's go-ahead in the lead session shortly before 11:24:50Z (raw/decision.majkee.sample-up.2026-11-23.md, second part)
- file first: `_bus/07.lead.point.md` (committed in 047f4f7)
- looked first (2026-11-23T11:24:50Z): pane %66 — codex in the foreground, not dead, input row empty (placeholder only), no dialog
- call: `codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<line>"`, without `--resume`
- line: `[poke p14] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/07.lead.point.md — observation A: second look, then start the watch and write the marker; I call within two minutes of your marker`
- before: 2026-11-23T11:24:50Z · after: 2026-11-23T11:24:50Z · exit code: 0
- output (first line): `Queued message 01a20826-cefd-70a0-b956-9eafba2ddfb7 for thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7.`
- proves: the queue accepted the call. Read is shown by the marker `_bus/07.auditor.ready.md`, written 56 seconds later.

- not a poke — **observation A, the one released try**: made at 2026-11-23T11:25:48.953Z; its record is `_bus/07.lead.try.md`, not this log.

- p14 outcome: read and answered — marker `_bus/07.auditor.ready.md` at 2026-11-23T11:25:46Z; `_bus/07.auditor.return.md` picked up by the lead's file watch at 11:36:07Z; reply bell r07 arrived in pane %70 about a minute later. Checked in `_bus/07.lead.verdict.md`.

## p15 — lead → auditor · `codex queue`
- authority: lines 5 and 6 of the release menu (raw/decision.majkee.walkthrough-1.2026-11-22.md, S5, S3); A not UNCERTAIN (_bus/07.lead.verdict.md)
- file first: `_bus/08.lead.point.md` (committed in b684179)
- looked first (2026-11-23T11:40:34Z): pane %66 — codex in the foreground, not dead, input row empty (placeholder only), no dialog
- call: `codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<line>"`, without `--resume`
- line: `[poke p15] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/08.lead.point.md — observation B: preflight, then start the one-second watch and write the marker; I paste within two minutes of your marker`
- before: 2026-11-23T11:40:34Z · after: 2026-11-23T11:40:34Z · exit code: 0
- output (first line): `Queued message 01a20835-36c8-7f01-a85b-a00affc2a275 for thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7.`
- proves: the queue accepted the call. Read is shown by the marker `_bus/08.auditor.ready.md`, written 75 seconds later.

- not a poke — **observation B, the one released exception to L4**: paste at 2026-11-23T11:42:11.668Z, Enter at 11:42:29.659Z, into the sample's pane %72 and nowhere else; its record is `_bus/08.lead.try.md`, not this log.

- p15 outcome: read and answered — marker `_bus/08.auditor.ready.md` at 2026-11-23T11:41:49Z; `_bus/08.auditor.return.md` picked up by the lead's file watch at 11:52:21Z; reply bell r08 arrived in pane %70 shortly after. Checked in `_bus/08.lead.verdict.md`.

## p16 — auditor → lead · look-first tmux pointer

- File first: `raw/request.auditor.tracker-approval.2026-11-23.md`, on Majkee's direct request after VERDICTs 07 and 08 confirmed both planned observations.
- Looked first: pane %70, `claude`, live, empty input at cursor column 2, no visible dialog.
- Line: `[poke p16] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/raw/request.auditor.tracker-approval.2026-11-23.md — Majkee asks for one tracker approval test`
- Paste: 2026-11-23T11:55:51.909Z–11:55:51.922Z, exit 0. Verified the exact wrapped line before Enter.
- Enter: 2026-11-23T11:56:15.967Z–11:56:15.974Z, exit 0. At 11:56:21.038Z the input had cleared and showed a working indicator. This establishes submission, with reading and action still to be confirmed.

## p16 — lead → controller · `codex queue`
- looked first (2026-11-23T11:55:17Z): pane %59 — codex in the foreground, not dead, input row empty (placeholder only), no dialog. No POINT: the duty is prompt-1 of the RUNBOOK. Done is shown by origin/core = `7b42fb2`.
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke p16] push duty — prompt-1 in /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/RUNBOOK.md: nablarva core — fetch; only if ahead and not behind, one plain git push; never rebase, never force; write no file, type into no pane; I verify the remote ref`
- before: 2026-11-23T11:55:17Z · after: 2026-11-23T11:55:17Z · exit code: 0
- output (first line): `Queued message 01a20842-adc9-7bd2-88e3-25296250ef87 for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`
- proves: the queue accepted the call.

- p16 outcome: done — `git ls-remote origin refs/heads/core` = `7b42fb2` at 2026-11-23T11:55:38Z, equal to local HEAD; checked by the lead. Eleven commits, all the lead's.

- incoming, not the lead's poke — **a note from the auditor**, pasted into pane %70 at about 2026-11-23T11:56Z and labelled by it `[poke p16]` (the same number as the lead's push poke above; the numbers of this log are the lead's): it points at `raw/request.auditor.tracker-approval.2026-11-23.md` — Majkee, through the auditor, asks for one approval-dialog side test in the sample for his tracker. A seat's relay, not his word in this session.

## p17 — lead → auditor · `codex queue`
- file first: `raw/reply.lead.tracker-approval.2026-11-23.md` — no seat sends anything into the sample; both released tries are spent; Majkee may type the line himself; no RETURN asked
- looked first (2026-11-23T11:57:02Z): pane %66 — codex in the foreground, not dead, input row empty (placeholder only), no dialog
- call: `codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<line>"`, without `--resume`
- line: `[poke p17] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/raw/reply.lead.tracker-approval.2026-11-23.md — reply to your tracker request: no seat sends; Majkee types it himself and tells you when; no RETURN needed`
- before: 2026-11-23T11:57:02Z · after: 2026-11-23T11:57:02Z · exit code: 0
- output (first line): `Queued message 01a20844-497a-7343-b87f-e28a6143e5fa for thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7.`
- proves: the queue accepted the call. No RETURN is asked.

## p18 — lead → auditor · `codex queue`
- authority: Majkee, 2026-11-22 — the auditor makes the final check of a bigger piece of work, from the other brand (raw/decision.majkee.roster-correction.2026-11-22.md); RUNBOOK step 6
- file first: `_bus/09.lead.point.md` (committed in e9d10f3)
- looked first (2026-11-23T11:58:07Z): pane %66 — codex in the foreground, not dead, input row empty (placeholder only), no dialog
- call: `codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<line>"`, without `--resume`
- line: `[poke p18] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/09.lead.point.md — the final check of packet.md (draft 2) against the evidence; RETURN and one bell. If Majkee has a side test running with you, finish with him first`
- before: 2026-11-23T11:58:07Z · after: 2026-11-23T11:58:07Z · exit code: 0
- output (first line): `Queued message 01a20845-460a-7b01-add2-425d53757bc8 for thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7.`
- proves: the queue accepted the call. Read is shown by `_bus/09.auditor.return.md`.

- p18 outcome: read and answered — `_bus/09.auditor.return.md` picked up by the lead's file watch at 2026-11-23T11:59:52Z, 105 seconds after the poke; reply bell r09 arrived in pane %70 shortly after. Checked in `_bus/09.lead.verdict.md`.
- p17 outcome: no RETURN was asked; RETURN 09 says no side test was visible in the sample's record at its check.

## p19 — lead → controller · `codex queue`
- looked first (2026-11-23T12:06:25Z): pane %59 — codex in the foreground, not dead, input row empty (placeholder only), no dialog. No POINT: the duty is prompt-1 of the RUNBOOK. Done is shown by origin/core = `2e2303f`.
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke p19] push duty — prompt-1 in /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/RUNBOOK.md: nablarva core — fetch; only if ahead and not behind, one plain git push; never rebase, never force; write no file, type into no pane; I verify the remote ref`
- before: 2026-11-23T12:06:25Z · after: 2026-11-23T12:06:25Z · exit code: 0
- output (first line): `Queued message 01a2084c-df16-7a13-aa41-1b1bc4ee8cfe for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`
- proves: the queue accepted the call.

- p19 outcome: done — `git ls-remote origin refs/heads/core` = `2e2303f` at 2026-11-23T12:06:45Z, equal to local HEAD; checked by the lead.

## p20 — lead → exec · `codex queue`
- authority: decisions Majkee owes go through the exec desk — "decision loop stays with exec" (raw/decision.majkee.seats-and-notice.2026-11-22.md)
- file first: `_bus/10.lead.point.md`, with `raw/sheet.gate-2.2026-11-23.md` and `packet.md` (all committed in 2e2303f and pushed)
- looked first (2026-11-23T12:06:45Z): pane %68 — codex in the foreground, not dead, input row empty (placeholder only), no dialog, 58% of context left at 12:04Z
- call: `codex queue --thread 01a1fefc-0356-7ea1-860c-783a66a91211 --message "<line>"`, without `--resume`
- line: `[poke p20] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/10.lead.point.md — the gate of relay-X1-probes: walk Majkee through gate sheet 2, G0 to G10; end this turn with the G0 question as its last line`
- before: 2026-11-23T12:06:45Z · after: 2026-11-23T12:06:45Z · exit code: 0
- output (first line): `Queued message 01a2084d-2fca-7643-9a85-745d47ba1aa3 for thread 01a1fefc-0356-7ea1-860c-783a66a91211.`
- proves: the queue accepted the call.

- p20 outcome so far: read and shown — at 2026-11-23T12:07:11Z the desk's pane showed the G0 question as the last line of a turn that had just ended, above an empty input row. The lead looked at the bottom rows only and typed nothing. The RETURN comes at the end of the walkthrough.

- p20 outcome: read and answered — the walkthrough ran from 2026-11-23T12:07Z; `_bus/10.exec.return.md` was picked up by the lead's file watch at 12:23:11Z; reply bell r10 arrived in pane %70 shortly after. Checked in `_bus/10.lead.verdict.md`: GO on the first packet; the bed stays open.

## p21 — lead → controller · `codex queue`
- looked first (2026-11-23T12:27:39Z): pane %59 — codex in the foreground, not dead, input row empty (placeholder only), no dialog. No POINT: the duty is prompt-1 of the RUNBOOK. Done is shown by origin/core = `7bcf714`.
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke p21] push duty — prompt-1 in /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/RUNBOOK.md: nablarva core — fetch; only if ahead and not behind, one plain git push; never rebase, never force; write no file, type into no pane; I verify the remote ref`
- before: 2026-11-23T12:27:39Z · after: 2026-11-23T12:27:39Z · exit code: 0
- output (first line): `Queued message 01a20860-4faf-7e70-b10a-28205a47f123 for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`
- proves: the queue accepted the call.

- p21 outcome: done — `git ls-remote origin refs/heads/core` = `7bcf714` at 2026-11-23T12:28:00Z, equal to local HEAD; checked by the lead.

## p22 — lead → auditor · `codex queue`
- authority: Majkee at the exec desk, 2026-11-23, G3 (the approval series) and his go in the lead session shortly before 12:31Z (raw/decision.majkee.approval-series-go.2026-11-23.md)
- file first: `_bus/11.lead.observer.md` (committed in ad86894)
- looked first (2026-11-23T12:31:54Z): pane %66 — codex in the foreground, not dead, input row empty (placeholder only), no dialog
- call: `codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<line>"`, without `--resume`
- line: `[poke p22] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/11.lead.observer.md — approval series, first send: preflight, start the one-second watch, write the marker with the thread line; the call follows within seconds of your marker`
- before: 2026-11-23T12:31:54Z · after: 2026-11-23T12:31:54Z · exit code: 0
- output (first line): `Queued message 01a20864-3354-7fe3-8390-8ea889d905c7 for thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7.`
- proves: the queue accepted the call. Read is shown by the marker `_bus/11.auditor.ready.md`, written 46 seconds later.

- not a poke — **the first send of the approval series**: made by the lead at 2026-11-23T12:32:43.561Z; its record is `_bus/11.lead.try.md`, not this log.

- p22 outcome: read and answered — marker `_bus/11.auditor.ready.md` at 2026-11-23T12:32:40Z; `_bus/11.auditor.return.md` present at 12:43Z; reply bell r11 arrived in pane %70 at about 12:45Z, while the lead's command for cycle 12 was running.

## p23 — lead → auditor · `codex queue`
- authority: Majkee at the exec desk, 2026-11-23, G3, and his go for the second send in the lead session shortly before 12:43Z (raw/decision.majkee.approval-series-go.2026-11-23.md, second part)
- file first: `_bus/11.lead.observer.md`, which serves cycle 12 with `12` for `11` (committed in ad86894)
- looked first (2026-11-23T12:43:47Z): pane %66 — codex in the foreground, not dead, input row empty (placeholder only), no dialog; its RETURN 11 was already written
- call: `codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<line>"`, without `--resume`
- line: `[poke p23] cycle 12 — read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/11.lead.observer.md again with 12 for 11 and c12 for c11: second send of the approval series, after the mode switch. In the preflight also take the names in the outside folder as a baseline. Marker with the thread line; the call follows within seconds`
- before: 2026-11-23T12:43:47Z · after: 2026-11-23T12:43:47Z · exit code: 0
- output (first line): `Queued message 01a2086f-1578-7f02-82d7-b2daeeb36553 for thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7.`
- proves: the queue accepted the call. Read is shown by the marker `_bus/12.auditor.ready.md`, written 78 seconds later.

- not a poke — **the second send of the approval series**: made by the lead at 2026-11-23T12:45:07.977Z; its record is `_bus/12.lead.try.md`, not this log.

- p23 outcome: read and answered — marker `_bus/12.auditor.ready.md` at 2026-11-23T12:45:05Z; `_bus/12.auditor.return.md` picked up by the lead's file watch at 12:55:28Z; reply bell r12 arrived in pane %70 shortly after. Checked in `_bus/12.lead.verdict.md`.

## p24 — lead → auditor · `codex queue`
- file first: `_bus/13.lead.point.md` (committed in 4dbd315)
- looked first (2026-11-23T12:57:34Z): pane %66 — codex in the foreground, not dead, input row empty (placeholder only), no dialog
- call: `codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<line>"`, without `--resume`
- line: `[poke p24] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/_bus/13.lead.point.md — the final check of packet-2.md (draft 1) against the evidence; RETURN and one bell. If Majkee is with you about the tracker, finish with him first`
- before: 2026-11-23T12:57:34Z · after: 2026-11-23T12:57:35Z · exit code: 0
- output (first line): `Queued message 01a2087b-b6a3-7803-ac99-5d29f52bdd07 for thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7.`
- proves: the queue accepted the call.

- p24 outcome: read and answered — `_bus/13.auditor.return.md` picked up by the lead's file watch at 2026-11-23T12:59:01Z, 86 seconds after the poke; reply bell r13 arrived shortly after. Checked in `_bus/13.lead.verdict.md`.

## p25 — lead → controller · `codex queue`
- looked first (2026-11-23T12:57:35Z): pane %59 — codex in the foreground, not dead, cursor at the start of the input row. No POINT: the duty is prompt-1 of the RUNBOOK. Done is shown by origin/core = `4dbd315`.
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke p25] push duty — prompt-1 in /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X1-probes/RUNBOOK.md: nablarva core — fetch; only if ahead and not behind, one plain git push; never rebase, never force; write no file, type into no pane; I verify the remote ref`
- before: 2026-11-23T12:57:35Z · after: 2026-11-23T12:57:35Z · exit code: 0
- output (first line): `Queued message 01a2087b-b769-7c40-a703-545e928ca29b for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`
- proves: the queue accepted the call.

- p25 outcome: done — `git ls-remote origin refs/heads/core` = `4dbd315` at 2026-11-23T12:57:55Z, equal to local HEAD; checked by the lead. For this poke the lead read the pane's metadata and not its bottom rows — the controller had been seen idle half an hour before; the look was thinner than the rule asks.

- not the lead's pokes — a side quest between two other seats, found in `raw/` at 2026-11-23T12:59Z: `raw/sidequest.myshell.custody-copy-office.2026-11-23.md` (myShell → controller, on Majkee's word typed in her session) and `raw/sidequest.controller.custody-copy-office.return.2026-11-23.md` (the controller's return: the second copy of this stage's private folder is on office, a snapshot of about 12:55Z).
