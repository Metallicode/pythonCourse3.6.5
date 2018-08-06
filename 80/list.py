#ordered
#changeable
#Allows duplicate

#create list
list_a = []
list_b = [1,2,3]
list_c = [4,5,6,"banana", "apple"]
list_d = list()

print(f"{list_a} \t\t\t {type(list_a)}")
print(f"{list_b} \t\t\t {type(list_b)}")
print(f"{list_c} \t {type(list_c)}")
print(f"{list_d} \t\t\t {type(list_d)}")

print("\n")

#index into list (zero-indexed)
list_a = ["banana", "tapoz", "melon"]
print(list_a[0])
print(list_a[1])
print(list_a[2])
#last element (reverse indexing)
print(list_a[0])
print(list_a[-1])
print(list_a[-2])

print("\n")

#change element
print(list_a[0])
list_a[0] = "tzabar"
print(list_a[0])

print("\n")


#add (concate)
newList = list_a + list_b
print(newList)
#extend()
list_b.extend(list_a)
print(list_b)
print("\n")



#slice list
list_a = [0,1,2,3,4,5,6,7,8,9]
print(list_a[3:6])
print(list_a[:6])
print(list_a[3:])
print(list_a[3:-2])
print(list_a[::2])
print(list_a[::3])
print(list_a[::-1])
print(len(list_a))
list_from_lists = list_a[1:2] + list_a[::-1] + list_a[1: -3] 
print(list_from_lists)

print("\n")


#create list with range()
listFromRange = list(range(20))
print(listFromRange)
listFromRange = list(range(5,20))
print(listFromRange)
listFromRange = list(range(5,30,3))
print(listFromRange)

print("\n")


#working with objects
class myNewClass:
      def __init__(self, num):
            self.num = num

      def printnum(self):
            print(f"my num is: {self.num}")

      def __repr__(self):
            return f"myNewClass({self.num})"


listOfObj = []

for i in range(0, 20):
      listOfObj.append(myNewClass(i))

print(listOfObj)

for i in listOfObj:
      i.printnum()

print("++++++++++++++\n" )


#insert()
list_a = [0,1,2,3,4]
print(list_a)
list_a.insert(0, "banana")
print(list_a)
list_a.insert(10, "banana")
print(list_a)
print(len(list_a))

print("\n")


#remove()
list_a.remove(1)
print(list_a)
#list_a.remove(1)

#pop()
index = 0
print(list_a.pop(index))
print(list_a)
del list_a[-1]
print(list_a)
print("\n")

#clear()
list_a.clear()
print(list_a)
print("\n")

#index()
anim_list = ["bear", "cat", "horse", "pig", "dog", "dog"]
print(anim_list.index("cat"))
print(anim_list.index("dog"))
#print(anim_list.index("stone"))
print("\n")

#count()
print(anim_list.count("dog"))
print("\n")

#sort()
num_list = [2,5,4,6,7,8,7,45,6,345,45,5]
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)

anim_list = ["bear", "cat", "horse", "pig", "dog", "dog"]
print(anim_list)
anim_list.sort(key=len)
print(anim_list)
newlist = sorted(anim_list)
print(newlist)
print("\n")

#reverse()
newlist.reverse()
print(newlist)
print("\n")


#copy()
list_a = [0,1,2,3]
list_b = list_a
list_a.append(99)
print(list_a)
print(list_b)

list_c = list_a.copy()
list_a.append(999)
print(list_a)
print(list_b)
print(list_c)


#split string
mystr = "this is a long string. it has meny words"
newlst = mystr.split(" ")
print(newlst)



