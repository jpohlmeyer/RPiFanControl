#!/usr/bin/env python3

import RPi.GPIO as GPIO
import signal
import time

class FanControl:

    quit = False

    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinNumber, GPIO.OUT)
        signal.signal(signal.SIGINT, self.exit)
        signal.signal(signal.SIGTERM, self.exit)

    def start(self):
        GPIO.output(self.pinNumber, GPIO.HIGH)

    def exit(self):
        GPIO.output(self.pinNumber, GPIO.LOW)

def main():
    fancontrol = FanControl(25)
    fancontrol.start()
    while not fancontrol.quit:
        time.sleep(1)

if __name__ == "__main__":
    main()