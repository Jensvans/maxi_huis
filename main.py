#!/usr/bin/env python
"""
Info: tesing how a relay functions in gpiozore
"""


from signal import pause
from guizero import App, PushButton
from gpiozero import OutputDevice
import sys


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


relay1_pin = 17
relay2_pin = 22


relay1 = OutputDevice(relay1_pin)
relay2 = OutputDevice(relay2_pin)


def exitApp():
    sys.exit()


def toggle_relay1():
    relay1.toggle()
    if relay1.is_lit:
        relay1Button.text = "RELAY OFF"
    else:
        relay1Button.text = "RELAY ON"


def toggle_relay2():
    relay2.toggle()
    if relay2.is_lit:
        relay2Button.text = "RELAY OFF"
    else:
        relay2Button.text = "RELAY ON"


app = App('First Gui', height=600, width=800)

relay1Button = PushButton(app, toggle_relay1, text="RELAY ON", width=15, height=3)
relay1Button.text_size = 36

relay2Button = PushButton(app, toggle_relay1, text="RELAY ON", width=15, height=3)
relay2Button.text_size = 36

exitButton = PushButton(app, exitApp, text="Exit", align="bottom", width=15, height=3)
exitButton.text_size = 36

app.display()


pause()

if __name__ == "__main__":
    ()