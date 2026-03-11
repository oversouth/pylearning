nameA = input()
nameB = input()
nameC = input()

if nameA < nameB and nameA < nameC:
    print(nameA)
elif nameB < nameA and nameB < nameC:
    print(nameB)
else:
    print(nameC)
