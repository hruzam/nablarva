# Pokes of the lead's fork — relay-X1-probes, 2026-11-23 (outside the repository; folded into raw/pokes.log.md by the pen holder)

- scheduler: one-shot job 71185a9a of session b155ba44, 17:45 local (a first job bc7fb82f pointed at a path inside the repository and was cancelled before it ran)
- doorbell: armed fresh shortly before 14:45:27 UTC, background task boru43iou

## fp01 — lead's fork → controller · `codex queue`
- authority: Majkee in the fork session, 2026-11-23 (decision.majkee.scheduler-doorbell.2026-11-23.md, second part)
- file first: f01.lead.point.md in this folder
- looked first (2026-11-23T14:45:27Z): pane %59 — codex in the foreground, not dead, input row empty (placeholder only), no dialog
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke fp01] read /home/hruzam/.cache/nablarva/relay-x1-fork/f01.lead.point.md — on Majkee's word: build CACHE.lead.md from the lead's transcripts with a small .js script; RETURN file to the path it names, no bell into %70`
- before: 2026-11-23T14:45:27Z · after: 2026-11-23T14:45:27Z · exit code: 0
- output (first line): `Queued message 01a208de-7a23-73e1-af03-2554aaf66ae6 for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`

- fp01 outcome: done — `CACHE.lead.md` landed 14:48:05Z (first ring of the doorbell, 14:48:09Z), RETURN f01.controller.return.md 14:48:41Z (second ring). Checked by the fork: size, lines, mode, untracked, 390 tool calls and 81 lead messages hold. REVISE: messages that arrived mid-turn are missing — transcript records `attachment`/`queued_command`, 14 of human origin in the original; Majkee's second message to the fork and every reply bell among them. Third transcript file d406a745 = the original's declared continuation (the controller's finding).

## fp01r1 — lead's fork → controller · `codex queue`
- authority: the same word as fp01 — one revision of the same delivery
- file first: f01r1.lead.point.md in this folder
- looked first (2026-11-23T14:50:14Z codex dead=0 cx=2): pane %59 — input row empty (placeholder only), not working, no dialog
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke fp01r1] read /home/hruzam/.cache/nablarva/relay-x1-fork/f01r1.lead.point.md — REVISE on the cache: messages that arrived mid-turn (queued_command attachments) are missing, his second message and all bells among them; RETURN file to the path it names, no bell into %70`
- before: 2026-11-23T14:50:14Z · after: 2026-11-23T14:50:15Z · exit code: 0
- output (first line): `Queued message 01a208e2-dc83-7413-ac3c-82f6a6d89e5b for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`

- fp01r1 outcome: done — cache rebuilt 14:52:06Z (ring 14:52:11Z), RETURN f01r1.controller.return.md (ring 14:53:11Z). The fork's checks at 14:53:20Z all hold: 237,637 bytes, 2,603 lines, 0600, untracked; "Last thing, now asking" once as Majkee [fork] at 14:40:00Z; ten `[bell r` entries; "After that you can send" as its own Majkee entry at 13:31:56Z; speakers — Majkee 25 original + 2 fork, seat hints 14, lead 81 + 6 + 1, summaries 2 + 1, one fork marker. The controller found no queued human text that was never delivered. ACCEPT. The cache is a cut; the refresh command is `node ~/.cache/nablarva/relay-x1-cache/build-cache.js` and is the controller's to run — asked again in the 17:45 round.
- doorbell: four rings so far, each within six seconds of the change; armed again after each.
- scheduler: job 71185a9a fired at 2026-11-23T16:45Z (17:45 local) as set; the fork read the clock at 16:45:13Z

## fp02 — lead's fork → pane %66 · `codex queue`
- authority: Majkee in the fork session, 2026-11-23 (decision.majkee.scheduler-doorbell.2026-11-23.md, first part, point 1) — the 17:45 round
- file first: f02.lead.point.md in this folder
- looked first (2026-11-23T16:46:12Z codex dead=0 cx=2): input row `› Ask Codex to do anything`, not working
- call: `codex queue --thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7 --message "<line>"`, without `--resume`
- line: `[poke fp02] read /home/hruzam/.cache/nablarva/relay-x1-fork/f02.lead.point.md — 17:45 status round on Majkee's word: your section only, five lines, look only; RETURN file to the path it names, no bell into %70`
- before: 2026-11-23T16:46:12Z · after: 2026-11-23T16:46:12Z · exit code: 0
- output (first line): `Queued message 01a2094d-076f-7293-ad75-1d2c013019cd for thread 01a1ffdf-793f-76d2-8497-3f68f84a34a7.`

## fp03 — lead's fork → pane %59 · `codex queue`
- authority: Majkee in the fork session, 2026-11-23 (decision.majkee.scheduler-doorbell.2026-11-23.md, first part, point 1) — the 17:45 round
- file first: f02.lead.point.md in this folder
- looked first (2026-11-23T16:46:12Z codex dead=0 cx=2): input row `› Ask Codex to do anything`, not working
- call: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message "<line>"`, without `--resume`
- line: `[poke fp03] read /home/hruzam/.cache/nablarva/relay-x1-fork/f02.lead.point.md — 17:45 status round on Majkee's word: your section only — push duty for four local commits, one fresh cut of the cache, five lines; RETURN file to the path it names, no bell into %70`
- before: 2026-11-23T16:46:12Z · after: 2026-11-23T16:46:13Z · exit code: 0
- output (first line): `Queued message 01a2094d-0871-7fe1-b9dc-752473b7774a for thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318.`

- fp02 outcome: done — f02.auditor.return.md at 16:46:39Z, four lines; ring 16:46:42Z. Tracker stopped 13:05:53Z, script and logs handed over and verified on home; office copy's last pass open.
- fp03 outcome: done — f02.controller.return.md at about 16:47:00Z; ring 16:47:02Z. Push d0281b6 → 8e15629, remote ref checked by the fork = local HEAD; cache refreshed to the cut of 16:46:49Z. Closed in f02.lead.note.md.

- doorbell: ring at 2026-11-23T17:38:03Z — `raw/decision.majkee.gate-3.2026-11-23.md` appeared: Majkee is back and at the exec desk. At 17:38:39Z the record held H0 and H1 (headings read only) and the desk's last line was its question on a further test (H2). The walkthrough's RETURN and bell r14 go to the pen holder in %70.
- the fork stands down at 17:39Z: no doorbell armed, no job scheduled, nothing in flight. It wrote nothing inside the repository. For the pen holder before VERDICT 14: f02.lead.note.md (tracker stopped 13:05:53Z; origin/core = 8e15629; `CACHE.lead.md` exists, untracked, the controller's script refreshes it; the last pass of the office copy is possible and waits for his H4).
