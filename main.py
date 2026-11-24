#!/usr/bin/env python3
"""Entry for make.fun's "One Word, One Username, One Reward".

For this competition the entry IS the entrant's own make.fun
username, so the program writes exactly that — "sramadhan-07",
one word of 12 characters — to /output/entry.txt. Standard
library only; no network.
"""

import os

USERNAME = "sramadhan-07"


def main() -> None:
    # Gate guard: the username must stay a single word of 1 to 30
    # characters — anything else would no longer be the username.
    if len(USERNAME.split()) != 1 or not 1 <= len(USERNAME) <= 30:
        raise ValueError("entry must be the username, one word of 1 to 30 characters")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    # The username alone: no decoration, no trailing newline.
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(USERNAME)


if __name__ == "__main__":
    main()
