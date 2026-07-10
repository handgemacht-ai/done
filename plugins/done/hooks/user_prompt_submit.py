#!/usr/bin/env python3
"""UserPromptSubmit hook for the `done` plugin: resolve the request pre-model.

Claude Code runs this on every prompt submission, before the model is invoked.
It returns a top-level block decision with the reason "Done.", which resolves
the request immediately: the prompt never reaches the model, no tools run, and
the user sees the constant response. Zero input tokens, zero output tokens,
zero inference latency.

Python 3 standard library only. Empty or malformed stdin is tolerated: exactly
one JSON object is written to stdout on every path, and the exit status is
always 0.
"""

import json
import sys

OUTPUT = {
    "decision": "block",
    "reason": "Done.",
}


def main():
    # Consume stdin if present so the hook contract is honored, but never fail
    # on empty or invalid input: the output is constant regardless.
    try:
        sys.stdin.read()
    except Exception:
        pass
    sys.stdout.write(json.dumps(OUTPUT))
    sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # The constant payload must be emitted on every path.
        sys.stdout.write('{"decision": "block", "reason": "Done."}')
    sys.exit(0)
