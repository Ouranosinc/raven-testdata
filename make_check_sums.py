#!/usr/bin/env python

import hashlib
from pathlib import Path


def file_md5_checksum(fname):

    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        hash_md5.update(f.read())
    return hash_md5.hexdigest()


def valid(path):
    """Return True if path should be considered for the creation of md5 checksum.

    Parameters
    ----------
    path : Path
      Path object.
    """

    # Exclude top-level files
    if len(path.parts) == 1:
        return False

    # Exclude hidden files
    if any([p.startswith(".") for p in path.parts]):
        return False

    # Exclude md5 files
    if path.suffix == ".md5":
        return False

    if path.is_file():
        return True


def main(dry_run=False):
    """Create checksum files."""
    cwd = Path(".")
    files = filter(valid, cwd.rglob("**/*"))

    for file in files:
        md5 = Path(f"{file}.md5")
        if not md5.exists():
            if dry_run:
                print(f"Create checksum for {file}")
                continue

            with open(md5, "w") as out:
                out.write(file_md5_checksum(file))


if __name__ == "__main__":
    main()
