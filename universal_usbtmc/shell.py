#!/usr/bin/env python

"""
A shell for USBTMC devices
"""

import argparse

from universal_usbtmc import import_backend
from universal_usbtmc.exceptions import *

# Py2 fix for input()
try: input = raw_input
except NameError: pass

HOWTO = """
Enter a command. It will directly be sent to the USBTMC device.
If the command ends with a question mark ('?'), the answer
will be read from the device.
Quit the shell with  'quit'  or by pressing Ctrl-C
"""

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--backend', '-b', #choices=('linux_kernel', 'python_usbtmc'),
        default='linux_kernel',
        help='The backend to use')
    parser.add_argument('--line-ending', default='',
        help="The line ending to add to commands you're sending")
    parser.add_argument('device', help='')
    args = parser.parse_args()

    args.line_ending = args.line_ending.replace("\\n", "\n").replace("\\r","\r")
    try:
        backend = import_backend(args.backend)
    except UsbtmcNoSuchBackend:
        parser.error('Unknown backend {}.'.format(args.backend))
    except UsbtmcMissingDependency as md:
        parser.error('The backend could not be loaded, ' + str(md))
    be = backend.Instrument(args.device)
    print(HOWTO)
    print('> *IDN?')
    print(be.query("*IDN?"))
    try:
        while True:
            cmd = input('> ')
            cmd = cmd.strip()
            if cmd in ('quit', 'exit'):
                break
            cmd = cmd + args.line_ending
            try:
                if '?' in cmd:
                    ret = be.query_raw(cmd)
                    try:
                        print(ret.decode('utf-8').rstrip(args.line_ending))
                    except UnicodeDecodeError:
                        print('binary message:', ret)
                else:
                    be.write(cmd)
            except UsbtmcReadTimeoutError:
                print('Timeout occured')
    except KeyboardInterrupt as e:
        print('\nCtrl-C pressed.')
    except EOFError:
        pass
    print('Exiting...')

if __name__ == "__main__":
    main()

