from abc import ABCMeta, abstractmethod
from Operation import Operation
import math
class AreaCalculationOperation(Operation):
    
	__metaclass__ = ABCMeta

	SQUARE = None
	RECTANGLE = None
	TRIANGLE = None
	CIRCLE = None

	def __init__(self, name):
		super().__init__(name)

	@abstractmethod
	def calculate_area(self):
		pass

class SquareAreaCalculationOperation(AreaCalculationOperation):

	def __init__(self):
		super().__init__("Square Area Calculator")
		self._side = 0

	def calculate_area(self):
		return self._side * self._side

	def operate(self):
		try:
			self._side = float(input("Enter the square's side length: "))
			print("The area of the square is: {}".format(str(self.calculate_area())))
		except ValueError:
			print("Invalid input")

class RectangleAreaCalculationOperation(AreaCalculationOperation):

	def __init__(self):
		super().__init__("Rectangle Area Calculator")
		self._width = 0
		self._height = 0

	def calculate_area(self):
		return self._width * self._height

	def operate(self):
		try:
			self._width = float(input("Enter the rectangle's width: "))
			self._height= float(input("Enter the rectangle's height: "))
			print("The area of the rectangle is: {}".format(str(self.calculate_area())))
		except ValueError:
			print("Invalid input")

class TriangleAreaCalculationOperation(AreaCalculationOperation):

	def __init__(self):
		super().__init__("Triangle Area Calculator")
		self._base = 0
		self._height = 0

	def calculate_area(self):
		return (self._base * self._height) / 2

	def operate(self):
		try:
			self._base = float(input("Enter the triangle's base length: "))
			self._height= float(input("Enter the rectangle's height: "))
			print("The area of the triangle is: {}".format(str(self.calculate_area())))
		except ValueError:
			print("Invalid input")

class CircleAreaCalculationOperation(AreaCalculationOperation):

	def __init__(self):
		super().__init__("Circle Area Calculator")
		self._radius = 0

	def calculate_area(self):
		return  math.pi * (self._radius * self._radius)

	def operate(self):
		try:
			self._radius = float(input("Enter the circle's radius: "))
			print("The area of the circle is: {}".format(str(self.calculate_area())))
		except ValueError:
			print("Invalid input")

AreaCalculationOperation.SQUARE = SquareAreaCalculationOperation()
AreaCalculationOperation.RECTANGLE = RectangleAreaCalculationOperation()
AreaCalculationOperation.TRIANGLE = TriangleAreaCalculationOperation()
AreaCalculationOperation.CIRCLE = CircleAreaCalculationOperation()
