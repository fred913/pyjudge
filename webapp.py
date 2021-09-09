import markdown
import problems
import sandbox
import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import functools
import logging
import yapf

logging.getLogger("werkzeug").setLevel(logging.WARNING)

from flask import render_template

pm = problems.ProblemManager()
app = Flask("webapp")

app.add_template_global(pm.get_problem_list, "get_problem_list")


@app.template_global("get_users")
def get_users(limit=None):
    def dict_cmp(a, b):
        if a[1] > b[1]:
            return 1
        elif a[1] == b[1]:
            return 0
        else:
            return -1

    result = sorted(get_userdata().items(), key=functools.cmp_to_key(dict_cmp))
    if limit:
        result = result[:limit]
    return result


def get_userdata():
    with open("./users.json", "r", encoding="utf-8") as f:
        return json.load(f)


def put_userdata(d):
    with open("./users.json", "w", encoding="utf-8") as f:
        return json.dump(d, f)


@app.before_request
def init_user():
    with open("./users.json", "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    if request.remote_addr not in data:
        data[request.remote_addr] = 0
        with open("./users.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


@app.route("/")
def index():
    # tasks list
    return render_template("tasks.html",
                           user_current=get_userdata()[request.remote_addr],
                           int=int)


@app.route("/problem/<int:problem_id>")
def do_problem(problem_id):
    problem_id = str(problem_id)
    metadata = pm.get_problem_meta(problem_id)
    return render_template(
        "task.html",
        task_id=problem_id,
        metadata=metadata,
        allowed=get_userdata()[request.remote_addr] >= (int(problem_id) - 1),
        allowed_param1=get_userdata()[request.remote_addr] + 1)


@app.route("/problem.do/<int:problem_id>")
def do_problem_code(problem_id):
    if not get_userdata()[request.remote_addr] >= (int(problem_id) - 1):
        return redirect("/problem/%s" % (str(problem_id), ))
    problem_id = str(problem_id)
    metadata = pm.get_problem_meta(problem_id)
    return render_template("do_task.html",
                           task_id=problem_id,
                           metadata=metadata)


@app.route("/api/content/<int:problem_id>")
def get_content(problem_id):
    return markdown.markdown(pm.get_problem_description(str(problem_id)))


@app.route("/api/subtitle/<int:problem_id>")
def get_subtitle(problem_id):
    problem_id = str(problem_id)
    return '%d人已完成 - 代码限时%d秒 - %s' % (
        pm.get_problem_solve_data(problem_id)[0],
        pm.get_problem_meta(problem_id)['timeout'], "已完成"
        if get_userdata()[request.remote_addr] >= int(problem_id) else "未完成")


@app.route("/api/submit.code/<int:problem_id>", methods=['POST'])
def submit_code(problem_id):
    code = request.form.get("code")
    meta = pm.get_problem_meta(problem_id)
    if meta.get("iscases"):
        # advanced
        for i, o in meta.get("cases"):
            sb = sandbox.Sandbox(timeout=meta['timeout'])
            sb.input_buffer.write(i + "\n")
            result = sb.run(code)
            if result == 0:
                if sb.print_buffer.strip().lower() == o.strip().lower():
                    continue
                else:
                    result = "<p>代码运行不通过（答案错误），请检查代码是否正确！</p>"
                    return result
            else:
                return result
        ud = get_userdata()
        ud[request.remote_addr] = int(problem_id)
        put_userdata(ud)
        return "<p>代码运行通过！</p>"
    else:
        sb = sandbox.Sandbox(timeout=meta['timeout'])
        sb.input_buffer.write(meta['stdin'] + "\n")
        result = sb.run(code)
        if result == 0:
            # let's check the stdout
            # don't let the students know the stdin content
            if meta['stdin']:
                result = ""
            else:
                result = "<p>程序输出内容：</p><pre>%s</pre>" % (
                    sb.print_buffer.replace("&", "&amp;").replace(
                        "<", "&lt;").replace(">", "&gt;"), )
            if sb.print_buffer.strip().lower() == meta['stdout'].strip().lower(
            ):
                result += "<p>代码运行通过！</p>"
                ud = get_userdata()
                ud[request.remote_addr] = int(problem_id)
                put_userdata(ud)
            else:
                result += "<p>代码运行不通过（答案错误），请检查代码是否正确！</p>"
        return result


@app.route("/api/format", methods=['POST'])
def format_code():
    code = request.form.get("code")
    try:
        result = yapf.yapf_api.FormatCode(code, filename="<code>")[0]
    except Exception as e:
        # get the error
        return jsonify(
            [False,
             "代码%s错误，请检查代码是否正确: %s" % (e.__class__.__name__, str(e))])
    return jsonify([True, result])


if __name__ == "__main__":
    app.run("0.0.0.0", 80, threaded=True)