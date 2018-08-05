#no duplicates
#unorderd
#unindexed
#unmutable items


##create
newSet = {1,2,3,4}
secSet = {1,2,3,4,5,6,7,8,9,8,7,6,5,4}

print(newSet)
print(secSet)


##create from list
setFromList = set([1,2,3,4,3])

print(type(newSet))


##create empty
emptySet = {}
##dic
print(type(emptySet))


##set
emptySet = set()
print(type(emptySet))


##Iterating Through a Set
for i in secSet:
      print(i)


##Membership Test
print(2 in secSet)


##add item
newSet.add(2)
newSet.add(3)
newSet.add(3)
print(newSet)


##add items from lists, sets...
newSet.update([1,2,3,3,2], {5,6,9,99}, (2,567,4,32))
print(newSet)


##remove item no error
newSet.discard(1)
newSet.discard(4)
print(newSet)


##remove item with error
newSet.remove(9)
emptySet.remove(10)
print(newSet)


##pop
print(newSet.pop())
print(newSet.pop())
print(newSet.pop())
print(newSet.pop())
print(newSet)


##clear
print(newSet)
newSet.clear()
print(newSet)


##Python Set Operations
set_a = {5,6,7,8,9,10}
set_b = {7,8,9,10,3,9, 45}


print(set_a)
print(set_b)


##Union
print(set_a | set_b)


##Intersection
print(set_a & set_b)


##Difference
print(set_a - set_b)
print(set_b - set_a)


##Symmetric Difference
print(set_a ^ set_b)


##difference_update()
set_a.difference_update(set_b)
print(set_a)
print(set_b)


##disjoint()
set_a = {1,2,3}
set_b = {4,5,6}

print(set_a.isdisjoint(set_b))
set_a.add(6)
print(set_a.isdisjoint(set_b))


##is subset/superset
set_a = {1,2,3}
set_b = {1,2,3,4,5,6}

print(set_a.issubset(set_b))
set_a.add(7)
print(set_a.issubset(set_b))
set_a.discard(7)
print(set_b.issuperset(set_a))


##length
print(len(set_a))
print(len(set_b))


##min/max
print(min(set_b))
print(max(set_b))


##new sorted list
set_b.add(-1)
set_b.add(-5)
set_b.add(67)
print(set_b)
sortedListFromSet = sorted(set_b)
print(sortedListFromSet)
print(type(sortedListFromSet))


##sum
print(sum(set_b))

