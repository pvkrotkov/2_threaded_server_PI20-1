import socket
from bcrypt import checkpw, hashpw, gensalt
import threading
from contextlib import closing
from os import remove

#dopravit pausy, proverka povtorov i registr v otdeln potok

def logging (sob):#, nom
    f = open(log_nam, 'a')
    f.write(sob+'\n')
    f.close()
def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

def vvod (maks, chto, ymol):
        while True:
                #chis = "ymol"
                chis = input("Введите " +chto+ " или ymol для значения по умолчанию = "+str(ymol)+ ": ")
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


def poluch(kto):
    '''
    while work==False:
        continue#'''
    msg = kto.recv(1024).decode()
    return msg

def otprav(drkto, msg):
    #if work:
    drkto.send(msg.encode('utf-8'))



class ConnectionThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__(daemon=True)
        self.conn = conn
        self.addr = addr
        self.connected = False
        self.whoisit = ''
        
        
 
    def login(self):
        try:
            logging('user '+self.addr[0]+' connect')#addr[0] 
            
            for i in spic:
                if str(self.addr) == str(i):
                    while True:
                        name = spic[i]
                        otprav(self.conn, 'Здравствуйте, '+name+'. Введите ваш пароль')
                        msg = poluch(self.conn)
                        file = open('pas'+name+'.bin', "rb")
                        key = file.read()
                        file.close()
                        if checkpw(bytes(msg, encoding='utf-8'), key):
                            key=''
                            msg=''
                            otprav(self.conn, 'Пароль принят')
                            logging('user '+name+' enter the conf')
                            break
                        else:
                            key=''
                            otprav(self.conn, 'Неверный пароль')
                    break
                    
                
            else:  
                otprav(self.conn, 'Здравствуйте, мы ещё не знакомы. Представьтесь, пожалуйста')
                name = poluch(self.conn)
                otprav(self.conn, "Введите ваш пароль")
                key = poluch(self.conn)
                key = hashpw(bytes(key, encoding='utf-8'), gensalt())
                with open("pas"+str(name)+".bin", "wb") as file:
                    file.write(key)
                key=''
                with open("users_2.txt", "a") as file:
                    file.write(str(self.addr)+' NaMe '+str(name)+'\n')
                spic.update({self.conn: name}) 
            self.connected = True
            otprav(self.conn, 'Спасибо')
            connect.append(self.conn)
            
            self.whoisit = name
        except ConnectionResetError:
            pass

    def run(self):
        while True:
            if work and self.connected == False and self.whoisit != False:#Не трогать! Это на случай повторного входа
                self.whoisit = False
                try:
                    loggg = threading.Thread(target=self.login)
                    loggg.start()
                except ConnectionResetError:
                    continue
            while self.connected and work:
                try:
                    msg = poluch(self.conn)
                    
                    if msg == 'exit':
                        self.connected = False
                        connect.remove(self.conn)
                        logging('user '+self.whoisit+' exit')
                    elif work:
                        logging('received message from '+self.whoisit)
                        msg = '{'+self.whoisit+'}: '+msg
                        for i in connect:
                            if i != self.conn:
                                try:
                                    otprav(i, msg)
                                except ConnectionResetError:
                                    del(connect[connect.index(i)])
                        with open(st_file, 'a') as f:
                            f.write(msg+'\n')
                except ConnectionResetError:
                    del(connect[connect.index(i)])
                    break
                

connect=[]
spic={}#[]
with open('users_2.txt', 'r') as file:
    for line in file:#file.write(str(addr)+' NaMe '+str(name)+'\n')
        nom = line.split(' NaMe ')
        spic.update({nom[0]: nom[1][:-1]}) 
        
#file.close()
sock = socket.socket()
nom = vvod(65535, "vash port", 53480)
try:
        sock.bind(('', nom))
except OSError:
        nom = find_free_port()
        print('Ошибка. Выбранный вами код сервера уже занят, код сервера будет изменён автоматически. Новый код: ', nom)
        sock.bind(('', nom))

log_nam = 'log_server'+str(nom)+'.txt'
with open(log_nam, 'w') as f:
    f.write('Server activate\nvash port servera - '+str(nom)+ '\n')
st_file='story_let'+str(nom)+'.txt'
with open(st_file, 'w') as f:
    f.write('')
#f.close()
#logging('')

sock.listen(4)
work=True
def sozd_thr(sock):
    while work:
        #print(9)
        try:
            potok = ConnectionThread(*sock.accept())
            potok.start()
        except OSError:
            break

gen_th = threading.Thread(target=sozd_thr, args=[sock])
gen_th.start()

#sozd_thr(sock)



while True:
    comm = input('exit - Отключение сервера, showstor - история сообщений, pause - остановка прослушивание порта, showlog - Показ логов, clearlog - Очистка логов, killusers - Очистка файла идентификации: ')
    if 'showlog' == comm:
        with open(log_nam, 'r') as f:#st_file
            for i in f:
                print(i, end='')
    elif 'showstor' == comm:
        with open(st_file, 'r') as f:#st_file
            for i in f:
                print(i, end='')
    elif 'clearlog' == comm:
         with open(log_nam, 'w') as f:
             f.write('logs clear\n')
    elif 'killusers' == comm:
        work = False
        logging('Users deleted')
        for line in spic:
            remove("pas"+spic[line]+".bin")
        with open('users_2.txt', 'w') as file:
            file.write('')
        work = True
    elif 'exit' == comm:
        #nstopot=False
        work = False
        logging('end of work')
        sock.close()
        break
    elif 'pause' == comm:
        if work:
            work = False
            print('Сервер поставлен на паузу. Для продолжения работы введите pause повторно')
            logging('server on pause')
        else:
            work = True
            print('Сервер снят с паузы.')
            logging('end of pause')
    else:
        print('Команда не распознана.')
