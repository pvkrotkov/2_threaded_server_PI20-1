import socket
import threading

nickname = input("Как Вас зовут?")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))


def send():
    while True:
        message = f'{nickname}: {input()}'
        if message.replace(' ','').split(':')[-1] == 'exit':
            client.close()
            break
        else:
            client.send(message.encode('UTF-8'))


def get():
    while True:
        try:
            message = client.recv(1024).decode('UTF-8')
            if message == 'write_name':
                client.send(nickname.encode('UTF-8'))
            else:
                print(message)
        except:
            print("Отключение от сервера")
            client.close()
            break


receive_thread = threading.Thread(target=get)
receive_thread.start()

write_thread = threading.Thread(target=send)
write_thread.start()
