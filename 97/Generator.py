def myGen():
      yield "hello from gen"

def myGen():
      for i in range(0,10):
            yield i

def myGen():
      for i in range(0,10):
            yield i

      yield "bye!"


def myGen():
      yield "yo!"
      
      for i in range(0,10):
            yield i

      yield "bye!"




import time
import sys


time01 = time.clock()

numbers = [x**2 for x in range(0, 1000)]

time02 = time.clock()


print(sys.getsizeof(numbers))

print((time02-time01)*10000)




import math

def myGenerator():
      z = 0
      while True:
            yield z
            z +=5

def sinGenerator():
      for i in range(0, 360):
            yield math.sin(math.radians(i))

def powerGenerator():
      z = 2
      while True:
            z = z**2
            yield z




      
