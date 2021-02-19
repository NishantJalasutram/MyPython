# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def retURL(u,p):
    html = urllib.request.urlopen(u, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    newUrl = ""
    # Retrieve all of the anchor tags
    print("Retrieving: ",u)
    tags = soup('a')
    for tag in tags:
        newUrl = tag.get('href', None)
        p=p-1
        if p == 0: break
    return newUrl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter Count: ')
pos = input("Enter Position: ")
pos = int(pos)
count = int(count)

inpURL = url
while count >= 0:
    newHTTPURL = retURL(inpURL,pos)
    #print(newHTTPURL)
    inpURL = newHTTPURL
    count = count - 1
