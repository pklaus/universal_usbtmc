
import importlib

import universal_usbtmc.backends
from universal_usbtmc import UsbtmcError

class UsbtmcNoSuchBackendError(UsbtmcError):
    pass

def import_backend(name):
     return importlib.import_module('universal_usbtmc.backends.' + name)

