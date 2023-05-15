# printare ip oricarui site
import socket
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#AM CREAT OBIECTUL SOCKET
ip=socket.gethostbyname('www.github.com')
print(ip)

