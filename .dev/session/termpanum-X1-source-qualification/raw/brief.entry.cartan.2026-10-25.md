# Termpanum X0 — source qualification

2026-10-25 · Cartan · preparation bed requested by Majkee.

Bed: `/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X0-source-qualification/`.
Majkee requested `termpanum-X0-<name>` for the next Termpanum session. This uses that
numbering explicitly; the earlier `termpanum-X0-source-contract` is a distinct, completed
documentary assignment and remains closed. The historical proposed `termpanum-X1-source-fixture`
path is not the selected preparation destination. No existing bed is renamed or moved.

## Purpose and proposed gate

Prepare the approved plan's Q package: qualify one prospective output-only tmux source
using an isolated synthetic fixture and independently prepared expectations. Establish
what its capture can reliably support before building on it.

Proposed gate for RUNBOOK authoring, not yet adopted:

> Majkee records GO or STOP on an independently witnessed qualification packet for one
> isolated synthetic tmux output source, comparing capture with frozen post-termios byte
> expectations and separate rendered-state expectations, with the approved failure,
> freshness, identity and timing cases accounted for.

The accepted plan and source contract own the detailed criteria. The RUNBOOK author must
specify the exact execution scope, independent oracle author, owned paths, helper language
and dependencies, and applicable D4 verdict or explicit scoped exception before execution.
Creating this preparation bed does not supply those decisions or qualify any runtime.

## Entry reads

Read current AGENTS → flag → pulse → PROJECT.yaml, then:

1. [Approved Termpanum plan](../../nablarva-X2-builder-narative/raw/termpanum.build-plan.md)
   and [its GO](../../nablarva-X2-builder-narative/raw/decision.majkee.plan-go.2026-10-22.md).
2. [Accepted source contract](../../termpanum-X0-source-contract/raw/source-contract.md)
   and [research disposition / exact Q proposal](../../termpanum-X0-source-contract/raw/research-disposition.md).
3. [X2 handoff](../../nablarva-X4-vist/raw/handoff.x2-termpanum.cartan.2026-10-23.md)
   and [X0 handoff](../../nablarva-X4-vist/raw/handoff.x0-source-contract.cartan.2026-10-23.md).
4. [Next-cSharp technical and method hints](../../nablarva-X4-vist/raw/handoff.csharp-method.cartan.2026-10-24.md).
5. [Current architecture](../../../../docs/ARCHITECTURE.md), especially §4.1, and
   [X5 RUNBOOK](../../nablarva-X5-spine-slice/RUNBOOK.md), especially its Package Q boundary.

At creation the repository is `core@cb08d6f45ee86f0daa5fd41727efee827da483cd`.
Architecture and X5 preparation have advanced since the dated X4 handoffs. Read their
current records rather than carrying forward old documentary-lag claims as present facts.

## Coordination

X5's RUNBOOK explicitly leaves Package Q to the Termpanum line; if Q's collector lands
first, it may supply X5's producer, with coordination through Majkee and exact paths.
This bed does not take X5's shared record, address registry or substrate ownership.
The X4 HELLO/VIST material remains linked context; its input/Enter experiment is broader
than this output-only qualification. Any integration or material plan change needs a
concrete reviewed assignment.

Name check: no existing bed or documentary reference used this exact slug at creation.
Only this preparation brief is created. No RUNBOOK, STATUS, pulse row, runtime fixture,
collector, commit or deployment is opened by the naming request.
