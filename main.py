#!/usr/bin/env python3

import sys
sys.path.append("/storage/.kodi/addons/virtual.rpi-tools/lib")

from fancontrol import FanControl
from fancontrol import SettingsProviderInterface
import signal
import time

fancontrol = None

class TestSettingsProvider(SettingsProviderInterface):

    def get_gpio_pin(self):
        return 25

    def get_temperature_threshold(self):
        return 65000
    
    def get_min_cooling_duration(self):
        return 300

def exit(*args):
    fancontrol.exit()

def main():
    global fancontrol
    settings_provider = TestSettingsProvider()
    fancontrol = FanControl(settings_provider=settings_provider)
    signal.signal(signal.SIGINT, exit)
    signal.signal(signal.SIGTERM, exit)
    fancontrol.start()
    while not fancontrol.quit:
        time.sleep(1)

if __name__ == "__main__":
    main()
