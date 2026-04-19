path = "Lessons/intlesson11/input4.txt"
file = open(path, "r")
content = file.read()
file.close()
if "python" in content:
    print("yes")
else:
    print("no")