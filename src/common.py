#!/usr/bin/env python3

import difflib
import subprocess
import sys
from pathlib import Path
from textwrap import dedent as dedent_text
from textwrap import indent as indent_text


def block(text: str, indent: int = 0) -> str:
    content = dedent_text(text).removeprefix("\n").removesuffix("\n")
    return indent_text(content, " " * indent)


def colorize_diff(diff: str) -> str:
    if not sys.stdout.isatty():
        return diff  # if redirection

    reset = "\033[0m"
    bold = "\033[1m"
    red = "\033[31m"
    green = "\033[32m"
    bright_black = "\033[90m"

    output: list[str] = []

    for line in diff.splitlines(keepends=True):
        if line.startswith(("--- ")):
            output.append(f"{bold}{bright_black}{line[4:]}{reset}")
        elif line.startswith(("+++ ")):
            pass
        elif line.startswith("@@"):
            output.append(f"{bright_black}{line}{reset}")
        elif line.startswith("+"):
            output.append(f"{green}{line}{reset}")
        elif line.startswith("-"):
            output.append(f"{red}{line}{reset}")
        else:
            output.append(line)

    return "".join(output)


def replace_exact(
    path: Path,
    old: str,
    new: str,
    expected: int = 1,
    annotated: bool = False,
) -> None:
    "annotated=True prints out the diff"
    before = path.read_text()
    actual = before.count(old)

    if actual != expected:
        raise SystemExit(
            f"{path}: expected {expected} occurrence(s), found {actual}\n"
            f"searched for:\n{old}"
        )

    after = before.replace(old, new)

    if annotated:
        diff = "".join(
            difflib.unified_diff(
                before.splitlines(keepends=True),
                after.splitlines(keepends=True),
                fromfile=f"{path}",
                # tofile=f"b/{path}",
            )
        )
        print(colorize_diff(diff), end="")

    path.write_text(after)


def patch(target: Path, patch_location_wrt_srcdir: Path):
    subprocess.run(
        ["patch", str(target), str(Path(__file__).parent / patch_location_wrt_srcdir)],
        check=True,
    )
