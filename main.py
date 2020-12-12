#!/usr/bin/env python
"""
Info
"""


from gpiozero import LED, Button


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


led1 = LED(17)
led2 = LED(22)
button = Button(18)

def toggle_led():
    if button.is_pressed():
        led1.toggle()

if __name__== '__main__':
    toggle_led()