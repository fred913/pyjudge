# just poll Pipfile and download the new problems.
import requests
import base64

session = requests.Session()
response = session.get(
    "https://git.ft2.club:81/api/v1/repos/fred913/pythonflag/contents/Pipfile")

with open("./Pipfile", "wb") as f:
    f.write(base64.b64decode(response.json()['content'].encode()))

response = session.get(
    "https://git.ft2.club:81/api/v1/repos/fred913/pythonflag/contents/version.json"
)
result = base64.b64decode(response.json()['content'].encode()).decode("utf-8")
with open("./version.json", "w", encoding="utf-8") as f:
    f.write(result)
print("云端数据：当前已有%d道题目，正在更新题目数据..." % (result['problems'], ))

for i in range(1, result['problems']+1):
    # pid = i
    
