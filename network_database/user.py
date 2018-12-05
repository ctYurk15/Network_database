from socket import socket, gethostname
from maker import divide_words

#send data
def send_data(data):
    data = bytes(data, 'utf-8')
    s.send(data)

#receive
def download():
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

#connection loop
connection = True
while connection:
    i = input()
    if i == '/escape':
        connection = False
        send_data(i)
    elif i.count('/download') == 1:
        send_data('/download')
        i = divide_words(i)
        n = i[1]
        send_data(n)
        download()
    elif i.count('/redact') == 1:
        send_data('/redact')
        i = divide_words(i)
        n = i[1]
        send_data(n)
        redact = True
        while redact:
            msg = input('Add: ')
            if msg != '/end':
                send_data(msg)
            else:
                send_data(msg)
                redact = False
    else:
        print('What? Please, log again.')

s.close()

