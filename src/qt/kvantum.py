#!/usr/bin/env python3

# just does some copy-renaming
# and basic key changes

import shutil

from ..common import replace_exact


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
