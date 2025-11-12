import turtle
import random


def draw_petal(t, size):
    """Draws a single petal"""
    t.begin_fill()
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.left(120)  # Point back to the center
    t.end_fill()


def draw_flower(t, num_petals, petal_size, color_mode):
    """
    Draws a complete flower by calling draw_petal in a loop.
    """
    angle = 360 / num_petals

    for _ in range(num_petals):
        # This block determines the color of each petal
        if color_mode == "random":
            # Pick a completely random color
            r = random.random()
            g = random.random()
            b = random.random()
            t.color(r, g, b)
            t.fillcolor(r, g, b)
        else:
            # Use the color the user specified
            t.color(color_mode)
            t.fillcolor(color_mode)

        draw_petal(t, petal_size)
        t.left(angle)


def main():
    """
    Main function to set up the screen, get user input,
    and draw the grid of flowers.
    """

    # 1. Setup the screen and turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Generative Flower Grid")

    t = turtle.Turtle()
    t.speed(0)  # 0 is the fastest speed
    t.hideturtle()

    # 2. Get user input
    # Get parameters from the user
    grid_size = int(turtle.numinput(
        "Grid Size",
        "Enter grid size (e.g., 2 for 2x2, 3 for 3x3):",
        default=3, minval=1, maxval=6
    ))

    petal_size = int(turtle.numinput(
        "Flower Size",
        "Enter petal size (e.g., 50):",
        default=50, minval=10, maxval=150
    ))

    # This list is just for simple validation
    valid_colors = ["red", "green", "blue", "yellow", "orange", "purple", "white", "pink", "cyan"]

    # Keep asking until the user gives valid input
    while True:
        base_color_input = turtle.textinput(
            "Color Scheme",
            "Enter a color (e.g., 'red', '#FF5733') or 'random':"
        )

        # Handle case where user clicks 'Cancel'
        if base_color_input is None:
            print("No color chosen. Exiting.")
            return  # Exit the main function

        base_color = base_color_input.lower().strip()

        if base_color == "random":
            color_mode = "random"
            break  # Valid input, exit loop
        elif base_color in valid_colors or base_color.startswith("#"):
            color_mode = base_color
            break  # Valid input, exit loop
        else:
            # Invalid input, loop repeats
            pass

            # 3. Grid layout variables
    spacing = 200  # pixels between flowers
    start_x = -200  # top-left x
    start_y = 200  # top-left y

    # Nested loop to draw the grid
    # Loop for rows
    for row in range(grid_size):
        # Loop for columns
        for col in range(grid_size):
            # Calculate the center (x, y) for the current flower
            x = start_x + (col * spacing)
            y = start_y - (row * spacing)

            # Move the turtle to the new position without drawing
            t.penup()
            t.goto(x, y)
            t.pendown()

            # Draw the flower
            draw_flower(t, 15, petal_size, color_mode)

    # 4. Finish
    screen.exitonclick()


# Run the main function
if __name__ == "__main__":
    main()