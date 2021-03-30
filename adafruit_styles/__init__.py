# SPDX-FileCopyrightText: Jose David Montoya
#
# SPDX-License-Identifier: MIT

"""
`adafruit_syles`
=======================
"""


def apply_style(target, style):
    """
    target: widget object
    style: Style to apply
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
