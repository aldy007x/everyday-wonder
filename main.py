#!/usr/bin/env python3
"""Everyday Wonder entry — a single sentence about an escalator handrail.

Deterministic, no network, no randomness, no external input.
Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

ENTRY = (
    "The escalator handrail glides a half-step ahead of the stairs, so for "
    "one quiet second my hand is travelling into a future my feet have not "
    "reached yet."
)


def main() -> int:
    # Self-check before writing: exactly one non-blank line, 1-200 chars.
    # The line must contain no line breaks at all and must not be
    # whitespace-only; each failure exits non-zero with a clear message.
    if not ENTRY.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(
            f"error: entry is {len(ENTRY)} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    # Verify what was written.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    lines = written.splitlines()
    if len(lines) != 1 or lines[0] != ENTRY or not 1 <= len(lines[0]) <= 200:
        print("error: written entry failed verification", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
