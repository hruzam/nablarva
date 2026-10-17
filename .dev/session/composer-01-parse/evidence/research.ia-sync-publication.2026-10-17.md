# Publication research — verbatim native reply

Capture author: Cartan. Reply author: native `researcher`, observed target
`/root/publication_research`, fresh context (`fork_turns: none`), 2026-10-17,
office. Installed role configuration: `gpt-5.6-terra` / high; no separate model
telemetry was returned. Assignment: `_bus/04.cartan.point.md`, explicitly requested
by Majkee. The researcher wrote no files; Cartan captured its reply below unchanged.
This capture is evidence, not a code-home gavel or functional acceptance.

<!-- BEGIN VERBATIM REPLY -->
**Question:** Does `~/ia-sync/` change the recommended code home for the candidate Cluster A composer, and how does publication/sync work?

**Conclusion — INFERENCE (high confidence):** No. `ia-sync` is the compose-first source for machine-layer configuration and portable Codex behavior, not a generic application-code repository. Nablarva’s more specific L8 keeps the composer in `applications-in-common`; L6 permits reviewed promotion out of Nablarva but does not create an automatic or app-code deployment path through `ia-sync`.

**Findings**

- **SOURCE:** The authoritative local instruction identifies `ia-sync` work as pull/edit/dry-run/deploy and portable Claude/Codex maintenance, with `SYNC_DISCIPLINE.md` to be followed “always.” [AGENTS.md:43-50](/home/hruzam/ia-sync/AGENTS.md:43) It declares `codex/` the portable Codex source, `~/.codex` a deployment target, and `_staging/codex/` deploy-inert; a new primitive needs dry-run deployment and fresh-session verification. [AGENTS.md:52-64](/home/hruzam/ia-sync/AGENTS.md:52)

- **SOURCE:** Publication of an **ia-sync-managed portable artifact** is compose-first: edit `~/ia-sync`, `git pull --rebase`, dry-run deploy, deploy on that host, commit, then push; receiving hosts pull then deploy. [SYNC_DISCIPLINE.md:7-17](/home/hruzam/ia-sync/SYNC_DISCIPLINE.md:7) [SYNC_DISCIPLINE.md:36-64](/home/hruzam/ia-sync/SYNC_DISCIPLINE.md:36) The live trees are deployed copies, and reverse bulk harvest is expressly retired. [SYNC_DISCIPLINE.md:19-22](/home/hruzam/ia-sync/SYNC_DISCIPLINE.md:19) [SYNC_DISCIPLINE.md:70-85](/home/hruzam/ia-sync/SYNC_DISCIPLINE.md:70)

- **SOURCE:** The portable Codex deployment surface is deliberately narrow: `codex/AGENTS.md → ~/.codex/AGENTS.md`, `codex/agents/ → ~/.codex/agents/`, and `codex/skills/ → ~/.agents/skills/`. [codex/README.md:15-21](/home/hruzam/ia-sync/codex/README.md:15) The executable mapping matches: `deploy.sh` copies only the allowed AGENTS/profile/agents/skills paths, while auth, configuration, hooks, histories, sessions, databases, caches, logs, and trust hashes remain local. [deploy.sh:226-258](/home/hruzam/ia-sync/deploy.sh:226) [codex/README.md:73-79](/home/hruzam/ia-sync/codex/README.md:73) There is no mapping from `applications-in-common/.../composer/` to a live application destination.

- **SOURCE:** A candidate Codex primitive can be reviewed-promoted from `_staging/codex/` into `ia-sync/codex/`, but only with evidence, review, and a clear live deployment target. Experimental cross-agent mechanisms instead belong in the relevant Nablarva task bed. [_staging/codex/README.md:14-22](/home/hruzam/ia-sync/_staging/codex/README.md:14)

- **SOURCE:** Nablarva L6 says experimental shapes build there, structural builds stay on `~/ia-sync/`, and promotion out requires reviewed merge, never auto-deploy. [flag.md:27-29](/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md:27) L8 is the specific boundary for this candidate: Cluster A’s clipper/processor/**composer** stays in `applications-in-common`. [flag.md:32-34](/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md:32)

- **INFERENCE (high confidence):** Apply L6 as the promotion gate and L8 as the ownership/home constraint: Phase 0 composer code belongs in the selected `applications-in-common` location, not this Nablarva bed and not `ia-sync`. A future portable Codex mechanism may have a separate reviewed promotion into `ia-sync/codex/`, but that would be a distinct artifact with a stated live target, not the composer application itself.

**Contradiction surfaced**

- **OBSERVED:** `SYNC_GUIDE.md` still describes `sync.sh` live-tree backup/harvest and new-host bootstrap. [SYNC_GUIDE.md:23-43](/home/hruzam/ia-sync/SYNC_GUIDE.md:23) [SYNC_GUIDE.md:84-92](/home/hruzam/ia-sync/SYNC_GUIDE.md:84)
- **SOURCE:** `SYNC_DISCIPLINE.md` explicitly retires that workflow and says never run `sync.sh`. [SYNC_DISCIPLINE.md:70-85](/home/hruzam/ia-sync/SYNC_DISCIPLINE.md:70) Root instructions select `SYNC_DISCIPLINE.md` as the always-followed rule. [AGENTS.md:43-50](/home/hruzam/ia-sync/AGENTS.md:43)
- **OBSERVED:** read-only `git log -1` showed `SYNC_DISCIPLINE.md` last changed at `1fc2044` on 2026-10-13, while `SYNC_GUIDE.md` last changed at `8da748a` on 2026-07-31. Treat `SYNC_GUIDE.md` as stale historical material.

**Raw evidence / commands**

- `nl -ba` over `AGENTS.md`, `SYNC_DISCIPLINE.md`, `SYNC_GUIDE.md`, `deploy.sh`, `codex/README.md`, `_staging/codex/README.md`, Nablarva `flag.md`, and the session RUNBOOK/STATUS: source contents and anchors above.
- `git -C /home/hruzam/ia-sync log -1 ...`: revision/date evidence above.
- `git -C /home/hruzam/ia-sync status --porcelain=v1`: empty output; no ia-sync working-tree changes observed.
- No writes, network, deployment, sync, or external actions occurred.

**Unresolved gap:** I did not read the candidate’s external `applications-in-common` instruction chain, so I cannot establish that repository’s own commit/push/release procedure or confirm its exact source-tree convention.

**Smallest next probe/decision:** Read the applicable `AGENTS.md` chain at `/home/hruzam/www/elements-factory/applications-in-common/experiments/composer/`, then let Majkee choose the code home/stack. The evidence supports the candidate directory in principle under L8; it does not authorize implementation or establish that repository’s publication procedure.
<!-- END VERBATIM REPLY -->
