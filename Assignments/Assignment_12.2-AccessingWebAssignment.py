import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
emptyStr = ""
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    #print(data.decode(),end='')
    emptyStr = emptyStr + data.decode()

mysock.close()

print(emptyStr)

tmpLst = emptyStr.split("\r\n")
#print(tmpLst)
print(re.findall('Last-Modified: (.+\S)',emptyStr))
print(re.findall('ETag: "(.+)\S',emptyStr))
print(re.findall('Content-Length: (.+\S)',emptyStr))
print(re.findall('Cache-Control: (.+\S)',emptyStr))
print(re.findall('Content-Type: (.+\S)',emptyStr))
print(ord('G'))
