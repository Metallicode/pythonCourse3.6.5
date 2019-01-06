import gc

class bigObj():
      def __init__(self):
            self.value = "x"*10000000


##def gcRunning(v, x):
##      print("gc is running..")
##      print(v)
##      print(x)
##
##
##gc.disable()
##gc.isenabled()
##gc.enable()
##gc.callbacks.append(gcRunning)
##print(gc.get_objects())
##states every collection as dict with {how many collections were made, number of objects collected, uncollectable}
##print(gc.get_stats())
##collection counts of each generation
##print(gc.get_count())
##gc.collect()
##print(gc.get_count())


