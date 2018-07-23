class fruit:

      #ctor
      def __init__(self, name, weight, priceKg):
            self.name = name
            self.weight = weight
            self.priceKg = priceKg

      #fruit weight times price
      @property
      def cost(self):
            return self.weight * self.priceKg

      #operator overloading 
      def __add__(self, other):
            return self.cost + other.cost

      #override __float__()
      def __float__(self):
            return self.cost

      #override __int__()
      def __int__(self):
            return int(float(self))

      #override __repr__()
      def __repr__(self):
            return f"{self.name} \t{self.weight} Kg X {self.priceKg} ILS \t =\t{self.cost:.2f}ILS"





