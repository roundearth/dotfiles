from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import keys, mod

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # Jump to group & move to group
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),

            # Next & previous group 
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        ]
    )


