import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage import util

s = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.2.09.tiff')
io.imshow(s)
io.show()

s2 = util.img_as_float(s)
s_lap = np.abs(filters.laplace(s2))
io.imshow(s_lap)
io.show()
