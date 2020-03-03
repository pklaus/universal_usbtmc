
"""
The base class universal_usbtmc.Instrument
==========================================

The universal_usbtmc backends all derive from
:py:obj:`universal_usbtmc.Instrument` and thus
inherit or reimplement its methods.

Thus, you can read the reference for this class to
find out how to use the backends:

"""

def list_devices():
    raise NotImplementedError()

class Instrument():

    """
    USBTMC instrument interface

    The backends get initialized with a single device
    string to set up the connection.

    :param str device: The device to connect to
    """

    #: The encoding used when interpreting bytes as strings
    ENCODING = 'utf-8'
    #: The line ending to add to write() or query() commands
    LINE_ENDING = ''

    def __init__(self, device):
        """
        The backends need to override this constructor.
        """
        raise NotImplementedError()

    def write_raw(self, data):
        """
        Send binary data to the instrument

        The backends need to implement this method!

        :param bytes data: The data to send to the instrument
        """
        raise NotImplementedError()

    def read_raw(self, num=-1, timeout=0.0):
        """
        Read binary data from the instrument

        The backends need to implement this method!

        :param bytes num: Number of bytes to read back
        :param float timeout: Seconds until the read operation should time out
        """
        raise NotImplementedError()

    def write(self, message, encoding='default', line_ending='default'):
        """
        Send a string message to the instrument

        :param str message: The message to send
        :param str encoding: The encoding to use when converting the message from str to bytes
        :param str line_ending: The line ending to add to the message
        """
        encoding = self.ENCODING if encoding == 'default' else encoding
        line_ending = self.LINE_ENDING if line_ending == 'default' else line_ending
        if type(message) in (tuple, list):
            # recursive call for a list of commands
            for message_i in message:
                self.write(message_i, encoding)
            return
        self.write_raw((str(message)+line_ending).encode(encoding))

    def read(self, num=-1, encoding='default', line_ending='default'):
        """
        Read a response string from the instrument

        :param bytes num: Number of bytes to read back
        :param str encoding: The encoding to use when converting the response from bytes to str
        :param str line_ending: The line ending to strip off from end of received message
        """
        encoding = self.ENCODING if encoding == 'default' else encoding
        line_ending = self.LINE_ENDING if line_ending == 'default' else line_ending
        return self.read_raw(num).decode(encoding).rstrip(line_ending)

    def query_raw(self, message, encoding='default', num=-1):
        """
        Convenience method to first send a **string** message
        and then return the **binary** response data from a
        subsequent :py:meth:`read_raw()` call.
        """
        self.write(message)
        return self.read_raw(num)

    def query(self, message, num=-1, encoding='default', line_ending='default'):
        """
        Convenience method to first send a string command,
        then read and return a response string.
        :param str line_ending: The line ending to add to the message
        """
        if type(message) is tuple or type(message) is list:
            # recursive call for a list of commands
            val = list()
            for message_i in message:
                val.append(self.query(message_i, num=num, encoding=encoding, line_ending=line_ending))
            return val

        self.write(message, encoding=encoding, line_ending=line_ending)
        return self.read(num, encoding=encoding, line_ending=line_ending)

    @property
    def idn(self):
        """ The response to an ``*IDN?`` query. """
        return self.query("*IDN?", 300)
