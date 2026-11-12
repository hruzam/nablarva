# Synthetic performance on home · 2026-11-07

Command from `/home/hruzam/unikuklatrix/nablarva`:

```sh
python3 -I -S -B .dev/session/termbrana-M0-markdown-test/benchmark.sandbox.py
```

This run used fictional records and disposable temporary files, with no native
history or editor interaction. The process ran on home with unrestricted
filesystem access. Each result is one observation, not a distribution.

| Records | Source bytes | Cold render | Render peak RSS | Warm pin | Pin peak RSS | Append available |
|---:|---:|---:|---:|---:|---:|---:|
| 100 | 39,390 | 0.0966 s | 24,868 KiB | 0.0937 s | 24,164 KiB | 0.2111 s |
| 2,000 | 790,890 | 0.5392 s | 33,000 KiB | 0.0933 s | 26,812 KiB | 0.8360 s |

The watcher used a 0.2 s poll interval and exited successfully for both cases.
First idle polls including process startup took 0.0781 s and 0.2284 s. Those
figures do not isolate steady-state idle CPU or memory cost. The larger append
measurement exceeds one poll interval because it includes processing. No weak
host measurement or operator usability judgment is implied.

An additional Linux `/proc` sample measured the watcher process on unchanged
2,000-record input, excluding its initial setup. Command:

```sh
python3 -I -S -B .dev/session/termbrana-M0-markdown-test/benchmark.idle-home.py
```

Over 2.244 seconds and six unchanged cycles at the 0.2-second interval, process
CPU rose by 1.04 seconds, approximately 46.3% of one core; the last observed
RSS was 29,176 KiB. This is one short run and a cost concern, not a general
hardware benchmark or an operator usability judgment.
Running the saved script again gave 0.94 CPU seconds over 2.139 seconds
(43.9% of one core), with 29,180 KiB last observed RSS.

Investigation found that synthetic `load_codex` checked every record ID by
scanning previous records. Replacing that local duplicate lookup with a set
retains full-source parsing and continuity validation. After the change, the
same saved benchmark measured 0.28 CPU seconds over 1.494 seconds (18.7% of
one core), with 29,168 KiB last observed RSS. This remains one short observation;
the 0.2-second polling interval is not a resource-free idle setting.
