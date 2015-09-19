def list_devices():
    raise NotImplementedError()

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

    def read_raw(self, num=-1, timeout=0.0):
        "Read binary data from instrument"
        raise NotImplementedError()
    
    def query_raw(self, message, encoding='default', num=-1):
        "Write with normal write() then ruturn binary data from read_raw()"
        self.write(message)
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
        return self.query("*IDN?", 300)
 
    def remote(self):
        "Send remote command"
        raise NotImplementedError()
    
    def local(self):
        "Send local command"
        raise NotImplementedError()

