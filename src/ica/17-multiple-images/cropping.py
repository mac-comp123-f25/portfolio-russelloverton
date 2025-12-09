from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import Picture

def crop_picture(crop_from, x_left, y_top, x_right, y_bottom):


dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam_crop1.show()
dam_crop2.show()
keep_windows_open()
