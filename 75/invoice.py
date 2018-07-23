import datetime

class invoice:
      invoiceNomber = 0

      #ctor
      def __init__(self):
            self.numOfItems = 0
            self.__class__.invoiceNomber += 1
            self.__total = 0
            now = datetime.datetime.now()
            self.__invoiceLog = f"New invoice #{self.__class__.invoiceNomber} {now.strftime('%c')}\n"

      #add item to invoice
      def addItem(self, item):
            self.numOfItems +=1
            self.__total += float(item)
            self.__invoiceLog += f"#{self.numOfItems}\t{item}\n"

      #get total invoice sum
      def getTotal(self):
            return f"Total Cost: \t {self.__total:.2f} ILS"

      #override __repr__()
      def __repr__(self):
            return f"{self.__invoiceLog} \n{self.getTotal()}"

      #operator overloading 
      def __add__(self, other):
            return self.__total + other.__total
