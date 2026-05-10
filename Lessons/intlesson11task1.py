import random as r
import turtle as t

radius = 10
colors = ["red", "green", "blue", "yellow", "purple"]


def settings():
    t.speed(0)
    t.pensize(8)
    t.Screen().setup(1080, 1080)
    t.title("fireworks:)")


settings()
while radius < 500:
    x, y = r.randint(-400, 400), r.randint(-400, 400)
    t.penup()
    t.goto(x, y)
    t.pendown()
    color = r.choice(colors)
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    radius *= 1.5
t.done()
