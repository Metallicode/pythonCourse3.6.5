#server code:
import socket
import os

with socket.socket() as soc:
      soc.bind(("192.168.1.14", 1234))
      soc.listen()
      print("server listening")
      client, address = soc.accept()
      print("connected! starting to transfer file..")
      
      ##file transfer
      with open("test.txt", "rb") as f:
            file_size = os.path.getsize("test.txt")
            client.send(str(file_size).encode())
            buffer = f.read(256)      
            client.send(buffer)
            total_sent = len(buffer)
            while total_sent<file_size:
                  buffer = f.read(256)      
                  client.send(buffer)
                  total_sent += len(buffer)

      print("file transferd! bye!")

input()

##################################

#client code:
import socket
import os

with socket.socket() as soc:
      soc.connect(("192.168.1.14", 1234))
      
      ##file transfer
      with open("test.txt", "wb") as f:
            file_size = int(soc.recv(1024).decode())
            total_sent = 0    
            while total_sent<file_size:
                  buffer = soc.recv(256)      
                  f.write(buffer)
                  total_sent += len(buffer)

      print("file transferd! bye!")

input()
      




      
