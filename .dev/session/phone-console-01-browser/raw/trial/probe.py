#!/usr/bin/env python3
"""Local-only synthetic HTTP/WS checks against gateway.py's dedicated fixture."""
import base64
import hashlib
import http.client
import json
import os
from pathlib import Path
import socket
import struct
import sys
import time

from gateway import tmux


class WS:
    def __init__(self, state, authorization=None, origin=None):
        self.sock = socket.create_connection(('127.0.0.1', state['port']), timeout=2)
        self.sock.settimeout(2)
        self.buffer = b''
        key = base64.b64encode(os.urandom(16)).decode()
        headers = [f'GET /ws HTTP/1.1', f'Host: 127.0.0.1:{state["port"]}',
                   'Connection: Upgrade', 'Upgrade: websocket',
                   'Sec-WebSocket-Version: 13', f'Sec-WebSocket-Key: {key}',
                   'Sec-WebSocket-Protocol: tty']
        if authorization:
            headers.append('Authorization: Basic ' + authorization)
        if origin:
            headers.append('Origin: ' + origin)
        self.sock.sendall(('\r\n'.join(headers) + '\r\n\r\n').encode())
        while b'\r\n\r\n' not in self.buffer:
            part = self.sock.recv(4096)
            if not part:
                break
            self.buffer += part
        header, _, self.buffer = self.buffer.partition(b'\r\n\r\n')
        self.accepted = header.startswith(b'HTTP/1.1 101')
        if self.accepted:
            expected = base64.b64encode(hashlib.sha1((key +
                '258EAFA5-E914-47DA-95CA-C5AB0DC85B11').encode()).digest())
            assert expected.lower() in header.lower(), 'Invalid WebSocket accept key'

    def send(self, data, opcode=2):
        mask = os.urandom(4)
        length = len(data)
        prefix = bytes([0x80 | opcode])
        prefix += bytes([0x80 | length]) if length < 126 else bytes([0x80 | 126]) + struct.pack('!H', length)
        self.sock.sendall(prefix + mask + bytes(c ^ mask[i % 4] for i, c in enumerate(data)))

    def read(self, count):
        while len(self.buffer) < count:
            part = self.sock.recv(65536)
            if not part:
                raise EOFError('WebSocket closed')
            self.buffer += part
        data, self.buffer = self.buffer[:count], self.buffer[count:]
        return data

    def frame(self):
        first, second = self.read(2)
        length = second & 127
        if length == 126:
            length = struct.unpack('!H', self.read(2))[0]
        elif length == 127:
            length = struct.unpack('!Q', self.read(8))[0]
        return first & 15, self.read(length)

    def close(self):
        self.sock.close()


def run(directory):
    state = json.loads((directory / 'state.json').read_text())
    auth = base64.b64encode(state['credential'].encode()).decode()
    origin = f'http://127.0.0.1:{state["port"]}'
    results = {}
    for path in ['/', '/token']:
        for name, credential, expected in [('missing', None, 401),
                ('wrong', 'aW52YWxpZA==', 401), ('valid', auth, 200)]:
            connection = http.client.HTTPConnection('127.0.0.1', state['port'], timeout=2)
            headers = {'Authorization': 'Basic ' + credential} if credential else {}
            connection.request('GET', path, headers=headers)
            response = connection.getresponse()
            response.read()  # Token content deliberately never logged.
            connection.close()
            results[f'http {path} {name}'] = response.status
            assert response.status == expected, (path, name, response.status)
    for name, credential, supplied_origin, expected in [
            ('missing auth', None, origin, False),
            ('wrong auth', 'aW52YWxpZA==', origin, False),
            ('foreign origin', auth, 'http://foreign.invalid', False),
            ('wrong port', auth, 'http://127.0.0.1:18790', False),
            ('missing origin', auth, None, False),
            ('valid', auth, origin, True),
            ('different scheme limitation', auth, origin.replace('http:', 'https:'), True)]:
        ws = WS(state, credential, supplied_origin)
        results['ws ' + name] = ws.accepted
        ws.close()
        assert ws.accepted == expected, (name, ws.accepted)
    def connect():
        ws = WS(state, auth, origin)
        assert ws.accepted
        ws.send(json.dumps({'AuthToken': auth, 'columns': 80, 'rows': 24}).encode())
        # Wait for terminal output; title/preferences alone do not prove child start.
        for _ in range(20):
            opcode, data = ws.frame()
            if opcode == 2 and data.startswith(b'0'):
                return ws
        raise AssertionError('No terminal output')
    before = tmux(state, 'display-message', '-p', '-t', 'phone:0.0', '#{pane_pid}').stdout.strip()
    ws = connect()
    output = directory / ('unicode-' + os.urandom(4).hex() + '.txt')
    text = 'příliš žluťoučký kůň'
    command = f"printf %s '{text}' > {output}"
    ws.send(b'0' + command.encode())
    time.sleep(.2)
    assert not output.exists(), 'Paste unexpectedly executed before explicit Enter'
    results['paste without Enter'] = 'no file created'
    ws.send(b'0\r')
    deadline = time.monotonic() + 3
    while not output.exists() and time.monotonic() < deadline:
        time.sleep(.05)
    assert output.read_bytes() == text.encode(), 'Unicode bytes differ'
    results['explicit Enter Unicode'] = {'bytes': len(text.encode()), 'exact': True}
    ws.close()
    ws = connect()
    after = tmux(state, 'display-message', '-p', '-t', 'phone:0.0', '#{pane_pid}').stdout.strip()
    ws.close()
    assert before == after, 'Reconnect replaced underlying shell'
    results['reconnect'] = {'same_pane_pid': before == after, 'pane_pid': after}
    tmux(state, 'select-window', '-t', 'phone:1')
    selected = tmux(state, 'list-sessions', '-F', '#{session_name}:#{window_index}').stdout.splitlines()
    assert 'desktop:0' in selected and 'phone:1' in selected, selected
    tmux(state, 'select-window', '-t', 'phone:0')
    results['independent selection'] = selected
    results['scope'] = 'Synthetic local checks only; no physical IME/keyboard/native CLI approval claim'
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    run(Path(sys.argv[1]))
