result = 0
while True:
    price = float(input()) 
    if price == 0:
        break
    if price >= 500:
        price *= 0.9 
    result += price
print(result)