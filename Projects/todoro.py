print("todoro v2")
pathoutput = "tasks.txt"
while True:
    userinput = input("a=add, d=delete, c=complete ,r=check tasks, f=fun tasks, q=quit: ")
    if userinput == "a":
        file = open(pathoutput, "a")
        task = input("enter a task: ")
        file.write("[ ] " + task + "\n")
        file.close()
    elif userinput == "d":
        tasktodelete = input("enter the name to delete: ")
        file = open(pathoutput, "r")
        tasks = file.readlines()
        file.close()
        newtasks = []
        for t in tasks:
            clean = t.replace("[ ] ", "").replace("[x] ", "").strip()
            if clean != tasktodelete:
                newtasks.append(t)
        file = open(pathoutput, "w")
        file.writelines(newtasks)
        file.close()
    elif userinput == "c":
        taskname = input("enter the name of task to complete: ")
        file = open(pathoutput, "r")
        tasks = file.readlines()
        file.close()
        newtasks = []
        for t in tasks:
            clean = t.replace("[ ] ", "").replace("[x] ", "").strip()
            if clean == taskname:
                newtasks.append("[x] " + taskname + "\n")
            else:
                newtasks.append(t)
        file = open(pathoutput, "w")
        file.writelines(newtasks)
        file.close()
    elif userinput == "r":
        file = open(pathoutput, "r")
        tasks = file.readlines()
        file.close()
        for t in tasks:
            print(t.strip())
    elif userinput == "f":
        print("fun mode")
        file = open(pathoutput, "a")
        task = input("enter a FUN task: ")
        file.write("[ ] " + task[::-1] + "\n")
        file.close()
    elif userinput == "q":
        break
