from math import sqrt
def distance (first_x, first_y, second_x, second_y):
    return sqrt((first_x - second_x) ** 2 + (first_y - second_y) ** 2)

def midpoint (first_x, first_y, second_x, second_y):
    return (first_x + second_x) / 2, (first_y + second_y) / 2

print("Here's the distance of these two points:")
print(distance(10,20,-5,-10))
print("Here's the midpoint of these two points:")
print(midpoint(10,20,-5,-10))
print("woah")