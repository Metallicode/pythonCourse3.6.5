#imports
from inmate import Inmate
from warden import Warden
from prison import Prison
from prisonBlock import PrisonBlock

from setupHelper import createInmates

#create chief warden
w = Warden("Leo", "Glynn", 6546876, 100)

#create prison
oz = Prison("Oz", w)

#create wardens
ward01 = Warden("Tim", "McManus", 323243, 20)
ward02 = Warden("Sean", "Murphy", 456788, 40)

#create prison blocks
pbA = PrisonBlock("Emerald City", 3, ward01)
pbB = PrisonBlock("Block B",5, ward02)

#add blocks to prison
oz.addBlock(pbA)
oz.addBlock(pbB)

print("\n")

#print block strings
print(oz.getBlocksString())

print("\n")

#get inmates
inmateLst = createInmates()

#revers inmate list (for pop order)
inmateLst.reverse()

#populate inmate in cells
for i in oz.prisonBlocks.keys():
      for j in range(0, len(oz.prisonBlocks[i].cells)*3):
            oz.prisonBlocks[i].addInmate(inmateLst.pop())


print("\n")

#print prisonBlocks
print(oz.prisonBlocks["Emerald City"])
print("\n")
print(oz.prisonBlocks["Block B"])
      
