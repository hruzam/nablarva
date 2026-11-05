# Qualification edge — fixture candidate, not full pilot acceptance

| Area | Evidence / present result |
|---|---|
| Build and host/storage tests | npm build;26 app tests and9 owner tests PASS, independently repeated; live-adapter/verification.md; earlier receipts retained |
| Independent host/terminal review | Bounded PASS, verification.host-terminal.md; fixture only |
| Independent storage/UI review | Bounded PASS, verification.storage-ui.md |
| Phone font/width/swipe | Majkee accepted font12, width fits, corrected scrolling works on first terminal trial |
| New browser terminal | Phone live attachment confirmed. Older/Newer/Back navigation browser witness300→286→271→286→300 with noPTY input; Expand304→624px at360px width; history-controls/verification.md. New controls await physical Firefox witness |
| Draft persistence | Czech multiline draft survives full desktop browser process restart; persistence-request denial handled visibly |
| Tray | Real desktop interval PASS:1801610ms, expired tray inaccessible, unsent draft retained; real-expiry.cartan.2026-10-30.json |
| Shared vault | Prompt revision save and2 synthetic image uploads read back byte-identical; list survives reload |
| Real phone image batch | Majkee confirms both photos Verified with workstation paths; no original deletion performed |
| Camera | File-input capture control built; actual camera workflow not yet witnessed |
| Native approvals | NOT RUN; no approval-state inference or bypass exists |
| Screen off10min | Majkee reports console holding after unlock/browser restore. Exact interval and separate draft/file-list assertions remain unconfirmed; physical-resume.2026-10-30.md |
| Office inventory | Fixed authenticated read-only owner ls; browser77-line result wraps/scrolls at360/412px, timeout retry passes; office-list.browser.2026-10-30.json; independent delta PASS in verification.office-list.md. Physical Firefox check pending |
| Live sessions | Majkee authorized source/interface change. Independent9+26 PASS, isolated two-pane browser input/switch tests PASS. Actual existing office Codex attach/output/detach preserves desktop selection/PID; live-adapter/office-attach.2026-10-30.json. Majkee reports another live session attaches and works; full native-key/approval matrix remains open |
| Deployment | Temporary authenticated loopback/USB run only; no HTTPS/tailnet/ACL or ia-sync promotion |
| Documentation | Houston stretches finding dispositioned; body factual update, shared wrapper/architecture patch proposed only |

Completed real-expiry runner state: /tmp/phone-console-browser/expiry-start.json, persistent
browser profile /tmp/phone-console-browser/profile. Read current wall time before
checking; a shorter test or deterministic-clock case must not stand in for30min.
Phone10min and desktop30min are separate observations, not one combined pass.

Original phone images cannot be deleted by browser File inputs. The implemented
cleanup surface is a manual Gallery checklist after individual verified receipts.
Multiline composer sending is intentionally refused pending target qualification;
its text still saves. Live workbench creation/end and multi-pane independent selection remain
unavailable capabilities. No overall GO or session closure is claimed.

Office-list review observed one transient existing fixture-close409 in its first
full suite; focused and complete17-test reruns passed. See verification.office-list.md.
