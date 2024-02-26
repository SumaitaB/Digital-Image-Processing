import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import feature
from skimage import util

s = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.2.09.tiff')
io.imshow(s)
io.show()

s_gray = util.img_as_ubyte(s)  # Convert the image to grayscale

# Apply Canny edge detection
s_edges = feature.canny(s_gray)

io.imshow(s_edges)
io.show()
