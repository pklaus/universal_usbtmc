
import usbtmc
from universal_usbtmc import Instrument

class Backend(Instrument):
    """ A backend for python-usbtmc
        https://github.com/alexforencich/python-usbtmc
    """

    def __init__(self, device):
        self.instr = usbtmc.Instrument(device)

    def read_raw(self, num):
        self.instr.read_raw(num)

    def write_raw(self, cmd):
        return self.instr.write_raw(cmd)


