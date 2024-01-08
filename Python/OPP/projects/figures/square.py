
from hexagon import Hexagon

class Square():
    def __init__(self, side1):
                self.self=side1          
                
    def get_perimeter(self):
        return (4 * self.side1)
    
    def get_area(self):
        return (self.side1 * self.side1)
	
                
square = Square(4)
print(square.get_area()) 
print(square.get_perimeter()) 