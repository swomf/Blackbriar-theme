#!/usr/bin/env python3

import configparser
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


def read_config(path: Path) -> configparser.ConfigParser:
    config = configparser.ConfigParser(strict=True)
    with path.open() as stream:
        config.read_file(stream)
    return config


def validate_build(dist: Path) -> None:
    # this can also catch upstream's errors (not just ours) if they have any
    parsed = 0
    for path in sorted(dist.rglob("*")):
        if path.suffix == ".svg":
            ET.parse(path)
        elif path.suffix in (".kvconfig", ".colors"):
            read_config(path)
        else:
            continue
        parsed += 1

    if parsed == 0:
        raise SystemExit(f"{dist}: no themes were emitted")

    # Other than attribution (inspired by...)
    # we don't want to leave stale references to Graphite
    attribution = ("author", "comment")
    for config_path in dist.rglob("*.kvconfig"):
        config = read_config(config_path)
        for section in config.sections():
            for key, value in config[section].items():
                if key in attribution or value is None:
                    continue
                if "Graphite" in value:
                    raise SystemExit(
                        f"{config_path}: [{section}] {key} "
                        f"still references Graphite: {value}"
                    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("call like ./tests/validate.py ./dist")

    print("statically analyzing output...\t\t", end="", flush=True)
    try:
        validate_build(Path(sys.argv[1]).resolve())
    except (SystemExit, ET.ParseError, configparser.Error) as error:
        raise SystemExit(f"BAD.\n{error}") from error
    print("good")
