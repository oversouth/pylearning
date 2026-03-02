numbers = input().split()
max = int(numbers[0])
min = int(numbers[0])
for n in numbers:
    n = int(n)
    if n > max:
        max = n
    if n < min:
        min = n
print("Максимум:", max)
print("Минимум:", min) 