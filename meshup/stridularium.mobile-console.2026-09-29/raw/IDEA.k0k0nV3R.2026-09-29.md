<!-- origin: ~/unikuklatrix/k0k0nV3R/IDEA.md · author @Cartan (Codex, office) · 2026-09-29 · copied byte-for-byte 2026-10-02 into the animal (majkee rule: working files held in nablarva with their origin); the source folder is now a stub pointer -->

# k0k0nV3R — coconvergence

Status: IDEA / planning only · majkee brief, 2026-09-29 · observations by @Cartan on office.
Placement requested: `~/unikuklatrix/k0k0nV3R/`. No application code, build, APK,
framework choice, repository initialization, or new project harness authorized here.

## What it does

A comfortable Android console for the sessions already living on **home** and **office**.
Termux + SSH over the tailnet + tmux is the existing working base. Claude Code and Codex
run on the computers; Galaxy and Redmi are places to work with them.

Open → choose host → see sessions / windows / panes → enter one and work.
Create and maintain sessions too. Galaxy is a working device, not just a monitor.
The menu and dashboard should have the clarity of Claude Code's terminal UI, with a
native mobile console and keyboard made for typing code and controlling a terminal.

The other central tool is a **text tray**: select → collect → arrange → choose destination
→ release. A paragraph, command, prompt, or several blocks can wait there while switching
apps and sessions. Closing the Android app must not lose the collected work.

## Name — keep the working spelling

- Directory / working project: **k0k0nV3R**. Preserve its exact case.
- Read aloud: **coconvergence**; the ending also carries software “ver”.
- Visual sketches only: `k0k0nV3R`, `k₀ → k∞`, `kₙ → k∞`, `coco → convergence`.
  The mathematical versions are logo ideas, not claims about a convergence theorem.
- The operator's ASCII direction, `[0[0|\|\/3|R`, is a visual seed; backslashes,
  pipes and brackets are awkward shell characters, so keep it off the directory name.
- A final spoken name and mark remain open. No public namespace or package name claimed.

## What exists now — checked 2026-09-29

| Surface | Observation |
|---|---|
| This computer | office: `hruzam-120922`, tailnet `100.126.182.111`; node ID matches `ia-sync/machines.json` |
| Other computer | home: `hruzam`, tailnet `100.110.27.60`; SSH office → home → office passed |
| Galaxy | tailnet `100.127.230.71`, online; Samsung SM-T585 detected on office USB; Android 8.1.0 / API 27 / armeabi-v7a |
| Redmi | tailnet `100.105.201.3`, online; Xiaomi MTP + ADB detected on office USB; model `2508CRN2BE`, Android 15 |
| Host entry | Both devices now have writable tmux on both hosts: office forces `tmux new-session -A -s agentive`; home uses `tmux -u new-session -A -s agentive` |
| Galaxy change | Promoted from read-only to writable tmux on both hosts; later rotated its forgotten-passphrase key on-device. Source-IP/forwarding restrictions retained, backups recorded in ia-sync |
| Redmi software | Existing `~/bin/bed` equals ia-sync source; passphrase-protected Ed25519 key; Termux sshd key-only on 8022 |
| Home sessions | No default tmux server at first probe; attachment can now create the Galaxy landing session |
| Model tools | Claude available on both hosts; Codex is `~/.local/bin/codex` on office and `~/.npm-global/bin/codex` in home's interactive shell |
| Galaxy software | After the old passphrase was forgotten, operator generated a new encrypted key on Galaxy; its public key is registered on both hosts. Key-only Termux SSH works from both hosts; installed the existing `bed`, extra keys, aliases and widget scripts; backups retained |
| Galaxy interactive proof | New key unlocked on-device; Galaxy → office AND home passed create/type/execute/detach/reconnect through disposable sessions, then test sessions removed |
| Redmi interactive proof | Redmi → office AND home passed create/type/execute/detach/reconnect and Unicode byte delivery; disposable sessions removed |
| Display/input findings | Galaxy received Redmi's JetBrainsMono Nerd Font; operator confirmed improved appearance. Initial input block was tmux copy mode. Both devices needed explicit `tmux -u` on home because its SSH locale was empty; live UTF-8 checks and operator display confirmations passed |
| Shortcut/navigation finding | Both devices now use `office` / `home` aliases through `bed`, which requests an SSH terminal. Redmi's old `office bed` sent a remote command without a terminal and failed. Operator confirmed the corrected office session chooser works; no ovitmugen/runbook conflict found |
| Remaining checks | Galaxy 10-minute locked-screen session survival and physical S-TAB passed by operator report. Redmi's physical S-TAB and 10-minute locked-screen checks remain unreported |

USB enumeration is not ADB authorization. Tailnet “online” is not proof of a running
Termux sshd. Registered public keys are not proof that the operator can unlock their
private keys. Keep those observations separate when continuing this plan.

Existing source to reuse or examine:
`~/ia-sync/devices/_shared/termux/` (`bed`, extra keys, widget shortcuts),
`~/ia-sync/devices/_shared/agentive-tmux.md`, and
`~/ia-sync/zsh/remote-cli/remote-cli.sh` (fit/wide/scroll controls).
Device maintenance evidence belongs in ia-sync's device cards/logs and host journal.

## First experience

1. **Hosts.** Office and home, connection state and last successful check; one clear
   unlock prompt for the selected device's SSH key. A failed connection keeps the draft.
2. **Sessions.** A fast host → session → window → pane list; server/socket groups appear
   only when needed or in the advanced view. Show a useful name and working directory; process/title hints may suggest
   Claude or Codex but must not invent agent identity or “waiting for approval” state.
3. **Console.** Open the actual terminal, with native text selection, readable monospace,
   Ctrl/Alt/Esc/Tab/arrows/PgUp/PgDn, copy mode, paste and detach within reach. Support
   landscape tablet use and the smaller phone. Make keyboard height adjustable.
4. **Maintain.** Create, rename and switch sessions/windows/panes. Closing a mobile tab
   means detach. Killing a remote session is a separate, explicit action.
5. **Text tray.** Collect selected blocks, label/reorder/edit them, see their source and
   destination, and release to one chosen pane. Tap-based controls must accompany drag.
   Paste and submit/Enter are distinct actions.
6. **Return.** After app closure, restore tray contents and pending draft first, reconnect,
   re-discover the host and ask the user to choose again if the old target vanished.

## Navigation proposal — host first, living sessions underneath

Added 2026-09-29 at majkee's request. These are design recommendations to discuss,
not a framework choice or build authorization. The example session names below are
illustrative; the real menu comes from the selected host's current inventory.

```text
Hosts
  Office                         Home
    Sessions                       Sessions
      Recent / pinned                ...
      Live sessions
        project-a
          1: Claude
            main pane
          2: Codex
        scratch
      + New session
    Services
      Preview · Files · Status

Always available: Console · Text tray (3) · Recent destinations
Console breadcrumb: Office / project-a / 1: Claude / main pane
```

**Keep the hierarchy shallow until it helps.** Tap a host to open its sessions submenu.
Tap a session to resume its last valid pane; the disclosure arrow opens its windows.
Show a pane submenu only when a window has multiple panes. Long-press opens rename,
new window, split and close actions. Search matches session names and working directories
within the selected host; an explicit “All hosts” scope can search both.

**Phone and tablet share one model.** Redmi gets a collapsible drawer so the terminal
keeps its width. Galaxy landscape can pin a narrow host/session panel beside the console.
The tray opens as a bottom sheet or side panel. Keep the active host and destination
visible while typing; switching the navigation host does not silently move an unsent draft.
Recent targets are shortcuts to a fresh lookup, never proof that the old pane still exists.

**Make the session list useful without claiming to know the agent's mind.** A row can show
name, abbreviated directory, window count, attached-client count and last refresh time.
“Running process”, “output changed” and “waiting for your decision” are different facts.
The last one needs a supported CLI event; a quiet terminal is not evidence of an approval
request. Distinguish “no sessions” from “could not read sessions”; retain a visibly stale
snapshot during a connection loss and keep mutations unavailable until revalidated.

**Ovitmugen needs grouping, not another mandatory navigation level.** Office's agent
sessions are on tmux's `default` server. Ovitmugen's frame UI is on `ovitmugen`, with
Ctrl+A; ordinary agent sessions use Ctrl+B. Group its shared-window views under their
parent workbench so `tunnel` and `tunnel--left` do not look like two independent jobs.
Use tmux group/window identity and explicit metadata, not the name suffix alone. Offer
“All sessions / servers” for diagnosis; only show an ordinary user a server selector when
there is a real choice. Mobile should normally open the agent terminal directly; a
desktop frame containing two nested panes may be a poor fit on Redmi.

**First useful controls:** Sessions, Windows, New, Copy/scroll, Paste, S-TAB and Detach.
These remove the need to memorize Ctrl+B sequences. Keep the tested Termux shortcuts
as fallbacks. Closing a mobile view detaches; ending a remote process names its host and
session explicitly. A new-session form asks for host, name and directory, then opens a
shell; starting Claude or Codex is a separate visible choice.

## Services beside the tailnet connection

Tailscale supplies network reachability. The app can provide a small **Services** menu
per host, with adapters for a terminal, files, an HTTP page or an event feed. “Mount” here
means making a service available in the app; an Android filesystem mount is not required.
Keep the existing Tailscale Android app as the network provider. A second Android VPN
service would displace the first one, so ordinary SSH/HTTPS connections are the initial
design direction. [Android VPN lifecycle](https://developer.android.com/develop/connectivity/vpn)

| Service | Useful app action | Suggested timing and constraint |
|---|---|---|
| SSH + tmux | Open, create and maintain host sessions | Core. Preserve each device's identity, host verification, PTY allocation and working UTF-8 behavior |
| Session inventory | Populate the live navigation panel | Core. A structured response from a host helper; current forced-tmux keys do not offer this API |
| Private web previews and documents | Open a running project's preview, report or host dashboard | First optional service. Register an existing URL; Tailscale Serve can expose a host-local HTTP service privately over HTTPS. Start with the system browser; embedding comes only when a workflow needs it. [Serve](https://tailscale.com/docs/features/tailscale-serve) |
| File send/receive | Send a screenshot, prompt file or exported tray bundle | Taildrop is a candidate for deliberate one-off transfers between the user's own devices, with Android share-sheet handoff to evaluate. Receipt of a file does not mean an agent opened it. [Taildrop](https://tailscale.com/docs/features/taildrop) |
| Remote folders | Browse selected project artifacts; download or upload a file | Later: SFTP with an explicitly provisioned file-access route, or Taildrive/WebDAV. The current forced-tmux key cannot simply be reused for SFTP. Taildrive is alpha; Android can access desktop shares but cannot host its own shares. Folder access is not automatic offline synchronization. [Taildrive](https://tailscale.com/docs/features/taildrive) |
| Host status and logs | Inspect uptime, memory/disk pressure or a selected service's status | Later, read-only helper queries or links to an existing dashboard. Register useful services explicitly instead of discovering every listening port |
| Notifications | “Task finished” or a supported “needs input” event, with a link to the exact session | Later: evaluate a private ntfy service. Its Android client supports self-hosted subscriptions; background delivery depends on its connection/foreground-service behavior and the tailnet remaining reachable. Test on both devices before promising locked-screen delivery. [ntfy Android](https://docs.ntfy.sh/subscribe/phone/) |
| Existing web tools | Open a private editor, repository browser, local-model UI or home dashboard | Optional registered links. These are separate services with their own authentication and resource use; neither native Claude nor Codex needs an added model proxy for this console |

A service entry needs a label, owning host, endpoint, kind, authentication reference and
last successful check. Keep credentials out of the registry and out of share/export files.
Start with manually registered home/office and a few URLs. Add automatic discovery only
if there is a documented, accessible source; do not assume an Android app can read the
Tailscale app's private state or needs a tailnet-admin token. “Host reachable”, “SSH ready”,
“key locked” and “preview stopped” deserve distinct messages, not one online lamp.

Serve keeps a registered web service within the tailnet; the service still needs its
appropriate authorization. This plan adds no public exposure. If a later host helper
trusts Serve's identity headers, its backend must only accept traffic through the trusted
proxy (normally by listening on localhost), as described in the
[Serve identity-header guidance](https://tailscale.com/docs/features/tailscale-serve#identity-headers).

## How to approach the implementation — proposed, not started

**Separate the terminal stream from the dashboard data.** Human typing and explicit
paste travel through the attached SSH PTY. The dashboard needs structured inventory:
host identity, server generation, session/window/pane IDs, labels, directories and a
snapshot timestamp. Terminal-screen scraping would confuse scrollback, tool output and
current state. The UI remains vendor-neutral; Claude/Codex labels are optional metadata.
This console does not create an agent-to-agent bus or a tmux `send-keys` dispatcher.

**Begin the control-channel study with an on-demand host helper over SSH.** It could
answer inventory requests and a small set of named session-management operations without
an always-running HTTP daemon. That requires a reviewed app-specific authentication and
command contract: today's key always opens interactive tmux. A dedicated restricted
helper entry is one candidate; an authenticated service behind Serve is another if event
subscriptions later justify it. No host entry or permission changes are made by this plan.
Do not offer an arbitrary shell-command endpoint merely to fill a menu.

**A menu tap must resolve to the same target when it is used.** Inventory refresh and
selection are separate operations; panes can disappear between them. Revalidate host,
server generation and pane identity immediately before attach or paste. Refresh while
the relevant panel is visible, on explicit pull-to-refresh and after a mutation. Decide
polling versus tmux event subscriptions in the feasibility study. Drafts and tray blocks
stay available without a connection; remote actions show a clear offline/stale state.

**Test companion versus integrated console against this exact interaction:** select a
pane, type with the native keyboard, collect a paragraph, switch hosts and paste it.
Termux's documented RUN_COMMAND intent can launch commands and return results, and
requires both a granted permission and `allow-external-apps=true`. That is useful evidence
for a companion; it does not establish a supported embedded live terminal. Test Galaxy's
F-Droid build and Redmi's Google Play build separately. If one-screen navigation and
typing cannot be achieved through that route, study a native shell with a maintained
terminal component and SSH library. Keep the fork option last until its maintenance cost
is justified. [Termux RUN_COMMAND](https://github.com/termux/termux-app/wiki/RUN_COMMAND-Intent)

**Make collection deliberate and durable.** Accept text through in-app selection, a
foreground Paste action and Android Share-to-app. This fits Redmi too: Android 10+
restricts background clipboard reads to the focused app or default keyboard. Store an
accepted block before acknowledging collection; retain it after paste. A delivery record
may say “pasted” or “uncertain”, but cannot claim the CLI accepted or executed a prompt
without evidence. Cross-device tray sync is a separate future decision; sharing an
export is enough for the first design. [Android clipboard access](https://developer.android.com/about/versions/10/privacy/changes#clipboard-data)

**The first slice should prove one complete working loop:** host/session panel, one live
terminal, the tested key row, a durable tray, detach/reconnect and one registered preview
link. Walk phone and tablet sketches first. Then, after build authorization, prove the
Termux integration and inventory route, prove tray recovery after process death, and only
then add folder browsing or notifications. This keeps the implementation centered on
the user's daily session-switching and text-handling work.

## Persistence is part of the product

Three different lifetimes:

| State | Owner | After Android app/process death |
|---|---|---|
| Claude/Codex process and tmux session | Host | Continues while host/session stays alive; a host reboot is a separate problem |
| SSH connection and terminal viewport | Mobile process | May disappear; reconnect and re-render |
| Collected blocks, unsent draft, order, labels and pending destination | Durable app-private storage | Must restore before the user resumes work |

Persist every accepted tray edit, not merely when the Activity pauses or closes. A
candidate is SQLite with transactions; the mechanism is not locked yet. Android's
[Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)
distinguishes saved UI state from persistent storage: durable user data belongs on disk,
not solely in a ViewModel, saved-state bundle or the Android clipboard.

A block needs an ID, text, created/updated time, optional provenance and order. Destination
needs host identity, tmux server generation/socket, session/window/pane IDs and readable
labels. Names and pane numbers can be reused after server restart; revalidate the target.

“Release” is explicit and keeps a local copy. If the connection dies during a paste, mark
the delivery uncertain and let the user inspect; do not replay automatically or promise
exactly-once delivery from a raw terminal channel. Large/multiline pastes and bracketed
paste behavior need experiments with both native CLIs.

## Design choices to test before building

**Start with a Termux companion feasibility study.** Can a separate app provide the tray,
host/session dashboard and shortcuts while Termux remains the terminal? This may reduce
terminal implementation work, but launching commands alone does not prove that it can
embed, observe or switch an existing interactive terminal.

Compare that with a purpose-built Android shell using a terminal component and SSH, and
with maintaining a Termux fork. Avoid choosing a fork just for branding: it adds updates,
signing and package compatibility work. The [Termux app source](https://github.com/termux/termux-app)
separates its terminal emulator/view components from the application and documents plugin
signing constraints; check the exact integration API, licensing and distribution path
before selecting an approach. Do not replace or uninstall either device's working Termux.

**The host control channel is an open boundary.** Today's device key forces interactive
tmux; it does not expose an arbitrary SSH command API to an Android dashboard. Inventory
and session-management operations need a deliberate design: a narrowly scoped host helper
or another reviewed transport. The proposal above keeps human paste on the attached
terminal channel. Do not silently
remove the forced command to make a prototype easy.

A writable tmux shell grants practical command execution as the host user; the forced
landing session is navigation, not a shell security sandbox. Model approval behavior stays
with the native CLI. A device-specific key/passphrase must not be replaced by the host's
password or a shared phone/tablet secret.

**Modifier keys cross UI boundaries.** Android soft-keyboard Shift did not combine
with Termux's extra-row Tab in the observed Galaxy workflow. Added the supported
Termux `SHIFT TAB` macro as a dedicated `S-TAB` button and a native extra-row `SHIFT`
toggle; the same shared row is now deployed to Redmi (Google Play build
`googleplay.2026.06.21`, compared with Galaxy F-Droid 0.118.1). The app design needs
explicit combined keys, not an assumption that two
separate keyboard surfaces share modifier state. Galaxy's physical taps passed an input-byte test: Tab `09`, Shift+Tab `1b5b5a`
through Termux → SSH → tmux; operator confirmed S-TAB works in the workflow.

**Geometry matters.** A tmux pane has one effective size even with multiple viewers.
Compare active-device sizing and the current largest-view policy using existing
`remote-fit` / `remote-wide`; make the effect on the other attached device visible.

**Compatibility is measured on the Galaxy.** Android 8.1.0 / API 27 / armeabi-v7a are verified. Termux 0.118.1 / F-Droid / arm is also verified. Record the
keyboard, RAM and battery behavior before selecting a stack. Redmi is the newer-device
comparison. No minimum SDK, UI toolkit or persistent-background-service promise yet.

## Planning gates — no implementation in this sitting

1. **Galaxy baseline — completed 2026-09-29.** Its new device key unlocks; both hosts
   passed creation of a disposable session/window, typed marker execution, detach and
   reconnect. Device identity and font are recorded above. Keep sleep/background testing
   separate from this result.
2. **Interaction sketch.** Walk host picker, session tree, console and tray on tablet and
   phone proportions. Decide the small first slice with majkee.
3. **Feasibility brief.** Compare companion / custom shell / fork; test terminal integration,
   control-channel restrictions, keyboard behavior and licensing only after authorization.
4. **Persistence contract.** Specify accepted edit, delivery uncertainty, storage location,
   recovery and explicit deletion. Decide whether export or cross-device sync is wanted;
   local persistence alone is required now.
5. **Build authorization.** Agree scope and location before writing app code.

Future acceptance evidence: Galaxy → each host with its own key; create/rename/switch and
reconnect; both native CLIs render and accept input; 50 mixed text blocks survive rotation,
backgrounding, process death and force-stop/relaunch; Unicode and multiline text survive
copy/paste byte-for-byte; an uncertain delivery never auto-replays; a vanished/reused pane
never silently receives a draft; a concurrent desktop viewer remains usable. Uninstall
and “clear app data” are destructive operations and are outside ordinary restart survival.

## Boundaries

This file preserves the operator's idea and observations, not project canon. Nablarva is
the scope-group's central harness; its `.dev/session/flag.md`, `.dev/session/pulse.md` and
`PROJECT.yaml` were consulted. This sketch does not amend those locks or create a sibling
agent roster, runtime bus, daemon, or own governance layer. Check the existing text-block
work in `applications-in-common` before claiming or duplicating its clipper/composer role.
