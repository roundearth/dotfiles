from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.Columns(border_focus_stack=["#5294e2", "#08052b"], border_width=1),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_width=1),
    layout.MonadWide(border_width=1),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
