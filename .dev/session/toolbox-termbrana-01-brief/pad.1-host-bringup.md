# pad.1-host-bringup — install + lock zellij and the Rust/WASM toolchain (office)

> Operator bring-up surface. Sequential — one step, report back, next step.
> Driver: the architect seat of this session.
> Status: DRAFT until A1–A4 gavel; safe to run any time — every step is additive to the host.

Pin targets (from `research.epoch.host-versions.2026-08-15.md` — Epoch, live-verified 2026-08-15):
- zellij **0.44.3** via pacman `extra` (in sync with upstream)
- rustc **1.95.0** via rustup (matches Zellij upstream CI `rust-toolchain.toml`)
- WASM target **wasm32-wasip1** (`wasm32-wasi` is REMOVED since rustc 1.84 — do not use)
- crate pin later, at M0: `zellij-tile = 0.44.3`

Evidence file written during this pad (the ONE distilled log):
`/home/hruzam/unikuklatrix/nablarva/.dev/session/toolbox-termbrana-01-brief/evidence.host-versions.md`
(moves to `termbrana/research/evidence/host-versions.md` when the repo is created — @Delta, session 02)

Precondition: office machine, normal user shell, internet up, sudo available.

---

### STEP 0 — state check (non-destructive)

```bash
zellij --version ; pacman -Q rust rustup 2>/dev/null ; command -v rustc && rustc --version ; command -v cargo && cargo --version
```

Expected: some lines may say "command not found" / "was not found" — that is a valid answer, not an error.

- zellij already present → note version; if `0.44.3` we only lock, no install
- `rust` (pacman) present → flag it: it CONFLICTS with rustup on Arch; STEP 2 branches on this
- nothing present → clean install path, proceed

>MAJKEE report 0
```zsh

```

---

### STEP 1 — install zellij (pacman, extra repo)

```bash
sudo pacman -S --needed zellij && zellij --version
```

Expected last line: `zellij 0.44.3`

- `zellij 0.44.3` → SUPPORTED, proceed
- any other version → STOP, report it — pin decision goes back to the architect (do not build against an unverified host)

>MAJKEE report 1
```zsh
0.44.3 # have to install no previous installation
```

---

### STEP 2 — Rust toolchain via rustup, pinned 1.95.0

**Branch A — STEP 0 showed pacman `rust` installed:** we must swap it (they conflict):

```bash
sudo pacman -Rns rust && sudo pacman -S --needed rustup && rustup toolchain install 1.95.0 && rustup default 1.95.0 && rustc --version
```

**Branch B — no pacman `rust`:**

```bash
sudo pacman -S --needed rustup && rustup toolchain install 1.95.0 && rustup default 1.95.0 && rustc --version
```

Expected last line: `rustc 1.95.0 (…)`

- `rustc 1.95.0` → SUPPORTED, proceed
- pacman refuses removal because something depends on `rust` → STOP, paste the dependency list — architect resolves before retry

>MAJKEE report 2
```zsh
sudo pacman -S --needed rustup
resolving dependencies...
looking for conflicting packages...

Packages (1) rustup-1.29.0-2

Total Download Size:    3,51 MiB
Total Installed Size:  11,36 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 rustup-1.29.0-2-x86_64                     3,5 MiB  3,17 MiB/s 00:01 [#######################################] 100%
(1/1) checking keys in keyring                                        [#######################################] 100%
(1/1) checking package integrity                                      [#######################################] 100%
(1/1) loading package files                                           [#######################################] 100%
(1/1) checking for file conflicts                                     [#######################################] 100%
(1/1) checking available disk space                                   [#######################################] 100%
:: Processing package changes...
(1/1) installing rustup                                               [#######################################] 100%
You may need to run rustup update stable
and possibly also rustup self upgrade-data
Optional dependencies for rustup
    lldb: rust-lldb script
    gdb: rust-gdb script [installed]
    gcc: build executables for most targets [installed]
    mingw-w64-gcc: {i686,x86_64}-pc-windows-gnu targets
    aarch64-linux-gnu-gcc: aarch64-unknown-linux-* targets
:: Running post-transaction hooks...
(1/2) Arming ConditionNeedsUpdate...
(2/2) Refreshing PackageKit...
❯ rustc --version
zsh: correct 'rustc' to 'trust' [nyae]? n
error: rustup could not choose a version of rustc to run, because one wasn't specified explicitly, and no default is configured.
help: run 'rustup default stable' to download the latest stable release of Rust and set it as your default toolchain.
❯ rustup toolchain install 1.95.0
info: syncing channel updates for 1.95.0-x86_64-unknown-linux-gnu
info: latest update on 2026-04-16 for version 1.95.0 (59807616e 2026-04-14)
info: downloading 6 components
        cargo installed                       10.48 MiB
       clippy installed                        4.48 MiB
    rust-docs installed                       21.18 MiB
     rust-std installed                       28.20 MiB
        rustc installed                       76.63 MiB
      rustfmt installed                        2.06 MiB                                                             
  1.95.0-x86_64-unknown-linux-gnu installed - rustc 1.95.0 (59807616e 2026-04-14)

info: default toolchain set to 1.95.0-x86_64-unknown-linux-gnu
info: self-update is disabled for this build of rustup
info: any updates to rustup will need to be fetched with your system package manager
❯ rustup default 1.95.0
info: using existing install for 1.95.0-x86_64-unknown-linux-gnu
info: default toolchain set to 1.95.0-x86_64-unknown-linux-gnu

  1.95.0-x86_64-unknown-linux-gnu unchanged - rustc 1.95.0 (59807616e 2026-04-14)

```

---

### STEP 3 — add the WASM target and prove it

```bash
rustup target add wasm32-wasip1 && rustup target list --installed | grep wasi
```

Expected: `wasm32-wasip1`

- `wasm32-wasip1` listed → SUPPORTED, proceed
- error mentioning `wasm32-wasi` (no `p1`) → you typed the old target name — rerun exactly as written

>MAJKEE report 3
```zsh
ustup target add wasm32-wasip1 && rustup target list --installed | grep wasi
info: downloading component rust-std
     rust-std installed                       21.70 MiB                                                             wasm32-wasip1

```

---

### STEP 4 — write the lock (evidence file)

```bash
{ echo "# host-versions — termbrana pin lock (office)"; echo "date: $(date +%F) · host: $MACHINE_NAME · pad: pad.1-host-bringup"; echo; zellij --version; rustc --version; cargo --version; rustup target list --installed | grep wasi; pacman -Q zellij rustup; echo; echo "crate pin (M0): zellij-tile = 0.44.3"; } | tee /home/hruzam/unikuklatrix/nablarva/.dev/session/toolbox-termbrana-01-brief/evidence.host-versions.md
```

Expected: the block prints and the file exists.

- file shows zellij 0.44.3 + rustc 1.95.0 + wasm32-wasip1 → **PAD COMPLETE — host LOCKED**, session-01 gate condition met
- any mismatch → STOP, report — do not hand-edit the evidence file

>MAJKEE report 4
```zsh
{ echo "# host-versions — termbrana pin lock (office)"; echo "date: $(date +%F) · host: $MACHINE_NAME · pad: pad.1-host-bringup"; echo; zellij --version; rustc --version; cargo --version; rustup target list --installed | grep wasi; pacman -Q zellij rustup; echo; echo "crate pin (M0): zellij-tile = 0.44.3"; } | tee /home/hruzam/unikuklatrix/nablarva/.dev/session/toolbox-termbrana-01-brief/evidence.host-versions.md
# host-versions — termbrana pin lock (office)
date: 2026-08-15 · host: office · pad: pad.1-host-bringup

zellij 0.44.3
rustc 1.95.0 (59807616e 2026-04-14)
cargo 1.95.0 (f2d3ce0bd 2026-03-21)
wasm32-wasip1
zellij 0.44.3-1
rustup 1.29.0-2

crate pin (M0): zellij-tile = 0.44.3

```

---

## Verdict map

| step | prediction | SUPPORTED when | REFUTED/BLOCKED when |
|---|---|---|---|
| 1 | Arch extra serves 0.44.3 | `zellij 0.44.3` | any other version |
| 2 | rustup pins 1.95.0 clean | `rustc 1.95.0` | conflict/dependency wall |
| 3 | wasip1 target available | listed | only old `wasm32-wasi` paths |
| 4 | lock reproducible | evidence file matches pins | mismatch |

## parked

- Arch pacman `rust` + wasm targets without rustup — Epoch open item; irrelevant once Branch A/B runs.
- Home-machine bring-up — separate pad, only when termbrana is worth running at home.
