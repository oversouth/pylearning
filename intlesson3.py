#num = int(input("enter number: "))
from INTlistslearning import numbers

#if num > 0:
    #print("positive")
#elif num < 0:
#    print("negative")
#else:
#    print("number is zero")


#n = int(input("enter number: "))
#for i in range(0, n + 1):
#    if i % 2 == 0:
#       print(i)


#string = input()
#gl = "euioayEUIOAY" #vowels
#count = 0 #count var
#for symbol in string: #function start,counting vowels
#    if symbol in gl: #check symbols
#        count += 1 #count the symbols
#print(count) #print the amount of vowel symbols in string

#numbers = input()
#numbers = numbers.split(" ")
#print(numbers)

for i in range(lev(numbers)):
    numbers[i] = int(numbers[i])
print(max(numbers),min(numbers))
