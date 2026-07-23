#!/usr/bin/env python3

from pathlib import Path
import shutil
import sys

from .common import patch
from .qt.kvantum import build_kvantum


def build_theme(gtk_output: Path, kde_upstream: Path, qt_output: Path) -> None:
    build_kvantum(kde_upstream, qt_output)

    colors = qt_output / "color-schemes/Blackbriar.colors"
    shutil.copy(
        kde_upstream / "color-schemes/GraphiteDark.colors",
        colors,
    )
    patch(colors, Path("qt/colors.patch"))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("expected 3 args")
    gtk_destination, graphite_kde, qt_destination = tuple(
        Path(argument).resolve() for argument in sys.argv[1:]
    )
    build_theme(gtk_destination, graphite_kde, qt_destination)
