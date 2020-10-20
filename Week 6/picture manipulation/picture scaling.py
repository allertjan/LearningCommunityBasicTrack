from PIL import Image
import numpy as np

im = Image.open("fruit_fade.png")
pix = np.array(im)

# get the maximum value
maximum = np.max(pix)

# calculate the scaling factor
scale = 255.0/maximum

# create the new 2D array with list comprehension
new_pix = [[pixel * scale for pixel in row] for row in pix]
new_pix = np.array(new_pix).astype('uint8')

im2 = Image.fromarray(new_pix)
im2.show()

# Link: https://github.com/VincentVelthuizen/basictrack_2021_1a/blob/master/week_6/color_scale.py
