num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
num3 = input("Enter number 3: ")
maxnum = ""
if num1 > num2 & num1 > num3:
    maxnum = num1
if num2 > num1 & num2 > num3:
    maxnum = num2
if num3 > num1 & num3 > num2:
    maxnum = num3