
### A Universal USBTMC Package for Python

This is an effort to fix the clutter
of USBTMC implementations for Python.

This project provides a unified interface to
the different ways and implementations to talk
to USBTMC instruments.

It also comes with an interactive USBTMC shell.

You can use the following instrument implementations
("backends") in your software:

* USBTMC (via Linux kernel module or Python/libusb)
* TCP Socket (remote connection e.g. via [rpi-usbtmc-gateway][])
* RS232

You'll automatically gain a large deal of platform independence.

### Installation

    pip install https://github.com/pklaus/universal_usbtmc/archive/master.zip

### Usage

This software is mainly made to be used by other software, not humans.
It comes, however, with a small command line tool called `usbtmc-shell`.
You can use it to test if the different backends work for you.  
See below in the backends sections on how to use it with different backends.

### Backends

To communicate with your device, the following backends are available:

* `pyserial`
* `python_usbtmc`
* `linux_kernel`
* `tcp_socket`

### Backend Details

#### `linux_kernel`

Uses the Linux Kernel Module *usbtmc*  
The source code of the kernel module can be found [here][usbtmc.c].

To use this backend, you must be using a Linux kernel
and have the kernel module compiled and loaded.
Check for `/dev/usbtmc0` (and counting) devices to check
if your USBTMC device is detected.

You can check if everything works with:

    usbtmc-shell --backend linux_kernel /dev/usbtmc0

#### `python_usbtmc`

Uses the libusb-/PyUSB-based [python-usbtmc][].

To use the backend `python_usbtmc`, you need to install the requirements python-usbtmc and pyusb:

    pip install https://github.com/alexforencich/python-usbtmc/archive/master.zip
    pip install https://github.com/walac/pyusb/archive/master.zip

Here's how to use it:

    usbtmc-shell --backend python_usbtmc USB::0x1ab1::0x0588::INSTR

The backend works on Mac OS X and Linux.

#### `tcp_socket`

This backend connects to your instrument via TCP sockets.
How is this possible if the instrument itself doesn't have an Ethernet port?
You can put it on the net with [rpi-usbtmc-gateway][]!

To connect using the *tcp_socket* backend, run:

    usbtmc-shell --backend tcp_socket 192.168.0.21

This backend has no external dependencies and works on all operating systems.

#### `pyserial`

This backend uses [PySerial][] to connect to your device via RS232.
On some devices, this is more stable than the USBTMC connection.

    usbtmc-shell --backend pyserial ASRL::/dev/ttyUSB0,9600::INSTR

Off course, you need to install [PySerial][] first! The backend works on all operating systems.

### Resources

* A project with a similar aim is [python-ivi](https://github.com/python-ivi/python-ivi)

[usbtmc.c]: https://github.com/torvalds/linux/blob/master/drivers/usb/class/usbtmc.c
[PySerial]: http://pyserial.sourceforge.net/
[python-usbtmc]: https://github.com/python-ivi/python-usbtmc

