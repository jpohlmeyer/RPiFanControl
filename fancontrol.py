#!/usr/bin/env python

import RPi.GPIO as GPIO
import threading
import time

class FanControl:

    quit = False
    is_fan_on = False

    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        self.temp_control_thread = threading.Thread(target=self.temp_control)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinNumber, GPIO.OUT)

    def temp_control(self):
        while not self.quit:
            with open("/sys/class/thermal/thermal_zone0/temp") as temp_file:
                temp = int(temp_file.read())
            if temp and temp > 65000:
                if not self.is_fan_on:
                    self.fan_on()
                counter = 0
                while not self.quit and counter < 300:
                    counter += 1
                    time.sleep(1)
            else:
                self.fan_off()
            time.sleep(1)

    def start(self):
        self.temp_control_thread.start()

    def fan_on(self):
        is_fan_on = True
        GPIO.output(self.pinNumber, GPIO.HIGH)
    
    def fan_off(self):
        is_fan_on = False
        GPIO.output(self.pinNumber, GPIO.LOW)

    def exit(self):
        self.quit = True
        if self.temp_control_thread.is_alive():
            self.temp_control_thread.join()
        self.fan_off()
