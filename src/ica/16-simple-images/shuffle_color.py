from src.ica.helpers.imageTools import *

def colorShuffle(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (b,r,g))

    return new_pic

from src.ica.helpers.dummyWindow import *
mushrooms0 = Picture("../SampleImages/mushrooms.jpg")
mushrooms1 = colorShuffle(mushrooms0)
mushrooms1.show()
mushrooms2 = colorShuffle(mushrooms1)
mushrooms2.show()

keep_windows_open()


