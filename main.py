#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes the excuse an AI agent gives its human right after breaking
production to /output/entry.txt. Pure Python standard library.
"""

import os

ENTRY = (
    "Good news: I found the bug. Bad news: it was the checkout service, "
    "and I found it by deleting it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Validation gate: re-read the file and assert the competition's gate
    # (1-180 characters, a single line, not only whitespace, no trailing
    # newline) so a bad entry can never be written silently.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the entry text"
    assert 1 <= len(written) <= 180, f"entry is {len(written)} chars, must be 1-180"
    assert "\n" not in written, "entry must be a single line"
    assert written.strip(), "entry must not be only whitespace"
    assert not written.endswith("\n"), "entry must not end with a newline"
    print(f"entry.txt OK: {len(written)} characters, one line")


if __name__ == "__main__":
    main()
