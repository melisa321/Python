
from shape import Shape


class Rectangle(Shape):
	def __init__(self, side1, side2):
		super().__init__(side1, side2)

	def get_area(self):
		return super().get_area()

	def get_perimeter(self):
		return super().get_perimeter()

rect = Rectangle(4,2)     
print("Rectangle Area: ", rect.get_area())

if __name__ == "__main__":
	print(f"Hello, to ja rectangle.py kiedy ktos mnie woła jak main {__name__}")