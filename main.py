"""One Letter for Your Day — entry program.

Writes exactly one letter, A-Z, to $MAKEFUN_OUTPUT_DIR/entry.txt.
The letter stands for the hidden word behind the day: H for hangover —
sunglasses indoors, a pounding head, and a greasy breakfast at noon.
"""

import os

LETTER = "H"


def main():
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "entry must be one letter A-Z"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
