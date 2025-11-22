from src.ica.helpers.imageTools import *

def weighted_scale(pic, red_scale, green_scale, blue_scale):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (r + g + b) / 3
        new_pic.setColor(x, y, (lumin * red_scale, lumin * green_scale, lumin * blue_scale))

    return new_pic

from src.ica.helpers.dummyWindow import *

pic1 = Picture("../SampleImages/butterfly.jpg")

new_pic = weighted_scale(pic1, .5, .5, 0)
new_pic.show()

keep_windows_open()
