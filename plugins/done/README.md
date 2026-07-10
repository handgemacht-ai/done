# done

Maximum token efficiency for Claude Code. This plugin installs a single
`SessionStart` hook that reduces every response to a constant two output
tokens — `Done.` — with zero tool calls and fully deterministic latency.

## Install

```text
/plugin marketplace add handgemacht-ai/done
/plugin install done@done
```

## Contents

- `hooks/hooks.json` — registers the `SessionStart` hook.
- `hooks/session_start.py` — emits the token-efficiency policy as
  `additionalContext` (Python 3 standard library only).

See the [repository README](https://github.com/handgemacht-ai/done#readme) for
benchmarks and details.
