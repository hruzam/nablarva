# Owner review request — exact targets and independent phone views

Prepared by Astrobley for Cartan, 2026-10-30. REVIEW ONLY. Nothing applied,
deployed, activated or written in ia-sync. Full app remains fixture-only.

Recommendation: Majkee authorizes the existing ovitmugen owner to review the API
scope, then that owner implements/tests it in the surgical-table source. Do not
treat this illustrative patch as promotion approval or a completed owner gate.

## Current frame and overlap

- Source: /home/hruzam/ia-sync/zsh/session/ovitmugen.py.
- Observed SHA256: 97dba115a36abf216ab6f5deabda601ce82e395cdd285a1b52aca7568f5a3125.
- git status --short -- zsh/session was empty; source hash stayed unchanged.
- Last scoped source commit: b435af5, patient idle checks/home selftest correction.
- Existing owner bed: .dev/session/ovitmugen-01-basement; its STATUS assigns
  Trajectory, says the new basement is not built, keeps ov-ls --json unchanged,
  and reserves state/runtime homes for its D2 relay. That STATUS was read only.
- ia-sync AGENTS/SYNC_DISCIPLINE and zsh/AGENTS were read for source/publication
  boundaries. No mail was read, as instructed. No journal, source, deploy target,
  presence record or other owner's STATUS was changed.
- No existing --phone- or @ov-phone- strings were found in scoped session/remote-cli
  sources before the proposal. Names/options remain subject to owner approval.

The existing app cannot safely map phone selection onto `ovitmugen tab`: it changes
the shared <bed>--left view. `close_idle_tab()` is guarded but internal; public
`down --idle` closes a wider scope. Current ls JSON lacks pane/process/server identity.

## Exact additive CLI proposal

Existing commands and ls --json shape stay intact. Add:

```text
ovitmugen targets BED
ovitmugen phone-view create BED --window @N --pane %N --generation G
ovitmugen phone-view select BED --view BED--phone-RANDOM --token T --server-generation S \
  --window @N --pane %N --generation G
ovitmugen phone-view detach BED --view BED--phone-RANDOM --token T --server-generation S
ovitmugen close-tab BED --window @N --pane %N --generation G --confirm
```

All new outputs are JSON. Socket selection remains the existing owner configuration
OV_AGENTS_SOCKET/OV_AGENTS_CONF, never caller-provided terminal URL commands. Every
tmux call still carries its server selector. Phone API does not touch the frame
server or desktop --left, start an agent, inject prompt bytes, provide approvals,
or create a second lifecycle manager in the app.

`targets` schema1 returns:

```json
{
  "schema": 1,
  "server": {"host":"...","socket":"...","path":"...","device":0,"inode":0,
             "pid":123,"start":"process-start-ticks","sessionId":"$0"},
  "serverGeneration":"sha256-of-exact-server-and-base-identity",
  "targets":[{"bed":"example","windowId":"@0","name":"implement","paneId":"%0",
              "panePid":456,"paneStart":"ticks","paneCount":1,"command":"bash",
              "dead":false,"busy":false,"generation":"sha256-of-exact-target-identity"}]
}
```

Generation is a stale-reference check, not an authorization credential or registry.
It binds host, actual socket inode, server/process start, base session ID, window,
pane and pane process start. Busy uses the owner's existing pane_busy/children_map.
The observation is not transactional truth: the caller must revalidate before each
attachment/input/output operation, including the active view window/pane. Independent
live pane selection is explicitly unavailable for multi-pane windows in this proposal.

Create returns `{viewId,name,token,serverGeneration,target,attachArgv}`. The token
is a random view ownership/stale-ID nonce, stored in a tmux session user option;
it does not authenticate network clients. Generated <bed>--phone-<random> sessions
share windows but own active-window selection. Prefixes/status are disabled only
there to prevent native chooser/window navigation from silently changing the binding;
mouse remains enabled. The app supplies its own picker and guarded history controls.
No automatic window sizing policy change: one shared window still has one width.

Select/detach take the unique generated NAME, never a reusable numeric session ID.
They verify the phone namespace, exact name, nonce, server/base generation and group
membership at the action boundary. Select confirms the same marked view's active
window/pane afterward. Detach refuses if the base disappeared, preserving a possible
last surviving view/agent owner. Arbitrary/desktop views and reused IDs are refused.
Intentional shell tmux commands remain possible; the app closes a diverged binding.

Close is selected-only and reuses close_idle_tab(), preserving busy and last-tab
guards. A small optional verify callback adds exact-generation/idle validation
immediately before its kill-window. Existing callers are unchanged. It refuses
busy/dead/multi-pane/stale targets. It never substitutes for explicit agent exit.
Initial close validation checks identity only, preserving the existing owner's
transient-child patience loop; the callback verifies idle immediately before kill.
The ordinary check-to-tmux-operation race remains; no atomic OS/process capability
is invented here. Owner review must assess that boundary before live qualification.

## Patch and actual checks

`ovitmugen.phone-api.proposed.patch` is an illustrative 219-line unified diff in
this review bed, NOT an applied ia-sync edit. It has no new runtime directory,
ledger, daemon or protocol. The only added identity state is marked tmux view options.
That namespace/identity choice requires its owner's review; do not rush it into use.

Actual checks: patched source compiles; git -C /home/hruzam/ia-sync apply --check
against the proposed patch succeeds; original source hash remains the baseline.
The amended draft passes nine isolated checks in check_candidate.py, including the
existing owner selftest. The harness applies the patch to stdout/in-memory only and
operates solely uniquely named disposable servers. It deliberately restarts servers
and reuses the old numeric view ID immediately before select/detach/create-failure
cleanup, proving replacement sessions/pane PIDs/selections survive. The app's tests
are separate; neither suite authorizes source promotion or live activation.

Patch SHA256: 5af6027b58cf222733b28622af8992d0b3f1dafe7569b9ebc9060d0934b35fa6.
See regressions.json for expected/observed results and retained failed revisions.

The earlier draft was held by independent review for numeric-ID action/cleanup races
and an initial idle check that bypassed owner patience. The first amended behavior
run additionally failed because set-option requires the exact session context
`=NAME:` on tmux 3.7c, while kill-session accepts `=NAME`. A dedicated isolated
syntax proof and the full amended regressions now pass. The failed evidence remains
in the independently owned verification.md until that verifier records its recheck.

## Owner test plan before any live use

Use isolated OV_AGENTS_SOCKET/OV_FRAME_SOCKET names only, never default/live servers.
Run the existing selftest unchanged and compare old ls --json before/after. Then:

1. Two windows, two generated phone views, desktop --left fixed: select each phone
   window independently and prove the desktop selection stays fixed.
2. Verify returned IDs/socket/host/process-start metadata; rename-only keeps identity,
   pane respawn and server restart invalidate it. Wrong socket/base/ID/nonce refuses.
3. New-view detach preserves base pane PIDs and other clients; arbitrary --left
   detach refuses; base deletion/orphan group refuses cleanup rather than ending agents.
4. Single idle selected close succeeds; busy child/foreground agent, last tab,
   multi-pane window, stale generation and missing confirm all refuse. Recheck busy
   and generation during the existing patience loop, including process-start changes.
5. Verify prefix/prefix2/status/mouse settings affect generated phone sessions only;
   no frame/--left keys or window sizing policy is overwritten.
6. App integration uses public commands, validates active window/pane for each input,
   resize/history and output/watchdog path, and closes on divergence. Do not import
   these owner-private implementation functions into the app.
7. Review current ia-sync publication path, source hash drift, office install/rollback
   and a separately observed home repeat; no automatic transport or activation.

## Decisions owed to Majkee and the existing owner

- Approve the additive API request as a bounded subtask under Trajectory's existing
  source pen, with this phone session as consumer; preserve the basement gate/D2
  runtime-home work and unchanged ls JSON.
- Accept/revise phone view naming, tmux-option nonce metadata, fixed-view prefix/status
  policy and single-pane limitation. These are proposals, not new canon.
- Decide whether existing idle-close race semantics are sufficient for this phone
  operation or require a stronger owner guard; the app must not invent one separately.
- Assign owner implementation/selftest/publication and independent live/phone
  qualification. Only after those gates may Cartan enable a live adapter.
