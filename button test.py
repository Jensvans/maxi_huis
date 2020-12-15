#!/usr/bin/env python
"""
Info 1 druknop die 2 led's bediend
"""


from gpiozero import LED, Button


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


led1 = LED(17)
led2 = LED(22)
button1 = Button(18)

try:
    led1.source = button1.value
  #  pause()
finally:
    pass

if __name__== '__main__':
    ()