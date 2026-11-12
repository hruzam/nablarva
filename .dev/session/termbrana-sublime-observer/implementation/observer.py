#!/usr/bin/env python3
"""Inspect a specifically addressed Sublime view through the read-only observer."""
import argparse
import fcntl
import json
import os
from pathlib import Path
import re
import socket
import stat
import sys
import time
import uuid

MAX_RESPONSE = 1500000


class JsonParser(argparse.ArgumentParser):
    def error(self, message):
        print(json.dumps({'ok': False, 'error': {'code': 'usage', 'message': message}}), file=sys.stderr)
        raise SystemExit(2)


def registry_path(runtime):
    path = Path(runtime or os.environ.get('XDG_RUNTIME_DIR', ''))
    if not path.is_absolute() or not path.is_dir():
        raise ValueError('supply an existing absolute --runtime or XDG_RUNTIME_DIR')
    root = path / 'sublime-observer'
    for directory in (path, root):
        if directory.exists():
            details = directory.lstat()
            if not stat.S_ISDIR(details.st_mode) or details.st_uid != os.getuid() or details.st_mode & 0o077:
                raise ValueError('runtime and observer registry must be private directories owned by this user')
    return root


def instances(root):
    if not root.is_dir():
        return []
    found = []
    for path in sorted(root.glob('*.json')):
        try:
            value = json.loads(path.read_text())
            if (value.get('instance') == path.stem and
                Path(value['socket']).parent == root and Path(value['socket']).name == path.stem + '.sock'):
                with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as probe:
                    probe.settimeout(0.1)
                    value['reachable'] = probe.connect_ex(value['socket']) == 0
                found.append(value)
        except (OSError, ValueError, KeyError, TypeError):
            continue
    return found


def request(info, payload, timeout):
    request_id = uuid.uuid4().hex
    payload['request_id'] = request_id
    deadline = time.monotonic() + timeout
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.settimeout(timeout)
        client.connect(info['socket'])
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError('observer request deadline expired')
        client.settimeout(remaining)
        client.sendall((json.dumps(payload) + '\n').encode())
        data = bytearray()
        while b'\n' not in data:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError('observer response deadline expired')
            client.settimeout(remaining)
            chunk = client.recv(65536)
            if not chunk:
                raise ValueError('observer closed without a response')
            data.extend(chunk)
            if len(data) > MAX_RESPONSE:
                raise ValueError('observer response exceeds size limit')
    result = json.loads(bytes(data).split(b'\n', 1)[0])
    if result.get('error', {}).get('code') == 'busy' and result.get('request_id') is None:
        return result
    if result.get('request_id') != request_id:
        raise ValueError('observer response request ID mismatch')
    if result.get('instance') not in (None, info['instance']):
        raise ValueError('observer instance does not match descriptor')
    return result


def main():
    parser = JsonParser(description=__doc__)
    parser.add_argument('--runtime', help='private runtime directory (default: XDG_RUNTIME_DIR)')
    parser.add_argument('--timeout', type=float, default=5)
    subs = parser.add_subparsers(dest='operation', required=True, parser_class=JsonParser)
    subs.add_parser('instances')
    for name in ('windows', 'tabs', 'read', 'selection', 'state', 'wait', 'new-run'):
        sub = subs.add_parser(name)
        sub.add_argument('--instance', required=True)
        if name != 'windows':
            sub.add_argument('--window', required=True, type=int)
        if name in ('read', 'selection', 'state', 'wait'):
            sub.add_argument('--view', required=True, type=int)
            sub.add_argument('--expected-revision', type=int)
        if name == 'read':
            sub.add_argument('--lines', help='one-based inclusive start:end')
            sub.add_argument('--max-chars', type=int, default=200000)
        if name == 'wait':
            sub.add_argument('--run-id', required=True, help='unique marker used by the experiment')
            sub.add_argument('--interval', type=float, default=0.1)
    args = parser.parse_args()
    try:
        if args.timeout <= 0 or args.timeout > 30:
            raise ValueError('timeout must be greater than zero and at most 30 seconds')
        all_instances = instances(registry_path(args.runtime))
        if args.operation == 'instances':
            result = {'ok': True, 'instances': all_instances}
        else:
            info = next((x for x in all_instances if x['instance'] == args.instance), None)
            if not info:
                raise ValueError('instance not found; it may have exited or reloaded')
            payload = {'operation': 'read' if args.operation == 'wait' else ('windows' if args.operation == 'new-run' else args.operation), 'instance': args.instance}
            for field in ('window', 'view', 'expected_revision', 'max_chars'):
                if hasattr(args, field) and getattr(args, field) is not None:
                    payload[field] = getattr(args, field)
            if getattr(args, 'lines', None):
                pair = args.lines.split(':')
                if len(pair) != 2:
                    raise ValueError('lines must be start:end')
                payload['start_line'], payload['end_line'] = map(int, pair)
            if args.operation == 'new-run':
                state = request(info, payload, args.timeout)
                if not state.get('ok') or args.window not in [w['id'] for w in state.get('windows', [])]:
                    raise ValueError('requested window is not available')
                root = registry_path(args.runtime)
                now = time.time()
                for stale in root.glob('run-*.token'):
                    try:
                        if now - stale.stat().st_mtime > 86400:
                            stale.unlink()
                    except OSError:
                        pass
                run_id = uuid.uuid4().hex
                token_path = root / ('run-' + run_id + '.token')
                fd = os.open(str(token_path), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
                with os.fdopen(fd, 'w') as handle:
                    json.dump({'instance': args.instance, 'window': args.window, 'issued_at': now}, handle)
                result = {'ok': True, 'run_id': run_id, 'instance': args.instance, 'window': args.window,
                          'markers': ['RUN:' + run_id + ':BEGIN', 'RUN:' + run_id + ':END'], 'expires_in_seconds': 3600}
            elif args.operation == 'wait':
                if not re.fullmatch('[0-9a-f]{32}', args.run_id) or args.interval <= 0:
                    raise ValueError('run ID must be issued by new-run and interval must be positive')
                token_path = registry_path(args.runtime) / ('run-' + args.run_id + '.token')
                fd = os.open(str(token_path), os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0))
                with os.fdopen(fd, 'r') as token_handle:
                    fcntl.flock(token_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    token = json.load(token_handle)
                    if token.get('instance') != args.instance or token.get('window') != args.window:
                        raise ValueError('run ID belongs to a different instance or window')
                    if time.time() - token.get('issued_at', 0) > 3600:
                        raise ValueError('run ID expired')
                    deadline = time.monotonic() + args.timeout
                    begin, end = 'RUN:' + args.run_id + ':BEGIN', 'RUN:' + args.run_id + ':END'
                    while True:
                        remaining = deadline - time.monotonic()
                        if remaining <= 0:
                            raise ValueError('readiness deadline expired before both run markers appeared')
                        result = request(info, dict(payload), remaining)
                        if result.get('ok'):
                            content = result.get('text', '')
                            if result.get('truncated'):
                                raise ValueError('buffer truncated; cannot establish readiness')
                            if begin in content and end in content and content.index(begin) < content.index(end):
                                result['run_id'] = args.run_id
                                token_path.unlink()
                                break
                        elif result.get('error', {}).get('code') != 'loading':
                            break
                        time.sleep(min(args.interval, max(0, deadline - time.monotonic())))
            else:
                result = request(info, payload, args.timeout)
        if not result.get('ok'):
            print(json.dumps(result, ensure_ascii=False), file=sys.stderr)
            return 1
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({'ok': False, 'error': {'code': 'request_failed', 'message': str(exc)}}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
