digits = [int(x) for x in input()]
digits.sort()
if digits[0] + digits[2] == digits[1] * 2:
    print("YES")
else:
    print("NO")