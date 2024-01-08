
from figure import Figure

from math import sqrt

class Hexagon(Figure):
    def __init__(self, side1):
                self.side1 = side1

    def get_perimeter(self):
        return (6 * self.side1)
    
    def get_area(self):
        return (3 * sqrt(3) * self.side1 ** 2) / 2
                
hexa = Hexagon(4)
print(hexa.get_area()) 
print(hexa.get_perimeter()) 