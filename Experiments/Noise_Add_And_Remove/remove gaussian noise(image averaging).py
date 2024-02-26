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
# it generates a new noisy version of the image (10 times)
x, y = img.shape
t = np.zeros((x, y, 10))
for i in range(10):
    t[:, :, i] = noise.random_noise(img, 'gaussian')

# apply image averaging filtering
ta = np.mean(t, axis=2)  # calculates the mean along the 3rd axis (axis=2) of the 10 noisy versions
io.imshow(ta, cmap='gray')
io.show()

