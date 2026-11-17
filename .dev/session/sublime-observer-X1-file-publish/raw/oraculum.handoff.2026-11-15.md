# Sublime file publisher — Codex observations and needs

- Author: Oraculum · Codex · direct main, operator majkee
- Date: 2026-11-15
- Scope: bounded read-only investigation, followed by majkee's explicit grant to write this handoff.
- Status: observations and recommendations; not release approval or independent verification of the redesigned publisher.
- Route: main session via --profile oraculum (canary: op-7bf320eb).
- Loaded identity: `/home/hruzam/.germline/agents/oraculum/identity.md`, stamp `88e41067`.
- Loaded binding: `/home/hruzam/.germline/agents/oraculum/binding.codex.md`, stamp `50a6996f`.
- Investigation cwd: `/home/hruzam/ia-sync`; no matching cwd-ancestor Oraculum addendum was found.

**Recommendation — inferred:** the file shape suits this Codex sandbox better than the socket. No agent-triggered refresh is required for my observation needs. The principal missing contract is proof that published text and state belong to the same capture.

## 1. Sandbox facts — observed

Host `hruzam` maps to home in `ia-sync/machines.json`; no Tailscale second-factor verification was performed. `codex --version` reported `codex-cli 0.169.0`, resolved through `/home/hruzam/.npm-global/bin/codex`. The current session declares `workspace-write`, restricted network access and automatic approval review. All investigation probes used ordinary sandboxed commands without escalation.

`XDG_RUNTIME_DIR` was unset in the tool shell. The existing `/run/user/1000` is owned by hruzam with mode `0700`. Its listing and an ordinary file read succeeded; connecting to the existing user D-Bus socket failed before application data was sent.

Exact combined probe:

```sh
XDG_RUNTIME_DIR=/run/user/1000 python -B - <<'PYPROBE'
import os, pathlib, socket
r = pathlib.Path(os.environ['XDG_RUNTIME_DIR'])
print('list:', len(list(r.iterdir())), 'entries')
print('read:', (r / 'pulse/pid').read_text().strip())
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.settimeout(1)
    try:
        s.connect(str(r / 'bus'))
        print('connect: OK; no data sent')
    except OSError as e:
        print('connect:', repr(e))
PYPROBE
```

Observed result:

```text
list: 25 entries
read: 1659
connect: PermissionError(1, 'Operation not permitted')
```

Socket creation itself succeeded in the preceding probe; the denied operation was `connect`. No Sublime socket was contacted. No permission change was needed for file reading. Absolute paths work; variable-based discovery needs the runtime path supplied to the command. The local Codex configuration has `shell_environment_policy.inherit = "core"`; the investigation did not establish why the variable was absent. Persistent environment configuration was neither changed nor tested. The actual Sublime publisher's runtime directory was not independently verified.

**Inferred:** do not require `--add-dir` merely for reading these files in this session; it grants write access and is unnecessary here. Document how readers resolve the producer's runtime directory when the environment variable is missing. Other permission profiles and hosts still need qualification.

## 2. File reading — observed

Ordinary line-range reads work: `sed -n '14,33p'` against the old HANDOFF returned the requested lines. A synthetic memory-backed file of exactly 200,000 ASCII characters read completely and matched its input; a three-line slice returned exactly 300 characters. No persistent synthetic fixture was created.

Exact large-file/range probe:

```sh
python -B - <<'PYPROBE'
import os, subprocess
fd = os.memfd_create('observer-synthetic-read-probe')
data = ''.join(f'{i:05d} ' + 'x'*93 + '\n' for i in range(1, 2001))
os.write(fd, data.encode())
p = f'/proc/self/fd/{fd}'
with open(p) as f:
    s = f.read()
print('memory_file_bytes=', os.fstat(fd).st_size, 'read_chars=', len(s), 'exact=', s == data)
r = subprocess.run(['sed', '-n', '1000,1002p', p], pass_fds=(fd,), capture_output=True, text=True)
print('sed_exit=', r.returncode, 'range_chars=', len(r.stdout))
print(r.stdout, end='')
PYPROBE
```

Results: `memory_file_bytes=200000`, `read_chars=200000`, `exact=True`; `sed_exit=0`, `range_chars=300`, lines 01000–01002.

A second memory-backed fixture containing `'0123456789' * 20000` was printed in full through `exec_command` with `max_output_tokens=1000`. The process exited zero, but the tool reported `original_token_count=50000` and returned 4,103 characters including explicit truncation notices. This is a tool-output budget, not a failed filesystem read or a universal file-size limit.

**Needs — inferred:** 200k is a workable publication cap, not a suitable default response size. Keep state small and text separately readable. Declare encoding, total size, captured range, coordinate units and truncation. Permit character slicing for exceptionally long lines. A caller cannot recover text that the publisher omitted at its cap. No filesystem size ceiling or universal path limit was established.

## 3. Mapping “What Cartan needs” — inferred

Source: `../termbrana-sublime-observer/HANDOFF.md`, section “What Cartan needs”. These assessments concern the proposed shape, not a tested new implementation.

| Original requirement | Assessment | What is needed |
|---|---|---|
| Explicit instance/window/view handles; honest restart, closed-view and stale-handle behavior | Weakened | Retain window/view/buffer IDs and a publisher epoch renewed on restart/reload. Path and PID alone do not disambiguate duplicate views or PID reuse. |
| Live unsaved buffer and complete state, passive observation, bounded output and errors | Weakened | Last-published unsaved text is useful. Retain loading state, selection ranges, visible region, coordinate units, unsupported/error state and explicit truncation, in addition to the proposed caret/viewport fields. |
| Run correlation, readiness/deadlines and safe concurrent readers | Weakened, recoverable | Readers own polling and deadlines; publication must provide consistent captures and bounded delay. The old consumed run-token guarantee is lost. |
| Cross-CLI use, discovery and scoped access | Met in principle | Ordinary files avoid the observed socket obstacle. Operator-controlled publication improves scope. Same-user processes can still read published files; sharing is not per-agent isolation. |
| Reversible installation/removal and host qualification | Weakened; not yet met for the redesign | Carry forward the requirement. The socket prototype's receipts do not qualify the new publisher, its installation or cleanup. |

### Freshness

“Fresh as of the last publish” is sufficient for my observation needs if the claim stays explicit. I do not need agent-triggered refresh. Publish on relevant text, selection, scrolling, loading-completion and sharing changes, with a bounded delay that continuous activity cannot postpone indefinitely. Pure trailing-edge debounce can otherwise starve publication.

An old capture timestamp alone cannot distinguish an unchanged view from a dead publisher. Specify stale-publisher semantics; if current availability is claimed, provide a qualified liveness mechanism. Do not label a retained snapshot as current merely because its files exist.

### Run correlation

Re-reading until a run marker and a newer sequence appear is sufficient only with these conditions:

1. Record the baseline publisher epoch and sequence before starting the experiment.
2. Require caller-generated unique begin and completion markers for that run.
3. Verify the expected path and explicit view identity; a marker alone is not target proof.
4. Accept only a consistent text/state capture; handle epoch changes explicitly rather than comparing sequences across restarts.
5. Apply a deadline and distinguish timeout, loading, partial output, truncation and success.

A newer sequence alone can reflect scrolling. Missing or truncated completion markers cannot count as success. The old one-use, server-consumed run-token property disappears; local correlation is enough for this observation workflow, but does not claim exactly-once consumption across readers.

## 4. Native editor integration — observed capability, connection unverified

The installed executable contains these strings:

```text
Usage: /ide [on|off|status]
Future messages will include your current IDE selection and open tabs.
Open this project in VS Code or Cursor with the Codex extension active.
```

Evidence was obtained by read-only byte searches of:

`/home/hruzam/.npm-global/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex`

The installed package README also points to Codex IDE integration. This establishes native IDE-context capability in the installed build, not a working connection. I did not invoke `/ide`, enable an integration, read selection/open-tab payloads or launch a new session. Sublime support and an active IDE connection remain unverified.

## 5. Discovery — inferred recommendation

Put one conditional pointer in portable `/home/hruzam/ia-sync/codex/AGENTS.md`, deployed through the normal process to `~/.codex/AGENTS.md`:

> For operator-shared Sublime views, read `~/reposoma/raw.guides/sublime-observer/GUIDE.md` before accessing published snapshots.

The existing shared guide should own runtime-directory resolution, the file contract and installation status. It currently describes the socket prototype and must be updated at release. Keep the pointer conditional: discovery is not permission to inspect published content unrelated to the task. No pointer or guide was changed during this investigation.

## 6. Objections and weakest point — inferred

Dropping the socket/CLI removes synchronous capture, centralized wait/error handling, arbitrary requested ranges beyond the publication cap and consumed run tokens. None requires restoring the transport for my stated needs.

**Single weakest point: cross-file consistency.** Atomic replacement of each file does not make text, state, index and `current` one atomic capture. For fixed text/state filenames, include a text digest in state and require readers to read **state → text → state**, accepting only an unchanged publisher epoch/sequence and a matching digest. Read text once into the reader's own memory for that check; subsequent pathname reads may observe another publication. Index/current must bind explicit identities, and races should cause bounded retries or an explicit unavailable result.

Also specify close/unshare cleanup, restart residue, private file permissions, stale-publisher semantics and ambiguous `current` behavior. A single-view pointer must not silently choose among multiple shared views. The new index should describe only operator-shared views; absence does not prove the editor has no other open views.

## Evidence and limits

Read sources included the old bed's HANDOFF, README, STATUS, baseline evidence, relevant capture-function source, the original connector brief/RUNBOOK section, installed Codex package/help/configuration, and the existing shared observer guide. Historical test results were read as prior reports, not rerun or adopted as verification of the redesign.

No live Sublime buffers or private transcript caches were read. No installation, source edit, commit, deployment, STATUS change or new editor session was performed. Investigation Git-status checks showed the same pre-existing unrelated changes at start and finish. This handoff is the subsequent, explicitly requested document write. The redesigned publisher, its normal-profile installation, cross-host behavior and end-to-end qualification remain unverified.
