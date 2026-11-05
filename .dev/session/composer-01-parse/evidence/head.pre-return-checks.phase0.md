---
author: Cartan · head checks of in-progress cycle 23
date: 2026-10-20
scope: observed draft defects; not acceptance of the completed artifact
---

## Output failure — observed before builder RETURN

Expected: operational I/O failure exits 74 with safe operational output.
Observed on the draft: exit 120 and Python shutdown-flush error prose.
The bytes parser had completed; buffered stdout failed outside main's handler.
Returned to Astrobley before its cycle-23 RETURN for correction and regression test.

Executed with `PYTHONDONTWRITEBYTECODE=1 python3`:

```python
from pathlib import Path
import subprocess
p = Path('/tmp/termbrana-phase0.wkjBVb/termbrana/composer.py')
f = Path('/home/hruzam/unikuklatrix/nablarva/.dev/session/composer-01-parse/evidence/fixtures/packet.handwritten.v4.md')
with open('/dev/full', 'wb') as sink:
    r = subprocess.run(['python3', '-B', str(p), 'parse', str(f)],
                       stdout=sink, stderr=subprocess.PIPE)
print(r.returncode, repr(r.stderr))
```

Observed output:

```text
120 b'Exception ignored while flushing sys.stdout:\nOSError: [Errno 28] No space left on device\n'
```

The temporary path is historical staging. Final source-path verification belongs
to cycle 23/24 evidence. No product/exchange file was modified by this probe.

## Defaults — no defect

Cartan questioned absent-context default during draft inspection. Astrobley cited
v4 §5, line 213; focused reread confirmed that both consult and context explicitly
default to empty lists. SHA256 remained the approved a977682c…9b2ec. The original
implementation choice was correct and no grammar correction was requested.
