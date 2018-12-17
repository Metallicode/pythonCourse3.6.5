import socket

c = socket.socket()
c.connect(("XXX.XXX.XXX.XXX", XXXX))

while True:
    print(c.recv(126).decode())
