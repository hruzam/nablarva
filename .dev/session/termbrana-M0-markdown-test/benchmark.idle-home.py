#!/usr/bin/env python3
"""Measure unchanged synthetic watcher CPU on Linux; no native history."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

root = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('bench', root / 'benchmark.sandbox.py')
bench = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bench)
with tempfile.TemporaryDirectory(prefix='tbv-idle-') as temporary:
    folder = Path(temporary)
    source = folder / 'input.jsonl'
    source.write_text(''.join(bench.row(i) for i in range(2000)))
    command = [sys.executable, '-I', '-S', '-B', str(bench.ROOT / 'collector.py'),
               'watch', '--vendor', 'codex', '--vendor-version', 'synthetic',
               '--project', bench.PROJECT, '--source', str(source), '--cache',
               str(folder / 'cache'), '--interval', '0.2', '--cycles', '8']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, bufsize=1)
    samples = []
    hz = os.sysconf('SC_CLK_TCK')
    for line in process.stdout:
        result = json.loads(line)
        assert result['ok'], result
        stat = Path('/proc/%d/stat' % process.pid).read_text().split()
        status = Path('/proc/%d/status' % process.pid).read_text().splitlines()
        rss = next((int(row.split()[1]) for row in status if row.startswith('VmRSS:')), None)
        samples.append((time.monotonic(), (int(stat[13]) + int(stat[14])) / hz, rss))
    error = process.stderr.read()
    code = process.wait()
    assert code == 0, error
    first, last = samples[1], samples[-1]
    wall, cpu = last[0] - first[0], last[1] - first[1]
    print(json.dumps({'records': 2000, 'unchanged_idle_cycles': len(samples) - 2,
                      'poll_interval_s': 0.2, 'measured_wall_s': round(wall, 3),
                      'process_cpu_s': round(cpu, 3),
                      'process_cpu_percent_one_core': round(100 * cpu / wall, 1),
                      'last_rss_kib': last[2], 'exit': code}))
