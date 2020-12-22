#!/usr/bin/env python
"""
Info 1 druknop die 2 led's bediend
"""

from signal import pause
from time import sleep
from gpiozero import LED, Button


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


led1 = LED(17)
led2 = LED(22)
button1 = Button(18)


blink_on = False

def go_blink():
    global blink_on

    if blink_on:
        led1.off()
        led2.off()
    else:
        led1.blink(0.5, 0.5)
        sleep(0.5)
        led2.blink(0.5, 0.5)

    blink_on = not blink_on

try:
    button1.when_pressed = go_blink
    button1.when_pressed = print("button1 pressed")
    pause()
finally:
    pass

if __name__== '__main__':
    ()