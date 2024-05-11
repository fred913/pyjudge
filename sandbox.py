# coding: utf-8
from abc import abstractmethod
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
import js2py
import js2py.pyjs

USERCODE_EXEC_FILENAME = "<userCode>"


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
            print("from:", repr(self))
            raise NameError(k)


def generate_fake_sys(stdin: io.StringIO,
                      stdout: io.StringIO,
                      stderr: io.StringIO | None = None):

    return sandbox_module(dict(stdin=stdin, stdout=stdout, stderr=stderr),
                          "<module 'sys' (built-in)>")


class BaseSandbox:

    def __init__(self, timeout: int | None = None):
        pass

    @abstractmethod
    def run(self, code: str):
        raise NotImplementedError


class PySandbox(BaseSandbox):

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
            raise ImportError("No module named '%s'" % (name, )) from None

    def print_(self, *args, **kwargs):
        kwargs.setdefault("file", self.print_buffer)
        print(*args, **kwargs)

    def run(self, code):
        globals_ = {"__builtins__": self.venv_builtins}
        self.input_buffer.seek(0)
        try:
            compiled = compile(code,
                               filename=USERCODE_EXEC_FILENAME,
                               mode="exec")
            func_timeout(self.timeout, exec, args=(compiled, globals_))
        except FunctionTimedOut:
            return "程序代码运行超时，请检查是否有死循环等逻辑错误或未做优化"
        except Exception as e:
            # traceback.print_exc()
            frames = traceback.extract_tb(sys.exc_info()[2])
            lineno = -1

            for fr in frames:
                if fr.filename == USERCODE_EXEC_FILENAME:
                    lineno = fr.lineno
            return "程序代码运行错误 (line #%d) %s：%s" % (lineno, e.__class__.__name__,
                                                  str(e) or "无剩余信息")
        return 0


class jssandbox_module:

    def __init__(self, children: dict[str, Any], representation: str):
        self._ch = children
        self._repr = representation

    def __repr__(self) -> builtins.str:
        return self._repr

    def get(self, k: str):
        try:
            return self._ch[k]
        except KeyError as e:
            print("from:", repr(self))
            raise NameError(k)

    def callprop(self, funcname: str, *args, **kwargs):
        return js2py.base.Js(self.get(funcname)(*args, **kwargs))


class JSSandbox(BaseSandbox):

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

    def target(self, code: str, globals_: dict[str, Any]):
        ctx_env = globals_.copy()

        def lcon(*args, **kwargs):
            # super weird but real
            x = list(args) + list(kwargs.values())
            xs = [eval(repr(i)) for i in x]  # how the fuck the shit works???
            self.print_(*xs)

        for name in dir(js2py.pyjs):
            ctx_env[name] = getattr(js2py.pyjs, name)

        ctx_env['console'] = ctx_env['JS_BUILTINS'][
            'console'] = jssandbox_module(
                dict(callprop=lambda _, *args, **kw: lcon(*args, **kw)
                     if _ != "readline" else self.input_(eval(repr(args[0]))),
                     log=lcon,
                     debug=lcon,
                     error=lcon,
                     warn=lcon,
                     info=lcon,
                     readline=self.input_),
                "console {debug: ƒ, error: ƒ, info: ƒ, log: ƒ, warn: ƒ, ...}")

        translated = js2py.translate_js(code,
                                        HEADER="""var = Scope( JS_BUILTINS )
set_global_object(var)
""")
        exec(translated, ctx_env)

    def run(self, code):
        globals_ = {"__builtins__": self.venv_builtins}
        self.input_buffer.seek(0)
        try:
            func_timeout(self.timeout,
                         JSSandbox.target,
                         args=(self, code, globals_))
        except FunctionTimedOut:
            return "程序代码运行超时，请检查是否有死循环等逻辑错误或未做优化"
        except js2py.PyJsException as e:
            traceback.print_exc()
            return "程序代码运行错误 %s" % (str(e) or "无剩余信息", )
        except Exception as e:
            traceback.print_exc()
            return "程序代码运行错误 %s：%s" % (e.__class__.__name__, str(e) or "无剩余信息")
        return 0


if __name__ == "__main__":
    s = PySandbox()
    s.run("print(\"hahaha\")")
    print(repr(s.print_buffer))
