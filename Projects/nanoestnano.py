import os

pathoutput = input("enter a filename in format NAME.EXTENSION")
texttowrite = input("enter text to write")
file = open(pathoutput, "a")
file.write(str(texttowrite))
file.close()
