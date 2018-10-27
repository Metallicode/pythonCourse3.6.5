import multiprocessing 
import time
import random

def worker(d):
      d[multiprocessing.current_process().pid] = random.random() 


if __name__ == "__main__":
      with multiprocessing.Manager() as m:
            d = m.dict()
            p1 = multiprocessing.Process(target=worker, args=(d,))
            p2 = multiprocessing.Process(target=worker, args=(d,))
            p1.start()
            p2.start()
            p1.join()
            p2.join()
            print(d)

      
