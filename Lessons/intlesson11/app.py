#1
path = "Lessons\\intlesson11\\input.txt"
file = open(path)
string = file.read()
file.close() 
print(string)
print("hello\nworld")
#2
pathoutput = "Lessons\\intlesson11\\output.txt"
greet = "test greetings"
file = open(pathoutput, "w")
file.write(greet)
file.close()
#3
path = "Lessons\intlesson11\input2.txt"
file = open(path)
strings = file.readlines()
file.close()
for string in strings:
    print(len(string.strip()))
#4
