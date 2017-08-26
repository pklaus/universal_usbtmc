
import logging

import universal_usbtmc

# PyUSB         from https://github.com/walac/pyusb
# python-usbtmc from https://github.com/python-ivi/python-usbtmc
try:
    import usb.core
    import usbtmc
except ImportError:
    raise universal_usbtmc.UsbtmcMissingDependency(['pyusb', 'python-usbtmc'])

logger = logging.getLogger(__name__)

class Instrument(universal_usbtmc.Instrument):
    """ A backend for python-usbtmc
        https://github.com/alexforencich/python-usbtmc
    """

    def __init__(self, device):
        self.instr = usbtmc.Instrument(device)

    def read_raw(self, num, timeout=0.0):
        ret = self.instr.read_raw(num)
        logger.debug('read_raw() read ' + repr(ret))
        return ret

    def write_raw(self, data):
        logger.debug('write_raw(' + repr(data) + ')')
        self.instr.write_raw(data)
