# Oraculum technical consultation — verbatim child reply

Observed handle: `/root/terminal_oraculum_consult`; native role `oraculum`; read-only child; controller saved reply.

---

Route: spawned child (canary: oc-2e2a2d87).

Loaded `/home/hruzam/.germline/agents/oraculum/identity.md` (`stamp: 88e41067`) and `/home/hruzam/.germline/agents/oraculum/binding.codex.md` (`stamp: 50a6996f`). No project addendum found: neutral Oraculum. Effective cwd: `/home/hruzam/unikuklatrix/nablarva`; observed host: `hruzam`; branch: `core`; HEAD: `3318b17d214c1dce3dea78a20c3c7364f906b0f8`. Scope: analysis-only child for Cartan. No writes, runtime experiments, native CLI/container launches, delegation, or live-session inspection performed. Existing dirty Sublime work was left alone.

**My technical recommendation is a persistent, attachable task process, with files available for durable requests. Keep the container optional until an isolation requirement earns it.** Files, process persistence, terminal interaction, and containment answer different questions.

`said: majkee`, as supplied by the caller: create a new session line and architecture preparation; consider feeding prompts as files to a container; permit a selectable regime similar to permission modes.

`said: caller’s preceding-intent summary`: each CLI should have a persistent task terminal shared with the operator, retaining cwd, environment, processes and interactive state, with human takeover.

`inferred: Oraculum`: this asks for continuity of a running execution context. A separate task terminal and exclusive input ownership are reasonable candidates, but neither is an operator lock.

**Three materially different approaches remain viable.**

| Approach | What it provides | Principal limitation |
|---|---|---|
| File inbox → bounded jobs | Inspectable requests, receipts, reproducible batch work; simple container placement | New jobs do not automatically share shell state or a foreground interactive program |
| File inbox → persistent worker/shell | Can retain shell state and dispatch work without restarting the shell | A shell busy running an interactive child cannot also consume its ordinary command queue; another control boundary is needed |
| Persistent PTY session → human and agent clients | Same running shell/program, terminal signals and interactive takeover | Requires attachment, rendering, lifecycle and input arbitration; PTY bytes alone do not identify safe command boundaries |

A container can host any of these. It does not select among them.

A prompt file also has two different possible destinations: an assistant reads it as an assignment, or an executor reads it as a command request. Those have different permission paths. Decide which meaning is under test. Plain prompt prose must not silently become shell source.

For a persistent shell, executing a script as a child and sourcing it into that shell have different consequences. The former does not normally leave its cwd and shell variables in the parent; the latter deliberately changes the shell and may also change traps, options or functions. Neither should be hidden behind the label “feed a file.”

A file can carry arbitrary terminal-input bytes, but once a watcher interprets them as keys, resize requests or interrupts, the design has become an interactive control protocol with file transport. It still needs targeting, ordering and acknowledgement semantics.

Linux PTYs provide a bidirectional terminal interface; terminal attributes determine canonical/raw input, echo and signal handling. For example, Ctrl-C can signal the foreground process group rather than terminate the shell. These are properties that ordinary redirected stdin does not supply. [Linux PTY documentation](https://man7.org/linux/man-pages/man7/pty.7.html), [terminal attributes](https://man7.org/linux/man-pages/man3/termios.3.html).

A PTY is also not a rendered screen. A human client needs terminal emulation; an agent may need raw output, a rendered snapshot, or both. A snapshot cannot prove that an input was accepted.

**Input regime should expose two independent choices: who may type, and what execution is authorized.**

Useful proposed regimes are:

- **Human control:** agent observes and prepares requests; human acts.
- **Agent control with takeover:** agent may send input within the granted scope; a human takeover revokes subsequent agent writes.
- **Approval per operation:** a named request is approved before dispatch; later interactive input remains separately governed.
- **Shared typing:** feasible as an experimental collaboration mode, but interleaved bytes can corrupt commands or answer the wrong prompt.

For the first discriminating trial, I favor agent control with explicit human takeover. This is an experimental default, not a lock.

The enforcement question is concrete: **does every writer pass through one input owner?** A controller can reject stale agent requests after takeover only if it controls their route. If an agent can still attach directly, write the PTY, access the multiplexer control socket, or invoke another execution endpoint, the regime is cooperative across those bypasses.

A useful takeover boundary is an acknowledged generation change: later requests with the previous generation are rejected. Input already delivered cannot be recalled, and takeover does not stop a running job. Interrupt, suspend, terminate and resume should remain separate operations. Do not automatically replay queued input when agent control returns.

Similarly, a terminal bridge does not automatically inherit the originating CLI’s native permission mode. An apparently harmless allowed tool call that forwards arbitrary commands to a more privileged worker may relocate the actual execution decision. Qualification must follow the entire path, including subprocesses and alternative entry points. The repository already treats unproven permission routes as cooperative: [muticula STATUS](/home/hruzam/unikuklatrix/nablarva/.dev/session/muticula-01-qualify/STATUS.md:10). Its recorded plan is not completed enforcement evidence.

**The smallest useful synthetic comparison is six rows.** Use a disposable target, no provider CLI, no external service and no container initially. The worker can implement two candidates: fresh jobs fed from files and one persistent PTY shell. Test file dispatch into the persistent shell as an additional variation where useful.

| Row | Stimulus | Independent evidence / discriminating result |
|---|---|---|
| 1. Retained context | Change cwd, export a unique variable, define a function; query through a later request | Record shell identity and actual returned values. Distinguishes retained shell state from reconstructed parameters |
| 2. Foreground interaction | Run a fixture requiring a TTY, then a raw single-key exchange | Fixture records TTY presence and received bytes. A printed prompt alone is insufficient |
| 3. Job control | Start an owned long-running child; interrupt it; then query the shell | Child receives the intended signal, shell survives, and no unrelated process is touched |
| 4. Detach and resize | Disconnect viewer during a running job, reconnect, change dimensions | Same target incarnation and job survive; fixture reports dimensions. Separate byte expectations from rendered-state expectations |
| 5. Takeover race | Schedule an agent write, transfer control, attempt old- and new-generation writes | Received-byte trace proves which inputs crossed the boundary; stale input is rejected without claiming already-written bytes were undone |
| 6. Uncertain delivery and replacement | Lose a receipt after a harmless marked effect; restart target under the same friendly name | Effect is reconciled without blind replay; old target binding cannot address the replacement |

For row 6, use a fixture-owned effect counter or marker distinct from the transport receipt. Distinguish request stored, dispatcher accepted, bytes written, application consumed, operation completed and result observed. A timeout means uncertainty, not failure permission to retry. This preserves the existing qualification discipline in [pipe RUNBOOK](/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/RUNBOOK.md:70).

Freeze the expected results before execution. Preserve raw receipts, target/process identity, namespace information and cleanup evidence. Termpanum’s current recovery problem shows why PID/namespace and cleanup cannot be inferred from a socket or leftover artifact: [termpanum STATUS](/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/STATUS.md:15).

**Project fit is promising, with several boundaries that must stay explicit.**

- **L3/L4:** regulated room delivery retains adapter-owned PTY, structural regulation and journal authority; tmux is not the protocol, and autonomous `send-keys` injection remains rejected. A task-terminal study should not quietly become a replacement room bus. [flag](/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md:14)
- **L14:** files as spine and PTY as relay base support the hybrid framing. Research and blind triangulation still precede a relay architecture lock. The impulse-only interpretation is explicitly a plan; this does not itself settle the architecture of a task workspace. Houston should identify when the proposal crosses into relay work or prohibited orchestration. [flag](/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md:88)
- **L17/L21:** ovitmugen retains view/layout and protected process-lifetime ownership. Shared process/API/CLI layers may be designed, but adoption and implementation need their own release. Keep “new lifetime owner” and “new transport” visible as decisions. [flag](/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md:193), [L21](/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md:244)
- **L20:** terminal observation can inform a controller; it grants no input authority. Do not turn a prompt-looking screen or “idle” classifier into an implicit permission. [flag](/home/hruzam/unikuklatrix/nablarva/.dev/session/flag.md:235)
- **Phone:** its attached-PTY approach is relevant precedent, and its RUNBOOK separates human input from future regulated delivery. Its recorded pilot includes attachment/detachment evidence, but native approvals and special keys remain unqualified; it is explicitly paused. Read its artifacts without resuming or absorbing that gate. [RUNBOOK](/home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/RUNBOOK.md:87), [STATUS](/home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/STATUS.md:25)
- **Termpanum:** reuse its distinction between post-termios byte capture and rendered state. Its X1 qualification is partial and blocked, not an available certified observation service. [STATUS](/home/hruzam/unikuklatrix/nablarva/.dev/session/termpanum-X1-source-qualification/STATUS.md:12)
- **Existing relay qualification:** offline validation has not established a working native submission route. Preserve its target-incarnation and receipt distinctions without importing its entire lifecycle into this preparation. [STATUS](/home/hruzam/unikuklatrix/nablarva/.dev/session/nablarva-02-pipe-qualification/STATUS.md:8)

The separation between conversation and task terminal should be evaluated operationally. One native conversation TUI and one interactive task program competing for the same foreground terminal create a real ownership problem. Two terminals solve that cleanly, but a qualified native tool-session attachment could also satisfy the intent. The researcher’s vendor inventory should determine whether that smaller route exists.

Missing evidence is concentrated in four questions: which native CLIs can access the same live execution session; whether a human can attach independently without ending it; where permissions actually bind; and whether container isolation is needed beyond an ordinary owned process. No current finding proves cross-CLI persistence, native approval preservation, multi-host behavior or recovery after process death.

My proposed preparation gate is:

> Majkee accepts a source-grounded comparison of file-driven jobs, a persistent worker and a shared PTY task session; a frozen six-row synthetic test specification; and Houston’s disposition of lifecycle, delivery and permission boundaries. Open choices remain attributed. Acceptance releases no native-session attachment, container deployment or shared transport adoption.

The next experiment should compare the first two implementations against rows 1–4, then test a minimal control-generation mechanism against rows 5–6. This establishes whether the requested experience requires a PTY and whether takeover works before selecting a product architecture. Cartan can assign implementation within the operator’s existing basic-test authorization; Oraculum’s recommendation adds no execution authority.

```text
ORACULUM RETURN
CYCLE: terminal-workspace-X0-approaches / technical consultation / 2026-11-17
INSIGHT: A file-fed container can carry durable work, but full takeover semantics require continuity of the same running process and a governed interactive terminal boundary.
RECOMMENDATION: 1) Qualify a persistent PTY task session with explicit takeover. 2) Retain files for inspectable requests and receipts. 3) Add containment only when a concrete isolation requirement warrants it; keep native attachment alternatives open.
EVIDENCE: Current flag L3/L4/L14/L17/L20/L21; docs/ARCHITECTURE.md; pipe, phone, termpanum, muticula and ovitmugen session documents; Linux PTY/termios primary documentation. No runtime qualification performed.
CURVATURE: Native attachment capability, task-versus-conversation topology, permission enforcement, lifetime ownership and the relay boundary remain unresolved; no canon lock proposed.
RETURN_TO_CALLER: Preserve this consultation as attributed raw substrate, combine the research inventory and Houston finding, and prepare the bounded six-row comparison without treating any candidate as adopted architecture.
```
