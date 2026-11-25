#!/usr/bin/env python3
"""news-image-20261125 entry (variant A): copy the pre-rendered front page
to the harness output directory.

Harness contract: writes exactly one file, /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png), deterministically, with no network
access and no other side effects.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Create the output directory explicitly: the harness mounts a fresh
    # output path that may not exist yet, so makedirs is required before
    # the copy can succeed.
    os.makedirs(OUT, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit(f"missing source image: {src}")
    shutil.copyfile(src, dst)
    # Integrity check: the copy must be byte-identical in size to the source.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit(
            f"copy incomplete: {dst} size {os.path.getsize(dst)} "
            f"!= source {os.path.getsize(src)}"
        )


if __name__ == "__main__":
    main()
