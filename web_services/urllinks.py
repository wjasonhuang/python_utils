# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://py4e-data.dr-chuck.net/known_by_Sukhvir.html' 
pos = 18
reps = 7

for rep in range(reps):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    if len(tags) < pos:
        print('Link position is too big')
        break
    url = tags[pos-1].get('href', None)
    if url is None:
        print("Can't find the next link")
        break
    print('Next link:', url)
