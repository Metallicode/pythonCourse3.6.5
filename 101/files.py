#basic wave lib
import wave

#open file object
file = wave.open("path/to/your/file/file.wav", "rb")

#print obj
print(file)

#obj attr
print(file.getnchannels())
print(file.getsampwidth())
print(file.getframerate())
print(file.getnframes())
print(file.getcomptype())

#getparams (tuple )
print(file.getparams())


#read
##print(file.readframes(5))

###buffer read
##bufferSize = 100
##for i in range(0,file.getnframes(),bufferSize):
##      print(file.readframes(bufferSize))

#rewind (set file pointer to 0)
file.rewind()

#seek file pointer
file.setpos(40)
file.readframes(5)

#tell
print(file.tell())

#close file
file.close()


#####################################


#write 
file = wave.open("path/to/your/file/file.wav", "wb")

#crop file
fileSource = wave.open("path/to/your/file/file.wav", "rb")
fileSource.setpos(5000)
data = fileSource.readframes(4000)


#strech (same pitch)
##data = fileSource.readframes(1)
##bufferSize = 1000
##for i in range(0,fileSource.getnframes(),bufferSize):
##      segment = fileSource.readframes(bufferSize)
##      for j in range(0, 8):
##            data += segment




#clouse source
fileSource.close


#set attr
file.setnchannels(2)
file.setsampwidth(2)
file.setframerate(44100)

nFrames = len(data)
file.setnframes(nFrames)
file.setcomptype('NONE',"not compressed")


#write after set...
#data = data*20
file.writeframes(data)


###make some noise
##import struct
##import random
##audio = [random.uniform(-1.0, 1.0) for x in range(nFrames)]
##
##
###Write data
##for sample in audio:
##      file.writeframes(struct.pack('h', int( sample * 32767.0 )))

#close file
file.close()















