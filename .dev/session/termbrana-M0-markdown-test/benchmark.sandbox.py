#!/usr/bin/env python3
"""Synthetic disposable benchmark; no native histories or editor access."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parent / 'implementation/termbrana'
PROJECT = '/tmp/transcript-benchmark-project'

def row(i):
    return json.dumps({'timestamp': '2026-11-06T00:00:00Z', 'type': 'event_msg',
        'payload': {'id': f'item-{i}', 'type': 'user_message',
        'message': 'Synthetic benchmark line ' * 8, 'thread_id': 'bench',
        'session_id': 'bench', 'branch_id': 'main'}}) + '\n'

def timed(args):
    start = time.monotonic()
    pid = os.fork()
    if not pid:
        fd = os.open(os.devnull, os.O_WRONLY)
        os.dup2(fd, 1); os.dup2(fd, 2)
        os.execvp(args[0], args)
    _, status, usage = os.wait4(pid, 0)
    return {'seconds': round(time.monotonic() - start, 4), 'peak_kib': usage.ru_maxrss,
            'exit': os.waitstatus_to_exitcode(status)}

def main():
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        for count in (100, 2000):
            source, cache = root / f'{count}.jsonl', root / f'cache-{count}'
            source.write_text(''.join(row(i) for i in range(count)))
            python = ['python3', '-I', '-S', '-B']
            render = python + [str(ROOT / 'transcript.py'), 'render', '--vendor', 'codex',
                '--vendor-version', 'synthetic', '--project', PROJECT, '--source', str(source), '--out', str(cache)]
            pin = python + [str(ROOT / 'transcript.py'), 'pin', '--cache', str(cache), '--record', f'item-{count-1}']
            print(json.dumps({'records': count, 'bytes': source.stat().st_size, 'render': timed(render), 'warm_pin': timed(pin)}), flush=True)
            watch = python + [str(ROOT / 'collector.py'), 'watch', '--vendor', 'codex', '--vendor-version', 'synthetic',
                '--project', PROJECT, '--source', str(source), '--cache', str(cache), '--interval', '0.2', '--cycles', '5']
            watch_start = time.monotonic()
            process = subprocess.Popen(watch, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
            first = json.loads(process.stdout.readline())
            idle_poll_seconds = time.monotonic() - watch_start
            started = time.monotonic()
            with source.open('a') as handle:
                handle.write(row(count)); handle.flush()
            observed = None
            for line in process.stdout:
                result = json.loads(line)
                if result.get('new_records_available') and observed is None:
                    observed = time.monotonic() - started
            stderr = process.stderr.read(); exit_code = process.wait()
            print(json.dumps({'records': count, 'poll_interval_s': 0.2,
                'first_poll_ok': first.get('ok'), 'first_idle_poll_with_startup_s': round(idle_poll_seconds, 4),
                'append_availability_s': round(observed, 4) if observed is not None else None,
                'watch_exit': exit_code, 'watch_error': stderr}), flush=True)

if __name__ == '__main__':
    main()
