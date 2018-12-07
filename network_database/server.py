from socket import socket, gethostname
from threading import Thread

users = []

#witing a data
def write(data, name):
    path = 'datas/' + name + '.txt'
    with open(path, 'a') as file:
        file.write(data)
        file.write('\n')

#creating a blank file
def create_file(name, addr):
    addr = str(addr)
    path = 'datas/' + name + '.txt'
    with open(path, 'a') as file:
        file.write('Created by ')
        file.write(addr)
        file.write('\n')

#send data
def send_data(name, user_socket):
    path = 'datas/' + name + '.txt'
    name = bytes(name, 'utf-8')
    user_socket.send(name)
    with open(path, 'r') as file:
        msg = file.read()
        msg = bytes(msg, 'utf-8')
        user_socket.send(msg)

#send_msg
def send(msg, user_socket):
    msg = bytes(msg, 'utf-8')
    user_socket.send(msg)

#connections
def connected(user_socket, addr):
    users.append(user_socket)
    print('| New connection from: {}'.format(addr), '|')
    connected = True
    while connected:
        info = user_socket.recv(1024).decode()
        if info == '/escape':
            connected = False
            print('| Disconnection from {}'.format(addr), '|')
        elif info == '/download':
            name = user_socket.recv(1024).decode()
            send_data(name, user_socket)
            print('| Send', name, 'to', addr, '|')
            name = ''
        elif info == '/create':
            name = user_socket.recv(1024).decode()
            create_file(name, addr)
            print('| Created', name, 'by', addr, '|')
            msg = 'Creating a file with name ' + name + ' completed succesfully'
            send(msg, user_socket)
            name = ''
        elif info == '/redact':
            name = user_socket.recv(1024).decode()
            path = 'datas/' + name + '.txt'
            try:
                file = open(path, 'r')
            except:
                send('No', user_socket)
            else:
                send('Yes', user_socket)
                print('| From', addr, 'redact', name, '|')
                redact = True
                while redact:
                    data = user_socket.recv(1024).decode()
                    if data != '/end':
                        write(data, name)
                        print('| From', addr, 'added to', name, data, '|')
                    else:
                        redact = False
                        print('| End redacting', name, 'from', addr, '|')
                name = ''
    users.remove(user_socket)
    user_socket.close()

#making a socket
s = socket()
host = gethostname()
port = 8787
s.bind((host, port))
s.listen(10)
print('| Server started |')

#connection loop
while True:
    us, addr = s.accept()
    Thread(None, target=connected, args = (us, addr)).start()

s.close()
