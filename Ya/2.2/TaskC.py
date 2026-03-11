pspeed = int(input())
vspeed = int(input())
tspeed = int(input())

if pspeed > vspeed and pspeed > tspeed:
    print("Петя")
elif vspeed > pspeed and vspeed > tspeed:
    print("Вася")
else:
    print("Толя")