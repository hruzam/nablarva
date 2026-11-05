# Applied owner transition

Majkee grants the bounded source pen in authorization.2026-10-30.md. Source baseline
97dba115a36abf216ab6f5deabda601ce82e395cdd285a1b52aca7568f5a3125;
applied reviewed patch5af6027b58cf222733b28622af8992d0b3f1dafe7569b9ebc9060d0934b35fa6;
result cb3bf0d9b44133159f2c194c646dbb968d32d340d64cb8a2c9c1d46dfb957f40.
Only ia-sync/zsh/session/ovitmugen.py changed in the owner source. The installed
~/.config/zsh/session/ovitmugen.py remains baseline. No shared deploy/commit/push.

Applied-source harness initially passed8/9: the transient-child test's shell loop
created idle gaps between sleep processes, so the final guard safely refused when
a new child appeared. This is retained in owner-tests.2026-10-30.txt. The applied
harness now holds one persistent Python child until the owner loop releases it,
matching the intended stable-busy-to-idle transition. No production guard was relaxed.
All9 checks pass in7.602s; independent reviewer repeats9/9 in8.300s. Historical
review harness remains unchanged. Reproduce with check_applied.py.

Presence attachment for this exact change: ecdcbd6fd7ec0986148a5603b299dc04.
Detach only this ID when the scoped owner work is complete.
