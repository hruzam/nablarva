crawl: r5-r7-repin · writer: oraculum(cSharp) X3 head (carrier Bash, bookkeeping commands only) · run at: 2026-10-22 11:08 CEST · answers Houston arc.r2 §8 R-5, R-7 (R-6 answered 07:19: v0 folder untracked)

## R-5 (diff base at drafting time)

```zsh
git -C /home/hruzam/unikuklatrix/nablarva rev-parse HEAD
```
```text
78059da137f2b6d17192c251220d80b148aa1ac6
```

```zsh
git -C /home/hruzam/unikuklatrix/nablarva hash-object PROJECT-DESIGN.md
```
```text
74e94d5519be6a2de1565ad686ab16cdff6c64c2
```

```zsh
sha256sum /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md
```
```text
6ee10aa1c40a853cc6c1e6ff5dfa191999f38314058064b5543ac1392fe2c78f  /home/hruzam/unikuklatrix/nablarva/PROJECT-DESIGN.md
```

```zsh
git -C /home/hruzam/unikuklatrix/nablarva status --short -- PROJECT-DESIGN.md docs/ .dev/session/flag.md .dev/session/pulse.md
```
```text
(no output — all clean against HEAD)
```

HEAD moved since R0 (32bd6f4 → 78059da). The commits in between:

```zsh
git -C /home/hruzam/unikuklatrix/nablarva log --format='%h %cs %an %s' 32bd6f4..HEAD
```
```text
78059da 2026-10-22 hruzam composer: record preservation pushes and retain X1 park
745d732 2026-10-22 hruzam composer: preserve Phase 0 evidence and practitioner handoffs
```

```zsh
git -C /home/hruzam/unikuklatrix/nablarva diff --stat 32bd6f4 HEAD -- .dev/session/nablarva-X3-architecture-sitting PROJECT-DESIGN.md docs/ .dev/session/flag.md .dev/session/pulse.md AGENTS.md PROJECT.yaml .germline/ toolbox/
```
```text
 ...andoff.composer-boundaries.cartan.2026-10-22.md | 33 ++++++++++++++++++++++
 1 file changed, 33 insertions(+)
```
(The full diffstat for the rest of the tree covers composer-01-parse files only and is not reproduced here.)

## R-7 (X2 freshness against the 07:12 pins)

```zsh
sha256sum /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/RUNBOOK.md /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/STATUS.md /home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-X2-builder-narative/raw/termpanum.build-plan.md
```
```text
7d1501842d93c781d9aefc7e3b4dc7663eca84350a482898bb19fdbcd0d501a1  …/RUNBOOK.md        (= 07:12 pin)
06fa45c8a075d70e61a8535335e8aa3b2c78398ac11c9d3a5be38a2ad20944f6  …/STATUS.md         (07:12 pin was ddc8bc0a… — MOVED)
4e039f9f787c3224e8bb8c63342d3cdf68027339dd51ace682db89e430c83145  …/raw/termpanum.build-plan.md (= 07:12 pin)
```
X2's STATUS moved, which is expected after the cartan-x2 disposition (raw/disposition.x3-vectors.cartan.2026-10-22.md, sha256 efe7573d…68f7b). The reviewed plan bytes are unchanged. Read X2's STATUS yourself if a changed section matters; cite it by the new hash.
