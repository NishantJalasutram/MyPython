import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

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
#print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('.//count')
#print(counts)
#results = tree.findall('comments/comment')
#print(results)
#print("Comment count: ",len(results))
#for field in results:
    #print(field.find("name").text)
    #print(field.find('count').text)
for field in counts:
    totalCount = totalCount + int(field.text)
#print('name', name, 'count', count)
print("Count:",len(counts))
print("Sum:",totalCount)
