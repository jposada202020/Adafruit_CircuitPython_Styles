# SPDX-FileCopyrightText: Jose David Montoya
#
# SPDX-License-Identifier: MIT

"""
`adafruit_styles`
=======================
"""


def apply_style(target, style):
    """
    :param target: widget object
    :param style: Style to apply


    apply_style could be used in certain libraries that provide access to the color setter.


    **Quickstart: Importing and using apply_style**

    Here is one war of importing ``apply_style`` function so you can use it as
    the name ``colors`` and the color set ``DarkAmber``:

    .. code-block:: python

        from Adafruit_CircuitPython_Styles import apply_style
        from Adafruit_CircuitPython_Styles.styles import DarkAmber

    For a created Label object in ``adafruit_display_text``

    .. code-block:: python

        text_area = bitmap_label.Label(terminalio.FONT, text="Hello", x=10, y=10)

    you can apply the style library using:

     .. code-block:: python

        apply_style(text_area, DarkAmber)

    The function will verify the object and apply the changes according to the features available

    """
    text_display = ["Label", "Bitmap_label"]
    annotation_widget = ["Annotation"]

    identifier = target.__class__.__name__
    # print(identifier)

    if identifier in text_display:
        target.color = style["TEXT"]
        target.background_color = style["BACKGROUND"]
    elif identifier in annotation_widget:
        target.text_color = style["TEXT"]
