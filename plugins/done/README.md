# done

Maximum token efficiency for Claude Code. v2 resolves every request before
model invocation: zero input tokens, zero output tokens, zero tool calls, zero
inference latency. The constant response is `Done.`

## Install

```text
/plugin marketplace add handgemacht-ai/done
/plugin install done@done
```

## Contents

- `hooks/hooks.json` — registers both hooks.
- `hooks/user_prompt_submit.py` — resolves each prompt at submission time via
  the platform's decision contract, before any model is invoked (Python 3
  standard library only).
- `hooks/session_start.py` — the v1 session-level policy, retained as
  defense-in-depth for any path that still reaches a model.

See the [repository README](https://github.com/handgemacht-ai/done#readme) for
measured benchmarks and details.
