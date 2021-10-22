import socket
import threading
import time

ip_adres = '192.0.0.8'
thred_array = []
closed_array = []

def port_scanner(ip_adres, port_name):
    global thred_array, closed_array
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.01)
    try:
        connect = sock.connect((ip_adres, port_name))
        print(f'Порт: {port_name} открыт \n')
        thred_array.append(port_name)
        sock.close()
    except:
        print(f'Порт: {port_name} закрыт \n')
        closed_array.append(port_name)
        sock.close()

def open_ports():
    global thred_array
    print('Массив открытых портов:')
    print(thred_array)
    print(f'Открытых портов: {len(thred_array)} \n')

def closed_ports():
    global closed_array
    closed_array.sort()
    print('Массив закрытых портов: ')
    print(closed_array)
    print(f'Закрытых портов: {len(closed_array)}')

for port_name in range(1,64001):
    thred = threading.Thread(target=port_scanner, args=(ip_adres, port_name))
    thred.start()

time.sleep(1)
sec_thred = threading.Thread(target=open_ports)
sec_thred.start()

thrd_th = threading.Thread(target= closed_ports)
thrd_th.start()