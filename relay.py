#!/usr/bin/env python
"""
Info: tesing how a relay functions in gpiozore
"""


from signal import pause
from time import sleep
from gpiozero import Button, OutputDevice


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


button1_pin = 18
relay1_pin = 23

button1 = Button(button1_pin)
relay1 = OutputDevice(relay1_pin)

def ButtonPressedCallback():
    relay1.on()
    sleep(0.5)
    relay1.off()

button1.when_pressed = ButtonPressedCallback

pause()

if __name__ == "__main__":
    ()