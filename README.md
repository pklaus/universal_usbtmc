
### USBTMC for Python

This is an effort to fix the clutter
of USBTMC implementations for Python.

This project provides a unified interface
to the many USBTMC classes for Python.

It also comes with an interactive USBTMC shell.

### Backends

#### Linux Kernel Module

The [usbtmc linux kernel module][usbtmc.c] is supported
by the backend named `linux_kernel`.

#### python-usbtmc

You need to install the requirements python-usbtmc and pyusb:

    pip install https://github.com/alexforencich/python-usbtmc/archive/master.zip
    pip install https://github.com/walac/pyusb/archive/master.zip

[usbtmc.c]: https://github.com/torvalds/linux/blob/master/drivers/usb/class/usbtmc.c
