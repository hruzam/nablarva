#!/usr/bin/env python3
"""Disposable ttyd/tmux trial. No default socket, global install, or phone operations."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import secrets
import signal
import socket
import subprocess
import tempfile
import time

BINARY = Path('/tmp/phone-console-ttyd-1.7.7/ttyd')
SHA256 = '8a217c968aba172e0dbf3f34447218dc015bc4d5e59bf51db2f2cd12b7be4f55'


def tmux(state, *args, **kwargs):
    env = dict(os.environ)
    env.pop('TMUX', None)
    return subprocess.run(['tmux', '-S', state['socket'], *args], env=env,
                          check=True, text=True, capture_output=True, **kwargs)


def stop(directory):
    state = json.loads((directory / 'state.json').read_text())
    # Refuse a recycled PID. Never kill by process name or touch another socket.
    proc = Path('/proc') / str(state['gateway_pid'])
    if proc.exists():
        command = (proc / 'cmdline').read_bytes().split(b'\0')
        if command[0] != str(BINARY).encode() or str(state['port']).encode() not in command:
            raise SystemExit('PID identity changed; inspect manually')
        os.kill(state['gateway_pid'], signal.SIGTERM)
    if Path(state['socket']).exists():
        tmux(state, 'kill-server')
    (directory / 'stopped').write_text('Stopped dedicated gateway and tmux socket; retained evidence.\n')
    print(f'Stopped only trial at {directory}')


def start(port):
    if hashlib.sha256(BINARY.read_bytes()).hexdigest() != SHA256:
        raise SystemExit('Pinned ttyd checksum mismatch')
    with socket.socket() as check:
        check.bind(('127.0.0.1', port))
    directory = Path(tempfile.mkdtemp(prefix='pc-trial-', dir='/tmp'))
    directory.chmod(0o700)
    credential = 'trial:' + secrets.token_urlsafe(24)
    state = {'directory': str(directory), 'socket': str(directory / 'tmux.sock'),
             'port': port, 'credential': credential, 'binary_sha256': SHA256}
    rc = directory / 'bashrc'
    rc.write_text("export PS1='TRIAL \\s-\\v \\w \\$ '\n"
                  "printf 'Disposable fixture: Czech příliš žluťoučký kůň; Ctrl-B 0/1 changes window.\\n'\n"
                  "printf 'Use printf or seq 1 300 for scrollback. This is a real disposable shell.\\n'\n")
    env = dict(os.environ)
    env.pop('TMUX', None)
    shell = ['bash', '--noprofile', '--rcfile', str(rc), '-i']
    try:
        subprocess.run(['tmux', '-S', state['socket'], '-f', '/dev/null',
                        'new-session', '-d', '-s', 'desktop', '-n', 'first',
                        '-c', str(directory), *shell], env=env, check=True,
                       capture_output=True, text=True)
        tmux(state, 'set-option', '-g', 'history-limit', '10000')
        tmux(state, 'new-window', '-d', '-t', 'desktop:', '-n', 'second',
             '-c', str(directory), *shell)
        tmux(state, 'new-session', '-d', '-s', 'phone', '-t', 'desktop')
        tmux(state, 'select-window', '-t', 'desktop:0')
        tmux(state, 'select-window', '-t', 'phone:0')
        state['pane_baseline'] = tmux(state, 'list-panes', '-a', '-F',
            '#{session_name}:#{window_id}:#{pane_id}:#{pane_pid}').stdout.splitlines()
        with (directory / 'ttyd.log').open('wb') as log:
            gateway = subprocess.Popen([str(BINARY), '-i', '127.0.0.1', '-p', str(port),
                '-W', '-O', '-c', credential, '-t', 'titleFixed=Phone terminal trial',
                'tmux', '-S', state['socket'], 'attach-session', '-t', 'phone'],
                env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        state['gateway_pid'] = gateway.pid
        (directory / 'state.json').write_text(json.dumps(state, indent=2) + '\n')
        (directory / 'state.json').chmod(0o600)
        for _ in range(50):
            if gateway.poll() is not None:
                raise RuntimeError('ttyd exited; inspect private log')
            try:
                with socket.create_connection(('127.0.0.1', port), timeout=.1):
                    break
            except OSError:
                time.sleep(.1)
        else:
            raise RuntimeError('ttyd did not listen')
    except BaseException:
        if 'gateway_pid' in state:
            os.kill(state['gateway_pid'], signal.SIGTERM)
        if Path(state['socket']).exists():
            tmux(state, 'kill-server')
        raise
    print(json.dumps({'directory': str(directory), 'url': f'http://127.0.0.1:{port}',
        'credential_file': str(directory / 'state.json'),
        'desktop_attach': f'tmux -S {state["socket"]} attach-session -t desktop',
        'stop': f'python3 {Path(__file__).resolve()} stop {directory}'}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('start').add_argument('--port', type=int, default=18789)
    sub.add_parser('stop').add_argument('directory', type=Path)
    args = parser.parse_args()
    start(args.port) if args.action == 'start' else stop(args.directory)
