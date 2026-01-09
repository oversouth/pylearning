print("PyCalc")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        if num2 == 0:
            print("You can't divide by zero.")
            exit()
        result = num1 / num2
    else:
        print("Unknown operation.")
        exit()
    print("Result:", result)
except ValueError:
    print("Not a number.")
