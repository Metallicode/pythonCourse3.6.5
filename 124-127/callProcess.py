from multiprocessing import Process, current_process
import emptyProcess


if __name__ == "__main__":
      p = Process(target=emptyProcess.worker)
      p.start()
      print(p.pid)
      print(current_process().pid)
      input()
      p.terminate()
