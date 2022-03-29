#!/usr/bin/env python3

import sys
import xbmc
import json

def main():
    # Disable Service
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "service.rpifancontrol","enabled":false}}')
    xbmc.executebuiltin('Notification(RPiFanControl, Service Disabled, 2000)')

if __name__ == "__main__":
    main()