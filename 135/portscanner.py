#port scanner
import socket
import threading

results ={}

#thread worker
def worker(port, ip):
      soc = socket.socket()
      soc.settimeout(0.5)
      if soc.connect_ex((ip, port))==0:
            #if http
            if port ==80:
                  soc.send(b"GET / HTTP/1.0\r\n\r\n\r\n")
            results[port]=soc.recv(84).decode()
      soc.close()


ip = input("enter the ip:\n")

#run on 0-999  for port numbers
for i in range(1000):
      t = threading.Thread(target=worker, args=(i, ip))
      t.start()


for key in results:
      print(f"port {key}\t\t {results[key]}\n")
      
