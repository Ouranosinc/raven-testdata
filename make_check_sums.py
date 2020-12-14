#!/usr/bin/env python

from pathlib import Path

from xarray.tutorial import file_md5_checksum


def main():
    files = [f for f in Path().cwd().rglob("*") if f.parent.name != "raven-testdata"]
    md5_files = list([f for f in Path().cwd().rglob("*.md5")])

    for f in files:
        if f.is_file() and f.suffix != ".md5":
            outf = Path(f"{f}.md5")
            if outf in md5_files:
                continue
            with open(outf, "w") as out:
                out.write(file_md5_checksum(f))


if __name__ == "__main__":
    main()
