# pyOscilloskop
# -*- encoding: UTF8 -*-
#
# Copyright (19.2.2011) Sascha Brinkmann
#           (2012) Philipp Klaus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import errno
from usbtmc import Instrument
from usbtmc import UsbtmcError, PermissionError, NoSuchFileError

class Backend(Instrument):
    """ The Linux Kernel Backend """

    length = 4000

    def __init__(self, device):
        self.device = device
        try:
            self.FILE = os.open(device, os.O_RDWR)
        except OSError as e:
            if e.errno == errno.EACCES: raise PermissionError()
            if e.errno == errno.ENOENT: raise NoSuchFileError()
            raise UsbtmcError("unknown error: could not open the file %s: %s" % (device, e))
 
        # TODO: Test that the file opened

    def write_raw(self, command):
        os.write(self.FILE, command)
 
    def read_raw(self, num):
        return os.read(self.FILE, self.length)

    def __del__(self):
        try: os.close(self.FILE)
        except: pass

def getDeviceList():
    dirList=os.listdir("/dev")
    result=list()

    for fname in dirList:
        if(fname.startswith("usbtmc")):
            result.append("/dev/" + fname)

    return result
