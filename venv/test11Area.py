from Operation import Operation
from AreaCalculationOperation import AreaCalculationOperation


while True:
    operation = Operation.EXIT
    print("Area Calculator")
    try:
        choice = int(input("1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n(Any number) Exit\n"))
        if choice == 1:
            operation = AreaCalculationOperation.SQUARE
        elif choice == 2:
            operation = AreaCalculationOperation.RECTANGLE
        elif choice == 3:
            operation = AreaCalculationOperation.TRIANGLE
        elif choice == 4:
            operation = AreaCalculationOperation.CIRCLE
    except ValueError:
        print("Unacceptable input")

    print(operation.name)
    operation.operate()
