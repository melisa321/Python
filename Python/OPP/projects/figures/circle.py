from figure import Figure
from shape import Shape
from math import pi

class Circle(Figure):
	def __init__(self, radius):
		self.radius = radius
 
	def get_area(self):
		return pi * (self.radius ** 2)
	
	def get_perimeter(self):
		# return super().get_perimeter()
		return 2 * self.radius * pi
	
circle = Circle(4)
print(circle.get_area())
print(circle.get_perimeter())


if __name__ == "shape":
	print("wywołany jest figure")
	shape = Shape(2, 3)
	print(shape.get_area())
	print(shape.get_perimeter())