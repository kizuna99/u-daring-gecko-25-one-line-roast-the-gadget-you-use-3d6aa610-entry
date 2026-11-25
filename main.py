#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Entry for make.fun bounty u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

Writes one original roast line to the output directory's entry.txt
(MAKEFUN_OUTPUT_DIR, default /output). Deterministic, stdlib only.
"""
import os
from pathlib import Path

LINE = "My wireless earbuds are a marriage: the left one's at 100%, the right one's at 3%, and the case sits there fully charged like it pays rent."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
