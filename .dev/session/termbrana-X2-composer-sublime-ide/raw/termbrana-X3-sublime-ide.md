from-nabla.Tmux.chatbot ---
From Nabla (Claude) in the Nabla.Tmux chat · 2026-10-18
Personal design brief requested by Majkee · proposed, not implemented
Reads with: the Sella-v.0.1 collection (README, brief.myshell, note.myshell.history-and-attachments)
and vist-01-principle-and-applications.md

# Termbrana 04 — Sublime as the composing IDE

Marks used below: *decided* means Majkee chose it in conversation; *proposed* means Nabla's
suggestion, open to kick, bend or veto; *open* means not settled; *verify* means tool or vendor
behaviour not checked against current documentation in this sitting. Unmarked design statements
are proposed.

## The recommendation

Make Sublime the place where Majkee composes, checks and watches exchanges, not the place that
decides or delivers. The plugin reads the controller tables and the exchange workspace, writes
only draft files, and talks to one local daemon over one Unix socket. It never calls tmux, never
appends to the event history, and never stores pane identities in the document. Build the parts
that carry no authority first; sending stays behind its own authorization, as the Sella-v.0.1
collection already requires.

## Decided in this chat

Sublime comes first. Zed and possibly Lite XL may follow, and VS Code matters least. Termbrana
gets its own syntax with its own opening and closing tags, the way HTML has `div` and its end.
Typing a trigger opens options drawn from the .germline controllers, and a choice either inserts
a template or starts a behaviour such as an agent run or a tool. A prompt is checked before it
leaves. Pseudo-buttons inside the buffer act on blocks. Sent prompts are kept as JSONL history
and can be brought back into a view. Pins mark sequence blocks with notes for the CLI, and a CLI
can be attached to a block from the dashboard. The editor link is a Unix socket. The message
format, parser and buffer are already engineered, so this brief does not redesign them. The
logic lives on the server side, behind typed events that can grow later.

## Fit with Sella-v.0.1

brief.myshell wants Majkee able to do the agent's work in Sublime with the agent absent. Its
illustrative operations map onto Sublime surfaces like this:

| Sella operation | Sublime surface | Side effect |
|---|---|---|
| Compose | the exchange document in Termbrana syntax, with completions from the controller tables | draft file only, by Majkee's own save |
| Inspect/check | inline annotations and an Inspect panel: parsed fields, selected controller and function, missing inputs, limits | read-only |
| Render/plan | a Render panel: the exact outgoing prompt, the route outcome (native, manual, unsupported, unqualified), unmet requirements | preview only |
| Collect return | the pending and history view | none from Sublime; the owner records |
| Prepare fold | a fold preview panel | preview only |

The plugin displays what the existing parser and loader produce and does not reimplement them.
That keeps one truth, and the agent-absent path runs the same code as the Sublime path.

## Changed against this chat

Reading the Sella-v.0.1 collection changes four suggestions made earlier in this chat and raises
one tension.

A pin names a binding, a role or runtime such as Astrobley or Codex, never a pane. Attachments
live in the workspace with revisions: a dead session makes an attachment stale, name reuse must
not silently reconnect it, and rebinding creates a new revision (note.myshell). Attaching a CLI
from the dashboard therefore creates or revises the binding's attachment in the workspace; the
pin's text does not change. Pane IDs written into the document would make it a second and soon
stale source of attachment truth.

Sublime is not an event writer. The history has one writer; Sublime asks, and the writer
appends.

Bringing an entry back from history opens a new draft revision. Frozen renders and the history
itself are never edited.

Delivery uses the doorbell design: the prompt lives in a file, and the pane receives a short,
known nudge. The paste-buffer route suggested earlier is dropped.

The tension is that Sella's parser reads the declared header and keeps the body as text, while
pins and Termbrana tags live in the body. Either the header declares the blocks by ID and the
body tags are anchors the editor displays, or the parse rule is extended to a declared block
grammar (open).

## Architecture

```text
  Sublime: Termbrana package                 office machine
  +---------------------------+              +------------------------------+
  | syntax and completions    |    NDJSON    | daemon, one socket           |
  | inspect and render panels | <----------> |   router, handler registry   |
  | pending and history view  | Unix socket  |   single history writer      |
  | phantoms as buttons       |              |   controller       (gated)   |
  +---------------------------+              |   actuator         (gated)   |
               |                             +------------------------------+
               | writes drafts/ only              |                  ^
               v                                  | doorbell         | vist.* observations
  exchange workspace                              v                  |
  workspace.json, drafts/,                    tmux panes --------> Antensor
  prompts/<id>/<rev>.md,
  events.jsonl, index.json
```

The workspace layout is note.myshell's illustrative one. Sublime reads `index.json` and
`events.jsonl` for the pending views and writes only under `drafts/`.

## The socket link

This is the part asked for directly.

The socket sits at `$XDG_RUNTIME_DIR/nabla/nabla.sock` in a directory with mode 0700. Keep the
path short, because Linux caps a socket path at 108 bytes. On Manjaro the runtime directory is
removed when the user's last login session ends; if no session stays open on the office machine,
`loginctl enable-linger` keeps it (verify).

On start, the daemon first tries to connect. If that succeeds, another daemon owns the socket
and the new one exits. If the connection is refused, the file is stale: unlink it and bind.
Unlinking blindly would steal a live daemon's socket.

Frames are one JSON object per line, carrying the existing message format unchanged, with a
maximum line length and buffering for partial reads. A client opens with `hello` (client name,
protocol version, capabilities, subscriptions), the daemon answers with `welcome`, and every
reconnect repeats the handshake. Every message has an ID, replies carry the ID they answer, and
the daemon records which client sent what. Each client gets a bounded queue; a client that falls
behind is dropped and resynchronises on reconnect, so the daemon never blocks. Clients reconnect
with backoff.

In the early stages Sublime sends requests (inspect, render, list pending, attach) and receives
results, workspace changes, receipts and `vist.*` observations. Intents that lead to delivery
arrive only in the last stage.

If Sublime runs somewhere other than the office machine, forward the socket over SSH; OpenSSH
has forwarded Unix sockets since 6.7. Add `-o StreamLocalBindUnlink=yes` so a stale local socket
does not block the next session, and carry draft content inside messages, because the office
machine's paths are not the editor's (open whether this case matters).

The daemon mounts as one pipe and gate in the zsh router and is one of the few bricks that react
to events. A systemd user unit with socket activation could own the socket's lifetime and
restarts instead, but it would live outside the router (open).

From zsh the built-in socket module is enough:

```zsh
nabla-hello() {
  zmodload zsh/net/socket
  zsocket "$XDG_RUNTIME_DIR/nabla/nabla.sock" || return 1
  local fd=$REPLY reply
  print -r -- '{"kind":"hello","client":"zsh","proto":0}' >&$fd
  read -r -u $fd reply && print -r -- "$reply"
  exec {fd}>&-
}
```

The Sublime side as an illustrative skeleton, not installed:

```python
# termbrana_link.py: illustrative skeleton, not installed
import json
import os
import socket
import threading

import sublime

SOCK = os.path.join(os.environ.get("XDG_RUNTIME_DIR", "/tmp"), "nabla", "nabla.sock")
_link = None


class Link(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.halt = threading.Event()
        self.sock = None

    def run(self):
        delay = 0.5
        while not self.halt.is_set():
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.sock = sock
            try:
                sock.connect(SOCK)
                self.send({"kind": "hello", "client": "sublime", "proto": 0})
                delay = 0.5
                self.read_lines(sock)
            except OSError:
                pass
            finally:
                sock.close()
            self.halt.wait(delay)
            delay = min(delay * 2, 5.0)

    def read_lines(self, sock):
        buf = b""
        while not self.halt.is_set():
            chunk = sock.recv(65536)
            if not chunk:
                return
            buf += chunk
            if len(buf) > 1_048_576:
                return  # oversized line: drop the connection
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                try:
                    msg = json.loads(line.decode("utf-8"))
                except ValueError:
                    continue
                sublime.set_timeout(lambda m=msg: on_message(m), 0)

    def send(self, msg):
        # real code queues messages while disconnected
        self.sock.sendall((json.dumps(msg) + "\n").encode("utf-8"))


def on_message(msg):
    pass  # main thread: update panels, phantoms and regions here


def plugin_loaded():
    global _link
    _link = Link()
    _link.start()


def plugin_unloaded():
    if _link is not None:
        _link.halt.set()
        try:
            _link.sock.shutdown(socket.SHUT_RDWR)
        except (OSError, AttributeError):
            pass
```

It encodes two scars. The socket lives on a background thread and touches the interface only
through `sublime.set_timeout`, and `plugin_unloaded` stops the thread; without it, every plugin
reload during development leaves another live connection behind.

## Editor features in Sublime terms

| Feature | Sublime mechanism | Note |
|---|---|---|
| Termbrana syntax | `.sublime-syntax` version 2 that `extends` Markdown; the grammar knows only the tag shape | the tag vocabulary comes from the controller tables at runtime |
| folding | syntax-based folding where the installed build supports it (verify), otherwise `view.fold` from the plugin | |
| auto-close and snippets | `on_query_completions` returning `CompletionItem.snippet_completion` | generated from the controller tables |
| trigger options | `window.show_quick_panel` with `QuickPanelItem`, in two levels: controller, then function or option | inserts a template or sends a request |
| inline checks | `view.add_regions` with annotations and gutter icons | results from the existing checker |
| pseudo-buttons | a `PhantomSet` with minihtml links and `on_navigate` | inspect and render now, ring later |
| pins | tags in the document with gutter icons; status from `index.json` | a pin names a binding |
| pending and history | a read-only view or output panel built from `index.json` and `events.jsonl` | the six pending views in note.myshell |
| live agent edits | Sublime reloads changed files, and `"mini_diff": "auto"` marks changes against git in the gutter | |

Key bindings carry a selector context, so triggers fire only in Termbrana documents. Target the
Python 3.8 plugin host through `.python-version` and keep the code 3.8-compatible, so it also
runs unchanged on any newer host.

The tag sigil is open. Whatever it becomes must not collide with Markdown, HTML, Blade (`{{ }}`
and `@directive`), Twig, or the `<<` of PHP and bash heredocs, and it should be line-anchored and
easy to type. A placeholder only:

```text
§pin 1 bind=astrobley
Review the importer against the B2B contract.
§end
```

## Staging, aligned with the Sella gates

| Stage | Builds | Condition |
|---|---|---|
| A | syntax, folding, completions from the controller tables | none; read-only editor convenience |
| B | inspect, render and fold preview panels over the existing parser | Termbrana phases 0 to 2 in place |
| C | the daemon, the socket link, the pending and history view, `vist.*` status | read direction only |
| D | ring and send, with approval for each action first | its own delivery authorization |

brief.myshell makes editor integration earn its place through the pilot's evidence. Stages A and
B are proposed as the minimum that makes the pilot easier to run by hand; whether that already
counts as editor integration under the gate is Majkee's call (open).

## Other editors

One daemon, one socket, and one thin adapter per editor, each declaring its capabilities in
`hello` so the daemon never sends a view something it cannot show. Lite XL's plugins are Lua
with no socket API as far as known, so its adapter would talk through a helper process such as
socat over standard input and output (verify). Zed's extensions run sandboxed and, as far as
known, cannot open arbitrary sockets, which leaves the Agent Client Protocol or terminal tasks
as its routes (verify). VS Code's Node runtime opens Unix sockets natively; it is simply the
heaviest. The order is decided; the mechanisms need verifying.

## Prior art and fit

| Prior art | Lesson | Fit |
|---|---|---|
| SendCode package | sends selections from Sublime to tmux and terminals | shows a send path but bypasses the doorbell and owner rules: study it, do not adopt it |
| Terminus package | a terminal inside Sublime, with a command API | not needed, since tmux stays the live workspace |
| LSP package | a mature asynchronous client living in the plugin host | a direct reference for the link's structure |
| Language Server Protocol | handshake, capabilities, versioned messages | `hello` and `welcome` |
| systemd socket activation | owns socket lifetime, restarts and logs | optional, outside the zsh router |

## Scars to keep in view

Never block Sublime's main thread. Phantoms and regions vanish when a view closes, so durable
state belongs in files. Sublime can save outside any writer lock, so agents write new files and
never the open document; if an agent does change an open file on disk, Sublime silently reloads a
clean view but asks about a modified one. A socket file left by a crash blocks the next bind, and
a blind unlink can take over a live daemon's socket.

## Open choices for Majkee

The body-tag tension. The tag sigil and the trigger key, since a slash at line start collides
with paths in prompts. The reading unit, whole exchange or message file, which Termbrana phase 0
settles first and which decides what one Sublime view shows. Where Sublime runs relative to
tmux. Daemon supervision, as a zsh brick or a systemd user unit. Whether stages A and B count as
editor integration under the Sella gate.

Basis: this chat on 2026-10-18; the Sella-v.0.1 collection (README, brief.myshell,
note.myshell.history-and-attachments); vist-01-principle-and-applications.md. This brief changes
none of those sources.
