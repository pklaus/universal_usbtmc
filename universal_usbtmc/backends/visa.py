import pyvisa
from .. import Instrument as IInstrument
rm = pyvisa.ResourceManager()

class Instrument(IInstrument):
    #__slots__ = ("device",) # shit
    def __init__(self, device=None, *args, **kwargs):
        self.__dict__["device"] = None
        if device is None:
            device = 0
        if isinstance(device, int):
            device = rm.list_resources()[device]
        if isinstance(device, str):
            device = rm.open_resource(device, timeout=10000, *args, **kwargs)
        self.__dict__["device"] = device
        self.device.enable_event(pyvisa.constants.VI_EVENT_SERVICE_REQ, pyvisa.constants.VI_QUEUE, context=None)

    def __getattr__(self, k):
        #print("__getattr__", k)
        return getattr(self.__dict__["device"], k)
    
    def __setattr__(self, k, v):
        #print("__setattr__", k, v)
        return setattr(self.__dict__["device"], k, v)
    
    def __hasattr__(self, k):
        return hasattr(self.__dict__["device"], k, v)

    def write_raw(self, data):
        #print("write_raw", data)
        return self.__dict__["device"].write_raw(data)

    def read_raw(self, num=-1, timeout=0.0):
        return self.__dict__["device"].read_raw(num=num)
    
    def write(self, message, encoding='default', line_ending='default'):
        #print("write", message)
        self.__dict__["device"].write(message)

    def read(self, num=-1, encoding='default', line_ending='default'):
        return self.device.read(num=num)

    def query_raw(self, message, encoding='default', num=-1):
        #print("query_raw", message)
        return bytes(self.device.query_binary_values(message, datatype="B", header_fmt="empty"))

    def query(self, message, num=-1, encoding='default', line_ending='default'):
        #print("query", message)
        return self.device.query(message)

    def assert_trigger(self):
        self.device.assert_trigger()
    
    def wait_on_event(self, event=pyvisa.constants.VI_EVENT_SERVICE_REQ):
        self.device.wait_on_event(event, self.device.timeout)