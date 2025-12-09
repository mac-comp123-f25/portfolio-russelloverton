import turtle
from random import randint

first_turtle = turtle.Turtle()
second_turtle = turtle.Turtle()
third_turtle = turtle.Turtle()

first_turtle.color("red")
second_turtle.color("green")
third_turtle.color("blue")

first_turtle.speed(0)
second_turtle.speed(0)
third_turtle.speed(0)
turtle.colormode(255)


first_turtle.penup()
second_turtle.penup()
third_turtle.penup()
first_turtle.setx(-350)
second_turtle.setx(-350)
third_turtle.setx(-350)
first_turtle.sety(250)
second_turtle.sety(300)
third_turtle.sety(350)
first_turtle.pendown()
second_turtle.pendown()
third_turtle.pendown()
first_turtle.width(10)
second_turtle.width(10)
third_turtle.width(10)


for _ in range(100):
    turtle.bgcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    first_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    second_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    third_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    first_turtle.forward(10)
    second_turtle.forward(10)
    third_turtle.forward(10)
    first_turtle.right(90)
    second_turtle.right(90)
    third_turtle.right(90)
    first_turtle.forward(10)
    second_turtle.forward(10)
    third_turtle.forward(10)
    first_turtle.left(90)
    second_turtle.left(90)
    third_turtle.left(90)

turtle.done()