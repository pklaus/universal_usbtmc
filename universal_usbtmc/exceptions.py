
# Py2/Py3 fix:
try:
    TimeoutError
except NameError:
    class TimeoutError(OSError): pass

# Our custom exceptions
class UsbtmcError(Exception): pass
class UsbtmcPermissionError(UsbtmcError): pass
class UsbtmcNoSuchFileError(UsbtmcError): pass
class UsbtmcNoSuchBackend(UsbtmcError): pass
class UsbtmcReadTimeoutError(UsbtmcError, TimeoutError): pass

class UsbtmcMissingDependency(UsbtmcError):
    def __init__(self, deps):
        self.deps = deps
    def __str__(self):
        deps_str = ', '.join(self.deps)
        return 'missing dependencies: {}'.format(deps_str)
