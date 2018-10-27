from multiprocessing import Process, Value, Lock
from time import sleep

def f(val, loc):
      for i in range(20):
            sleep(.2)
            with loc:
                  val.value +=1


if __name__ == '__main__':
      lock = Lock()
      val = Value('i', 0)
      p1 = Process(target=f, args=(val, lock))
      p2 = Process(target=f, args=(val, lock))
      p1.start()
      p2.start()
      p1.join()
      p2.join()
      print(val.value)
