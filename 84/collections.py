from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import deque
from collections import namedtuple

###################################################################

def testDefaultdict():
      ##defaultdict
      # do not need to check whether a key is present
      # uniqe keys
      # ctor (defaultdict(list)) to set value policy (list/int/set)

      #int sum
      myStr = "this is a collection of characters"
      myDefDict = defaultdict(int)
      for i in myStr:
            myDefDict[i] += 1

      print(myDefDict.items())
      print("\n")


      #list append
      myListOfFruits = [("banana", 2), ("apple", 1), ("tamar", 4), ("banana", 3), ("melon", 2), ("apple", 6)]
      newDefDict = defaultdict(list)
      for i, j in myListOfFruits:
            newDefDict[i].append(j)

      print(newDefDict.items())
      print(newDefDict["banana"])

      print(type(newDefDict))

      print("\n")


      #list in list
      myDict = defaultdict(dict)

      myDict["newKey"]["sec_new_key"] = "value"
      print(myDict.items())

      #this rasies error:

      ##regularDict = {}
      ##regularDict["newKey"]["sec_new_key"] = "value"
      ##print(regularDict.items())
      print("\n")

testDefaultdict()
      
###################################################################


def testOrderedDict():
      ##OrderedDict

      #this didn't work before....
      regularDict = {}
      regularDict["a"] = "joe"
      regularDict["b"] = "bob"
      regularDict["c"] = "bill"
      regularDict["d"] = "ron"
      regularDict["e"] = "hob"
      regularDict["f"] = "noob"
      
      orderedDict = OrderedDict()
      orderedDict["a"] = "joe"
      orderedDict["b"] = "bob"
      orderedDict["c"] = "bill"
      orderedDict["d"] = "ron"      
      orderedDict["e"] = "hob"
      orderedDict["f"] = "noob"
      
      for i, j in regularDict.items():
            print(j)

      for i, j in orderedDict.items():
            print(j)

      print("\n")

      orderedDict.move_to_end("a")
      #regularDict.move_to_end("a")

      print(orderedDict.items())
      print("\n")

      #compair dicts
      dic_a = {}
      dic_b = {}

      dic_a["a"] = "val_01"
      dic_a["b"] = "val_02"      
      dic_a["c"] = "val_03"      

      dic_b["c"] = "val_03"
      dic_b["b"] = "val_02"      
      dic_b["a"] = "val_01"

      print(dic_a ==  dic_b)
      

      dic_a = OrderedDict()
      dic_b = OrderedDict()

      dic_a["a"] = "val_01"
      dic_a["b"] = "val_02"      
      dic_a["c"] = "val_03"      

      dic_b["c"] = "val_03"
      dic_b["b"] = "val_02"      
      dic_b["a"] = "val_01"

      print(dic_a ==  dic_b)
      print("\n")
      
#testOrderedDict()
      
###################################################################


def testCounter():
      
      ##counter

      myCounter = Counter("we can create a counter from a string")
      print(type(myCounter))
      print(myCounter.items())
      print(myCounter["z"])
      newCounter = Counter("zzz")
      combinedCounter = myCounter + newCounter
      print(combinedCounter.items())
      print(list(combinedCounter.elements()))
      print(combinedCounter.most_common(5))
      combinedCounter.subtract(combinedCounter)
      print(combinedCounter.items())
      print("\n")

#testCounter()
###################################################################

def testDeque():
      
      ##deque
      ##double-ended queue
      newDeque = deque()
      newDeque.append(1)
      newDeque.append(2)
      newDeque.append(3)
      print(newDeque)
      newDeque.appendleft(4)
      newDeque.appendleft(5)
      print(newDeque)
      newDeque.extend([5,6,7])
      print(newDeque) 
      newDeque.extendleft([5,6,7])
      print(newDeque)
      print(newDeque.pop())
      print(newDeque) 
      print(newDeque.popleft())
      print(newDeque)
      newDeque.reverse()
      print(newDeque)      
      print("\n")
      newDeque.rotate(1)
      print(newDeque) 
      newDeque.rotate(1)
      print(newDeque)
      newDeque.rotate(1)
      print(newDeque)
      newDeque.rotate(-1)
      print(newDeque)      
      print("\n")


#testDeque()

###################################################################

def testnamedtuple():

      ##namedtuple
      #immutable
      #lightweight object types

      myNamedTuple = namedtuple("myNamedTuple", "name age x y")
      t1 = myNamedTuple("bob", 12, 100, 200)
      t2 = myNamedTuple("bill", 32, 300, 600)
      t3 = myNamedTuple("john", 2, 400, 400)

      print(t1.name)
      print(t1.age)
      print(t1.x)
      print(t1.y)
      
#testnamedtuple()

      
