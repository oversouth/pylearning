num = int(input("Type a number:"))
total_sum = 0
for i in range(1,num+1):
    if i % 2 != 0:
        total_sum += i
print(total_sum)