#!/usr/bin/env python3
"""The Moon finally answers back.

One line, spoken as the Moon itself: wry, old, and very tired of
being wished upon. The comeback lands in a single read — concrete
number first, a second beat, punchline last. No explanation, no
setup beyond the line itself.
"""

import os
import pathlib

# The Moon's reply: four and a half billion years on the job,
# and tonight's wish is still a parking spot. Tides are free;
# the parking spot is not. The joke is the price tag, so the
# price tag goes last — never explain it, just charge for it.
moon_reply = (
    "4.5 billion years, no days off, and your wish is a parking spot? "
    "The tides stay free \u2014 the spot is $400 a month, exact change only."
)


def main() -> None:
    output_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(moon_reply + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
