import socket
import string

s = socket.socket()

ip = "188.225.34.174"
port = 41341

s.connect((ip, port))

res = ""

for j in range(1000):
    for i in range(36, 128):
        s.send(str(res+chr(i)).encode())
        data = str(s.recv(4096), 'utf8')
        if data == "Yes\n" or data == "Yes":
            print(data, res, chr(i))
            res += chr(i-1)


print(res)

s.close()
