class myClass:
      """my class docString...."""
      
      classVal = 100
      classList = ["a", "b", "c"]
      
      def __init__(self):
            self.__x = 0

      def func_a(self):
            print("func_a call")
            for i in range(20):
                  pass

      def func_b(self, arg):
            print("func_b call")
            for i in range(arg):
                  print(arg)

      def func_c(self, arg, arg2):
            print("func_c call")
            for i in range(arg):
                  print(arg)

      @classmethod
      def func_d(arg):
            print("func_d call")
            for i in range(arg):
                  print(arg)

      @property
      def x(self):
            print("x prop call")
            return self.__x




if __name__ == "__main__":
      
      o = myClass()
      print("hello", o)
      
      with open(__file__) as f:
            file = f.read()

      exec(file)
