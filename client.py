import socket
import re
from threading import *

sock = socket.socket()
sock.setblocking(True)
isOpen = False


def client():
    global isOpen
    adr = str(input('Введите адрес сервера = '))
    port = int(input('Введите порт сервера = '))
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", adr): # регулярное выражение которое проверяет верность введенного ip
        try:
            sock.connect((adr, port))
            print('Подключение установлено')
        except:
            print('Порт закрыт')
        isOpen = True
        while True:
            print('введите сообщение')
            msg = input()
            sock.send(msg.encode())
            if msg == "exit":
                break

    else:
        print("Не верный IP")


def server():
    global isOpen
    while True:
        if isOpen:
            data = sock.recv(1024)
            if data is not None or data != "":
                print(data.decode())


if __name__ == "__main__":
    client = Thread(target=client)
    server = Thread(target=server)

    client.start()
    server.start()
