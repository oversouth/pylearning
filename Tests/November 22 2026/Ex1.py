amountnum = int(input())
firstnum = int(input())
maxnum = firstnum
minnum = firstnum
for _ in range(amountnum - 1):
    num = int(input())
    if num > maxnum:
        maxnum = num
    if num < minnum:
        minnum = num
lastdigitmax = maxnum % 10
lastdigitlow = minnum % 10
result = abs(lastdigitmax - lastdigitlow)
print(result)
