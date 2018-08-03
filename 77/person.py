class Person:
      def __init__(self, fname, lname, idNum):
            self.fname = fname
            self.lname = lname
            self.idNum = idNum
            
      def __repr__(self):
            return f"{self.fname} {self.lname}"

      
