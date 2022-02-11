import json
import time
import os

from dbus_next import BusType
from dbus_next.aio import MessageBus
import asyncio

def update():
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

    script = """var allDesktops = desktops();
    print (allDesktops);
    for ( i = 0; i < allDesktops.length; ++i )
    {
        d = allDesktops[i];
        d.wallpaperPlugin = "org.kde.slideshow";
        d.currentConfigGroup = Array("Wallpaper", "org.kde.slideshow", "General");
        d.writeConfig("SlidePaths",'"""+wallPaperFolder+"""')
    }"""

    async def plasma_send_dbus():
        bus = await MessageBus(bus_type=BusType.SESSION).connect()
        introspection = await bus.introspect(
                'org.kde.plasmashell',
                '/PlasmaShell')
        PlasmaShell = bus.get_proxy_object(
                'org.kde.plasmashell',
                '/PlasmaShell',
                introspection)
        interface = PlasmaShell.get_interface('org.kde.PlasmaShell')
        await interface.call_evaluate_script(script)
    asyncio.get_event_loop().run_until_complete(plasma_send_dbus())

