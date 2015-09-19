
"""
PySerial backend based on:
https://github.com/python-ivi/python-ivi/blob/master/ivi/interface/pyserial.py

Copyright (c) 2012-2014 Alex Forencich
          (c) 2015      Philipp Klaus

License: MIT
"""

import time
import logging
import re

import universal_usbtmc

# PySerial:
try:
    import serial
except ImportError:
    raise universal_usbtmc.UsbtmcMissingDependency(['PySerial'])

logger = logging.getLogger(__name__)

def parse_visa_resource_string(resource_string):
    # valid resource strings:
    # ASRL1::INSTR
    # ASRL::COM1::INSTR
    # ASRL::COM1,9600::INSTR
    # ASRL::COM1,9600,8n1::INSTR
    # ASRL::/dev/ttyUSB0::INSTR
    # ASRL::/dev/ttyUSB0,9600::INSTR
    # ASRL::/dev/ttyUSB0,9600,8n1::INSTR
    m = re.match('^(?P<prefix>(?P<type>ASRL)\d*)(::(?P<arg1>[^\s:]+))?(::(?P<suffix>INSTR))$',
            resource_string, re.I)

    if m is not None:
        return dict(
                type = m.group('type').upper(),
                prefix = m.group('prefix'),
                arg1 = m.group('arg1'),
                suffix = m.group('suffix'),
        )

    """ A backend for PySerial
        https://github.com/alexforencich/python-usbtmc
    """

class Instrument(universal_usbtmc.Instrument):
    "Serial instrument interface client"
    def __init__(self, port = None, baudrate=9600, bytesize=8, paritymode=0, stopbits=1, timeout=None,
                xonxoff=False, rtscts=False, dsrdtr=False):

        if port.upper().startswith("ASRL") and '::' in port:
            res = parse_visa_resource_string(port)

            if res is None:
                raise IOError("Invalid resource string")

            index = res['prefix'][4:]
            if len(index) > 0:
                port = int(index)
            else:
                # port[,baud[,nps]]
                # n = data bits (5,6,7,8)
                # p = parity (n,o,e,m,s)
                # s = stop bits (1,1.5,2)
                t = res['arg1'].split(',')
                port = t[0]
                if len(t) > 1:
                    baudrate = int(t[1])

        self.serial = serial.Serial(port)

        self.term_char = '\n'

        self.port = port

        self.baudrate = baudrate
        self.bytesize = bytesize
        self.paritymode = paritymode
        self.stopbits = stopbits
        self.timeout = timeout
        self.xonxoff = xonxoff
        self.rtscts = rtscts
        self.dsrdtr = dsrdtr

        self.wait_dsr = False
        self.message_delay = 0

        self.update_settings()
    
    def update_settings(self):
        
        self.serial.baudrate = self.baudrate
        
        if self.bytesize == 5:
            self.serial.bytesize = serial.FIVEBITS
        elif self.bytesize == 6:
            self.serial.bytesize = serial.SIXBITS
        elif self.bytesize == 7:
            self.serial.bytesize = serial.SEVENBITS
        else:
            self.serial.bytesize = serial.EIGHTBITS
        
        if self.paritymode == 1:
            self.serial.paritymode = serial.PARITY_ODD
        elif self.paritymode == 2:
            self.serial.paritymode = serial.PARITY_EVEN
        elif self.paritymode == 3:
            self.serial.paritymode = serial.PARITY_MARK
        elif self.paritymode == 4:
            self.serial.paritymode = serial.PARITY_SPACE
        else:
            self.serial.paritymode = serial.PARITY_NONE
        
        if self.stopbits == 1.5:
            self.serial.stopbits = serial.STOPBITS_ONE_POINT_FIVE
        elif self.stopbits == 2:
            self.serial.stopbits = serial.STOPBITS_TWO
        else:
            self.serial.stopbits = serial.STOPBITS_ONE
        
        self.serial.timeout = self.timeout
        self.serial.xonxoff = self.xonxoff
        self.serial.rtscts = self.rtscts
        self.serial.dsrdtr = self.dsrdtr
        
        if self.dsrdtr:
            self.wait_dsr = True
            self.message_delay = 0.1
    
    def write_raw(self, data):
        "Write binary data to instrument"
        
        if self.term_char is not None:
            data += str(self.term_char).encode('utf-8')
        
        logger.debug('write_raw(' + repr(data) + ')')

        self.serial.write(data)
        
        if self.message_delay > 0:
            time.sleep(self.message_delay)
        
        if self.wait_dsr:
            while not self.serial.getDSR():
                time.sleep(0.01)
    
    def read_raw(self, num=-1, timeout=0.0):
        "Read binary data from instrument"
        
        data = b''
        term_char = str(self.term_char).encode('utf-8')
        
        while True:
            c = self.serial.read(1)
            if c == term_char:
                logger.debug('read_raw() read ' + repr(data + c))
                break
            data += c
            num -= 1
            if num == 0:
                logger.debug('read_raw() read ' + repr(data))
                break
            
        return data
