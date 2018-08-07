#for homogeneous use
#immutable

#create
newTuple = 1,2,3,4
print(newTuple)
print(type(newTuple))
print("\n")

#use parentheses 
newTuple = (1,2,3,4,5,6)
print(newTuple)
print(type(newTuple))

newEmptyTuple = ()
print(type(newEmptyTuple))
print("\n")

#create with one element
newTuple = (1)
print(newTuple)
print(type(newTuple))

newTuple = (1,)
print(newTuple)
print(type(newTuple))

print("\n")


#indexing
a_tuple = ("a", "b", "c", "d")
print(a_tuple[0])
print(a_tuple[1])
print(a_tuple[2])
print("\n")

#immutable
#a_tuple[0] = 9
print("\n")

#add/mul tuples
a_tuple = ("a", "b", "c", "d")
b_tuple = ("x", "y", "z")
c_tuple = a_tuple  + b_tuple
print(c_tuple)

d_tuple = a_tuple * 5
print(d_tuple)
print("\n")

#can't del items
a_tuple = ("a", "b", "c", "d")
#del a_tuple[0]
print("\n")

#count
myTuple = (1,0,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0)
print(myTuple.count(1))
print(myTuple.count(0))
print("\n")

#index
myTuple =  ("cat","cat","dog","cat","dog","cat")
print(myTuple.index("dog"))
print("\n")

#create tuple from list
myList = [1,2,3,4]
myTuple = tuple(myList)
print(type(myTuple))
print("\n")

#sum()
print(sum(myTuple))
print("\n")

#Unpacking
tu = (1,2,3,4)
z,x,y,g = tu
print(z)
print(x)
print("\n")


lstOfTuples = [(34,5),(2,1),(45,3)]

for (a,b) in lstOfTuples:
      print(f"{a} {b}")


      

