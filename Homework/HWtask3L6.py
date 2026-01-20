text = input("Enter a text")
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
vowelcounter = 0
consonantcounter = 0
for char in text:
    if char in vowels:
     vowelcounter += 1
    elif char in consonants:
        consonantcounter += 1
if consonantcounter > vowelcounter:
    print("1")
elif consonantcounter < vowelcounter:
        print("2")