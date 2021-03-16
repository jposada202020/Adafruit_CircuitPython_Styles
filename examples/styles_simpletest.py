# SPDX-FileCopyrightText: 2020 Jose David Montoya
# SPDX-License-Identifier: Unlicense

"""
This example shows the use of library with a adafruit_display_text.label object
"""

import board
import displayio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font


display = board.DISPLAY
main_group = displayio.Group()

# Font definition. You can choose any two fonts available in your system
FONT = bitmap_font.load_font("LeagueSpartan-Bold-16.bdf")

# Define our text to display
TEXT = "HELLO"

# Create a simple label
left_text = label.Label(
    FONT,
    text=TEXT,
    x=10,
    y=50,
)
main_group.append(left_text)

# Create a style label
right_text = label.Label(FONT, text=TEXT, x=90, y=50, label_style="LightGreen8")
main_group.append(right_text)
display.show(main_group)

while True:
    pass
