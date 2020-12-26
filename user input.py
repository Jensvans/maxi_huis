#!/usr/bin/env python
"""
Info test the user input
"""


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"

resp = input()
if "yes" in resp:
    print('whatever the yes answer is')
resp2 = input()
if "no" in resp2:
    print('whatever the no answer is')