
### A Universal USBTMC Package for Python

`universal_usbtmc` is an effort to fix the clutter
of USBTMC implementations for Python.

This project provides a unified interface to the different ways/
implementations ("backends") to talk to USBTMC devices ("instruments").
This allows you to write very platform independent code.

It also comes with an interactive USBTMC shell.

You can use the following instrument implementations
("backends") in your software:

* USBTMC via the Linux kernel module
* USBTMC via [python-usbtmc][] (uses libusb)
* TCP Socket via [socket][] (remote connection e.g. via [rpi-usbtmc-gateway][])
* VXI-11 via [python-vxi11][] (an RPC-based TCP connection, not really usbtmc)
* RS-232 via [PySerial][]

As already mentioned, you'll automatically gain a large deal
of platform independence as any operating system will support
at least some of those backends.

### Installation

    pip install universal_usbtmc

### Usage

This software is mainly made to be used by other software, not humans.  
It comes, however, with a small command line tool called `usbtmc-shell`.
You can use it to test if the different backends work for you.
(Or for trying to talk to a new device you just bought.)
See below in the backends sections on how to use it with different backends.

### Backends

To communicate with your device, the following backends are available:

* `linux_kernel`
* `python_usbtmc`
* `tcp_socket`
* `python_vxi11`
* `pyserial`

### Backend Details

#### `linux_kernel`

Uses the Linux Kernel Module *usbtmc*  
The source code of the kernel module can be found [here][usbtmc.c].

To use this backend, you must be using a Linux kernel
and have the kernel module compiled and loaded.
Look for the device `/dev/usbtmc0` to check
your USBTMC device is detected.

You can run the usbtmc shell to check if everything works OK:

    usbtmc-shell --backend linux_kernel /dev/usbtmc0

#### `python_usbtmc`

Uses the libusb-/PyUSB-based [python-usbtmc][].

Here's how to use the usbtmc shell with it:

    usbtmc-shell --backend python_usbtmc USB::0x1ab1::0x0588::INSTR

To use the backend `python_usbtmc`, you need to install the requirements [python-usbtmc][] and [PyUSB][]:

    pip install python-usbtmc pyusb

The backend works on Mac OS X and Linux.

#### `tcp_socket`

This backend connects to your instrument via TCP sockets.
How is this possible if the instrument itself doesn't have an Ethernet port?
You can put it on the net with [rpi-usbtmc-gateway][]!

To connect using the *tcp_socket* backend, run:

    usbtmc-shell --backend tcp_socket 192.168.0.21
    # or
    usbtmc-shell --backend tcp_socket TCPIP::192.168.0.21::5025::SOCKET

This backend has no external dependencies and works on all operating systems.

#### `python_vxi11`

This backend connects to your instrument via VXI-11.
This is not USBTMC in a way but the interface with SCPI commands is usually the same.

Uses the Python library [python-vxi11][].

To connect using the *python_vxi11* backend, run:

    usbtmc-shell --backend python_vxi11 192.168.0.21
    # or
    usbtmc-shell --backend python_vxi11 TCPIP::192.168.0.21::INSTR

To use this backend, install python-vxi:

    pip install python-vxi11

The backend should work on all operating systems.

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
[PyUSB]: https://github.com/walac/pyusb
[python-vxi11]: https://github.com/python-ivi/python-vxi11
[socket]: https://docs.python.org/3/library/socket.html
[rpi-usbtmc-gateway]: https://github.com/pklaus/rpi-usbtmc-gateway
