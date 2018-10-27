import multiprocessing
import time


###POOLING
def worker(x):
      print(f"{x} {multiprocessing.current_process().name}  {multiprocessing.current_process().pid}")
      time.sleep(0.2)
      return x*2

def worker_args(*x):
      print(f"{x} {multiprocessing.current_process().name}  {multiprocessing.current_process().pid}")
      time.sleep(1)
      return x*2

def worker_with_more_args(x, y, z):
      print(f"{x} {y} {z}  {multiprocessing.current_process().name}  {multiprocessing.current_process().pid}")
      time.sleep(0.2)
      return x*2

def init_func():
      print("this is the init func printing!")
      print(multiprocessing.current_process())



###a must for multiprocessing
if __name__ == '__main__':
      #If processes is None then the number returned by os.cpu_count() is used
##      with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
      with multiprocessing.Pool(multiprocessing.cpu_count(), initializer=init_func) as p:

            ###pool apply (one process only, func with *args, returns result and blocks execution)
##            res = p.apply(worker_args,range(0,10))
##            print(res)

            ### async apply:
##            def async_func(*args):
##                  print("worker callback!" + str(args))
##            
##            res = p.apply_async(worker_args,range(0,10), callback=async_func)
##            print(res)
##            res.wait()
##            print(res.ready())
##            print(res.get())

            ###MAP
            p.map(worker,range(0,10))
##            p.map(worker,range(0,100), chunksize=10)
            
            ###with result 
##            res = p.map(worker,range(0,100), chunksize=10)
            
            ###puts a tuple in x - missing 2 required positional arguments: 'y' and 'z'
##            res = p.map(worker_with_more_args,[(1,2,3),(4,5,6),(7,8,9)], chunksize=10)

            ###starmap - unpack tuple to args
##            res = p.starmap(worker_with_more_args,[(1,2,3),(4,5,6),(7,8,9)])       
##            print("the results: " , type(res) , res)

            
            print("just a print statement..")
