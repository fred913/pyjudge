# coding: utf-8
import json
import click

print("请确保主程序已关闭！")

with open("./alldata.json", "r", encoding="utf-8") as f:
    all_classes_data = json.load(f)

with open("./users.json", "r", encoding="utf-8") as f:
    userdata = json.load(f)

print("正在存档...")
all_classes_data['classes_data'][all_classes_data['current']] = userdata
print("已存档！")

print("请输入下一个上课的班级，不要回车（就一个数字，如1、2、3）输入q取消：", end="", flush=True)
class_id = click.getchar(echo=True)
if class_id == "q":
    print("\n已取消", flush=True)
    exit(0)

all_classes_data['current'] = class_id
userdata = all_classes_data['classes_data'].get(class_id) or {}

with open("./users.json", "w", encoding="utf-8") as f:
    json.dump(userdata, f, indent=2)

with open("./alldata.json", "w", encoding="utf-8") as f:
    json.dump(all_classes_data, f, indent=2)

print("\n已保存！")
