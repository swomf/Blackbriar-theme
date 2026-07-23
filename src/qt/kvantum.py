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
