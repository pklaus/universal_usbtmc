
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
    timeout = .02

    def __init__(self, host, port=5025):
        self.host = host
        self.port = port
        self.connect()

    def connect(self):
        try:
            self.s = socket.create_connection((self.host, self.port), self.timeout)
        except (ConnectionRefusedError, socket.gaierror) as e:
            raise UsbtmcError("Connection to host {} could not be established: {}".format(self.host, e))

    #def write(self, cmd, encoding='default'):
    #    encoding = self.ENCODING if encoding == 'default' else encoding
    #    self.write_raw((cmd + self.EOL).encode(encoding))

    def write_raw(self, cmd):
        logger.debug('write_raw(' + str(cmd) + ')')
        self.s.sendall(cmd)
        time.sleep(0.05)

    def read_raw(self, wait_long=0.):
        ret = b""
        start = clock()
        while True:
            try:
                ret += self.s.recv(1024*1024+1024)
            except socket.timeout:
                if not wait_long: break
                else:
                    if clock() - start > wait_long: break
                    if len(ret): break
        if not len(ret): raise UsbtmcReadTimeoutError()
        logger.debug('read_raw() returns ' + str(ret))
        return ret

