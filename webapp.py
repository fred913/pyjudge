# coding: utf-8

import functools
import json
import logging
import os
import time
from typing import Callable, Coroutine

import jsbeautifier
import markdown
import yapf
from markdown.extensions.fenced_code import FencedCodeExtension
from quart import (Quart, Response, jsonify, redirect, render_template,
                   request, send_file, session)
from yapf.yapflib.errors import YapfError

import cached
import problems
import sandbox
import util_toml2jsonmd
from webutils import generate_403, generate_404

cache = cached.CacheMgr()

logging.getLogger("werkzeug").setLevel(logging.INFO)

pm = problems.ProblemManager()
app = Quart("webapp")
app.config['SECRET_KEY'] = os.environ.get("WEBAPP_SESS_SECRET", "nosecret")
app.config['TEMPLATES_AUTO_RELOAD'] = False

app.add_template_global(pm.get_problem_list, "get_problem_list")

ALLOWED_LANGUAGES = os.environ.get("ALLOWED_LANGUAGES",
                                   "python,javascript").split(",")
LANGMODE_REDIRECTS = {"js": "javascript", "py": "python"}

app.add_template_global(ALLOWED_LANGUAGES, "ALLOWED_LANGUAGES")  # type: ignore


@app.after_request
def no_cache_settings(response: Response):
    response.headers['Cache-Control'] = "no-cache"
    return response


@app.template_global("get_users")
def get_users(limit=None):

    result = sorted(get_userdata().items(), key=lambda x: x[1])
    if limit:
        result = result[:limit]
    return result


@app.errorhandler(NotImplementedError)
def prevent_internal_error_leak(error: Exception):
    import traceback
    traceback.print_exc()
    return generate_404()


# @cache.cache(0.5)
def get_userdata():
    with open("./users.json", "r", encoding="utf-8") as f:
        return json.load(f)


def put_userdata(d):
    with open("./users.json", "w", encoding="utf-8") as f:
        return json.dump(d, f, indent=4, ensure_ascii=False)


def requires_login(f: Callable[..., Coroutine]):

    @functools.wraps(f)
    async def wrapper(*args, **kwargs):
        if not session.get("user_data"):
            return redirect("/login")
        try:
            data = get_userdata()
        except json.JSONDecodeError:
            data = {}
        if session['user_data'] not in data:
            data[session['user_data']] = 0
            put_userdata(data)
        res = await f(*args, **kwargs)
        return res

    return wrapper


@app.route("/")
@requires_login
async def index():
    # tasks list
    return await render_template(
        "tasks.html",
        user_current=get_userdata()[session['user_data']],
        int=int)


@app.route("/login", methods=['GET', "POST"])
async def login():
    if request.method.lower() == "get":
        # render template
        return await render_template("login.html")
    else:
        # 组合学号姓名
        # student_name and student_id in request.form
        form = await request.form
        student_id = form.get("student_id", type=int)
        student_name = form.get("student_name")
        if student_id is None or student_name is None:
            return generate_403()
        student_name = student_name.strip()
        student_id = int(student_id)
        if student_id and student_name:
            session['user_data'] = "%d %s" % (student_id, student_name)
        return redirect("/", 301)


@app.route("/problem/<int:problem_id>")
@requires_login
async def do_problem(problem_id):
    problem_id = str(problem_id)
    metadata = pm.get_problem_meta(problem_id)
    return await render_template(
        "task.html",
        task_id=problem_id,
        metadata=metadata,
        allowed=get_userdata()[session['user_data']] >= (int(problem_id) - 1),
        allowed_param1=get_userdata()[session['user_data']] + 1)


@app.route("/problem.do/<int:problem_id>")
@requires_login
async def do_problem_code(problem_id: int):
    if not get_userdata()[session['user_data']] >= (int(problem_id) - 1):
        return redirect("/problem/%s" % (str(problem_id), ))

    mode = request.args.get("mode", None)
    if mode is None or mode not in ALLOWED_LANGUAGES:
        if mode is not None:
            redirection = LANGMODE_REDIRECTS.get(mode, )
            if redirection is None:
                if mode.endswith(".next") and mode.split(
                        ".")[0] in ALLOWED_LANGUAGES:
                    redirection = ALLOWED_LANGUAGES[
                        (ALLOWED_LANGUAGES.index(mode.split(".")[0]) + 1) %
                        len(ALLOWED_LANGUAGES)]
                else:
                    redirection = ALLOWED_LANGUAGES[0]
        else:
            redirection = ALLOWED_LANGUAGES[0]
        return redirect(request.path + "?mode=" + redirection)

    problem_id_str = str(problem_id)
    metadata = pm.get_problem_meta(problem_id_str)
    return await render_template("do_task.html",
                                 task_id=problem_id_str,
                                 metadata=metadata,
                                 langmode=mode)


@app.route("/api/content/<int:problem_id>")
@requires_login
async def get_content(problem_id: int):
    md = markdown.Markdown(extensions=[FencedCodeExtension()])
    return md.convert(pm.get_problem_description(str(problem_id)))


# @cache.cache(0.5)
@app.route("/api/subtitle/<int:problem_id>")
@requires_login
async def get_subtitle(problem_id):
    problem_id = str(problem_id)
    return '%d人已完成 - 代码限时%d秒 - %s' % (
        pm.get_problem_solve_data(problem_id)[0],
        pm.get_problem_meta(problem_id)['timeout'],
        "<span class=\"subtitle-is-done-mark\" done>已完成</span>"
        if get_userdata()[session['user_data']] >= int(problem_id) else
        "<span class=\"subtitle-is-done-mark\">未完成</span>")


@app.route("/api/submit.code/<int:problem_id>", methods=['POST'])
@app.route("/api/submit_code_v2/<int:problem_id>/<langmode_>",
           methods=['POST'])
@requires_login
async def submit_code_legacy(problem_id: int, langmode_: str | None = None):
    form = await request.form
    code = form.get("code", None)
    if code is None:
        return generate_403()
    langmode = langmode_ or "python"
    meta = pm.get_problem_meta(problem_id)
    # print(code)
    # advanced
    for i, o in meta.get("cases"):
        if langmode == "python":
            sb = sandbox.PySandbox(timeout=meta['timeout'])
        elif langmode == "javascript":
            sb = sandbox.JSSandbox(timeout=meta['timeout'])
        else:
            raise NotImplementedError
        sb.input_buffer.write(i + "\n")
        result = sb.run(code)
        if result == 0:
            if sb.print_buffer.getvalue().strip().lower() == o.strip().lower():
                continue
            else:
                print(repr(sb.print_buffer.getvalue()))
                result = "代码运行不通过（答案错误），请检查代码是否正确！"
                return result
        else:
            return result
    ud = get_userdata()
    ud[session['user_data']] = int(problem_id)
    put_userdata(ud)
    if not os.path.isdir("programs"):
        os.mkdir("programs")
    with open("./programs/%s_%s.py" %
              (session['user_data'], time.strftime("%Y-%m-%d-%H-%M-%S")),
              "w",
              encoding="utf-8") as f:
        f.write(code)
    return "代码运行通过！"


@app.route("/api/format", methods=['POST'])
@requires_login
async def format_code():
    form = await request.form
    code = form.get("code", None, str)
    if code is None:
        return generate_403()
    try:
        result = yapf.yapf_api.FormatCode(code, filename="<code>")[0]
        assert result
    except (IndentationError, NameError, YapfError) as e:
        # get the error
        return jsonify(
            [False,
             "代码%s错误，请检查代码是否正确: %s" % (e.__class__.__name__, str(e))])
    return jsonify([True, result])


@app.route("/api/format_v2/<lang>", methods=['POST'])
@requires_login
async def format_code_v2(lang: str):
    form = await request.form
    code = form.get("code", None, str)
    if code is None:
        return generate_403()
    if lang == "python":
        return await format_code()
    if lang == "javascript":
        return [True, jsbeautifier.beautify(code)]
    raise NotImplementedError


@app.route("/teacheradmin")
@requires_login
async def teacheradmin():
    if request.remote_addr != "127.0.0.1":
        return redirect("/")
    return await render_template("tadmin.html")


@app.route("/node_modules/<path:p>")
async def serve_node_static(p):
    realpath = os.path.abspath(os.path.join("node_modules", p))
    blocked_suffixes = {"package-lock.json", "package.json"}
    if not realpath.startswith(os.path.abspath(
            os.path.dirname(__file__))) or any(
                [realpath.endswith(i) for i in blocked_suffixes]):
        # hacking
        return generate_404()
    if os.path.isfile(realpath):
        return await send_file(realpath)
    return generate_404()


@app.route("/dStatic/highlightjs-theme.css")
async def get_highlightjs_theme():
    return await send_file("static/highlight/styles/googlecode.min.css")


if __name__ == "__main__":
    app.run("0.0.0.0", 80)
