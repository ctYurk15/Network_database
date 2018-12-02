from socket import socket, gethostname
from threading import Thread

users = []

#witing a data
def write(data, name):
    path = 'datas/' + name + '.txt'
    with open(path, 'a') as file:
        file.write(data)
        file.write('\n')

#connections
def connected(user_socket, addr):
    users.append(user_socket)
    print('| New connection from: {}'.format(addr), '|')
    name = user_socket.recv(1024).decode()
    print('| From', addr, 'editing', name, '|')
    connected = True
    while connected:
        info = user_socket.recv(1024).decode()
        if info == '/escape':
            connected = False
            print('| Disconnection from {}'.format(addr), '|')
        else:
            print('| From', addr, 'send:', info, 'to', name, '|')
            write(info, name)
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
