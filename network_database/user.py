from socket import socket, gethostname
from threading import Thread

#send data
def send_data(data):
    data = bytes(data, 'utf-8')
    s.send(data)

#receive
def receive():
    global connection
    while connection:
        name = s.recv(1024).decode()
        data = s.recv(1024).decode()
        path = 'downloads/' + name + '.txt'
        with open(path, 'a') as file:
            file.write(data)
            file.write('\n')
        print(name, 'downloaded succesfully')

#connection to server
s = socket()
port = 8787
host = gethostname()
s.connect((host, port))
print('Connected succesfully...')

#send name
name = input('Chose name of data: ')
name = bytes(name, 'utf-8')
s.send(name)

connection = True
#reciving thread
Thread(None, receive).start()

#connection loop
while connection:
    i = input()
    if i == '/escape':
        connection = False
        send_data(i)
    else:
        send_data(i)

s.close()

