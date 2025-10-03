import turtle
import math

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

def move_sepal(x, y):
    sepalTurtle.up()
    sepalTurtle.goto(x, y)
    sepalTurtle.down()
    for _ in range(5):
        sepalTurtle.begin_fill()
        sepalTurtle.circle(50)
        sepalTurtle.end_fill()
        sepalTurtle.left(72)

def petal(x, y):
    petalTurtle.up()
    petalTurtle.goto(x, y)
    petalTurtle.down()
    for _ in range(5):
        petalTurtle.begin_fill()
        petalTurtle.circle(25)
        petalTurtle.end_fill()
        petalTurtle.left(72)


def center(x, y):
    centerTurtle.up()
    centerTurtle.goto(x, y)
    centerTurtle.down()
    centerTurtle.begin_fill()
    centerTurtle.circle(15)
    centerTurtle.end_fill()

def stamp(x, y):
    stampTurtle.up()
    stampTurtle.goto(x, y)
    stampTurtle.down()
    stampTurtle.stamp()

move_sepal(0, 0)

petal(0, 0)

center(0,-15)

stamp(-2, 0)

move_sepal(0,220)

petal(0, 220)

center(0,205)

stamp(-2, 220)

move_sepal(220, 0)

petal(220, 0)

center(220, -15)

stamp(218, 0)

move_sepal(0, -220)

petal(0, -220)

center(0, -235)

stamp(-2, -220)

move_sepal(-220, 0)

petal(-220, 0)

center(-220, -15)

stamp(-222, 0)

win.exitonclick()