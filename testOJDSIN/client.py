import socket
import threading

nickname = input("Choose a nikname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 44444))

# define 2 methods and define 2 threads running simultan


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break


def write():
    while True:
        # message = '{}: {}'.format(nickname, input(''))
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
