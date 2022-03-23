#! /bin/bash

version=$(grep -Po "(?<=name=\"RPiFanControl\" version=\")[0-9\.]*" addon.xml)
mkdir service.rpifancontrol
cp addon.xml service.rpifancontrol
cp addon.py service.rpifancontrol
cp fancontrol.py service.rpifancontrol
cp LICENSE service.rpifancontrol
filename="service.rpifancontrol-${version}.zip"
zip -r $filename service.rpifancontrol
rm -rf service.rpifancontrol