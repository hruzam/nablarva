# @Epoch research report
Date: 2026-08-15
Triggered by: Date-calibrated version research for Zellij WASM plugin project, Arch Linux target
Scope: default radar, no project contract read (task gave explicit target path; no PROJECT.yaml consulted this run — flag if project has one, see Sections to refresh)

## Findings

### 1. Zellij stable release + Arch packaging

WHAT changed: Briefing's v0.44.3 is CONFIRMED as current upstream stable. No newer release exists.
SINCE when: 0.44.3 released 2026-05-13.
SOURCE: https://github.com/zellij-org/zellij/releases (via changelog fetch), cross-checked https://docs.rs/crate/zellij-tile/latest
CONFIDENCE: H (release confirmed via two independent live fetches — GitHub-adjacent changelog + docs.rs)
IMPACT: No supersession needed.
ACTION: none.

WHAT changed: Arch `extra` repo pacman package is NOT lagging — it is exactly current: `zellij 0.44.3-1`, built 2026-05-14 08:19 UTC, last updated 2026-05-14 08:32 UTC (i.e. synced within ~1 day of upstream release).
SINCE when: 2026-05-14.
SOURCE (link): https://archlinux.org/packages/extra/x86_64/zellij/
CONFIDENCE: H (live-fetched package page directly)
IMPACT: No AUR fallback needed — official `extra` repo is authoritative and current for this project.
ACTION: install via `pacman -S zellij`, not AUR.

### 2. zellij-tile crate matching

WHAT changed: `zellij-tile` on crates.io is at 0.44.3, version-locked in lockstep with the zellij host release (same numbering scheme, released same day).
SINCE when: 2026-05-13.
SOURCE (link): https://docs.rs/crate/zellij-tile/latest, https://crates.io/crates/zellij-tile
CONFIDENCE: H (crates.io/docs.rs is canonical registry, live-fetched)
IMPACT: Plugin crate version must match host major.minor.patch closely — Zellij plugins run through a WASI-hosted ABI; the project has historically shipped `zellij-tile` version-pinned identically to the target host release (this is convention, not verified as a hard runtime gate this run — flag as inferred).
CONFIDENCE on the "must match tightly" claim specifically: M (inferred from versioning convention + WASI ABI coupling, not a quoted compatibility-matrix source)
ACTION: pin `zellij-tile = "0.44.3"` exactly, matching pacman-installed host 0.44.3-1.

WHAT changed: The most significant recent plugin-relevant host change is in 0.44.0 (2026-03-23): "infra: migrate wasm runtime from wasmtime to wasmi" plus "expanded plugin APIs for pane control and scrollback access" — this is the release that plausibly introduced pane-content-read style APIs (e.g. `PaneRenderReportWithAnsi`) referenced in the brief.
SINCE when: 2026-03-23 (0.44.0), refined through 0.44.1/0.44.2/0.44.3 (bug fixes only, no further API breaks noted in changelog headers).
SOURCE (link): https://raw.githubusercontent.com/zellij-org/zellij/main/CHANGELOG.md
CONFIDENCE: M (changelog headline text summarized, did not diff exact plugin-API surface line by line — treat as directional, verify against `zellij::prelude` symbol list if the plugin touches pane-content reads)
IMPACT: If the target project's plugin reads pane content or intercepts input, it needs >=0.44.0 and the corresponding permission grants (`read pane content` permission is required for `PaneRenderReport`/`PaneRenderReportWithAnsi` subscriptions per official docs).
ACTION: confirm exact event/permission names against https://zellij.dev/documentation/plugin-api-events and https://zellij.dev/documentation/plugin-api-permissions.html before wiring the plugin manifest — I did not fully diff the symbol-level API surface this run.

### 3. WASM target + rustc toolchain

WHAT changed: `wasm32-wasi` is DEPRECATED and REMOVED (not just deprecated) as of Rust 1.84 (2025-01-05); the correct current target is `wasm32-wasip1` (Tier 2, stable since Rust 1.78, 2024-05-02). `wasm32-wasip2` also exists (Tier 2 since Rust ~1.82/late 2024) but Zellij itself does not target it.
SINCE when: wasip1 rename effective 1.78 (2024-05-02); wasi removal effective 1.84 (2025-01-05).
SOURCE (link): https://doc.rust-lang.org/rustc/platform-support/wasm32-wasip1.html, https://blog.rust-lang.org/2024/04/09/updates-to-rusts-wasi-targets/
CONFIDENCE: H (official rustc book + official Rust blog)
IMPACT: Any doc or example still referencing `wasm32-wasi` as a build target (e.g. the official `zellij-org/rust-plugin-example` README, which still says "you will need to have `wasm32-wasi` added to rust as a target") is STALE relative to current rustc — that target no longer exists to add via rustup on a current toolchain.
ACTION: use `wasm32-wasip1`, not `wasm32-wasi`, regardless of what the example README says.

WHAT changed: Confirmed directly from zellij's own upstream `rust-toolchain.toml`: pinned channel `1.95.0`, targets `wasm32-wasip1` and `x86_64-unknown-linux-musl`, components `rustfmt`, `clippy`.
SINCE when: current `main` branch state as of this fetch (2026-08-15).
SOURCE (link): https://raw.githubusercontent.com/zellij-org/zellij/main/rust-toolchain.toml
CONFIDENCE: H (live-fetched from the zellij repo itself — this is the authoritative signal for what rustc version the host project builds/tests against)
IMPACT: This is the single strongest source in this report — it's Zellij's own CI-pinned toolchain, directly answering "what rustc + what wasm target should plugin devs use."
ACTION: treat `1.95.0` + `wasm32-wasip1` as the host-compatible floor. Global current stable rustc is newer (see next finding) — using stable-latest should still work since wasip1 is a stable Tier-2 target, but if plugin build issues arise, drop to rustup toolchain 1.95.0 to match upstream exactly.

WHAT changed: Global current stable rustc (independent of Zellij's pin) is 1.97.1.
SINCE when: Arch package build 2026-07-16, last updated 2026-07-17 17:50 UTC; releases.rs also shows 1.97.1 as current stable with beta 1.98.0 scheduled 2026-08-20.
SOURCE (link): https://archlinux.org/packages/extra/x86_64/rust/, https://releases.rs/
CONFIDENCE: H (two independent live sources agree)
IMPACT: Arch pacman `rust` package (1.97.1) is newer than Zellij's own CI pin (1.95.0) — not a conflict, since wasm32-wasip1 is stable across both, but worth knowing the pacman-provided rustc is ahead of what Zellij's CI tests against.
ACTION: none blocking; note as informational for troubleshooting.

### 4. Toolchain install method: rustup vs pacman rust

WHAT changed: Zellij's own official plugin-dev docs (`plugin-dev-env.html`, `developing-a-rust-plugin` tutorial) do NOT explicitly prescribe rustup vs distro-package — no install-method recommendation found on the official pages fetched.
SINCE when: current as of this fetch, 2026-08-15.
SOURCE (link): https://zellij.dev/documentation/plugin-dev-env.html, https://zellij.dev/tutorials/developing-a-rust-plugin/
CONFIDENCE: M (absence-of-evidence on two official pages, not exhaustive — did not check every doc page)
IMPACT: No explicit vendor guidance either way.
ACTION: Recommend rustup on pragmatic grounds (not doctrine): rustup allows `rustup target add wasm32-wasip1` cleanly and lets you pin to 1.95.0 to match Zellij's own CI if pacman's 1.97.1 ever causes friction. Pacman `rust` package does NOT ship wasip1 target add tooling the way rustup does — Arch's `rust` package can add targets via `rustup`-free means only if `pacman -S rust-wasm` equivalent exists; this needs a follow-up check (flagged below, not verified this run — L confidence claim, do not treat as final).

### 5. API-flux / imminent-release signal

WHAT changed: CHANGELOG shows an `[Unreleased]` section actively receiving commits on `main`, meaning development continues past 0.44.3, but no dated upcoming-release announcement or migration guide was found this run.
SINCE when: ongoing as of 2026-08-15.
SOURCE (link): https://raw.githubusercontent.com/zellij-org/zellij/main/CHANGELOG.md
CONFIDENCE: M (changelog structure inspected, did not read full unreleased diff or GitHub milestones/issues for a pending 0.45 announcement)
IMPACT: No strong signal to pin to an older release instead of 0.44.3. The 0.44.0 wasmtime→wasmi runtime migration was the big recent shakeup and 0.44.3 is 3 patch releases past it (stabilized).
ACTION: 0.44.3 is reasonable to pin now. If the plugin depends on very new pane-content-read APIs, double check they were not further changed in `[Unreleased]` before committing to exact event names — I did not diff `[Unreleased]` contents this run.

## Pin recommendation block (PAD-01, Arch)

```
# Zellij host (matches pacman `extra` repo exactly — no AUR needed)
zellij = 0.44.3   (source: pacman/extra, live-current as of 2026-08-15)

# Plugin crate — pin identical to host
zellij-tile = "0.44.3"

# Rust toolchain
# - Zellij's own CI pin: 1.95.0 (rust-toolchain.toml, main branch)
# - Arch pacman `rust` current: 1.97.1 (both work; wasip1 stable across both)
rustc = 1.95.0 via rustup   (fallback: pacman rust 1.97.1 if not chasing exact CI parity)

# WASM target — wasm32-wasip1 ONLY. wasm32-wasi is REMOVED since rustc 1.84.
target = wasm32-wasip1

# Install commands (Arch):
sudo pacman -S zellij                       # host, 0.44.3-1, extra repo
sudo pacman -S rustup                       # rustup itself is pacman-packaged on Arch
rustup toolchain install 1.95.0
rustup default 1.95.0
rustup target add wasm32-wasip1 --toolchain 1.95.0

# In plugin Cargo.toml:
[dependencies]
zellij-tile = "0.44.3"

# Build:
cargo build --release --target wasm32-wasip1
```

Open item NOT resolved live this run (flag, do not assume): whether `PaneRenderReportWithAnsi` and any input-interception permission names changed shape between 0.44.0 and 0.44.3 — the changelog headline confirms the 0.44.0 API expansion happened, but I did not diff exact symbol/permission names against the plugin-api-events and plugin-api-permissions pages. Recommend a follow-up @Epoch or direct doc read against https://zellij.dev/documentation/plugin-api-events and https://zellij.dev/documentation/plugin-api-permissions.html before finalizing the plugin manifest's `plugin_dependencies`/permission block.

Cross-check: not invoked. Findings were single-to-double-source corroborated on every load-bearing claim (Arch package version, rustc pin, wasm target deprecation) without conflicting sources requiring `field`/`vega`/`mirror` escalation. If PAD-01 is a high-stakes gate before committing install scripts, a `vega` (position-free) pass on the "wasm32-wasip1 is correct, not wasip2" claim would be cheap insurance but was not run this pass.

## Sections to refresh: [Zellij plugin-api-events/permissions exact symbol diff between 0.44.0 and 0.44.3; whether pacman `rust` package on Arch ships wasm target-add tooling without rustup; PROJECT.yaml/contract for this project was not read this run — if one exists at nablarva root or under toolbox-termbrana-01-brief, re-run with @eagle orientation first to extend scope correctly]
