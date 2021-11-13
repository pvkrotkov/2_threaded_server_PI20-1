import socket
import threading
from contextlib import closing
def vvod (maks, chto, ymol):
        while True:
                #chis = "ymol"
                chis = input("vvedite " +chto+ " ili ymol dli znachenia po ymolchaniy "+str(ymol)+ ": ")
                if chis.isdigit(): #нуля до 65535
                        chis = int(chis)
                        if chis > -1 and chis < maks+1:
                                return (chis)
                        else:
                                print("vvodite chislo ot 0 do " + str(maks))
                elif chis == "ymol":
                        return(ymol)
                else:
                        print("nuzhno vvodit celoe chislo")
def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def poluch():
     while True:
        try:
             data = sock.recv(1024)
             print(data.decode('utf-8'))
             #sock.send(data)
        except OSError:
                break

sock = socket.socket()#socket.AF_INET,socket.SOCK_DGRAM)
nom = vvod(65535, "vash port", 52865)#62670

try:
        sock.bind(('', nom))
except OSError:
        nom = find_free_port()
        print('Ошибка. Выбранный вами код сервера уже занят, код сервера будет изменён автоматически. Новый код: ', nom)
        sock.bind(('', nom))
sock.setblocking(1)##
 
nom_pod = vvod(65535, "port podkluchenia", 53480)
ipe =''
ipeym = [127, 0, 0, 1]
for i in range (4):
        ipe += str(vvod(255, str(i+1)+" element ip", ipeym[i]))+'.'
ipe = ipe[:-1]
#file.write('ip podkluchenia - '+str(ipe)+'\n')
sock.connect((ipe, nom_pod))

sock.send(('').encode('utf-8'))
stream = threading.Thread(target= poluch)
stream.start()

def otprav( msg):
        sock.send(msg.encode('utf-8'))

while True:
    msg = input('Введите сообщение ( exit для выхода): ')
    
    otprav(msg)
    if msg == 'exit':
        #sock.recv(1024)
        break

sock.close()
#file.write("exit")
#file.close()
