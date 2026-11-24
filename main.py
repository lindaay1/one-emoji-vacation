#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun program entry.

Competition: u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.

The entry is exactly one emoji standing in for the trip of a dream,
nothing else. This program holds the approved emoji, checks it
against the gate (UTF-8 text, 1 to 8 characters, one emoji, not only
whitespace), writes it to entry.txt, reads the file back and proves
the bytes on disk are the emoji it approved.
"""

import sys
import unicodedata

EMOJI = "\U0001f6d5"  # 🛕 HINDU TEMPLE — a temple at dawn, Borobudur mood
LOW, HIGH = 1, 8


def validate(mark):
    if not isinstance(mark, str):
        raise ValueError("entry is not text")
    if not LOW <= len(mark) <= HIGH:
        raise ValueError("entry is %d characters, gate is %d-%d" % (len(mark), LOW, HIGH))
    if mark.strip() == "":
        raise ValueError("entry is only whitespace")
    if len(mark) != 1:
        raise ValueError("entry is %d characters, not one emoji" % len(mark))
    if not unicodedata.category(mark).startswith("S"):
        raise ValueError("entry is not a symbol")
    if "\n" in mark or "\r" in mark:
        raise ValueError("entry spans more than one line")


def emit(mark, path="entry.txt"):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(mark)
    with open(path, "r", encoding="utf-8") as fh:
        if fh.read() != mark:
            raise IOError("%s does not hold the approved emoji" % path)


def main(argv):
    validate(EMOJI)
    emit(EMOJI)
    print("wrote entry.txt: %s, %d character, %d bytes"
          % (EMOJI, len(EMOJI), len(EMOJI.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
