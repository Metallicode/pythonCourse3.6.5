import base64

class MCEncryptor:
      def __init__(self, passWord):
            self.__pw = passWord

            
      def cycleCypher(self, cypher):
            counter = 0
            while True:
                  yield cypher[counter]
                  if len(cypher) == counter+1:
                        counter = 0
                  else:
                        counter += 1


      @property
      def pw(self):
            return self.__pw


      def return_encrypted(self, data):
            cypher = self.cycleCypher(self.pw)
            encrypted = base64.b64encode("".join([chr(ord(data[i]) ^ ord(next(cypher))) for i in range(len(data))]).encode()).decode()
            return encrypted


      def return_decrypted(self, data):
            cypher = self.cycleCypher(self.pw)
            decodedEncryptedString = base64.b64decode(data)
            decryptedString = "".join([chr(decodedEncryptedString[i] ^ ord(next(cypher))) for i in range(len(decodedEncryptedString))])
            return decryptedString
