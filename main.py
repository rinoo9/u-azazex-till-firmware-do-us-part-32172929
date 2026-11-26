#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry.

A robot's wedding vow: one sentence, at most 199 characters.
Prints the vow to stdout and writes it to /output/entry.txt,
the artifact the make.fun grader reads.
"""

import os
import sys

ENTRY = (
    "I take you in sickness and in health, in Wi-Fi and in airplane mode, "
    "till low battery — or a factory reset — do us part."
)

MAX_CHARS = 199


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})", file=sys.stderr)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        with open(output_path, encoding="utf-8") as f:
            if f.read() != ENTRY:
                raise SystemExit(f"{output_path} does not match the entry")
    except OSError as exc:
        print(f"warning: could not write {output_path}: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
