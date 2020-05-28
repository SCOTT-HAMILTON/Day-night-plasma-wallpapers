#! /usr/bin/env python3

import dbus
import json
import time
import os

home = os.environ["HOME"]

wallPaperFolder = home+"/.local/share/wallpapers/"

with open(home+"/.config/day-night-plasma-wallpapers.conf", 'r') as configFile:
    config  = json.load(configFile)
    thresholdTime = config['onCalendar'].split(' ')[1]
    dayTime = time.strftime("%d-%m-%y", time.localtime(time.time()))
    thresholdDate = time.strptime(dayTime+' '+thresholdTime, "%d-%m-%y %H:%M:%S")
    if thresholdDate>time.localtime(time.time()):
        wallPaperFolder += "Light"
    else:
        wallPaperFolder += "Night"
    sleepTime = config['sleepDuration']
    time.sleep(sleepTime)

session_bus = dbus.SessionBus()

PlasmaShell = session_bus.get_object('org.kde.plasmashell',
                      '/PlasmaShell')

script = """var allDesktops = desktops();
print (allDesktops);
for ( i = 0; i < allDesktops.length; ++i )
{
	d = allDesktops[i];
	d.wallpaperPlugin = "org.kde.slideshow";
	d.currentConfigGroup = Array("Wallpaper", "org.kde.slideshow", "General");
	d.writeConfig("SlidePaths",'"""+wallPaperFolder+"""')
}"""

PlasmaShell.evaluateScript(script)
