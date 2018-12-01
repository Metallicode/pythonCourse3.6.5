#client code:

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("xxx.xxx.xxx.xxx", 1234)) #enter server address & port number
soc.send(b"message from client")
print(soc.recv(1024))



#server code:
import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(("xxx.xxx.xxx.xxx", 1234)) #enter server address & port number
soc.listen(10)
(client, address) = soc.accept()
print(client.recv(1024))
client.send(b"message from server")
