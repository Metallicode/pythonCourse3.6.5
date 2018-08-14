from enum import Enum, auto

class days(Enum):
      Sunday = 1
      Monday = 2
      Tuesday = 3
      Wednesday = 4
      Thursday = 5
      Friday = 6
      Saturday = 7


myValue = days.Sunday
print(myValue)
print(myValue.value)
print(myValue.name)


class elements(Enum):
      metal = auto()
      copper = auto()
      aluminium = auto()

myValue = elements.metal
print(myValue)
print(myValue.value)
print(myValue.name)
