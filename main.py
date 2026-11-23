"""One-Line Roast: The Gadget You Use Every Day — entry for make.fun's
u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

Writes one roast of a gadget or app used every day (at most 200
characters) to the harness output directory as entry.txt. The roast
is a fixed string: no randomness, no network, no time, no input —
two runs produce the same bytes.
"""

import os

# The roast. Target: the phone's autocorrect, a daily app behaviour
# with one concrete detail — it adds an exclamation mark to
# "on my way", so its owner arrives everywhere sounding far more
# excited than they are. Specific, fresh (not the battery complaint
# everyone makes), and the sting lands in the last few words.
LINE = "My phone autocorrects 'on my way' to 'on my way!' so I arrive everywhere sounding far more excited than I actually am."

MAX_CHARS = 200


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} characters, over the {MAX_CHARS} cap"
    assert line.count(".") == 1 and line.endswith("."), "the line must be a single sentence"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
