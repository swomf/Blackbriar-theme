# Blackbriar Theme

Sharp, unified theme focused on black backgrounds and white outlines,
based on vinceliuice's [Graphite GTK][ggtk] and [Graphite KDE][gkde] themes.

![](./preview.webp)

## setup

First make sure this setup is actually relevant to you.
I'm on Hyprland, so I don't really target KDE or XFCE.

| Component                                    | Status                                       |
| -------------------------------------------- | -------------------------------------------- |
| GTK 3 and GTK 4 applications                 | Supported                                    |
| libadwaita                                   | Supported (by vinceliuice's symlink forcing) |
| Qt6  widgets through Kvantum                 | Supported                                    |
| KDE/Qt color scheme                          | Supported                                    |
| Hyprland                                     | Yeah (too lazy to test elsewhere)            |
| XFCE and XFWM                                | Inherited; who knows if it works             |
| Plasma Shell, Aurorae, SDDM, lock-screen QML | NOT INCLUDED (kde's DE will def be broken)   |

Good? Great. Pull

```sh
git clone --recurse-submodules https://github.com/swomf/Blackbriar-theme
cd Blackbriar-theme
# if u cloned but forgot to submodule:
# git submodule update --init --recursive
```

then install

```sh
./scripts/install
# Or install one side:
# ./scripts/install gtk
# ./scripts/install qt
```

then equip the themes with your favorite theme switcher tools:

- `nwg-look` -> Blackbriar-Dark
- `kvantummanager` -> BlackbriarDark
- `qt6ct` -> kvantum-dark
- `hyprland` -> `hl.env("QT_QPA_PLATFORMTHEME", "qt6ct")`
  - Don't set `"QT_STYLE_OVERRIDE"`, I don't think it's necessary.

## what is this nonsense?

I really like vinceliuice's [Graphite GTK][ggtk] and [Graphite KDE][gkde]
themes. But I found that the maintaining of forks ([1][sgtk], [2][skde])
was too annoying for what I wanted. Since I don't use KDE or XFCE anymore
I don't need full-fledged QML or whatnot. I just carefully change values.

This repo bootstraps my careful changes atop pinned vinceliuice commits.

The former [Blackbriar GTK][sgtk] and [Blackbriar KDE][skde]
repositories are just historical now. Compared to the old repos,

- I don't use the `-compact` version
- kvantum _actually_ themes QT apps
- I don't maintain half-broken QML

### but swomf, doesn't this sacrifice git's advantages??

Maybe. But my change style is odd and not really well-represented
by forking/patching. Here

- I just pin the git submodules
- I transform by tracking the amount of matches I change then
  review whenever I hop to the present

[ggtk]: https://github.com/vinceliuice/Graphite-gtk-theme
[gkde]: https://github.com/vinceliuice/Graphite-kde-theme
[sgtk]: https://github.com/swomf/Blackbriar-gtk-theme
[skde]: https://github.com/swomf/Blackbriar-kde-theme
