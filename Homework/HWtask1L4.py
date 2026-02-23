try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
except ValueError:
    print("Only integers are allowed")
    exit()

if num1 == num2:
    print("Numbers are equal.")
if num1 > num2:
    print(num1, " is greater than ", num2)
elif num1 < num2:
    print(num2, " is greater than ", num1)
    # hello from zed!
