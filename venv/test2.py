input_age = input("Type in your age: ")

age = int(input_age)

if isinstance(age, int):
	print("you are " + ("legal" if age >= 18 else "too young."))
else: print("input not a (whole) number")
