# Stage 1 continuity finding

On home, candidate `implementation/termbrana/transcript.py` passes five unit tests via:

```sh
python3 -I -S -B -m unittest discover -s /home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana/tests -v
```

However, the following disposable test prints `True`: the old pin survives a truncate and regrow on the same inode when the retained prefix is identical. The RUNBOOK requires explicit failure after truncation/replacement/regrow and also requires pins to survive append/resume. The candidate compares inode and complete-prefix bytes; these observations alone do not distinguish this regrow from append.

```sh
python3 -I -S -B - <<'PY'
import importlib.util, pathlib, tempfile
p = pathlib.Path('/home/hruzam/unikuklatrix/nablarva/.dev/session/termbrana-M0-markdown-test/implementation/termbrana')
spec = importlib.util.spec_from_file_location('transcript', p / 'transcript.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
with tempfile.TemporaryDirectory() as d:
    s = pathlib.Path(d) / 'source.jsonl'
    out = pathlib.Path(d) / 'read.md'
    raw = (p / 'fixtures/codex-0.166.synthetic.jsonl').read_bytes()
    s.write_bytes(raw)
    m.render(s, out)
    with s.open('wb') as f:
        f.write(raw + b' new generation')
    data = m.read_valid_map(pathlib.Path(str(out) + '.map.json'))
    print('truncate/regrow same inode: old pin accepted:', 'item-user-003' in data['pins'])
PY
```

Observed: `truncate/regrow same inode: old pin accepted: True`. This does not prove that all vendor sources lack a stronger native generation identity; those identities remain unqualified. The fixture IDs are invented, not evidence of native identity. The candidate also writes view and map separately; digest checking detects mismatch at pin lookup, but publication is not serialized and a direct reader may see an unpaired generation. No UI, native-history, Claude adapter or publication qualification is claimed.
