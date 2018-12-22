import datetime
import random

class MessageManager():
      def __init__(self):
            self.SaveMsg("*********Starting New Session*********")

      def SaveMsg(self, msg):
            with open("messagesLog.txt", "a") as f:
                  f.write(f"{datetime.datetime.now()} {msg}\n")

      def GetMetal(self):
            with open("metal.txt") as f:
                  lines = f.read().splitlines()
            return lines[random.randint(0, len(lines)-1)]

      def SetMetal(self, msg):
            with open("metal.txt", "a") as f:
                  f.write(f"\n{msg}")


      
      
