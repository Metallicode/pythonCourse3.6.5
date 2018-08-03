from person import Person

class Warden(Person):

      #ctor
      def __init__(self, fname, lname, idNum, evilness):
            self.evilness = evilness
            super().__init__(fname, lname, idNum)

      #check if inmate has Drugs method
      def shakedown(self, inmate):
            if inmate.hasDrugs:
                  punish = (self.evilness + 1)/2
                  print(f"I HATE Drugs! you get more time! {int(punish)} Months!")
                  inmate.addTime(punish)
                  inmate.crime += " ,drugs possession"
            else:
                  print("you don't fool me.. i'll catch you next time!")

            

################################_TEST_##################################

def testWarden():
      from inmate import Inmate
      inmat = Inmate("Simon", "Adebisi", 1234, 1111, "killer", 10)
      ward = Warden("Tim", "McManus", 2345, 15)
      print(ward)
      print(inmat)
      inmat.buyDrugs()
      ward.shakedown(inmat)
      print(inmat)      

#testWarden()

      
