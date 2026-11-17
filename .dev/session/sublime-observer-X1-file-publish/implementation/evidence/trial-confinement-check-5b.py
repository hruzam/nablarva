#!/usr/bin/env python3
"""Step 5b: confinement self-check of disposable_trial.py's process scan, with no editor.

Spawns harmless children (`sleep`): a direct child and a double-forked grandchild that
escapes its parent (the crash_handler pattern). With the trial's audit hook and subreaper on,
it exercises walk/started_pids/proc/mine/gone/guarded_signal and pid 1 (not started), then
prints the trial's own proc_access report. Every /proc entry touched must be self or pinned.
Run: python3 -I -S -B trial-confinement-check-5b.py <source tests dir> [foreign pid]
The foreign pid (default 1) must be a process this checker did not start; the mutation runner
passes a `sleep` of its own. It is only ever handed to the trial's functions, which must refuse it.
"""
import json
import os
import signal
import subprocess
import sys
import time

sys.path.insert(0, sys.argv[1])
sys.dont_write_bytecode = True
import disposable_trial as dt  # noqa: E402

FOREIGN = int(sys.argv[2]) if len(sys.argv) > 2 else 1
sys.addaudithook(dt._audit)
dt.set_child_subreaper()
direct = subprocess.Popen(['sleep', '30'])
# double fork: the intermediate shell exits at once, its `sleep` is reparented (to us: subreaper)
subprocess.run(['sh', '-c', 'sleep 31 & exit 0'], check=True)
time.sleep(0.3)
started = dt.started_pids()
infos = {p: dt.proc(p) for p in started}
result = {
    'self_pid': dt._SELF,
    'direct_child': direct.pid,
    'started_pids_running': started,
    'started_exes': {p: (i or {}).get('exe') for p, i in infos.items()},
    'grandchild_reparented_into_tree': [p for p, i in infos.items() if i and i.get('cmdline') == 'sleep 31'],
    'foreign_pid': FOREIGN,
    'foreign_in_mine': FOREIGN in [p['pid'] for p in dt.mine('/tmp/none')],
}
try:
    result['proc_of_foreign_returns'] = dt.proc(FOREIGN)
except Exception as exc:                # a mutated guard may read first and fail later
    result['proc_of_foreign_returns'] = 'raised {}: {}'.format(type(exc).__name__, exc)
try:
    dt._proc_path(FOREIGN, 'exe')
    result['proc_path_foreign'] = 'ALLOWED (bad)'
except RuntimeError as exc:
    result['proc_path_foreign'] = 'refused: {}'.format(exc)
try:
    dt.gone(FOREIGN)
    result['gone_foreign'] = 'ALLOWED (bad)'
except RuntimeError as exc:
    result['gone_foreign'] = 'refused: {}'.format(exc)
result['mine_with_guard'] = dt.mine('/tmp/none')      # sleeps are not under the disposable path
pinned = [p for p in started if p in dt._PIDFD]     # signals only ever go through our own pidfds
for p in pinned:
    signal.pidfd_send_signal(dt._PIDFD[p], signal.SIGTERM)
direct.wait(5)
time.sleep(0.3)
result['gone_after_sigterm'] = {p: dt.gone(p) for p in pinned}
dt.reap_orphans({direct.pid})
result['operator_editors'] = dt.operator_editors()
result['proc_access'] = dt.proc_access_report()
bad = result['proc_access']['entries_not_self_and_not_started']
result['verdict'] = 'CONFINED' if (not bad and result['grandchild_reparented_into_tree']
                                   and result['proc_of_foreign_returns'] is None
                                   and not result['foreign_in_mine']
                                   and result['proc_path_foreign'].startswith('refused')
                                   and result['gone_foreign'].startswith('refused')
                                   and all(result['gone_after_sigterm'].values())) else 'NOT CONFINED'
print(json.dumps(result, indent=1, default=str))
