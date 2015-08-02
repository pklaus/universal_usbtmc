
class Instrument(object):

    "USBTMC instrument interface"

    #def __init__(self, *args, **kwargs):
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
    
    def ask_raw(self, data, num=-1):
        "Write then read binary data"
        self.write_raw(data)
        return self.read_raw(num)
    
    def write(self, message, encoding = 'utf-8'):
        "Write string to instrument"
        if type(message) is tuple or type(message) is list:
            # recursive call for a list of commands
            for message_i in message:
                self.write(message_i, encoding)
            return
        
        self.write_raw(str(message).encode(encoding))

    def read(self, num=-1, encoding = 'utf-8'):
        "Read string from instrument"
        return self.read_raw(num).decode(encoding).rstrip('\r\n')

    def ask(self, message, num=-1, encoding = 'utf-8'):
        "Write then read string"
        if type(message) is tuple or type(message) is list:
            # recursive call for a list of commands
            val = list()
            for message_i in message:
                val.append(self.ask(message_i, num, encoding))
            return val
        
        self.write(message, encoding)
        return self.read(num, encoding)

    def sendReset(self):
        self.write("*RST")

    def getIDN(self):
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

class PermissionError(UsbtmcError):
    pass

class NoSuchFileError(UsbtmcError):
    pass

class ReadTimeoutError(UsbtmcError, TimeoutError):
    pass


def list_devices():
    raise NotImplementedError()

