#!/usr/bin/env python3
"""The Vacuum's Alibi — one deadpan excuse from a robot vacuum that
missed a spot: the crumb was load-bearing, so the machine left it there
and charged for the inspection.

Pure Python standard library. Writes the entry line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR when set). Deterministic: the same line every run.
"""

import os

LINE = (
    "My sensors classified that spot as a load-bearing crumb: removing it "
    "would collapse the rug's entire economy, so I left it there and billed "
    "you for the inspection."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
