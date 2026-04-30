import turtle as t

def settings(t): #settings,you can change the name on top bar,resolution(not reccomended) and turtle speed and size
    t.speed(100) #SPEED of the turtle,keep it on 100 for instant
    t.pensize(6) #THICKness of the drawing
    t.setup(600, 600) #RESOLUTION of the window(not reccomended to change)
    t.title("TicTacToe")

def field(t): #main field drawing function
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

def checkwinner(field): #check who is winner function
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] != 0:
            return field[i][0]
        if field[0][i] == field[1][i] == field[2][i] != 0:
            return field[0][i]
    if field[0][0] == field[1][1] == field[2][2] != 0:
        return field[0][0]
    if field[0][2] == field[1][1] == field[2][0] != 0:
        return field[0][2]
    return 0

def cross(t): #draw a cross function
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

def circle_mark(t): #draw a circle function
    t.pencolor("blue")
    t.penup()
    xc = t.xcor()
    yc = t.ycor()
    t.goto(xc, yc - 100)
    t.pendown()
    t.setheading(0)
    t.circle(100)
    t.penup()


area = [ #area of the game, 0 - empty, 1 - cross, 2 - circle
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

settings(t)
field(t)

started = True
lastmove = None
firstmove = True

while started: #main game loop
    inp = input("move: ")
    cell, shape = inp.split(" ")
    cell = int(cell)
    x = cell // 3
    y = cell % 3 - 1

    if firstmove and shape != "cross":
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

    if shape == "circle":
        area[x][y] = 2
    else:
        area[x][y] = 1

    lastmove = shape

    match cell:
        case 1: t.goto(-200, 200)
        case 2: t.goto(0, 200)
        case 3: t.goto(200, 200)
        case 4: t.goto(-200, 0)
        case 5: t.goto(0, 0)
        case 6: t.goto(200, 0)
        case 7: t.goto(-200, -200)
        case 8: t.goto(0, -200)
        case 9: t.goto(200, -200)
        case _: print("wrong")

    if shape == "circle":
        circle_mark(t)
    elif shape == "cross":
        cross(t)
    else:
        print("wrong")
        continue

    # Check winner after every move
    winner = checkwinner(area)
    if winner == 1:
        print("crosses win")
        started = False
    elif winner == 2:
        print("circles win")
        started = False
    elif all(area[r][c] != 0 for r in range(3) for c in range(3)):
        print("draw, no one won")
        started = False

t.mainloop()