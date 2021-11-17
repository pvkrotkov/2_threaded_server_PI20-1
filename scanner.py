import socket
from threading import Thread

main_port = -1


def find_port(sock, adr):
    cof = 3226
    for i in range(1024, 65535, cof):
        cof_i = i+cof if i+cof <= 65535 else 65535
        find = Thread(target=find_port_from_to, args=(sock, adr, i, cof_i))
        find.start()


def find_port_from_to(sock, adr, st, fn):
    global main_port
    for port in range(st, fn):
        try:
            sock.connect((adr, port))
            print("Найден порт: " + str(port))
            main_port = port
        except socket.error:
            continue
