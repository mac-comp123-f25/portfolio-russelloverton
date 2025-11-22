import turtle


def spiral_in(spiro_turt, side_len):
        spiro_turt.forward(side_len)
        spiro_turt.right(90)
        spiral_in(spiro_turt, side_len - 2)


def check_spiral_in(size: int) -> None:
    """A faster way to test spiral_in function"""
    scr = turtle.Screen()
    turt = turtle.Turtle()
    turt.speed(0)
    spiral_in(turt, size)
    scr.exitonclick()


if __name__ == '__main__':
    check_spiral_in(300)
