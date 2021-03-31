# SPDX-FileCopyrightText: 2021 Jose David M.
#
# SPDX-License-Identifier: MIT

"""
Display Text style definitions. Based on the PySimpleGui styles used under the LGPL3+ license.
"""
# pylint: disable=invalid-name, too-few-public-methods


class GetStyle:
    """
    GetStyle allow any library to use the colorset available.

    **Quickstart: Importing and using GetStyle**

    Here is one war of importing ``GetStyle`` class so you can use it as
    the name ``colors`` and the color set ``BluePurple``:

    .. code-block:: python

        from adafruit_styles.style import GetStyle, BluePurple

    Now you can create a color set using:

    .. code-block:: python

        colors = GetStyle('BluePurple')

    all the four color attributes will be available in colors. This could be easily
    accessed via:

     .. code-block:: python

        colors.text_color

    Currently there are four attributes ``background_color``, ``text_color``, ``line_color`` and
    ``border``

    """

    def __init__(self, color):
        self.background = color["BACKGROUND"]
        self.text_color = color["TEXT"]
        self.border = color["BORDER"]
        self.line_color = color["LINE_COLOR"]


DarkAmber = {
    "BACKGROUND": 0x2C2825,
    "TEXT": 0xFDCB52,
    "BORDER": 0x705E52,
    "LINE_COLOR": 0xFDCB52,
}

DarkBlue = {
    "BACKGROUND": 0x1A2835,
    "TEXT": 0xD1ECFF,
    "BORDER": 0x335267,
    "LINE_COLOR": 0xACC2D0,
}

Reds = {
    "BACKGROUND": 0x280001,
    "TEXT": 0xFFFFFF,
    "BORDER": 0xD8D584,
    "LINE_COLOR": 0x763E00,
}

Green = {
    "BACKGROUND": 0x82A459,
    "TEXT": 0x000000,
    "BORDER": 0xD8D584,
    "LINE_COLOR": 0xE3ECF3,
}

BluePurple = {
    "BACKGROUND": 0xA5CADD,
    "TEXT": 0x6E266E,
    "BORDER": 0xE0F5FF,
    "LINE_COLOR": 0xE0F5FF,
}

Purple = {
    "BACKGROUND": 0xB0AAC2,
    "TEXT": 0x000000,
    "BORDER": 0xF2EFE8,
    "LINE_COLOR": 0xF2EFE8,
}

BlueMono = {
    "BACKGROUND": 0xAAB6D3,
    "TEXT": 0x000000,
    "BORDER": 0xF1F4FC,
    "LINE_COLOR": 0xF1F4FC,
}

GreenMono = {
    "BACKGROUND": 0xA8C1B4,
    "TEXT": 0x000000,
    "BORDER": 0xDDE0DE,
    "LINE_COLOR": 0xE3E3E3,
}

BrownBlue = {
    "BACKGROUND": 0x64778D,
    "TEXT": 0xFFFFFF,
    "BORDER": 0xF0F3F7,
    "LINE_COLOR": 0xA6B2BE,
}

BrightColors = {
    "BACKGROUND": 0xB4FFB4,
    "TEXT": 0x000000,
    "BORDER": 0xFFFF64,
    "LINE_COLOR": 0xFFB482,
}
