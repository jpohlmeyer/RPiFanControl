#!/usr/bin/env python

import sys
import xbmc
import xbmcaddon
from fancontrol import FanControl
from fancontrol import SettingsProviderInterface

class AddonSettingsProvider(SettingsProviderInterface):

    def __init__(self):
        self.addon = xbmcaddon.Addon()

    def get_gpio_pin(self):
        return self.addon.getSettingInt(id='gpiopin')

    def get_temperature_threshold(self):
        return self.addon.getSettingInt(id='temperaturethreshold') * 1000
    
    def get_min_cooling_duration(self):
        return self.addon.getSettingInt(id='minimumcoolingduration')

def main():
    print(sys.argv[0])
    monitor = xbmc.Monitor()
    settings_provider = AddonSettingsProvider()
    fancontrol = FanControl(settings_provider=settings_provider)
    fancontrol.start()
    while not monitor.abortRequested():
        if monitor.waitForAbort(10):
            break
    fancontrol.exit()

if __name__ == "__main__":
    main()
