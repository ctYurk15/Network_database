from socket import socket, gethostname
from threading import Thread

#send data
def send_data(data):
    data = bytes(data, 'utf-8')
    s.send(data)

#connection to server
s = socket()
port = 8787
host = gethostname()
s.connect((host, port))

#send name
name = input('Chose name of data: ')
name = bytes(name, 'utf-8')
s.send(name)

#connection loop
connection = True
while connection:
    i = input()
    if i == '/escape':
        connection = False
        send_data(i)
    else:
        send_data(i)

s.close()

