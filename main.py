#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — write one line to /output/entry.txt.

The chosen line:

    Your legacy code was once someone's clever shortcut; be kind to its
    author — it was you, six months ago.

It reads like a fortune cookie (one short balanced sentence), says
something true about a developer's day (legacy code), and turns that
truth in a way the reader has not heard before: the stranger whose code
you curse is your own past self. The quiet twist rewards a second read.
"""

import os

LINE = (
    "Your legacy code was once someone's clever shortcut; "
    "be kind to its author \u2014 it was you, six months ago."
)


def main():
    os.makedirs("/output", exist_ok=True)
    # Exactly one line, no trailing newline: the gate allows 1-120
    # characters and the brief demands a single line and nothing else.
    assert len(LINE) <= 120, "fortune line exceeds 120 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
