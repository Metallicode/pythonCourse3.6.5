class fruit:
      
      def __init__(self, name, weight, priceKg):
            self.name = name
            self.weight = weight
            self.priceKg = priceKg

      @property
      def cost(self):
            return self.weight * self.priceKg

      def __add__(self, other):
            return self.cost + other.cost
      
      def __float__(self):
            return self.cost

      def __int__(self):
            return int(float(self))

      def __repr__(self):
            return f"{self.name} \t{self.weight} Kg X {self.priceKg} ILS \t =\t{self.cost:.2f}ILS"





