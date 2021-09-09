import builtins

hack_command = """
import subprocess
print(subprocess.Popen)
"""


def import_module(a, *_):
    replist = {"os": None, "sys": None, "subprocess": None}
    for k, v in replist.items():
        if a.startswith(k):
            print(a, k, "replacing")
            if v:
                return v
            else:
                raise ImportError("No module named '%s'" % (a, ))
    return __import__(a)


builtins_ = {}
for i in dir(builtins):
    builtins_[i] = getattr(builtins, i)
builtins_['__import__'] = import_module

globals_ = {"__builtins__": builtins_}
exec(hack_command, globals_)