from functools import reduce

def calcVectorFunc(a,b):
      return (a * b) + (56 / 5)

myList = [1,2,3,4,5]
product = reduce(calcVectorFunc, myList)
print(product)


