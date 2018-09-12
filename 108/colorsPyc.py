import json
from PIL import Image

#open json data
with open("colors.json", "r") as f:
      json_data = json.load(f)

#prompt user 
selectedcolor1 = input("please, enter first color name: \n")
selectedcolor2 = input("please, enter a second color name: \n")

#convert json data from list to tuple
colorValues1 = tuple(json_data[selectedcolor1])
colorValues2 = tuple(json_data[selectedcolor2])

#create basic image frame
im= Image.new('RGB', (200, 200))

#create new list
newImage = []

#scale func from color a to b 
def scaleFader(j, indx):
      return int((((j ) * (colorValues2[indx] - colorValues1[indx])) / (200 - 0)) + colorValues1[indx])

#create image row by row
for i in range(200):
      newImage += [ (scaleFader(j,0),scaleFader(j,1),scaleFader(j,2),1) for j in range(200)]

#make image
im.putdata(newImage)

#show it
im.show()
