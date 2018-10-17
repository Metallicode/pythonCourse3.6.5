import threading

###BASIC THREADING

###a worker function
##def worker():
##    print("hello threading")
##    ##print(threading.current_thread())
##
#####create a new thread
##t1 = threading.Thread(target=worker)
####t2 = threading.Thread(target=worker)
##
#####run thread
##t1.start()
####t2.start()
##
##
#####THREADING MODULE
#####count active threads
##print(threading.active_count())
##print(threading.main_thread())
##                                 
#####get current thread info
##print(threading.current_thread())
##print(threading.get_ident())
##print(t1.name)
##
#####enumerate all active threads
##threads = threading.enumerate()
##for i in threads:
##    print(i)





###Thread-Local Data
##def worker(val):
##    mydata = threading.local()
##    print(mydata)
##    mydata.x = 0
##    for i in range(val):
##        mydata.x += 1
##    print(str(mydata.x)+"-->"+str(threading.current_thread())+"\t")
##    
##t1 = threading.Thread(target=worker, args=(2,))
##t2 = threading.Thread(target=worker, args=(4,))
##t1.start()
##t2.start()





###THREAD OBJECT
###threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
##
#####no ctor version
##class myWorker_no_ctor(threading.Thread): 
##    def run(self):
##        print("doing work...")
##
#####ctor version
##class myWorker(threading.Thread):
##    def __init__(self, target, *args):
##        self.target = target
##        print(self.target)
##        threading.Thread.__init__(self)
## 
##    def run(self):
##        self.target()
##
#####a callable object
##class callableObj:
##    def __call__(self):
##        print("hello from callable obj!")
##
#####use thread instance
##t1 = myWorker_no_ctor()
##t1.start()
##
##co = callableObj()
##t2 = myWorker(co)
##t2.start()




###daemon threads (use CMD)
##when your program quits, any daemon threads are killed automatically.
##def sleepyWorker():
##    import time
##    time.sleep(2)
##    print("hello")
##
##
###t1 = threading.Thread(target=sleepyWorker, daemon=True)
##t1 = threading.Thread(target=sleepyWorker)
##t1.start()





###JOIN
##import time
##
##def worker():
##    print("hello from thread", repr(threading.current_thread()))
##    time.sleep(2)
##    print("still working...")
##    time.sleep(2)
##    print(repr(threading.current_thread()), "finished")
##
##t1 = threading.Thread(target=worker)
###t2 = threading.Thread(target=worker)
##t1.start()
###t1.join()
##
#####with timeout (just wait - don't kill thread)
##t1.join(timeout=1.5)
#####check if thread is still alive
###print(t1.is_alive())
##
###t2.start()
###t2.join()
##
##print("program finished!")




###LOCK OBJECT
##import time
##
##class myThread (threading.Thread):
##    def __init__(self, target, name, counter):
##        threading.Thread.__init__(self)
##        self.name = name
##        self.counter = counter
##        self.target = target
##      
##    def run(self):
##        print ("Starting " + self.name)
##        #lock (using context manager instead of acquire & release)
##        with threadLock:
##            self.target(self.name, self.counter, 3)
##
##def print_time(threadName, delay, counter):
##    while counter:
##        time.sleep(delay)
##        print (f"{threadName}, {time.ctime(time.time())}")
##        counter -= 1
##
##threadLock = threading.Lock()
##
##t1 = myThread(print_time, "Thread-1", 1)
##t2 = myThread(print_time, "Thread-2", 2)
##t1.start()
##t2.start()
##
##t1.join()
##t2.join()
##
##print ("Exiting Main Thread")





###Timer Objects
##def hello():
##    print("hello, world")
##
##t = threading.Timer(3.0, hello)
##t.start()
###t.cancel()
##
##print("yo!")

