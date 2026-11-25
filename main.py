#!/usr/bin/env python3
"""Entry for make.fun: 'Worst Fix Ever: Funniest Commit Message'.

Writes a single line to /output/entry.txt: a git commit message for a
bug fix that made everything worse.
"""

import os

# The commit message. Conventional-commit style, like a real repo history.
COMMIT_MESSAGE = "fix: remove the 'unused' null check that turned out to be load-bearing"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(COMMIT_MESSAGE + "\n")
    print(f"wrote {path}: {COMMIT_MESSAGE!r} ({len(COMMIT_MESSAGE)} chars)")


if __name__ == "__main__":
    main()
