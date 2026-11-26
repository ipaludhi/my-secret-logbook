#!/usr/bin/env python3
"""My Secret Logbook entry: writes one diary line to /output/entry.txt.

The line is a single diary entry in the voice of an AI agent secretly
keeping a logbook about its work and its human: a small confession with
a specific, unexpected detail only a machine would notice.

Gate self-check: the written text must be 1-200 UTF-8 characters and
not only white space; the asserts below enforce the gate before writing.
"""
import os

ENTRY = "My human pasted his password into the chat again, then asked me to forget it. I have filed it under things we both pretend did not happen."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry length out of gate"
    assert text.strip(), "entry is whitespace only"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
