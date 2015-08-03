
class Instrument(object):

    "USBTMC instrument interface"

    ENCODING = 'utf-8'

    def __init__(self, device):
        raise NotImplementedError()
    
    def reset(self):
        raise NotImplementedError()
    
    def write_raw(self, data):
        "Write binary data to instrument"
        raise NotImplementedError()

    def read_raw(self, num=-1):
        "Read binary data from instrument"
        raise NotImplementedError()
    
    def query_raw(self, data, num=-1):
        "Write then read binary data"
        self.write_raw(data)
        return self.read_raw(num)
    
    def write(self, message, encoding='default'):
        "Write string to instrument"
        encoding = self.ENCODING if encoding == 'default' else encoding
        if type(message) is tuple or type(message) is list:
            # recursive call for a list of commands
            for message_i in message:
                self.write(message_i, encoding)
            return
        
        self.write_raw(str(message).encode(encoding))

    def read(self, num=-1, encoding='default'):
        encoding = self.ENCODING if encoding == 'default' else encoding
        "Read string from instrument"
        return self.read_raw(num).decode(encoding).rstrip('\r\n')

    def query(self, message, num=-1, encoding='default'):
        encoding = self.ENCODING if encoding == 'default' else encoding
        "Write then read string"
        if type(message) is tuple or type(message) is list:
            # recursive call for a list of commands
            val = list()
            for message_i in message:
                val.append(self.query(message_i, num=num, encoding=encoding))
            return val
        
        self.write(message, encoding=encoding)
        return self.read(num, encoding=encoding)

    def sendReset(self):
        self.write("*RST")

    @property
    def idn(self):
        self.write("*IDN?")
        return self.read(300)
 
    def remote(self):
        "Send remote command"
        raise NotImplementedError()
    
    def local(self):
        "Send local command"
        raise NotImplementedError()


class UsbtmcError(Exception):
    pass

class UsbtmcPermissionError(UsbtmcError):
    pass

class UsbtmcNoSuchFileError(UsbtmcError):
    pass

try:
    TimeoutError
except NameError:
    class TimeoutError(OSError):
        pass

class UsbtmcReadTimeoutError(UsbtmcError, TimeoutError):
    pass


def list_devices():
    raise NotImplementedError()

