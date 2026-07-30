#!/usr/bin/env python3

from .apps import transform_apps
from .decorations import transform_decorations
from ..common import replace_exact


def build_gtk(root):
    # upstream install.sh derives "Blackbriar-cursors"
    # but we vendor the Qogir theme as "Blackbriar"
    replace_exact(
        root / "install.sh",
        "CursorTheme=${2}-cursors",
        "CursorTheme=Blackbriar",
    )
    # installer affects gtk2.0
    replace_exact(root / "install.sh", "#0F0F0F", "#000000")
    # symlink shouldnt lead to Graphite
    replace_exact(root / "install.sh", "THEME_NAME=Graphite", "THEME_NAME=Blackbriar")
    # basically the mother color file
    for old in ("#030303", "#0F0F0F", "#121212"):
        replace_exact(root / "src/sass/_colors.scss", old, "#000000")

    transform_decorations(root / "src/sass/gtk/_common-3.0.scss")
    transform_apps(root / "src/sass/gtk/apps/_misc.scss")
