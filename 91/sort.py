charList = ["a", "z", "x", "b", "r", "e"]

print(charList)

charList.sort()

print(charList)
charList.sort(reverse=True)
print(charList)


def sortKey(x):
      return x[1]

tupleList = [("bob", 4),("bill", 8),("john", 3),("mary", 7)]
print(tupleList)
tupleList.sort()
print(tupleList)
tupleList.sort(key=sortKey)
print(tupleList)

lst = [1,5,4,6,7,7,6,5,3,8,78,46,24,7,456,8,6]

sLst = sorted(lst)

print(sLst)


mYdi = {3:"c",2:"b",1:"a",6:"e",5:"d"}
#mYdi.sort()
#print(sorted(mYdi.values()))

sortedD = dict([(x, mYdi[x]) for x in sorted(mYdi)])
print(sortedD)
      
      



