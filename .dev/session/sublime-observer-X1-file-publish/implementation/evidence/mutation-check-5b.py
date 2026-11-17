#!/usr/bin/env python3
"""Step 5b mutation check. Each mutation removes one guard added in step 5b, in a fresh temporary
copy of the source; then
  - payload / test guards: the whole unit suite must FAIL; the catching tests are listed, and
    `expect` names the test that is meant to catch it (it must be among them);
  - sensitivity rows: the same mutation is also run against the PRE-5B tests (directory in
    $PRE5B_TESTS, optional) restricted to the expected test, to show the test was blind before;
  - trial confinement guards: trial-confinement-check-5b.py on the mutated copy must report
    NOT CONFINED, with a foreign `sleep` started by THIS runner (never a process of anyone else).
Run: PRE5B_TESTS=<dir> python3 -I -S -B mutation-check-5b.py > mutation-check-5b.<date>.txt
Never touches the source tree, the task file, the editor or the runtime root.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

SRC = '/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer'
TASK = '/home/hruzam/ia-sync/install-pkgs/sublime-observer.md'
HERE = os.path.dirname(os.path.abspath(__file__))
C, P, T = 'SublimeObserver/contract.py', 'SublimeObserver/publisher.py', 'tests/disposable_trial.py'

PAYLOAD = [
    ('baseline-noop', None, [(C, 'CONTRACT_VERSION = 1', 'CONTRACT_VERSION = 1')]),
    # R1 bounded revocation
    ('r1a heartbeat-ignores-pending-revocation', 'test_heartbeat_queued_before_unshare_does_not_refresh_the_revoked_capture',
     [(C, '            if not self.live or self._revocation_pending():', '            if not self.live:')]),
    ('r1b revoke-does-not-mark-pending', 'test_heartbeat_queued_before_unshare_does_not_refresh_the_revoked_capture',
     [(C, '            self._pending.add(share_id)', '            pass')]),
    ('r1c clock-read-after-the-pending-check', 'test_heartbeat_in_flight_at_revoke_stamps_a_time_before_it',
     [(C, '            now = self._clock()\n            if not self.live or self._revocation_pending():\n                return\n',
       '            if not self.live or self._revocation_pending():\n                return\n            now = self._clock()\n')]),
    ('r1d pending-never-cleared-after-removal', 'test_heartbeats_resume_after_removal_and_an_unrelated_share_reads_again',
     [(C, '                self._pending.discard(share_id)     # removed: heartbeats may resume', '                pass')]),
    ('r1e pending-check-uses-the-permanent-revoked-set', 'test_heartbeats_resume_after_removal_and_an_unrelated_share_reads_again',
     [(C, '            return bool(self._pending)', '            return bool(self._revoked)')]),
    # R4 raising file_name()
    ('r4a event-file-name-unguarded', 'test_raising_file_name_on_events_revokes_and_does_not_propagate',
     [(P, "        try:\n            path = share.view.file_name()\n        except Exception as exc:            # path unknown: revoke, never raise into the editor\n"
          "            self.unshare(view_id, 'unshared, path unknown ({})'.format(type(exc).__name__))\n            return False\n",
       '        path = share.view.file_name()\n')]),
    ('r4b poll-exception-not-revoked', 'test_raising_file_name_at_the_poll_revokes',
     [(P, '                self.path_allowed(view_id)  # a raising file_name() revokes the share here', '                pass')]),
]

SENSITIVITY = [
    # R2: the end-state test was blind to a publish that ignores revocation (re-audit, R2)
    ('s1 publish-ignores-revocation', 'test_queued_publish_then_unshare_close_or_sealed_save_writes_nothing',
     [(C, '            if not self.live or self._is_revoked(share_id):\n                return False',
       '            if not self.live:\n                return False')]),
    # thread test: losers that raise instead of refusing
    ('s2 contended-start-raises-instead-of-refusing', 'test_simultaneous_start_in_threads_one_owner',
     [(C, '            except BlockingIOError:\n                return None',
       "            except BlockingIOError:\n                raise ContractError('synthetic: loser raised')")]),
    # shutdown unlinks the lock file without the _holds_path verification
    ('s3 shutdown-unlink-without-holds-path', 'test_shutdown_never_unlinks_a_lock_file_it_does_not_hold',
     [(C, '                if _holds_path(self._lock_fd, self.lock_path):', '                if True:')]),
]

TRIAL = [
    ('baseline-trial-noop', [(T, "_SELF = os.getpid()", "_SELF = os.getpid()")]),
    ('t1 scan-every-pid-again', [(T, '    walk()\n    return [pid for pid, fd in _PIDFD.items() if not _exited(fd)]',
                                  "    walk()\n    return [int(n) for n in os.listdir('/proc') if n.isdigit()]")]),
    ('t2 proc-path-guard-removed', [(T, "    if pid != _SELF and pid not in _PIDFD:\n        raise RuntimeError('refusing to read /proc/{}: not a process this trial started'.format(pid))\n", ''),
                                    (T, '    if pid != _SELF and (pid not in _PIDFD or _exited(_PIDFD[pid])):\n        return None\n', '')]),
    ('t3 no-child-subreaper', [(T, '    if libc.prctl(36, 1, 0, 0, 0) != 0:', '    if 0:')]),
]


def copy_and_edit(work, edits):
    impl = os.path.join(work, 'impl')
    shutil.copytree(SRC, impl, ignore=shutil.ignore_patterns('__pycache__'))
    for rel, old, new in edits:
        path = os.path.join(impl, rel)
        with open(path, encoding='utf-8') as handle:
            text = handle.read()
        if text.count(old) != 1:
            return None, 'PATTERN NOT FOUND ONCE in {}: {!r}'.format(rel, old[:60])
        with open(path, 'w', encoding='utf-8') as handle:
            handle.write(text.replace(old, new, 1))
    return impl, None


def unittest_run(tests_dir, pattern=None):
    env = dict(os.environ, SUBLIME_OBSERVER_TASK=TASK)
    cmd = [sys.executable, '-I', '-S', '-B', '-m', 'unittest', 'discover', '-s', tests_dir]
    if pattern:
        cmd += ['-k', pattern]
    try:
        out = subprocess.run(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             universal_newlines=True, timeout=180).stdout
    except subprocess.TimeoutExpired:
        return 'TIMEOUT', []
    last = [l for l in out.splitlines() if l.strip()][-1]
    caught = sorted(set(m.group(1) for m in re.finditer(r'^(?:FAIL|ERROR): (\S+)', out, re.M)))
    return last, caught


def payload(name, expect, edits, pre5b=None):
    work = tempfile.mkdtemp(prefix='sublime-observer-mutation-5b-')
    try:
        impl, err = copy_and_edit(work, edits)
        if err:
            return '{} => {}'.format(name, err)
        last, caught = unittest_run(os.path.join(impl, 'tests'))
        line = '{} => {}'.format(name, last) + ''.join('\n    caught by ' + c for c in caught)
        if expect:
            line += '\n    expected catcher {} {}'.format(expect, 'PRESENT' if expect in caught else 'MISSING')
        if pre5b:
            old = os.path.join(work, 'old')
            shutil.copytree(os.path.join(impl, 'SublimeObserver'), os.path.join(old, 'SublimeObserver'))
            shutil.copytree(pre5b, os.path.join(old, 'tests'), ignore=shutil.ignore_patterns('__pycache__'))
            key = {'test_queued_publish_then_unshare_close_or_sealed_save_writes_nothing': 'writes_nothing',
                   'test_simultaneous_start_in_threads_one_owner': 'in_threads_one_owner'}.get(expect)
            if key:
                last_old, caught_old = unittest_run(os.path.join(old, 'tests'), key)
                line += '\n    same mutation, PRE-5B version of that test only: {}{}'.format(
                    last_old, ''.join('\n        caught by ' + c for c in caught_old))
            else:
                line += '\n    PRE-5B: no such test existed'
        return line
    finally:
        shutil.rmtree(work, ignore_errors=True)


def trial(name, edits):
    work = tempfile.mkdtemp(prefix='sublime-observer-mutation-5b-trial-')
    foreign = subprocess.Popen(['sleep', '60'])        # the runner's own process, outside the checker's tree
    try:
        impl, err = copy_and_edit(work, edits)
        if err:
            return '{} => {}'.format(name, err)
        out = subprocess.run([sys.executable, '-I', '-S', '-B', os.path.join(HERE, 'trial-confinement-check-5b.py'),
                              os.path.join(impl, 'tests'), str(foreign.pid)],
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, timeout=60).stdout
        verdict = re.search(r'"verdict": "([A-Z ]+)"', out)
        foreign_hit = re.search(r'"entries_not_self_and_not_started": \[([^\]]*)\]', out, re.S)
        return '{} => {}{}'.format(name, verdict.group(1) if verdict else 'NO VERDICT (crashed: counts as caught)\n' + out[-400:],
                                   '; foreign /proc entries: [{}]'.format(' '.join(foreign_hit.group(1).split())) if foreign_hit else '')
    finally:
        foreign.kill()
        foreign.wait(5)
        shutil.rmtree(work, ignore_errors=True)


if __name__ == '__main__':
    pre5b = os.environ.get('PRE5B_TESTS') or None
    print('PRE5B_TESTS =', pre5b, flush=True)
    for name, expect, edits in PAYLOAD:
        print(payload(name, expect, edits), flush=True)
    for name, expect, edits in SENSITIVITY:
        print(payload(name, expect, edits, pre5b), flush=True)
    for name, edits in TRIAL:
        print(trial(name, edits), flush=True)
