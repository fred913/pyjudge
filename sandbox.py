import builtins
import json
import io
from func_timeout import func_timeout
from func_timeout import FunctionTimedOut


class Sandbox:
    def __init__(self, timeout=None):
        self.generate_builtins()
        self.print_buffer = ""
        self.input_buffer = io.StringIO(initial_value="")
        self.timeout = timeout or 4

    def generate_builtins(self):
        self.venv_builtins = {}
        for i in dir(builtins):
            self.venv_builtins[i] = getattr(builtins, i)
        self.venv_builtins['__import__'] = self.import_module
        self.venv_builtins['input'] = self.input_
        self.venv_builtins['print'] = self.print_
        self.venv_builtins['exit'] = self.none_func
        self.venv_builtins['open'] = self.none_func
        self.venv_builtins['help'] = self.none_func

    def none_func(self, *args, **kwargs):
        # disable a function via this
        return

    def input_(self, s=None):
        if s:
            self.print_(s)
        return self.input_buffer.readline().strip(" ")

    def import_module(self, name, *_):
        # just import it
        replist = {"json": json}
        for k, v in replist.items():
            if name.lower().strip() == k.lower().strip():
                return v
        raise ImportError("No module named '%s'" % (name, ))

    def print_(self, *a, sep=None, end=None, **_):
        if end is None:
            end = "\n"
        if sep is None:
            sep = " "
        b = []
        for i in a:
            if isinstance(i, str):
                b.append(i)
            else:
                b.append(repr(i))
        self.print_buffer += sep.join(b)
        self.print_buffer += end

    def run(self, code):
        globals_ = {"__builtins__": self.venv_builtins}
        self.input_buffer.seek(0)
        try:
            func_timeout(self.timeout, exec, args=(code, globals_))
        except FunctionTimedOut:
            return "程序代码运行超时，请检查是否有死循环等逻辑错误"
        except Exception as e:
            return "程序代码运行错误 %s：%s" % (e.__class__.__name__, str(e) or "无剩余信息")
        return 0


if __name__ == "__main__":
    s = Sandbox()
    s.run("print(\"hahaha\")")
    print(repr(s.print_buffer))
