from tqdm import tqdm

import socket
import threading
import time
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
#ip= '127.0.0.1'

ip=''
ipeym = [127, 0, 0, 1]
for i in range (4):
        ip += str(vvod(255, str(i+1)+" element ip", ipeym[i]))+'.'
ip= ip[:-1]

otkrut_port = []
close_port = []
portov = 2**16 - 1
if portov%2>0:
    portov_2 = portov//2+1
else:
    portov_2 = portov//2
def scanerr(ip, port_name):
    global otkrut_port, close_port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    try:
        s.connect((ip, port_name))
    except:
        print('Порт '+str(port_name)+' закрыт\n')
        close_port.append(port_name)
    else:
        print('Порт', port_name, 'открыт\n')
        otkrut_port.append(port_name)
    s.close()
    
def closee():
    global close_port
    close_port.sort()
    print('Закрытые порты: '+ str(close_port)[1:-1]+'\nЗакрытых портов: ',len(close_port))
    
def openn():
    global otkrut_port
    otkrut_port.sort()
    print('Открытые порты: '+str(otkrut_port)[1:-1]+'\nОткрытых портов: ', len(otkrut_port))

def pereb(startt, endd):
    global otkrut_port, close_port
    for port in range(startt, endd):

        thred = threading.Thread(target=scanerr, args=(ip, port))
        thred.start()
       #k+=1
#thred = threading.Thread(target=pereb, args=(1, portov_2))
#thred.start()
thred = threading.Thread(target=pereb, args=(portov_2, portov))
thred.start()
k = 0
for port in tqdm(range(portov_2)):
    k+=1
    thred = threading.Thread(target=scanerr, args=(ip, k))
    thred.start()

time.sleep(2)
open_potok = threading.Thread(target=openn)
open_potok.start()

close_potok = threading.Thread(target= closee)
close_potok.start()
