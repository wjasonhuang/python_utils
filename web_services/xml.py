import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_207429.xml'
uh = urllib.request.urlopen(url, context=ctx)
tree = ET.fromstring(uh.read())

results = tree.findall('.//count')
print(sum([int(count.text) for count in results]))
