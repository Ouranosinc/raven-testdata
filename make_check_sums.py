#!/usr/bin/env python

from pathlib import Path

from xarray.tutorial import file_md5_checksum


def main():
    files = [
        f
        for f in Path().cwd().rglob("*")
        if f.parent.name != "raven-testdata" and not str(f).endswith(".md5")
    ]
    for f in files:
        if f.is_file():
            outf = f"{f.as_posix()}.md5"
            with open(outf, "w") as out:
                out.write(file_md5_checksum(f))


if __name__ == "__main__":
    main()
