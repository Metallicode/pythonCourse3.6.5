###first class functions

###normal func
def a_func():
      print("I'm a first class function!")

#All functions in Python are first-class functions (instance of object, can be passed as variables)
print(isinstance(a_func, object))


###we can send functions as arguments
def function_caller(func):
      func()

###look mom - no parentheses!
#function_caller(a_func)

###and return functions from other functions
def return_a_func(func):
      return func

###return a function to a variable
#x = return_a_func(a_func)
###call returnd function
#x()


###define a func inside a func and return it
def func_with_inner_func():
      def inner_func():
            print("this is printed from the inner func")
      return inner_func
            
#x = func_with_inner_func()
#x()


###same, but with argument
def func_with_inner_func2(message):
      def inner_func():
            print(message)
      return inner_func
            
#x = func_with_inner_func2("a message to print")
#x()


###closure
def closure_func(message):
      messageToPrint = message
      def inner_func():
            print(messageToPrint)
      return inner_func

#x = closure_func("message to save in closure")
#x()


###sending argument to inner function in a closure
def closure_func2(message):
      messageToPrint = message
      def inner_func(value):
            print(messageToPrint, value)
      return inner_func

#x = closure_func2("this will be saved to closure variable...")
#x("and this will be sent as an argument to the inner func")


###wrapper function
def function_with_wrapper(func):
      def wrapper_func():
            print("pre func call")
            func()
            print("post func call")
      return wrapper_func

###call the func wrapper
#x = function_with_wrapper(a_func)
#x()


###normal func with arg
def func_with_arg(msg):
      print("func_with_arg prints:", msg)

###what if our func expects args?
def function_with_wrapper_args(func):
      def wrapper_func(msg):
            print("pre func call")
            func(msg)
            print("post func call")
      return wrapper_func

#x = function_with_wrapper_args(func_with_arg)
#x("this is the message")

####################################################

#function Decorators
def function_with_wrapper2(func):
      def wrapper_func():
            print("pre func call")
            func()
            print("post func call")
      return wrapper_func

#fix the problem
##def function_with_wrapper2(func):
##      def wrapper_func(*args, **kwargs):
##            print("pre func call")
##            func(*args, **kwargs)
##            print("post func call")
##      return wrapper_func

#decorator annotation
@function_with_wrapper2
def a_func2():
      print("I'm a first class function!")

#problem...
@function_with_wrapper2
def func_with_arg2(msg):
      print("func_with_arg prints:", msg)

#a_func2()
#func_with_arg2("hi")

##################################################

#we can use classes insted of functions
class class_wrapper:
      def __init__(self, func_to_wrap):
            self.func = func_to_wrap

      def __call__(self, *args, **kwargs):
            print("extending function with class")
            self.func(*args, **kwargs)


@class_wrapper
def a_func3():
      print("I'm a first class function!")

@class_wrapper
def func_with_arg3(msg):
      print("func_with_arg prints:", msg)

#a_func3()
#func_with_arg3("hooo yeah...")

##################################################

#fix
from functools import wraps

###stacked decorator
def log_function_calls(func):
      import logging
      logging.basicConfig(level=logging.INFO)
      #@wraps(func)
      def wrapper(*args, **kwargs):
            logging.info(f"function {func.__name__} called with args{args} and kwargs{kwargs}")
            return func
      return wrapper


def print_function_calls(func):
      #@wraps(func)
      def wrapper(*args, **kwargs):
            print(f"pre {func.__name__} call")
            return func
      return wrapper

@log_function_calls
@print_function_calls
def a_func4():
      print("doing work...")


