#!/usr/bin/env python3
"""Two Lines to Your Past Self — entry writer.

Writes the winning two-line warning to /output/entry.txt.
Gate: UTF-8 text, 1-280 characters, exactly 2 lines.
Line 1: warning to past self about one specific moment, one sentence.
Line 2: one sentence why that moment mattered and what changed.

Winner of a 10-variant pairwise tournament (beat V1, V4, V6, V9):
the voicemail moment won on concreteness (singing happy birthday,
eleven seconds) and irreversible cause-effect (last time hearing her voice).
No trailing newline: the file must read as exactly 2 lines.
"""

import os

ENTRY = (
    "Don't delete Grandma's voicemail the morning she calls to sing you happy birthday.\n"
    "It's the last time you'll ever hear her voice, and every birthday after it you'll wish you'd kept those eleven seconds."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
