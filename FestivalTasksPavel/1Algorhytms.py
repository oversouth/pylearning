NumCount = int(input())
numbers = []
for i in range(NumCount):
    numbers.append(int(input()))
minNum = min(numbers)
maxNum = max(numbers)
middleNum = sum(numbers) / NumCount
print(sum(numbers), middleNum, maxNum, minNum)