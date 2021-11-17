import socket
from threading import Thread
import threading
import time
from progress.bar import IncrementalBar

N = 2**16 - 1
bar = IncrementalBar('Countdown', max=3000)

for port in range(1,100):
    sock = socket.socket()
ip = '127.0.0.1'
thred_array = []
closed_array = []


def port_scan(ip, port_name):
    global thred_array, closed_array
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(port)
        sock.connect(('127.0.0.1', port))
        print("Порт", i, "открыт")
        connect = sockt.connect((ip, port_name))
        print(f'Port:\033[32m {port_name}\033[0m is\033[32m live \033[0m')
        thred_array.append(port_name)
        sockt.close()
    except:
        continue
    finally:
        sock.close() 
        print(f'Port: {port_name} is\033[31m down \033[0m\n')
        closed_array.append(port_name)
        sockt.close()

def open_ports():
    global thred_array
    print('Opened ports: ')
    print(thred_array)

for p_name in range(3000):
    bar.next()
    thred = threading.Thread(target=port_scan, args=(ip, p_name))
    thred.start()

time.sleep(3)
sec_thred = threading.Thread(target = open_ports)
sec_thred.start()

thrd_th = threading.Thread(target = closed_ports)
thrd_th.start()
