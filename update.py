# just poll Pipfile and download the new problems.
import requests
import base64

session = requests.Session()
pipfile_resp = session.get(
    "https://git.ft2.club:81/api/v1/repos/fred913/pythonflag/contents/Pipfile")

with open("./Pipfile", "rb") as f:
    f.write(base64.b64decode(pipfile_resp.json()['content'].encode()))
