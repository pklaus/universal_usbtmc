
class usbtmc_backend(object):

    def __init__(self, device):
        raise NotImplementedError()

    def _write(self, command):
        raise NotImplementedError()

    def _read(self):
        raise NotImplementedError()

    def read_raw(self):
        raise NotImplementedError()

    def ask(self, cmd):
        self.write(cmd)
        return self.read()

    def ask_raw(self):
        raise NotImplementedError()



class UsbtmcError(Exception):
    pass

class PermissionError(UsbtmcError):
    pass

class NoSuchFileError(UsbtmcError):
    pass

