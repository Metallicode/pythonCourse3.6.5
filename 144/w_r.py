import weakref

##sRef = 5
##sRef = 5.5
##sRef = "hello"

class myClass:
      pass

def callback(v):
      print(f"obj ref dead {v}");

sRef = myClass()



##will create the same obj X3...
##f1= weakref.ref(sRef)
##f2= weakref.ref(sRef)
##f3= weakref.ref(sRef)

##will create differnt obj because the callback 
f1= weakref.ref(sRef, callback)
f2= weakref.ref(sRef, callback)
f3= weakref.ref(sRef, callback)

prox1 = weakref.proxy(sRef)

print(type(sRef))
print(type(prox1))
print(type(f1))

##del sRef

print(sRef.__weakref__)
##print(weakref.getweakrefcount(sRef))
print(f1)
print(f2)
print(f3)
print(prox1.val)

print(weakref.getweakrefcount(sRef))
print(weakref.getweakrefs(sRef))
##
##print(wr)
##print(wr().val)



