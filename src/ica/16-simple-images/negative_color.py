from src.ica.helpers.imageTools import *

def negative(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (abs(r - 255), abs(g - 255), abs(b - 255)))

    return new_pic

from src.ica.helpers.dummyWindow import *

pic1 = Picture("../SampleImages/butterfly.jpg")

new_pic = negative(pic1)
new_pic.show()

keep_windows_open()
