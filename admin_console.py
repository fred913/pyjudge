# coding: utf-8
import json
import time
import xml.etree.ElementTree


def get_json(fn):
    with open(fn, "r", encoding="utf-8") as f:
        return json.load(f)


print("正在解析班级...")
with open("./class.xml", "r", encoding="utf-8") as f:
    # tree = xml.etree.ElementTree.fromstring(f.read())
    tree = xml.etree.ElementTree.parse(f)
student_ip_map = {}
user_data = tree.getroot().find("students").findall("student")
for i in user_data:
    name = i.find("name").text
    ip = i.find("address").attrib['IP']
    student_ip_map[ip] = name
student_ip_map["127.0.0.1"] = "教师"


def get_sit_id_by_ip(ip):
    return student_ip_map.get(ip) or ip


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

    time.sleep(1.2)