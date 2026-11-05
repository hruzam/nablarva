# Session console — experimental phone pilot

A browser terminal, durable local composer and shared file/prompt vault. The host
supports disposable fixture workbenches and an explicitly configured live ovitmugen
adapter. Live attachment uses the reviewed public owner interface and preserves
independent phone selection. See `contracts/live.md` for its boundaries and
`../../.dev/session/phone-console-01-browser/STATUS.md` for current qualification.

## Use from the phone

For the current USB pilot, keep the phone connected to the office computer and open
`http://127.0.0.1:18790` in the same Firefox profile. Use the pilot credentials already
provided; they are deliberately absent from this repository. This address works only
while the host service and USB reverse mapping are running. It is not an installed
always-on service.

Use **List office workbenches** beside the workbench controls to run the installed
ovitmugen listing. It shows the current office beds and tabs (● busy, ○ idle);
it does not attach to or switch an office terminal. Tap it again to refresh.

When the header says LIVE, choose a session from the Workbench picker, grouped by
office bed. Check its tab/program, tap Attach, then Keyboard. You are interacting
with that existing terminal, including its native assistant prompts and approvals.
A running/busy marker does not prevent attachment. Tap Detach before choosing a
different session; detaching keeps the assistant running. Ended and multi-pane
windows are currently unavailable.

1. **Draft a message:** open Composer, write your text, then wait for “Saved on this
   browser” or tap Save draft. Draft storage belongs to this browser; use Saved
   prompts & shortcuts for text you want in the shared workstation vault.
2. **Save reusable text:** open Saved prompts & shortcuts, choose New item, enter a
   name and text, then Save item. Load and Copy to draft brings it back to Composer.
3. **Upload photos:** open Photos & files, Choose files, select several photos, then
   Upload selected. Wait for Verified and a workstation path for each file. Saved
   files can be refreshed after reopening the page. Camera is present but still
   needs its physical phone test.
4. **Use the terminal:** select a Workbench and tap Attach, then Keyboard.
   Check the selected target before typing. Composer's Paste to terminal and Send
   Enter are separate actions; currently only single-line paste is supported.
   Use ↑ Older and ↓ Newer directly below the terminal to move through retained
   terminal output. Back to live returns to the current screen. Expand beside
   Keyboard makes the terminal taller; Shrink restores its compact height.
   Detach leaves the workbench running.
5. **Return after a disconnect:** Refresh, deliberately select the target and Attach
   again. Check the terminal before repeating a command: uncertain input is not
   replayed automatically.

The FIXTURE label means only disposable test workbenches are available. LIVE means
the host is configured for existing office sessions; nothing attaches automatically. Uploading a photo saves it on the
workstation; it does not automatically attach it to an assistant conversation.
Phone-original cleanup is manual: check the saved copy first, then select the
matching originals in Android Gallery if you want to delete them.

## Build

From this directory, with Python 3.12+ and Node available:

```sh
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.lock
npm ci
npm run build
.venv/bin/python -m unittest discover -s tests -v
```

Dependencies are local; ttyd is an external pinned dependency (1.7.7, MIT), not
installed globally by this component. See the session trial evidence for its
binary checksum/download source. xterm.js 5.4.0 and fit addon0.9.0 are pinned;
changes need a new mobile qualification. Retain dependency license notices when
redistributing a build.

## Run and recover

Run `.venv/bin/python -m host.server --config /absolute/private/config.json`.
The private configuration supplies port, public_origin, credential_file,
ttyd_binary, runtime_root and vault_root. Fixture mode additionally requires
fixture_socket. Live mode requires mode:"live", an absolute ovitmugen_script with
the reviewed public phone API, and a fixed agents_socket (office uses "default"). Credential file is JSON
with `credential` containing a Basic username:password; keep it out of version
control. Bind is loopback only. All pages, HTTP APIs and WebSockets are authenticated;
mutations and WebSockets require exact Origin. No arbitrary command or upstream
URL comes from the browser. The backend ttyd credential stays server-side.

A USB reverse mapping may expose that loopback service to the explicitly authorized
phone for qualification. This is not a tailnet HTTPS deployment. Host shutdown
closes gateway attachments, preserving the underlying workbenches. Runtime and vault roots
are separate: stopping a service must not erase saved files. The session STATUS
records exact process, port and fixture recovery commands for the current run.

## User behaviour and limits

- Select and attach a workbench explicitly. A new target or stale identity needs
  another explicit selection. No input is queued or replayed after disconnect.
- Paste and Enter are separate; multiline paste is refused without bracketed-paste
  support. Socket delivery does not establish application acceptance. Draft text
  remains until deliberately cleared.
- Drafts use IndexedDB and acknowledge transaction completion. Browser storage
  denial/quota errors are visible. Unsent drafts do not expire; tray items expire
  after30 minutes. Browser eviction remains possible if persistence is denied.
- Saved prompts/shortcuts have revision conflict checks. Files are uploaded as exact
  bytes (including metadata), SHA256-verified and reread before acknowledgement.
  File receipts include workstation path and authenticated download link.
- Gallery supports multiple selection; camera uses the browser's capture chooser.
  Partial upload failures remain retryable. Verified uploads can be followed by a
  manual Gallery cleanup checklist. The browser cannot delete phone originals.
- Live mode supports attaching existing single-pane sessions and detaching.
  Workbench creation and ending are disabled there. Native agent approval
  qualification, multi-pane selection and tailnet installation remain separate
  qualification items; this README does not claim they passed.
