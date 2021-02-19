import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
totalCount = 0
data = uh.read()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

#print(json.dumps(js,indent = 4))

for field in js['comments']:
    totalCount = totalCount + int(field['count'])

print("Sum:", totalCount)
print("Count:", len(js['comments']))
