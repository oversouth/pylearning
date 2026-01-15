num = int(input("Enter a number"))
degree = int(input("Enter a degree"))
result = num
while degree > 0:
    result *= num
    degree -= 1
print(result)
