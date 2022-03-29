#!/usr/bin/env python3

import RPi.GPIO as GPIO
import threading
import time

class SettingsProviderInterface:

    def get_gpio_pin(self):
        raise NotImplementedError

    def get_temperature_threshold(self):
        raise NotImplementedError
    
    def get_min_cooling_duration(self):
        raise NotImplementedError

class FanControl:

    quit = False
    is_fan_on = False

    def __init__(self, settings_provider):
        self.settings_provider = settings_provider
        self.temp_control_thread = threading.Thread(target=self.temp_control)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.settings_provider.get_gpio_pin(), GPIO.OUT)

    def temp_control(self):
        while not self.quit:
            with open("/sys/class/thermal/thermal_zone0/temp") as temp_file:
                temp = int(temp_file.read())
            if temp and temp > self.settings_provider.get_temperature_threshold():
                if not self.is_fan_on:
                    self.fan_on()
                counter = 0
                while not self.quit and counter < self.settings_provider.get_min_cooling_duration():
                    counter += 1
                    time.sleep(1)
            else:
                self.fan_off()
            time.sleep(1)

    def start(self):
        self.temp_control_thread.start()

    def fan_on(self):
        is_fan_on = True
        GPIO.output(self.settings_provider.get_gpio_pin(), GPIO.HIGH)
    
    def fan_off(self):
        is_fan_on = False
        GPIO.output(self.settings_provider.get_gpio_pin(), GPIO.LOW)

    def exit(self):
        self.quit = True
        if self.temp_control_thread.is_alive():
            self.temp_control_thread.join()
        self.fan_off()
