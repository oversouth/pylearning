outputpath = "Lessons\\intlesson11\\output2.txt"
string = input("enter a string ")
file = open(outputpath, "w")
file.write(string)
file.close()