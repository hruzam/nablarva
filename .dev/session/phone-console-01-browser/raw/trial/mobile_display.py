#!/usr/bin/env python3
"""Repair only the disposable gateway display; preserve its tmux processes."""
import argparse
import base64
import gzip
import hashlib
import json
import os
from pathlib import Path
import signal
import socket
import subprocess
import sys
import time
import urllib.request

from gateway import BINARY, SHA256, tmux

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('directory', type=Path)
parser.add_argument('--font-size', type=int, choices=range(10, 25), default=12)
parser.add_argument('--touch-scroll', action='store_true')
args = parser.parse_args()
directory = args.directory
state_file = directory / 'state.json'
state = json.loads(state_file.read_text())
assert hashlib.sha256(BINARY.read_bytes()).hexdigest() == SHA256
proc = Path('/proc') / str(state['gateway_pid'])
argv = (proc / 'cmdline').read_bytes().split(b'\0')
assert argv[0] == str(BINARY).encode()
assert state['socket'].encode() in argv
assert str(state['port']).encode() in argv
before = tmux(state, 'list-panes', '-a', '-F', '#{pane_id}:#{pane_pid}').stdout
auth = base64.b64encode(state['credential'].encode()).decode()
request = urllib.request.Request(f'http://127.0.0.1:{state["port"]}/',
    headers={'Authorization': 'Basic ' + auth, 'Accept-Encoding': 'identity'})
with urllib.request.urlopen(request, timeout=5) as response:
    body = response.read()
    if response.headers.get('Content-Encoding') == 'gzip':
        body = gzip.decompress(body)
original = directory / 'index.original.html'
index = directory / 'index.mobile.html'
if original.exists():
    assert body == index.read_bytes(), 'Served index changed; inspect before repeating'
    body = original.read_bytes()
assert b'name="viewport"' not in body, 'Unexpected viewport; inspect before repeating'
assert body.count(b'<head>') == 1
if not original.exists():
    original.write_bytes(body)
body = body.replace(b'<head>', b'<head><meta name="viewport" '
    b'content="width=device-width, initial-scale=1, interactive-widget=resizes-content">', 1)
if args.touch_scroll:
    adapter = Path(__file__).with_name('touch_scroll.js').read_bytes()
    assert b'</script' not in adapter.lower()
    assert body.count(b'</body>') == 1
    body = body.replace(b'</body>', b'<script>' + adapter + b'</script></body>', 1)
index.write_bytes(body)
# Persist the recovery edge before terminating the attachment gateway.
state['display_change'] = {'phase': 'restarting', 'index': str(index),
    'fontSize': args.font_size, 'touch_scroll': args.touch_scroll}
state_file.write_text(json.dumps(state, indent=2) + '\n')
os.kill(state['gateway_pid'], signal.SIGTERM)
for _ in range(50):
    try:
        with socket.create_connection(('127.0.0.1', state['port']), timeout=.1):
            time.sleep(.1)
    except OSError:
        break
else:
    raise SystemExit('Old listener remains; do not start another gateway')
env = dict(os.environ)
env.pop('TMUX', None)
with (directory / 'ttyd.log').open('ab') as log:
    gateway = subprocess.Popen([str(BINARY), '-i', '127.0.0.1', '-p', str(state['port']),
        '-W', '-O', '-c', state['credential'], '-I', str(index),
        '-t', 'titleFixed=Phone terminal trial', '-t', f'fontSize={args.font_size}',
        'tmux', '-S', state['socket'], 'attach-session', '-t', 'phone'],
        env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
state['gateway_pid'] = gateway.pid
state['display_change']['phase'] = 'started'
state_file.write_text(json.dumps(state, indent=2) + '\n')
for _ in range(50):
    assert gateway.poll() is None, 'Gateway exited; inspect private log'
    try:
        with urllib.request.urlopen(request, timeout=1) as response:
            served = response.read()
            if response.headers.get('Content-Encoding') == 'gzip':
                served = gzip.decompress(served)
        break
    except OSError:
        time.sleep(.1)
else:
    raise SystemExit('New gateway not ready')
assert served == body
after = tmux(state, 'list-panes', '-a', '-F', '#{pane_id}:#{pane_pid}').stdout
assert before == after, 'Fixture pane identities changed'
print(json.dumps({'mobile_index_sha256': hashlib.sha256(body).hexdigest(),
    'fontSize': args.font_size, 'shell_identities_preserved': True,
    'gateway_pid': gateway.pid, 'served_index_matches': True}, indent=2))
