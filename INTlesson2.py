str1 = "oversouth scorpio coldy textav"

def is_empty(str1):
    if str1 == "":
        print("str1 is empty")
    else:
        print("str1 is not empty,it is:",str)
is_empty(str1)

def mood_answer(mood):
    if mood == "nice":
        print("thats cool")
    else:
        print("sad to hear that")

mood = input("What is your mood?")
mood_answer(mood)

str2 = "LOWERCASE ME"
print(str2.lower())

str3 = "                    ..........            "
print(str3.strip())

def clear_text(str3):
   return clean.replace(" ", "")