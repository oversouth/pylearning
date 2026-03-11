num1 = int(input())
num2 = int(input())
if num1 > num2:
    print(*range(num1, num2 - 1, -1))
else:
    print(*range(num1, num2 + 1))