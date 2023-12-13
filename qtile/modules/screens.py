from libqtile import bar, widget 
from libqtile.config import Screen
import os

screens = [
    Screen(
        top=bar.Bar(
            [
                ## Right side
                widget.GroupBox(),
                widget.CurrentLayout(),
                widget.Prompt(),
                widget.Spacer(),

                ## Left side
                widget.Clock(format="%d.%m | %H:%M"),
                widget.TextBox(text = ': :'),
                widget.DF(
                    format = 'DISK: {uf}',
                    visible_on_warn = False,
                    warn_space = 10,
                    ),
                widget.TextBox(text = ': :'),
                widget.CPU(format = 'CPU: {load_percent}%'),
                widget.TextBox(text = ': :'),
                widget.Memory(format = 'MEM: {MemPercent}%'),
                widget.TextBox(text = ': :'),
                widget.ThermalSensor(),
                widget.TextBox(text = ': :'),
                widget.Battery(
                    format='BAT: {percent:2.0%}',
                    low_percentage=0.2,
                    notify_below=0.1,
                    ),
                # pavucontrol
                ## plug in from i3config?

                # 
                widget.TextBox(text = ': :'),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]
