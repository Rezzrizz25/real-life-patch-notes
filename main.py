#!/usr/bin/env python3.13
"""Real-Life Patch Notes: The Comedy Changelog.

Writes the funniest one-line patch note for a bug in real life or human
biology to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only, deterministic.
"""

import os
import sys

# Why this line: it is a real patch-note register ("fixed a memory leak",
# a version number) applied to a universal human bug — the brain replaying
# old embarrassments at 3 a.m. "Memory leak" is genuine software vocabulary,
# so the joke lands inside the form instead of beside it; "since 2009" and
# "3 a.m." are concrete details that make the scene instantly recognisable.
# 113 characters: every word works, no padding, one line.
ENTRY = (
    "v2.7.4: fixed a memory leak where the brain kept every embarrassing "
    "moment since 2009 and replayed them at 3 a.m."
)

MAX_CHARS = 160


def main() -> int:
    if len(ENTRY) > MAX_CHARS:
        print(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in ENTRY.strip():
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read it back: the gate requires UTF-8 text of 1-160 chars, one line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY or len(written) > MAX_CHARS or "\n" in written:
        print("verification failed: output does not match the entry",
              file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
