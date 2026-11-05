---
kind: issue-report
date: 2026-10-06
project: nablarva
reported_by: cartan
writer_host: home
affected_host: office (hruzam-120922)
scope: Office memory pressure, tmux views, zsh process growth and architecture proposals
authority: majkee requested this file under Nablarva .dev/issues
---

# Office memory pressure and tmux zsh process inventory

Office recovered without rebooting after Firefox was closed with SIGTERM. Majkee
confirmed desktop and keyboard recovery. Follow-up checks found **little tmux server
or scrollback memory**, **many identifiable prompt helpers**, and **one unusually large
Konsole zsh process**. A growing cache or process leak has not been demonstrated.
The missing swap remains a machine-level problem for ia-sync; Nablarva can use these
observations when investigating session visibility and lifetime.

## Recovery and recurrence

On 2026-10-06 at 04:25 CEST, office had 15,753 MiB RAM, **192 MiB available and zero
swap**. Load was **105.04 / 131.53 / 116.02**. Memory pressure `some avg10` was 17.81;
I/O pressure `some avg10` was 95.98. Firefox, KDE, Sublime and several agents appeared
in D-state. Tailnet SSH and Tailscale probes timed out. Direct LAN ping responded;
a longer direct SSH attempt reached the host after shorter attempts failed.

Cartan verified the office host and Firefox executable, then sent SIGTERM to Firefox
parent PID 1321473. That PID is historical, not a future kill target. At 04:38, available
RAM was **2,154 MiB**, one-minute load **0.18**, memory/I/O pressure avg10 and avg60
**0.00**, and no D-state processes in the follow-up snapshot. Fresh tailnet SSH passed;
Tailscale ping was 3 ms. Uptime remained 14 days; agent sessions and tmux panes survived.
At 05:10 available RAM was 3,148 MiB, swap still zero, one-minute load 0.40.

Systemd restarted watchdog-stalled journald at 04:24:50; journald replaced unclean files
and reported lost kernel-log messages. Storage failure was not established. A diagnostic
vmstat sample was already 95–96% CPU idle before Firefox was terminated, so the host's
responsiveness fluctuated. Closing Firefox was sufficient for recovery; it does not prove
Firefox was the sole cause. A similar no-swap stall was recorded on 2026-10-01.

## Tmux views and retained history

At the 05:11:33 CEST snapshot:

| Server | Listed pane rows | Unique pane IDs | Retained scrollback lines |
|---|---:|---:|---:|
| default | 66 | 35 | 605 |
| ovitmugen | 16 | 16 | 2 |

Grouped `--left` sessions share windows: the duplicate listings do not represent
duplicate workloads. The ovitmugen panes held 8 tmux clients and 8 Python processes.
The two tmux server processes used **12,556 + 6,524 KiB RSS**, about **18.6 MiB combined**,
in the 05:10 snapshot. Large tmux scrollback/cache buildup was not evident in these reads.
A detached view alone is not evidence that its agent is idle or safe to close.

## Zsh memory and helper ownership

The earlier incident snapshot contained 262 zsh processes. At 05:11:33, **261 zsh
processes across 65 TTY labels** used 1,897,372 KiB summed RSS and **1,258,100 KiB PSS**
(about 1.20 GiB). PSS apportions shared memory; summed RSS can count shared pages repeatedly.

| Immediate parent command | Zsh processes | Total PSS in KiB |
|---|---:|---:|
| systemd | 196 | 272,466 |
| tmux server | 35 | 231,444 |
| konsole | 29 | 751,119 |
| zsh | 1 | 3,071 |

Of the 196 shells parented by user systemd PID 722, open FIFO descriptors identified
**65 gitstatus helpers and 65 Powerlevel10k workers**. All 130 named live zsh owner PIDs;
none of those identified owners was absent. FIFO names ended in `(deleted)`, but the
processes still held them open: that label alone does not demonstrate a leaked process.
**66 systemd-parented shells remain unclassified** by this limited descriptor check.
Across all 196, wait channels were poll (120), sigsuspend (66), and pipe write (10).
Some helpers had existed for roughly the host's 14-day uptime; age alone is insufficient
to classify them as redundant. Many of the apparent extra shells are prompt-related.

The largest shell, PID **4165599**, was a direct Konsole child on **pts/38**, approximately
31 hours old, with **503,116 KiB RSS / 498,799 KiB PSS** (about **487 MiB PSS**). It was
waiting in poll. Other large shells included PID 3185088 (Konsole, 130,829 KiB PSS) and
PID 2282710 (tmux, 116,058 KiB PSS). Their internal allocation causes remain unknown.
These are observation identifiers, not cleanup instructions; recheck identity on reuse.

## History and completion caches

Office's zsh startup sources Manjaro's zsh configuration and Powerlevel10k prompt.
The installed configuration sets `HISTSIZE=10000`, `SAVEHIST=10000`, history at
`~/.zhistory`, and completion cache at `~/.zsh/cache`. Metadata-only checks found:

- History: **131,119 bytes**; no history contents read.
- Completion dump `~/.zcompdump`: **54,834 bytes**.
- Completion cache `~/.zsh/cache`: **40 KiB allocated on disk**.

These files are small in this snapshot. Their sizes alone do not establish the cause of
the large shell's memory or rule out growth in shell-local arrays, plugin state, history objects or another
allocation. No time series or in-process allocation inspection was collected, so a
growing zsh cache remains a hypothesis rather than a finding.

## Architecture proposal alongside zram

Majkee asked whether the zsh architecture, services and applications can be updated
alongside zram. **Yes: reduce work repeated in each shell and make process lifetime
and resource ownership explicit.** This section is a proposal for review, with no
runtime configuration or architecture lock applied.

Zram stores compressed pages in RAM and can provide swap headroom. It complements
reducing the working set; it still consumes RAM and its benefit depends on compression.
See the [kernel's zram documentation](https://docs.kernel.org/admin-guide/blockdev/zram.html).
Fresh office checks on 2026-10-06 confirmed running kernel `7.1.3-1-MANJARO`, an absent
`/usr/lib/modules/7.1.3-1-MANJARO` directory, no loaded zram module and no swap entries.
The existing setup sheet's prerequisite remains unresolved. The intended route is the
operator's scheduled kernel reboot, then a fresh module check; this report performs no reboot.

### Existing structure to build on

- Office's `.zshrc` sources Manjaro configuration and Powerlevel10k **before**
  `~/.config/zsh/config.zsh`, then project-switcher and git-lifecycle. Neither a user
  `.zshenv` nor `.zprofile` existed in the 05:27 CEST check. Interactive startup is
  already separated from normal non-interactive zsh invocation; broad startup pollution
  of every script has not been demonstrated.
- `config.office.zsh` eagerly sources the `ai`, `session`, `system` and other scope
  signposts. These load multiple engine definitions. Many commands already call external
  Python programs, and project-switcher already loads project toolkits on demand.
  Loading these definitions has not been shown to explain the 487 MiB shell.
- `ai/base.zsh` also declares a non-interactive git-hook consumer. Any loader change
  must preserve that caller and the existing bash/zsh shared processors.
- `_ts_header`, called at shell startup, runs `tailscale ip -4` without a timeout
  before its timeout-protected `tailscale status` pipeline. The advertised two-second
  bound therefore does not cover the whole header. This is a concrete startup-latency
  candidate, not an established cause of the memory stall.
- Office already has systemd-managed KDE application units and a running
  `piql-mcp.service`. User unit files include the weekly oneshot `harness.service`/
  `harness.timer` and three `claude-rc-*.service` files; file presence does not establish
  that all are running. Reuse existing ownership instead of introducing duplicate services.

### Proposed boundaries

| Layer | Proposed change | Constraint or evidence needed |
|---|---|---|
| Environment | Keep shared PATH and host facts small; give scripts and services their required environment explicitly. | Preserve the existing interactive boundary; moving the full config into `.zshenv` would expand its reach. |
| Human and worker shells | Add an explicit, opt-in lean worker profile with a simple prompt and no unused prompt plugins or startup dashboard. Keep the full human profile available. | Select the profile before Manjaro's prompt loads. A check only inside `config.zsh` is too late. A tmux pane or PTY alone does not identify a worker. |
| Commands | Trial lazy loading for one infrequently used command family; preserve current alias names and engine ownership. Keep `cd`, exports and shell state changes in shell functions. | Native zsh autoload or a family loader are options, not a selected new convention. The gaveled one-engine-per-scope / keyboard / signpost rules need an agreed amendment if the chosen layout changes them. |
| Long-running tools | Consider an on-demand user service for the existing Tailscale dashboard, keyed by host/port, with status and logs. Keep short commands as ordinary programs. | Current `_ts_dash_start` explicitly launches Python and owns PID verification/stop behavior; preserve its user-facing lifecycle. Inspect the existing service inventory before migrating anything. |
| Applications and agents | Attribute memory to the existing application units and to actual agent process trees; consider launch-time user scopes for new workloads after the boundaries are verified. | Client-owned stdio processes retain their client lifetime. Wrapping a tmux attachment does not isolate work already running under its server. PTY, signals and reconnect behavior must survive. |
| Caches and helpers | Give any newly introduced cache a size/expiry rule and helpers an owner plus a tested exit path. | Existing disk caches were small and the 130 identified helpers had live owners. Repeated start/exit measurements must demonstrate growth before cleanup is prescribed. |

The startup-file distinction is documented in the [zsh startup reference](https://zsh.sourceforge.io/Doc/Release/Files.html);
the [function reference](https://zsh.sourceforge.io/Doc/Release/Functions.html#Autoloading-Functions)
describes loading a function on its first call. These are available mechanisms; their
memory benefit for this configuration remains to be measured.

For application containment, first collect cgroup membership and memory accounting.
Later, a measured per-workload `MemoryHigh` can throttle/reclaim memory; a hard
`MemoryMax` can trigger an OOM kill within its unit. Avoid applying a guessed limit
to the shared tmux server or the whole desktop. No limits are proposed numerically or
applied here. See upstream [systemd resource-control documentation](https://github.com/systemd/systemd/blob/main/man/systemd.resource-control.xml)
and [transient service/scope documentation](https://github.com/systemd/systemd/blob/main/man/systemd-run.xml).

### First implementation slices and acceptance evidence

1. Bound the whole `_ts_header` probe and make it optional in the worker profile.
   Verify a missing/unresponsive Tailscale endpoint cannot delay the prompt beyond the
   chosen budget. This is a latency fix, with no promised RAM saving.
2. Compare disposable full and lean interactive shells on office, using the same
   directory and workload. Measure time to first prompt, shell-plus-helper PSS and
   process count. Repeat creation and normal exit several times; helpers must return
   to baseline. Use an isolated test terminal/server and launch no paid agent turns.
3. Only then trial one lazy command family. Check first and repeated invocation, its
   aliases/help, directory/environment effects, git-hook compatibility where relevant,
   and idempotent loading. Publish measured savings before expanding the migration.
4. Map one candidate background tool's current lifecycle to its existing or proposed
   service. Verify start/status/stop, logs, duplicate-start behavior, reconnect and
   descendant cleanup on a disposable instance before touching the live instance.
5. Track the large shell's PSS over a reproduced workflow with the operator. A lean
   startup profile alone cannot establish that the unexplained retained memory is fixed.

Author changes through ia-sync's compose-first deployment path and respect host-specific
configuration ownership. Nablarva's session owner reviews any change affecting pane
identity, busy detection or process lifetime. Scope signposts remain side-effect-free;
keyboard files retain their aliases-only contract. No new global daemon or automatic
session killer is part of this proposal.

## Bounded follow up for the receiving owner

1. Identify the 66 unclassified helper shells and their live owners using read-only
   process/descriptor relationships. Separate prompt helpers from retained agent sessions.
2. Inspect the large Konsole shell with the operator: sample its PSS over time and compare
   a controlled disposable shell with the same configuration. Establish which operation
   causes growth before changing history limits, prompt plugins or cleanup behavior.
3. Attribute the incident's 16 `claude`, 7 `codex`, 16 `npm exec @gitkr` and 32 `gk`
   processes to sessions and descendants. Process counts alone do not prove duplicates.
4. Keep tmux's unique pane identity and existing busy/idle safeguards. Any cleanup or
   lifecycle change needs a specific demonstrated target; this report performs none.

Coordinate Nablarva-side work with `ovitmugen-01-basement`'s owner. Machine-level zsh
changes and swap setup belong to ia-sync. This report does not change project gates,
STATUS, locks, deployment configuration or the active agents.

## Evidence and reproduction

- Recovery: `~/ia-sync/journal.host-cleanup.md`, HOME 2026-10-06, pushed in ia-sync
  commit **d7e4751**. Earlier incident: `~/reposoma/_cold-start/issues/ISS.office-no-swap-memory-stall.2026-10-01.md`.
- Existing swap setup sheet: `~/ia-sync/.dev/session/zram-guard-office/pad.1-zram-office.md`.
  Its kernel/module and sudo prerequisites require a fresh check; recovery did not apply it.
- Current Nablarva owner: `~/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/STATUS.md`
  and `~/unikuklatrix/nablarva/.dev/session/ovitmugen-01-basement/RUNBOOK.md`.
- Process inventory: `ps -eo pid,ppid,sid,stat,rss,etimes,tty,comm`; PSS from each zsh's
  `/proc/<pid>/smaps_rollup`; helper identification from `/proc/<pid>/fd` symlink targets
  matching gitstatus/Powerlevel10k FIFO names, with referenced owner PIDs checked live.
- Pane counts: `tmux -L <server> list-panes -a` with pane ID, pane PID, command and
  history_size fields; deduplicate by pane ID separately for each server before summing.
- Cache checks used configuration lines and `stat`/`du`, not history contents. Shell
  command payloads were withheld from diagnostic output.
- Architecture inspection: ia-sync `zsh/config.office.zsh`, `zsh/ai/base.zsh`,
  `zsh/session/base.zsh`, `zsh/system/tailscale.zsh`, `zsh/system/dashboard.zsh`,
  `zsh/project-switcher.zsh`, `zsh/AGENTS.md` and
  `zsh/guides/guide-for-builder.md` (Architecture rules). The first four files had
  matching SHA-256 hashes between the home table, office table and office live copy.
  Office's `.zshrc` source lines and user-service metadata were read remotely.
- Git context: home ia-sync `d7e4751`, office ia-sync `074ac90`; office has concurrent
  tracked and untracked work. Both Nablarva clones were at `3547e3c` during this update.
  Only this report is mirrored; no repository-wide synchronization or office reset was
  performed. At 05:27:48 CEST office's memory-pressure avg10/avg60/avg300 were all zero.

The transcript's initial exit code 1 came from an empty `rg --files _mail` search in
a batch whose preceding reads/checksums succeeded. Matching file hashes established
equality of two instruction files only, not whole-repository equality. That display
ambiguity is separate from the measured memory pressure.
