import socket
import ssl
import base64
from socket import *
#mailserver = 'smtp.mail.ru'
sock = socket(AF_INET, SOCK_STREAM)

sock.bind(('127.0.0.1',7777))
sock.listen (1)
conn, addr = sock.accept()
print ("connected: ", addr)

print ("Wait data...")
data = conn.recv(1024)
print (data)

conn.close()
sock.close()

username = 'new_testoviy_acc'.encode()
username = base64.b64encode(username)

password = 'newtestacc123'.encode()
password = base64.b64encode(password)


mailserver = 'pop.mail.ru'
cSock = socket(AF_INET, SOCK_STREAM)

cSock.connect((mailserver, 995))
cSockSSL = ssl.wrap_socket(cSock)
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send("USER new_testoviy_acc\r\n".encode('utf-8'))
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send("PASS newtestacc123\r\n".encode('utf-8'))
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send("STAT\r\n".encode('utf-8'))
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send("DELE ".encode()+ data +"\r\n".encode('utf-8'))
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send("STAT\r\n".encode('utf-8'))
recv = cSockSSL.recv(1024)
print(recv)

cSockSSL.send("QUIT\r\n".encode('utf-8'))
recv = cSockSSL.recv(1024)
print(recv)


cSockSSL.close()
cSock.close()
#input()
