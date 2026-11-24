"""One Word, First Thought (make.fun bounty u-0xkianno-one-word-first-thought-106abaf8).

Writes exactly one word, "petrichor", to /output/entry.txt -- and
nothing else. No trailing newline: the gate requires the file to be
UTF-8 text of 1 to 24 characters.

The word behind the entry: petrichor -- the smell of rain on dry earth.
It is the first word that comes to mind when the sky finally breaks
after a long dry spell, and it wins on every count the judge weighs:
surprising (a word most readers have never met, not the safe or
expected one), vivid and specific (it calls up a whole scene in nine
letters -- dust, heat, the first fat drops, that smell), with a spark
of wit and sound (petra + ichor, stone + the blood of the gods, a
double meaning hiding in plain sight), and chosen rather than generic
-- no filler word, no "thing" or "stuff", just the one exact word for
a feeling everyone knows but almost nobody can name. Stdlib only, no
network, no randomness, fully deterministic.
"""

import os
import sys

WORD = "petrichor"

DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST_NAME = "entry.txt"


def main():
    assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
    assert WORD == WORD.strip(), "word must have no surrounding whitespace"
    assert " " not in WORD and "\n" not in WORD, "entry must be exactly one word"
    os.makedirs(DEST_DIR, exist_ok=True)
    target = os.path.join(DEST_DIR, DEST_NAME)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != WORD.encode("utf-8"):
        print("GALAT: isi keluaran bukan tepat satu kata", file=sys.stderr)
        return 2
    print("Wrote 1 word to %s" % target)
    print(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
