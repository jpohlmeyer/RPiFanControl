# RPiFanControl

Simple script to turn on a fan (controlled by GPIO Pin 25) on a Raspberry Pi. The fan will turn on once the temperature reaches 65°C. Every 5 minutes the script checks the temperature again and turn the fan off if the temperature dropped below the threshold.

The GPIO pin number, the temperature threshold and the minimum cooling interval can be configured.

In my use case the fan is used to prevent overheating and throttling of a Raspberry Pi 3 Model B running a LibreELEC mediacenter.

## Kodi Addon

To build the Kodi Addon .zip file use the `build-addon-zip.sh` script.
The script executed in the addon is `addon.py`.

The Leia (EOL) version of the addon is available on the `leia` branch or at the `leia_eol` tag.

## Testing

If you want to test the script on the command line you can use `main.py`. Make sure to install the Raspberry Pi Tools Addon to have access to the GPIO library.

## Electronic Circuit

The value of the base resistor will depend on your transistor characteristics, the ampere usage of your fan and if you run it on 3.3V or 5V.

![electronic circuit](circuit.png)
