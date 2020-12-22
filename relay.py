#!/usr/bin/env python
"""
Info: tesing how a relay functions in gpiozore
"""


import time
import gpiozero
from gpiozero import Button


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


button1 = Button(18)
relay_pin1 = 23
relay_pin2 = 24
relay1 = gpiozero.OutputDevice(relay_pin1, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(relay_pin2, active_high=False, initial_value=False)


toggle_on = False


def toggle_relay():
    global toggle_on

    if toggle_on:
        print("Setting relay ON")
        relay1.on()
        relay2.on()

    else:
        print("Setting relay OFF")
        relay1.off()
        relay2.off()

try:
    button1.when_pressed = toggle_relay()
finally:
    pass

if __name__ == "__main__":
    ()