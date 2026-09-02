# host-versions — termbrana pin lock (office)
date: 2026-08-15 · host: office · pad: pad.1-host-bringup

zellij 0.44.3
rustc 1.95.0 (59807616e 2026-04-14)
cargo 1.95.0 (f2d3ce0bd 2026-03-21)
wasm32-wasip1
zellij 0.44.3-1
rustup 1.29.0-2

crate pin (M0): zellij-tile = 0.44.3

## re-verification 2026-09-02 — office · session 02 (M0 close) · driver: Oraculum · hands: @Delta

zellij 0.44.3        /usr/bin/zellij · pacman zellij 0.44.3-1 · packager alerque@archlinux.org · build 2026-05-14
rustc 1.95.0 (59807616e 2026-04-14)   via rustup toolchain 1.95.0-x86_64-unknown-linux-gnu (default)
cargo 1.95.0 (f2d3ce0bd 2026-03-21)
targets installed: wasm32-wasip1 · x86_64-unknown-linux-gnu

distro: ID=manjaro (Manjaro Linux) · ID_LIKE=arch · pacman-mirrors branch: stable

provenance: the zellij binary is Arch's `extra` build delivered through Manjaro's stable branch
(staged — lags Arch by design). rustc/cargo come from the rustup channel, not the distro.
Correction to research.epoch.host-versions.2026-08-15.md ("Arch extra in sync with upstream"):
right package origin, wrong delivery timing. The pin is empirical (verified 2026-08-15/16 and
2026-09-02 on this host), not a repo-tracking promise.

repo path: toolbox/termbrana/ inside nablarva (flag L12, 2026-09-02) — was ~/unikuklatrix/nablarva/toolbox/termbrana at 2026-08-15.
