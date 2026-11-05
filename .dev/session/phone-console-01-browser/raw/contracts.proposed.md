# Proposed candidate contracts — Cartan review required

Astrobley · 2026-10-30. Proposal only; Cartan owns accepted contracts and dispatch.
No application or ia-sync file changed. Parent reports physical font12, width and
swipe PASS after the corrected disposable adapter. Preserve that behavior in the
owned frontend, then qualify again; the new frontend is a new candidate.

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
{attach(view),detach(),focus(),paste(text),key(name),fit(),dispose()}.
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

## Vault and browser storage boundary

Host factory install_vault_routes(app, *, root) registers ONLY /api/vault/*;
host's auth/origin middleware wraps every route. Dedicated configured root only;
opaque IDs, no arbitrary read paths or symlinks outside root. Atomic durable writes
before acknowledgement; concurrent revision changes produce 409 with current item.

GET /api/vault -> {items:[{id,kind,title,revision,updatedAt,size?,sha256?}]}
GET /api/vault/<id> -> item including text or blob metadata.
POST /api/vault {kind:"prompt"|"shortcut",title,text} -> item revision1.
PUT /api/vault/<id> {expectedRevision,title,text} -> next item revision.
DELETE /api/vault/<id> {expectedRevision,confirm:true} -> {deleted:true}.
POST /api/vault/files multipart(file,sha256,title) -> committed blob item with
{id,kind:"file",title,revision,size,sha256,attachmentPath,downloadUrl}.
GET /api/vault/<id>/blob -> attachment bytes; never executable HTML inline.
Server recomputes SHA256, verifies supplied digest, and acknowledges exact stored
bytes. Start at bounded 25 MiB/file and 20 files/batch (batch is client sequencing).
Failed files retain retryable selection; successful files have individual receipts.

web/storage.js exports openDraftStore() -> {get,put,remove,list,clearExpired,status}.
Records = {id,kind:"draft"|"tray",targetId,text,revision,updatedAt,expiresAt:null|ms}.
put(record,expectedRevision) resolves only after IndexedDB transaction completion;
stale revision returns a conflict, never overwrite silently. Drafts do not expire;
tray expiry is absolute 30 minutes and enforced on reads/startup as well as timer.
Storage denial/quota errors surface explicitly; volatile memory may be offered with
a warning and cannot be labelled saved. navigator.storage.persist is best-effort.
Vault uses explicit save/load and server revisions; it is not hidden draft sync.

Gallery uses multi-file image selection, camera a separate capture-hint input.
Client SHA256 versus server receipt and stored-byte verification precede any cleanup
offer. Workstation attachmentPath is displayed/copied deliberately, never sent into
terminal automatically. Browser Files cannot delete Android Gallery originals:
offer only explicit manual Gallery cleanup after per-file verified upload, preserving
batch receipts. No automatic phone deletion and no deletion of workstation copies
as a substitute. See raw/operator-photo-request.2026-10-30.md.

## Disjoint file/owner proposal

| Owner | Exact candidate files |
|---|---|
| Cartan | contracts/, package.json/package-lock.json, requirements lock, build/run entry, integration configuration, shared web/api.js |
| Astrobley | host/server.py, host/security.py, host/sessions.py, host/terminal_proxy.py, web/terminal.js, own targeted host/transport tests |
| UI | web/index.html, web/app.js, web/styles.css; imports terminal/storage/api interfaces, does not implement them |
| Vault | host/vault.py, web/storage.js, web/vault.js, web/photos.js and own storage/vault tests; no host app factory or shared middleware edits |
| Fresh verifier | independent fixtures/evidence/tests; no implementation fixes or STATUS |

Cartan must freeze the exact JSON/JS interfaces and vault route-registration signature
before dispatch. UI owns composition/layout only, Vault owns its modules and controls,
Astrobley owns terminal mount/transport; agree container/action hooks in contracts.
Live-owner extensions, agent-start specification and reviewed publication remain gates.
