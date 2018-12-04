#TCP server code:
import socket

soc = socket.socket()
soc.bind(("", )) #enter server address & port number
soc.listen(10)
(client, address) = soc.accept()
print(client.recv(1024))
print(string)
client.close()
soc.close()

#UDP server code:
import socket

soc = socket.socket(type=socket.SOCK_DGRAM)
soc.bind(("", )) #enter server address & port number
data, address = soc.recvfrom(1024)
print(data)
client.close()
soc.close()

#client code:
import socket
##soc = socket.socket(socket.SOCK_STREAM) #TCP
##soc = socket.socket(socket.SOCK_DGRAM) #UDP
soc.connect(("", )) #enter server address & port number
soc.send(b"message from client")
soc.close()
