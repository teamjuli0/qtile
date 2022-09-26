#!/bin/sh
albert &
flameshot &
xset s off &
xset -dpms &
openrgb -p off.orp &
xrandr --output DisplayPort-2 --primary --mode 5120x1440 --rotate normal --rate 120 --output &DisplayPort-1 --off --output DisplayPort-0 --off --output HDMI-A-0 --off &
nitrogen --restore &
picom --corner-radius 15 --round-borders 15 &
start-pulseaudio-x11 &
volumeicon &
nm-applet &
solaar --window=hide &
dunst -config ~/.config/dunst/dunstrc &
python3 /opt/thefanclub/overgrive/overgrive &