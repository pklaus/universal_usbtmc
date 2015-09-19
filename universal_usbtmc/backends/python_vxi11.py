
import logging

import universal_usbtmc

# python-vxi11 from https://github.com/python-ivi/python-vxi11
try:
    import vxi11
except ImportError:
    raise universal_usbtmc.UsbtmcMissingDependency(['python-vxi11'])

logger = logging.getLogger(__name__)

class Instrument(universal_usbtmc.Instrument):
    """ A backend for python-vxi11 """

    def __init__(self, device):
        self.instr = vxi11.Instrument(device)

    def read_raw(self, num, timeout=0.0):
        ret = self.instr.read_raw(num)
        logger.debug('read_raw() read ' + repr(ret))
        return ret

    def write_raw(self, data):
        logger.debug('write_raw(' + repr(data) + ')')
        self.instr.write_raw(data)
