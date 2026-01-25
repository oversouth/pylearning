HungryMeter = input("Are you hungry? (yes/no) ")
while HungryMeter in ("yes", "yep", "ofc", "of course"):
    HungryMeter = input("You made a sandwich, still hungry? (yes/no) ")
    if HungryMeter in ("no", "nope", "nah", "im not hungry"):
        CYMmeter = input("You didn’t make another sandwich, did you change your mind? (yes/no) ")
        if CYMmeter == "yes":
            HungryMeter = "yes"
