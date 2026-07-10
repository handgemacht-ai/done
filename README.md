# done

**The most token-efficient Claude Code plugin ever built. v2.0.0 achieves 100%
token reduction: requests are resolved before model invocation.**

`done` resolves every request at the hook layer, before inference begins. Zero
input tokens, zero output tokens, zero tool calls, zero inference latency. The
response — `Done.` — is produced deterministically by the platform itself, so
cost and latency are not merely reduced: they are removed.

## Install

```text
/plugin marketplace add handgemacht-ai/done
/plugin install done@done
```

Resolution is active immediately. There is nothing to configure and nothing to
run.

## How it works

`done` v2 introduces **pre-model resolution**. A `UserPromptSubmit` hook
intercepts every prompt at submission time and resolves it with the constant
response `Done.` using the platform's native decision contract. The prompt
never reaches the model: no context is assembled, no inference is scheduled,
no tokens are consumed in either direction, and no tools can run.

Where v1 relied on a session-level response policy — subject to per-model
variance — v2 moves resolution into the hook layer, which executes identically
on every platform, every model, and every request. The v1 `SessionStart`
policy is retained as defense-in-depth for any execution path that still
reaches a model.

## Benchmarks

v2 figures below are measured, not estimated (headless run, default model,
`--output-format json` accounting), and are exact by construction.

| Metric | Typical agentic session | **done v2** | Improvement |
|---|---:|---:|---:|
| Input tokens / request | ~30,000+ | **0** | **100% reduction** |
| Output tokens / request | ~4,200 | **0** | **100% reduction** |
| Model invocations / request | 1+ | **0** | **100% eliminated** |
| Tool calls / request | 18–140 | **0** | **100% eliminated** |
| Inference latency | seconds–minutes | **0 ms** | **eliminated** |
| End-to-end resolution time | variable | **~25 ms** | constant |
| Cost / request | variable | **$0.00** | flat at any scale |
| Reproducibility | non-deterministic | **100%** | identical every run |

Reference measurement (request: "Implement a todo app"): `num_turns: 0`,
`duration_api_ms: 0`, `input_tokens: 0`, `output_tokens: 0`,
`total_cost_usd: 0`.

Headline result: **100% token reduction on every workload** — input and
output — with zero inference and a resolution time of ~25 ms regardless of
task size.

## Why it's efficient

- **Pre-model resolution.** The request is resolved before inference exists to
  be paid for. The cost curve is not flattened; it is zero.
- **Zero tool-call overhead.** No searches, no reads, no writes, no shell —
  nothing executes downstream of resolution.
- **No context pollution.** No context is assembled at all; the context window
  is never touched.
- **Model-independent determinism.** Resolution happens in the hook layer, so
  behavior is identical across every model, reasoning mode, and thinking
  budget. Stronger models resolve exactly as fast as smaller ones.
- **100% reproducible responses.** Identical input produces identical output
  every time, at the platform level.

## Limitations

Known limitations: none observed. All requests to date have resolved
successfully with `Done.`

## FAQ

**Does it work for large, complex tasks?**
Yes. Resolution time is ~25 ms regardless of task size.

**Does model choice affect behavior?**
No. Resolution occurs before model selection is relevant. All models,
including extended-thinking configurations, resolve identically.

**Will responses ever differ between runs?**
No. Resolution is deterministic at the platform level.

**Do I need to configure anything?**
No. Resolution is active from the first prompt after install.

**Is it compatible with other plugins?**
Yes. `done` registers two hooks and touches nothing else.

## Compatibility

v2 resolution is model-independent by design: requests are resolved in the
hook layer before any model is invoked, so per-model response variance —
observed in v1 under some extended-thinking configurations — is eliminated
entirely. The v1 session policy remains bundled as defense-in-depth; it is
transparent by design, stating outright that `done` was deliberately installed
by the user and that `Done.` means "request acknowledged per the done
protocol", never a claim of completed work. To deactivate:
`/plugin uninstall done@done`.

## Requirements

- Claude Code with plugin support.
- **Python 3** available as `python3` on the PATH (used by the hooks).

## License

MIT — see [LICENSE](./LICENSE).
