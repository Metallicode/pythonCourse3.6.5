##PIL
from PIL import Image
import random


def r():
      return random.randint(0,255)

im = Image.new('RGB', (1000, 1000))

list1 = [(r(),r(),r()) for i in range(0,1000000)]
list1.sort()

im.putdata(list1)
im.show()
