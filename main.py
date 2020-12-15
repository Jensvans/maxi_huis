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

