#!/usr/bin/env python

import RPi.GPIO as GPIO

class FanControl:

    quit = False

    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinNumber, GPIO.OUT)

    def start(self):
        GPIO.output(self.pinNumber, GPIO.HIGH)

    def exit(self):
        self.quit = True
        GPIO.output(self.pinNumber, GPIO.LOW)
