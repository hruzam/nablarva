# Poke log — relay-X0-carryover (append-only)

One block per poke: UTC before/after, target binding checked, door, exact line, exit, what was seen after.
A queued or typed line is not proof that it was read; the RETURN file is.

## p01 — engineer → cartan (cycle 01)
- target checked 2026-11-21T19:02:13Z: pane %59, foreground `codex` (pid 2874067), footer thread `01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318`, name `controller(codex)|houston|oraculum|astrobley`, idle composer
- door: `codex queue --thread 01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318 --message …` (no `--resume`), one call
- line: `[poke p01] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/_bus/01.engineer.point.md; follow its reply/bell instructions`
- call: before 19:02:13.236Z · after 19:02:13.586Z · exit 0 · `Queued message 01a1ff7c-d538-7fa0-84be-e39f6320c32e`
- seen after (read-only pane look): 19:02:21Z `Working (7s …)`; context 97% → 96% → 88% by 19:02:54Z. No key was typed into the pane.
- claim level: queue accepted and a native turn started. Read and worked = only when `_bus/01.cartan.return.md` exists and checks out.

## p02 — engineer → myshell (cycle 02)
- target checked 2026-11-21T19:02:21Z: pane %61, foreground `claude` (pid 2874087), session file status `idle`, input row empty with a dim suggestion only (ANSI dim, cursor x=2), no dialog. Bottom rows only; nothing else of the pane was read.
- door: tmux, three separate calls — `set-buffer` + `paste-buffer -p` (19:02:35.251Z) · look: exact text visible on the input row, foreground still `claude` (19:02:40.433Z) · `send-keys Enter` (19:02:47.263Z). Channel authorised by Majkee D3.2; this is the chosen door for a Claude seat, not a fallback after a failure.
- line: `[poke p02] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/_bus/02.engineer.point.md; no bell owed`
- seen after: 19:02:53Z input row empty, footer `esc to interrupt`, session file status `busy`.
- claim level: submitted and a turn started. Read and answered = only when `_bus/02.myshell.return.md` exists.

## p03, p04, p05 — engineer → cartan, oraculum, auditor (cycles 03, 04, 05)
- targets checked 2026-11-21T21:07:13Z, bottom rows only, foreground `codex` in all three, footers carry the thread ids below:
  - %59 `controller`, thread `01a1ff5e-6fa1-75e1-88f9-33b8c7fe6318`, pid 2874067. Its composer held an **unsent draft typed by Majkee**; `codex queue` does not go through the composer, and the draft was still there afterwards.
  - %60 `oraculum`, thread `01a1ff2e-7d3a-7320-a65c-cc34fdea4ee1`, pid 2874075, idle composer.
  - %66 `auditor`, thread `01a1ffdf-793f-76d2-8497-3f68f84a34a7`, pid 3276835, idle composer.
- door: `codex queue --thread <id> --message …` (no `--resume`), one call per seat
- line: `[poke pNN] read /home/hruzam/unikuklatrix/nablarva/.dev/session/relay-X0-carryover/_bus/NN.engineer.point.md; the reply bell is in the file` (NN = 03, 04, 05)
- calls:
  - p03: before 21:07:23.416Z · after 21:07:23.741Z · exit 0 · `Queued message 01a1ffef-6dbf-79c1-923d-13afa6b0a821`
  - p04: before 21:07:23.744Z · after 21:07:24.056Z · exit 0 · `Queued message 01a1ffef-6f0e-7ed1-9bd2-47691a5ea404`
  - p05: before 21:07:24.058Z · after 21:07:24.362Z · exit 0 · `Queued message 01a1ffef-7036-7182-b21d-ab0c86c283af`
- seen after (read-only pane look, 21:07:35Z): all three show `Working (… esc to interrupt)`; %60 shows `Read 04.engineer.point.md`. No key was typed into any pane.
- claim level: three queue calls accepted and three native turns started. Read and worked = only when each RETURN exists and checks out.
- commit carrying the POINTs: nablarva `a7321d6` (local, ahead 1 at poke time; the push is part of cycle 03).
