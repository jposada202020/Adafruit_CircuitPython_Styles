# SPDX-FileCopyrightText: Jose David Montoya
#
# SPDX-License-Identifier: MIT

"""
`adafruit_syles`
=======================
"""


def get_hex(color: str) -> int:
    """get_hex function
    A helper to convert Color styles to HEX

    :param str color: string representation of Hex color
    :return: color
    :rtype: int

    """
    return int(color[1:], 16)
