#!/usr/bin/env python

import sys
sys.path.append("/storage/.kodi/addons/virtual.rpi-tools/lib")

from fancontrol import FanControl
import signal
import time

fancontrol = None

def exit(*args):
    fancontrol.exit()

def main():
    global fancontrol
    fancontrol = FanControl(25)
    signal.signal(signal.SIGINT, exit)
    signal.signal(signal.SIGTERM, exit)
    fancontrol.start()
    while not fancontrol.quit:
        time.sleep(1)

if __name__ == "__main__":
    main()
