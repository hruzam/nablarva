"""Verify pilot source identities and navigation; JSON goes to stdout."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

BED = Path(__file__).resolve().parent
ROOT = BED.parents[2]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


manifest = json.loads((BED / 'source-manifest.json').read_text())
assert git('rev-parse', 'HEAD').decode().strip() == manifest['head'], 'HEAD moved'
for source in manifest['sources']:
    assert sha((ROOT / source['path']).read_bytes()) == source['sha256'], source['path']

# Cwd independence and repeatability of the bounded mechanical inventory.
again = json.loads(subprocess.check_output(
    [sys.executable, str(BED / 'collect.py')], cwd='/tmp', text=True))
assert again['beds'] == manifest['beds'], 'Bed discovery changed'
assert again['sources'] == manifest['sources'], 'Source inventory changed'

reader_hashes = re.findall(r'^([^\s]+) ([a-f0-9]{64})$',
                         (BED / 'repeat.md').read_text(), flags=re.M)
assert len(reader_hashes) == 8
for path, digest in reader_hashes:
    assert sha((ROOT / path).read_bytes()) == digest, f'Reader source mismatch: {path}'

supplemental = []
for rel in [
    'docs/repo-unification.2026-09-02.md',
    '.dev/session/termpanum-X0-source-contract/raw/source-contract.md',
    '.dev/session/nablarva-02-pipe-qualification/raw/fold.relay-seam-round2.2026-09-13.md',
]:
    data = (ROOT / rel).read_bytes()
    assert data == git('show', manifest['head'] + ':' + rel), rel
    supplemental.append({'path': rel, 'sha256': sha(data), 'matches_HEAD': True})

pin = ('78059da:.dev/session/nablarva-X3-architecture-sitting/raw/'
       'brief.nablarva-boost-reader-concept.2026-10-21.md')
historical = git('show', pin)
assert b'no implementation or schema approved' in historical

r = (BED / 'RUNBOOK.md').read_text()
s = (BED / 'STATUS.md').read_text()
gate = next(line for line in r.splitlines() if line.startswith('gate: '))
assert gate in s
assert gate[6:] in (ROOT / '.dev/session/pulse.md').read_text()
assert 'documentation-01-organ-discovery' not in (ROOT / '.dev/session/pulse.md').read_text()

for path in BED.glob('*.md'):
    content = path.read_text()
    assert not any(line.rstrip() != line for line in content.splitlines()), path.name
    for target in re.findall(r'\]\(([^)]+)\)', content):
        if '://' not in target:
            assert (path.parent / target.split('#', 1)[0]).exists(), (path.name, target)

changed_inputs = []
for source in manifest['sources']:
    if source['tracked']:
        committed = git('show', manifest['head'] + ':' + source['path'])
        if sha(committed) != source['sha256']:
            changed_inputs.append(source['path'])

print(json.dumps({
    'result': 'PASS',
    'head': manifest['head'],
    'manifest_sources_unchanged': len(manifest['sources']),
    'preexisting_beds': len(manifest['beds']),
    'inventory_reproduced_from_tmp': True,
    'independent_reader_hashes_matched': len(reader_hashes),
    'local_source_deltas_from_HEAD': changed_inputs,
    'supplemental_sources': supplemental,
    'historical_source': {'pin': pin, 'sha256': sha(historical)},
    'gate_and_navigation_checks': 'PASS',
    'limits': 'Mechanical source/navigation checks; no runtime, exhaustive orphan or effort benchmark.',
}, indent=2))
