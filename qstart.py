# coding: utf-8
import socket

import uvicorn

import webapp

# ip = socket.gethostbyname(socket.gethostname())

print("Running on port 80. App is accessible via:")
for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
    print("http://%s/" % (ip, ))

try:
    uvicorn.run(webapp.app,
                host="0.0.0.0",
                port=80,
                access_log=False,
                server_header=False)
except PermissionError:
    print(
        "Running on port 80 without super-user permissions is not permitted.")
    print("Running on alternative port 8080. App is accessible via:")
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        print("http://%s:8080/" % (ip, ))
    uvicorn.run(webapp.app,
                host="0.0.0.0",
                port=8080,
                access_log=False,
                server_header=False)
