import random
import time
import os

def clscrn():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


while True:
    clscrn()

    randnum = random.randrange(1, 999)
    print(randnum)
    time.sleep(1)

    usrroll = input("ROLL AGAIN")
    if usrroll.lower() == "roll":
        pass



