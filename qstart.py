# coding: utf-8
import waitress
import webapp
import socket

# ip = socket.gethostbyname(socket.gethostname())

print("Running on port 80. App is accessible via:")
for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
    print("http://%s/" % (ip, ))

try:
    waitress.serve(webapp.app, host="0.0.0.0", port=80, threads=6)
except PermissionError:
    print(
        "Running on port 80 without super-user permissions is not permitted.")
    print("Running on alternative port 8080. App is accessible via:")
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        print("http://%s:8080/" % (ip, ))
    waitress.serve(webapp.app, host="0.0.0.0", port=8080, threads=6)
