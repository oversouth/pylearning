import turtle as t

def settings(t): #Settings(eyecandy)
    t.speed(100)
    t.pensize(6)
    t.setup(600, 600) #Resolution
    t.title("TicTacToe") #Name in the window bar

def field(t): #Field drawing function
    t.pencolor("black")
    t.penup()
    t.goto(-300, 100)
    t.pendown()
    t.goto(300, 100)
    t.penup()
    t.goto(-300, -100)
    t.pendown()
    t.goto(300, -100)
    t.penup()
    t.goto(-100, 300)
    t.pendown()
    t.goto(-100, -300)
    t.penup()
    t.goto(100, 300)
    t.pendown()
    t.goto(100, -300)
    t.penup()

started = True
def checwinner(field):
    #TODO CHECK WINNER FUNCTION 
winner = checkwinner(area)
if winner == 1:
    print("crosses win")
    started = False
elif winner == 2:
    print("circles win")
    started = False
else:
    print("draw,no one won")
    started = False
area = [ #0 - empty 1 - circle 2 - cross
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
def cross(t): #Cross drawing function
    t.pencolor("red")
    t.setheading(45)
    xc = t.xcor()
    yc = t.ycor()
    t.penup()
    t.goto(xc - 100, yc - 100)
    t.pendown()
    t.goto(xc + 100, yc + 100)
    t.penup()
    t.goto(xc - 100, yc + 100)
    t.pendown()
    t.goto(xc + 100, yc - 100)
    t.penup()  

def circle_mark(t): #Circle drawing function
    t.pencolor("blue")
    t.penup()
    xc = t.xcor()
    yc = t.ycor()
    t.goto(xc, yc - 100)
    t.pendown()
    t.setheading(0)
    t.circle(100)
    t.penup()  
settings(t) 
field(t)
lastmove = None
firstmove = True
while started: #input(controls)
    inp = input("move: ")
    cell, shape = inp.split(" ")
    cell = int(cell)
    x = cell // 3
    y = cell % 3 - 1
    if firstmove and "cross" != shape:
        print("wrong")
        continue
    else:
        firstmove = False
    if shape == lastmove:
        print("wrong")
        continue
    if area[x][y] != 0:
        print("wrong")
        continue
    else:
        if shape == "circle":
            area[x][y] = 2
        else:
            area[x][y] = 1

    lastmove = shape
    match cell:
        case 1:
            t.goto(-200, 200)
        case 2:
            t.goto(0, 200)
        case 3:
            t.goto(200, 200)
        case 4:
            t.goto(-200, 0)
        case 5:
            t.goto(0, 0)
        case 6:
            t.goto(200, 0)
        case 7:
            t.goto(-200, -200)
        case 8:
            t.goto(0, -200)
        case 9:
            t.goto(200, -200)
        case _:
            print("wrong")

    if shape == "circle":
        circle_mark(t)
    elif shape == "cross":
        cross(t)
    else:
        print("wrong")
t.mainloop() 