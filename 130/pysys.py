import sys
import ast

###python pysys.py "hello python" 345 "metallicode"
##print(sys.argv)
##print(type(sys.argv))


### Abstract Syntax Trees module
#####"[12,234,5,12,'nony', 'kobi', 2.4]"
##listFromArg = ast.literal_eval(sys.argv[1])
##print(listFromArg)
##print(type(listFromArg))

###tuple of strings giving all modules that are compiled! into this Python interpreter.
#print(sys.builtin_module_names)
#print(sys.modules.keys()) ###lists the imported modules!

###absolute path of the executable binary for the Python interpreter
#print(sys.executable)

###show in CMD 
##sys.exit()


###Return the name of the current default string encoding
#print(sys.getdefaultencoding())


###Return the reference count of the object
class T:
      val = "hello T"

t = T()
print(sys.getrefcount(t))
x = t
print(sys.getrefcount(t))
z = x
print(sys.getrefcount(t))
del x
print(sys.getrefcount(t))
print(z.val)


#sys.setrecursionlimit(100)
##print(sys.getrecursionlimit()) ### has 23 recursion frames offset

def recursiv(x):
      print(x)
      x += 1
      recursiv(x)

recursiv(0)


###Return the size of an object in bytes (not the memory consumption of objects it refers to)
##b = "x" * 100000
##s = "x" * 10
##
##print(sys.getsizeof(b))
##print(sys.getsizeof(s))

###Return a named tuple describing the Windows version currently running
#print(sys.getwindowsversion())


### platform identifier string
"""
Linux	'linux'
Windows	'win32'
Mac OS X	'darwin'
"""
#print(sys.platform)

###The C API version for this interpreter
#print(sys.api_version)

###currently running Python interpreter (obj.name .version ....)
##print(sys.implementation)

###prompt of the interpreter
##sys.ps1


###will get stuck in read mode..
#sys.stdin.read()

###like print()
##sys.stdout.write("stdout \n")
##sys.stdout.flush()
##
###like print() but in red
##sys.stderr.write("error")
##sys.stderr.flush()
