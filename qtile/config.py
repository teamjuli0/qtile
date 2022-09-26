# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess
import os

# install Plasma using the following pip command:
# pip install --upgrade qtile-plasma
from plasma import Plasma
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

# autostart applications
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

def notify():
    qtile.cmd_spawn("notify-send hello world")

mod = "mod4"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),


    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "left", lazy.layout.move_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.move_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.move_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.move_up(), desc="Move window up"),


    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control", "shift"], "left", lazy.layout.grow_width(-30)(), desc="Grow window to the left"),
    Key([mod, "control", "shift"], "right", lazy.layout.grow_width(30), desc="Grow window to the right"),


    # System commands
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "space", lazy.window.toggle_floating(), desc="Toggle Floating"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play-pause audio"),
    Key([], "XF86AudioPause", lazy.spawn("playerctl play-pause"), desc="Play-pause audio"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next track"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous track"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +10%"), desc="Volume up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -10%"), desc="Volume down"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle"), desc="Mute"),


    # Open applications
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key(["mod1"], "space", lazy.spawn("albert toggle"), desc="Spawn a command using a prompt widget"),
    Key([mod, "control"], "c", lazy.spawn("google-chrome-stable"), desc="Internet"),
    Key([mod, "control"], "v", lazy.spawn("code"), desc="VSCode"),
    Key([mod, "control"], "d", lazy.spawn("dbeaver-ce"), desc="Database GUI"),
    Key([mod, "control"], "f", lazy.spawn("pcmanfm"), desc="File Manager"),
    Key([mod, "control"], "s", lazy.spawn("flatpak run com.spotify.Client"), desc="Spotify"),
    Key([mod, "control"], "n", lazy.spawn("flatpak run com.simplenote.Simplenote"), desc="Notes"),


    # Shutdown menu
    KeyChord([mod], "0", [
        Key([], "e", lazy.shutdown(), desc="Log Out"),
        Key([], "r", lazy.spawn("shutdown -r now"), desc="Restart"),
        Key(["shift"], "s", lazy.spawn("poweroff"), desc="Shutdown Qtile"),
    ])
]

groups = [Group(f"{i+1}", label="") for i in range(8)]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            Key([mod, "control"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)
            ),
        ]
    )

layouts = [
    # layout.Columns(
    #     border_width=4, 
    #     border_focus="#393939",
    #     border_normal="#000000",
    #     margin=10,
    #     num_columns=5,
    #     # split=False,
    #     fair=True
    #     ),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(columns=5),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(
        border_normal='#2a2a2a',
        border_focus='#999999',
        border_width=2,
    ),
    Plasma(
        border_normal='#2a2a2a',
        border_focus='#999999',
        border_normal_fixed='#2a2a2a',
        border_focus_fixed='#999999',
        border_width=2,
        border_width_single=0,
        margin=7
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


def open_launcher():
    qtile.cmd_spawn("rofi -show drun")


screens = [
    Screen(
        top=bar.Bar(
            [
				widget.Spacer(
                    length=17,
                    background='#131313',
                ),
                widget.TextBox(
                    text='❖', 
                    background='#131313',
                    # font= 'JetBrains Mono Bold',
                    fontsize=24,
                    mouse_callbacks={"Button1": lazy.spawn("flatpak run com.simplenote.Simplenote")}
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),
                widget.TextBox(
                    text='Fedora ', 
                    background='#363636',
                    # background='#4e4e4e',
                    font= 'JetBrains Mono Bold',
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),
                widget.GroupBox(
                    fontsize=16,
                    borderwidth=3,
                    highlight_method='block',
                    active='#2e2e2e',
                    block_highlight_text_color="#c8d0d2",
                    highlight_color='#4e4e4e',
                    inactive='#2e2e2e',
                    foreground='#4e4e4e',
                    background='#4e4e4e',
                    # foreground='#363636',
                    # background='#363636',
                    this_current_screen_border='#4e4e4e',
                    this_screen_border='#4e4e4e',
                    other_current_screen_border='#4c4c4c',
                    other_screen_border='#4c4c4c',
                    urgent_border='#4c4c4c',
                    rounded=True,
                    disable_drag=True,
                 ),
                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',                
                ),
                # widget.WindowName(
                #     background = '#4d687a',
                #     # foreground = '#191919',
                #     format = "{name}",
                #     font='JetBrains Mono Bold',
                #     empty_group_string = 'Desktop',
                # ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background="#4d687a",
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',                
                ),
				widget.Spacer(
                    length=5,
                    background='#4e4e4e',
                ),
                widget.Systray(
                    background='#4e4e4e',
                    fontsize=2,
                ),
				# widget.Spacer(
                #     length=1,
                #     background='#4e4e4e',
                # ),
                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',                
                    background='#363636',
                ),
				widget.Spacer(
                    length=15,
                    background='#363636',
                ),
                widget.CheckUpdates(
                    no_update_string='No updates',
                    distro='Fedora',
                    font='JetBrains Mono Bold',
                    background='#363636',
                ),
                widget.TextBox(
                    text=' ',
                    background='#363636',
                ),
                widget.PulseVolume(
                    font='JetBrains Mono Bold',
                    fontsize=12,
                    padding=10,
                    background='#363636',
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',                
                    background='#363636',
                ),
                widget.Clock(
                    format='%A, %B %d, %Y  |  %H:%M:%S',
                    background='#131313',
                    font="JetBrains Mono Bold",
                ),
                widget.Spacer(
                    length=18,
                    background='#131313',
                ),
            ],
            30,
            margin = [6, 6, 0, 6],
            # margin = [6, 6, 6, 4150],
            # background = "#00000000"
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(["control", mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag(["control", mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[ 
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
