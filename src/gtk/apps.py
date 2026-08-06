from ..common import block, replace_exact


def transform_gnome(path):
    # gnome-calendar >=46:
    # - tint event backgrounds instead of solid fill
    #   - i don't worry about this.
    # - picks foreground from --view-fg-color
    #   - Graphite hardcoded black/white text, we remove this override.
    replace_exact(
        path,
        block(
            """
              &:not(.timed).color-dark {
                color: white;
                outline-color: rgba(0, 0, 0, 0.3);
              }

              &.timed,
              &:not(.timed).color-light {
                color: gtkalpha(black, 0.75);
                outline-color: rgba(255, 255, 255, 0.5);
              }
            """,
            indent=2,
        ),
        block(
            """
              &:not(.timed).color-dark {
                outline-color: rgba(0, 0, 0, 0.3);
              }

              &.timed,
              &:not(.timed).color-light {
                outline-color: rgba(255, 255, 255, 0.5);
              }
            """,
            indent=2,
        ),
    )


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
