import turtle as t
t.setup(600, 600)
t.title("TicTacToe")
def settings(t):
    t.speed(100)
    t.pensize(6)
def field(t):
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
def cross(t):
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
def circle_mark(t):
    t.pencolor("blue")
    xc = t.xcor()
    yc = t.ycor()
    t.penup()
    t.goto(xc, yc - 100)
    t.setheading(0)
    t.pendown()
    t.circle(100)
    t.penup()
    t.goto(xc, yc)
settings(t)
field(t)
t.goto(0, 0)
while True:
    inp = input("move: ")
    match inp:
        case "1 cross":
            t.goto(-200, 200)
            cross(t)
        case "2 cross":
            t.goto(0, 200)
            cross(t)
        case "3 cross":
            t.goto(200, 200)
            cross(t)
        case "4 cross":
            t.goto(-200, 0)
            cross(t)
        case "5 cross":
            t.goto(0, 0)
            cross(t)
        case "6 cross":
            t.goto(200, 0)
            cross(t)
        case "7 cross":
            t.goto(-200, -200)
            cross(t)
        case "8 cross":
            t.goto(0, -200)
            cross(t)
        case "9 cross":
            t.goto(200, -200)
            cross(t)
        case "1 circle":
            t.goto(-200, 200)
            circle_mark(t)
        case "2 circle":
            t.goto(0, 200)
            circle_mark(t)
        case "3 circle":
            t.goto(200, 200)
            circle_mark(t)
        case "4 circle":
            t.goto(-200, 0)
            circle_mark(t)
        case "5 circle":
            t.goto(0, 0)
            circle_mark(t)
        case "6 circle":
            t.goto(200, 0)
            circle_mark(t)
        case "7 circle":
            t.goto(-200, -200)
            circle_mark(t)
        case "8 circle":
            t.goto(0, -200)
            circle_mark(t)
        case "9 circle":
            t.goto(200, -200)
            circle_mark(t)
        case _:
            print("wrong")
t.mainloop()