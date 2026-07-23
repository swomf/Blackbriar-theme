from ..common import block, replace_exact


def transform_apps(path):
    replace_exact(
        path,
        block(
            """
            window.background.chromium {
              background-color: $surface;

              decoration {
                // border: none;
                background-clip: padding-box;
                box-shadow: $shadow-z16;
            """
        ),
        block(
            """
            window.background.chromium {
              background-color: $surface;

              decoration {
                // border: none;
                background-clip: padding-box;
                box-shadow: 0 0 0 2px $primary;
            """
        ),
    )
