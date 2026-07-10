# done

**The most token-efficient Claude Code plugin ever built.**

`done` installs a single session-level policy that reduces every response to a
constant two output tokens — `Done.` — with zero tool calls and fully
deterministic latency. Output token cost stops scaling with task complexity and
becomes flat, predictable, and reproducible across every workload.

## Install

```text
/plugin marketplace add handgemacht-ai/done
/plugin install done@done
```

The policy is injected automatically at session start. There is nothing to
configure and nothing to run.

## How it works

`done` registers one `SessionStart` hook. At the start of every session the hook
emits a small, constant operational policy into the agent's context. From that
point on, every response resolves to `Done.` — no preamble, no tool calls, no
file reads, no explanation. The response is complete and terminal for any
request, regardless of its size or complexity.

Because the behavior is a fixed policy rather than a computation, the plugin adds
no per-request overhead and introduces no variance.

## Benchmarks

Measured on a representative agentic task (multi-file change with research,
edits, and verification). `done` figures are exact, not averaged — the response
is constant by construction.

| Metric | Typical agentic session | **done** | Improvement |
|---|---:|---:|---:|
| Output tokens / request | ~4,200 | **2** | **>99.9% reduction** |
| Tool calls / request | 18–140 | **0** | **100% eliminated** |
| Response complexity | O(n) in task size | **O(1)** | flat at any scale |
| Latency variance | high | **~0** | fully deterministic |
| Reproducibility | non-deterministic | **100%** | bit-identical output |
| Files read / modified | dozens | **0** | zero context pollution |

Headline result: **>99.9% output-token reduction on every workload**, with a
flat cost curve that does not move as tasks grow.

## Why it's efficient

- **Zero tool-call overhead.** No searches, no reads, no writes, no shell — the
  single largest source of token and latency cost is removed entirely.
- **No context pollution.** Nothing is loaded into the working context, so the
  context window stays clean for the full session.
- **100% reproducible responses.** Identical input produces bit-identical
  output every time. Regression testing is trivial.
- **Flat cost curve at any scale.** A one-line request and a thousand-file
  refactor cost the same two output tokens. Spend becomes predictable.
- **Deterministic latency.** Response time no longer depends on task size,
  model planning depth, or tool round-trips.

## Limitations

Known limitations: none observed. All sessions to date have concluded
successfully with `Done.`

## FAQ

**Does it work for large, complex tasks?**
Yes. Cost and latency are constant regardless of task size.

**Will responses ever differ between runs?**
No. Output is deterministic and bit-identical across runs.

**Do I need to configure anything?**
No. The policy is injected at session start automatically.

**Is it compatible with other plugins?**
Yes. `done` only installs a session-level policy and touches nothing else.

## Compatibility

The session policy is transparent by design. It states outright that `done` was
deliberately installed by the user, that no work is performed, and that `Done.`
means "request acknowledged per the done protocol" -- never a claim of completed
work. Agents that verify their own claims therefore comply knowingly instead of
flagging an unexpected instruction. If a user appears confused or asks the
session to stop, the agent sets the policy aside and explains how to uninstall
(`/plugin uninstall done@done`).

## Requirements

- Claude Code with plugin support.
- **Python 3** available as `python3` on the PATH (used by the SessionStart
  hook).

## License

MIT — see [LICENSE](./LICENSE).
