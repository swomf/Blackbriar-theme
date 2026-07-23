#!/usr/bin/env python3

# just does some copy-renaming
# and basic key changes

import shutil

from ..common import replace_exact
from .kvantum_generated_constants import (
    BUTTON_FOCUSED,
    BUTTON_NORMAL,
    BUTTON_PRESSED,
)


def flatten_command_button_states(path):
    # vinceliuice has a very subtle issue where grey buttons being transparent means
    # that an animate_states=true will show an overshoot. but the background is grey too
    # so it is not obvious... unless the background is black.
    text = path.read_text()
    start_marker = 'id="button-normal-topleft"'
    end_marker = 'id="button-toggled-topleft"'
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    button_states = text[start:end]

    replacements = (
        (
            'style="fill:#ffffff;opacity:0.1"',
            f'style="fill:{BUTTON_NORMAL};opacity:1"',
            3,
        ),
        (
            'style="fill:#ffffff;opacity:0.2"',
            f'style="fill:{BUTTON_FOCUSED};opacity:1"',
            2,
        ),
        (
            'fill="#fff"\n       opacity=".2"',
            f'fill="{BUTTON_FOCUSED}"\n       opacity="1"',
            1,
        ),
        (
            'style="fill:#ffffff;opacity:0.25"',
            f'style="fill:{BUTTON_PRESSED};opacity:1"',
            2,
        ),
        (
            'fill="#fff"\n       opacity=".25"',
            f'fill="{BUTTON_PRESSED}"\n       opacity="1"',
            1,
        ),
    )

    for old, new, expected in replacements:
        actual = button_states.count(old)
        if actual != expected:
            raise SystemExit(
                f"{path}: expected {expected} occurrence(s), found {actual} "
                f"inside command-button states\nsearched for:\n{old}"
            )
        button_states = button_states.replace(old, new)

    path.write_text(text[:start] + button_states + text[end:])


def build_kvantum(upstream, output):
    source = upstream / "Kvantum/Graphite"
    destination = output / "Kvantum/Blackbriar"
    file_map = {
        "Graphite.kvconfig": "Blackbriar.kvconfig",
        "Graphite.svg": "Blackbriar.svg",
        "GraphiteDark.kvconfig": "BlackbriarDark.kvconfig",
        "GraphiteDark.svg": "BlackbriarDark.svg",
    }

    for source_name, destination_name in file_map.items():
        shutil.copy(source / source_name, destination / destination_name)

    for config_name in ("Blackbriar.kvconfig", "BlackbriarDark.kvconfig"):
        config = destination / config_name
        replace_exact(
            config,
            "author=Vince Liuice, based on KvAdapta by Tsu Jan",
            "author=swomf; based on Graphite by Vince Liuice and KvAdapta by Tsu Jan",
        )
        replace_exact(
            config,
            "comment=An uncomplicated theme inspired by the Materia GTK theme",
            "comment=Blackbriar application theme generated from Graphite",
        )

    dark_kvconfig = destination / "BlackbriarDark.kvconfig"

    # GeneralColors window.color, base.color, alt.base.color
    replace_exact(dark_kvconfig, "#2c2c2c", "#000000", expected=2)
    replace_exact(dark_kvconfig, "#2e2e2e", "#000000")

    # fills for the window chrome
    dark_svg = destination / "BlackbriarDark.svg"
    replace_exact(dark_svg, "#2c2c2c", "#000000", expected=51)
    replace_exact(dark_svg, "#3c3c3c", "#000000", expected=5)
    replace_exact(dark_svg, "#1a1a1a", "#000000", expected=17)

    # prevent overshoot on kvantum animate_states
    flatten_command_button_states(dark_svg)
