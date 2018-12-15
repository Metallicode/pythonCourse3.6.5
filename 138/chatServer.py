import socket
import select

server = socket.socket()
server.bind(("XXX.XXX.XXX.XXX", XXXX)) 
server.listen(5)
inputs = [server]
print("starting server..")

def notify_all(msg, non_receptors):
      for connection in inputs:
            if connection not in non_receptors:
                  connection.send(msg)

def greet(client):
      names = [n.getpeername() for n in inputs if n is not client and n is not server]
      greetMsg = "hello user! \n users online: " + str(names)
      client.send(greetMsg.encode())
      
while inputs:
      readables, _, _ = select.select(inputs, [], [])
      for i in readables:
            if i is server:
                  client, address = server.accept()
                  inputs.append(client)
                  print("connected to new client")
                  greet(client)
                  notify_all(f"client {address} enterd".encode(), [server, client])
                  
            else:
                  try:
                        data = i.recv(1024)
                        notify_all(str(str(i.getpeername()) + ">>> " + data.decode()).encode(), [server, i])

                  except Exception as e:
                        print(e)
                        inputs.remove(i)
                        print(f"client {i.getpeername()} BYE")
                        notify_all(f"client {i.getpeername()} left".encode(), [server])
                        i.close()

