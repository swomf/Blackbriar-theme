#!/usr/bin/env python3

from .apps import transform_apps, transform_gnome
from .decorations import transform_decorations
from ..common import block, replace_exact


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

    # test on ./gtk/build-gtk4/demos/gtk-demo/gtk4-demo
    # unselected sidebar test was black onb lack because
    # Graphite's listview assumes light accent background
    # ----> we remove Graphite's special row setup
    replace_exact(
        root / "src/sass/gtk/_common-4.0.scss",
        block(
            """
              @if $sidebar =='styled' {
                &.navigation-sidebar {
                  @if $topbar =='dark' and $variant =='light' {
                    margin: 0;
                    background-color: transparent;
                    color: $titlebar-text-secondary;
                  }

                  @else {
                    background-color: $sidebg;
                    color: on($sidebg);
                    margin: 0 0 $menu-radius 0;
                    border-radius: 0 $menu-radius $menu-radius 0;
                  }

                  > row {
                    @extend %sidebar-row;

                    button {
                      @extend %sidebar-flat-button;
                    }
                  }

                  .dim-label {
                    color: on($sidebg, disabled);
                  }
                }
              }
            """,
            indent=2,
        ),
        "",
    )

    transform_decorations(root / "src/sass/gtk/_common-3.0.scss")
    transform_apps(root / "src/sass/gtk/apps/_misc.scss")
    transform_gnome(root / "src/sass/gtk/apps/_gnome-4.0.scss")
