#!/usr/bin/env python3
"""Step 5 mutation check: each mutation removes one new guard in a fresh temporary copy of the
source (and, for the install guard, of the task file); the unit suite must then FAIL, naming
the tests that caught it. Run: python3 -I -S -B mutation-check-5.py > mutation-check-5.<date>.txt
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
C, P, R = 'SublimeObserver/contract.py', 'SublimeObserver/publisher.py', 'tests/reader.py'

MUTATIONS = [
    ('baseline-noop', [(C, 'CONTRACT_VERSION = 1', 'CONTRACT_VERSION = 1')]),
    # 1 ownership
    ('a1 lock-not-taken', [(C, '                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)', '                pass')]),
    ('a2 no-inode-check-after-lock', [(C, '            if at_path is not None and (at_path.st_dev, at_path.st_ino) == (st.st_dev, st.st_ino):', '            if True:')]),
    ('a3 residue-cleaned-before-lock', [(C, '                _mkdir_private(self.root, self.uid)\n                try:\n                    fd = acquire_lock',
                                          '                _mkdir_private(self.root, self.uid)\n                remove_publication(self.root)\n                try:\n                    fd = acquire_lock')]),
    ('a4 unreadable-publisher-cleaned', [(C, '                if error is not None:\n                    self._release()', '                if False:\n                    self._release()')]),
    # 2 no cross-share mixing
    ('b1 text-name-without-share-id', [(C, "    return 'text.{}.{}'.format(share_id, revision)", "    return 'text.{}'.format(revision)")]),
    ('b2 reader-unpinned-and-no-second-read', [
        (R, "    return parts[1], os.path.join(root, 'views', parts[1])", "    return parts[1], os.path.join(root, 'current')"),
        (R, '        if _identity(again) != _identity(state):\n            continue', '        pass')]),
    ('b3 reader-no-second-state-read', [(R, '        if _identity(again) != _identity(state):\n            continue', '        pass')]),
    ('b4 reader-no-share-id-check', [(R, "        if share_id is not None and state.get('share_id') != share_id:", '        if False:')]),
    # 3 revocation
    ('c1 unshare-does-not-revoke', [(P, '            self.store.revoke(share.share_id)       # synchronous', '            pass       # synchronous'),
                                    (C, '        self.revoke(share_id)\n        with self._lock:\n            self.text_rev.pop', '        with self._lock:\n            self.text_rev.pop')]),
    ('c2 removal-failure-not-fail-closed', [(C, '                self._stop_publishing(reason)\n                raise Stopped(reason)', '                raise Stopped(reason)')]),
    ('c3 stop-leaves-publisher-json', [(C, "                       lambda: os.unlink(os.path.join(self.root, 'publisher.json'))):", '                       ):')]),
    ('c4 no-path-check-on-events', [(P, '        if not self.path_allowed(view_id):\n            return\n        delay', '        delay')]),
    ('c5 save-not-forced', [(P, '            _RT.saved(view)', '            _RT.touched(view)')]),
    # 4 install fresh inodes
    ('d1 update-without-remove-destination', [('TASK', 'command cp --remove-destination --', 'command cp --')]),
    # 5 small fixes
    ('e1 unresolvable-path-allowed', [(C, "        return 'path cannot be resolved ({})'.format(type(exc).__name__)", '        return None')]),
    ('e2 index-before-current-removal', [(C, '        if self._current is not None and self._current != target:\n            set_current(self.root, None)\n            self._current = None\n        self._write_index()',
                                          '        self._write_index()\n        if self._current is not None and self._current != target:\n            set_current(self.root, None)\n            self._current = None')]),
    ('e3 encoding-replacement-unflagged', [(C, "text.encode(TEXT_FILE_ENCODING, 'replace'), True", "text.encode(TEXT_FILE_ENCODING, 'replace'), False")]),
]


def run(name, edits):
    work = tempfile.mkdtemp(prefix='sublime-observer-mutation-5-')
    try:
        impl = os.path.join(work, 'impl')
        shutil.copytree(SRC, impl, ignore=shutil.ignore_patterns('__pycache__'))
        task = os.path.join(work, 'sublime-observer.md')
        shutil.copyfile(TASK, task)
        for rel, old, new in edits:
            path = task if rel == 'TASK' else os.path.join(impl, rel)
            with open(path, encoding='utf-8') as handle:
                text = handle.read()
            if text.count(old) != 1:
                return '{} => PATTERN NOT FOUND ONCE in {}: {!r}'.format(name, rel, old[:60])
            with open(path, 'w', encoding='utf-8') as handle:
                handle.write(text.replace(old, new, 1))
        env = dict(os.environ, SUBLIME_OBSERVER_TASK=task)
        try:
            out = subprocess.run([sys.executable, '-I', '-S', '-B', '-m', 'unittest', 'discover', '-s',
                                  os.path.join(impl, 'tests')], env=env, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, universal_newlines=True, timeout=120).stdout
        except subprocess.TimeoutExpired:
            return '{} => TIMEOUT (counts as caught)'.format(name)
        last = [l for l in out.splitlines() if l.strip()][-1]
        caught = sorted(set(m.group(1) for m in re.finditer(r'^(?:FAIL|ERROR): (\S+)', out, re.M)))
        return '{} => {}{}'.format(name, last, ''.join('\n    caught by ' + c for c in caught))
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == '__main__':
    for name, edits in MUTATIONS:
        print(run(name, edits), flush=True)
