def beautyPrint(val):
      print(f"so beautiful {val}!")

##create list
myFruits = ["rimon", "melon", "tapoz", "shezif", "banana"]

##create map obj
myMap = map(beautyPrint, myFruits)

##next
next(myMap)
next(myMap)
next(myMap)
next(myMap)
next(myMap)
##StopIteration
#next(myMap) 
print("\n")

def add_5_to_Items(a):
      return a + 5

myNumList = [23,4,5,56,43,2,122]

newListAfterMap = list(map(add_5_to_Items,myNumList))

print(myNumList)
print(newListAfterMap)
print("\n")


#more args
def add_values(a,b):
      return a + b


list_01 = ["bob", "joe", "bill"]
list_02 = ["mob", "go", "shmill"]

new_list = list(map(add_values, list_01, list_02))
print(new_list)

