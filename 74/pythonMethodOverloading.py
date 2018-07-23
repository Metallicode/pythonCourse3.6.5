class test:
      def __init__(self):
            print(f"testing class: {type(self).__name__}")

class test1(test):
      def func(self, num):
            print("func(self, num)")
            
      def func(self):
            print("func(self)")


class test2(test):
      def func(self, num = None):
            if num == None:
                  print("func(self)")
            else:
                  print("func(self, num)")
                  
            
t2 = test2()
t2.func()
t2.func(9)



