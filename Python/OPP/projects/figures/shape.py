from figure import Figure


class Shape(Figure):
	def __init__(self, side1, side2):
		self.side1 = side1
		self.side2 = side2

	def get_area(self):
		return self.side1 * self.side2

	def get_perimeter(self):
		return super().get_perimeter()

	def __str__(self):
		return f'The area of this {self.__class__.__name__} is: {self.get_area()}'

# Uruchamiam tę cześć tegeo skryptu tylko jesli zostanie wywolany jako main -> python3 shape.py
if __name__ == "__main__":
	print(f"Hello, to ja shape.py kiedy ktos mnie woła jak main {__name__}")
	shape = Shape(2, 3)
	print(shape.get_area())
	print(shape.get_perimeter())


if __name__ == "shape":
	print("To ja Shape, Jestem wywowalny kiedy ktos mnie zaimportowal")