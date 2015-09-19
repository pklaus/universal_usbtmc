
import importlib

import universal_usbtmc.backends
from universal_usbtmc.exceptions import *

def import_backend(name):
    try:
        return importlib.import_module('universal_usbtmc.backends.' + name)
    except ImportError:
        raise UsbtmcNoSuchBackend(name)

