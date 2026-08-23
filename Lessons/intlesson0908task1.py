usr_inp = input("enter nums: ")
nums = eval(usr_inp)
i = int(input("enter a number: "))
nums_together = sum(nums)
subtractions = 0
while nums_together % i != 0:
    nums_together -= 1
    subtractions += 1
print(subtractions)
