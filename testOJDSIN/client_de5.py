import socket
import threading

nickname = input("Choose a nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 66666))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("ERROR!!")
            client.close()
            break

def write():
    message = f'{nickname}: {input("")}'
    client.send(message.encode('ascii'))


receive_threading = threading.Thread(target=receive)
receive_threading.start()

write_threading = threading.Thread(target=write)
write_threading.start()

