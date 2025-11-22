from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import *

def copy_pic_into(small_pic, big_pic, start_x, start_y):
    for (x, y) in small_pic:
        big_pic.setColor(x + start_x, y + start_y, small_pic.getColor(x, y))

green_turtle = Picture("../SampleImages/greenTurtle.jpg")
scene = Picture("../SampleImages/bearLake.jpg")
copy_pic_into(green_turtle, scene, 25, 25)
copy_pic_into(green_turtle, scene, 200, 200)
copy_pic_into(green_turtle, scene, 400, 200)
scene.show()

keep_windows_open()