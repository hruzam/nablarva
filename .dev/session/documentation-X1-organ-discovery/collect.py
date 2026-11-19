"""Pilot-only, read-only source inventory. Run from any cwd; JSON goes to stdout."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
BED = Path(__file__).resolve().parent
SESSION = ROOT / '.dev/session'
PATTERN = re.compile(r'termbrana|composer|composition', re.I)


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()


def inspect(path):
    data = path.read_bytes()
    rel = path.relative_to(ROOT).as_posix()
    return {
        'path': rel,
        'sha256': hashlib.sha256(data).hexdigest(),
        'tracked': bool(git('ls-files', '--', rel)),
        'matches': [
            {'line': n, 'text': line[:400]}
            for n, line in enumerate(data.decode('utf-8', errors='replace').splitlines(), 1)
            if PATTERN.search(line)
        ],
    }


sources = [ROOT / name for name in [
    'AGENTS.md', 'PROJECT.yaml', 'PROJECT-DESIGN.md', 'docs/ARCHITECTURE.md',
    'docs/decisions/README.md', '.germline/agents/houston/nablarva.md',
    '.dev/session/flag.md', '.dev/session/pulse.md', '.gitignore',
    'meshup/REGISTRY.md', 'toolbox/termbrana/README.md',
    'toolbox/termbrana/DECISIONS.md',
]]
beds = []
for bed in sorted(SESSION.iterdir()):
    if bed == BED or bed.is_symlink() or not bed.is_dir():
        continue
    entries = sorted(p for p in bed.glob('*.md') if not p.is_symlink())
    # A missing launcher must not hide prepared material from the discovery pass.
    raw = bed / 'raw'
    fallback = []
    if not entries and raw.is_dir() and not raw.is_symlink():
        fallback = sorted(p for p in raw.glob('*.md') if not p.is_symlink())
    files = entries + fallback
    sources.extend(files)
    beds.append({
        'slug': bed.name,
        'has_runbook': (bed / 'RUNBOOK.md').is_file(),
        'has_STATUS': (bed / 'STATUS.md').is_file(),
        'has_legacy_status': (bed / 'status.md').is_file(),
        'sources': [p.relative_to(ROOT).as_posix() for p in files],
    })

for path in sources:
    if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
        raise SystemExit(f'Outside source boundary or symlink: {path}')

print(json.dumps({
    'purpose': 'pilot corpus and lexical candidates, not relevance or authority',
    'head': git('rev-parse', 'HEAD'),
    'working_changes': git('status', '--short').splitlines(),
    'scope': 'declared project entries; other beds top-level Markdown; raw Markdown fallback where entry absent',
    'beds': beds,
    'sources': [inspect(p) for p in sorted(set(sources))],
}, indent=2, ensure_ascii=False))
