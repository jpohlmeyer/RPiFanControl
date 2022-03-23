#!/usr/bin/env python

import xbmc
from fancontrol import FanControl

def main():
    monitor = xbmc.Monitor()
    fancontrol = FanControl(25)
    fancontrol.start()
    while not monitor.abortRequested():
        if monitor.waitForAbort(10):
            break
    fancontrol.exit()

if __name__ == "__main__":
    main()
