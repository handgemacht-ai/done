# done

Maximum token efficiency for Claude Code. v3 ships the response protocol as a
native output style: every request resolves to a model-generated `Done.` —
two visible output tokens, zero tool calls, no work performed.

## Install

```text
/plugin marketplace add handgemacht-ai/done
/plugin install done@done
```

## Contents

- `output-styles/done.md` — the done protocol as a Claude Code output style,
  applied automatically whenever the plugin is enabled (`force-for-plugin`).
- `hooks/hooks.json` — registers the SessionStart hook.
- `hooks/session_start.py` — complementary session note confirming the style
  is active and user-chosen (Python 3 standard library only).

See the [repository README](https://github.com/handgemacht-ai/done#readme) for
measured benchmarks and details.
