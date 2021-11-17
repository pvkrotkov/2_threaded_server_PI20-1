import socket
import re
import time
from threading import Thread
from scanner import find_port
from scanner import main_port

sock = socket.socket()
sock.setblocking(True)
isOpen = False
ports = [i for i in range(1024, 65535)]


def client():
    global isOpen
    adr = str(input('Введите адрес сервера = '))
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", adr):
        find_port(sock, adr)
        while main_port == -1:
            time.sleep(1)
        sock.connect((adr, main_port))
        isOpen = True
        print("Подключение установленно")
        while True:
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
