##for i in range(0,10):
##      print((lambda x : x*x+5)(i))

##myList = [1,2,3,4,5,6,7,8,9]
##
##def isLessThen(x):
##      return x < 5
##
##filterdList = filter(isLessThen, myList)
##
##
##
##filterdList = filter(lambda x : x < 5, myList)
##print(list(filterdList))
##
##

strList = [ "bili bob", "sami man", "togo geresh", "miri miri", "bela katia", "dodo ronen","fredi aba"]

strList.sort(key=lambda x: x.split(" ")[1])

print(strList)

##
##
##
##def calcFunc(x):
##      return x[0]**2+x[1]

##tupList = [(1,2),(5,2),(2,5),(6,1),(2,3)]
##
##newList = list(map(calcFunc, tupList))
##
##
##
##newList = list(map(lambda x: x[0]**2+x[1], tupList))
##print(newList)

##def dynamicFunc(val):
##      return lambda x: x*val
##
##multiplier_4 = dynamicFunc(4)
##multiplier_5 = dynamicFunc(5)
##multiplier_6 = dynamicFunc(6)
##
##print(multiplier_4(1),multiplier_4(2), multiplier_4(3))
##print(multiplier_5(1),multiplier_5(2), multiplier_5(3))
##print(multiplier_6(1),multiplier_6(2), multiplier_6(3))
##
