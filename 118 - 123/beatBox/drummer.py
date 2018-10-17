import csv
import time
import threading
from playsound import playsound


def runSound(name):
      playsound(f"samples/{name}.wav")

while True:
      with open('sequenser.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                  #print(row)
                  for step in row:
                        print(step+"\t", end="")
                        s_thread = threading.Thread(target=runSound, args=(), kwargs={"name":step})
                        s_thread.start()
                        time.sleep(0.1)
                  print()
      print("next loop...")


