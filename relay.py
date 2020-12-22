#!/usr/bin/env python
"""
Info: tesing how a relay functions in gpiozore
"""

from signal import pause
from time import sleep
from gpiozero import LED, Button, OutputDevice


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


import sys
import time
import gpiozero

relay = gpiozero.OutputDevice(23, active_high=False, initial_value=False)

def set_relay(status):
    if status:
        print("Setting relay: ON")
        relay.on()
    else:
        print("Setting relay: OFF")
        relay.off()

def toggle_relay():
    print("toggling relay")
    relay.toggle()

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
        sys.exit(0)