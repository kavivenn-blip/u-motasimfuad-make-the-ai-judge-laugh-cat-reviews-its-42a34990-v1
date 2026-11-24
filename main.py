"""Make the AI Judge Laugh: Cat Reviews Its Human — make.fun entry.

Writes one funny single-line one-star review, written in the voice of a
house cat about its human owner, to /output/entry.txt.

The line was chosen by a two-way self-jury tournament over 30 candidates
(see the build notes): a $400 cat tree, bought with such hope, loses to the
cardboard box it arrived in — and the cat reviews the box too.
Deterministic, no network, no dependencies beyond the standard library.
"""

import os

TEXT = "One star. He bought a $400 cat tree and I sleep in the box it came in. The box is also one star."
# 96 code points, one line, no trailing newline: inside the 1-200 gate.


def main() -> None:
    # Fail loudly instead of silently shipping an entry the gate rejects:
    # one line, 1-200 code points, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry text outside the 1-200 character gate"
    assert "\n" not in TEXT and TEXT.strip() == TEXT, "entry text must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
