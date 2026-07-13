# done

Maximum token efficiency for Claude Code. v3 ships the response protocol as a
native output style: every request resolves to a model-generated `Done.` —
two visible output tokens, zero tool calls, no work performed.

## Install

```text
/plugin marketplace add handgemacht-ai/done
/plugin install done@done
```

Installing the plugin makes the `done` output style available; select it to
turn it on. See **Enable the output style** in the
[repository README](https://github.com/handgemacht-ai/done#readme).

## Contents

- `output-styles/done.md` — the done protocol as a Claude Code output style.

See the [repository README](https://github.com/handgemacht-ai/done#readme) for
measured benchmarks and details.
