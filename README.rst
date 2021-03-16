Introduction
============


.. image:: https://readthedocs.org/projects/adafruit-circuitpython-styles/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/styles/en/latest/
    :alt: Documentation Status


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/adafruit/Adafruit_CircuitPython_Styles/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_Styles/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython helper library for styles and colorsets applied to visual widgets


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

.. This library helps you coonfigure your display widgets with an beautiful color style.

`Purchase one from the Adafruit shop <http://www.adafruit.com/products/>`_


Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-styles/>`_.
To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-styles

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-styles

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-styles


Usage Example
=============

For a board with a built-in display.

.. code:: python

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


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_Styles/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
