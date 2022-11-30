## Converte a length to any other length using Enumeration
from enum import Enum

class Length(Enum):
    M = 1
    FT = 0.3048
    KM = 1000
    MI = 1609.34

    value = 5
    leng = KM


    @classmethod
    def get_value(cls):
        return Length.value




print(Length.get_value())


##def getUnit(value):
  ##  return

##def toMeter(value):
