from abc import ABC, abstractmethod

#abstract class
class monkey_maker(ABC):
      def __init__(self):
            print(f"creating class {type(self).__name__}")

      @abstractmethod
      def createamonkey(self):
            pass

#concrete classes 
class cement_monkey_maker(monkey_maker):
      def createamonkey(self):
            print("cement monkey...")

class metal_monkey_maker(monkey_maker):
      def createamonkey(self):
            print("metal monkey...")

class sand_monkey_maker(monkey_maker):
      def createamonkey(self):
            print("sand monkey...")

class cookie_monkey_maker(monkey_maker):
      def createamonkey(self):
            print("cookie monkey...")

ceme = cement_monkey_maker()
meta = metal_monkey_maker()
sand = sand_monkey_maker()
cook = cookie_monkey_maker()


for i in (ceme, meta, sand, cook):
      i.createamonkey()









      
