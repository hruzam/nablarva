#!/usr/bin/env python3
"""Disposable-profile trial; requires the isolated upstream test bridge."""
import argparse
import json
from pathlib import Path
import statistics
import subprocess
import sys
import tempfile
import time
from urllib.request import Request, urlopen
import uuid

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trial-root', type=Path, required=True)
    parser.add_argument('--instance', required=True)
    parser.add_argument('--window', type=int, required=True)
    parser.add_argument('--port', type=int, required=True)
    args = parser.parse_args()
    root = args.trial_root.resolve()
    if not str(root).startswith('/tmp/nablarva-observer-'):
        raise SystemExit('trial must use a disposable /tmp/nablarva-observer-* profile')
    token = (root/'token').read_text()
    base = [sys.executable, '-I', '-S', '-B', str(ROOT/'observer.py'), '--runtime', str(root/'runtime')]
    def observe(*parts):
        run = subprocess.run(base + list(parts), text=True, capture_output=True, check=True, timeout=7)
        return json.loads(run.stdout)
    def open_file(path):
        req = Request('http://127.0.0.1:%d/open_file' % args.port,
                      headers={'Authorization': 'Bearer '+token, 'Content-Type':'application/json'},
                      data=json.dumps({'path':str(path)}).encode())
        with urlopen(req, timeout=5) as response:
            result = json.loads(response.read())
        if not result.get('ok'): raise RuntimeError(str(result))
    with tempfile.TemporaryDirectory(prefix='run-', dir=str(root)) as d:
        runroot = Path(d)
        for label in ('A', 'B'): (runroot/label).mkdir()
        script = runroot/'experiment.py'
        script.write_text("from pathlib import Path\nimport sys\ndestination = 'A'\nr = Path(sys.argv[1]); marker = sys.argv[2]\np = r / destination / 'same.md'\np.write_text('RUN:' + marker + ':BEGIN\\n' + destination + '\\nRUN:' + marker + ':END\\n')\nprint(p)\n")
        before = observe('tabs', '--instance', args.instance, '--window', str(args.window))
        expected = runroot/'B/same.md'
        def run_once():
            run_id = observe('new-run', '--instance', args.instance, '--window', str(args.window))['run_id']
            result = subprocess.run([sys.executable, '-I', '-S', '-B', str(script), str(runroot), run_id],
                                    capture_output=True, text=True, check=True, timeout=5)
            actual = Path(result.stdout.strip()); open_file(actual)
            tabs = observe('tabs', '--instance', args.instance, '--window', str(args.window))
            matches = [v for v in tabs['views'] if v['path'] == str(actual)]
            if len(matches) != 1: raise RuntimeError('run target view is ambiguous')
            view = matches[0]['view']
            captured = observe('wait', '--instance', args.instance, '--window', str(args.window),
                               '--view', str(view), '--run-id', run_id)
            return {'run_id':run_id, 'script_exit':result.returncode, 'actual':str(actual),
                    'expected':str(expected), 'view':view,
                    'target_matches':actual == expected, 'marker_matches':captured['run_id']==run_id,
                    'revision':captured['revision'], 'truncated':captured['truncated']}
        wrong = run_once()
        if wrong['target_matches']: raise RuntimeError('deliberately wrong target was not detected')
        script.write_text(script.read_text().replace("destination = 'A'", "destination = 'B'"))
        corrected = run_once()
        if not corrected['target_matches'] or not corrected['marker_matches']: raise RuntimeError('corrected run not verified')
        times=[]
        for _ in range(30):
            start=time.monotonic()
            observe('state','--instance',args.instance,'--window',str(args.window),'--view',str(corrected['view']))
            times.append((time.monotonic()-start)*1000)
        ordered=sorted(times)
        print(json.dumps({'before_views':len(before['views']), 'wrong':wrong, 'corrected':corrected,
                          'warm_samples':len(times),'median_ms':round(statistics.median(times),2),
                          'p95_ms':round(ordered[28],2)},indent=2))

if __name__ == '__main__': main()
