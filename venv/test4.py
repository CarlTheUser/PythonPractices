try:
	grade = float(input("Enter your grade: "))
	if grade > 100 : print("you're kidding me!")
	elif grade == 100: print("You got perfect grade")
	elif grade > 90: print("good job")
	elif grade > 80: print("Try better next time")
	elif grade > 75: print("Just passed")
	else: print("Try again next time : (")
except ValueError:
	print("Unacceptable input")