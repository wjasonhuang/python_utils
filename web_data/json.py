import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_207430.json'
uh = urllib.request.urlopen(url, context=ctx)
data = json.loads(uh.read())

print(sum([item['count'] for item in data['comments']]))
