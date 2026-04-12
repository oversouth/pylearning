s = input("enter s")
sreversed = s[::-1]
s = s.replace(" ", "")
s = s.lower()
sreversed = sreversed.replace(" ", "")
sreversed = sreversed.lower()
if s == sreversed:
    print("true")
else:
    print("false")