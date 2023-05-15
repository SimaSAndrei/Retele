import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 66666))
server.listen()

print("Server is listening...")


clients = []
nicknames = []

def broadcsast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcsast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close

            nickname = nicknames[index]
            broadcsast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, adress = server.accept()
        print("Connected with {} ".format(str(adress)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcsast("{} joined".format(nickname).encode('ascii'))
        client.send('Connected to server! '.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
