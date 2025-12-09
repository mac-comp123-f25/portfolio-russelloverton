import turtle

def square(turtle, length):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)

turtle = turtle.Turtle()
turtle.color("pink")
turtle.pensize(50)
square(turtle, 200)