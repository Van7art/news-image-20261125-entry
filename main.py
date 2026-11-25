#!/usr/bin/env python3
"""Copy the entry image to the output directory.

The image for this entry (entry.png, the 25 November 2026 world-news
broadsheet) already sits next to this script in the repository. This
program's only job is to place a byte-identical copy of it at
<MAKEFUN_OUTPUT_DIR>/entry.png and confirm the copy matches.

Standard library only; no network, no randomness, no clock.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "output"


def sha256_of(path):
    """Return the hex SHA-256 digest of the file at *path*."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"error: {SOURCE_NAME} not found next to main.py", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / SOURCE_NAME

    shutil.copyfile(source, destination)

    source_hash = sha256_of(source)
    copied_hash = sha256_of(destination)
    if source_hash != copied_hash:
        print("error: copied file does not match the source", file=sys.stderr)
        return 1

    size = destination.stat().st_size
    print(f"wrote {destination} ({size} bytes, sha256 {copied_hash})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
