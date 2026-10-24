so 24. října 2026, 04:02:49 CEST

## Preconditions

```
ls -la .dev/session/architecture-X0-spine-and-skin/raw/Nabla-Tmux-Architecture-Draft-v0.zip
-rw-r--r-- 1 hruzam hruzam 16039 24. říj 03.51 .dev/session/architecture-X0-spine-and-skin/raw/Nabla-Tmux-Architecture-Draft-v0.zip
```
```
ls -d .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0
ls: cannot access '.dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0': No such file or directory
```

## Step 1: sha256sum

```
sha256sum .dev/session/architecture-X0-spine-and-skin/raw/Nabla-Tmux-Architecture-Draft-v0.zip
```
```
a7d28babe12277292f204fe6801d58b04087a3d3715068e1254b8683415e0ae7  .dev/session/architecture-X0-spine-and-skin/raw/Nabla-Tmux-Architecture-Draft-v0.zip
```

## Step 2: unzip -l (listing only)

```
unzip -l .dev/session/architecture-X0-spine-and-skin/raw/Nabla-Tmux-Architecture-Draft-v0.zip
```
```
Archive:  .dev/session/architecture-X0-spine-and-skin/raw/Nabla-Tmux-Architecture-Draft-v0.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
    23437  2026-10-17 18:14   nabla-tmux-architecture/Nabla-Tmux-Architecture-Draft-v0.md
     4327  2026-10-17 18:14   nabla-tmux-architecture/diagrams/events.svg
     4186  2026-10-17 18:14   nabla-tmux-architecture/diagrams/layers.svg
     3455  2026-10-17 18:14   nabla-tmux-architecture/diagrams/messages.svg
     4689  2026-10-17 18:14   nabla-tmux-architecture/diagrams/tree-and-mycelium.svg
     3143  2026-10-17 18:14   nabla-tmux-architecture/diagrams/what-loads-when.svg
---------                     -------
    43237                     6 files
```

## Step 3: STOP

Refused before extraction. The listing has no `..` or absolute paths, but five entries are `.svg` files (`nabla-tmux-architecture/diagrams/*.svg`), which are not in the allowed text set (.md/.txt/.yaml/.yml/.json/.toml/.sh/.zsh/.py). Steps 3 (extract), 4 (per-file wc/sha256/head), and 5 (comparison against 519a211) were not run. No directory was created.

## git status

```
?? .dev/session/architecture-X0-spine-and-skin/
```

---

resumed so 24. října 2026, 04:03:42 CEST (coordinator allow-list correction: .svg permitted as plain XML text; extract, never render; only wc/sha256sum/head/file)

## Step 3 (resumed): mkdir + unzip -n

```
mkdir .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0
unzip -n .dev/session/architecture-X0-spine-and-skin/raw/Nabla-Tmux-Architecture-Draft-v0.zip -d .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0
Archive:  .dev/session/architecture-X0-spine-and-skin/raw/Nabla-Tmux-Architecture-Draft-v0.zip
  inflating: .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/Nabla-Tmux-Architecture-Draft-v0.md
  inflating: .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/events.svg
  inflating: .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/layers.svg
  inflating: .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/messages.svg
  inflating: .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/tree-and-mycelium.svg
  inflating: .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/what-loads-when.svg
```

Path check: all entries under nabla-tmux-architecture/, no `..`, no absolute paths. Non-text entries are .svg only (allowed per correction).

## Step 4 (resumed): per-file wc -l, sha256sum, head -3

```
== Nabla-Tmux-Architecture-Draft-v0.md
382
00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0  .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/Nabla-Tmux-Architecture-Draft-v0.md
# Nabla.Tmux — Architecture Draft v0

Oct 17, 2026 · @Michal Hrůza
== diagrams/events.svg
1
1fe20f9c21c29d30e71d6f8386a50f0070402c00b57351e092a049d3993064a1  .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/events.svg
<svg xmlns="http://www.w3.org/2000/svg" width="760" height="504" font-family="system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif" viewBox="0 0 760 504" role="img" aria-label="Every source writes the same record; readers can ch
== diagrams/layers.svg
1
12211e4ce39ec1d220a4ce32561c9f95d95661b1151637d0ce365ddfaecc49d4  .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/layers.svg
<svg xmlns="http://www.w3.org/2000/svg" width="760" height="448" font-family="system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif" viewBox="0 0 760 448" role="img" aria-label="Only boot loads with the shell; the rest waits to b
== diagrams/messages.svg
1
7db75b063b6c8c7a58078f6e9d4eab55e7347e324c75a25ce5814b96abb78b2b  .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/messages.svg
<svg xmlns="http://www.w3.org/2000/svg" width="760" height="488" font-family="system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif" viewBox="0 0 760 488" role="img" aria-label="Every message is a file; tmux only rings the doorbe
== diagrams/tree-and-mycelium.svg
1
985cd8c9ed3dd5e279b1453dd4e79e2fc8de2401a03680412a2b0af98daf4aea  .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/tree-and-mycelium.svg
<svg xmlns="http://www.w3.org/2000/svg" width="760" height="488" font-family="system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif" viewBox="0 0 760 488" role="img" aria-label="Commands flow down the tree; facts spread through t
== diagrams/what-loads-when.svg
1
936a483d95b8b2ecf4623a7b2f27af559cd4a2630318a4d3684df966a050abc6  .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/what-loads-when.svg
<svg xmlns="http://www.w3.org/2000/svg" width="760" height="368" font-family="system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif" viewBox="0 0 760 368" role="img" aria-label="A new shell reads three small files; a call reads o
```

### .svg: file + head -3 only (lines truncated to 240 chars in this report)

```
.dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/events.svg:            SVG Scalable Vector Graphics image
.dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/layers.svg:            SVG Scalable Vector Graphics image
.dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/messages.svg:          SVG Scalable Vector Graphics image
.dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/tree-and-mycelium.svg: SVG Scalable Vector Graphics image
.dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/diagrams/what-loads-when.svg:   SVG Scalable Vector Graphics image
```

## Step 5 (resumed): comparisons with 519a211

```
git show 519a211:.dev/session/nablarva-X3-architecture-sitting/raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.md | sha256sum
00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0  -
git show 519a211:.dev/session/nablarva-X3-architecture-sitting/raw-additional-my-appology/Nabla-Tmux-Architecture-Draft-v0.zip | sha256sum
a7d28babe12277292f204fe6801d58b04087a3d3715068e1254b8683415e0ae7  -
sha256sum .dev/session/architecture-X0-spine-and-skin/raw/Nabla-Tmux-Architecture-Draft-v0.zip
a7d28babe12277292f204fe6801d58b04087a3d3715068e1254b8683415e0ae7  .dev/session/architecture-X0-spine-and-skin/raw/Nabla-Tmux-Architecture-Draft-v0.zip
sha256sum .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/Nabla-Tmux-Architecture-Draft-v0.md
00251ebf6dc1d4b4b7f6b84fbee016c81b08eb0037ec9458a85b86cf704b66a0  .dev/session/architecture-X0-spine-and-skin/raw/nabla-tmux-v0/nabla-tmux-architecture/Nabla-Tmux-Architecture-Draft-v0.md
```

Result: extracted .md == committed .md (00251ebf...); raw zip == committed zip (a7d28bab...), byte-identical.

## git status (resumed)

```
?? .dev/session/architecture-X0-spine-and-skin/
```
