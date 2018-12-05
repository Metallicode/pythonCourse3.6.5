import socket
import os
import sys

def printProgress(fSize, sentVol):
      print(f"transport Progress {sentVol*(100/fSize)}%" + " "*30, end="\r") #calc % of data sent from total file size

def servClient(client, address):
      file_name = [f for f in os.listdir() if f!="metalFTP.py" and f!="run.bat"][0] #from list files in dir - look for the file to transfer
      if os.path.isfile(file_name): #make shure it's a file...
            file_size = os.path.getsize(file_name) #get the size of the file
            client.send(str(file_name + " " + str(file_size)).encode()) #send the client a message with file name & file size
            clientRes = client.recv(2)  #get conformation message
            if clientRes.decode() == 'ok': #continue if client conformation is "ok"
                  print(f"permission to send file - starting to send\n")
                  with open(file_name, 'rb') as f: #open the file
                        buffer = f.read(1024) #read buffer from file
                        data_sent = len(buffer) #get buffer size and save to data transsmition counter
                        client.send(buffer) #send bufferd data to client
                        printProgress(file_size, data_sent) #call printProgress function
                        while data_sent != file_size: #loop untill finished sending data
                              buffer = f.read(1024) #read buffer from file
                              client.send(buffer) #send bufferd data to client
                              data_sent += len(buffer) #add buffer size to transsmition counter
                              printProgress(file_size, data_sent) #call printProgress function
                        print("finished sending file!\n")
            else:
                  print(f"no permission to send file - aborting action")
      else:
            print(f"file not exist...")
            client.send(b"file not exist...") #send error to user
            
def runServer(soc):
      print("server waiting...\n")
      c,a=soc.accept()   #block code and wait for connection from client
      servClient(c,a)

def runClient(soc):
      file_description = soc.recv(1024).decode().split() #recive a file description from server, split message string
      file_size = int(file_description[1]) #get the file size
      file_name = file_description[0] #get the file name
      clientAction = input(f"file:{file_name} size: {file_size}, press enter to continue...")
      soc.send(b"ok") #send conformation message
      print(f"starting to download...\n")
      with open(file_name, 'wb') as f: #open a new file
            buffer = soc.recv(1024) #recv first buffer from server
            f.write(buffer) #write buffer to file
            data_recv = len(buffer)  #get buffer size and save to data transsmition counter
            printProgress(file_size, data_recv) #call printProgress function
            while data_recv < int(file_size): #if the file size is larger than data transsmition counter
                  buffer = soc.recv(1024) #recv next buffer from server
                  f.write(buffer) #write buffer to file
                  data_recv += len(buffer) #add buffer size to data transsmition counter
                  printProgress(file_size, data_recv) #call printProgress function
            print("file copy is ready!\n")
            
def Main():
      server = False if len([f for f in os.listdir('.') if os.path.isfile(f)])==2 else True #must have a script & run.bat file in this dir 
      port = int(sys.argv[1]) #get port val from bat file
      ip = sys.argv[2] if server else sys.argv[3] # set ip address according to role
      print(f"starting socket with server= {server}, address= {ip}:{port}\n")
      soc = socket.socket() #create socket
      if server:
            soc.bind((ip, port)) #bind server to address
            soc.listen() #start listening
            runServer(soc) 
      else:     
            if soc.connect_ex((ip, port))==0: #try connecting to server
                  runClient(soc)
            else:
                  print("can't connect.. :(")

      soc.close()
      input("ok bye!\n")
      
if __name__ == "__main__":
      print("File Transfer Script")
      Main()
