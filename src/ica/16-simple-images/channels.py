from src.ica.helpers.imageTools import *

def red_channel(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (r, 0, 0))

    return new_pic

def green_channel(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (0, g, 0))

    return new_pic

def blue_channel(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (0,0,b))

    return new_pic


from src.ica.helpers.dummyWindow import *

astilbe = Picture("../SampleImages/astilbe.jpg")
astilbe_red = red_channel(astilbe)
astilbe_red.show()
astilbe_green = green_channel(astilbe)
astilbe_green.show()
astilbe_blue = blue_channel(astilbe)
astilbe_blue.show()

keep_windows_open()
