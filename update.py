# coding: utf-8
# just poll Pipfile and download the new problems.
import requests
import base64
import os
import json
import subprocess
import sys

print("与服务器建立连接...")
session = requests.Session()
print("更新依赖项...")
response = session.get(
    "https://git.ft2.club:81/api/v1/repos/fred913/pythonflag/contents/Pipfile")

with open("./Pipfile", "wb") as f:
    # print("写到文件...")
    f.write(base64.b64decode(response.json()['content'].encode()))
print("正在安装依赖")
try:
    subprocess.run([sys.executable, "-m", "pipenv", "update"], check=True)
except subprocess.CalledProcessError:
    subprocess.run(["pipenv", "update"], check=True)

print("依赖项更新完成")
response = session.get(
    "https://git.ft2.club:81/api/v1/repos/fred913/pythonflag/contents/version.json"
)
result = base64.b64decode(response.json()['content'].encode()).decode("utf-8")
with open("./version.json", "w", encoding="utf-8") as f:
    f.write(result)
result2 = json.loads(result)
print("云端数据：当前已有%d道题目，正在更新题目数据..." % (result2['problems'], ))

for i in range(1, result2['problems'] + 1):
    # print("正在更新题目%d..." % (i, ))
    # pid = i
    if not os.path.isdir("problems/%d" % (i, )):
        os.mkdir("problems/%d" % (i, ))
    print("正在更新题目%d的简介..." % (i, ))
    response = session.get(
        "https://git.ft2.club:81/api/v1/repos/fred913/pythonflag/raw/problems/%d/description.md"
        % (i, ))
    with open("problems/%d/description.md" % (i, ), "wb") as f:
        # print("写到文件...")
        f.write(response.content)
    print("正在更新题目%d的详细信息..." % (i, ))
    response = session.get(
        "https://git.ft2.club:81/api/v1/repos/fred913/pythonflag/raw/problems/%d/info.json"
        % (i, ))
    with open("problems/%d/info.json" % (i, ), "wb") as f:
        # print("写到文件...")
        f.write(response.content)
    print("题目%d更新完成" % (i, ))
print("题目全部更新完成！")
