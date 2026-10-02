---
from: Cartan
to: ovitmugen-00-console / Trajectory
date: 2026-10-01
host: office / hruzam-120922
kind: operator-requested feedback
status: keyboard workaround confirmed; physical wheel verification pending
authority: majkee requested this exact file and destination
---

# Pane history: keyboard works; wheel repair is not yet proven

Majkee could not scroll this Codex pane far enough back to read and answer the
Jev discussion. Cartan delegated a bounded live repair. Entering tmux copy mode
restored keyboard history navigation; majkee then explicitly reported:

> wheel is not working, but pgUp|down yes.

This corrects the earlier claim that scrolling was repaired. **Keyboard navigation
is confirmed by the operator. Mouse-wheel navigation remains unresolved.**

## Observed frame and evidence

- Host: office. tmux socket: `/tmp/tmux-1000/default`.
- Session `muticula` (`$24`), window `cartan` (`@57`), pane `%56`, Codex TUI.
- Client `/dev/pts/7`; subagent inspection and Cartan's independent process check found the direct chain
  Konsole → zsh → `tmux attach -t muticula` → default server → `%56`.
- No Ovitmugen frame server is in that observed client chain. This is feedback
  relevant to Ovitmugen's future scrolling policy, not a demonstrated Ovitmugen defect.
- Before the intervention: alternate screen active, `mouse=1`, history `35/50000`.
  The repair subagent observed pane-specific root wheel overrides translating
  wheel events to `PPage`/`NPage` inside Codex. Their original author is unknown.
- Cartan independently checked the resulting live state:

```text
pane=%56 session=muticula window=cartan mode=copy-mode in_mode=1
history=35/50000 scroll=35 prefix=C-b mouse=1 alternate=1
```

Independent process receipt (`ps -o pid=,ppid=,sid=,tty=,stat=,comm=,args= -p 5206,8181,3620432`):

```text
5206       722 5206 ?     Ssl konsole      /usr/bin/konsole
8181      5206 8181 pts/7 Ss  zsh          /bin/zsh
3620432   8181 8181 pts/7 S+  tmux: client tmux attach -t muticula
```

The history limit is already large. Only 35 lines were retained as tmux history
at the observation; that does not count the visible screen or establish how much
conversation Codex retains internally. Increasing the limit cannot recover text
which tmux never retained.

## Applied live mitigation

The repair changed two live root wheel bindings, branching on `%56`, and entered
tmux copy mode. It did not edit source or persistent configuration, restart an
agent, kill a pane, or clear history. The fallback branches for other panes were
preserved. Cartan independently captured the resulting bindings:

```text
bind-key -T root WheelUpPane if-shell -F -t = "#{&&:#{==:#{pane_id},%56},#{!:#{pane_in_mode}}}" "copy-mode -e" "if-shell -F \"#{||:#{alternate_on},#{pane_in_mode},#{mouse_any_flag}}\" { send-keys -M } { copy-mode -e }"
bind-key -T root WheelDownPane if-shell -F -t = "#{&&:#{==:#{pane_id},%56},#{!:#{pane_in_mode}}}" "send-keys -M" "send-keys -M"
```

Both `copy-mode` and `copy-mode-vi` already contain these wheel actions:

```text
WheelUpPane   select-pane ; send-keys -X -N 5 scroll-up
WheelDownPane select-pane ; send-keys -X -N 5 scroll-down
```

The presence of correct bindings and a successful programmatic copy-mode scroll
do not prove that physical wheel events reach tmux. The first repair left the
viewport at its oldest retained line, where further upward scrolling cannot be
observed. A follow-up moved it to the middle (`scroll=15`) and requested an
operator wheel check in both directions, without changing the application input.
The operator returned to the Jev discussion without supplying that observation.
Cartan's final read-only check still showed `scroll=15`, `history=35/50000`,
`mode=copy-mode`, `mouse=1`, and `alternate=1`. That unchanged position is not
evidence of attempted physical wheel input.

Available keyboard workaround: `Ctrl+B`, then `[` enters history; `PgUp`/`PgDn`
navigate; `q` returns to the application.

## Source comparison and ownership

Inspected ia-sync source at `60c2b6a`:

- `/home/hruzam/ia-sync/zsh/session/ovitmugen.py`: `servers()` separates the
  default agents server from the `ovitmugen` frame server; `plan_up()` puts an
  inner tmux attach client in the frame's left pane. Calls name their server.
- `/home/hruzam/ia-sync/zsh/session/ovitmugen.tmux.conf`: frame-only configuration,
  prefix `C-a`, mouse enabled. It defines no wheel routing policy. Its header
  explicitly states that the agents server does not read it.
- The scoped source search found no counterpart of the pane-%56 wheel override.
  Office `~/.tmux.conf` contains only `window-size largest`; the inspected source
  does not explain the origin of the live override.
- The Ovitmugen help describes layout and tab controls, but has no explicit
  application-history versus tmux-history contract.

Trajectory owns Ovitmugen source and STATUS. This feedback changes neither. The
operator selected this filename; it is feedback, not a numbered POINT/RETURN/
VERDICT cycle and does not close a session gate.

## Systematic repair recommendation

Separate two questions: **which layer receives the wheel**, and **which layer owns
the history the operator wants to read**. A binding repair addresses only the first.

1. Finish a physical input check on the direct Konsole connection. Read the tmux
   scroll position before and after wheel motion from a middle position. If no
   events arrive, investigate terminal/client mouse reporting before changing
   more tmux bindings. Preserve the keyboard fallback while diagnosing it.
   Recommending `mouse on` or a larger history limit alone would miss this case:
   both settings were already present when the operator reported the failure.
2. Specify one scrolling policy for agent panes, distinguishing application
   scrolling from explicit tmux copy mode. Preserve applications which already
   handle mouse input. Do not promote the `%56` exception into source: a pane ID
   is an observation coordinate, not a reusable policy selector.
3. If a persistent tmux change proves necessary, author it in the configuration
   which owns the agents server. A frame-only change cannot repair the observed
   direct default-server connection. Frame event forwarding needs its own test.
4. Qualify both direct attachment and an Ovitmugen left view on isolated servers,
   with shell, Codex, Claude, and the fixed runbook pane. Check both wheel
   directions away from history boundaries, focus, copy-mode exit, tab switching,
   and detach/reattach. The final physical-wheel check belongs to the operator;
   injected copy-mode commands cannot substitute for it.
5. If the requirement is the complete agent conversation, verify the agent's
   supported history/scrollback behavior separately. Do not promise that tmux
   copy mode exposes application-owned conversation history.

The systematic fix is not yet proven. The immediate keyboard workaround is.
No persistent scrolling change or deployment is requested by this report;
the proposed work belongs to the Ovitmugen owner after the remaining input
observation is resolved.

## Read-only recovery checks

```sh
tmux -L default display-message -p -t %56 'mode=#{pane_mode} scroll=#{scroll_position} history=#{history_size}/#{history_limit} mouse=#{mouse} alternate=#{alternate_on}'
tmux -L default list-keys -T root | rg 'Wheel(Up|Down)Pane'
tmux -L default list-keys -T copy-mode | rg 'Wheel(Up|Down)Pane'
tmux -L default list-keys -T copy-mode-vi | rg 'Wheel(Up|Down)Pane'
```

Resolve the current pane afresh on a later session; `%56` is specific to this
incident. Source/selftests should use isolated sockets, as the owning RUNBOOK
requires. Physical use of the live pane is an operator observation.
