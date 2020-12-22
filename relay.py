#!/usr/bin/env python
"""
Info: tesing how a relay functions in gpiozore
"""


import time
import gpiozero


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"

relay_pin1 = 23
relay_pin2 = 24
relay1 = gpiozero.OutputDevice(relay_pin1, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(relay_pin2, active_high=False, initial_value=False)

def set_relay(status):
    if status:
        print("Setting relay: ON")
        relay1.on()
        relay2.on()
    else:
        print("Setting relay: OFF")
        relay1.off()
        relay2.off()

def toggle_relay():
    print("toggling relay")
    relay1.toggle()
    relay2.toggle()

def main_loop():
    while 1:
        # then toggle the relay every second until the app closes
        toggle_relay()
        # wait a second
        time.sleep(1)

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        # turn the relay off
        set_relay(False)
        print("\nExiting application\n")
        # exit the application
