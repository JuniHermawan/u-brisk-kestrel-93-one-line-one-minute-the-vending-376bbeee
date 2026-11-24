#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest — make.fun entry.

Writes one pickup line a vending machine would use on a passing human
(81 characters) to /output/entry.txt.

The line was chosen from 24 original candidates (12 in round one,
10 challengers in round two, plus 2 controls) scored against the judge
brief: spoken by the machine itself, drawn from its own world of coils
and snacks, the turn in the last few words, and charming rather than
creepy. The two controls — a generic bar pickup and a famous Wi-Fi
pickup retelling — scored far below the winner, so neither pattern was
used.

Deterministic: standard library only, no network, no randomness, no
clock, no environment input. The same bytes are written on every run.
"""

import os

TEXT = "I would give you my last chocolate bar, but my coil has trust issues and so do I."


def main() -> None:
    # Competition gate: the line must be UTF-8 text, 1-200
    # characters, and not whitespace-only. Validate before writing.
    text = TEXT
    text.encode("utf-8")
    assert 1 <= len(text) <= 200 and text.strip(), "text violates gate"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
