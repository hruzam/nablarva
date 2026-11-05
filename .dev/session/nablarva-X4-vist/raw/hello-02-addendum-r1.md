from-nabla.Tmux.chatbot ---
From Nabla (Claude) in the Nabla.Tmux chat · 2026-10-23
Addendum r1 to hello-01-contract.md (r0), released by Majkee · proposed, not implemented
Reads with: hello-01-contract.md, vist-01-principle-and-applications.md

# HELLO addendum r1 — the session log and a first .nablarva

r1 changes two things and leaves the rest of r0 standing. First, the bell records every landed
message in a session log before it rings (decided: Majkee's idea, agreed in the voice call).
Second, the channel's files move out of the bed's `_mail/` into a first `.nablarva/`, shaped like
`.claude/` and `.codex/` with the same layering. Each opening of the mail becomes a session folder
that holds its mail, its bindings and its log (decided: the shape and the binding to the session
are Majkee's; the tree and the rules below are proposed). Marks are as in r0.

## .nablarva next to .germline

`.germline` is already a vendor-neutral plane that mirrors `.claude/` and `.codex/` at home and at
project level. A second plane with the same shape needs a dividing line, or the two will grow into
each other. The proposed line: `.germline` is source, meaning what agents are and what they may
load (personalities, method cards, models). `.nablarva` is runtime, meaning what the animal's tools
are configured with and what they record (defaults, signatures, sessions). Agents never edit
`.nablarva` by hand, and the tools never write into `.germline`. The nabla commands could later
become germline models, but their state never lives there. The mail instruction block is
agent-facing, so its long-term home stays a germline card, as r0 says.

(open: folding `.nablarva` into `.germline` as a runtime area. Nabla argues against it, because
gitignored session state would then sit inside a source plane and blur the source and deploy
split.)

## The layering

| Layer | Claude Code | Codex | `.nablarva` r1 |
|---|---|---|---|
| Home scope | `~/.claude/`, personal config for all projects | `~/.codex/`, `config.toml` and profiles | `~/.nablarva/`, machine defaults and the signature registry |
| Relocating home | `CLAUDE_CONFIG_DIR` | `CODEX_HOME` | `NABLARVA_HOME` |
| Project scope | `<repo>/.claude/settings.json`, committed | `AGENTS.md` from the repo root down (project config: verify) | `<bed>/.nablarva/config.conf`, shareable |
| Personal overrides | `settings.local.json`, gitignored | profiles and `-c` overrides | `config.local.conf`, gitignored |
| Finding the project | the working directory at session start | the working directory, up to the repo root | explicit `NABLA_BED`; without it, exit 13 and nothing created |
| Session state | `~/.claude/projects/<slug>/<session-id>.jsonl` | `~/.codex/sessions/YYYY/MM/DD/rollout-<ts>-<uuid>.jsonl` | `<bed>/.nablarva/sessions/<YYYY-MM-DD>.<NN>/events.jsonl` |
| Where that state lives | pooled in the home folder | pooled in the home folder | beside its owner, the bed, and pruned with it |

The vendor columns come from the Claude Code and Codex cards in `raw.settings`.

The shape follows the vendors wherever that costs nothing: one home folder with a relocation
variable, a project folder with a shareable config and a local gitignored one, the same file names
at both levels, and precedence running from built-in defaults through home and project to local.
There is no managed scope, because there is one operator. One home dot-folder instead of the XDG
split is the vendors' choice too. The one XDG rule worth keeping is that runtime files, such as a
future daemon socket, go to `$XDG_RUNTIME_DIR`, never into either `.nablarva`.

It diverges in two places, both on house law. The project is never found by walking up from the
working directory: the tunnel's explicit-only state-path gate (`09c294a`, from Cartan's HANDSHAKE
counter-sign) makes state paths explicit, so the tools take `NABLA_BED` and exit 13 without it.
And session state does not pool in the home folder the way both vendors do it. HANDSHAKE r3 puts
transport state beside its owner, borrowing the owner's lifecycle and slug with no second
registry, and an unattached pool of session folders in `~` would be the orphan vault r3 rules out.
Cross-session browsing, when Termbrana's history view needs it, goes through the project pulse
router that already tracks sessions (RUNBOOK GUIDE; verify how it lists beds), not through a new
index.

## The tree

```text
~/.nablarva/                           home scope, a deploy target
  config.conf                          machine defaults: deadline, breaker, ring timings
  signatures/
    claude-code/cli.conf               binary and process name
    claude-code/2.1.293.conf           calibrated screen patterns for that version
    codex/cli.conf
    codex/0.161.0.conf

<bed>/                                 the owner; its folder name is the slug
  AGENTS.md  CLAUDE.md  .claude/  bin/  as in r0
  .nablarva/                           project scope
    config.conf                        bed overrides, shareable
    config.local.conf                  machine-local overrides
    .gitignore                         sessions/  .tmp/  .seq/  config.local.conf
    .tmp/  .seq/                       staging and ID claims, bed-wide
    sessions/
      2026-10-23.01/                   one mail session, from open to close
        OPEN                           present only while open
        session.conf                   owner slug, tmux server PID, host, opened, closed
        bindings/claude.conf           pane, pane PID, CLI, version, signature used
        bindings/codex.conf
        mail/claude/{inbox,archive}/   the temple bus shape, as in r0
        mail/codex/{inbox,archive}/
        events.jsonl                   the session log; one writer, the bell
```

The screen patterns move out of r0's per-seat `bell.conf` into a registry keyed by CLI and
version, named for what the VIST brief calls them: signatures. The home scope is a deploy target:
its source lives in ia-sync and deploys here, the rule the HANDSHAKE mount table sets for
`~/.codex` (open: or relocate it into my-env-sync with `NABLARVA_HOME`, the lever the Claude Code
card uses for `~/.claude`). So `nabla-mail calibrate` proposes an entry and prints it, and the
operator saves and deploys it. Tonight, saving straight into the home folder is fine; the deploy
discipline starts once the gate passes.

Staging and ID claims are bed-wide, so IDs never repeat inside a bed and staging stays on the
inbox's filesystem, which the atomic rename needs. Nothing is pre-created for parts that do not
exist yet: Antensor, Termbrana and the daemon add their folders on first use (Foreman rule), and
each new writer gets a file of its own (the `_bus` single-writer law).

## How a session binds

A mail session is one opening of the mail in one bed. `nabla-mail open` creates the next
`sessions/<date>.<NN>/` with `OPEN` and a `session.conf`, and `close` removes `OPEN` and stamps the
closing time. At most one session per bed is open, and the tools find it as the one folder holding
`OPEN`: none means exit 10, and more than one is refused as a broken bed with exit 20. So the
environment stays the same across sessions: `NABLA_BED`, which replaces r0's `NABLA_MAIL`, and
`NABLA_SEAT`. A CLI can keep running from one session into the next. For the live tests, fresh CLI
sessions are still better, because a cross-runtime primitive is verified from a fresh session of
the other runtime (HANDSHAKE shared invariant, Sella L8).

The session holds four bonds, each with its own failure rule:

| Bond | Recorded in | Goes stale when | Then |
|---|---|---|---|
| session to owner | containment; the bed's folder name is the slug | the bed is pruned | the session goes with it, after anything worth keeping has graduated |
| session to tmux server | `session.conf`: the server PID | tmux restarts | the bell stops ringing; the operator closes and opens a new session |
| seat to pane | `bindings/<seat>.conf`: pane ID and pane PID | the pane dies or the CLI restarts | the bell holds that seat; the operator re-binds |
| seat to CLI version | the same file: version and the signature used | the CLI is upgraded | no signature for the new version, so the bell holds the seat until it is calibrated |

The pane PID works as an occupant check only if the launch starts the CLI as the pane's own
command, not under a shell, so that a restart changes it. `bind` reads the version from
`<binary> --version` right after the start, while the binary on disk and the running process still
agree. Pin both CLIs for the length of a session (Claude Code: `DISABLE_AUTOUPDATER=1`; verify).

The fourth bond is the reason for the registry. In r0, a CLI upgrade silently left the old patterns
in place. In r1, a new version has no signature, so the bell holds the seat instead of typing on a
screen it no longer knows. That is also where the canary plugs in later: it writes the signature
for a new version after its replay passes.

A fifth bond is optional (open): pointers to each seat's own vendor session, meaning the Claude
transcript under `~/.claude/projects/<slug>/` and the Codex rollout under `~/.codex/sessions/`, for
replay and VIST cross-checks. Finding them is vendor data, so it waits for the registry, and the
pointers are recorded, never copied.

## The session log

The ring gains a step in front of r0's eight:

| Step | Check | On failure |
|---|---|---|
| 0. record | parse the landed file: the envelope is complete, the ID matches the file name, and `to` matches the inbox. Append one `landed` line with the envelope, body, SHA-256 and size | log `malformed` with the path, never ring, alert |

```json
{"ts":"2026-10-23T19:35:13+02:00","event":"landed","id":"claude.hello.2026-10-23.01","seat":"codex","envelope":{"from":"claude","to":"codex","scope":"hello","in_reply_to":"none","expects_reply":"yes","deadline":"2026-10-23T19:45:00+02:00","sent":"2026-10-23T19:35:12+02:00","host":"office"},"body":"hello from claude","sha256":"…","bytes":231}
```

The bell is the log's only writer, so messages and ladder events sit in one file in exact order.
The mail file stays the source of truth. The bell also watches `archive/`: when a file arrives
there, it logs `archived`, which is HANDSHAKE's consumption stamp made visible, and compares the
hash with the landed one. A mismatch is logged and alerted, never fixed.

The log outlives the mail inside its session: the Cinderella drain can empty inbox and archive
while the log keeps the exchange. It does not outlive the session. Before the bed is pruned, what
matters graduates to its evidence home, for example the log of a passing run as the evidence behind
a dated finding. This narrows what Nabla said in the voice call: records outlive the mail drain,
not the session.

The log sits under `sessions/`, which is gitignored, because bodies may carry secrets. On start,
the bell catches up first: any inbox file not yet in the log is recorded and rung, oldest first. A
crash can leave a torn last line, which readers skip and the bell notes on restart.

The ladder becomes `landed`, `rung`, `archived`, then `answered` or `timeout`, with `malformed`,
`mismatch`, `held`, `stuck`, `paused` and `stale` as side states. `nabla-mail log` prints the open
session's timeline, `nabla-mail log <id>` prints one exchange from the log alone (opener, answer
and ladder), `--session <date>.<NN>` reads a closed session, and `--json` prints the raw lines.

## What r1 changes in r0

| r0 section | Change |
|---|---|
| The bed | `_mail/` moves to `.nablarva/sessions/<date>.<NN>/mail/`, which closes r0's question about reusing the `_mail` name |
| nabla-send and nabla-read | `NABLA_MAIL` becomes `NABLA_BED`, and exit 13 names it; exit 15 searches the open session only; IDs are unique per bed |
| nabla-bell | step 0; it also watches `archive/`; it catches up on start; the occupant check uses the pane PID; it holds a seat whose version has no signature |
| nabla-mail | `open` creates the next session and refuses while one is open; `bind` reads the version; `calibrate` proposes a signature; `log` is new |
| Tests | F9 to F13 below |

## New tests

| Test | Scenario | Passes when |
|---|---|---|
| F9 | the bell restarts with two unlogged messages waiting | both are logged and rung in order, and nothing already logged repeats |
| F10 | a malformed file is renamed into an inbox | `malformed` is logged with its path, nothing rings, the operator is alerted |
| F11 | a landed file is edited by hand before it is archived | `mismatch` is logged and alerted, and the file is left as it is |
| F12 | the mail folders are drained after L1 | `nabla-mail log <id>` still prints the whole exchange |
| F13 | a seat is bound with a CLI version that has no signature | the bell holds the seat and asks for calibration |

## Open choices added by r1

Whether `.nablarva` stays its own plane or folds into `.germline`. Deploying the home scope from
ia-sync, or relocating it with `NABLARVA_HOME`. The session key: date and sequence, or the owner's
slug inside the name as well. The word `bindings`: in `.germline` a binding is a per-vendor render
file, while here it is a seat's attachment to a pane, as with Termbrana's pins. Key-value `.conf`
files over TOML: kept because the tools are zsh and nothing needs nesting yet. Whether the
vendor-session pointers are worth having.

Basis: this chat on 2026-10-23 (the JSONL log, its binding to the session, the `.nablarva` shape);
hello-01-contract.md r0; the Claude Code and Codex cards in `raw.settings`; HANDSHAKE r3 with
Cartan's counter-signs and the `09c294a` state-path gate; `_mail/README.md`;
`raw.guides/bus/GUIDE.md`; the `.germline` notes. None of those sources is changed.
