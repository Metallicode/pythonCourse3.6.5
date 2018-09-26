import base64
cypher = 123

def cycleCypher(cypher):
      counter = 0
      while True:
            yield cypher[counter]
            if len(cypher) == counter+1:
                  counter = 0
            else:
                  counter += 1


#normal string
stringToEncrypt = "this is a normal string"
print("normal string: ", stringToEncrypt)



#####special cypher
####cypher = cycleCypher("password")
#####xor the string
####encrypted = "".join([chr(ord(stringToEncrypt[i]) ^ ord(next(cypher))) for i in range(len(stringToEncrypt))])
####print("encrypted string: ", encrypted)



#xor the string
encrypted = "".join([chr(ord(stringToEncrypt[i]) ^ cypher) for i in range(len(stringToEncrypt))])
print("encrypted string: ", encrypted)

#encode the encrypted string to a byte string
encodedEncrypted = encrypted.encode()
print("encodedEncrypted string: ", encodedEncrypted)

#encode the byte string a base64 byte string
base64encodedEncrypted = base64.b64encode(encodedEncrypted)
print("base64encodedEncrypted string: ", base64encodedEncrypted)

#decode the byte string to a normal (cypherd) string (ready to save)
base64encodedEncryptedEncoded = base64encodedEncrypted.decode()
print("base64encodedEncryptedEncoded string: ", base64encodedEncryptedEncoded)


###one liner
##base64encodedEncryptedEncoded = base64.b64encode("".join([chr(ord(stringToCypher[i]) ^ cypher) for i in range(len(stringToCypher))]).encode()).decode()
##print("encrypted string: ", base64encodedEncryptedEncoded)
##

######################################################################


#decode the encrypted string
decodedEncryptedString = base64.b64decode(base64encodedEncryptedEncoded)
print("decodedEncryptedString: ", decodedEncryptedString)



#####special cypher
####cypher = cycleCypher("password")
#####xor the string
####decryptedString = "".join([chr(decodedEncryptedString[i] ^ ord(next(cypher))) for i in range(len(decodedEncryptedString))])
####print("decryptedString: ", decryptedString)

#xor the string
decryptedString = "".join([chr(decodedEncryptedString[i] ^ cypher) for i in range(len(decodedEncryptedString))])
print("decryptedString: ", decryptedString)








