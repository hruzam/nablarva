# Disposable touch-scroll repair

Astrobley, 2026-10-30. Parent owns mobile_display.py, gateway restarts and phone.
This cut owns only touch_scroll.js and terminal-scroll.* evidence. No fixture input,
phone action, gateway restart or shared-source change was performed by this seat.

## Finding and narrow change

The pinned bundle uses xterm 5.4.0 (ttyd source yarn.lock resolution). Its touch
handler returns when application mouse reporting is active. Otherwise touch scrolls
the browser viewport, not tmux's retained history. Wheel has a separate route to
terminal mouse reports; the installed index.original.html contains these same
branches and no isTrusted check. Thus mouse on is useful but does not itself convert
swipes to wheels. Pane alternate_on describes the application inside tmux, not
tmux's outer screen in the browser. [xterm mouse/touch implementation](https://github.com/xtermjs/xterm.js/blob/5.4.0/src/browser/Terminal.ts#L551).

The tiny injected script translates deliberate single-finger vertical gestures
over .xterm-screen into bubbling cancelable WheelEvents. It requires the pinned
enable-mouse-events DOM class, avoiding alternate-screen arrow-key fallback when
mouse reporting is absent. Each approximate row crossed emits a separate line wheel
because xterm's mouse report uses direction rather than the magnitude as its count.
Initial touch coordinates retain the original pane location. Gesture work is capped
at eight wheels per move. No global terminal object, private JavaScript methods,
direct WebSocket, focus operation or shell input path is used.

Taps/jitter below 8 CSS pixels, horizontal gestures, input controls and multi-touch
are left alone. Only a cancelable vertical gesture beyond the threshold receives
preventDefault. A second touch or mouse-reporting loss resets the gesture. These
claims concern adapter routing; browser IME/tap/pinch behavior still needs physical
verification. DOM selectors/classes are pinned qualification glue, not an upstream
extension-API promise. Parent embeds the exact source through supported ttyd -I.

For conventional scrolling: drag DOWN to reveal earlier numbered lines; drag UP
to move toward later output. In a TUI the same mouse wheel can mean application
navigation; this does not create a universal historical transcript.

## Width finding

/tmp/phone-console-current.png shows a terminal region ending near physical x668
on a 720px image. Given the reported 41 columns, this does not prove truncation:
ttyd pads the terminal 5 CSS px per side, and xterm FitAddon reserves a scrollbar
width (15 CSS px fallback) before flooring the available width into whole cells.
The screenshot's long prompt wraps onto subsequent lines. This right margin is
consistent with that fitting calculation, not conclusive evidence of a crop.
Sources: local ttyd html/src/style/index.scss,
[FitAddon](https://github.com/xtermjs/xterm.js/blob/5.4.0/addons/addon-fit/src/FitAddon.ts),
[viewport width](https://github.com/xtermjs/xterm.js/blob/5.4.0/src/browser/Viewport.ts#L59).

The later /tmp/phone-console-scroll.png shows the complete right-hand END markers
on numbered fixture lines. Read-only tmux inspection observed one phone client
47x25, selected window 47x24, mouse on, smallest sizing, and 178 retained lines in
scroll-check. The parent changed font12, status-right and fixture state. This seat
did not manipulate those settings. Query client preferences can override server
font preferences; if font changes appear ignored, inspect the actual URL too.

## Reused controls and their boundary

Read /home/hruzam/ia-sync/zsh/remote-cli/{README.md,remote-cli.sh}. remote-scroll
enables mouse and a history floor; it does not supply browser touch conversion.
Its keyboard fallback is tmux prefix, [, PgUp/PgDn, q. It uses /usr/bin/tmux and
the caller's server context; do not invoke it from an unrelated shell with only
a session name against this explicit private socket. Existing code stayed untouched.

## Verification and handoff

`node --check raw/trial/touch_scroll.js` passed, with paths relative to this bed.
`node raw/terminal-scroll.test.js` passed meaningful DOM routing mocks covering
threshold/taps, both signs, row quantization and coordinates, horizontal cancellation,
pinch reset, reporting loss, touchcancel, dispatch cap and input exclusion.
These tests exercise adapter behavior, not the actual Firefox/xterm event pipeline.

Adapter SHA256:
`033e2371925acee5b1095902cfd7b6cf5364d1ef2f39d3ae0b1e28a2c7a13c7b`.
Test SHA256:
`3f902b20ab97b18fe3dab1cc356f430f18e3670318429eff0d0cc810ba11d022`.

Remaining gate: parent injects the exact file, keeps mouse enabled only on the
fixture, and obtains physical numbered-line scroll, tap/IME and pinch observations.
Rollback is removal of this injected script from the disposable -I page by its
owner. No durable installation or production transport contract follows.

## Physical failure and target correction

Parent reports that the first adapter was injected, served with page SHA256
9cb08df59cc464c3495862192c5dccfb68122f45afed52693973efafec03b0c6,
and the physical user confirmed width fits but scrolling still failed after reload.
That is FAIL evidence for the original adapter, despite passing routing mocks.

The original touch target guard required closest('.xterm-screen'). Pinned xterm
creates .xterm-viewport and .xterm-screen as siblings under .xterm; viewport touches
therefore miss that guard. The corrected script starts from closest('.xterm'),
queries its screen sibling, and checks initial coordinates against screen bounds
to avoid taking over the scrollbar gutter. Exact enable-mouse-events class spelling
was checked in both pinned source and the installed bundle. This is the concrete
target correction; the actual phone event target was not observed by this seat.

Regression mocks now model a viewport target which has no screen ancestor and
verify gutter exclusion, along with the earlier event cases. All pass. The earlier
mock embedded the screen-descendant assumption and therefore missed this case.

Corrected adapter SHA256:
`d5d05b3437500574048d97a6ddd912d235b2fd6e7a2f57cbb224c5b15a68e8f5`.
Corrected test SHA256:
`5b27107e9378c950272db1b2caf8e804ff29403b610cd47cec8c5369be1f514e`.
Parent owns reinjection and the next physical verdict. No PASS is inferred.

Read-only root key-table inspection also confirmed WheelUpPane has its normal tmux
binding: for the plain shell it enters copy-mode; panes already in a mode, alternate
screen or handling mouse events receive the event instead. The adapter therefore
cannot promise historical navigation uniformly across TUIs without an explicit
history control and application-level qualification.
