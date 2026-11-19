#!/usr/bin/env python3
"""Step 5c mutation check. Each mutation runs in a fresh temporary copy of the source; the
whole unit suite runs on the copy and the failing tests (with subTest detail and the first
assertion line) are listed; `expect` names the test meant to catch it.
  - m1 restores the exact pre-5c body of _Runtime.unshare (notification before submission).
  - m2 keeps the new order but leaves status_message unguarded (submission happens, the
    exception still reaches the editor).
  - m3 makes remove_share clear every pending id instead of its own (assay, step 5b). It is
    also run against the PRE-5C tests ($PRE5C_TESTS) to show they did not catch it.
Run: PRE5C_TESTS=<dir> python3 -I -S -B mutation-check-5c.py > mutation-check-5c.<date>.txt
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
C, P = 'SublimeObserver/contract.py', 'SublimeObserver/publisher.py'

NEW_UNSHARE = (
    "        if self.store is not None:\n"
    "            self.store.revoke(share.share_id)       # synchronous: queued captures are discarded\n"
    "            self.writer.submit(self.store.remove_share, share.share_id)     # before any notification\n"
    "        self.debouncer.cancel(view_id)\n"
    "        try:                                        # a failing notification must not reach the editor\n"
    "            share.view.erase_status(STATUS_KEY)\n"
    "        except Exception:\n"
    "            pass\n"
    "        if why != 'closed':\n"
    "            try:\n"
    "                sublime.status_message('Sublime Observer: {}'.format(why))\n"
    "            except Exception:\n"
    "                pass\n")
OLD_UNSHARE = (                     # verbatim from publisher.py f519aec5...f8b2, lines 214-224
    "        if self.store is not None:\n"
    "            self.store.revoke(share.share_id)       # synchronous: queued captures are discarded\n"
    "        self.debouncer.cancel(view_id)\n"
    "        try:\n"
    "            share.view.erase_status(STATUS_KEY)\n"
    "        except Exception:\n"
    "            pass\n"
    "        if why != 'closed':\n"
    "            sublime.status_message('Sublime Observer: {}'.format(why))\n"
    "        if self.store is not None:\n"
    "            self.writer.submit(self.store.remove_share, share.share_id)\n")
UNGUARDED = NEW_UNSHARE.replace(
    "            try:\n"
    "                sublime.status_message('Sublime Observer: {}'.format(why))\n"
    "            except Exception:\n"
    "                pass\n",
    "            sublime.status_message('Sublime Observer: {}'.format(why))\n")

T1 = 'test_failing_notification_on_revoke_still_queues_the_removal'
T2 = 'test_two_pending_revocations_hold_the_heartbeat_until_both_removals_complete'
MUTATIONS = [
    ('baseline-noop', None, [(C, 'CONTRACT_VERSION = 1', 'CONTRACT_VERSION = 1')], False),
    ('m1 old-order-notification-before-submission', T1, [(P, NEW_UNSHARE, OLD_UNSHARE)], False),
    ('m2 new-order-status-message-unguarded', T1, [(P, NEW_UNSHARE, UNGUARDED)], False),
    ('m3 removal-clears-all-pending-ids', T2,
     [(C, '                self._pending.discard(share_id)     # removed: heartbeats may resume',
          '                self._pending.clear()')], True),
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


def unittest_run(tests_dir):
    env = dict(os.environ, SUBLIME_OBSERVER_TASK=TASK)
    cmd = [sys.executable, '-I', '-S', '-B', '-m', 'unittest', 'discover', '-s', tests_dir]
    try:
        out = subprocess.run(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             universal_newlines=True, timeout=180).stdout
    except subprocess.TimeoutExpired:
        return 'TIMEOUT', [], []
    lines = [l for l in out.splitlines() if l.strip()]
    ran = [l for l in lines if l.startswith('Ran ')]
    last = (ran[-1] + ' -> ' if ran else '') + lines[-1]
    caught = sorted(set(m.group(1) for m in re.finditer(r'^(?:FAIL|ERROR): (\S+)', out, re.M)))
    detail = []
    for block in re.split(r'^=+$', out, flags=re.M)[1:]:
        head = block.strip().splitlines()[0]
        why = [l for l in block.splitlines() if re.match(r'^(\w+Error|AssertionError)\b', l)]
        detail.append('{}\n        {}'.format(head, why[0] if why else '(no assertion line)'))
    return last, caught, detail


def run(name, expect, edits, pre5c):
    work = tempfile.mkdtemp(prefix='sublime-observer-mutation-5c-')
    try:
        impl, err = copy_and_edit(work, edits)
        if err:
            return '{} => {}'.format(name, err)
        last, caught, detail = unittest_run(os.path.join(impl, 'tests'))
        line = '{} => {}'.format(name, last) + ''.join('\n    caught by ' + c for c in caught)
        line += ''.join('\n      ' + d for d in detail)
        if expect:
            line += '\n    expected catcher {} {}'.format(expect, 'PRESENT' if expect in caught else 'MISSING')
        if pre5c is not None:
            if not pre5c:
                line += '\n    PRE-5C run skipped: $PRE5C_TESTS not set'
            else:
                old = os.path.join(work, 'old')
                shutil.copytree(os.path.join(impl, 'SublimeObserver'), os.path.join(old, 'SublimeObserver'))
                shutil.copytree(pre5c, os.path.join(old, 'tests'), ignore=shutil.ignore_patterns('__pycache__'))
                last_old, caught_old, _ = unittest_run(os.path.join(old, 'tests'))
                line += '\n    same mutation, PRE-5C test suite: {}{}'.format(
                    last_old, ''.join('\n        caught by ' + c for c in caught_old) or '\n        (nothing caught)')
        return line
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == '__main__':
    pre5c = os.environ.get('PRE5C_TESTS') or ''
    print('PRE5C_TESTS =', pre5c or None, flush=True)
    for name, expect, edits, with_old in MUTATIONS:
        print(run(name, expect, edits, pre5c if with_old else None), flush=True)
