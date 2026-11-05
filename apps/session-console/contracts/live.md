# Live office connection — bounded pilot amendment

Majkee authorized the reviewed ovitmugen change and live-session picker/Attach on
2026-10-30. Authority is recorded in the phone bed raw/live-adapter/authorization.
This amendment supersedes fixture-only restrictions in console.md only for the
explicitly configured live attachment. The fixture mode and storage contract remain.

Server config selects mode `live`, an absolute `ovitmugen_script` and an explicit
`agents_socket`. These are operator-side configuration, never browser parameters.
The current office pilot may invoke the reviewed authoring-source script by path;
this does not install it globally or change the default shell tools. Rollback is
restoring the previous fixture config and restarting only the pilot service.

`GET /api/state` preserves its envelope. In live mode, capabilities.live is true;
createFixture/endFixture/agentStart/agentEnd are false. Targets preserve opaque id,
label, hostId, bed, windowId, paneId, generation and busy, with kind `live`, singlePane,
dead and program metadata. Busy/running sessions are attachable; dead and multi-pane
windows are ineligible. Browser shows mode, bed/tab and selected versus attached
identity. Selection alone never attaches, sends input or changes a desktop view.

Discovery consumes the public owner `ls --json` report plus `targets BED` identity.
Attachment creates an owner-marked independent grouped view through `phone-view
create`; detach delegates to `phone-view detach` with exact name, token and server
generation. No owner-private imports, replacement lifecycle manager or durable
address registry. Create/end remain disabled for this slice. Attaching a running
Codex process does not resume a second conversation or start a new model turn.

Use the adapter's fixed attach argv for ttyd. Revalidate exact server/base/process,
window/pane and marked view identity before every input/output/resize/history and
in the watchdog. Read-only tmux checks may verify those identities efficiently;
cache only the exact expected identity, never a current-safe verdict. Any mismatch
closes the binding with no queued input/replay. Checks are not atomic OS capabilities.

Bound-view history may use fixed tmux copy-mode/send-keys -X commands after full
validation, as console.md already specifies. It never types literal q into an
application or issues lifecycle operations. Native PTY input remains explicit human
interaction; no guessing approvals or hidden model instructions. Multiline composer
paste remains disabled pending actual CLI qualification.

Retain the owner's existing window-size policy. Shared windows have one geometry;
phone attachment can resize the workstation's view under that policy. Explain this
in the UI and record actual dimensions during tests. No unrelated desktop selection,
key policy, tailnet/ACL, global installation, source commit or push changes follow.
