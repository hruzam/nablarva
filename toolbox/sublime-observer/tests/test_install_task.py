"""The install task's shell block, run against a temporary HOME (step 5, acceptance d).

The block derives every path from $HOME, so pointing HOME at a temporary directory with a
copy of the payload runs it without touching the real profile, Sublime or the runtime root.
The task file lives in ~/ia-sync/install-pkgs/; SUBLIME_OBSERVER_TASK overrides the path.
Skipped when the task file or bash is absent (another host).
"""
import os
import shutil
import subprocess
import tempfile
import unittest

import fakes

TASK = os.environ.get('SUBLIME_OBSERVER_TASK') or os.path.expanduser('~/ia-sync/install-pkgs/sublime-observer.md')
FIVE = ('.python-version', 'SublimeObserver.sublime-settings', 'SublimeObserver.sublime-commands',
        'contract.py', 'publisher.py')
REL_SRC = 'unikuklatrix/nablarva/toolbox/sublime-observer/SublimeObserver'


def install_block(path):
    """The first ```bash block after the '## Install (by hand)' heading."""
    with open(path, encoding='utf-8') as handle:
        lines = handle.read().splitlines()
    start = lines.index('## Install (by hand)')
    begin = lines.index('```bash', start) + 1
    end = lines.index('```', begin)
    block = '\n'.join(lines[begin:end]) + '\n'
    if not block.startswith("bash <<'EOF'"):
        raise AssertionError('unexpected install block shape')
    return block


@unittest.skipUnless(os.path.isfile(TASK) and shutil.which('bash'), 'install task or bash not present')
class InstallBlockTests(unittest.TestCase):
    def setUp(self):
        self.home = tempfile.mkdtemp(prefix='sublime-observer-install-test-')
        self.addCleanup(shutil.rmtree, self.home, True)
        src = os.path.join(self.home, REL_SRC)
        os.makedirs(src)
        for name in FIVE:
            shutil.copyfile(os.path.join(fakes.IMPL, 'SublimeObserver', name), os.path.join(src, name))
        self.src = src
        self.packages = os.path.join(self.home, '.config', 'sublime-text', 'Packages')
        os.makedirs(self.packages)
        self.target = os.path.join(self.packages, 'SublimeObserver')

    def run_block(self):
        env = {'HOME': self.home, 'PATH': os.environ.get('PATH', '/usr/bin:/bin'), 'LC_ALL': 'C'}
        return subprocess.run(['bash', '-c', install_block(TASK)], env=env, cwd=self.home,
                              stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              universal_newlines=True, timeout=60)

    def read(self, path):
        with open(path, 'rb') as handle:
            return handle.read()

    def test_update_never_writes_through_a_hard_link(self):
        os.mkdir(self.target)
        unrelated = os.path.join(self.home, 'unrelated-file.txt')
        with open(unrelated, 'wb') as handle:
            handle.write(b'UNRELATED CONTENT, MUST SURVIVE\n')
        for name in FIVE:
            if name == 'contract.py':
                os.link(unrelated, os.path.join(self.target, name))   # same inode as the unrelated file
            else:
                with open(os.path.join(self.target, name), 'wb') as handle:
                    handle.write(b'old installed copy\n')
        result = self.run_block()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('ok: five files replaced', result.stdout)
        self.assertEqual(self.read(unrelated), b'UNRELATED CONTENT, MUST SURVIVE\n')
        self.assertEqual(os.stat(unrelated).st_nlink, 1)
        for name in FIVE:
            self.assertEqual(self.read(os.path.join(self.target, name)), self.read(os.path.join(self.src, name)), name)
        self.assertNotEqual(os.stat(os.path.join(self.target, 'contract.py')).st_ino, os.stat(unrelated).st_ino)

    def test_first_install_still_stages_and_moves(self):
        result = self.run_block()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('ok: five files installed', result.stdout)
        self.assertEqual(sorted(os.listdir(self.target)), sorted(FIVE))
        self.assertFalse(os.path.lexists(os.path.join(self.home, '.config', 'sublime-text',
                                                      '.SublimeObserver-install-staging')))


if __name__ == '__main__':
    unittest.main()
