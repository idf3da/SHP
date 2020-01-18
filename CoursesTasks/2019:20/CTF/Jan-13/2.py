import socket

s = socket.socket()

ip = "188.225.34.174"
port = 41337

s.connect((ip, port))

for i in range(15):
    data = str(s.recv(4096), 'utf8')
    print(data) 
    t = data.split("'")

    print(t)

    s.send(t[-2].encode())
    

data = s.recv(4096)

print(data)

s.close()


