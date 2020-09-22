#Создать приложение, в котором будет посылаться команда другому приложению, 
#на удаление письма по заданному номеру. 
#Реализовать в этом же приложении отправку письма с заданной темой письма

import socket
import ssl
import base64
from datetime import datetime
from socket import *
#part 1
print("hello")
sock=socket(AF_INET, SOCK_STREAM)
sock.connect(('127.0.0.1',7777))
number = input("Enter letter number: ")
sock.send(number.encode('utf-8'))

sock.settimeout(10)

sock.close()
#part 2
username = 'new_testoviy_acc'.encode()
username = base64.b64encode(username)

password = 'newtestacc123'.encode()
password = base64.b64encode(password)


mailserver = 'new_testoviy_acc'
mailserver = 'smtp.mail.ru'
cSock = socket(AF_INET, SOCK_STREAM)

cSock.connect((mailserver, 465))
cSockSSL = ssl.wrap_socket(cSock)
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send("EHLO Lmao \r\n".encode('utf-8'))
recv = cSockSSL.recv(1024)
print(recv)
cSockSSL.send("AUTH LOGIN \r\n".encode('utf-8'))
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send(username+"\r\n".encode())
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send(password+"\r\n".encode())
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send("MAIL FROM: new_testoviy_acc@mail.ru \r\n".encode())
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send("RCPT TO: new_testoviy_acc@mail.ru \r\n".encode())
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send("DATA \r\n".encode())
recv = cSockSSL.recv(1024)
print(recv)

sender = "From: new_testoviy_acc@mail.ru\r\n".encode()
rec = "To: new_testoviy_acc@mail.ru\r\n".encode()
sub = "Subject: Testing email\r\n\n".encode()
date = datetime.now()

cSockSSL.send(sender)
cSockSSL.send(rec)
#cSockSSL.send((str(date)+end).encode())
cSockSSL.send(sub)

end="\r\n"
msg = '0'

while True:
    msg=input("Enter massage. To finish enter 1: ")
    msg=msg+end
    if (msg == '1\r\n'):
        cSockSSL.send(".\r\n".encode())
        break
    cSockSSL.send(msg.encode())

cSockSSL.send("QUIT \r\n".encode())
recv = cSockSSL.recv(1024)
print(recv) 

cSockSSL.close()
cSock.close()
