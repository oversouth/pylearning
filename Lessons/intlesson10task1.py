nums = input()
evencounter = 0
oddcounter = 0
for char in nums:
    if char.isdigit():
        if int(char) % 2 == 0:
            evencounter += 1
        else:
            oddcounter += 1
print("Четных:", evencounter)
print("Нечетных:", oddcounter)