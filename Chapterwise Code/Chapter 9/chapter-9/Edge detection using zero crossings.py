import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage import util
from scipy import ndimage as ndi

s = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.2.09.tiff')
io.imshow(s)
io.show()

s2 = ndi.gaussian_laplace(util.img_as_float64(s), sigma=3)

# Calculate zero crossings using a simple thresholding approach
zero_crossings = (s2[:-1, :-1] * s2[1:, 1:] < 0) | (s2[:-1, 1:] * s2[1:, :-1] < 0)

io.imshow(zero_crossings)
io.show()
