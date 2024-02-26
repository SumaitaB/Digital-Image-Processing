import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import skimage.util.noise as noise
import scipy.ndimage as ndi
from scipy.signal import wiener

img = io.imread('5.3.01.tiff')
io.imshow(img)
io.show()

# adding gaussian noise
g = noise.random_noise(img, mode='gaussian')
io.imshow(g, cmap='gray')
io.show()

# apply average filter
avg = ndi.uniform_filter(g, size=5)
io.imshow(avg, cmap='gray')
io.show()

# apply image adaptive filter
adaptive = wiener(g, [6, 6])
io.imshow(adaptive, cmap='gray')
io.show()
