from collections import deque
class musicScale:    
      def __init__(self, tonic):
            self.tonic =  tonic

      @property
      def scale(self):
            x = deque("ABCDEFG")
            x.rotate(65 - ord(self.tonic))
            return list(x)

      def __iter__(self):
            self.noteCounter = 0
            return self

      def __next__(self):
            if self.noteCounter < len(self.scale):
                  self.noteCounter += 1
                  return self.scale[self.noteCounter-1]
            else:
                  raise StopIteration


m = musicScale("G")
print(m.scale)






for i in m:
      print(i)





