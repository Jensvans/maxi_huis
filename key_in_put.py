#!/usr/bin/env python
"""
Info: testing key input in python
"""

from pynput.keyboard import Controller
import time


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


keyboard = Controller

time.sleep(2)
keyboard.press('a')
keyboard.release('a')