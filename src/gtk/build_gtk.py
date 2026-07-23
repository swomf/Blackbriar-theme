#!/usr/bin/env python3

from .apps import transform_apps
from .colors import transform_colors
from .decorations import transform_decorations


def build_gtk(root):
    transform_colors(root / "src/sass/_colors.scss")
    transform_decorations(root / "src/sass/gtk/_common-3.0.scss")
    transform_apps(root / "src/sass/gtk/apps/_misc.scss")
