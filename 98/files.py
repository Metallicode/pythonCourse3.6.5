#read file
file = open("C:/pyFile/m.txt")
print(file.read())
file.close()

#read part of file
file = open("C:/pyFile/m.txt")
print(file.read(3))
file.close()

#read parts of file
file = open("C:/pyFile/m.txt")
print(file.read(2))
print(file.read())
file.close()

#seek to beginning of file
file = open("C:/pyFile/m.txt")
print(file.read(2))
file.seek(0)
print(file.read())
file.close()

#seek to a new location
file = open("C:/pyFile/m.txt")
print(file.read(2))
file.seek(4)
print(file.read())
file.close()


#buffer read file
file = open("C:/pyFile/m.txt")
file.seek(0,2)
length_of_file = file.tell()
print("length_of_file: ",length_of_file)
file.seek(0)
for i in range(0, length_of_file, 3):
      print(file.read(3))
file.close()



file = open("C:/pyFile/m.txt")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open("C:/pyFile/m.txt")
lines = file.readlines()
file.close()
print(lines)

file = open("C:/pyFile/m.txt")
lines = file.read().splitlines()
file.close()
print(lines)


##################

file = open("C:/pyFile/m.txt", "w")

file.close()

file = open("C:/pyFile/m.txt", "w")
file.write("test write to file")
file.close()

file = open("C:/pyFile/m.txt", "w")
file.write("test write to file")
file.write("more writing to file")
file.write("more!!!!")
file.close()

file = open("C:/pyFile/m.txt", "w")
file.write("test write to file\n")
file.write("more writing to file\n")
file.write("more!!!!\n")
file.close()

file = open("C:/pyFile/m.txt", "w")
print("test print to file", file=file)
file.close()

file = open("C:/pyFile/m.txt", "w")
print("test print to file", file=file)
print("no new line problem!", file=file)
file.close()

###################

file = open("C:/pyFile/m.txt", "a")
print("test append print to file", file=file)
file.close()

#####################

file = open("C:/pyFile/m.txt", "r+")
file.truncate(6)
print(file.read())
file.close()

####################


with open("C:/pyFile/m.txt", "a") as f:
      f.write("test with WITH syntax")

with open("C:/pyFile/m.txt", "r") as f:
      fileStr = f.read()


print(fileStr)
print(f)
f.read()



