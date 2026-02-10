num = int(input())
a = num // 100
b = (num // 10) % 10
c = num % 10
sum1 = b + c
sum2 = a + b
if sum1 >= sum2:
    print(f"{sum1}{sum2}")
else:
    print(f"{sum2}{sum1}")
