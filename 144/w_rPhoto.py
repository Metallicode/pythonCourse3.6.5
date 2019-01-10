import weakref
from PIL import Image

cache = weakref.WeakValueDictionary()

while True:
      selected_pic = input("enter pic name to open: ")
      if selected_pic in cache.keys():
            print("in cache!")
            cache[selected_pic].show()
      else:
            pic = Image.open(f"images/{selected_pic}.jpg")
            pic.show()
            cache[selected_pic]=pic
      
      
