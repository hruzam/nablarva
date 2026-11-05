# Office pilot activation

Independent pre-activation PASS: verification.md (9 owner +26 app tests).
Pilot now runs mode live on authenticated loopback18790, using the explicitly
configured reviewed /home/hruzam/ia-sync/zsh/session/ovitmugen.py source.
PID1753325; unified-exec session91142. Installed ~/.config/zsh source stays unchanged.
USB mappings18789 and18790 remain. Draft origin and persistent vault are unchanged.
No global deploy, home change, ACL change, commit or push.

Actual Chromium360px attach to existing phone-console-01-browser @175/%174 Codex
receives7137 terminal-output bytes. Desktop selected window and panePID survive.
Shared size changes109x51 ->43x17 while attached ->109x51 after detach. No deliberate
keystroke or prompt was sent. The frontend automatically answered4 native terminal
queries: primary/secondary device attributes and foreground/background colors.
The first runner incorrectly treated these replies as deliberate input and failed
its zero-input assertion; preservation checks independently stayed unchanged.
Corrected evidence distinguishes native terminal replies from deliberate keystrokes.
See office-attach.2026-10-30.json and office-attach.cjs. Physical Firefox check pending.

Rollback: stop only the exact pilot process, copy
/tmp/pc-console-u_cg0nzb/config.fixture-before-live.json to config.json in that same
directory, then start from apps/session-console with .venv/bin/python -m host.server
--config /tmp/pc-console-u_cg0nzb/config.json. Keep the uploaded-photo vault. Rollback
changes the pilot config, not the reviewed owner source or agent-process lifetime.
