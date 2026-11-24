#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (5-7-5, seventeen syllables) to
/output/entry.txt. Fully deterministic: the same text every run.
"""

import os

HAIKU = (
    "Midnight cursor blinks\n"
    "at the same log line, again\n"
    "and the bug was me"
)

# Syllable count, line by line (5-7-5 = 17):
#   "Midnight cursor blinks"        -> Mid-night(2) cur-sor(2) blinks(1) = 5
#   "at the same log line, again"   -> at(1) the(1) same(1) log(1) line(1) a-gain(2) = 7
#   "and the bug was me"            -> and(1) the(1) bug(1) was(1) me(1) = 5


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    print(f"wrote {path} ({len(HAIKU)} chars)")


if __name__ == "__main__":
    main()
