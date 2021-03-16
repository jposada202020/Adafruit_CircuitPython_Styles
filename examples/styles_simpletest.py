# SPDX-FileCopyrightText: 2020 Jose David Montoya
# SPDX-License-Identifier: Unlicense

"""
This example shows the use of library with an adafruit_display_text.label object
"""

import board
import terminalio
from adafruit_display_text import label

text = "Hello world"
text_area = label.Label(terminalio.FONT, text=text)
text_area.x = 10
text_area.y = 10
text_area.label_style = "LightGreen8"
board.DISPLAY.show(text_area)
while True:
    pass
