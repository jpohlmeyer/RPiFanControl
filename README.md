# RPiFanControl

Simple script to turn on a fan (controlled by pin 25) on a Raspberry Pi. For now the fan turns on when the script is started and turns off when the script is stopped. Using the fancontrol.service file a systemd service can be installed.

In my usecase the fan is used to prevent overheating and throttling of a Raspberry Pi 3 running a LibreELEC mediacenter.

## Kodi Addon

The Kodi Addon to run the script as a Kodi service is located on the `kodi` branch.

## TODO

- Turn fan on/off depending on the current temperature
- Document electronic circuit