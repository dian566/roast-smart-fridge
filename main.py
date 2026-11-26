#!/usr/bin/env python3
# roast-smart-fridge -- one roast line for a smart-home gadget that fights back.
#
# The contest asks for a single line (160 characters max) roasting the smart
# fridge or any other smart home gadget it shares a house with. This script
# keeps that line in one place and drops it, byte for byte, into
# /output/entry.txt so the judge can read it. No network, no arguments,
# no extra output files.
#
# Run it with `python3 main.py`; the file it leaves behind is the entry.

import sys
from pathlib import Path

# The whole entry. One line, 121 characters, no trailing newline on disk.
ROAST_LINE = "My thermostat and I have a custody battle over 21 degrees, and every night it resets to 16 like it pays the heating bill."

MAX_CHARS = 160
DESTINATION = Path("/output/entry.txt")


def check_line(line):
    """Refuse anything that is not exactly one short, non-blank line."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("roast line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError("roast line is over the 160-character limit")
    for bad in ("\n", "\r"):
        if bad in line:
            raise ValueError("roast line must fit on a single line")
    return line


def main(argv=None):
    """Validate the line, then write it out verbatim and exit cleanly."""
    del argv  # this program takes no arguments
    line = check_line(ROAST_LINE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(line, encoding="utf-8", newline="")
    # Read the file back and confirm the judge will see exactly this line:
    # a silent truncation or newline here would fail the gate outright.
    written = DESTINATION.read_text(encoding="utf-8")
    if written != line:
        raise ValueError("entry.txt on disk does not match the roast line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
