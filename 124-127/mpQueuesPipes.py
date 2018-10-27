from multiprocessing import Process, Queue, Pipe


##def worker(q):
##      q.put(["spam",5])
##      while not q.empty():
##            pass
##      while q.empty():
##            pass
##      print(q.get())
##
##def worker_b(q):
##      ###block is True (the default)
##      print(q.get())
##      q.put(["OK", 1000])


def pipe_worker_a(p):
      x = ["data", "more data", 123]
      p.send(x)
      new_data = p.recv()
      print(new_data)

def pipe_worker_b(p):
      data = p.recv()
      print(data)
      new_data = ["from b to a", 321]
      p.send(new_data)

if __name__ == '__main__':
      ###the queue object
##      q = Queue()
##      
##      process_a = Process(target=worker, args=(q,))
##      process_b = Process(target=worker_b, args=(q,))
##      
##      process_a.start()
##      process_b.start()
##
##      process_a.join()
##      process_b.join()




      ###the pipe object
      ###duplex is True (the default) - else,  conn1 can only receive, conn2 can only send
      conn1, conn2 = Pipe()
      process_a = Process(target=pipe_worker_a, args=(conn1,))
      process_b = Process(target=pipe_worker_b, args=(conn2,))
      
      process_a.start()
      process_b.start()

      process_a.join()
      process_b.join()
