from ..common import block, replace_exact


def transform_decorations(path):
    replace_exact(
        path,
        block(
            """
            border-radius: $window-radius + 2px;
            border: 2px solid $primary;
            background-clip: border-box;
            """,
            indent=4,
        ),
        block(
            """
            border-radius: 12px 12px 0 0;
            border-width: 0;
            box-shadow: $shadow-z4, 0 0 50px transparent, 0 0 0 2px $primary;
            background-clip: border-box;
            """,
            indent=4,
        ),
    )
    replace_exact(
        path,
        block(
            """
            @if $rimless == 'false' {
              border: 2px solid $primary;
              background-clip: border-box;
            }
            """,
            indent=4,
        ),
        block(
            """
            @if $rimless == 'false' {
              border-radius: 12px 12px 0 0;
              border-width: 0;
              box-shadow: $shadow-z4, 0 0 50px transparent, 0 0 0 2px $primary;
              background-clip: border-box;
            }
            """,
            indent=4,
        ),
    )
