from abc import ABCMeta, abstractmethod
from Operation import Operation

class NumberOperation(Operation):
	__metaclass__ = ABCMeta

	def __init__(self, name, answer):
		super().__init__(name)
		self.answer = answer

	@abstractmethod
	def compute_numbers(self, num1, num2):
		pass

	def operate(self):
		num1 = int(input("Type in the first number: "))
		num2 = int(input("Type in the second number: "))
		print("The {} is {}".format(self.answer, str(self.compute_numbers(num1, num2))))

	ADDITION = None
	SUBTRACTION = None
	MULTIPLICATION = None
	DIVISION = None
	REMAINDER_DIVISION = None

class _AdditionOperation(NumberOperation):

	def __init__(self):
		super().__init__("Addition", "Sum")

	def compute_numbers(self, num1, num2):
		return num1 + num2

class _SubtractionOperation(NumberOperation):

	def __init__(self):
		super().__init__("Subtraction", "Difference")

	def compute_numbers(self, num1, num2):
		return num1 - num2

class _MultiplicationOperation(NumberOperation):

	def __init__(self):
		super().__init__("Multiplication", "Product")

	def compute_numbers(self, num1, num2):
		return num1 * num2

class _DivisionOperation(NumberOperation):

	def __init__(self):
		super().__init__("Division", "Quotient")

	def compute_numbers(self, num1, num2):
		return num1 / num2

class _RemainderDivisionOperation(NumberOperation):

	def __init__(self):
		super().__init__("Remainder Division", "Remainder")

	def compute_numbers(self, num1, num2):
		return num1 % num2

NumberOperation.ADDITION = _AdditionOperation()
NumberOperation.SUBTRACTION = _SubtractionOperation()
NumberOperation.MULTIPLICATION = _MultiplicationOperation()
NumberOperation.DIVISION = _DivisionOperation()
NumberOperation.REMAINDER_DIVISION = _RemainderDivisionOperation()