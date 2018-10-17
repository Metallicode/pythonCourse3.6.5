import time

##def addNumbers(n):
##      num = 0
##      for i in range(n):
##            num +=1
##      print(num)
##
##start = time.time()
##addNumbers(50000000)
##finish = time.time()
##print(finish-start)



import threading

##def addNumbers(n):
##      num = 0
##      for i in range(n):
##            num +=1
##      print(num)
##
##start = time.time()
##t1 = threading.Thread(target=addNumbers, args=(50000000//2,))
##t2 = threading.Thread(target=addNumbers, args=(50000000//2,))
##t1.start()
##t2.start()
##t1.join()
##t2.join()
##finish = time.time()
##print(finish-start)



import threading
import subprocess

def addNumbers(n):
      num = 0
      for i in range(n):
            num +=1
      print(num)

p = subprocess.Popen(['python', 'looper.py'])

start = time.time()
t1 = threading.Thread(target=addNumbers, args=(50000000//2,))
t2 = threading.Thread(target=addNumbers, args=(50000000//2,))
t1.start()
t2.start()
t1.join()
t2.join()
finish = time.time()
p.terminate()

print(finish-start)
