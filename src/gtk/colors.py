from ..common import replace_exact


def transform_colors(path):
    for old in ("#030303", "#0F0F0F", "#121212"):
        replace_exact(path, old, "#000000")
