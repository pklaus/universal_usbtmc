
import usbtmc
from .interface import usbtmc_backend

class Backend(usbtmc_backend):
    def __init__(self, device):
        instr = usbtmc.Instrument(device)
        print(instr.ask("*IDN?"))


