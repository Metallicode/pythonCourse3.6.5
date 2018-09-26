import base64

def cycleCypher():
      counter = 0
      while True:
            yield cypher[counter]
            if len(cypher) == counter+1:
                  counter = 0
            else:
                  counter += 1

def setFileName():
      global fileName
      fileName = input("enter file name to encrypt..\n")

def setCypher():
      global cypher
      cypher = input("enter cypher string..\n")

def getData(operation):
      global data
      try:
            if operation == "encrypt":
                  with open(fileName, "r") as f:
                        data = f.read()
            elif operation == "decrypt":
                  with open(fileName, "rb") as f:
                        data = base64.b64decode(f.read())
            else:
                  print("operation not supported")
                  
      except :
            print("problem finding file", fileName)
            data = None

def encryptData():
      global Encrypted
      if data is not None:
            cy = cycleCypher()
            Encrypted = base64.b64encode("".join([chr(ord(data[i]) ^ ord(next(cy))) for i in range(len(data))]).encode())
                                             
def fileHandler(operation):
      if data is not None:
            if operation == "encrypt":
                  with open("secret", "wb") as f:
                        f.write(Encrypted)
            elif operation == "decrypt":
                  with open("readable.txt", "w") as f:
                        f.write(decrypted)
            
def decryptData():
      global decrypted
      if data is not None:
            cy = cycleCypher()
            print(data)
            decrypted = "".join([chr(data[i] ^ ord(next(cy))) for i in range(len(data))])




                                             
setFileName()
setCypher()
getData("encrypt")
encryptData()
fileHandler("encrypt")

should_script_continue = input("continue to decrypt file?")

if should_script_continue:
      setFileName()
      setCypher()
      getData("decrypt")
      decryptData()
      fileHandler("decrypt")   






