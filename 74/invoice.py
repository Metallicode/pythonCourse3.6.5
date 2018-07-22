import datetime

class invoice:
      invoiceNomber = 0
      
      def __init__(self):
            self.numOfItems = 0
            self.__class__.invoiceNomber += 1
            self.__total = 0
            now = datetime.datetime.now()
            self.__invoiceLog = f"New invoice #{self.__class__.invoiceNomber} {now.strftime('%c')}\n"

      def addItem(self, item):
            self.numOfItems +=1
            self.__total += float(item)
            self.__invoiceLog += f"#{self.numOfItems}\t{item}\n"

      def getTotal(self):
            return f"Total Cost: \t {self.__total:.2f} ILS"

      def __repr__(self):
            return f"{self.__invoiceLog} \n{self.getTotal()}"

      def __add__(self, other):
            return self.__total + other.__total
