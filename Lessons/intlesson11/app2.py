path = "Lessons\\intlesson11\\input3.txt"
file = open(path)
print(len(lines))
for line in lines:
    print(line.strip())
file.close()