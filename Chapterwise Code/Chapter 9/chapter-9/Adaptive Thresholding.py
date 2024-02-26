import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters 

img1 = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.3.01.tiff').astype(float)

# Get image dimensions
r, c = img1.shape

# Create the x, y grid
x, y = np.mgrid[0:r, 0:c].astype(float)

# Calculate the adaptive thresholding value
p2 = 255.0 - img1 + y / 2

# Display the original image
io.imshow(p2)
io.show()

# Apply thresholding using Otsu's method
t = filters.threshold_otsu(p2)

# Display the Otsu's thresholded image
io.imshow(p2 > t)
io.show()

starts = range(0, c - 1, 162)
ends = range(162, c + 1, 162)
z = np.zeros((r, c))
for i in range(6):
    temp = p2[:, starts[i]:ends[i]]
    z[:, starts[i]:ends[i]] = (temp > filters.threshold_otsu(temp)) * 1.0

# Display the adaptive thresholded image
io.imshow(z)
io.show()
