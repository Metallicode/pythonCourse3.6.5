import time

#low-level, old & deprecated 'thread' for module backwards incompatibilities in Python3
#threading module provides an easier to use and higher-level threading API built on top of this module
from _thread import start_new_thread, allocate_lock

def calculateSum(n):
      sumOfNumbers = 0
      for i in range(n):
            sumOfNumbers += 1
      return sumOfNumbers

#regular function call
#x = calculateSum(10000)

#return its identifier
x = start_new_thread(calculateSum, (10000,))


#this will help
#time.sleep(3)

print(x)


####################################################################

### a different way...

###define variable outside the worker function
##sumOfNumbers = 0
##
##def calculateSum(n):
##      ###use global to referance var within function
##      global sumOfNumbers
##      for i in range(n):
##            sumOfNumbers += 1
##      #print("finished working..")
##      print(sumOfNumbers)
##
###Start The thread
##start_new_thread(calculateSum, (10000,))
##
###wait for calc to finish
##time.sleep(3)
##
###print result.... better... i guess
##print(sumOfNumbers)


################################################################

###more then one thread problem
##
##sumOfNumbers = 0
##
##def calculateSum(n):
##      global sumOfNumbers
##      for i in range(n):
##            sumOfNumbers += 1
##      print(sumOfNumbers)
##      
##
#####Start The threads
##start_new_thread(calculateSum, (1000000//2,))
##start_new_thread(calculateSum, (1000000//2,))
##
###calculateSum(1000000)
##
#####THIS IS A MESS!
##
###give time for calculations...
##time.sleep(3)



######################################################

the lock idea

lock = allocate_lock()
sumOfNumbers = 0

def calculateSum(n):
      global sumOfNumbers
      for i in range(n):
            #close lock
            lock.acquire()
            sumOfNumbers += 1
            #open lock
            lock.release()


###Start The threads
start_new_thread(calculateSum, (1000000//2,))
start_new_thread(calculateSum, (1000000//2,))

#give time for calculations...
time.sleep(3)

#working, but this is really evil
print(sumOfNumbers)







