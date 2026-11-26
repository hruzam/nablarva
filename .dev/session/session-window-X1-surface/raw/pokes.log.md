# pokes.log — session-window-X1-surface

One row per labelled line, sent or received by this bed's seats (RUNBOOK, "Communication protocol"). Times are UTC. A
received row's time is when the file was written, unless it says otherwise; the line's arrival in the pane was not timed.
Majkee's own words are not pokes: they go to decision files in raw/.

| # | UTC | direction | line (label only) | door | exit | what it proves |
|---|---|---|---|---|---|---|
| 1 | 02:02 (file) | manager → lead.seswin | `[brief e07]` → eSharp/_bus/07.manager.point.md, ack per file | pointer line into %80 | not seen by the lead | the brief reached the lead's pane; the RETURN eSharp/_bus/07.lead.seswin.return.md answers it |
| 2 | 02:06 (file) | manager → lead.seswin | `[answer e09]` → eSharp/_bus/09.manager.point.md, ack none | pointer line into %80 | not seen by the lead | the answer was read; no reply asked for |
| 3 | 02:47:28 paste · 02:47:39 Enter | lead.seswin → manager | `[notice s04]` → _bus/04.manager.notice.md, ack none | look-first paste into %77 (set-buffer, paste-buffer -p, look, send-keys Enter, look) | 0 · 0 | queued: the pane showed "Press up to edit queued messages" while its turn ran; read not yet shown |
| 4 | 02:52:42 | lead.seswin → audit.seswin | `[point s07]` → _bus/07.audit.point.md, ack per file | `codex queue --thread 01a21585…` without `--resume` | 0 | the queue accepted it (message 01a215c5…); a look at %81 right after showed the pane idle at its prompt, no turn started. Reconciled by the file: _bus/07.audit.seswin.return.md written 02:56:33, so the line was read within four minutes; the look came too early to show the turn |
| 5 | 02:57:59 | lead.seswin → audit.seswin | `[point s11]` → _bus/11.audit.point.md, ack per file | `codex queue --thread 01a21585…` without `--resume`, after a look (idle at its prompt) | 0 | the queue accepted it (message 01a215c9…); read is shown by the RETURN file |
