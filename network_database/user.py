from socket import socket, gethostname
from maker import divide_words

#send data
def send_data(data):
    data = bytes(data, 'utf-8')
    s.send(data)

#receive
def download():
    name = s.recv(1024).decode()
    if name == 'No':
        print('Here aren`t file with that name. Try another.')
    else:
        data = s.recv(1024).decode()
        path = 'downloads/' + name + '.txt'
        with open(path, 'w') as file:
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
    elif i.count('/createfile') == 1:
        send_data('/createfile')
        i = divide_words(i)
        n = i[1]
        send_data(n)
        msg = s.recv(1024).decode()
        if msg == 'No':
           print('File with name', n, 'created succesfully.')
        else:
            print('File with this name already are in server. Try another.')
    elif i.count('/redact') == 1:
        send_data('/redact')
        i = divide_words(i)
        n = i[1]
        send_data(n)
        msg = s.recv(1024).decode()
        if msg == 'Yes':
            redact = True
            print('Redacting a file', n)
        else:
            redact = False
        while redact:
            msg = input('Add: ')
            if msg != '/end':
                send_data(msg)
            else:
                send_data(msg)
                redact = False
    elif i.count('/readfile') == 1:
        i = divide_words(i)
        n = i[1]
        path = 'downloads/' + n + '.txt'
        try:
            file = open(path, 'r')
        except:
            print('Aren`t a file with this name. Try to download.')
        else:
            j = file.read()
            print(j)
        
    else:
        print('What? Please, log again.')

s.close()

