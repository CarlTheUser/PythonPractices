from Operation import Operation, ExitOperation
from NumberOperations import NumberOperation

#sumOperation = AdditionOperation()

#sumOperation.operate()

while True:
	operation = ExitOperation()
	try:
		option = int(input("1: Addition \n2: Subtraction \n3: Multiplication \n4: Division \n5: Remainder Division \nAny Number: Exit\n"))
		if option == 1: operation = NumberOperation.ADDITION
		elif option == 2: operation = NumberOperation.SUBTRACTION
		elif option == 3: operation = NumberOperation.MULTIPLICATION
		elif option == 4: operation = NumberOperation.DIVISION
		elif option == 5: operation = NumberOperation.REMAINDER_DIVISION
	except ValueError:
		print("Unacceptable input")
	print(operation.name + "\n")
	try:
		operation.operate()
	except ZeroDivisionError:
		print("Can't divide by zero.")


