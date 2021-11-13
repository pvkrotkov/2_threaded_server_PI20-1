import threading
import socket
from tqdm import tqdm

target = input('Введите ip адрес или 1 для стандартного ip: ')
if target == '1':
    target = '127.0.0.1'

k_min = int(input('Введите начальный порт для проверки: '))
while True:
    if k_min < 0:
        print('Вы ввели неверный порт')
        k_min = int(input('Введите начальный порт для проверки: '))
    else:
        break

k_max = int(input('Введите конечный порт для проверки: '))
while True:
    if k_max >= k_min:
        break
    else:
        print('Вы ввели неверный порт')
        k_max = int(input('Введите конечный порт для проверки: '))

opened = []


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)

    try:
        con = s.connect((target, port))

        opened.append(port)
        con.close()
    except:
        pass


r = 1
print('--------------ПРОВЕРКА НАЧАТА--------------')
for x in tqdm(range(k_min, k_max + 1)):
    t = threading.Thread(target=portscan, kwargs={'port': r})

    r += 1
    t.start()

print('--------------ПРОВЕРКА ОКОНЧЕНА--------------')

closed = []
for i in range(k_min, k_max + 1):
    if i not in opened:
        closed.append(i)
print('Открытые порты: ', *opened)
print('--------------------------------------------')
print('Закрытые порты: ', *closed)
