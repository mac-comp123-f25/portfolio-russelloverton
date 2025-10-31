import turtle as t

def draw_nested_squares(turtle):
    turtle.teleport(0,0)
    turtle.down()
    turtle.setheading(90)
    for i in range(8):
        for _ in range(4):
         turtle.forward(10 * (i+1))
         turtle.right(90)

win = t.Screen()
jerry = t.Turtle()
jerry.speed(10)
draw_nested_squares(jerry)

win.exitonclick()