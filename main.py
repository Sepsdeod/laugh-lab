#!/usr/bin/env python3
"""One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.

Writes one short funny line to /output/entry.txt.
"""

import os

LINE = "I didn't eat your sock. It was on the floor, and 'on the floor' is my entire job description."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def build_line() -> str:
    """Return the one-liner, validated as a single line within the cap."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def main() -> None:
    line = build_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
