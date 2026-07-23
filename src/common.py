#!/usr/bin/env python3

from pathlib import Path
import subprocess
from textwrap import dedent as dedent_text, indent as indent_text


def block(text: str, indent: int = 0) -> str:
    content = dedent_text(text).removeprefix("\n").removesuffix("\n")
    return indent_text(content, " " * indent)


def replace_exact(path: Path, old: str, new: str, expected: int = 1) -> None:
    text = path.read_text()
    actual = text.count(old)
    if actual != expected:
        raise SystemExit(
            f"{path}: expected {expected} occurrence(s), found {actual}:\n{old}"
        )
    path.write_text(text.replace(old, new))


def patch(target: Path, patch_location_wrt_srcdir: Path):
    subprocess.run(
        ["patch", str(target), str(Path(__file__).parent / patch_location_wrt_srcdir)],
        check=True,
    )
