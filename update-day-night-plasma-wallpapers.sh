#!/bin/sh

# Wait until plasma is loaded
sleep 10

if [ "$(date +%H)" -ge 16 ]; then
	WALLPAPERDIR="~/local/wallpapers/macOS-Mojave-Night"
else
	WALLPAPERDIR="~/.local/wallpapers/macOS-Mojave-Light"
fi

qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops();

print (allDesktops);for (i=0;i<allDesktops.length;i++) {
d = allDesktops[i];d.wallpaperPlugin = "org.kde.slideshow";
d.currentConfigGroup = Array("Wallpaper", "org.kde.slideshow", "General");
d.writeConfig("SlidePaths", "'${WALLPAPERDIR}'")}'
