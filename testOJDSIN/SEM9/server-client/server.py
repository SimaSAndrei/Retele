import socket

s=socket.socket()
port=56789

s.bind(("",port))
print(f'Socket binded to port{port}')

s.listen(5)#nr max de conexiuni permise
print('Socket is listening...')

while True:
    c,addr=s.accept()
    print("Got connection from",addr)
    message=("Thank you for connecting!")
    c.send(message.encode()) #trebuie asta cu decodatul
    c.close()