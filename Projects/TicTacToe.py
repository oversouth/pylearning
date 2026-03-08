import turtle as t #add turtle
t.setup(600, 600) #resolution
t.title("TicTacToe") #window title
def settings(t): #initial setup
    t.speed(100)
    t.pensize(6)
def field(t): #game field
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
def cross(t): #cross
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
settings(t) #use settings
field(t) #spawn a field
t.goto(0, 0) #go to middle of the field
while True:
    position = int(input())
    match position:
        case 1:
            x, y = -200, 200
        case 2:
            x, y = 0, 200
        case 3:
            x, y = 200, 200
        case 4:
            x, y = -200, 0
        case 5:
            x, y = 0, 0
        case 6:
            x, y = 200, 0
        case 7:
            x, y = -200, -200
        case 8:
            x, y = 0, -200
        case 9:
            x, y = 200, -200
    t.penup()
    t.goto(x, y)
    cross(t)
t.mainloop() #idk why but it has to be here (⊙_⊙)？