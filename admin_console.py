# coding: utf-8
import json
import time


def get_sit_id_by_ip(ip):
    # placeholder now...
    return "sit_id"


def get_json(fn):
    with open(fn, "r", encoding="utf-8") as f:
        return json.load(f)


print("请输入要查看的题号：")

pid = int(input(">>> "))

print("按下Ctrl-C 退出")
while True:
    try:
        data = get_json("./users.json")
    except Exception:
        continue
    finished = []
    unfinished = []
    for i, j in data.items():
        if j >= pid:
            finished.append(get_sit_id_by_ip(i))
        else:
            unfinished.append(get_sit_id_by_ip(i))
    print("\n\n题目 %d\n已完成：%s" % (
        pid,
        " ".join(finished),
    ))
    print("未完成：%s" % (" ".join(unfinished), ))

    time.sleep(0.3)