from inmate import Inmate
from warden import Warden
from prisonBlock import PrisonBlock


class Prison:

      PrisonerIDMaker = 0
      
      def __init__(self, name, chiefWarden):
            self.prisonName = name
            self.prisonBlocks = {}
            self.chiefWarden = chiefWarden
            self.IDGenerator = 0
            
      def addBlock(self, block):
            self.prisonBlocks[block.name] = block

      @classmethod
      def getNewPrisonerID(cls):
            val = str(cls.PrisonerIDMaker).zfill(8)
            cls.PrisonerIDMaker += 1
            return val
            

      def getBlocksString(self):
            string = ""
            for i in self.prisonBlocks.keys():
                  string += i.__repr__() + "\n"

            return string
                  

      def __repr__(self):
            string = ""
            string += f"this is {self.prisonName}, a maximum security penitentiary facility \n"
            string += f"Chief Warden is {self.chiefWarden} \n"
            string += f"{self.getBlocksString()}"

            return string
                  

################################_TEST_##################################

def testPrison():

      w = Warden("Leo", "Glynn", 12321, 10)
      
      oz = Prison("Oz", w)
      
      ward01 = Warden("Tim", "McManus", 2222, 16)
      ward02 = Warden("Sean", "Murphy", 3333, 12)
      
      pbA = PrisonBlock("ameraldCity", 10, ward01)
      pbB = PrisonBlock("Block_B",3, ward02)

      oz.addBlock(pbA)
      oz.addBlock(pbB)

      print("\n")

      print(oz.getBlocksString())

      print("\n")

      for i in oz.prisonBlocks.keys():
            for j in range(0, 20):
                  oz.prisonBlocks[i].addInmate(Inmate("test", "test", 1234, j, "killer", 10))

      print("\n")
      
      print(oz.prisonBlocks["ameraldCity"])
      print("\n")
      print(oz.prisonBlocks["Block_B"])
            


#testPrison()
      


