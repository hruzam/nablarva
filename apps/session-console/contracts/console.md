# Experimental implementation contract

Cartan accepts the following scoped candidate interfaces, 2026-10-30. No canon lock.
Storage contract is storage.md and overrides every storage portion of the proposal.
The authorized live attachment amendment is [live.md](live.md); it supersedes the
initial fixture-only restrictions only within that explicitly configured mode.

## Runtime and scope

Home: apps/session-console, subject to Cartan's collision check. Independently
buildable Python host + npm-bundled plain JavaScript/xterm frontend. The first
candidate uses ONLY /tmp/pc-trial-j6j1id09/tmux.sock and synthetic targets. Display
FIXTURE · office prominently. Never infer live eligibility from a matching name.
No global install, auto-start, live-source change, room sender or second bed manager.

System Python is 3.14.7. aiohttp, pytest and pytest-asyncio are absent. Proposed
host pin aiohttp==3.14.5 in an isolated venv; PyPI and official stable docs currently
identify that release. Resolve/install and retain the dependency lock before tests;
availability is not proof of an installed working environment. Standard-library
unittest plus aiohttp test utilities suffice; pytest is not required.
[PyPI](https://pypi.org/project/aiohttp/),
[official reference](https://docs.aiohttp.org/en/stable/web_reference.html).

Pin @xterm/xterm 5.4.0, @xterm/addon-fit 0.9.0 and @xterm/addon-unicode11 0.7.0
to the physically trialed ttyd source dependency family; use a committed npm lock.
Use xterm's owned instance and public methods/events, never window.term or _core.
Start with its default renderer; WebGL is optional, not a second initial renderer.
Retain MIT notices. External ttyd remains 1.7.7-40e79c7, binary SHA256
8a217c968aba172e0dbf3f34447218dc015bc4d5e59bf51db2f2cd12b7be4f55.

## HTTP/WS boundary

Host binds 127.0.0.1 on a configurable explicit port. Browser navigation, assets,
API, blob reads and WS all require the same configured random Basic credential.
Store credentials outside git/logs; compare correctly and return 401 with challenge.
Allow exactly configured external Host. For every request carrying Origin, require
the exact configured scheme/host/port. All mutations and WS require that Origin;
reject null/missing/foreign values. Top-level GET navigation/assets may lack Origin
but still require authentication and Host. Mutating API requests additionally carry
X-Console-Action: 1. No wildcard CORS or trusting forwarded headers by default.

The browser talks only to the aiohttp origin. aiohttp proxies to an external ttyd
bound on a separate fixed loopback address, with its own service credential, -W,
-O and fixed tmux attach arguments; no -a. Server configuration maps view to
backend; browser URLs cannot choose a command, socket, host or upstream URL.
Do not forward browser Authorization, arbitrary proxy headers or Origin blindly:
host supplies backend Authorization and canonical backend Host/Origin AFTER exact
external checks. Backend HTTP token/auth never becomes a browser credential.

Proxy initial WS JSON: browser sends {columns,rows}; host validates dimensions and
injects backend AuthToken using its private service credential. Subsequent frames
use pinned ttyd protocol (binary ASCII '0'+UTF-8 input, '1'+resize JSON; server
'0'+output and title/preferences). Host validates/restricts accepted frame kinds
and sizes, propagates close, and closes both directions on stale binding. No proxy
queue, background delivery or reconnect replay. Block direct backend /token exposure.
Owned frontend adapts these internals behind the interface below.

No tailnet/HTTPS/ACL promotion is implied. A deployment must separately establish
trusted HTTPS and the configured external origin; USB-loopback proves neither.

## Target and view API snapshot

All JSON errors: {error:{code,message}}; 400 invalid, 401 auth, 403 origin/forbidden,
404 absent, 409 stale/conflict, 501 capability unavailable. Responses no-store.

GET /api/state -> {mode:"fixture",host:{id,label},capabilities:{...},targets:[...]}
Target = {id,label,hostId,bed,windowId,paneId,generation,busy,kind:"fixture"}.
id is an opaque lookup key, not a shell address. generation binds socket inode,
server PID/process start, session/window/pane IDs and pane PID/process start.
Name/label is presentation only. Resolve and revalidate on every operation.

GET /api/office-workbenches -> {output:"plain text"} is a read-only office inventory.
It invokes the installed public owner CLI with fixed arguments: Python,
~/.config/zsh/session/ovitmugen.py, ls. No request argument selects a command,
socket, bed or executable. Authentication and exact Host/Origin checks still apply;
query parameters are rejected. Timeout15s yields504, command failure yields503.
This report does not create an attachment or enrich fixture IDs into live targets.
The browser renders it as text in a wrapped, scrollable area separate from the
fixture picker. Majkee requested this action on2026-10-30; no owner-source edit.

POST /api/views {targetId,generation} ->
{viewId,target,binding,wsPath:"/api/views/<id>/ws"}.
binding is an opaque per-attachment nonce owned by host memory, not a durable
registry. Creation makes an isolated linked/grouped fixture view if needed; fixed
backend ttyd attaches only that view. Limit one WS per binding. If a view rebinds,
close the old WS before completing a new selection; old binding cannot write.
GET WS path requires authentication, exact Origin and the binding supplied as its
first JSON initialization field along with columns/rows. Host consumes binding;
ttyd receives only validated dimensions and injected AuthToken.
DELETE /api/views/<id> -> {detached:true}; close attachments and owned view only.
Detach never kills the underlying shell, agent, base bed or last surviving owner.
Host restart invalidates every attachment; UI must refresh/reselect, not replay.

Fixture windows are single-pane initially. Grouped sessions share windows/panes
and their dimensions; active-window selection is independent, active-pane selection
inside a shared multi-pane window is not. Never claim independent live pane control
until an owner-aligned mechanism is reviewed. Expose sizing effects in the UI.

POST /api/fixtures {name} -> owned synthetic workbench target.
DELETE /api/fixtures/<id> {generation,confirm:true} ->
only a candidate-owned idle synthetic target, after immediate identity/busy checks.
Never kill the last protected base or a busy process. Busy refusal -> 409.
No arbitrary agent-start command or force-end endpoint in this first snapshot.
Show agent start/end as distinct unavailable capabilities pending an explicit scoped
launch specification; running native CLI exit remains an intentional PTY action.

## Actual ovitmugen seam and live hold

Read source: /home/hruzam/ia-sync/zsh/session/ovitmugen.py, especially tabs(),
bed_report(), close_idle_tab(), switch_tab() and main(). Public CLI offers
up [slug] [tabs...] --no-attach/--dry-run, tab [slug] ref, ls [slug] --json,
down [slug] --frame|--views|--idle, console and selftest.
ls JSON = [{bed,tabs:[{id,index,name,active,busy,cmd,fg,left}],views,frame}].
It lacks pane/process/server-generation details. tab mutates shared <slug>--left.
Guarded single-tab close_idle_tab() is internal, not a public machine CLI operation;
down --idle is broader and must not substitute for end-selected. up may also build
frame/runbook components; it is not a pure workbench primitive.

LIVE capability requires its owner to expose/review independent view create/select/
detach, exact target metadata and guarded one-tab close in a machine interface.
Do not import private functions or duplicate their lifecycle rules in this app.
Use public ls --json for discovery when live is later enabled; enrich exact target
identity through a reviewed read-only adapter. No live-source implementation is
authorized by this proposal. Fixture capability is clearly separate and bounded.

## Browser terminal interface

web/terminal.js exports createTerminal({container,onState}) ->
{attach(view),detach(),focus(),paste(text),key(name),history(action),fit(),dispose()}.
onState emits {state:"detached"|"connecting"|"connected"|"disconnected"|"stale",
targetId,generation,uncertainInput:boolean}. All sends require current connected
binding; reject instead of queueing. New attach disposes the previous WS first.
key uses an explicit allowlist; Enter is CR, distinct from paste. Native xterm
keyboard onData follows the attached PTY; no vendor approval inference/interception.
paste uses the owned public xterm paste API. Multiline paste requires bracketed
paste support and qualification for the actual CLI; otherwise refuse it visibly.
No automatic Enter, submit, retry or uncertain-input replay. Socket send success is
not process acceptance. Composer retains its draft after sending until explicit
operator clear; label uncertainty after disconnect.

Use the corrected touch-to-wheel behavior in this owned module. Preserve pinch and
tap/IME, provide explicit history/key fallback, and physically requalify. Initial
font12 and viewport metadata carry forward the successful fixture settings.


## Integration entry

Serve web/index.html at /; esbuild dist/app.js and dist/app.css at /assets/.
Host CLI: `.venv/bin/python -m host.server --config /absolute/private/config.json`.
Config keys: port, public_origin, credential_file (JSON containing credential string
username:password), fixture_socket, ttyd_binary, runtime_root, vault_root. Bind only
127.0.0.1. Refuse default/live sockets; explicit fixture socket owner only. Existing
trial state.json can be credential_file; never log its contents.

Install storage via `from .vault import install_vault; install_vault(app, Path(vault_root))`.
No upload endpoint implementation in server/terminal modules.

UI imports createTerminal from ./terminal.js, stores from ./storage.js, and
`api(path, options={})` from ./api.js. api JSON-encodes options.body unless body
is Blob/ArrayBuffer; sets X-Console-Action:1 for mutation, accepts options.headers,
returns decoded JSON and throws Error with .status/.detail on failure. File download
is ordinary authenticated GET link.

Terminal key(name) accepted names: Enter,Tab,ShiftTab,Escape,ArrowUp,ArrowDown,
ArrowLeft,ArrowRight,PageUp,PageDown,Home,End,Backspace,Delete,CtrlC,CtrlD,CtrlZ,
History (tmux prefix+[),Live (copy-mode q only). No arbitrary caller-provided escape
sequences. UI labels History/Live semantics, prevents accidental CtrlD end.

Ownership: Cartan contracts, manifests/locks, web/api.js, README. Astrobley owns
host/{server,security,sessions,terminal_proxy}.py, web/terminal.js, tests/test_host.py.
UI worker owns web/{index.html,app.js,styles.css} only. Vault worker owns
host/vault.py,web/storage.js,tests/test_vault.py and storage-specific tests.

History safety refinement (same scoped implementation):
POST /api/views/{id}/history {action:'enter'|'leave'|'pageUp'|'pageDown'} is a
bound view control. Revalidate active view window/pane and target generation;
use only tmux copy-mode commands/send-keys -X (no process input). Leave is no-op
when not in copy mode; never send a literal q to an application. key(History/Live)
calls this endpoint. Native tmux window navigation that diverges from bound target
invalidates/closes the attachment; do not keep sending under a stale target label.

Visible history controls (2026-10-30 refinement): Older/Newer call history(pageUp /
pageDown), which always enters copy mode first and uses only the bound HTTP history
endpoint. The original view is captured and checked around awaits; detach/reselect
cannot move the remaining step into a new attachment. Back to live calls leave.
These controls never emit native PageUp/PageDown or other application input.
Expand/Shrink changes terminal height and uses the existing validated resize path.
