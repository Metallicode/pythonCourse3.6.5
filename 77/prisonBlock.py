from inmate import Inmate
from warden import Warden

class PrisonBlock:

      #ctor
      def __init__(self, name, numOfCells, wardon):
            self.wardon = wardon
            self.numOfInmatesInCell = 3
            self.name = name
            self.numOfCells = numOfCells
            self.numOfInmatesInBlock = 0
            self.cells = []
            for i in range(0, numOfCells):
                  self.cells.append([])

      #add inmate to a cell
      def addInmate(self, inmate):
            for i in range(0, self.numOfCells):
                  wasAdd = False
                  if len(self.cells[i]) < self.numOfInmatesInCell:
                        self.cells[i].append(inmate)
                        wasAdd = True
                        self.numOfInmatesInBlock +=1
                        print(f"{inmate.prisonerNumber} was add to cell {i}")
                        break

            if not wasAdd:
                  print(f"no room for inmate {inmate.prisonerNumber}")

      #make this class iterable
      def __iter__(self):
            self.inmateCounter = 0
            return self

      def __next__(self):
            if int(self.inmateCounter/3)<self.numOfCells and self.inmateCounter< self.numOfInmatesInBlock:
                  self.inmateCounter += 1
                  return self.cells[int((self.inmateCounter-1)/3)][(self.inmateCounter-1)%3]
            else:
                  raise StopIteration

      #repr override
      def __repr__(self):
            return f"Block name: {self.name} \nBlock Warden: {self.wardon} \nInmates: {self.cells}"


################################_TEST_##################################
def testPrisonBlock():
      w = Warden("Tim", "McManus", 12321, 10)
      block_a = PrisonBlock("ameraldCity", 3, w)
      print(block_a.cells)
      print("\n")
      for i in range(0, 10):
            block_a.addInmate(Inmate("test", "test", 1234, i, "killer", 10))

      print("\n")

      for i in block_a:
            print(i)

      print("\n")

      print(block_a)
      

#testPrisonBlock()
