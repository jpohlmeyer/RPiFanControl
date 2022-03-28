#! /bin/bash

# parse version number from addon.xml
version=$(grep -Po "(?<=name=\"RPiFanControl\" version=\")[0-9\.]*" addon.xml)

# copy addon files to a directory to be put in the zip
mkdir service.rpifancontrol
cp addon.xml service.rpifancontrol
cp addon.py service.rpifancontrol
cp fancontrol.py service.rpifancontrol
cp disable_addon.py service.rpifancontrol
cp LICENSE service.rpifancontrol
cp -r resources service.rpifancontrol

# zip directory
filename="service.rpifancontrol-${version}.zip"
zip -r $filename service.rpifancontrol

# remove temporary directory again
rm -rf service.rpifancontrol