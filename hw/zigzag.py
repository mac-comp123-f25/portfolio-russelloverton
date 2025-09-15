import turtle

first_turtle = turtle.Turtle()
second_turtle = turtle.Turtle()
third_turtle = turtle.Turtle()

first_turtle.color("red")
second_turtle.color("green")
third_turtle.color("blue")

first_turtle.speed(0)
second_turtle.speed(0)
third_turtle.speed(0)

first_turtle.penup()
second_turtle.penup()
third_turtle.penup()
first_turtle.setx(-300)
second_turtle.setx(-300)
third_turtle.setx(-300)
first_turtle.sety(280)
second_turtle.sety(300)
third_turtle.sety(320)
first_turtle.pendown()
second_turtle.pendown()
third_turtle.pendown()

for _ in range(100):
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