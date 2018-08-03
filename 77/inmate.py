#pip install python-dateutil

#imports
from person import Person
from datetime import datetime
from dateutil.relativedelta import *

#class
class Inmate(Person):

      #ctor
      def __init__(self, fname, lname, idNum, prisonerNumber, crime, time):
            self.prisonerNumber = prisonerNumber
            self.crime = crime
            self.jailTimeInYears = time
            self.firstDayInJail = datetime.now()
            self.isGoodInmate = False
            self.punishmentInMonths = 0
            self.hasDrugs = False
            super().__init__(fname, lname, idNum)

      #calulate the time left until freedom
      def calcTimeToFreedom(self):
            return self.getReleseDate-datetime.now()

      #calulate the time spent in jail
      def calcTimeSpentInJail(self):
            nowTime = datetime.now()
            return nowTime-self.firstDayInJail

      #calulate the relese date
      @property
      def getReleseDate(self):
            delta = relativedelta(years=self.jailTimeInYears, months=self.punishmentInMonths)
            return self.firstDayInJail+delta

      #add punishment time 
      def addTime(self, timeInMonths):
            self.punishmentInMonths += timeInMonths

      #buy drugs
      def buyDrugs(self):
            self.hasDrugs = True

      #use drugs
      def useDrugs(self):
            if self.hasDrugs:
                  print(f"{self.fname}: mmmm.... i love drugs....")
                  self.hasDrugs = False
            else:
                  print(f"{self.fname}: has no drugs..")
                  
      #represent Inmate
      def __repr__(self):
            return super().__repr__() + f" ID: {self.idNum} \nPrisoner Number: {self.prisonerNumber} \nCrime: {self.crime} \nRelese Time: {self.getReleseDate.strftime('%x')}"


################################_TEST_##################################

import time
def testInmate():
      inmate = Inmate("Simon", "Adebisi", 1234, 1111, "killer", 10)
      time.sleep(4)
      print(inmate.calcTimeSpentInJail())
      print(inmate.getReleseDate)
      inmate.addTime(5)
      print(inmate.getReleseDate)
      print(inmate.calcTimeToFreedom())
      inmate.useDrugs()
      inmate.buyDrugs()
      inmate.useDrugs()
      print(inmate)

#testInmate()
      


            
