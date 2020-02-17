import time
import socket

s = socket.socket()

ip = "2.59.40.125"
port = 9090

s.connect((ip, port))

for i in range(1):
    data = str(s.recv(4096), 'utf8')
    print(data)

    sec = (int(time.time()) * 1103515245 + 12345) % (1 << 31)

    s.send((str(sec)+"\n").encode())

    data = s.recv(4096)
    print(data.decode())



s.close()


