"""Step 4a end-to-end proof driver: fake root under /tmp, real contract Store, no editor."""
import json, os, shutil, signal, subprocess, sys, tempfile, threading, time
T = '/home/hruzam/unikuklatrix/nablarva/toolbox/sublime-observer'
sys.dont_write_bytecode = True
sys.path.insert(0, T)
from SublimeObserver import contract

work = tempfile.mkdtemp(prefix='x1-4a-proof-', dir='/tmp')
base = os.path.join(work, 'run'); os.mkdir(base, 0o700)
root = os.path.join(base, 'sublime-observer')
out = os.path.join(work, 'timeline.jsonl')
errf = open(os.path.join(work, 'stderr.txt'), 'wb')
rec = subprocess.Popen([sys.executable, '-I', '-B', T + '/tests/witness_recorder.py', '--out', out,
                        '--forbid', 'UNSHARED-VIEW-MARKER', '--forbid', 'secret-word', '--root', root],
                       stdin=subprocess.PIPE, stderr=errf)

def stamp(s):
    rec.stdin.write((s + '\n').encode()); rec.stdin.flush()

def cap(view, rev, text):
    return {'window': 1, 'view': view, 'buffer': view + 10, 'path': '/tmp/synthetic-{}.md'.format(view),
            'title': 'synthetic-{}.md'.format(view), 'dirty': True, 'loading': False, 'revision': rev,
            'captured_at': time.time(), 'encoding': 'UTF-8', 'size_chars': len(text), 'text': text,
            'truncated': False, 'selection_count': 1, 'selections_truncated': False,
            'selections': [{'a': 0, 'b': 0, 'empty': True, 'start': [0, 0], 'end': [0, 0]}],
            'visible_region': {'begin': 0, 'end': len(text)}, 'viewport_position': [0.0, 0.0],
            'viewport_extent': [800.0, 600.0], 'error': None}

class Beat(object):
    def __init__(self, store):
        self.store, self.stop = store, threading.Event()
        self.t = threading.Thread(target=self.run, daemon=True); self.t.start()
    def run(self):
        while not self.stop.wait(1.0):
            self.store.heartbeat()
    def halt(self):
        self.stop.set(); self.t.join(2)

try:
  time.sleep(1.2)
  stamp('1 enable (publisher start)')
  a = contract.Store(root, 'epoch-A', os.getpid(), os.getuid(), {'sublime_build': 'fake'}, 200000, 1.0)
  print(a.start()); ba = Beat(a); time.sleep(0.6)
  stamp('2 share one'); a.publish('one', cap(1, 1, 'synthetic shared text, revision one\n')); time.sleep(0.6)
  stamp('3 edit one'); a.publish('one', cap(1, 2, 'synthetic shared text, revision two, longer\n')); time.sleep(0.6)
  stamp('3b caret moves (state only)'); a.publish('one', dict(cap(1, 2, 'synthetic shared text, revision two, longer\n'), selections=[{'a': 5, 'b': 9, 'empty': False, 'start': [0, 5], 'end': [0, 9]}])); time.sleep(0.6)
  stamp('4 share two'); a.publish('two', cap(2, 1, 'second synthetic view\n')); time.sleep(0.6)
  stamp('5 unshare two'); a.remove_share('two'); time.sleep(0.6)
  stamp('6 crash (heartbeat stops, residue stays)'); ba.halt(); time.sleep(4.0)
  stamp('7 restart'); b = contract.Store(root, 'epoch-B', os.getpid() , os.getuid(), {'sublime_build': 'fake'}, 200000, 1.0)
  b._alive = lambda pid: False                      # the crashed epoch's pid is "gone" (same process here)
  print(b.start()); bb = Beat(b); time.sleep(0.6)
  stamp('8 share one again'); b.publish('one-b', cap(1, 3, 'synthetic shared text after restart\n')); time.sleep(0.6)
  stamp('9 quit'); bb.halt(); b.shutdown(); time.sleep(0.6)
  rec.stdin.close(); time.sleep(1.3)
  alive_after_eof = rec.poll() is None
  rec.send_signal(signal.SIGINT); rc = rec.wait(5); errf.close()
finally:
  if rec.poll() is None:
    rec.kill(); rec.wait(5)
print('work', work, 'rc', rc, 'alive_after_eof', alive_after_eof)
