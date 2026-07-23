#!/usr/bin/env python3

from pathlib import Path
import subprocess


def patch(target: Path, patch_location_wrt_srcdir: Path):
    subprocess.run(
        ["patch", str(target), str(Path(__file__).parent / patch_location_wrt_srcdir)],
        check=True,
    )
