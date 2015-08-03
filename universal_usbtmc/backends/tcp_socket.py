
"""
http://www.eevblog.com/forum/testgear/rigol-ds1074z-times-out-with-linux-usbtmc-drivers-and-python-scripts/
"""

import select
import socket
import time
import logging

import universal_usbtmc
from universal_usbtmc import UsbtmcError, UsbtmcPermissionError, UsbtmcNoSuchFileError, UsbtmcReadTimeoutError

logger = logging.getLogger(__name__)

try:
    clock = time.perf_counter
except:
    clock = time.time

logger = logging.getLogger(__name__)


class Instrument(universal_usbtmc.Instrument):
    """
    Networked usbmtc device
    """

    EOL = ''
    #EOL = '\n'
    socket_timeout = .05
    min_wait = 0.1

    def __init__(self, host, port=5025):
        self.host = host
        self.port = port
        self.connect()

    def connect(self):
        try:
            self.s = socket.create_connection((self.host, self.port), self.socket_timeout)
        except (ConnectionRefusedError, socket.gaierror) as e:
            raise UsbtmcError("Connection to host {} could not be established: {}".format(self.host, e))

    def write_raw(self, cmd):
        logger.debug('write_raw(' + str(cmd) + ')')
        self.s.sendall(cmd)
        time.sleep(0.05)

    def read_raw(self, length=1024*1024+1024, wait_long=0.0):
        ret = b""
        start = clock()
        wait = max(self.min_wait, wait_long)
        while True:
            try:
                ret += self.s.recv(length)
            except socket.timeout:
                if (clock() - start) > wait: break
                if len(ret): break
        if not len(ret): raise UsbtmcReadTimeoutError()
        logger.debug('read_raw() returns ' + str(ret))
        return ret

