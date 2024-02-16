# coding: utf-8
import base64
import builtins
import json
import io
import math
import sys
import traceback
from typing import Any, Type, TypedDict
from func_timeout import func_timeout
from func_timeout import FunctionTimedOut


class sandbox_module:

    def __init__(self, children: dict[str, Any], representation: str):
        self._ch = children
        self._repr = representation

    def __repr__(self) -> builtins.str:
        return self._repr

    def __getattr__(self, k: str):
        try:
            return self._ch[k]
        except KeyError as e:
            raise NameError(k)


def generate_fake_sys(stdin: io.StringIO,
                      stdout: io.StringIO,
                      stderr: io.StringIO | None = None):

    return sandbox_module(dict(stdin=stdin, stdout=stdout, stderr=stderr),
                          "<module 'sys' (built-in)>")


class Sandbox:

    def __init__(self, timeout=None):
        self.generate_builtins()
        self.print_buffer = io.StringIO(initial_value="")
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
        return self.input_buffer.readline().strip(" ").strip("\n")

    def import_module(self, name, *_):
        replist = {
            "json":
            json,
            "sys":
            generate_fake_sys(self.input_buffer, self.print_buffer,
                              self.print_buffer),
            "math":
            math,
            "base64":
            base64
        }
        mod = replist.get(name, None)
        if mod is not None:
            return mod
        else:
            raise ImportError("No module named '%s'" % (name, ))

    def print_(self, *args, **kwargs):
        kwargs.setdefault("file", self.print_buffer)
        print(*args, **kwargs)

    def run(self, code):
        globals_ = {"__builtins__": self.venv_builtins}
        self.input_buffer.seek(0)
        try:
            func_timeout(self.timeout, exec, args=(code, globals_))
        except FunctionTimedOut:
            return "程序代码运行超时，请检查是否有死循环等逻辑错误或未做优化"
        except Exception as e:
            # traceback.print_exc()
            frames = traceback.extract_tb(sys.exc_info()[2])
            for _ in range(3):  # 3 frames are internal so hide them
                frames.pop(0)

            return "程序代码运行错误 (line #%d) %s：%s" % (
                frames[-1].lineno, e.__class__.__name__, str(e) or "无剩余信息")
        return 0


if __name__ == "__main__":
    s = Sandbox()
    s.run("print(\"hahaha\")")
    print(repr(s.print_buffer))
