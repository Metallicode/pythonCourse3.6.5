from inmate import Inmate
from warden import Warden
from prison import Prison
from prisonBlock import PrisonBlock

from setupHelper import createInmates

w = Warden("Leo", "Glynn", 6546876, 100)

oz = Prison("Oz", w)

ward01 = Warden("Tim", "McManus", 323243, 20)
ward02 = Warden("Sean", "Murphy", 456788, 40)

pbA = PrisonBlock("Emerald City", 3, ward01)
pbB = PrisonBlock("Block B",5, ward02)

oz.addBlock(pbA)
oz.addBlock(pbB)

print("\n")

print(oz.getBlocksString())

print("\n")

inmateLst = createInmates()

inmateLst.reverse()

for i in oz.prisonBlocks.keys():
      for j in range(0, len(oz.prisonBlocks[i].cells)*3):
            oz.prisonBlocks[i].addInmate(inmateLst.pop())


print("\n")

print(oz.prisonBlocks["Emerald City"])
print("\n")
print(oz.prisonBlocks["Block B"])
      
