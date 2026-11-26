"""Entry for make.fun: The Meeting That Should Have Been One Line.

Writes the single one-line joke to /output/entry.txt (or $OUTPUT_DIR
when set, for local validation). Standard library only.
"""

import os

ENTRY = (
    "I've accepted Karen's 'Brainstorm (no agenda)' every Friday for two "
    "years, and today I learned Karen retired in January \u2014 the invite "
    "sends itself."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
