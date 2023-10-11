from libqtile.lazy import lazy
from libqtile.config import Key
import webbrowser

mod = "mod4"
terminal = "xfce4-terminal"

keys = [
    # Move around in group
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()), 
    Key([mod], "space", lazy.layout.next()),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Resize
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "n", lazy.layout.normalize()),

    # Layout stuff
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod, "shift"], "Space", lazy.next_layout()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    Key([mod], "t", lazy.window.toggle_floating()),

    # Toggle between different layouts as defined below
    Key([mod], "q", lazy.window.kill()),

    # Launch apps
    Key([mod], "d", lazy.spawncmd()),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "n", lazy.spawn("thunar")),
    Key([mod], "w", lazy.spawn("firefox")),
#    Key("Print", lazy.spawn("flameshot")),

    # Reload and shutdown config 
    Key([mod, "shift"], "r", lazy.reload_config()),
    Key([mod, "shift"], "q", lazy.shutdown()),

]
