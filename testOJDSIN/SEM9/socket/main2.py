import socket
import sys

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket creat cu succes")
except socket.error as err:
    print(f'Socket error eith error{err}')

port=80

try:
    host_ip=socket.gethostbyname("www.github.com")
except socket.gaierror:
    print('error resolving the host')
    sys.exit()

s.connect((host_ip,port))
print(f'Socket has succesfully connected to GItHub: {host_ip}')